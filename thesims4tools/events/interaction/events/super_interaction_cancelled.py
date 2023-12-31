"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any, Dict
from interactions.base.super_interaction import SuperInteraction
from interactions.interaction_finisher import FinishingType
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TSuperInteractionCancelledEvent(CommonEvent):
    """TS4TSuperInteractionCancelledEvent(interaction, finishing_type, cancel_reason_msg, **kwargs)

    An event that occurs upon a super interaction being cancelled.

    .. note:: This event fires BEFORE the super interaction is actually cancelled. Like a Pre-Cancel.

    :Example usage:

    .. highlight:: python
    .. code-block:: python

        from thesims4tools.events.event_handling.common_event_registry import CommonEventRegistry
        from thesims4tools.modinfo import ModInfo

        class ExampleEventListener:

            # In order to listen to an event, your function must match these criteria:
            # - The function is static (staticmethod).
            # - The first and only required argument has the name "event_data".
            # - The first and only required argument has the Type Hint for the event you are listening for.
            # - The argument passed to "handle_events" is the name or identity of your Mod.
            @staticmethod
            @CommonEventRegistry.handle_events(ModInfo.get_identity())
            def handle_event(event_data: TS4TSuperInteractionCancelledEvent) -> bool:
                # Return True from here to signify the event listener ran successfully. Return False or None here to signify the event listener failed to run successfully.
                return True

    :param interaction: The super interaction that is being cancelled.
    :type interaction: SuperInteraction
    :param finishing_type: The finishing type of the interaction.
    :type finishing_type: FinishingType
    :param cancel_reason_msg: The reason the interaction was cancelled.
    :type cancel_reason_msg: str
    """

    def __init__(self, interaction: SuperInteraction, finishing_type: FinishingType, cancel_reason: str, **kwargs):
        self._interaction = interaction
        self._finishing_type = finishing_type
        self._cancel_reason = cancel_reason
        self._kwargs = kwargs

    @property
    def interaction(self) -> SuperInteraction:
        """The super interaction that is being cancelled.

        :return: The super interaction that is being cancelled.
        :rtype: SuperInteraction
        """
        return self._interaction

    @property
    def finishing_type(self) -> FinishingType:
        """The finishing type of the interaction.

        :return: The finishing type of the interaction.
        :rtype: FinishingType
        """
        return self._finishing_type

    @property
    def cancel_reason(self) -> str:
        """The reason the interaction was cancelled.

        :return: The reason the interaction was cancelled.
        :rtype: str
        """
        return self._cancel_reason

    @property
    def keyword_arguments(self) -> Dict[str, Any]:
        """Keyword arguments sent to the cancelled interaction.

        :return: Keyword arguments sent to the cancelled interaction.
        :rtype: Dict[str, Any]
        """
        return self._kwargs
