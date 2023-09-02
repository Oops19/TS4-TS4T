"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from pprint import pformat

from broadcasters.broadcaster import Broadcaster
from thesims4tools.exceptions.common_exceptions_handler import CommonExceptionHandler
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils
from thesims4tools.utils.resources.common_interaction_utils import CommonInteractionUtils


# Some interactions cause an error in this function, this is here to catch those errors and provide more information about them.
@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Broadcaster, Broadcaster.apply_broadcaster_effect.__name__, handle_exceptions=False)
def _common_broadcaster_apply(original, self: Broadcaster, *_, **__) -> None:
    try:
        return original(self, *_, **__)
    except Exception as ex:
        if self.interaction is not None:
            interaction = self.interaction
            # noinspection PyTypeChecker
            CommonExceptionHandler.log_exception(None, 'Error occurred while running apply_broadcaster_effect for broadcaster {} for interaction {} with short name {} and display name {} (This exception is not caused by TS4T, but rather caught)'.format(pformat(self), pformat(interaction), CommonInteractionUtils.get_interaction_short_name(interaction), CommonInteractionUtils.get_interaction_display_name(interaction)), exception=ex)
        elif self.broadcasting_object is not None:
            broadcasting_object = self.broadcasting_object
            # noinspection PyTypeChecker
            CommonExceptionHandler.log_exception(None, 'Error occurred while running apply_broadcaster_effect for broadcaster {} from object {} (This exception is not caused by TS4T, but rather caught)'.format(pformat(self), pformat(broadcasting_object)), exception=ex)
        else:
            # noinspection PyTypeChecker
            CommonExceptionHandler.log_exception(None, 'Error occurred while running apply_broadcaster_effect for broadcaster {} (This exception is not caused by TS4T, but rather caught)'.format(pformat(self)), exception=ex)
    return None
