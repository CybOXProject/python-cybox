# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_service_object as win_service_binding
from cybox.common import HashList
from cybox.objects.win_process_object import WinProcess
from cybox.common import ObjectProperties, String


class ServiceDescriptionList(entities.EntityList):
    _binding = win_service_binding
    _binding_class = win_service_binding.ServiceDescriptionListType
    _namespace = "http://cybox.mitre.org/objects#WinServiceObject-2"
    description = fields.TypedField("Description", String, multiple=True)


class WinService(WinProcess):
    _binding = win_service_binding
    _binding_class = win_service_binding.WindowsServiceObjectType
    _namespace = "http://cybox.mitre.org/objects#WinServiceObject-2"
    _XSI_NS = "WinServiceObj"
    _XSI_TYPE = "WindowsServiceObjectType"

    service_dll_signature_exists = fields.TypedField("service_dll_signature_exists")
    service_dll_signature_verified = fields.TypedField("service_dll_signature_verified")
    description_list = fields.TypedField("Description_List", ServiceDescriptionList)
    display_name = fields.TypedField("Display_Name", String)
    group_name = fields.TypedField("Group_Name", String)
    service_name = fields.TypedField("Service_Name", String)
    service_dll = fields.TypedField("Service_DLL", String)
    service_dll_certificate_issuer = fields.TypedField("Service_DLL_Certificate_Issuer", String)
    service_dll_certificate_subject = fields.TypedField("Service_DLL_Certificate_Subject", String)
    service_dll_hashes = fields.TypedField("Service_DLL_Hashes", HashList)
    service_dll_signature_description = fields.TypedField("Service_DLL_Signature_Description", String)
    startup_command_line = fields.TypedField("Startup_Command_Line", String)
    startup_type = fields.TypedField("Startup_Type", String)
    service_status = fields.TypedField("Service_Status", String)
    service_type = fields.TypedField("Service_Type", String)
    started_as = fields.TypedField("Started_As", String)
