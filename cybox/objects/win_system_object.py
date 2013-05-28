# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_system_object as win_system_binding
from cybox.objects.system_object import System
from cybox.objects.win_handle_object import WinHandleList
from cybox.common import ObjectProperties, String, HexBinary

class WinSystem(System):
    _XSI_NS = "WinSystemObj"
    _XSI_TYPE = "WindowsSystemObjectType"

    def __init__(self):
        super(WinSystem, self).__init__()
        self.domains = []
        self.global_flag_list = None
        self.netbios_name = None
        self.open_handle_list = None
        self.product_id = None
        self.product_name = None
        self.registered_organization = None
        self.registered_owner = None
        self.windows_directory = None
        self.windows_system_directory = None
        self.windows_temp_directory = None

    def to_obj(self):
        win_system_obj = super(WinSystem,self).to_obj(win_system_binding.WindowsSystemObjectType())
        
        if self.global_flag_list is not None : win_system_obj.set_Global_Flag_List(self.global_flag_list.to_obj())
        if self.netbios_name is not None : win_system_obj.set_NetBIOS_Name(self.netbios_name.to_obj())
        if self.open_handle_list is not None : win_system_obj.set_Open_Handle_List(self.open_handle_list.to_obj())
        if self.product_id is not None : win_system_obj.set_Product_ID(self.product_id.to_obj())
        if self.product_name is not None : win_system_obj.set_Product_Name(self.product_name.to_obj())
        if self.registered_organization is not None : win_system_obj.set_Registered_Organization(self.registered_organization.to_obj())
        if self.registered_owner is not None : win_system_obj.set_Registered_Owner(self.registered_owner.to_obj())
        if self.windows_directory is not None : win_system_obj.set_Windows_Directory(self.windows_directory.to_obj())
        if self.windows_system_directory is not None : win_system_obj.set_Windows_System_Directory(self.windows_system_directory.to_obj())
        if self.windows_temp_directory is not None : win_system_obj.set_Windows_Temp_Directory(self.windows_temp_directory.to_obj())
        if len(self.domains) > 0:
            for domain in self.domains:
                win_system_obj.add_Domain(domain.to_obj())
        return win_system_obj

    def to_dict(self):
        win_system_dict = super(WinSystem, self).to_dict()
        if self.global_flag_list is not None : win_system_dict['global_flag_list'] = self.global_flag_list.to_list()
        if self.netbios_name is not None : win_system_dict['netbios_name'] = self.netbios_name.to_dict()
        if self.open_handle_list is not None : win_system_dict['open_handle_list'] = self.open_handle_list.to_list()
        if self.product_id is not None : win_system_dict['product_id'] = self.product_id.to_dict()
        if self.product_name is not None : win_system_dict['product_name'] = self.product_name.to_dict()
        if self.registered_organization is not None : win_system_dict['registered_organization'] = self.registered_organization.to_dict()
        if self.registered_owner is not None : win_system_dict['registered_owner'] = self.registered_owner.to_dict()
        if self.windows_directory is not None : win_system_dict['windows_directory'] = self.windows_directory.to_dict()
        if self.windows_system_directory is not None : win_system_dict['windows_system_directory'] = self.windows_system_directory.to_dict()
        if self.windows_temp_directory is not None : win_system_dict['windows_temp_directory'] = self.windows_temp_directory.to_dict()
        if len(self.domains) > 0:
            domain_list = []
            for domain in self.domains:
                domain_list.append(domain.to_dict())
            win_system_dict['domains'] = domain_list
        return win_system_dict

    @staticmethod
    def from_dict(win_system_dict):
        if not win_system_dict:
            return None
        win_system_ = System.from_dict(win_system_dict, WinSystem())
        win_system_.domains = [String.from_dict(x) for x in win_system_dict.get('domains', [])]
        win_system_.global_flag_list = GlobalFlagList.from_list(win_system_dict.get('global_flag_list'))
        win_system_.netbios_name = String.from_dict(win_system_dict.get('netbios_name'))
        win_system_.open_handle_list = WinHandleList.from_list(win_system_dict.get('open_handle_list'))
        win_system_.product_id = String.from_dict(win_system_dict.get('product_id'))
        win_system_.product_name = String.from_dict(win_system_dict.get('product_name'))
        win_system_.registered_organization = String.from_dict(win_system_dict.get('registered_organization'))
        win_system_.registered_owner = String.from_dict(win_system_dict.get('registered_owner'))
        win_system_.windows_directory = String.from_dict(win_system_dict.get('windows_directory'))
        win_system_.windows_system_directory = String.from_dict(win_system_dict.get('windows_system_directory'))
        win_system_.windows_temp_directory = String.from_dict(win_system_dict.get('windows_temp_directory'))
        return win_system_

    @staticmethod
    def from_obj(win_system_obj):
        if not win_system_obj:
            return None
        win_system_ = System.from_obj(win_system_obj, WinSystem())
        win_system_.domains = [String.from_obj(x) for x in win_system_obj.get_Domain()]
        win_system_.global_flag_list = GlobalFlagList.from_obj(win_system_obj.get_Global_Flag_List())
        win_system_.netbios_name = String.from_obj(win_system_obj.get_NetBIOS_Name())
        win_system_.open_handle_list = WinHandleList.from_obj(win_system_obj.get_Open_Handle_List())
        win_system_.product_id = String.from_obj(win_system_obj.get_Product_ID())
        win_system_.product_name = String.from_obj(win_system_obj.get_Product_Name())
        win_system_.registered_organization = String.from_obj(win_system_obj.get_Registered_Organization())
        win_system_.registered_owner = String.from_obj(win_system_obj.get_Registered_Owner())
        win_system_.windows_directory = String.from_obj(win_system_obj.get_Windows_Directory())
        win_system_.windows_system_directory = String.from_obj(win_system_obj.get_Windows_System_Directory())
        win_system_.windows_temp_directory = String.from_obj(win_system_obj.get_Windows_Temp_Directory())
        return win_system_

