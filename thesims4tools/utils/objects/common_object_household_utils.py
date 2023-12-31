"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from objects.game_object import GameObject


class CommonObjectHouseholdUtils:
    """Utilities for manipulating Household ownership of Objects.

    """

    @staticmethod
    def set_owning_household_id(game_object: GameObject, household_id: int) -> bool:
        """set_owning_household_id(game_object, household_id)

        Set the Household that owns the Object.
        .. note: THIS FUNCTION IS OBSOLETE PLEASE USE See :class:`.CommonObjectOwnershipUtils` for updated functions.

        :param game_object: An instance of an Object.
        :type game_object: GameObject
        :param household_id: The decimal identifier of a Household.
        :type household_id: int
        :return: True, if the Household was successfully set as the owner. False, if not.
        :rtype: bool
        """
        from thesims4tools.utils.objects.common_object_ownership_utils import CommonObjectOwnershipUtils
        return CommonObjectOwnershipUtils.set_owning_household_id(game_object, household_id)

    @staticmethod
    def get_owning_household_id(game_object: GameObject) -> int:
        """get_owning_household_id(game_object)

        Retrieve the decimal identifier of the Household that owns the Object.

        .. note: THIS FUNCTION IS OBSOLETE PLEASE USE See :class:`.CommonObjectOwnershipUtils` for updated functions.

        :param game_object: An instance of an Object.
        :type game_object: GameObject
        :return: The decimal identifier of the Household that owns the object.
        :rtype: int
        """
        from thesims4tools.utils.objects.common_object_ownership_utils import CommonObjectOwnershipUtils
        return CommonObjectOwnershipUtils.get_owning_household_id(game_object)
