"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any

from interactions.context import InteractionContext
from sims.sim import Sim
from thesims4tools.classes.testing.common_test_result import CommonTestResult
from thesims4tools.enums.strings_enum import CommonStringId
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.sims.common_sim_name_utils import CommonSimNameUtils
from thesims4tools.utils.sims.common_sim_pregnancy_utils import CommonSimPregnancyUtils
from thesims4tools.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from thesims4tools.utils.localization.common_localization_utils import CommonLocalizationUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
from thesims4tools.utils.common_type_utils import CommonTypeUtils


class TS4TDebugInduceLaborInteraction(CommonImmediateSuperInteraction):
    """ Handle the interaction to Induce Labor. """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 'ts4t_debug_induce_labor'

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        if interaction_target is None or not CommonTypeUtils.is_sim_or_sim_info(interaction_target):
            cls.get_log().debug('Target is not a Sim.')
            return CommonTestResult.NONE
        target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
        if not CommonSimPregnancyUtils.can_be_impregnated(target_sim_info):
            cls.get_log().format_with_message('Sim cannot be impregnated and thus cannot be pregnant.', target_sim=target_sim_info)
            return CommonTestResult.NONE
        if not hasattr(target_sim_info, 'pregnancy_tracker'):
            cls.get_log().format_with_message('Target does not have a pregnancy tracker.', target_sim=target_sim_info)
            return CommonTestResult.NONE
        cls.get_log().format_with_message('Checking if Sim is pregnant.', target_sim=target_sim_info)
        if not CommonSimPregnancyUtils.is_pregnant(target_sim_info):
            cls.get_log().format_with_message('Sim is not pregnant.', sim=target_sim_info)
            return cls.create_test_result(False, reason='\'{}\' is not pregnant.'.format(CommonSimNameUtils.get_full_name(target_sim_info)), tooltip=CommonLocalizationUtils.create_localized_tooltip(CommonStringId.TS4T_SIM_IS_NOT_PREGNANT, tooltip_tokens=(target_sim_info, )))
        cls.get_log().debug('Success.')
        return CommonTestResult.TRUE

    # noinspection PyMissingOrEmptyDocstring
    def on_started(self, interaction_sim: Sim, interaction_target: Sim) -> bool:
        target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
        self.log.format_with_message('The baby wants out now! Labor induced in Sim.', target_sim=target_sim_info)
        CommonSimPregnancyUtils.induce_labor_in_sim(target_sim_info)
        return True
