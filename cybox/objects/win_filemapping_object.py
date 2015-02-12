# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_filemapping_object as win_filemapping_binding
from cybox.objects.win_handle_object import WinHandle
from cybox.common import ObjectProperties, String, UnsignedLong


class WinFilemapping(ObjectProperties):
    _binding = win_filemapping_binding
    _binding_class = win_filemapping_binding.WindowsFilemappingObjectType
    _namespace = "http://cybox.mitre.org/objects#WinFilemappingObject-1"
    _XSI_NS = "WinFilemappingObj"
    _XSI_TYPE = "WindowsFilemappingObjectType"

    name = cybox.TypedField("Name", String)
    file_handle = cybox.TypedField("File_Handle", WinHandle)
    handle = cybox.TypedField("Handle", WinHandle)
    page_protection_value = cybox.TypedField("Page_Protection_Value", String)
    page_protection_attribute = cybox.TypedField("Page_Protection_Attribute", String, multiple=True)
    maximum_size = cybox.TypedField("Maximum_Size", UnsignedLong)
    actual_size = cybox.TypedField("Actual_Size", UnsignedLong)
    security_attributes = cybox.TypedField("Security_Attributes", String)
