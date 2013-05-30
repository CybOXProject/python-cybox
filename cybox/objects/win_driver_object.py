# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.win_driver_object as win_driver_binding
from cybox.common import ObjectProperties, String, HexBinary, UnsignedLong

class WinDriver(ObjectProperties):
    _XSI_NS = "WinDriverObj"
    _XSI_TYPE = "WindowsDriverObjectType"

    def __init__(self):
        super(WinDriver, self).__init__()
        self.driver_init = None
        self.driver_name = None
        self.driver_object_address = None
        self.driver_start_io = None

    def to_obj(self):
        driver_obj = win_driver_binding.WindowsDriverObjectType()
        super(WinDriver, self).to_obj(driver_obj)
        if self.driver_init is not None: driver_obj.set_Driver_Init(self.driver_init.to_obj())
        if self.driver_name is not None: driver_obj.set_Driver_Name(self.driver_name.to_obj())
        if self.driver_object_address is not None: driver_obj.set_Driver_Object_Address(self.driver_name.to_obj())
        if self.driver_start_io is not None: driver_obj.set_Driver_Start_IO(self.driver_start_io.to_obj())
        return driver_obj

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

    @staticmethod
    def from_obj(driver_obj):
        if not driver_obj:
            return None
        driver_ = WinDriver()
        driver_.driver_init = UnsignedLong.from_obj(driver_obj.get_Driver_Init())
        driver_.driver_name = String.from_obj(driver_obj.get_Driver_Name())
        driver_.driver_object_address = HexBinary.from_obj(driver_obj.get_Driver_Object_Address())
        driver_.driver_start_io = HexBinary.from_obj(driver_obj.get_Driver_Start_IO())
        return driver_
