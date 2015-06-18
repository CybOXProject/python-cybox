# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

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

    type_ = fields.TypedField("Type", String)
    handle = fields.TypedField("Handle", WinHandle)
    hooking_function_name = fields.TypedField("Hooking_Function_Name", String)
    hooking_module = fields.TypedField("Hooking_Module", Library)
    thread_id = fields.TypedField("Thread_ID", NonNegativeInteger)
