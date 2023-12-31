"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any, Tuple, Union

from buffs.buff import Buff
from interactions.utils.death import DeathTracker, DeathType
from objects.components.buff_component import BuffComponent
from objects.game_object import GameObject
from objects.script_object import ScriptObject
from sims.aging.aging_mixin import AgingMixin
from sims.occult.occult_enums import OccultType
from sims.occult.occult_tracker import OccultTracker
from sims.outfits.outfit_enums import OutfitCategory
from sims.sim import Sim
from sims.sim_info import SimInfo
from sims.sim_info_types import Age
from sims.sim_spawner import SimSpawner
from thesims4tools.enums.common_age import CommonAge
from thesims4tools.enums.common_death_types import CommonDeathType
from thesims4tools.enums.common_gender import CommonGender
from thesims4tools.events.event_handling.common_event_registry import CommonEventRegistry
from thesims4tools.events.sim.events.sim_added_occult_type import TS4TSimAddedOccultTypeEvent
from thesims4tools.events.sim.events.sim_after_set_current_outfit import TS4TSimAfterSetCurrentOutfitEvent
from thesims4tools.events.sim.events.sim_buff_added import TS4TSimBuffAddedEvent
from thesims4tools.events.sim.events.sim_buff_removed import TS4TSimBuffRemovedEvent
from thesims4tools.events.sim.events.sim_changed_age import TS4TSimChangedAgeEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_body_frame import TS4TSimChangedGenderOptionsBodyFrameEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_breasts import \
    TS4TSimChangedGenderOptionsBreastsEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_can_impregnate import \
    TS4TSimChangedGenderOptionsCanImpregnateEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_can_reproduce import \
    TS4TSimChangedGenderOptionsCanReproduceEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_clothing_preference import TS4TSimChangedGenderOptionsClothingPreferenceEvent
from thesims4tools.events.sim.events.sim_changed_gender import TS4TSimChangedGenderEvent
from thesims4tools.events.sim.events.sim_changed_occult_type import TS4TSimChangedOccultTypeEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_can_be_impregnated import TS4TSimChangedGenderOptionsCanBeImpregnatedEvent
from thesims4tools.events.sim.events.sim_changed_gender_options_toilet_usage import TS4TSimChangedGenderOptionsToiletUsageEvent
from thesims4tools.events.sim.events.sim_changing_occult_type import TS4TSimChangingOccultTypeEvent
from thesims4tools.events.sim.events.sim_died import TS4TSimDiedEvent
from thesims4tools.events.sim.events.sim_pre_despawned import TS4TSimPreDespawnedEvent
from thesims4tools.events.sim.events.sim_initialized import TS4TSimInitializedEvent
from thesims4tools.events.sim.events.sim_loaded import TS4TSimLoadedEvent
from thesims4tools.events.sim.events.game_object_added_to_sim_inventory import TS4TGameObjectAddedToSimInventoryEvent
from thesims4tools.events.sim.events.game_object_pre_removed_from_sim_inventory import TS4TGameObjectPreRemovedFromSimInventoryEvent
from thesims4tools.events.sim.events.sim_removed_occult_type import TS4TSimRemovedOccultTypeEvent
from thesims4tools.events.sim.events.sim_revived import TS4TSimRevivedEvent
from thesims4tools.events.sim.events.sim_set_current_outfit import TS4TSimSetCurrentOutfitEvent
from thesims4tools.events.sim.events.sim_skill_leveled_up import TS4TSimSkillLeveledUpEvent
from thesims4tools.events.sim.events.sim_spawned import TS4TSimSpawnedEvent
from thesims4tools.events.sim.events.sim_trait_added import TS4TSimTraitAddedEvent
from thesims4tools.events.sim.events.sim_trait_removed import TS4TSimTraitRemovedEvent
from thesims4tools.modinfo import ModInfo
from thesims4tools.services.common_service import CommonService
from thesims4tools.utils.cas.common_outfit_utils import CommonOutfitUtils
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
from statistics.skill import Skill
from traits.trait_tracker import TraitTracker
from traits.traits import Trait


