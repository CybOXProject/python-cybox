# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_registry_key_object as win_registry_key_binding

from cybox.common import (ByteRuns, DateTime, ObjectProperties, String,
        UnsignedInteger)
from cybox.objects.win_handle_object import WinHandleList


class RegistryValue(cybox.Entity):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistryValueType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"

    name = cybox.TypedField("Name", String)
    data = cybox.TypedField("Data", String)
    datatype = cybox.TypedField("Datatype", String)
    byte_runs = cybox.TypedField("Byte_Runs", ByteRuns)


class RegistryValues(cybox.EntityList):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistryValuesType
    _binding_var = "Value"
    _contained_type = RegistryValue
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"


class RegistrySubkeys(cybox.EntityList):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistrySubkeysType
    _binding_var = "Subkey"
    # We haven't defined the contained type yet, so we specify it below.
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"


class WinRegistryKey(ObjectProperties):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.WindowsRegistryKeyObjectType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"
    _XSI_NS = "WinRegistryKeyObj"
    _XSI_TYPE = "WindowsRegistryKeyObjectType"

    key = cybox.TypedField("Key", String)
    hive = cybox.TypedField("Hive", String)
    number_values = cybox.TypedField("Number_Values", UnsignedInteger)
    values = cybox.TypedField("Values", RegistryValues)
    modified_time = cybox.TypedField("Modified_Time", DateTime)
    creator_username = cybox.TypedField("Creator_Username", String)
    handle_list = cybox.TypedField("Handle_List", WinHandleList)
    number_subkeys = cybox.TypedField("Number_Subkeys", UnsignedInteger)
    subkeys = cybox.TypedField("Subkeys", RegistrySubkeys)
    byte_runs = cybox.TypedField("Byte_Runs", ByteRuns)


RegistrySubkeys._contained_type = WinRegistryKey
