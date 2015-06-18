# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_thread_object as win_thread_binding
from cybox.common import (DateTime, HexBinary, NonNegativeInteger,
        ObjectProperties, String, UnsignedInteger)
from cybox.objects.win_handle_object import WinHandle


class WinThread(ObjectProperties):
    _binding = win_thread_binding
    _binding_class = win_thread_binding.WindowsThreadObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinThreadObject-2'
    _XSI_NS = "WinThreadObj"
    _XSI_TYPE = "WindowsThreadObjectType"

    thread_id = fields.TypedField("Thread_ID", NonNegativeInteger)
    handle = fields.TypedField("Handle", WinHandle)
    running_status = fields.TypedField("Running_Status", String)
    context = fields.TypedField("Context", String)
    priority = fields.TypedField("Priority", UnsignedInteger)
    creation_flags = fields.TypedField("Creation_Flags", HexBinary)
    creation_time = fields.TypedField("Creation_Time", DateTime)
    start_address = fields.TypedField("Start_Address", HexBinary)
    parameter_address = fields.TypedField("Parameter_Address", HexBinary)
    security_attributes = fields.TypedField("Security_Attributes", String)
    stack_size = fields.TypedField("Stack_Size", NonNegativeInteger)