class CommonSimEventDispatcherService(CommonService):
    """A service that dispatches Sim events (Init, Spawn, Add Occult, Remove Occult, Change Gender, etc.).

    .. warning:: Do not use this service directly to listen for events!\
        Use the :class:`.CommonEventRegistry` to listen for dispatched events.

    """

    def _on_sim_change_gender(self, sim_info: SimInfo) -> bool:
        from thesims4tools.utils.sims.common_gender_utils import CommonGenderUtils
        new_gender = CommonGender.get_gender(sim_info)
        if CommonGenderUtils.is_male_gender(new_gender):
            # If they are now Male, it means they used to be Female.
            old_gender = CommonGender.FEMALE
        else:
            # If they are now Female, it means they used to be Male.
            old_gender = CommonGender.MALE
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderEvent(sim_info, old_gender, new_gender))

    def _on_sim_change_gender_options_breasts(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsBreastsEvent(sim_info))

    def _on_sim_change_gender_options_toilet_usage(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsToiletUsageEvent(sim_info))

    def _on_sim_change_gender_options_body_frame(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsBodyFrameEvent(sim_info))

    def _on_sim_change_gender_options_clothing_preference(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsClothingPreferenceEvent(sim_info))

    def _on_sim_change_gender_options_can_impregnate(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsCanImpregnateEvent(sim_info))

    def _on_sim_change_gender_options_can_be_impregnated(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsCanBeImpregnatedEvent(sim_info))

    def _on_sim_change_gender_options_can_reproduce(self, sim_info: SimInfo) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimChangedGenderOptionsCanReproduceEvent(sim_info))

    def _on_sim_init(self, sim_info: SimInfo, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimInitializedEvent(sim_info))

    def _on_sim_load(self, sim_info: SimInfo, *_, **__) -> bool:
        from thesims4tools.events.zone_spin.common_zone_spin_event_dispatcher import CommonZoneSpinEventDispatcher
        if CommonZoneSpinEventDispatcher.get().game_loading:
            return False
        return CommonEventRegistry.get().dispatch(TS4TSimLoadedEvent(sim_info))

    def _on_sim_spawned(self, sim_info: SimInfo, *_, **__) -> bool:
        from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
        return CommonEventRegistry.get().dispatch(TS4TSimSpawnedEvent(CommonSimUtils.get_sim_info(sim_info)))

    def _on_sim_died(self, sim_info: SimInfo, death_type: CommonDeathType, is_off_lot_death: bool, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimDiedEvent(sim_info, death_type, is_off_lot_death))

    def _on_sim_revived(self, sim_info: SimInfo, previous_death_type: CommonDeathType, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimRevivedEvent(sim_info, previous_death_type))

    def _pre_sim_despawned(self, sim_info: SimInfo, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TSimPreDespawnedEvent(sim_info))

    def _on_sim_change_age(self, sim_info: SimInfo, new_age: Age, current_age: Age) -> bool:
        from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
        return CommonEventRegistry.get().dispatch(TS4TSimChangedAgeEvent(CommonSimUtils.get_sim_info(sim_info), CommonAge.convert_from_vanilla(current_age), CommonAge.convert_from_vanilla(new_age)))

    def _on_sim_add_occult_type(self, occult_tracker: OccultTracker, occult_type: OccultType) -> bool:
        sim_info = occult_tracker._sim_info
        return CommonEventRegistry.get().dispatch(TS4TSimAddedOccultTypeEvent(sim_info, occult_type, occult_tracker))

    def _on_sim_changing_occult_type(self, occult_tracker: OccultTracker, occult_type: OccultType, *_, **__) -> bool:
        sim_info = occult_tracker._sim_info
        return CommonEventRegistry.get().dispatch(TS4TSimChangingOccultTypeEvent(sim_info, occult_type, occult_tracker))

    def _on_sim_changed_occult_type(self, occult_tracker: OccultTracker, occult_type: OccultType, *_, **__) -> bool:
        sim_info = occult_tracker._sim_info
        return CommonEventRegistry.get().dispatch(TS4TSimChangedOccultTypeEvent(sim_info, occult_type, occult_tracker))

    def _on_sim_remove_occult_type(self, occult_tracker: OccultTracker, occult_type: OccultType) -> bool:
        sim_info = occult_tracker._sim_info
        return CommonEventRegistry.get().dispatch(TS4TSimRemovedOccultTypeEvent(sim_info, occult_type, occult_tracker))

    def _on_sim_trait_added(self, trait_tracker: TraitTracker, trait: Trait, *_, **__) -> None:
        sim_info = trait_tracker.get_sim_info_from_provider()
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TSimTraitAddedEvent(sim_info, trait, trait_tracker))

    def _on_sim_trait_removed(self, trait_tracker: TraitTracker, trait: Trait, *_, **__) -> None:
        sim_info = trait_tracker.get_sim_info_from_provider()
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TSimTraitRemovedEvent(sim_info, trait, trait_tracker))

    def _on_sim_buff_added(self, buff: Buff, sim_id: int) -> None:
        sim_info = CommonSimUtils.get_sim_info(sim_id)
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TSimBuffAddedEvent(sim_info, buff))

    def _on_sim_buff_removed(self, buff: Buff, sim_id: int) -> None:
        sim_info = CommonSimUtils.get_sim_info(sim_id)
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TSimBuffRemovedEvent(sim_info, buff))

    def _on_sim_set_current_outfit(self, sim_info: SimInfo, outfit_category_and_index: Tuple[OutfitCategory, int]) -> None:
        from thesims4tools.utils.cas.common_outfit_utils import CommonOutfitUtils
        CommonEventRegistry.get().dispatch(TS4TSimSetCurrentOutfitEvent(sim_info, CommonOutfitUtils.get_current_outfit(sim_info), outfit_category_and_index))

    def _after_sim_set_current_outfit(self, sim_info: SimInfo, previous_outfit_category_and_index: Tuple[OutfitCategory, int], outfit_category_and_index: Tuple[OutfitCategory, int]) -> None:
        CommonEventRegistry.get().dispatch(TS4TSimAfterSetCurrentOutfitEvent(sim_info, previous_outfit_category_and_index, outfit_category_and_index))

    def _on_skill_leveled_up(self, skill: Skill, old_skill_level: int, new_skill_level: int) -> None:
        if skill.tracker is None or skill.tracker._owner is None:
            return
        sim_info = CommonSimUtils.get_sim_info(skill.tracker._owner)
        CommonEventRegistry.get().dispatch(TS4TSimSkillLeveledUpEvent(sim_info, skill, old_skill_level, new_skill_level))

    def _on_object_added_to_sim_inventory(self, sim: Sim, added_game_object: GameObject) -> None:
        sim_info = CommonSimUtils.get_sim_info(sim)
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TGameObjectAddedToSimInventoryEvent(sim_info, added_game_object))

    def _on_object_removed_from_sim_inventory(self, sim: Sim, removed_game_object: GameObject) -> None:
        sim_info = CommonSimUtils.get_sim_info(sim)
        if sim_info is None:
            return
        CommonEventRegistry.get().dispatch(TS4TGameObjectPreRemovedFromSimInventoryEvent(sim_info, removed_game_object))


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfo, SimInfo.__init__.__name__, handle_exceptions=False)
def _common_on_sim_init(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_init(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfo, SimInfo.load_sim_info.__name__, handle_exceptions=False)
def _common_on_sim_load(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_load(self, *args, **kwargs)
    return result


# noinspection PyUnusedLocal
@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimSpawner, SimSpawner.spawn_sim.__name__, handle_exceptions=False)
def _common_on_sim_spawn(original, cls, *args, **kwargs) -> Any:
    result = original(*args, **kwargs)
    if result:
        CommonSimEventDispatcherService.get()._on_sim_spawned(*args, **kwargs)
    return result


# noinspection PyUnusedLocal
@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Sim, Sim.destroy.__name__, handle_exceptions=False)
def _common_on_sim_despawn(original, self, *args, **kwargs) -> Any:
    CommonSimEventDispatcherService.get()._pre_sim_despawned(CommonSimUtils.get_sim_info(self), *args, **kwargs)
    return original(self, *args, **kwargs)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), DeathTracker, DeathTracker.set_death_type.__name__)
