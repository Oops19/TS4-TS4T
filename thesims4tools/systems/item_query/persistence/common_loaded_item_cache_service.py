"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Generic, TypeVar, Tuple, Union, Dict, Any

from thesims4tools.systems.item_query.dtos.common_loaded_item import CommonLoadedItem
from thesims4tools.systems.item_query.persistence.common_loaded_item_cache import CommonLoadedItemCache
from thesims4tools.systems.caching.common_serializable_object_cache_service import \
    CommonSerializableObjectCacheService
from thesims4tools.mod_support.mod_identity import CommonModIdentity


CommonLoadedItemCacheType = TypeVar('CommonLoadedItemCacheType', bound=CommonLoadedItemCache[CommonLoadedItem])


class CommonLoadedItemCacheService(CommonSerializableObjectCacheService[CommonLoadedItemCacheType], Generic[CommonLoadedItemCacheType]):
    """A service that manages a cache of Loaded Items."""

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_identity(self) -> CommonModIdentity:
        raise NotImplementedError()

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        return 'common_loaded_item_cache_service'

    @property
    def _cache_file_name(self) -> str:
        raise NotImplementedError()

    def _deserialize_cache(self, data: Union[str, Dict[str, Any]]) -> CommonLoadedItemCacheType:
        raise NotImplementedError()

    # noinspection PyMissingOrEmptyDocstring
    def create_cache(self, objects: Tuple[CommonLoadedItem], checksums: Tuple[Any]) -> CommonLoadedItemCacheType:
        checksum_data = dict()
        for (snippet_name, snippet_id, checksum_value) in checksums:
            checksum_data[f'{snippet_name}-{snippet_id}'] = checksum_value
        return CommonLoadedItemCacheType[Any](objects, checksum_data)
