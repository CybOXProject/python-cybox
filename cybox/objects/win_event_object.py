#import cybox.utils as utils
#import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_event_object_1_3 as win_event_binding
from cybox.objects.win_handle_object import WinHandle
from cybox.common import DefinedObject, String

class WinEvent(DefinedObject):
    _XSI_TYPE = "WindowsEventObjectType"

    def __init__(self):
        self.name = None
        self.handle = None
        self.type = None

    def to_obj(self):
        win_event_obj = win_event_binding.WindowsEventObjectType()
        win_event_obj.set_anyAttributes_({'xsi:type' : 'WinEventObj:WindowsEventObjectType'})
        
        if self.name is not None: win_event_obj.set_Name(self.name.to_obj())
        if self.handle is not None: win_event_obj.set_Handle(self.handle.to_obj())
        if self.type is not None: win_event_obj.set_Type(self.type.to_obj())

        return win_event_obj

    def to_dict(self):
        win_event_dict = {}

        if self.name is not None: win_event_dict['name'] = self.name.to_dict()
        if self.handle is not None: win_event_dict['handle'] = self.handle.to_dict()
        if self.type is not None: win_event_dict['type'] = self.type.to_dict()
        win_event_dict['xsi:type'] = _XSI_TYPE

        return win_event_dict

    @staticmethod
    def from_dict(win_event_dict):
        if not win_event_dict:
            return None
        win_event_ = WinEvent()

        win_event_.handle = WinHandle.from_dict(win_event_dict.get('handle'))
        win_event_.name = String.from_dict(win_event_dict.get('name'))
        win_event_.type = String.from_dict(win_event_dict.get('type'))

        return win_event_    
    
    @staticmethod
    def from_obj(win_event_obj):
        if not win_event_obj:
            return None
        win_event_ = WinEvent()

        win_event_.handle = WinHandle.from_obj(win_event_obj.get_Handle())
        win_event_.name = String.from_obj(win_event_obj.get_Name())
        win_event_.type = String.from_obj(win_event_obj.get_Type())

        return win_event_
        
    #@classmethod
    #def object_from_dict(cls, win_event_dict):
    #    """Create the Win Event Object object representation from an input dictionary"""
    #    win_event_obj = win_event_binding.WindowsEventObjectType()
    #    win_event_obj.set_anyAttributes_({'xsi:type' : 'WinEventObj:WindowsEventObjectType'})
        
    #    for key, value in win_event_dict.items():
    #        if key == 'name' and utils.test_value(value): win_event_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
    #        elif key == 'handle' : win_event_obj.set_Handle(Win_Handle.object_from_dict(value))
    #        elif key == 'type' and utils.test_value(value) : win_event_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
 
    #    return win_event_obj    
    
    #@classmethod
    #def dict_from_object(cls, win_event_obj):
    #    """Parse and return a dictionary for a Win Event Object object"""
    #    win_event_dict = {}
    #    if win_event_obj.get_Name() is not None: win_mutex_dict['name'] = Base_Object_Attribute.dict_from_object(win_event_obj.get_Name())
    #    if win_event_obj.get_Handle() is not None: win_mutex_dict['handle'] = Win_Handle.dict_from_object(win_mutex_obj.get_Handle())
    #    if win_event_obj.get_Type() is not None: win_mutex_dict['type'] = Base_Object_Attribute.dict_from_object(win_event_obj.get_Type())    
    #    return win_event_dict