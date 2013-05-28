# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_service_object as win_service_binding
from cybox.common import HashList
from cybox.objects.win_process_object import WinProcess
from cybox.common import ObjectProperties, String

class WinService(WinProcess):
    _XSI_NS = "WinServiceObj"
    _XSI_TYPE = "WindowsServiceObjectType"
    superclass = WinProcess

    def __init__(self):
        super(WinService, self).__init__()
        self.service_dll_signature_exists = None
        self.service_dll_signature_verified = None
        self.description_list = []
        self.display_name = None
        self.group_name = None
        self.service_name = None
        self.service_dll = None
        self.service_dll_certificate_issuer = None
        self.service_dll_certificate_subject = None
        self.service_dll_hashes = None
        self.service_dll_signature_description = None
        self.startup_command_line = None
        self.startup_type = None
        self.service_status = None
        self.service_type = None
        self.started_as = None

    def to_obj(self):
        win_service_obj = super(WinService, self).to_obj(win_service_binding.WindowsServiceObjectType())

        if self.service_dll_signature_exists is not None: win_service_obj.set_service_dll_signature_exists(self.service_dll_signature_exists)
        if self.service_dll_signature_verified is not None: win_service_obj.set_service_dll_signature_verified(self.service_dll_signature_verified)
        if len(self.description_list) > 0: 
            description_list_obj = win_service_binding.ServiceDescriptionListType()
            for description in self.description_list:
                description_list_obj.add_Description(description.to_obj())
            win_service_obj.set_Description_List(description_list_obj)
        if self.display_name is not None: win_service_obj.set_Display_Name(self.display_name.to_obj())
        if self.group_name is not None: win_service_obj.set_Group_Name(self.group_name.to_obj())
        if self.service_name is not None: win_service_obj.set_Service_Name(self.service_name.to_obj())
        if self.service_dll is not None: win_service_obj.set_Service_DLL(self.service_dll.to_obj())
        if self.service_dll_certificate_issuer is not None: win_service_obj.set_Service_DLL_Certificate_Issuer(self.service_dll_certificate_issuer.to_obj())
        if self.service_dll_certificate_subject is not None: win_service_obj.set_Service_DLL_Certificate_Subject(self.service_dll_certificate_subject.to_obj())
        if self.service_dll_hashes is not None: win_service_obj.set_Service_DLL_Hashes(self.service_dll_hashes.to_obj())
        if self.service_dll_signature_description is not None: win_service_obj.set_Service_DLL_Signature_Description(self.service_dll_signature_description.to_obj())
        if self.startup_command_line is not None: win_service_obj.set_Startup_Command_Line(self.startup_command_line.to_obj())
        if self.startup_type is not None: win_service_obj.set_Startup_Type(self.startup_type.to_obj())
        if self.service_status is not None: win_service_obj.set_Service_Status(self.service_status.to_obj())
        if self.service_type is not None: win_service_obj.set_Service_Type(self.service_type.to_obj())
        if self.started_as is not None: win_service_obj.set_Started_As(self.started_as.to_obj())

        return win_service_obj

    def to_dict(self):
        win_service_dict = super(WinService, self).to_dict()

        if self.service_dll_signature_exists is not None: win_service_dict['service_dll_signature_exists'] = self.service_dll_signature_exists
        if self.service_dll_signature_verified is not None: win_service_dict['service_dll_signature_verified'] = self.service_dll_signature_verified
        if self.description_list is not None: win_service_dict['description_list'] = [x.to_dict() for x in self.description_list]
        if self.display_name is not None: win_service_dict['display_name'] = self.display_name.to_dict()
        if self.group_name is not None: win_service_dict['group_name'] = self.group_name.to_dict()
        if self.service_name is not None: win_service_dict['service_name'] = self.service_name.to_dict()
        if self.service_dll is not None: win_service_dict['service_dll'] = self.service_dll.to_dict()
        if self.service_dll_certificate_issuer is not None: win_service_dict['service_dll_certificate_issuer'] = self.service_dll_certificate_issuer.to_dict()
        if self.service_dll_certificate_subject is not None: win_service_dict['service_dll_certificate_subject'] = self.service_dll_certificate_subject.to_dict()
        if self.service_dll_hashes is not None: win_service_dict['service_dll_hashes'] = self.service_dll_hashes.to_list()
        if self.service_dll_signature_description is not None: win_service_dict['service_dll_signature_description'] = self.service_dll_signature_description.to_dict()
        if self.startup_command_line is not None: win_service_dict['startup_command_line'] = self.startup_command_line.to_dict()
        if self.startup_type is not None: win_service_dict['startup_type'] = self.startup_type.to_dict()
        if self.service_status is not None: win_service_dict['service_status'] = self.service_status.to_dict()
        if self.service_type is not None: win_service_dict['service_type'] = self.service_type.to_dict()
        if self.started_as is not None: win_service_dict['started_as'] = self.started_as.to_dict()
        win_service_dict['xsi:type'] = self._XSI_TYPE

        return win_service_dict
        
    @staticmethod
    def from_dict(win_service_dict):
        if not win_service_dict:
            return None

        win_service_ = WinProcess.from_dict(win_service_dict, WinService())
        win_service_.service_dll_signature_exists = win_service_dict.get('service_dll_signature_exists')
        win_service_.service_dll_signature_verified = win_service_dict.get('service_dll_signature_verified')
        win_service_.description_list = [String.from_dict(x) for x in win_service_dict.get('description_list', [])]
        win_service_.display_name = String.from_dict(win_service_dict.get('display_name'))
        win_service_.group_name = String.from_dict(win_service_dict.get('group_name'))
        win_service_.service_name = String.from_dict(win_service_dict.get('service_name'))
        win_service_.service_dll = String.from_dict(win_service_dict.get('service_dll'))
        win_service_.service_dll_certificate_issuer = String.from_dict(win_service_dict.get('service_dll_certificate_issuer'))
        win_service_.service_dll_certificate_subject = String.from_dict(win_service_dict.get('service_dll_certificate_subject'))
        win_service_.service_dll_hashes = HashList.from_list(win_service_dict.get('service_dll_hashes'))
        win_service_.service_dll_signature_description = String.from_dict(win_service_dict.get('service_dll_signature_description'))
        win_service_.startup_command_line = String.from_dict(win_service_dict.get('startup_command_line'))
        win_service_.startup_type = String.from_dict(win_service_dict.get('startup_type'))
        win_service_.service_status = String.from_dict(win_service_dict.get('service_status'))
        win_service_.service_type = String.from_dict(win_service_dict.get('service_type'))
        win_service_.started_as = String.from_dict(win_service_dict.get('started_as'))

        return win_service_

    @staticmethod
    def from_obj(win_service_obj):
        if not win_service_obj:
            return None

        win_service_ = WinProcess.from_obj(win_service_obj, WinService())
        win_service_.service_dll_signature_exists = win_service_obj.get_service_dll_signature_exists()
        win_service_.service_dll_signature_verified = win_service_obj.get_service_dll_signature_verified()
        if win_service_obj.get_Description_List() is not None:
            win_service_.description_list = [String.from_obj(x) for x in win_service_obj.get_Description_List().get_Description()]
        win_service_.display_name = String.from_obj(win_service_obj.get_Display_Name())
        win_service_.group_name = String.from_obj(win_service_obj.get_Group_Name())
        win_service_.service_name = String.from_obj(win_service_obj.get_Service_Name())
        win_service_.service_dll = String.from_obj(win_service_obj.get_Service_DLL())
        win_service_.service_dll_certificate_issuer = String.from_obj(win_service_obj.get_Service_DLL_Certificate_Issuer())
        win_service_.service_dll_certificate_subject = String.from_obj(win_service_obj.get_Service_DLL_Certificate_Subject())
        win_service_.service_dll_hashes = HashList.from_obj(win_service_obj.get_Service_DLL_Hashes())
        win_service_.service_dll_signature_description = String.from_obj(win_service_obj.get_Service_DLL_Signature_Description())
        win_service_.startup_command_line = String.from_obj(win_service_obj.get_Startup_Command_Line())
        win_service_.startup_type = String.from_obj(win_service_obj.get_Startup_Type())
        win_service_.service_status = String.from_obj(win_service_obj.get_Service_Status())
        win_service_.service_type = String.from_obj(win_service_obj.get_Service_Type())
        win_service_.started_as = String.from_obj(win_service_obj.get_Started_As())

        return win_service_
