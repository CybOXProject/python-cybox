import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_thread_object_1_3 as win_thread_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.objects.win_handle_object import win_handle_object

class win_thread_object:
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, thread_attributes):
        """Create the Windows Thread Object object representation from an input dictionary"""
        thread_obj = win_thread_binding.WindowsThreadObjectType()
        thread_obj.set_anyAttributes_({'xsi:type' : 'WinThreadObj:WindowsThreadObjectType'})
        
        for key, value in thread_attributes.items():
            if key == 'thread_id' and utils.test_value(value):
                thread_obj.set_Thread_ID(baseobjectattribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'handle':
                thread_obj.set_Handle(win_handle_object.object_from_dict(value)) 
            elif key == 'running_status':
                thread_obj.set_Running_Status(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'context':
                thread_obj.set_Context(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'priority':
                thread_obj.set_Priority(baseobjectattribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'creation_flags':
                thread_obj.set_Creation_Flags(baseobjectattribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'creation_time':
                thread_obj.set_Creation_Time(baseobjectattribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'start_address':
                thread_obj.set_Start_Address(baseobjectattribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'parameter_address':
                thread_obj.set_Parameter_Address(baseobjectattribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'security_attributes':
                thread_obj.set_Security_Attributes(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'stack_size':
                thread_obj.set_Stack_Size(baseobjectattribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
        return thread_obj

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Windows Thread Object object"""
        defined_object_dict = {}
        if defined_object.get_Thread_ID() is not None: defined_object_dict['thread_id'] = baseobjectattribute.dict_from_object(defined_object.get_Thread_ID())
        if defined_object.get_Handle() is not None: defined_object_dict['handle'] = win_handle_object.dict_from_object(defined_object.get_Handle())
        if defined_object.get_Running_Status() is not None: defined_object_dict['running_status'] = baseobjectattribute.dict_from_object(defined_object.get_Running_Status())
        if defined_object.get_Context() is not None: defined_object_dict['context'] = baseobjectattribute.dict_from_object(defined_object.get_Context())
        if defined_object.get_Priority() is not None: defined_object_dict['priority'] = baseobjectattribute.dict_from_object(defined_object.get_Priority())
        if defined_object.get_Creation_Flags() is not None: defined_object_dict['creation_flags'] = baseobjectattribute.dict_from_object(defined_object.get_Creation_Flags())
        if defined_object.get_Creation_Time() is not None: defined_object_dict['creation_time'] = baseobjectattribute.dict_from_object(defined_object.get_Creation_Time())
        if defined_object.get_Start_Address() is not None: defined_object_dict['start_address'] = baseobjectattribute.dict_from_object(defined_object.get_Start_Address())
        if defined_object.get_Parameter_Address() is not None: defined_object_dict['parameter_address'] = baseobjectattribute.dict_from_object(defined_object.get_Parameter_Address())
        if defined_object.get_Security_Attributes() is not None: defined_object_dict['security_attributes'] = baseobjectattribute.dict_from_object(defined_object.get_Security_Attributes())
        if defined_object.get_Stack_Size() is not None: defined_object_dict['stack_size'] = baseobjectattribute.dict_from_object(defined_object.get_Stack_Size())
        return defined_object_dict