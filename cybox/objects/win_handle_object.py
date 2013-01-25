import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.win_handle_object_1_3 as cybox_win_handle_object

class win_handle_object:
    def __init__(self, id):
        pass
        
    @classmethod
    def create_from_dict(cls, handle_attributes):
        handle_obj = cybox_win_handle_object.WindowsHandleObjectType()
        handle_obj.set_anyAttributes_({'xsi:type' : 'WinHandleObj:WindowsHandleObjectType'})
        
        for key, value in handle_attributes.items():
            if key == 'id' and common_methods.test_value(value):
                handle_obj.set_ID(common_methods.create_element_from_dict(cybox_common.UnsignedIntegerObjectAttributeType(datatype='UnsignedInt'), value))
            if key == 'name' and common_methods.test_value(value):
                handle_obj.set_Type(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            if key == 'type' and common_methods.test_value(value):
                handle_obj.set_Type(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'), value))
            if key == 'object_address' and common_methods.test_value(value):
                handle_obj.set_Object_Address(common_methods.create_element_from_dict(cybox_common.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'access_mask' and common_methods.test_value(value):
                handle_obj.set_AccessMask(common_methods.create_element_from_dict(cybox_common.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'pointer_count' and common_methods.test_value(value):
                handle_obj.set_Poointer_Count(common_methods.create_element_from_dict(cybox_common.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
                
        return handle_obj
    
    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
            
        if defined_object.get_ID() is not None:
            defined_object_dict["id"] = common_methods.parse_element_into_dict(defined_object.get_ID())
        if defined_object.get_Type() is not None:
            defined_object_dict["type"] = common_methods.parse_element_into_dict(defined_object.get_Type())
        if defined_object.get_Name() is not None:
            defined_object_dict["name"] = common_methods.parse_element_into_dict(defined_object.get_Name())
        if defined_object.get_Object_Address() is not None:
            defined_object_dict["object_address"] = common_methods.parse_element_into_dict(defined_object.get_Object_Address())
        if defined_object.get_Access_Mask() is not None:
            defined_object_dict["access_mask"] = common_methods.parse_element_into_dict(defined_object.get_Acess_Mask())
        if defined_object.get_Pointer_Count() is not None:
            defined_object_dict["type"] = common_methods.parse_element_into_dict(defined_object.get_Pointer_Count())
            
        return defined_object_dict