"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any

from services.persistence_service import SaveGameData
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TSaveSavedEvent(CommonEvent):
    """TS4TSaveSavedEvent(save_slot_data)

    An event that occurs upon a Save being saved (Before it has been saved).

    .. note:: This event will only occur when the Player manually saves the game.

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
            def handle_event(event_data: TS4TSaveSavedEvent):
                pass

    :param save_game_data: The data that will be saved.
    :type save_game_data: SaveGameData
    """

    def __init__(self, save_game_data: SaveGameData):
        self._save_game_data = save_game_data

    @property
    def save_game_data(self) -> Any:
        """The game data that will be saved."""
        return self._save_game_data

    @property
    def save_slot_name(self) -> str:
        """The name of the save slot."""
        return self.save_game_data.slot_name

    @property
    def save_slot_id(self) -> int:
        """The id of the save slot."""
        return self.save_game_data.slot_id
