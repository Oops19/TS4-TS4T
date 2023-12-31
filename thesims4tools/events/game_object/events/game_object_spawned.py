"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from objects.game_object import GameObject
from thesims4tools.events.event_handling.common_event import CommonEvent


class TS4TGameObjectSpawnedEvent(CommonEvent):
    """TS4TGameObjectSpawnedEvent(game_object)

    An event that occurs after a Game Object has been spawned.

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
            def handle_event(event_data: TS4TGameObjectSpawnedEvent):
                pass

    :param game_object: The Game Object that was spawned.
    :type game_object: GameObject
    """

    def __init__(self, game_object: GameObject):
        self._game_object = game_object

    @property
    def game_object(self) -> GameObject:
        """The Game Object that was spawned.

        :return: The Game Object that was spawned.
        :rtype: GameObject
        """
        return self._game_object
