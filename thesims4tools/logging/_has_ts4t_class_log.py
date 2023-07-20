"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.logging.has_class_log import HasClassLog
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.modinfo import ModInfo


class _HasS4CLClassLog(HasClassLog):
    """_HasS4CLClassLog()

    .. note:: This class should only be used by S4CL itself, do not inherit from this class in your own mods!

    """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_mod_identity(cls) -> CommonModIdentity:
        return ModInfo.get_identity()

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_log_identifier(cls) -> str:
        raise NotImplementedError()