class GlobalFlag(cybox.Entity):
    def __init__(self):
        super(GlobalFlag, self).__init__()
        self.abbreviation = None
        self.destination = None
        self.hexadecimal_value = None
        self.symbolic_name = None

    def to_obj(self):
        global_flag_obj = win_system_binding.GlobalFlagType()
        if self.abbreviation is not None : global_flag_obj.set_Abbreviation(self.abbreviation.to_obj())
        if self.destination is not None : global_flag_obj.set_Destination(self.destination.to_obj())
        if self.hexadecimal_value is not None : global_flag_obj.set_Hexadecimal_Value(self.hexadecimal_value.to_obj())
        if self.symbolic_name is not None : global_flag_obj.set_Symbolic_Name(self.symbolic_name.to_obj())
        return global_flag_obj

    def to_dict(self):
        global_flag_dict = win_system_binding.GlobalFlagType()
        if self.abbreviation is not None : global_flag_dict['abbreviation'] = self.abbreviation.to_dict()
        if self.destination is not None : global_flag_dict['destination'] = self.destination.to_dict()
        if self.hexadecimal_value is not None : global_flag_dict['hexadecimal_value'] = self.hexadecimal_value.to_dict()
        if self.symbolic_name is not None : global_flag_dict['symbolic_name'] = self.symbolic_name.to_dict()
        return global_flag_dict

    @staticmethod
    def from_dict(global_flag_dict):
        if not global_flag_dict:
            return None
        global_flag_ = GlobalFlag()
        global_flag_.abbreviation = String.from_dict(global_flag_dict.get('abbreviation'))
        global_flag_.destination = String.from_dict(global_flag_dict.get('destination'))
        global_flag_.hexadecimal_value = HexBinary.from_dict(global_flag_dict.get('hexadecimal_value'))
        global_flag_.symbolic_name = String.from_dict(global_flag_dict.get('symbolic_name'))
        return global_flag_

    @staticmethod
    def from_obj(global_flag_obj):
        if not global_flag_obj:
            return None
        global_flag_ = GlobalFlag()
        global_flag_.abbreviation = String.from_obj(global_flag_obj.get_Abbreviation())
        global_flag_.destination = String.from_obj(global_flag_obj.get_Destination())
        global_flag_.hexadecimal_value = HexBinary.from_obj(global_flag_obj.get_Hexadecimal_Value())
        global_flag_.symbolic_name = String.from_obj(global_flag_obj.get_Symbolic_Name())
        return global_flag_

class GlobalFlagList(cybox.EntityList):
    _contained_type = GlobalFlag
    _binding_class = win_system_binding.GlobalFlagListType

    def __init__(self):
        super(GlobalFlagList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Global_Flag(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Global_Flag()
