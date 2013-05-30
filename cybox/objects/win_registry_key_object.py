# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_registry_key_object as win_registry_key_binding

from cybox.common import ObjectProperties, String, DateTime, UnsignedInteger, ByteRuns
from cybox.objects.win_handle_object import WinHandleList

class WinRegistryKey(ObjectProperties):
    _XSI_NS = "WinRegistryKeyObj"
    _XSI_TYPE = "WindowsRegistryKeyObjectType"

    def __init__(self):
        super(WinRegistryKey, self).__init__()
        self.key = None
        self.hive = None
        self.number_values = None
        self.values = []
        self.modified_time = None
        self.creator_username = None
        self.handle_list = WinHandleList()
        self.number_subkeys = None
        self.subkeys = []
        self.byte_runs = ByteRuns()

    def to_obj(self):
        registry_key_obj = win_registry_key_binding.WindowsRegistryKeyObjectType()
        super(WinRegistryKey, self).to_obj(registry_key_obj)

        if self.key is not None: registry_key_obj.set_Key(self.key.to_obj())
        if self.hive is not None: registry_key_obj.set_Hive(self.hive.to_obj())
        if self.number_values is not None: registry_key_obj.set_Number_Values(self.number_values.to_obj())
        if len(self.values) > 0: 
            values_obj = win_registry_key_binding.RegistryValuesType()
            for value in self.values:
                values_obj.add_Value(value.to_obj())
            registry_key_obj.set_Values(values_obj)
        if self.modified_time is not None: registry_key_obj.set_Modified_Time(self.modified_time.to_obj())
        if self.creator_username is not None: registry_key_obj.set_Creator_Username(self.creator_username.to_obj())
        if self.handle_list is not None: registry_key_obj.set_Handle_List(self.handle_list.to_obj())
        if self.number_subkeys is not None: registry_key_obj.set_Number_Subkeys(self.number_subkeys.to_obj())
        if len(self.subkeys) > 0: 
            subkeys_obj = win_registry_key_binding.RegistrySubkeysType()
            for subkey in self.subkeys:
                subkeys_obj.add_Subkey(subkey.to_obj())
            registry_key_obj.set_Subkeys(subkeys_obj)
        #if self.byte_runs is not None: registry_key_obj.set_Byte_Runs(self.byte_runs.to_obj())

        return registry_key_obj

    def to_dict(self):
        registry_key_dict = {}
        super(WinRegistryKey, self).to_dict(registry_key_dict)

        if self.key is not None: registry_key_dict['key'] = self.key.to_dict()
        if self.hive is not None: registry_key_dict['hive'] = self.hive.to_dict()
        if self.number_values is not None: registry_key_dict['number_values'] = self.number_values.to_dict()
        if len(self.values) > 0: 
            values_list = []
            for value in self.values:
                values_list.append(value.to_dict())
            registry_key_dict['values'] = values_list
        if self.modified_time is not None: registry_key_dict['modified_time'] = self.modified_time.to_dict()
        if self.creator_username is not None: registry_key_dict['creator_username'] = self.creator_username.to_dict()
        if self.handle_list is not None: registry_key_dict['handle_list'] = self.handle_list.to_dict()
        if self.number_subkeys is not None: registry_key_dict['number_subkeys'] = self.number_subkeys.to_dict()
        if len(self.subkeys) > 0: 
            subkeys_list = []
            for subkey in self.subkeys:
                subkeys_list.append(subkey.to_dict())
            registry_key_dict['subkeys'] = subkeys_list
        #if self.byte_runs is not None: registry_key_dict['byte_runs'] = self.byte_runs.to_dict()


        return registry_key_dict 
        
    @staticmethod
    def from_dict(registry_key_dict):
        if not registry_key_dict:
            return None
        
        win_registry_key_ = WinRegistryKey()
        win_registry_key_.key = String.from_dict(registry_key_dict.get('key'))
        win_registry_key_.hive = String.from_dict(registry_key_dict.get('hive'))
        win_registry_key_.number_values = UnsignedInteger.from_dict(registry_key_dict.get('number_values'))
        win_registry_key_.modified_time = DateTime.from_dict(registry_key_dict.get('modified_time'))
        win_registry_key_.creator_username = String.from_dict(registry_key_dict.get('creator_username'))
        win_registry_key_.handle_list = WinHandleList.from_list(registry_key_dict.get('handle_list'))
        win_registry_key_.number_subkeys = UnsignedInteger.from_dict(registry_key_dict.get('number_subkeys'))
        #win_registry_key_.byte_runs = ByteRuns.from_dict(registry_key_dict.get('byte_runs'))

        if registry_key_dict.get('values') is not None:
            for registry_value_dict in registry_key_dict.get('values'):
                win_registry_key_.values.append(RegistryValue.from_dict(registry_value_dict))
        if registry_key_dict.get('subkeys') is not None:
            for registry_subkey_dict in registry_key_dict.get('subkeys'):
                win_registry_key_.subkeys.append(WinRegistryKey.from_dict(registry_subkey_dict))

        return win_registry_key_

    @staticmethod
    def from_obj(registry_key_obj):
        if not registry_key_obj:
            return None

        win_registry_key_ = WinRegistryKey()
        win_registry_key_.key = String.from_obj(registry_key_obj.get_Key())
        win_registry_key_.hive = String.from_obj(registry_key_obj.get_Hive())
        win_registry_key_.number_values = UnsignedInteger.from_obj(registry_key_obj.get_Number_Values())
        win_registry_key_.modified_time = DateTime.from_obj(registry_key_obj.get_Modified_Time())
        win_registry_key_.creator_username = String.from_obj(registry_key_obj.get_Creator_Username())
        win_registry_key_.handle_list = WinHandleList.from_obj(registry_key_obj.get_Handle_List())
        win_registry_key_.number_subkeys = UnsignedInteger.from_obj(registry_key_obj.get_Number_Subkeys())
        #win_registry_key_.byte_runs = ByteRuns.from_obj(registry_key_obj.get_Byte_Runs())

        if registry_key_obj.get_Values() is not None:
            for registry_value_obj in registry_key_obj.get_Values().get_Value():
                win_registry_key_.values.append(RegistryValue.from_obj(registry_value_obj))
        if registry_key_obj.get_Subkeys() is not None:
            for registry_subkey_obj in registry_key_dict.get_Subkeys().get_Subkey():
                win_registry_key_.subkeys.append(WinRegistryKey.from_obj(registry_subkey_obj))

        return win_registry_key_