def _common_on_sim_set_death_type(original, self, death_type: Union[DeathType, None], is_off_lot_death: bool = False, *_, **__) -> Any:
    previous_death_type = self._death_type
    original_result = original(self, death_type, is_off_lot_death=is_off_lot_death, *_, **__)
    if death_type is None and previous_death_type is None:
        return original_result

    sim_info = CommonSimUtils.get_sim_info(self._sim_info)
    if death_type is None:
        CommonSimEventDispatcherService.get()._on_sim_revived(sim_info, CommonDeathType.convert_from_vanilla(previous_death_type))
    else:
        if previous_death_type is None:
            CommonSimEventDispatcherService.get()._on_sim_died(sim_info, CommonDeathType.convert_from_vanilla(death_type), is_off_lot_death)
    return original_result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), DeathTracker, DeathTracker.clear_death_type.__name__)
def _common_on_sim_clear_death_type(original, self, *_, **__) -> Any:
    previous_death_type = self._death_type
    original_result = original(self, *_, **__)
    if previous_death_type is None:
        return original_result
    sim_info = CommonSimUtils.get_sim_info(self._sim_info)
    CommonSimEventDispatcherService.get()._on_sim_revived(sim_info, CommonDeathType.convert_from_vanilla(previous_death_type))
    return original_result


