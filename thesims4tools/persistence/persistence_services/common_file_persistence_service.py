"""
The The Sims 4 Tools is licensed under the Creative Commons Attribution 4.0 International public license (CC BY 4.0).
It is a clone of The Sims 4 Community Library (https://github.com/ColonolNutty/Sims4CommunityLibrary) written by and copyright COLONOLNUTTY.

https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode
All modifications by and copyright Oops19.
"""


import os
from typing import Dict, Any

from thesims4tools.exceptions.common_exceptions_handler import CommonExceptionHandler
from thesims4tools.mod_support.mod_identity import CommonModIdentity
from thesims4tools.persistence.persistence_services.common_persistence_service import CommonPersistenceService
from thesims4tools.utils.common_json_io_utils import CommonJSONIOUtils
from thesims4tools.utils.save_load.common_save_utils import CommonSaveUtils


class CommonFilePersistenceService(CommonPersistenceService):
    """CommonFilePersistenceService(per_save=True, per_save_slot=False, folder_name=None, custom_file_name=None, data_folder_path=None)

    A service that persists data into a file and loads data from a file on the system.

    :param per_save: If True, the data will persist for each Game Save file (Set "per_save_slot" to True to persist per save SLOT as well!). If False, the data will persist for all Game Save files. Default is True.
    :type per_save: bool, optional
    :param per_save_slot: If True, the data will persist for each Save slot. If False, the data will persist for each Game file only. Default is False. (This argument requires "per_save" to be True as well!)
    :type per_save_slot: bool, optional
    :param folder_name: Use to specify a custom file path after the normal file path, example: "The Sims 4/Mods/mod_data/<mod_name>/<folder_name>". Default is None.
    :type folder_name: str, optional
    :param custom_file_name: Use to specify a custom name for the loaded and saved file. example: "The Sims 4/Mods/mod_data/<mod_name>/<custom_file_name>" and if "folder_name" is specified: "The Sims 4/Mods/mod_data/<mod_name>/<folder_name>/<custom_file_name>". Default is None.
    :type custom_file_name; str, optional
    :param data_folder_path: Use to specify a custom folder path at the top level for which to save/load data to/from. Default is "Mods/mod_data".
    :type data_folder_path: str, optional
    """

    def __init__(self, per_save: bool=True, per_save_slot: bool=False, folder_name: str=None, custom_file_name: str=None, data_folder_path: str=None) -> None:
        super().__init__()
        self._per_save = per_save
        self._per_save_slot = per_save_slot
        self._folder_name = folder_name
        self._custom_file_name = custom_file_name
        from thesims4tools.utils.common_log_utils import CommonLogUtils
        self._data_folder_path = data_folder_path or CommonLogUtils.get_mod_data_location_path()

    # noinspection PyMissingOrEmptyDocstring
    def load(self, mod_identity: CommonModIdentity, identifier: str=None) -> Dict[str, Any]:
        file_path = self._file_path(mod_identity, identifier=identifier)
        if not file_path:
            return dict()

        self.log.format_with_message('Loading data.', mod=mod_identity, file_path=file_path)

        if not os.path.exists(file_path):
            self.log.format_with_message('No data was found at path.', mod=mod_identity, file_path=file_path)
            return dict()

        loaded_data: Dict[str, Any] = CommonJSONIOUtils.load_from_file(file_path)
        if loaded_data is None:
            return dict()
        self.log.format_with_message('Done loading data.', mod=mod_identity, file_path=file_path, loaded_data=loaded_data)
        return loaded_data

    # noinspection PyMissingOrEmptyDocstring
    def save(self, mod_identity: CommonModIdentity, data: Dict[str, Any], identifier: str=None) -> bool:
        if not data:
            return False
        file_path = self._file_path(mod_identity, identifier=identifier)
        if not file_path:
            return False

        self.log.format_with_message('Loading data.', mod=mod_identity, file_path=file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if os.path.exists(file_path):
            self.log.debug('File existed already, removing the existing one.')
            os.rename(file_path, file_path + '.Old')

        try:
            result = CommonJSONIOUtils.write_to_file(file_path, data)
            self.log.format_with_message('Done saving data.', file_path=file_path)
        except Exception as ex:
            CommonExceptionHandler.log_exception(mod_identity, 'Failed to save data', exception=ex)
            if os.path.exists(file_path + '.Old'):
                os.rename(file_path + '.Old', file_path)
            return False
        if result and os.path.exists(file_path + '.Old'):
            os.remove(file_path + '.Old')
        return result

    # noinspection PyMissingOrEmptyDocstring
    def remove(self, mod_identity: CommonModIdentity, identifier: str=None) -> bool:
        file_path = self._file_path(mod_identity, identifier=identifier)

        self.log.format_with_message('Loading data.', mod=mod_identity, file_path=file_path)

        if os.path.exists(file_path):
            self.log.debug('File existed already, removing the existing one.')
            os.remove(file_path)

        self.log.format_with_message('Data deleted successfully.', file_path=file_path)
        return not os.path.exists(file_path)

    def _file_path(self, mod_identity: CommonModIdentity, identifier: str=None) -> str:
        data_name = self._format_data_name(mod_identity, identifier=identifier)
        folder_path = os.path.join(self._data_folder_path, mod_identity.base_namespace.lower())
        if self._folder_name is not None:
            folder_path = os.path.join(folder_path, self._folder_name)
        if self._custom_file_name is not None:
            return os.path.join(folder_path, self._custom_file_name)
        if self._per_save:
            save_slot_guid = CommonSaveUtils.get_save_slot_guid()
            from thesims4tools.ts4t_configuration import TS4TConfiguration
            if self._per_save_slot or TS4TConfiguration().persist_mod_data_per_save_slot:
                save_slot_id = CommonSaveUtils.get_save_slot_id()
                if save_slot_id == 0:
                    return ''
                return os.path.join(folder_path, f'{data_name}_id_{save_slot_id}_guid_{save_slot_guid}.json')
            else:
                return os.path.join(folder_path, f'{data_name}_guid_{save_slot_guid}.json')
        else:
            return os.path.join(folder_path, f'{data_name}.json')
