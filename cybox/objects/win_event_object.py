# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_event_object as win_event_binding
from cybox.objects.win_handle_object import WinHandle
from cybox.common import ObjectProperties, String


class WinEvent(ObjectProperties):
    _binding = win_event_binding
    _binding_class = win_event_binding.WindowsEventObjectType
    _namespace = "http://cybox.mitre.org/objects#WinEventObject-2"
    _XSI_NS = "WinEventObj"
    _XSI_TYPE = "WindowsEventObjectType"

    name = cybox.TypedField("Name", String)
    handle = cybox.TypedField("Handle", WinHandle)
    type = cybox.TypedField("Type", String)
       
