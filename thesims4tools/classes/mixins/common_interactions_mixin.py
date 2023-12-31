"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Tuple, Iterator

from interactions.base.interaction import Interaction


class CommonInteractionsMixin:
    """A mixin that will do something with interactions."""

    def __init__(self) -> None:
        self._cached_interactions = None

    @property
    def interaction_ids(self) -> Tuple[int]:
        """A collection of interaction identifiers.

        :return: A collection of interaction identifiers.
        :rtype: Tuple[int]
        """
        raise NotImplementedError()

    def _interaction_instances_gen(self) -> Iterator[Interaction]:
        if self._cached_interactions is not None:
            yield from self._cached_interactions
        else:
            cached_interactions = list()
            from thesims4tools.utils.resources.common_interaction_utils import CommonInteractionUtils
            for interaction_id in self.interaction_ids:
                interaction = CommonInteractionUtils.load_interaction_by_id(interaction_id)
                if interaction is None:
                    continue
                yield interaction
                cached_interactions.append(interaction)
            self._cached_interactions = cached_interactions
