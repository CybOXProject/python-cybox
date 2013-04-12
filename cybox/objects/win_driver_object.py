import cybox
import cybox.utils as utils
import cybox.bindings.win_driver_object_1_2 as win_driver_binding
from cybox.common import DefinedObject, String, DateTime, UnsignedInteger, Duration

class WinDriver(DefinedObject):
    _XSI_TYPE = "WindowsDriverObjectType"

    def __init__(self):
        self.driver_init = None
        self.driver_name = None
        self.driver_object_address = None
        self.driver_start_io = None

    def to_obj(self):
        driver_obj = win_driver_binding.WindowsDriverObjectType()
        driver_obj.set_anyAttributes_({'xsi:type' : 'WinDriverObj:WindowsDriverObjectType'})
        if self.driver_init is not None: driver_obj.set_Driver_Init(self.driver_init.to_obj())
        if self.driver_name is not None: driver_obj.set_Driver_Name(self.driver_name.to_obj())
        if self.driver_object_address is not None: driver_obj.set_Driver_Object_Address(self.driver_name.to_obj())
        if self.driver_start_io is not None: driver_obj.set_Driver_Start_IO(self.driver_start_io.to_obj())
        return driver_obj

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(driver_dict):
        if not driver_dict:
            return None
        driver_ = WinDriver()
        driver_.driver_init = driver_dict.get('driver_init')
        driver_.driver_name = driver_dict.get('driver_name')
        driver_.driver_object_address = driver_dict.get('driver_object_address')
        driver_.driver_start_io = driver_dict.get('driver_start_io')
        return driver_

    @staticmethod
    def from_obj(driver_obj):
        pass
