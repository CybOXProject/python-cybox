# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.unix_pipe_object as unix_pipe_binding
from cybox.common import String
from cybox.objects.pipe_object import Pipe


class UnixPipe(Pipe):
    _binding = unix_pipe_binding
    _binding_class = unix_pipe_binding.UnixPipeObjectType
    _namespace = "http://cybox.mitre.org/objects#UnixPipeObject-2"
    _XSI_NS = "UnixPipeObj"
    _XSI_TYPE = "UnixPipeObjectType"

    permission_mode = fields.TypedField("Permission_Mode", String)
