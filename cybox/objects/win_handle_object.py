# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_handle_object as win_handle_binding
from cybox.common import (ObjectProperties, String, UnsignedLong,
        UnsignedInteger)


class WinHandle(ObjectProperties):
    _binding = win_handle_binding
    _binding_class = win_handle_binding.WindowsHandleObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinHandleObject-2'
    _XSI_NS = "WinHandleObj"
    _XSI_TYPE = "WindowsHandleObjectType"

    id_ = fields.TypedField("ID", UnsignedInteger)
    name = fields.TypedField("Name", String)
    type_ = fields.TypedField("Type", String)
    object_address = fields.TypedField("Object_Address", UnsignedLong)
    access_mask = fields.TypedField("Access_Mask", UnsignedLong)
    pointer_count = fields.TypedField("Pointer_Count", UnsignedLong)


class WinHandleList(entities.EntityList):
    _binding = win_handle_binding
    _binding_class = win_handle_binding.WindowsHandleListType
    _namespace = 'http://cybox.mitre.org/objects#WinHandleObject-2'
    handle = fields.TypedField("Handle", WinHandle, multiple=True)