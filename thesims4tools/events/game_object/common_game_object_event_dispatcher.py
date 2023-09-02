"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any

from objects.game_object import GameObject
from objects.script_object import ScriptObject
from thesims4tools.events.event_handling.common_event_registry import CommonEventRegistry
from thesims4tools.events.game_object.events.game_object_added_to_inventory import TS4TGameObjectAddedToInventoryEvent
from thesims4tools.events.game_object.events.game_object_pre_despawned import TS4TGameObjectPreDespawnedEvent
from thesims4tools.events.game_object.events.game_object_pre_deleted import TS4TGameObjectPreDeletedEvent
from thesims4tools.events.game_object.events.game_object_initialized import TS4TGameObjectInitializedEvent
from thesims4tools.events.game_object.events.game_object_loaded import TS4TGameObjectLoadedEvent
from thesims4tools.events.game_object.events.game_object_pre_removed_from_inventory import \
    TS4TGameObjectPreRemovedFromInventoryEvent
from thesims4tools.events.game_object.events.game_object_spawned import TS4TGameObjectSpawnedEvent
from thesims4tools.events.game_object.events.game_object_added_to_game_object_inventory import \
    TS4TGameObjectAddedToGameObjectInventoryEvent
from thesims4tools.events.game_object.events.game_object_pre_removed_from_game_object_inventory import \
    TS4TGameObjectPreRemovedFromGameObjectInventoryEvent
from thesims4tools.modinfo import ModInfo
from thesims4tools.services.common_service import CommonService
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils


class CommonGameObjectEventDispatcherService(CommonService):
    """A service that dispatches Game Object events (Init, Spawn, Destroy, etc.).

    .. warning:: Do not use this service directly to listen for events!\
        Use the :class:`.CommonEventRegistry` to listen for dispatched events.

    """

    def _on_game_object_init(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectInitializedEvent(game_object))

    def _on_game_object_load(self, game_object: GameObject, *_, **__) -> bool:
        from thesims4tools.events.zone_spin.common_zone_spin_event_dispatcher import CommonZoneSpinEventDispatcher
        if CommonZoneSpinEventDispatcher.get().game_loading:
            return False
        return CommonEventRegistry.get().dispatch(TS4TGameObjectLoadedEvent(game_object))

    def _on_game_object_spawned(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectSpawnedEvent(game_object))

    def _on_game_object_despawned(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectPreDespawnedEvent(game_object))

    def _on_game_object_destroy(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectPreDeletedEvent(game_object))

    def _on_game_object_added_to_inventory(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectAddedToInventoryEvent(game_object))

    def _on_game_object_pre_removed_from_inventory(self, game_object: GameObject, *_, **__) -> bool:
        return CommonEventRegistry.get().dispatch(TS4TGameObjectPreRemovedFromInventoryEvent(game_object))

    def _on_game_object_added_to_game_object_inventory(self, game_object: GameObject, added_object: GameObject) -> None:
        CommonEventRegistry.get().dispatch(TS4TGameObjectAddedToGameObjectInventoryEvent(game_object, added_object))

    def _on_game_object_pre_removed_from_game_object_inventory(self, game_object: GameObject, removed_object: GameObject) -> None:
        CommonEventRegistry.get().dispatch(TS4TGameObjectPreRemovedFromGameObjectInventoryEvent(game_object, removed_object))


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.__init__.__name__, handle_exceptions=False)
def _common_on_game_object_init(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonGameObjectEventDispatcherService.get()._on_game_object_init(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.load_object.__name__, handle_exceptions=False)
def _common_on_game_object_load(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonGameObjectEventDispatcherService.get()._on_game_object_load(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.destroy.__name__, handle_exceptions=False)
def _common_on_game_object_load(original, self, *args, **kwargs) -> Any:
    CommonGameObjectEventDispatcherService.get()._on_game_object_destroy(self, *args, **kwargs)
    result = original(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_add.__name__)
def _common_on_game_object_added(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonGameObjectEventDispatcherService.get()._on_game_object_spawned(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_remove.__name__)
def _common_on_game_object_removed(original, self, *args, **kwargs) -> Any:
    CommonGameObjectEventDispatcherService.get()._on_game_object_despawned(self, *args, **kwargs)
    result = original(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_added_to_inventory.__name__)
def _common_on_game_object_added_to_inventory(original, self, *args, **kwargs) -> Any:
    result = original(self, *args, **kwargs)
    CommonGameObjectEventDispatcherService.get()._on_game_object_added_to_inventory(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_removed_from_inventory.__name__)
def _common_on_game_object_removed_from_inventory(original, self, *args, **kwargs) -> Any:
    CommonGameObjectEventDispatcherService.get()._on_game_object_pre_removed_from_inventory(self, *args, **kwargs)
    result = original(self, *args, **kwargs)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_object_added_to_inventory.__name__, handle_exceptions=False)
def _common_on_game_object_added_to_game_object_inventory(original, self: GameObject, obj: ScriptObject, *args, **kwargs):
    result = original(self, obj, *args, **kwargs)
    if isinstance(obj, GameObject):
        CommonGameObjectEventDispatcherService.get()._on_game_object_added_to_game_object_inventory(self, obj)
    return result


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), GameObject, GameObject.on_object_removed_from_inventory.__name__, handle_exceptions=False)
def _common_on_game_object_removed_from_game_object_inventory(original, self: GameObject, obj: ScriptObject, *args, **kwargs):
    if isinstance(obj, GameObject):
        CommonGameObjectEventDispatcherService.get()._on_game_object_pre_removed_from_game_object_inventory(self, obj)
    result = original(self, obj, *args, **kwargs)
    return result
