"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils
from zone import Zone

if hasattr(Zone, 'register_callback'):
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Zone, Zone.register_callback.__name__, handle_exceptions=False)
    def _common_fix_register_callback_missing_key(original, self: Zone, callback_type, *_, **__):
        if callback_type not in self._zone_state_callbacks:
            return
        return original(self, callback_type, *_, **__)


if hasattr(Zone, 'unregister_callback'):
    @CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), Zone, Zone.unregister_callback.__name__, handle_exceptions=False)
    def _common_fix_unregister_callback_missing_key(original, self: Zone, callback_type, *_, **__):
        if callback_type not in self._zone_state_callbacks:
            return
        return original(self, callback_type, *_, **__)
