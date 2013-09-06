# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_driver_object as win_driver_binding
from cybox.common import ObjectProperties, String, HexBinary, UnsignedLong
from cybox import TypedField


class WinDriver(ObjectProperties):
    _binding = win_driver_binding
    _binding_class = win_driver_binding.WindowsDriverObjectType
    _namespace = "http://cybox.mitre.org/objects#WinDriverObject-2"
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "WindowsDriverObjectType"

    driver_init = TypedField("Driver_Init", UnsignedLong)
    driver_name = TypedField("Driver_Name", String)
    driver_object_address = TypedField("Driver_Object_Address", HexBinary)
    driver_start_io = TypedField("Driver_Start_IO", HexBinary)
    
    def __init__(self):
        super(WinDriver, self).__init__()
