"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from thesims4tools.enums.enumtypes.common_int import CommonInt


class CommonRelationshipTrackId(CommonInt):
    """Identifiers for vanilla sim relationship tracks.

    """
    INVALID: 'CommonRelationshipTrackId' = 0
    AUTHORITY: 'CommonRelationshipTrackId' = 161998
    FEUD: 'CommonRelationshipTrackId' = 193901
    FRIENDSHIP: 'CommonRelationshipTrackId' = 16650
    MISCHIEF: 'CommonRelationshipTrackId' = 26920
    RIVALRY: 'CommonRelationshipTrackId' = 161999
    ROMANCE: 'CommonRelationshipTrackId' = 16651
    SIM_TO_PET_FRIENDSHIP: 'CommonRelationshipTrackId' = 159228
    SMART_HUB_FRIENDSHIP: 'CommonRelationshipTrackId' = 203686
