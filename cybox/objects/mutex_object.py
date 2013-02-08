import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.mutex_object_1_3 as mutex_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class mutex_object(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, mutex_attributes, mutex_obj = None):
        """Create the Mutex Object object representation from an input dictionary"""
        if mutex_obj == None:
            mutex_obj = mutex_binding.MutexObjectType()
            mutex_obj.set_anyAttributes_({'xsi:type' : 'MutexObj:MutexObjectType'})
        
        for key, value in mutex_attributes.items():
            if key == 'name' and utils.test_value(value):
                mutex_obj.set_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
                mutex_obj.set_named(True)
            elif key == 'named' and utils.test_value(value):
                mutex_obj.set_named(value.get('value'))
        
        return mutex_obj
    
    
    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Mutex Object object"""
        defined_object_dict = {}
        if defined_object.get_Name() is not None: defined_object_dict['name'] = baseobjectattribute.dict_from_object(defined_object.get_Name())
        if defined_object.get_named() is not None: defined_object_dict['named'] = {'value' : defined_object.get_named()}
            
        return defined_object_dict