# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_mailslot_object as win_mailslot_binding
from cybox.common import NonNegativeInteger, ObjectProperties, String
from cybox.objects.win_handle_object import WinHandle


class WinMailslot(ObjectProperties):
    _binding = win_mailslot_binding
    _binding_class = win_mailslot_binding.WindowsMailslotObjectType
    _namespace = "http://cybox.mitre.org/objects#WinMailslotObject-2"
    _XSI_NS = "WinMailslotObj"
    _XSI_TYPE = "WindowsMailslotObjectType"

    handle = fields.TypedField("Handle", WinHandle)
    max_message_size = fields.TypedField("Max_Message_Size", NonNegativeInteger)
    name = fields.TypedField("Name", String)
    read_timeout = fields.TypedField("Read_Timeout", NonNegativeInteger)
    security_attributes = fields.TypedField("Security_Attributes", String)
