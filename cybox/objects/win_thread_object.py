# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
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

    thread_id = cybox.TypedField("Thread_ID", NonNegativeInteger)
    handle = cybox.TypedField("Handle", WinHandle)
    running_status = cybox.TypedField("Running_Status", String)
    context = cybox.TypedField("Context", String)
    priority = cybox.TypedField("Priority", UnsignedInteger)
    creation_flags = cybox.TypedField("Creation_Flags", HexBinary)
    creation_time = cybox.TypedField("Creation_Time", DateTime)
    start_address = cybox.TypedField("Start_Address", HexBinary)
    parameter_address = cybox.TypedField("Parameter_Address", HexBinary)
    security_attributes = cybox.TypedField("Security_Attributes", String)
    stack_size = cybox.TypedField("Stack_Size", NonNegativeInteger)
