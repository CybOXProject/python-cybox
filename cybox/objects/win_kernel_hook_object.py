# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_kernel_hook_object as win_kernel_hook_binding
from cybox.common import (DigitalSignature, ObjectProperties, String,
        UnsignedLong)


class WinKernelHook(ObjectProperties):
    _binding = win_kernel_hook_binding
    _binding_class = win_kernel_hook_binding.WindowsKernelHookObjectType
    _namespace = "http://cybox.mitre.org/objects#WinKernelHookObject-2"
    _XSI_NS = "WinKernelHookObj"
    _XSI_TYPE = "WindowsKernelHookObjectType"

    digital_signature_hooking = cybox.TypedField("Digital_Signature_Hooking",
                                                 DigitalSignature)
    digital_signature_hooked = cybox.TypedField("Digital_Signature_Hooked",
                                                DigitalSignature)
    hooking_address = cybox.TypedField("Hooking_Address", UnsignedLong)
    hook_description = cybox.TypedField("Hook_Description", String)
    hooked_function = cybox.TypedField("Hooked_Function", String)
    hooked_module = cybox.TypedField("Hooked_Module", String)
    hooking_module = cybox.TypedField("Hooking_Module", String)
    type_ = cybox.TypedField("Type", String)
