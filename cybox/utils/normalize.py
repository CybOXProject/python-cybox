# CybOX Object Normalization Methods
# For normalizing certain CybOX Objects to enable better correlation

# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import re
from cybox.objects.file_object import File
from cybox.objects.win_registry_key_object import WinRegistryKey
from cybox.objects.process_object import Process
from cybox.objects.mutex_object import Mutex

# Normalization-related mappings

# Windows-specific file normalization mappings
# Replace with CSIDL values, if possible
# As a backup, replace with Windows environment variable values
file_path_normalization_mapping = [{'search_string' : '%System%', 
                                    'replacement' : 'CSIDL_SYSTEM'},
                                    {'search_string' : '%SYSTEMROOT%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'search_string' : '%SystemRoot%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'search_string' : '%systemroot%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'search_string' : '%Windir%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'search_string' : '%windir%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'search_string' : '%AppData%', 
                                     'replacement' : 'CSIDL_APPDATA'},
                                    {'search_string' : '%CommonAppData%', 
                                     'replacement' : 'CSIDL_COMMON_APPDATA'},
                                    {'search_string' : '%CommonPrograms%', 
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'search_string' : '%ProgramFiles%',  
                                     'replacement' : 'CSIDL_PROGRAM_FILES'},
                                    {'search_string' : '%Programs%',  
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'search_string' : '%Temp%', 
                                     'replacement' : 'TEMP'},
                                    {'search_string' : '%USERPROFILE%', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'search_string' : '%userprofile%', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'search_string' : '%Profiles%', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'regex_string' : '[\w][:]\\\\[W|w][I|i][N|n][D|d][O|o][W|w][S|s]\\\\[S|s][Y|y][S|s][T|t][E|e][M|m]32', 
                                     'replacement' : 'CSIDL_SYSTEM'},
                                    {'regex_string' : '[\w][:]\\\\[W|w][I|i][N|n][D|d][O|o][W|w][S|s](?:(?!\\\\[S|s][Y|y][S|s][T|t][E|e][M|m]32))', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\[A|a][P|p][P|p][L|l][I|i][C|c][A|a][T|t][I|i][O|o][N|n] [D|d][A|a][T|t][A|a]', 
                                     'replacement' : 'CSIDL_APPDATA'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\[A|a][L|l][L|l] [U|u][S|s][E|e][R|r][S|s]\\\\[A|a][P|p][P|p][L|l][I|i][C|c][A|a][T|t][I|i][O|o][N|n] [D|d][A|a][T|t][A|a]', 
                                     'replacement' : 'CSIDL_COMMON_APPDATA'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\[A|a][L|l][L|l] [U|u][S|s][E|e][R|r][S|s]\\\\[S|s][T|t][A|a][R|r][T|t] [M|m][E|e][N|n][U|u]\\\\[P|p][R|r][O|o][G|g][R|r][A|a][M|m][S|s]', 
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\[T|t][E|e][M|m][P|p]', 
                                     'replacement' : 'TEMP'},
                                    {'regex_string' : '[\w][:]\\\\[U|u][S|s][E|e][R|r][S|s]\\\\[A-Z+a-z~ ()0-9]+', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'regex_string' : '^\w:\\{0,2}$', 
                                     'replacement' : '%SystemDrive%'},
                                    {'regex_string' : '^\w:\\\\Documents and Settings\\\\All Users', 
                                     'replacement' : '%ALLUSERSPROFILE%'},
                                    {'regex_string' : '^\w:\\\\ProgramData', 
                                     'replacement' : '%ALLUSERSPROFILE%'}]

registry_hive_normalization_mapping = [{'regex_string' : '^[H|h][K|k][L|l][M|m]$',
                                        'replacement' : 'HKEY_LOCAL_MACHINE'},
                                       {'regex_string' : '^[H|h][K|k][C|c][C|c]$',
                                        'replacement' : 'HKEY_CURRENT_CONFIG'},
                                       {'regex_string' : '^[H|h][K|k][C|c][R|r]$',
                                        'replacement' : 'HKEY_CLASSES_ROOT'},
                                       {'regex_string' : '^[H|h][K|k][C|c][U|u]$',
                                        'replacement' : 'HKEY_CURRENT_USER'},
                                       {'regex_string' : '^[H|h][K|k][U|u]$',
                                        'replacement' : 'HKEY_USERS'},]

# Normalization-related methods

def perform_replacement(entity, mapping_list):
    '''Perform a replacement on the value of an entity using a replacement mapping, if applicable'''
    # Make sure the entity has a value to begin with
    if not entity.value:
        return
    entity_value = entity.value
    # Attempt the replacement
    for mapping_dict in mapping_list:
        # Do the direct replacement, if applicable
        if 'search_string' in mapping_dict.keys():
            search_string = mapping_dict['search_string']
            replacement = mapping_dict['replacement']
            if search_string in entity_value:
                entity.value = entity_value.replace(search_string, replacement)
        # Do the regex replacement, if applicable
        if 'regex_string' in mapping_dict.keys():
            regex_string = mapping_dict['regex_string']
            replacement = mapping_dict['replacement']
            if re.search(regex_string, entity_value):
                entity.value = re.sub(regex_string, replacement, entity_value)

def normalize_object_properties(object_properties):
    '''Normalize the values of an ObjectProperties instance'''
    # Normalize file object properties/subclasses
    if isinstance(object_properties, File):
        # Normalize any windows-related file paths
        if object_properties.file_path:
            perform_replacement(object_properties.file_path, file_path_normalization_mapping)
    # Normalize windows registry key object properties
    elif isinstance(object_properties, WinRegistryKey):
        # Normalize any windows-related file paths in a registry key value
        if object_properties.values:
            for registry_value in object_properties.values:
                if registry_value.data:
                    perform_replacement(registry_value.data, file_path_normalization_mapping)
        # Normalize any short-hand hive values
        if object_properties.hive:
            perform_replacement(object_properties.hive, registry_hive_normalization_mapping)
    # Normalize process object properties/subclasses
    elif isinstance(object_properties, Process):
        # Normalize any windows-related file paths in the process image path
        if object_properties.image_info and object_properties.image_info.path:
            perform_replacement(object_properties.image_info.path, file_path_normalization_mapping)
    # Normalize mutex object properties/subclasses
    elif isinstance(object_properties, Mutex):
        # Normalize some oddities in mutex-name reporting
        if object_properties.name:
            mutex_name = object_properties.name.value
            if mutex_name.startswith('C:\\'):
                object_properties.name.value = mutex_name[3:]
            