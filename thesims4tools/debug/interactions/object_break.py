"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any
from interactions.context import InteractionContext
from objects.game_object import GameObject
from sims.sim import Sim
from thesims4tools.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from thesims4tools.classes.testing.common_test_result import CommonTestResult
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_type_utils import CommonTypeUtils
from thesims4tools.utils.objects.common_object_state_utils import CommonObjectStateUtils


class S4CLDebugObjectBreakInteraction(CommonImmediateSuperInteraction):
    """S4CLDebugObjectBreakInteraction(*_, **__)

    Set the target Object to a broken state.
    """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 'ts4t_debug_break_object'

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        if interaction_target is None or CommonTypeUtils.is_sim_or_sim_info(interaction_target):
            cls.get_log().debug('Failed, Target is None.')
            return CommonTestResult.NONE
        interaction_target: GameObject = interaction_target
        if CommonObjectStateUtils.is_broken(interaction_target):
            cls.get_log().debug('Failed, the Object is already broken.')
            return CommonTestResult.NONE
        cls.get_log().debug('Success, can break object.')
        return CommonTestResult.TRUE

    # noinspection PyMissingOrEmptyDocstring
    def on_started(self, interaction_sim: Sim, interaction_target: GameObject) -> bool:
        return CommonObjectStateUtils.break_object(interaction_target)
