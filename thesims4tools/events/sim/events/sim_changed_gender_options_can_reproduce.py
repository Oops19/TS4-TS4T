"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from sims.sim_info import SimInfo
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TSimChangedGenderOptionsCanReproduceEvent(CommonEvent):
    """TS4TSimChangedGenderOptionsCanReproduceEvent(sim_info)

    An event that occurs when a Pet Sim has changed whether they can reproduce or not.

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
            def handle_event(event_data: TS4TSimChangedGenderOptionsCanReproduceEvent):
                pass

    :param sim_info: The Sim that changed.
    :type sim_info: SimInfo
    """

    def __init__(self, sim_info: SimInfo):
        self._sim_info = sim_info

    @property
    def sim_info(self) -> SimInfo:
        """The Sim that changed.

        :return: The Sim that changed.
        :rtype: SimInfo
        """
        return self._sim_info
