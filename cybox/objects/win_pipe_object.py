# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_pipe_object as win_pipe_binding
from cybox.objects.pipe_object import Pipe
from cybox.objects.win_handle_object import WinHandle
from cybox.common import String, NonNegativeInteger, HexBinary


class WinPipe(Pipe):
    _binding = win_pipe_binding
    _binding_class = win_pipe_binding.WindowsPipeObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinPipeObject-2'
    _XSI_NS = "WinPipeObj"
    _XSI_TYPE = "WindowsPipeObjectType"

    default_time_out = fields.TypedField("Default_Time_Out", NonNegativeInteger)
    handle = fields.TypedField("Handle", WinHandle)
    in_buffer_size = fields.TypedField("In_Buffer_Size", NonNegativeInteger)
    max_instances = fields.TypedField("Max_Instances", NonNegativeInteger)
    open_mode = fields.TypedField("Open_Mode", HexBinary)
    out_buffer_size = fields.TypedField("Out_Buffer_Size", NonNegativeInteger)
    pipe_mode = fields.TypedField("Pipe_Mode", HexBinary)
    security_attributes = fields.TypedField("Security_Attributes", String)
