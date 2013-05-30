# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.win_kernel_hook_object as win_kernel_hook_binding
from cybox.common.digitalsignature import DigitalSignature
from cybox.common import ObjectProperties, String, UnsignedLong

class WinKernelHook(ObjectProperties):
    _XSI_NS = "WinKernelHookObj"
    _XSI_TYPE = "WindowsKernelHookObjectType"

    def __init__(self):
        super(WinKernelHook, self).__init__()
        self.digital_signature_hooking = None
        self.digital_signature_hooked = None
        self.hooking_address = None
        self.hook_description = None
        self.hooked_function = None
        self.hooked_module = None
        self.hooking_module = None
        self.type = None

    def to_obj(self):
        win_kernel_hook_obj = win_kernel_hook_binding.WindowsKernelHookObjectType()
        super(WinKernelHook, self).to_obj(win_kernel_hook_obj)

        if self.digital_signature_hooking is not None: win_kernel_hook_obj.set_Digital_Signature_Hooking(self.digital_signature_hooking.to_obj())
        if self.digital_signature_hooked is not None: win_kernel_hook_obj.set_Digital_Signature_Hooked(self.digital_signature_hooked.to_obj())
        if self.hooked_address is not None: win_kernel_hook_obj.set_Hooked_Address(self.hooked_address.to_obj())
        if self.hook_description is not None: win_kernel_hook_obj.set_Hook_Description(self.hook_description.to_obj())
        if self.hooked_function is not None: win_kernel_hook_obj.set_Hooked_Function(self.hooked_function.to_obj())
        if self.hooked_module is not None: win_kernel_hook_obj.set_Hooked_Module(self.hooked_module.to_obj())
        if self.hooking_module is not None: win_kernel_hook_obj.set_Hooking_Module(self.hooking_module.to_obj())
        if self.type is not None: win_kernel_hook_obj.set_Type(self.type.to_obj())

        return win_kernel_hook_obj

    def to_dict(self):
        win_kernel_hook_dict = {}
        super(WinKernelHook, self).to_dict(win_kernel_hook_dict)

        if self.digital_signature_hooking is not None: win_kernel_hook_dict['digital_signature_hooking'] = self.digital_signature_hooking.to_dict()
        if self.digital_signature_hooked is not None: win_kernel_hook_dict['digital_signature_hooked'] = self.digital_signature_hooked.to_dict()
        if self.hooked_address is not None: win_kernel_hook_dict['hooked_address'] = self.hooked_address.to_dict()
        if self.hook_description is not None: win_kernel_hook_dict['hook_description'] = self.hook_description.to_dict()
        if self.hooked_function is not None: win_kernel_hook_dict['hooked_function'] = self.hooked_function.to_dict()
        if self.hooked_module is not None: win_kernel_hook_dict['hooked_module'] = self.hooked_module.to_dict()
        if self.hooking_module is not None: win_kernel_hook_dict['hooking_module'] = self.hooking_module.to_dict()
        if self.type is not None: win_kernel_hook_dict['type'] = self.type.to_dict()

        return win_kernel_hook_dict

    @staticmethod
    def from_dict(win_kernel_hook_dict):
        if not win_kernel_hook_dict:
            return None

        win_kernel_hook_ = WinKernelHook()
        win_kernel_hook_.digital_signature_hooking = DigitalSignature.from_dict(win_kernel_hook_dict.get('digital_signature_hooking'))
        win_kernel_hook_.digital_signature_hooked = DigitalSignature.from_dict(win_kernel_hook_dict.get('digital_signature_hooked'))
        win_kernel_hook_.hooked_address = UnsignedLong.from_dict(win_kernel_hook_dict.get('hooked_address'))
        win_kernel_hook_.hook_description = String.from_dict(win_kernel_hook_dict.get('hook_description'))
        win_kernel_hook_.hooked_function = String.from_dict(win_kernel_hook_dict.get('hooked_function'))
        win_kernel_hook_.hooked_module = String.from_dict(win_kernel_hook_dict.get('hooked_module'))
        win_kernel_hook_.type = String.from_dict(win_kernel_hook_dict.get('type'))

        return win_kernel_hook_

    @staticmethod
    def from_obj(win_kernel_hook_obj):
        if not win_kernel_hook_obj:
            return None

        win_kernel_hook_ = WinKernelHook()
        win_kernel_hook_.digital_signature_hooking = DigitalSignature.from_obj(win_kernel_hook_obj.get_Digital_Signature_Hooking())
        win_kernel_hook_.digital_signature_hooked = DigitalSignature.from_obj(win_kernel_hook_obj.get_Digital_Signature_Hooked())
        win_kernel_hook_.hooked_address = UnsignedLong.from_obj(win_kernel_hook_obj.get_Hooked_Address())
        win_kernel_hook_.hook_description = String.from_obj(win_kernel_hook_obj.get_Hook_Description())
        win_kernel_hook_.hooked_function = String.from_obj(win_kernel_hook_obj.get_Hooked_Function())
        win_kernel_hook_.hooked_module = String.from_dict(win_kernel_hook_obj.get_Hooked_Module())
        win_kernel_hook_.type = String.from_obj(win_kernel_hook_obj.get_Type())

        return win_kernel_hook_
