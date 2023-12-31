"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Tuple

from sims.outfits.outfit_enums import OutfitCategory
from sims.sim_info import SimInfo
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TSimAfterSetCurrentOutfitEvent(CommonEvent):
    """TS4TSimAfterSetCurrentOutfitEvent(sim_info, old_outfit_category_and_index, new_outfit_category_and_index)

    An event that occurs after the current outfit of a Sim is set.

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
            def handle_event(event_data: TS4TSimAfterSetCurrentOutfitEvent):
                pass

    :param sim_info: The Sim that changed.
    :type sim_info: SimInfo
    :param old_outfit_category_and_index: The outfit category and index for the outfit the Sim has changed from.
    :type old_outfit_category_and_index: Tuple[OutfitCategory, int]
    :param new_outfit_category_and_index: The outfit category and index for the outfit the Sim has changed to.
    :type new_outfit_category_and_index: Tuple[OutfitCategory, int]
    """

    def __init__(self, sim_info: SimInfo, old_outfit_category_and_index: Tuple[OutfitCategory, int], new_outfit_category_and_index: Tuple[OutfitCategory, int]):
        self._sim_info = sim_info
        self._old_outfit_category_and_index = old_outfit_category_and_index
        self._new_outfit_category_and_index = new_outfit_category_and_index

    @property
    def sim_info(self) -> SimInfo:
        """The Sim that changed."""
        return self._sim_info

    @property
    def old_outfit_category_and_index(self) -> Tuple[OutfitCategory, int]:
        """The outfit category and index for the outfit the Sim has changed from."""
        return self._old_outfit_category_and_index

    @property
    def new_outfit_category_and_index(self) -> Tuple[OutfitCategory, int]:
        """The outfit category and index for the outfit the Sim has changed to."""
        return self._new_outfit_category_and_index
