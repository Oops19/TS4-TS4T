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


class TS4TDebugShowRunningAndQueuedInteractionsInteraction(CommonImmediateSuperInteraction):
    """TS4TDebugShowRunningAndQueuedInteractionsInteraction(*_, **__)

    Show the currently running and queued interactions of a Sim.
    """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 'ts4t_debug_show_running_and_queued_interactions'

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def on_test(cls, interaction_sim: Sim, interaction_target: Any, interaction_context: InteractionContext, **kwargs) -> CommonTestResult:
        if interaction_target is None or not CommonTypeUtils.is_sim_or_sim_info(interaction_target):
            cls.get_log().debug('Failed, Target is not a Sim.')
            return CommonTestResult.NONE
        cls.get_log().debug('Success, can show running and queued interactions.')
        return CommonTestResult.TRUE

    # noinspection PyMissingOrEmptyDocstring
    def on_started(self, interaction_sim: Sim, interaction_target: Sim) -> bool:
        target_sim_info = CommonSimUtils.get_sim_info(interaction_target)
        target_sim_name = CommonSimNameUtils.get_full_name(target_sim_info)
        from thesims4tools.utils.sims.common_sim_interaction_utils import CommonSimInteractionUtils
        from thesims4tools.utils.resources.common_interaction_utils import CommonInteractionUtils
        running_interaction_strings: List[str] = list()
        for interaction in CommonSimInteractionUtils.get_running_interactions_gen(target_sim_info):
            interaction_name = CommonInteractionUtils.get_interaction_short_name(interaction)
            interaction_id = CommonInteractionUtils.get_interaction_id(interaction)
            running_interaction_strings.append('{} ({})'.format(interaction_name, interaction_id))
        running_interaction_strings = sorted(running_interaction_strings, key=lambda x: x)
        running_interaction_names = ', '.join(running_interaction_strings)

        queued_interaction_strings: List[str] = list()
        for interaction in CommonSimInteractionUtils.get_queued_interactions_gen(target_sim_info):
            interaction_name = CommonInteractionUtils.get_interaction_short_name(interaction)
            interaction_id = CommonInteractionUtils.get_interaction_id(interaction)
            queued_interaction_strings.append('{} ({})'.format(interaction_name, interaction_id))
        queued_interaction_strings = sorted(queued_interaction_strings, key=lambda x: x)
        queued_interaction_names = ', '.join(queued_interaction_strings)
        text = ''
        text += 'Running Interactions:\n{}\n\n'.format(running_interaction_names)
        text += 'Queued Interactions:\n{}\n\n'.format(queued_interaction_names)
        self.log.enable()
        sim_running_interactions_for_log = ',\n'.join(running_interaction_strings)
        for_log_text = 'Running Interactions:\n{}\n\n'.format(sim_running_interactions_for_log)
        sim_queued_interactions_for_log = ',\n'.join(queued_interaction_strings)
        for_log_text += 'Queued Interactions:\n{}\n\n'.format(sim_queued_interactions_for_log)
        self.log.debug(f'{target_sim_name} ({CommonSimUtils.get_sim_id(target_sim_info)}): {for_log_text}')
        self.log.disable()
        CommonBasicNotification(
            CommonLocalizationUtils.create_localized_string('{} Running and Queued Interactions ({})'.format(target_sim_name, CommonSimUtils.get_sim_id(target_sim_info))),
            CommonLocalizationUtils.create_localized_string(text)
        ).show(
            icon=IconInfoData(obj_instance=interaction_target)
        )
        return True
