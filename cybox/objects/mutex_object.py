import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.mutex_object_1_3 as mutex_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Mutex(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, mutex_dict, mutex_obj = None):
        """Create the Mutex Object object representation from an input dictionary"""
        if mutex_obj == None:
            mutex_obj = mutex_binding.MutexObjectType()
            mutex_obj.set_anyAttributes_({'xsi:type' : 'MutexObj:MutexObjectType'})
        
        for key, value in mutex_dict.items():
            if key == 'name' and utils.test_value(value):
                mutex_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
                mutex_obj.set_named(True)
            elif key == 'named' and utils.test_value(value):
                mutex_obj.set_named(value)
        
        return mutex_obj
    
    
    @classmethod
    def dict_from_object(cls, mutex_obj):
        """Parse and return a dictionary for a Mutex Object object"""
        mutex_dict = {}
        if mutex_obj.get_Name() is not None: mutex_dict['name'] = Base_Object_Attribute.dict_from_object(mutex_obj.get_Name())
        if mutex_obj.get_named() is not None: mutex_dict['named'] = mutex_obj.get_named()
            
        return mutex_dict
