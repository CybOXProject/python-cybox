# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_service_object as win_service_binding
from cybox.common import HashList
from cybox.objects.win_process_object import WinProcess
from cybox.common import ObjectProperties, String

class ServiceDescriptionList(cybox.EntityList):
    _binding = win_service_binding
    _binding_class = win_service_binding.ServiceDescriptionListType
    _binding_var = "Description"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinServiceObject-2"

class WinService(WinProcess):
    _binding = win_service_binding
    _binding_class = win_service_binding.WindowsServiceObjectType
    _namespace = "http://cybox.mitre.org/objects#WinServiceObject-2"
    _XSI_NS = "WinServiceObj"
    _XSI_TYPE = "WindowsServiceObjectType"

    service_dll_signature_exists = cybox.TypedField("service_dll_signature_exists")
    service_dll_signature_verified = cybox.TypedField("service_dll_signature_verified")
    description_list = cybox.TypedField("Description_List", ServiceDescriptionList)
    display_name = cybox.TypedField("Display_Name", String)
    group_name = cybox.TypedField("Group_Name", String)
    service_name = cybox.TypedField("Service_Name", String)
    service_dll = cybox.TypedField("Service_DLL", String)
    service_dll_certificate_issuer = cybox.TypedField("Service_DLL_Certificate_Issuer", String)
    service_dll_certificate_subject = cybox.TypedField("Service_DLL_Certificate_Subject", String)
    service_dll_hashes = cybox.TypedField("Service_DLL_Hashes", HashList)
    service_dll_signature_description = cybox.TypedField("Service_DLL_Signature_Description", String)
    startup_command_line = cybox.TypedField("Startup_Command_Line", String)
    startup_type = cybox.TypedField("Startup_Type", String)
    service_status = cybox.TypedField("Service_Status", String)
    service_type = cybox.TypedField("Service_Type", String)
    started_as = cybox.TypedField("Started_As", String)
