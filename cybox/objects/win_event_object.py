import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_event_object_1_3 as win_event_binding
from cybox.objects.win_handle_object import Win_Handle
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Event(object):
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_event_dict):
        """Create the Win Event Object object representation from an input dictionary"""
        win_event_obj = win_event_binding.WindowsEventObjectType()
        win_event_obj.set_anyAttributes_({'xsi:type' : 'WinEventObj:WindowsEventObjectType'})
        
        for key, value in win_event_dict.items():
            if key == 'name' and utils.test_value(value): win_event_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'handle' : win_event_obj.set_Handle(Win_Handle.object_from_dict(value))
            elif key == 'type' and utils.test_value(value) : win_event_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
 
        return win_event_obj    
    
    @classmethod
    def dict_from_object(cls, win_event_obj):
        """Parse and return a dictionary for a Win Event Object object"""
        win_event_dict = {}
        if win_event_obj.get_Name() is not None: win_mutex_dict['name'] = Base_Object_Attribute.dict_from_object(win_event_obj.get_Name())
        if win_event_obj.get_Handle() is not None: win_mutex_dict['handle'] = Win_Handle.dict_from_object(win_mutex_obj.get_Handle())
        if win_event_obj.get_Type() is not None: win_mutex_dict['type'] = Base_Object_Attribute.dict_from_object(win_event_obj.get_Type())    
        return win_event_dict