class RegistryValue(cybox.Entity):

    def __init__(self):
        super(RegistryValue, self).__init__()
        self.name = None
        self.data = None
        self.datatype = None
        self.byte_runs = None

    def to_obj(self):
        registry_value_obj = win_registry_key_binding.RegistryValueType()

        if self.name is not None: registry_value_obj.set_Name(self.name.to_obj())
        if self.data is not None: registry_value_obj.set_Data(self.data.to_obj())
        if self.datatype is not None: registry_value_obj.set_Datatype(self.datatype.to_obj())
        #if self.byte_runs is not None: registry_value_obj.set_Byte_Runs(self.byte_runs.to_obj())

        return registry_value_obj

    def to_dict(self):
        registry_value_dict = {}

        if self.name is not None: registry_value_dict['name'] = self.name.to_dict()
        if self.data is not None: registry_value_dict['data'] = self.data.to_dict()
        if self.datatype is not None: registry_value_dict['datatype'] = self.datatype.to_dict()
        #if self.byte_runs is not None: registry_value_dict['byte_runs'] = self.byte_runs.to_dict()

        return registry_value_dict

    @staticmethod
    def from_obj(registry_value_obj):
        if not registry_value_obj:
            return None

        registry_value_ = RegistryValue()
        registry_value_.name = String.from_obj(registry_value_obj.get_Name())
        registry_value_.data = String.from_obj(registry_value_obj.get_Data())
        registry_value_.datatype = String.from_obj(registry_value_obj.get_Datatype())
        #registry_value_.byte_runs = ByteRuns.from_obj(registry_value_obj.get_Byte_Runs())

        return registry_value_

    @staticmethod
    def from_dict(registry_value_dict):
        if not registry_value_dict:
            return None

        registry_value_ = RegistryValue()
        registry_value_.name = String.from_dict(registry_value_dict.get('name'))
        registry_value_.data = String.from_dict(registry_value_dict.get('data'))
        registry_value_.datatype = String.from_dict(registry_value_dict.get('datatype'))
        #registry_value_.byte_runs = ByteRuns.from_dict(registry_value_dict.get('byte_runs'))

        return registry_value_
