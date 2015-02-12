# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_handle_object as win_handle_binding
from cybox.common import (ObjectProperties, String, UnsignedLong,
        UnsignedInteger)


class WinHandle(ObjectProperties):
    _binding = win_handle_binding
    _binding_class = win_handle_binding.WindowsHandleObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinHandleObject-2'
    _XSI_NS = "WinHandleObj"
    _XSI_TYPE = "WindowsHandleObjectType"

    id_ = cybox.TypedField("ID", UnsignedInteger)
    name = cybox.TypedField("Name", String)
    type_ = cybox.TypedField("Type", String)
    object_address = cybox.TypedField("Object_Address", UnsignedLong)
    access_mask = cybox.TypedField("Access_Mask", UnsignedLong)
    pointer_count = cybox.TypedField("Pointer_Count", UnsignedLong)


class WinHandleList(cybox.EntityList):
    _binding = win_handle_binding
    _binding_class = win_handle_binding.WindowsHandleListType
    _binding_var = "Handle"
    _contained_type = WinHandle
    _namespace = 'http://cybox.mitre.org/objects#WinHandleObject-2'
