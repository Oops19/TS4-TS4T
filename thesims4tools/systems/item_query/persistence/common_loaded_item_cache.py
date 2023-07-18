"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import TypeVar, Generic

from thesims4tools.systems.item_query.dtos.common_loaded_item import CommonLoadedItem
from thesims4tools.systems.caching.common_serializable_object_cache import CommonSerializableObjectCache

CommonLoadedItemCacheType = TypeVar('CommonLoadedItemCacheType', bound=CommonLoadedItem)


class CommonLoadedItemCache(CommonSerializableObjectCache[CommonLoadedItemCacheType], Generic[CommonLoadedItemCacheType]):
    """A cache of Loaded Items."""
    pass
