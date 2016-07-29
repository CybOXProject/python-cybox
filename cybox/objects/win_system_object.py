# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_system_object as win_system_binding
from cybox.objects.system_object import System
from cybox.objects.win_handle_object import WinHandleList
from cybox.common import String, HexBinary


class GlobalFlag(entities.Entity):
    _binding = win_system_binding
    _binding_class = win_system_binding.GlobalFlagType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"

    abbreviation = fields.TypedField("Abbreviation", String)
    destination = fields.TypedField("Destination", String)
    hexadecimal_value = fields.TypedField("Hexadecimal_Value", HexBinary)
    symbolic_name = fields.TypedField("Symbolic_Name", String)


class GlobalFlagList(entities.EntityList):
    _binding = win_system_binding
    _binding_class = win_system_binding.GlobalFlagListType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"
    global_flag = fields.TypedField("Global_Flag", GlobalFlag, multiple=True)


class WinSystem(System):
    _binding = win_system_binding
    _binding_class = win_system_binding.WindowsSystemObjectType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"
    _XSI_NS = "WinSystemObj"
    _XSI_TYPE = "WindowsSystemObjectType"

    domain = fields.TypedField("Domain", String, multiple=True)
    global_flag_list = fields.TypedField("Global_Flag_List", GlobalFlagList)
    netbios_name = fields.TypedField("NetBIOS_Name", String)
    open_handle_list = fields.TypedField("Open_Handle_List", WinHandleList)
    product_id = fields.TypedField("Product_ID", String)
    product_name = fields.TypedField("Product_Name", String)
    registered_organization = fields.TypedField("Registered_Organization", String)
    registered_owner = fields.TypedField("Registered_Owner", String)
    windows_directory = fields.TypedField("Windows_Directory", String)
    windows_system_directory = fields.TypedField("Windows_System_Directory", String)
    windows_temp_directory = fields.TypedField("Windows_Temp_Directory", String)
