"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


# The purpose of this file is to fix the fact that when trying to access the "full_name" attribute on Sims an empty string is returned.
# noinspection PyBroadException
from sims.sim_info import SimInfo
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils
from thesims4tools.utils.sims.common_sim_name_utils import CommonSimNameUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), SimInfo, 'full_name')
def _common_fix_full_name_returning_empty_string(original, self: SimInfo, *_, **__):
    original_value = original(self, *_, **__)
    if original_value == '':
        return CommonSimNameUtils.get_full_name(CommonSimUtils.get_sim_info(self))
    return original_value