# noinspection PyUnusedLocal
@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Skill, Skill.on_skill_level_up.__name__, handle_exceptions=False)
def _common_on_sim_skill_level_up(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    if result:
        CommonSimEventDispatcherService.get()._on_skill_leveled_up(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), AgingMixin, AgingMixin.change_age.__name__, handle_exceptions=False)
def _common_on_sim_change_age(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_change_age(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), OccultTracker, OccultTracker.add_occult_type.__name__, handle_exceptions=False)
def _common_on_sim_add_occult_type(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_add_occult_type(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), OccultTracker, OccultTracker.switch_to_occult_type.__name__, handle_exceptions=False)
def _common_on_sim_change_occult_type(original, self, *args, **kwargs) -> Any:
    CommonSimEventDispatcherService.get()._on_sim_changing_occult_type(self, *args, **kwargs)
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_changed_occult_type(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), OccultTracker, OccultTracker.remove_occult_type.__name__, handle_exceptions=False)
def _common_on_sim_remove_occult_type(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_remove_occult_type(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfo, SimInfo.set_current_outfit.__name__, handle_exceptions=False)
def _common_on_sim_set_current_outfit(original, self, *args, **kwargs) -> Any:
    old_outfit_category_and_index = CommonOutfitUtils.get_current_outfit(self)
    CommonSimEventDispatcherService.get()._on_sim_set_current_outfit(self, *args, **kwargs)
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._after_sim_set_current_outfit(self, old_outfit_category_and_index, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), TraitTracker, TraitTracker._add_trait.__name__, handle_exceptions=False)
def _common_on_sim_trait_added(original, self: TraitTracker, *args, **kwargs):
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_trait_added(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), TraitTracker, TraitTracker._remove_trait.__name__, handle_exceptions=False)
def _common_on_sim_trait_removed(original, self: TraitTracker, *args, **kwargs):
    result = original(self, *args, **kwargs)
    CommonSimEventDispatcherService.get()._on_sim_trait_removed(self, *args, **kwargs)
    return result


@CommonEventRegistry.handle_events(ModInfo.get_identity())
def _common_register_buff_added_or_removed_on_sim_spawned(event_data: TS4TSimSpawnedEvent) -> bool:
    from thesims4tools.utils.sims.common_buff_utils import CommonBuffUtils
    buff_component: BuffComponent = CommonBuffUtils.get_buff_component(event_data.sim_info)
    if not buff_component:
        return False

    dispatcher_service = CommonSimEventDispatcherService()
    if dispatcher_service._on_sim_buff_added not in buff_component.on_buff_added:
        buff_component.on_buff_added.append(dispatcher_service._on_sim_buff_added)

    if dispatcher_service._on_sim_buff_removed not in buff_component.on_buff_removed:
        buff_component.on_buff_removed.append(dispatcher_service._on_sim_buff_removed)
    return True


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Sim, Sim.on_object_added_to_inventory.__name__, handle_exceptions=False)
def _common_on_object_added_to_sim_inventory(original, self: Sim, obj: ScriptObject, *args, **kwargs):
    result = original(self, obj, *args, **kwargs)
    if isinstance(obj, GameObject):
        CommonSimEventDispatcherService.get()._on_object_added_to_sim_inventory(self, obj)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Sim, Sim.on_object_removed_from_inventory.__name__, handle_exceptions=False)
def _common_on_object_removed_from_sim_inventory(original, self: Sim, obj: ScriptObject, *args, **kwargs):
    if isinstance(obj, GameObject):
        CommonSimEventDispatcherService.get()._on_object_removed_from_sim_inventory(self, obj)
    result = original(self, obj, *args, **kwargs)
    return result
