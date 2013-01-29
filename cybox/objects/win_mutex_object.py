import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_mutex_object_1_2 as win_mutex_object_binding
from cybox.objects.mutex_object import mutex_object
from cybox.objects.win_handle_object import win_handle_object

class win_mutex_object(object):
    def __init__(self):
        pass
        
    @classmethod
    def create_from_dict(cls, win_mutex_attributes):
        """Create the Win Mutex Object object representation from an input dictionary"""
        win_mutex_obj = mutex_object.create_from_dict(win_mutex_attributes,win_mutex_object_binding.WindowsMutexObjectType())
        win_mutex_obj.set_anyAttributes_({'xsi:type' : 'WinMutexObj:WindowsMutexObjectType'})
        
        for key, value in win_mutex_attributes.items():
            if key == 'handle' : win_mutex_obj.set_Handle(win_handle_object.create_from_dict(value))
            elif key == 'security_attributes' and common_methods.test_value(value):
                win_mutex_obj.set_Security_Attributes(baseobjectattribute.create_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
        
        return win_mutex_obj    
    
    @classmethod
    def parse_into_dict(cls, defined_object):
        """Parse and return a dictionary for a Win Mutex Object object"""
        defined_object_dict = mutex_object.parse_into_dict(defined_object)
        if defined_object.get_Handle() is not None: defined_object_dict['handle'] = win_handle_object.parse_into_dict(defined_object.get_Handle())
        if defined_object.get_Security_Attributes() is not None: defined_object_dict['security_attributes'] = baseobjectattribute.parse_into_dict(defined_object.get_Security_Attributes())
            
        return defined_object_dict