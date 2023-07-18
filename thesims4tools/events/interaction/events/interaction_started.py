"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any

from interactions.base.interaction import Interaction
from sims.sim_info import SimInfo
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TInteractionStartedEvent(CommonEvent):
    """TS4TInteractionStartedEvent(interaction, sim_info, target)

    An event that occurs when a Sim has started an interaction.

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
            def handle_event(event_data: TS4TInteractionStartedEvent) -> bool:
                # Return True here to signify the event listener ran successfully. Return False or None here to signify the event listener failed to run.
                return True

    :param interaction: The interaction that was run.
    :type interaction: Interaction
    :param sim_info: The Sim doing the interaction.
    :type sim_info: SimInfo
    :param target: The Target of the interaction.
    :type target: Any
    """

    def __init__(self, interaction: Interaction, sim_info: SimInfo, target: Any):
        self._sim_info = sim_info
        self._target = target
        self._interaction = interaction

    @property
    def interaction(self) -> Interaction:
        """The interaction that was run.

        :return: The interaction that was run.
        :rtype: Interaction
        """
        return self._interaction

    @property
    def sim_info(self) -> SimInfo:
        """The Sim that started the interaction."""
        return self._sim_info

    @property
    def target(self) -> Any:
        """The target of the interaction."""
        return self._target
