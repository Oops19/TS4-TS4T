"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Union, Any, Iterator, Callable
from protocolbuffers.Localization_pb2 import LocalizedString
from sims.sim_info import SimInfo
from thesims4tools.dialogs.option_dialogs.common_choose_sim_option_dialog import CommonChooseSimOptionDialog
from thesims4tools.dialogs.option_dialogs.options.sims.common_dialog_sim_option import CommonDialogSimOption
from thesims4tools.dialogs.option_dialogs.options.sims.common_dialog_sim_option_context import \
    CommonDialogSimOptionContext
from thesims4tools.enums.strings_enum import CommonStringId
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo
from thesims4tools.services.commands.common_console_command import CommonConsoleCommand
from thesims4tools.services.commands.common_console_command_output import CommonConsoleCommandOutput
from thesims4tools.utils.common_function_utils import CommonFunctionUtils
from thesims4tools.utils.localization.common_localization_utils import CommonLocalizationUtils
from thesims4tools.utils.localization.common_localized_string_colors import CommonLocalizedStringColor
from thesims4tools.utils.sims.common_age_utils import CommonAgeUtils
from thesims4tools.utils.sims.common_sim_name_utils import CommonSimNameUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils


class CommonPremadeChooseSimOptionDialog(CommonChooseSimOptionDialog):
    """CommonPremadeChooseSimOptionDialog(\
        title_identifier,\
        description_identifier,\
        title_tokens=(),\
        description_tokens=(),\
        on_close=CommonFunctionUtils.noop,\
        mod_identity=None,\
        include_sim_callback=None,\
        instanced_sims_only=True,\
        on_sim_chosen=CommonFunctionUtils.noop\
    )

    A premade dialog that will display a list of Sims based on a filter and will prompt the player to choose a single Sim.

    .. note:: To see an example dialog, run the command :class:`ts4t_testing.show_premade_choose_sim_option_dialog` in the in-game console.

    :Example usage:

    .. highlight:: python
    .. code-block:: python

        def _on_chosen(_sim_info: SimInfo):
            pass

        # LocalizedStrings within other LocalizedStrings
        title_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
                text_color=CommonLocalizedStringColor.GREEN
            ),
        )
        description_tokens = (
            CommonLocalizationUtils.create_localized_string(
                CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME,
                tokens=(CommonSimUtils.get_active_sim_info(),),
                text_color=CommonLocalizedStringColor.BLUE
            ),
        )

        # Create the dialog that will only show adult Sims in the current area.
        option_dialog = CommonPremadeChooseSimOptionDialog(
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            mod_identity=ModInfo.get_identity(),
            include_sim_callback=CommonAgeUtils.is_adult,
            instanced_sims_only=True,
            on_sim_chosen=_on_chosen
        )

        option_dialog.show(
            sim_info=CommonSimUtils.get_active_sim_info(),
            column_count=4
        )

    :param title_identifier: A decimal identifier of the title text.
    :type title_identifier: Union[int, str, LocalizedString, CommonStringId]
    :param description_identifier: A decimal identifier of the description text.
    :type description_identifier: Union[int, str, LocalizedString, CommonStringId]
    :param title_tokens: An iterator of Tokens to format into the title.
    :type title_tokens: Iterator[Any], optional
    :param description_tokens: An iterator of Tokens to format into the description.
    :type description_tokens: Iterator[Any], optional
    :param on_close: A callback invoked upon the dialog closing.
    :type on_close: Callable[[], None], optional
    :param mod_identity: The identity of the mod creating the dialog. See :class:`.CommonModIdentity` for more information.
    :type mod_identity: CommonModIdentity, optional
    :param include_sim_callback: If the result of this callback is True, the sim will be included in the results. If set to None, All sims will be included.
    :type include_sim_callback: Callable[[SimInfo], bool], optional
    :param instanced_sims_only: If True, only Sims that are currently spawned will be shown. If False, all Sims will be shown. Default is True.
    :type instanced_sims_only: bool, optional
    :param on_sim_chosen: Called upon a Sim being chosen. Default is :func:`~CommonFunctionUtils.noop`.
    :type on_sim_chosen: Callable[[SimInfo], Any], optional
    """
    def __init__(
        self,
        title_identifier: Union[int, str, LocalizedString, CommonStringId],
        description_identifier: Union[int, str, LocalizedString, CommonStringId],
        title_tokens: Iterator[Any]=(),
        description_tokens: Iterator[Any]=(),
        on_close: Callable[[], None]=CommonFunctionUtils.noop,
        mod_identity: CommonModIdentity=None,
        include_sim_callback: Callable[[SimInfo], bool]=None,
        instanced_sims_only: bool=True,
        on_sim_chosen: Callable[[SimInfo], Any]=CommonFunctionUtils.noop
    ):
        super().__init__(
            title_identifier,
            description_identifier,
            title_tokens=title_tokens,
            description_tokens=description_tokens,
            on_close=on_close,
            mod_identity=mod_identity
        )

        if instanced_sims_only:
            _sim_info_list = CommonSimUtils.get_instanced_sim_info_for_all_sims_generator(include_sim_callback=include_sim_callback)
        else:
            _sim_info_list = CommonSimUtils.get_sim_info_for_all_sims_generator(include_sim_callback=include_sim_callback)

        for _sim_info in _sim_info_list:
            self.add_option(
                CommonDialogSimOption(
                    _sim_info,
                    CommonDialogSimOptionContext(),
                    on_chosen=on_sim_chosen
                )
            )

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 'ts4t_premade_choose_sim_option_dialog'


@CommonConsoleCommand(
    ModInfo.get_identity(),
    'ts4t_testing.show_premade_choose_sim_option_dialog',
    'Show an example of CommonPremadeChooseSimOptionDialog.'
)
def _common_testing_show_premade_choose_sim_option_dialog(output: CommonConsoleCommandOutput):
    output('Showing test premade choose sim option dialog.')

    def _on_chosen(_sim_info: SimInfo):
        output('Chose Sim with name \'{}\''.format(CommonSimNameUtils.get_full_name(_sim_info)))

    # LocalizedStrings within other LocalizedStrings
    title_tokens = (
        CommonLocalizationUtils.create_localized_string(
            CommonStringId.TESTING_SOME_TEXT_FOR_TESTING,
            text_color=CommonLocalizedStringColor.GREEN
        ),
    )
    description_tokens = (
        CommonLocalizationUtils.create_localized_string(
            CommonStringId.TESTING_TEST_TEXT_WITH_SIM_FIRST_AND_LAST_NAME,
            tokens=(CommonSimUtils.get_active_sim_info(),),
            text_color=CommonLocalizedStringColor.BLUE
        ),
    )

    # Create the dialog that will only show adult Sims in the current area.
    option_dialog = CommonPremadeChooseSimOptionDialog(
        CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
        CommonStringId.TESTING_TEST_TEXT_WITH_STRING_TOKEN,
        title_tokens=title_tokens,
        description_tokens=description_tokens,
        mod_identity=ModInfo.get_identity(),
        include_sim_callback=CommonAgeUtils.is_adult,
        instanced_sims_only=True,
        on_sim_chosen=_on_chosen
    )

    option_dialog.show(
        sim_info=CommonSimUtils.get_active_sim_info(),
        column_count=4
    )
    output('Done showing.')
