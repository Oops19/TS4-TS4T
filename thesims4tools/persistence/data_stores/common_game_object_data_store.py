"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Dict, Any
from thesims4tools.persistence.data_stores.common_data_store import CommonDataStore


class CommonGameObjectDataStore(CommonDataStore):
    """ A store of Game Object Data. """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_identifier(cls) -> str:
        return 'game_object_data'

    @property
    def _version(self) -> int:
        return 1

    @property
    def _default_data(self) -> Dict[str, Any]:
        return dict()

    # noinspection PyMissingOrEmptyDocstring
    def get_default_value_by_key(self, key: str) -> Any:
        return dict()
