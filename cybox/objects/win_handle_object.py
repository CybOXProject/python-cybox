import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_handle_object_1_3 as win_handle_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Handle:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_handle_dict):
        """Create the Win Handle Object object representation from an input dictionary"""
        win_handle_obj = win_handle_binding.WindowsHandleObjectType()
        win_handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})
        
        for key, value in win_handle_dict.items():
            if key == 'id' and utils.test_value(value):
                win_handle_obj.set_ID(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'), value))
            if key == 'name' and utils.test_value(value):
                win_handle_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'type' and utils.test_value(value):
                win_handle_obj.set_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'object_address' and utils.test_value(value):
                win_handle_obj.set_Object_Address(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'access_mask' and utils.test_value(value):
                win_handle_obj.set_Access_Mask(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'pointer_count' and utils.test_value(value):
                win_handle_obj.set_Pointer_Count(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
                
        return win_handle_obj
    
    @classmethod
    def dict_from_object(cls, win_handle_obj):
        """Parse and return a dictionary for a Win Handle Object object"""
        win_handle_dict = {}
        if win_handle_obj.get_ID() is not None:
            win_handle_dict["id"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_ID())
        if win_handle_obj.get_Type() is not None:
            win_handle_dict["type"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Type())
        if win_handle_obj.get_Name() is not None:
            win_handle_dict["name"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Name())
        if win_handle_obj.get_Object_Address() is not None:
            win_handle_dict["object_address"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Object_Address())
        if win_handle_obj.get_Access_Mask() is not None:
            win_handle_dict["access_mask"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Access_Mask())
        if win_handle_obj.get_Pointer_Count() is not None:
            win_handle_dict["type"] = Base_Object_Attribute.dict_from_object(win_handle_obj.get_Pointer_Count())
            
        return win_handle_dict

class Win_Handle_List:
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, handle_list):
        """Create a Win Handle List Object from an input handle list"""
        handle_list_object = win_handle_binding.WindowsHandleListType()
        for win_handle_dict in handle_list:
            win_handle_object = Win_Handle.object_from_dict(win_handle_dict)
            if win_handle_object.hasContent_():
                handle_list_object.add_Handle(win_handle_object)

        return handle_list_object

    @classmethod
    def list_from_object(cls, win_handle_obj):
        """Parse and return a dictionary for a Win Handle List object"""
        handle_list = []
        for win_handle in win_handle_obj.get_Handle():
            handle_list.append(Win_Handle.dict_from_object(win_handle))
            
        return handle_list

