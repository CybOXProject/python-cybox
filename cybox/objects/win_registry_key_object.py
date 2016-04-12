# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_registry_key_object as win_registry_key_binding

from cybox.common import (ByteRuns, DateTime, ObjectProperties, String,
        UnsignedInteger)
from cybox.objects.win_handle_object import WinHandleList


class RegistryValue(entities.Entity):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistryValueType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"

    name = fields.TypedField("Name", String)
    data = fields.TypedField("Data", String)
    datatype = fields.TypedField("Datatype", String)
    byte_runs = fields.TypedField("Byte_Runs", ByteRuns)


class RegistryValues(entities.EntityList):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistryValuesType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"
    value = fields.TypedField("Value", RegistryValue, multiple=True)


class RegistrySubkeys(entities.EntityList):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.RegistrySubkeysType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"
    subkey = fields.TypedField("Subkey", type_="cybox.objects.win_registry_key_object.WinRegistryKey", multiple=True)


class WinRegistryKey(ObjectProperties):
    _binding = win_registry_key_binding
    _binding_class = win_registry_key_binding.WindowsRegistryKeyObjectType
    _namespace = "http://cybox.mitre.org/objects#WinRegistryKeyObject-2"
    _XSI_NS = "WinRegistryKeyObj"
    _XSI_TYPE = "WindowsRegistryKeyObjectType"

    key = fields.TypedField("Key", String)
    hive = fields.TypedField("Hive", String)
    number_values = fields.TypedField("Number_Values", UnsignedInteger)
    values = fields.TypedField("Values", RegistryValues)
    modified_time = fields.TypedField("Modified_Time", DateTime)
    creator_username = fields.TypedField("Creator_Username", String)
    handle_list = fields.TypedField("Handle_List", WinHandleList)
    number_subkeys = fields.TypedField("Number_Subkeys", UnsignedInteger)
    subkeys = fields.TypedField("Subkeys", RegistrySubkeys)
    byte_runs = fields.TypedField("Byte_Runs", ByteRuns)

