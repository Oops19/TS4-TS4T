"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Tuple

from objects.game_object import GameObject
from objects.script_object import ScriptObject
from sims.sim import Sim
from thesims4tools.enums.affordance_list_ids import CommonAffordanceListId
from thesims4tools.enums.enumtypes.common_int import CommonInt
from thesims4tools.enums.interactions_enum import CommonInteractionId
from thesims4tools.services.interactions.interaction_registration_service import CommonInteractionRegistry, \
    CommonInteractionType, CommonScriptObjectInteractionHandler, CommonInteractionHandler
from thesims4tools.services.resources.common_instance_manager_modification_registry import \
    CommonInstanceManagerModificationRegistry
from thesims4tools.services.resources.modification_handlers.common_add_interactions_to_affordance_lists_handler import \
    CommonAddInteractionsToAffordanceListsModificationHandler
from thesims4tools.utils.common_type_utils import CommonTypeUtils
from thesims4tools.utils.objects.common_object_state_utils import CommonObjectStateUtils


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _TS4TObjectBrokennessDebugInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_OBJECT_BREAK,
            CommonInteractionId.TS4T_DEBUG_OBJECT_FIX
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        if not isinstance(script_object, GameObject):
            return False
        script_object: GameObject = script_object
        return CommonObjectStateUtils.can_become_broken(script_object)


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _TS4TObjectDirtinessDebugInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_OBJECT_MAKE_DIRTY,
            CommonInteractionId.TS4T_DEBUG_OBJECT_MAKE_CLEAN
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        if not isinstance(script_object, GameObject):
            return False
        script_object: GameObject = script_object
        return CommonObjectStateUtils.can_become_dirty(script_object)


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_SCRIPT_OBJECT_LOAD)
class _TS4TDebugEverywhereObjectInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS,
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_GAME_TAGS,
            CommonInteractionId.TS4T_DEBUG_CHANGE_OBJECT_STATES,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return not CommonTypeUtils.is_sim_or_sim_info(script_object)


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_TERRAIN_LOAD)
class _TS4TDebugEverywhereTerrainInteractionHandler(CommonInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS,
        )
        return result


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ON_OCEAN_LOAD)
class _TS4TDebugEverywhereOceanInteractionHandler(CommonInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS,
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_GAME_TAGS,
            CommonInteractionId.TS4T_DEBUG_CHANGE_OBJECT_STATES,
        )
        return result


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ADD_TO_SIM_RELATIONSHIP_PANEL_INTERACTIONS)
class _TS4TDebugSimRelationshipPanelInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: Sim, *args, **kwargs) -> bool:
        return CommonTypeUtils.is_sim_or_sim_info(script_object)


@CommonInteractionRegistry.register_interaction_handler(CommonInteractionType.ADD_TO_SIM_PHONE_INTERACTIONS)
class _TS4TDebugSimPhoneInteractionHandler(CommonScriptObjectInteractionHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interactions_to_add(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS_PHONE,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    def should_add(self, script_object: ScriptObject, *args, **kwargs) -> bool:
        return CommonTypeUtils.is_sim_or_sim_info(script_object)


@CommonInstanceManagerModificationRegistry.register_modification_handler()
class _TS4TAddDebugInteractionsToAffordanceWhitelist(CommonAddInteractionsToAffordanceListsModificationHandler):
    # noinspection PyMissingOrEmptyDocstring
    @property
    def interaction_ids(self) -> Tuple[CommonInt]:
        result: Tuple[CommonInt, ...] = (
            CommonInteractionId.TS4T_DEBUG_SHOW_RUNNING_AND_QUEUED_INTERACTIONS,
            CommonInteractionId.TS4T_DEBUG_SHOW_ACTIVE_BUFFS,
            CommonInteractionId.TS4T_DEBUG_SHOW_TRAITS,
            CommonInteractionId.TS4T_DEBUG_SHOW_RUNNING_SITUATIONS,
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS,
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_INTERACTIONS_PHONE,
            CommonInteractionId.TS4T_DEBUG_INDUCE_LABOR,
            CommonInteractionId.TS4T_DEBUG_OBJECT_BREAK,
            CommonInteractionId.TS4T_DEBUG_OBJECT_FIX,
            CommonInteractionId.TS4T_DEBUG_OBJECT_MAKE_DIRTY,
            CommonInteractionId.TS4T_DEBUG_OBJECT_MAKE_CLEAN,
            CommonInteractionId.TS4T_DEBUG_LOG_ALL_GAME_TAGS,
            CommonInteractionId.TS4T_DEBUG_CHANGE_OBJECT_STATES,
        )
        return result

    # noinspection PyMissingOrEmptyDocstring
    @property
    def affordance_list_ids(self) -> Tuple[int]:
        result: Tuple[int, ...] = (
            CommonAffordanceListId.DEBUG_AFFORDANCES,
        )
        return result
