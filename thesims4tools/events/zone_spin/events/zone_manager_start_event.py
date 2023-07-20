"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from server.client import Client
from thesims4tools.events.event_handling.common_event import CommonEvent
from zone import Zone
from zone_manager import ZoneManager


class S4CLZoneManagerStartEvent(CommonEvent):
    """S4CLZoneManagerStartEvent(zone_manager)

    An event that occurs after the Zone Manager is started.

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
            def handle_event(event_data: S4CLZoneManagerStartEvent):
                pass

    :param zone_manager: The Zone Manager.
    :type zone_manager: ZoneManager
    """

    def __init__(self, zone_manager: ZoneManager):
        self._zone_manager = zone_manager

    @property
    def zone_manager(self) -> ZoneManager:
        """The Zone Manager

        :return: The Zone Manager.
        :rtype: ZoneManager
        """
        return self._zone_manager