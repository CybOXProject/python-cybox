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

    def to_dict(self):
        driver_dict = {}
        super(WinDriver, self).to_dict(driver_dict)
        if self.driver_init is not None: driver_dict['driver_init'] = self.driver_init.to_dict()
        if self.driver_name is not None: driver_dict['driver_name'] = self.driver_name.to_dict()
        if self.driver_object_address is not None: driver_dict['driver_object_address'] = self.driver_object_address.to_dict()
        if self.driver_start_io is not None: driver_dict['driver_start_io'] = self.driver_start_io.to_dict()
        return driver_dict

    @staticmethod
    def from_dict(driver_dict):
        if not driver_dict:
            return None
        driver_ = WinDriver()
        driver_.driver_init = UnsignedLong.from_dict(driver_dict.get('driver_init'))
        driver_.driver_name = String.from_dict(driver_dict.get('driver_name'))
        driver_.driver_object_address = HexBinary.from_dict(driver_dict.get('driver_object_address'))
        driver_.driver_start_io = HexBinary.from_dict(driver_dict.get('driver_start_io'))
        return driver_
