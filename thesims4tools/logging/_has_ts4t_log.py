"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.logging.has_log import HasLog
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo


class _HasS4CLLog(HasLog):
    """_HasS4CLLog()

    .. note:: This class should only be used by S4CL itself, do not inherit from this class in your own mods!

    """

    # noinspection PyMissingOrEmptyDocstring
    @property
    def mod_identity(self) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @property
    def log_identifier(self) -> str:
        raise NotImplementedError()
