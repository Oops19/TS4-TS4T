"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from buffs.buff import Buff
from sims.sim_info import SimInfo
from thesims4tools.events.event_handling.common_event import CommonEvent
from thesims4tools.utils.sims.common_buff_utils import CommonBuffUtils


class TS4TSimBuffRemovedEvent(CommonEvent):
    """TS4TSimBuffRemovedEvent(sim_info, buff)

    An event that occurs when a Buff is removed from a Sim.

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
            @CommonEventRegistry.handle_events(ModInfo.get_identity())
            def handle_event(event_data: TS4TSimBuffRemovedEvent):
                pass

    :param sim_info: The Sim that changed.
    :type sim_info: SimInfo
    :param buff: The Buff that was removed.
    :type buff: Buff
    """

    def __init__(self, sim_info: SimInfo, buff: Buff):
        self._sim_info = sim_info
        self._buff = buff

    @property
    def sim_info(self) -> SimInfo:
        """The Sim that lost the buff.

        :return: The Sim that lost the buff.
        :rtype: SimInfo
        """
        return self._sim_info

    @property
    def buff(self) -> Buff:
        """The Buff that was removed.

        :return: The Buff that was removed.
        :rtype: Buff
        """
        return self._buff

    @property
    def buff_id(self) -> int:
        """The decimal identifier of the Buff.

        :return: The decimal identifier of the Buff.
        :rtype: int
        """
        return CommonBuffUtils.get_buff_id(self.buff)
