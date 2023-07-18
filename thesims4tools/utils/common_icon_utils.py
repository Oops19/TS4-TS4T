"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any, Union
from sims4.resources import Types
from thesims4tools.enums.icons_enum import CommonIconId
from thesims4tools.utils.common_resource_utils import CommonResourceUtils


class CommonIconUtils:
    """Utilities for loading icons.

    """
    @staticmethod
    def load_arrow_right_icon() -> Any:
        """load_arrow_right_icon()

        Get the Resource Key for the ARROW_RIGHT_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_ARROW_RIGHT_ICON)

    @staticmethod
    def load_arrow_left_icon() -> Any:
        """load_arrow_left_icon()

        Get the Resource Key for the ARROW_LEFT_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_ARROW_LEFT_ICON)

    @staticmethod
    def load_arrow_navigate_into_icon() -> Any:
        """load_arrow_navigate_into_icon()

        Get the Resource Key for the ARROW_NAVIGATE_INTO_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_ARROW_NAVIGATE_INTO_ICON)

    @staticmethod
    def load_question_mark_icon() -> Any:
        """load_question_mark_icon()

        Get the Resource Key for the QUESTION_MARK_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_QUESTION_MARK_ICON)

    @staticmethod
    def load_checked_square_icon() -> Any:
        """load_checked_square_icon()

        Get the Resource Key for the CHECKED_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_CHECKED_SQUARE_ICON)

    @staticmethod
    def load_checked_circle_icon() -> Any:
        """load_checked_circle_icon()

        Get the Resource Key for the CHECKED_CIRCLE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_CHECKED_CIRCLE_ICON)

    @staticmethod
    def load_unchecked_square_icon() -> Any:
        """load_unchecked_square_icon()

        Get the Resource Key for the UNCHECKED_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_UNCHECKED_SQUARE_ICON)

    @staticmethod
    def load_x_icon() -> Any:
        """load_x_icon()

        Get the Resource Key for the X_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_X_ICON)

    @staticmethod
    def load_six_sided_dice_icon() -> Any:
        """load_six_sided_dice_icon()

        Get the Resource Key for the SIX_SIDED_DICE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_SIX_SIDED_DICE_ICON)

    @staticmethod
    def load_blank_square_icon() -> Any:
        """load_blank_square_icon()

        Get the Resource Key for the BLANK_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_BLANK_SQUARE_ICON)

    @staticmethod
    def load_text_prev_icon() -> Any:
        """load_text_prev_icon()

        Get the Resource Key for the TEXT_PREV_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_TEXT_PREV_SQUARE_ICON)

    @staticmethod
    def load_text_next_icon() -> Any:
        """load_text_next_icon()

        Get the Resource Key for the TEXT_NEXT_SQUARE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_TEXT_NEXT_SQUARE_ICON)

    @staticmethod
    def load_unfilled_circle_icon() -> Any:
        """load_unfilled_circle_icon()

        Get the Resource Key for the UNFILLED_CIRCLE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_UNFILLED_CIRCLE_ICON)

    @staticmethod
    def load_filled_circle_icon() -> Any:
        """load_filled_circle_icon()

        Get the Resource Key for the FILLED_CIRCLE_ICON.

        :return: An identifier for the icon.
        :rtype: Any
        """
        return CommonIconUtils._load_icon(CommonIconId.TS4T_FILLED_CIRCLE_ICON)
    
    @staticmethod
    def _load_icon(icon_id: Union[int, CommonIconId]) -> Any:
        return CommonResourceUtils.get_resource_key(Types.PNG, icon_id)
