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
file_path_normalization_mapping = [{'regex_string' : '%system%', 
                                    'replacement' : 'CSIDL_SYSTEM'},
                                    {'regex_string' : '%appdata%', 
                                     'replacement' : 'CSIDL_APPDATA'},
                                    {'regex_string' : '%commonappdata%', 
                                     'replacement' : 'CSIDL_COMMON_APPDATA'},
                                    {'regex_string' : '%commonprograms%', 
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'regex_string' : '%programfiles%',  
                                     'replacement' : 'CSIDL_PROGRAM_FILES'},
                                    {'regex_string' : '%programs%',  
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'regex_string' : '%temp%', 
                                     'replacement' : 'TEMP'},
                                    {'regex_string' : '%userprofile%', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'regex_string' : '%profiles%', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'regex_string' : '%windir%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'regex_string' : '%systemroot%', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'regex_string' : '[\w][:]\\\\windows\\\\system32', 
                                     'replacement' : 'CSIDL_SYSTEM'},
                                    {'regex_string' : '[\w][:]\\\\windows(?:(?!\\\\system32))', 
                                     'replacement' : 'CSIDL_WINDOWS'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\application data', 
                                     'replacement' : 'CSIDL_APPDATA'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\all users\\\\application data', 
                                     'replacement' : 'CSIDL_COMMON_APPDATA'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\all users\\\\start menu\\\\programs', 
                                     'replacement' : 'CSIDL_COMMON_PROGRAMS'},
                                    {'regex_string' : '[\w][:]\\\\[A-Z+a-z~ ()0-9\\\\]+\\\\temp', 
                                     'replacement' : 'TEMP'},
                                    {'regex_string' : '[\w][:]\\\\users\\\\[A-Z+a-z~ ()0-9]+', 
                                     'replacement' : 'CSIDL_PROFILE'},
                                    {'regex_string' : '^\w:\\\\{0,2}$', 
                                     'replacement' : '%SystemDrive%'},
                                    {'regex_string' : '^\w:\\\\documents and settings\\\\all users', 
                                     'replacement' : '%ALLUSERSPROFILE%'},
                                    {'regex_string' : '^\w:\\\\programdata', 
                                     'replacement' : '%ALLUSERSPROFILE%'}]

# Windows Registry Hive Abbreviated -> Full mappings
registry_hive_normalization_mapping = [{'regex_string' : '^hklm$',
                                        'replacement' : 'HKEY_LOCAL_MACHINE'},
                                       {'regex_string' : '^hkcc$',
                                        'replacement' : 'HKEY_CURRENT_CONFIG'},
                                       {'regex_string' : '^hkcr$',
                                        'replacement' : 'HKEY_CLASSES_ROOT'},
                                       {'regex_string' : '^hkcu$',
                                        'replacement' : 'HKEY_CURRENT_USER'},
                                       {'regex_string' : '^hku$',
                                        'replacement' : 'HKEY_USERS'}]

# Normalization-related methods

def perform_replacement(entity, mapping_list):
    '''Perform a replacement on the value of an entity using a replacement mapping, if applicable.'''
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
            if re.search(regex_string, entity_value, flags=re.IGNORECASE):
                entity.value = re.sub(regex_string, replacement, entity_value, flags=re.IGNORECASE)

def normalize_object_properties(object_properties):
    '''Normalize the field values of certain ObjectProperties instances.
       
       Currently supports: File Objects
                             --File_Path field. Normalized for common Windows
                                                paths/environment variables.
                           Windows Registry Key Objects
                             --Registry Value/Data field. Normalized for common
                                                          Windows paths/environment
                                                          variables.
                             --Hive field. Normalized for full representation  
                                           from abbreviated form.
                                           E.g., HKLM -> HKEY_LOCAL_MACHINE.
                           Process Objects
                             --Image_Info/Path field. Normalized for common
                                                      Windows paths/environment
                                                      variables. '''
                           
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