# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_hook_object as win_hook_binding
from cybox.objects.library_object import Library
from cybox.objects.win_handle_object import WinHandle
from cybox.common import ObjectProperties, String, NonNegativeInteger

class WinHook(ObjectProperties):
    _binding = win_hook_binding
    _binding_class = win_hook_binding.WindowsHookObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinHookObject-1'
    _XSI_NS = "WinHookObj"
    _XSI_TYPE = "WindowsHookObjectType"

    type_ = cybox.TypedField("Type", String)
    handle = cybox.TypedField("Handle", WinHandle)
    hooking_function_name = cybox.TypedField("Hooking_Function_Name", String)
    hooking_module = cybox.TypedField("Hooking_Module", Library)
    thread_id = cybox.TypedField("Thread_ID", NonNegativeInteger)
