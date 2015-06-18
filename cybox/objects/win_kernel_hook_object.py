# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_kernel_hook_object as win_kernel_hook_binding
from cybox.common import (DigitalSignature, ObjectProperties, String,
        UnsignedLong)


class WinKernelHook(ObjectProperties):
    _binding = win_kernel_hook_binding
    _binding_class = win_kernel_hook_binding.WindowsKernelHookObjectType
    _namespace = "http://cybox.mitre.org/objects#WinKernelHookObject-2"
    _XSI_NS = "WinKernelHookObj"
    _XSI_TYPE = "WindowsKernelHookObjectType"

    digital_signature_hooking = fields.TypedField("Digital_Signature_Hooking",
                                                 DigitalSignature)
    digital_signature_hooked = fields.TypedField("Digital_Signature_Hooked",
                                                DigitalSignature)
    hooking_address = fields.TypedField("Hooking_Address", UnsignedLong)
    hook_description = fields.TypedField("Hook_Description", String)
    hooked_function = fields.TypedField("Hooked_Function", String)
    hooked_module = fields.TypedField("Hooked_Module", String)
    hooking_module = fields.TypedField("Hooking_Module", String)
    type_ = fields.TypedField("Type", String)
