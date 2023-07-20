"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any, List

from distributor.shared_messages import IconInfoData
from interactions.context import InteractionContext
from sims.sim import Sim
from thesims4tools.classes.interactions.common_immediate_super_interaction import CommonImmediateSuperInteraction
from thesims4tools.classes.testing.common_test_result import CommonTestResult
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo
from thesims4tools.notifications.common_basic_notification import CommonBasicNotification
from thesims4tools.utils.common_type_utils import CommonTypeUtils
from thesims4tools.utils.localization.common_localization_utils import CommonLocalizationUtils
from thesims4tools.utils.sims.common_sim_name_utils import CommonSimNameUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
from thesims4tools.utils.resources.common_situation_utils import CommonSituationUtils
from thesims4tools.utils.sims.common_sim_situation_utils import CommonSimSituationUtils


class S4CLDebugShowRunningSituationsInteraction(CommonImmediateSuperInteraction):
    """S4CLDebugShowRunningSituationsInteraction(*_, **__)

    Show the currently running Situations of a Sim.
    """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 'ts4t_debug_show_running_situations'

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        if interaction_target is None or not CommonTypeUtils.is_sim_or_sim_info(interaction_target):
            cls.get_log().debug('Failed, Target is not a Sim.')
            return CommonTestResult.NONE
        cls.get_log().debug('Success, can show active Buffs.')
        return CommonTestResult.TRUE

    # noinspection PyMissingOrEmptyDocstring
    def on_started(self, interaction_sim: Sim, interaction_target: Sim) -> bool:
        target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
        target_sim_name = CommonSimNameUtils.get_full_name(target_sim_info)
        situation_strings: List[str] = list()
        for situation in CommonSimSituationUtils.get_situations(target_sim_info):
            from situations.situation import Situation
            situation: Situation = situation
            situation_name = CommonSituationUtils.get_situation_name(situation)
            situation_id = CommonSituationUtils.get_situation_id(situation)
            current_job = situation.get_current_job_for_sim(interaction_target)
            # noinspection PyBroadException
            try:
                job_name = current_job.__name__ or 'No Job'
            except:
                job_name = 'No Job'
            current_role = situation.get_current_role_state_for_sim(interaction_target)
            # noinspection PyBroadException
            try:
                role_name = current_role.__name__ or 'No Role'
            except:
                role_name = 'No Role'
            situation_strings.append('S:{} ({})\n  Job: {}\n  Role: {}'.format(situation_name, situation_id, job_name, role_name))

        situation_strings = sorted(situation_strings, key=lambda x: x)
        sim_situations = '\n\n'.join(situation_strings)
        text = ''
        text += 'Running Situations:\n{}'.format(sim_situations)
        self.log.enable()
        sim_buffs_for_log = '\n\n'.join(situation_strings)
        for_log_text = 'Running Situations:\n{}\n\n'.format(sim_buffs_for_log)
        self.log.debug(f'{target_sim_name} ({CommonSimUtils.get_sim_id(target_sim_info)}): {for_log_text}')
        self.log.disable()
        CommonBasicNotification(
            CommonLocalizationUtils.create_localized_string('{} Running Situations ({})'.format(target_sim_name, CommonSimUtils.get_sim_id(target_sim_info))),
            CommonLocalizationUtils.create_localized_string(text)
        ).show(
            icon=IconInfoData(obj_instance=interaction_target)
        )
        return True
