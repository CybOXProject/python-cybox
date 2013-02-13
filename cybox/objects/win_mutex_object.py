import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_mutex_object_1_2 as win_mutex_binding
from cybox.objects.mutex_object import Mutex
from cybox.objects.win_handle_object import Win_Handle
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Mutex(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_mutex_dict):
        """Create the Win Mutex Object object representation from an input dictionary"""
        win_mutex_obj = Mutex.object_from_dict(win_mutex_attributes,win_mutex_binding.WindowsMutexObjectType())
        win_mutex_obj.set_anyAttributes_({'xsi:type' : 'WinMutexObj:WindowsMutexObjectType'})
        
        for key, value in win_mutex_dict.items():
            if key == 'handle' : win_mutex_obj.set_Handle(Win_Handle.object_from_dict(value))
            elif key == 'security_attributes' and utils.test_value(value):
                win_mutex_obj.set_Security_Attributes(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
        
        return win_mutex_obj    
    
    @classmethod
    def dict_from_object(cls, win_mutex_obj):
        """Parse and return a dictionary for a Win Mutex Object object"""
        win_mutex_dict = Mutex.dict_from_object(defined_object)
        if win_mutex_obj.get_Handle() is not None: win_mutex_dict['handle'] = Win_Handle.dict_from_object(win_mutex_obj.get_Handle())
        if win_mutex_obj.get_Security_Attributes() is not None: win_mutex_dict['security_attributes'] = Base_Object_Attribute.dict_from_object(win_mutex_obj.get_Security_Attributes())
            
        return win_mutex_dict