"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from interactions.base.interaction import Interaction
from interactions.interaction_queue import InteractionQueue
from thesims4tools.classes.testing.common_test_result import CommonTestResult
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TInteractionPostQueuedEvent(CommonEvent):
    """TS4TInteractionPostQueuedEvent(interaction, interaction_queue, queue_result)

    An event that occurs after a Sim adds an interaction to their interaction queue.

    .. note:: This event fires AFTER the interaction is actually queued. Like a Post-Queue.

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
            def handle_event(event_data: TS4TInteractionPostQueuedEvent) -> bool:
                # Return True here to signify the event listener ran successfully. Return False or None here to signify the event listener failed to run.
                return True

    :param interaction: The interaction that was queued.
    :type interaction: Interaction
    :param interaction_queue: The interaction queue of the Sim.
    :type interaction_queue: InteractionQueue
    :param queue_result: The result of the interaction being Queued.
    :type queue_result: CommonTestResult
    """

    def __init__(self, interaction: Interaction, interaction_queue: InteractionQueue, queue_result: CommonTestResult):
        self._interaction = interaction
        self._interaction_queue = interaction_queue
        self._queue_result = queue_result

    @property
    def interaction(self) -> Interaction:
        """The interaction that was queued.

        :return: The interaction that was queued.
        :rtype: Interaction
        """
        return self._interaction

    @property
    def interaction_queue(self) -> InteractionQueue:
        """The interaction queue of the Sim that queued the interaction.

        :return: The interaction queue of the Sim that queued the interaction.
        :rtype: InteractionQueue
        """
        return self._interaction_queue

    @property
    def queue_result(self) -> CommonTestResult:
        """The result of the interaction being Queued.

        :return: The result of the interaction being Queued.
        :rtype: CommonTestResult
        """
        return self._queue_result
