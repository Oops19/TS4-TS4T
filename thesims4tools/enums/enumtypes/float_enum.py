"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Any
from thesims4tools.enums.common_enum import CommonEnumMetaclass


class CommonEnumFloat(float):
    """CommonEnumFloat(enum_name, enum_value, class_name)

    An enum that holds a float value.

    :param enum_name: The name of the enum.
    :type enum_name: str
    :param enum_value: The value of the enum.
    :type enum_value: float
    :param class_name: The name of the class containing the enum.
    :type class_name: str
    """
    def __init__(self, enum_name: str, enum_value: float, class_name: str):
        super().__init__()
        self._name = enum_name
        self._value = enum_value
        self._class_name = class_name

    def __new__(cls, _, enum_value: float, class_name: str):
        return super().__new__(cls, enum_value)

    @property
    def name(self) -> str:
        """The name of the enum.

        :return: The name of the enum.
        :rtype: str
        """
        return self._name

    @property
    def value(self) -> float:
        """The value of the enum.

        :return: The value of the enum.
        :rtype: float
        """
        return self._value

    def __eq__(self, other: Any):
        other_value = other
        if hasattr(other, 'value'):
            other_value = other.value
        return self.value.__eq__(other_value)

    def __repr__(self) -> str:
        return '{}.{}'.format(self._class_name, self.name)

    def __str__(self) -> str:
        return self.__repr__()

    def __hash__(self) -> int:
        return hash(self.value)


class CommonEnumFloatMetaclass(CommonEnumMetaclass):
    """A metaclass for float enums.

    """

    # noinspection PyMissingOrEmptyDocstring
    @classmethod
    def get_enum_type(mcs) -> Any:
        return float

    @classmethod
    def _get_common_enum(mcs, enum_name: str, enum_value: float, class_name: str):
        return CommonEnumFloat(enum_name, enum_value, class_name)


class CommonEnumFloatBase(float, metaclass=CommonEnumFloatMetaclass):
    """An inheritable class to turn properties into float enums.

    """
    def __call__(self, val) -> CommonEnumFloat:
        pass
