# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_system_object as win_system_binding
from cybox.objects.system_object import System
from cybox.objects.win_handle_object import WinHandleList
from cybox.common import String, HexBinary


class GlobalFlag(cybox.Entity):
    _binding = win_system_binding
    _binding_class = win_system_binding.GlobalFlagType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"

    abbreviation = cybox.TypedField("Abbreviation", String)
    destination = cybox.TypedField("Destination", String)
    hexadecimal_value = cybox.TypedField("Hexadecimal_Value", HexBinary)
    symbolic_name = cybox.TypedField("Symbolic_Name", String)


class GlobalFlagList(cybox.EntityList):
    _binding = win_system_binding
    _binding_class = win_system_binding.GlobalFlagListType
    _binding_var = "Global_Flag"
    _contained_type = GlobalFlag
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"


class WinSystem(System):
    _binding = win_system_binding
    _binding_class = win_system_binding.WindowsSystemObjectType
    _namespace = "http://cybox.mitre.org/objects#WinSystemObject-2"
    _XSI_NS = "WinSystemObj"
    _XSI_TYPE = "WindowsSystemObjectType"

    domain = cybox.TypedField("Domain", String, multiple=True)
    global_flag_list = cybox.TypedField("Global_Flag_List", GlobalFlagList)
    netbios_name = cybox.TypedField("NetBIOS_Name", String)
    open_handle_list = cybox.TypedField("Open_Handle_List", WinHandleList)
    product_id = cybox.TypedField("Product_ID", String)
    product_name = cybox.TypedField("Product_Name", String)
    registered_organization = cybox.TypedField("Registered_Organization", String)
    registered_owner = cybox.TypedField("Registered_Owner", String)
    windows_directory = cybox.TypedField("Windows_Directory", String)
    windows_system_directory = cybox.TypedField("Windows_System_Directory", String)
    windows_temp_directory = cybox.TypedField("Windows_Temp_Directory", String)
