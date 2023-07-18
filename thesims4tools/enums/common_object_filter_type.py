"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.enums.enumtypes.common_int import CommonInt


class CommonObjectFilterType(CommonInt):
    """The type of an object filter."""
    OBJECT_DEFINITION_FILTER = 0
    OBJECT_TAG_FILTER = 1
    CUSTOM = 5000
