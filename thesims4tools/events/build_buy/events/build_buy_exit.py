"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.events.event_handling.common_event import CommonEvent
from zone import Zone


class TS4TBuildBuyExitEvent(CommonEvent):
    """TS4TBuildBuyEnterEvent(zone)

    An event that occurs upon exiting Build/Buy on a lot.

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
            # - The argument passed to "handle_events" is the name of your Mod.
            @staticmethod
            @CommonEventRegistry.handle_events(ModInfo.get_identity().name)
            def handle_event(event_data: TS4TBuildBuyExitEvent):
                pass

    :param zone: The zone the player has exited Build/Buy on.
    :type zone: Zone
    """

    def __init__(self, zone: Zone):
        self._zone = zone

    @property
    def zone(self) -> Zone:
        """The zone the event occurred on.

        :return: The zone the event occurred on.
        :rtype: Zone
        """
        return self._zone
