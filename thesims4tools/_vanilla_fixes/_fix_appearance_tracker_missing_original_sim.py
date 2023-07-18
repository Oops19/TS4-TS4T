"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from typing import Union

from buffs.appearance_modifier.appearance_modifier import AppearanceModifier
from sims.outfits.outfit_enums import BodyTypeFlag
from sims.sim_info import SimInfo
from sims.sim_info_base_wrapper import SimInfoBaseWrapper
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), AppearanceModifier.BaseAppearanceModification, AppearanceModifier.BaseAppearanceModification.__init__.__name__)
def _common_keep_original_sim_info_around(original, self, *_, **__) -> None:
    original_result = original(self, *_, **__)

    original_modify_sim_info = self.modify_sim_info

    def _fixed_modify_sim_info(source_sim_info: Union[SimInfo, SimInfoBaseWrapper], modified_sim_info: SimInfoBaseWrapper, random_seed: int) -> BodyTypeFlag:
        if not hasattr(modified_sim_info, 'original_unmodified_sim_info'):
            setattr(modified_sim_info, 'original_unmodified_sim_info', source_sim_info)
        return original_modify_sim_info(source_sim_info, modified_sim_info, random_seed)

    self.modify_sim_info = _fixed_modify_sim_info
    return original_result
