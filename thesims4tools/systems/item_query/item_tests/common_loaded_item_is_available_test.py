"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.systems.item_query.dtos.common_loaded_item import CommonLoadedItem
from thesims4tools.systems.item_query.item_tests.common_loaded_item_test import CommonLoadedItemTest
from thesims4tools.classes.testing.common_test_result import CommonTestResult
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo


class CommonLoadedItemIsAvailableTest(CommonLoadedItemTest[CommonLoadedItem]):
    """ Test for an item is available. """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        return 'common_loaded_item_is_available'

    # noinspection PyMissingOrEmptyDocstring
    def test_item(self, item: CommonLoadedItem) -> CommonTestResult:
        if not item.is_available:
            return CommonTestResult(False, reason='Item is not available.')
        return CommonTestResult.TRUE
