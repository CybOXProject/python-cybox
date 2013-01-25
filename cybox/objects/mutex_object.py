import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.win_mutex_object_1_2 as cybox_win_mutex_object
import cybox_helper.objects.win_handle_object.win_handle_object as cybox_win_handle_object


class mutex_object(object):
    def __init__(self):
        self.id = id
        
    @classmethod
    def create_from_dict(cls, mutex_attributes):
        mutex_obj = cybox_win_mutex_object.WindowsMutexObjectType()
        mutex_obj.set_anyAttributes_({'xsi:type' : 'WinMutexObj:WindowsMutexObjectType'})
        
        for key, value in mutex_attributes.items():
            if key == 'name' and common_methods.test_value(value):
                mutex_obj.set_Name(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
                mutex_obj.set_named(True)
            if key == 'security_attributes' and common_methods.test_value(value):
                mutex_obj.set_Security_Attributes(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
            if key == 'handle' and common_methods.test_value(value):
                mutex_obj.set_Handle(cybox_win_handle_object.create_from_dict(value))
        
        return mutex_object
    
    
    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
            
            if defined_object.get_Name() is not None:
                defined_object_dict["name"] = common_methods.parse_element_into_dict(defined_object.get_Name())
            if defined_object.get_Security_Attributes() is not None:
                defined_object_dict["security_attributes"] = common_methods.parse_element_into_dict(defined_object.get_Security_Attributes())
            if defined_object.get_Handle() is not None:
                defined_object_dict["handle"] = cybox_win_handle_object.parse_into_dict(defined_object.get_Handle())
            
        return defined_object_dict