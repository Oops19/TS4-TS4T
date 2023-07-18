"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


from objects.game_object import GameObject
from thesims4tools.modinfo import ModInfo
from thesims4tools.services.commands.common_console_command import CommonConsoleCommand, \
    CommonConsoleCommandArgument
from thesims4tools.services.commands.common_console_command_output import CommonConsoleCommandOutput
from thesims4tools.utils.common_log_registry import CommonLogRegistry
from thesims4tools.utils.misc.common_fire_utils import CommonFireUtils
from thesims4tools.utils.objects.common_object_location_utils import CommonObjectLocationUtils
from thesims4tools.utils.objects.common_object_utils import CommonObjectUtils
from thesims4tools.utils.sims.common_sim_location_utils import CommonSimLocationUtils
from thesims4tools.utils.sims.common_sim_utils import CommonSimUtils
from thesims4tools.utils.sims.common_trait_utils import CommonTraitUtils

log = CommonLogRegistry().register_log(ModInfo.get_identity(), 'ts4t_commands')
log.enable()


@CommonConsoleCommand(ModInfo.get_identity(), 'ts4t.the_mother_calls', 'Invokes the mothers call.', show_with_help_command=False)
def _common_the_mother_calls(output: CommonConsoleCommandOutput):
    output('She calls and you must listen! Who shall answer the call?')
    sim_count = 0
    # trait_Strangerville_Infected
    trait_id = 201407
    output(f'The call has begun, who shall answer it?')
    for sim_info in CommonSimUtils.get_sim_info_for_all_sims_generator():
        if CommonTraitUtils.has_trait(sim_info, trait_id):
            continue
        if CommonTraitUtils.add_trait(sim_info, trait_id):
            sim_count += 1
    output(f'{sim_count} Sim(s) have answered the call.')


@CommonConsoleCommand(ModInfo.get_identity(), 'ts4t.come_to_me_now', 'Formally request all objects in the area to come to the active Sim.', show_with_help_command=False)
def _common_come_to_me_now(output: CommonConsoleCommandOutput):
    sim_info = CommonSimUtils.get_active_sim_info()
    new_location = CommonSimLocationUtils.get_location(sim_info)
    object_count = 0
    output(f'Attempting to request all objects to come to {sim_info}.')
    for game_object in CommonObjectUtils.get_instance_for_all_game_objects_generator():
        # noinspection PyBroadException
        try:
            CommonObjectLocationUtils.set_location(game_object, new_location)
            object_count += 1
        except:
            continue
    output(f'{object_count} Object(s) came to {sim_info}.')


@CommonConsoleCommand(ModInfo.get_identity(), 'ts4t.burn_it_all', 'Some Sims just want to see the world burn.', show_with_help_command=False)
def _common_burn_it_all(output: CommonConsoleCommandOutput):
    object_count = 0
    output(f'Do you smell smoke?')
    for game_object in CommonObjectUtils.get_instance_for_all_game_objects_generator():
        # noinspection PyBroadException
        try:
            if CommonFireUtils.spawn_fires_on_object(game_object):
                object_count += 1
        except:
            continue
    output(f'{object_count} Object(s) have been set ablaze. You might want to run now.')


@CommonConsoleCommand(
    ModInfo.get_identity(),
    'ts4t.burn_it',
    'Some Sims just want to see the world burn.',
    command_arguments=(
        CommonConsoleCommandArgument('game_object', 'Decimal ID', 'The Decimal Identifier of the object to spawn a fire at.'),
    ),
    show_with_help_command=False
)
def _common_burn_it(output: CommonConsoleCommandOutput, game_object: GameObject):
    output(f'Do you smell smoke?')
    if not CommonFireUtils.is_fire_allowed_at_location(CommonObjectLocationUtils.get_location(game_object)):
        output(f'Fires are not allowed on the object. {game_object}.')
        return
    if CommonFireUtils.spawn_fires_on_object(game_object):
        output(f'{game_object} has been set ablaze. You might want to run now.')
    else:
        output(f'For some reason {game_object} failed to catch fire.')
