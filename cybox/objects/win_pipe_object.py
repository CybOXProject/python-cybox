import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_pipe_object_1_2 as win_pipe_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.pipe_object import Pipe
from cybox.objects.win_handle_object import Win_Handle

class Win_Pipe:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_pipe_dict):
        """Create the Win Pipe Object object representation from an input dictionary"""
        win_pipe_obj = Pipe.object_from_dict(win_pipe_attributes, win_pipe_binding.WindowsPipeObjectType())
        win_pipe_obj.set_anyAttributes_({'xsi:type' : 'WinPipeObj:WindowsPipeObjectType'})
        
        for key, value in win_pipe_dict.items():
            if key == 'default_time_out' and utils.test_value(value):
                win_pipe_obj.set_Default_Time_Out(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'handle':
                win_pipe_obj.set_Handle(Win_Handle.object_from_dict(value))
            elif key == 'in_buffer_size' and utils.test_value(value):
                win_pipe_obj.set_In_Buffer_Size(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'max_instances' and utils.test_value(value):
                win_pipe_obj.set_Max_Instances(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'open_mode' and utils.test_value(value):
                win_pipe_obj.set_Open_Mode(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'out_buffer_size' and utils.test_value(value):
                win_pipe_obj.set_Out_Buffer_Size(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'pipe_mode' and utils.test_value(value):
                win_pipe_obj.set_Pipe_Mode(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'security_attributes' and utils.test_value(value):
                win_pipe_obj.set_Security_Attributes(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))

        return win_pipe_obj

    @classmethod
    def dict_from_object(cls, win_pipe_obj):
        """Parse and return a dictionary for a Win Pipe Object object"""
        win_pipe_dict = Pipe.dict_from_object(win_pipe_obj)
        if win_pipe_obj.get_Default_Time_Out() is not None: win_pipe_dict['default_time_out'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Default_Time_Out())
        if win_pipe_obj.get_Handle() is not None: win_pipe_dict['handle'] = Win_Handle.dict_from_object(win_pipe_obj.get_Handle())
        if win_pipe_obj.get_In_Buffer_Size() is not None: win_pipe_dict['in_buffer_size'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_In_Buffer_Size())
        if win_pipe_obj.get_Max_Instances() is not None: win_pipe_dict['max_instances'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Max_Instances())
        if win_pipe_obj.get_Open_Mode() is not None: win_pipe_dict['open_mode'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Open_Mode())
        if win_pipe_obj.get_Out_Buffer_Size() is not None: win_pipe_dict['out_buffer_size'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Out_Buffer_Size())
        if win_pipe_obj.get_Pipe_Mode() is not None: win_pipe_dict['pipe_mode'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Pipe_Mode())
        if win_pipe_obj.get_Security_Attributes() is not None: win_pipe_dict['security_attributes'] = Base_Object_Attribute.dict_from_object(win_pipe_obj.get_Security_Attributes())
        return win_pipe_dict




