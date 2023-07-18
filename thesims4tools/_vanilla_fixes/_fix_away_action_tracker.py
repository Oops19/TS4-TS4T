"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from away_actions.away_action_tracker import AwayActionTracker
from thesims4tools.modinfo import ModInfo
from thesims4tools.utils.common_injection_utils import CommonInjectionUtils


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), AwayActionTracker, AwayActionTracker.remove_on_away_action_ended_callback.__name__)
def _common_fix_remove_on_away_action_ended_callback(original, self: AwayActionTracker, callback):
    if callback not in self._on_away_action_ended:
        return
    return original(self, callback)


@CommonInjectionUtils.inject_safely_into(ModInfo.get_identity(), AwayActionTracker, AwayActionTracker.remove_on_away_action_started_callback.__name__)
def _common_fix_remove_on_away_action_started_callback(original, self: AwayActionTracker, callback):
    if callback not in self._on_away_action_started:
        return
    return original(self, callback)
