import cybox
import cybox.utils as utils
#import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_handle_object_1_3 as win_handle_binding
from cybox.common import DefinedObject, String, UnsignedLong, UnsignedInteger

class WinHandle(DefinedObject):
    _XSI_TYPE = "WindowsHandleObjectType"

    def __init__(self):
        self.id = None
        self.name = None
        self.type = None
        self.object_address = None
        self.access_mask = None
        self.pointer_count = None

    def to_obj(self):
        win_handle_obj = win_handle_binding.WindowsHandleObjectType()
        win_handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})

        if self.id is not None: win_handle_obj.set_ID(self.id.to_obj())
        if self.name is not None: win_handle_obj.set_Name(self.name.to_obj())
        if self.type is not None: win_handle_obj.set_Type(self.type.to_obj())
        if self.object_address is not None: win_handle_obj.set_Object_Address(self.object_address.to_obj())
        if self.access_mask is not None: win_handle_obj.set_Access_Mask(self.access_mask.to_obj())
        if self.pointer_count is not None: win_handle_obj.set_Pointer_Count(self.pointer_count.to_obj())

        return win_handle_obj

    def to_dict(self):
        win_handle_dict = {}
        if self.id is not None: win_handle_dict['id'] = self.id.to_dict()
        if self.name is not None: win_handle_dict['name'] = self.name.to_dict()
        if self.type is not None: win_handle_dict['type'] = self.type.to_dict()
        if self.object_address is not None: win_handle_dict['object_address'] = self.object_address.to_dict()
        if self.access_mask is not None: win_handle_dict['access_mask'] = self.access_mask.to_dict()
        if self.pointer_count is not None: win_handle_dict['pointer_count'] = self.pointer_count.to_dict()
        win_handle_dict['xsi:type'] = self._XSI_TYPE

        return win_handle_dict

    @staticmethod
    def from_dict(win_handle_dict):
        if not win_handle_dict:
            return None
        win_handle_ = WinHandle()
        
        win_handle_.id = UnsignedInteger.from_dict(win_handle_dict.get('id'))        
        win_handle_.name = String.from_dict(win_handle_dict.get('name'))
        win_handle_.type = String.from_dict(win_handle_dict.get('type'))
        win_handle_.object_address = UnsignedLong.from_dict(win_handle_dict.get('id'))
        win_handle_.access_mask = UnsignedLong.from_dict(win_handle_dict.get('access_mask'))
        win_handle_.pointer_count = UnsignedLong.from_dict(win_handle_dict.get('id')) 

        return win_handle_
    
    @staticmethod
    def from_obj(win_handle_obj):
        if not win_handle_obj:
            return None
        win_handle_ = WinHandle()

        win_handle_.id = UnsignedInteger.from_obj(win_handle_obj.get_ID())        
        win_handle_.name = String.from_obj(win_handle_obj.get_Name())
        win_handle_.type = String.from_obj(win_handle_obj.get_Type())
        win_handle_.object_address = UnsignedLong.from_obj(win_handle_obj.get_Object_Address())
        win_handle_.access_mask = UnsignedLong.from_obj(win_handle_obj.get_Access_Mask())
        win_handle_.pointer_count = UnsignedLong.from_obj(win_handle_obj.get_Pointer_Count()) 

        return win_handle_

    #@classmethod
    #def object_from_dict(cls, win_handle_dict):
    #    """Create the Win Handle Object object representation from an input dictionary"""
    #    win_handle_obj = win_handle_binding.WindowsHandleObjectType()
    #    win_handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})
        
    #    for key, value in win_handle_dict.items():
    #        if key == 'id' and utils.test_value(value):
    #            win_handle_obj.set_ID(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'), value))
    #        if key == 'name' and utils.test_value(value):
    #            win_handle_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
    #        if key == 'type' and utils.test_value(value):
    #            win_handle_obj.set_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
    #        if key == 'object_address' and utils.test_value(value):
    #            win_handle_obj.set_Object_Address(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
    #        if key == 'access_mask' and utils.test_value(value):
    #            win_handle_obj.set_Access_Mask(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
    #        if key == 'pointer_count' and utils.test_value(value):
    #            win_handle_obj.set_Pointer_Count(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
                
    #    return win_handle_obj
    
    #@classmethod
    #def dict_from_object(cls, win_handle_obj):
    #    """Parse and return a dictionary for a Win Handle Object object"""
    #    win_handle_dict = {}
    #    if win_handle_obj.get_ID() is not None:
    #        win_handle_dict["id"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_ID())
    #    if win_handle_obj.get_Type() is not None:
    #        win_handle_dict["type"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Type())
    #    if win_handle_obj.get_Name() is not None:
    #        win_handle_dict["name"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Name())
    #    if win_handle_obj.get_Object_Address() is not None:
    #        win_handle_dict["object_address"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Object_Address())
    #    if win_handle_obj.get_Access_Mask() is not None:
    #        win_handle_dict["access_mask"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Access_Mask())
    #    if win_handle_obj.get_Pointer_Count() is not None:
    #        win_handle_dict["type"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Pointer_Count())
            
    #    return win_handle_dict

class WinHandleList(cybox.Entity):
    def __init__(self):
        self.handle_obj_list = []

    def add_handle(self, handle):
        self.handle_obj_list.append(handle)

    def to_obj(self):
        handle_list_obj = win_handle_binding.WindowsHandleListType()
        for handle_obj in self.handle_obj_list:
            handle_list_obj.add_Handle(handle_obj.to_obj())
        return handle_list_obj

    def to_list(self):
        handle_dict_list = []
        for handle_obj in self.handle_obj_list:
            handle_dict_list.append(handle_obj.to_dict())
        return handle_dict_list

    @staticmethod
    def from_list(handle_list):
        if not handle_list:
            return None
        win_handle_list_ = WinHandleList()
        for handle_dict in handle_list:
            win_handle_list_.add_handle(WinHandle.from_dict(handle_dict))
        return win_handle_list_

    @staticmethod
    def from_obj(win_handle_list_obj):
        if not win_handle_obj:
            return None
        win_handle_list_ = WinHandleList()
        for handle_obj in win_handle_list_obj.get_Handle():
            win_handle_list_.add_handle(WinHandle.from_obj(handle_obj))
        return win_handle_list_
