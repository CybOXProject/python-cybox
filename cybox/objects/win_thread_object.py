# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_win_thread_object_1_3 as win_thread_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.win_handle_object import Win_Handle

class Win_Thread:
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, win_thread_dict):
        """Create the Windows Thread Object object representation from an input dictionary"""
        win_thread_obj = win_thread_binding.WindowsThreadObjectType()
        win_thread_obj.set_anyAttributes_({'xsi:type' : 'WinThreadObj:WindowsThreadObjectType'})
        
        for key, value in win_thread_dict.items():
            if key == 'thread_id' and utils.test_value(value):
                win_thread_obj.set_Thread_ID(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'handle':
                win_thread_obj.set_Handle(Win_Handle.object_from_dict(value)) 
            elif key == 'running_status':
                win_thread_obj.set_Running_Status(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'context':
                win_thread_obj.set_Context(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'priority':
                win_thread_obj.set_Priority(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'creation_flags':
                win_thread_obj.set_Creation_Flags(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'creation_time':
                win_thread_obj.set_Creation_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'),value))
            elif key == 'start_address':
                win_thread_obj.set_Start_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'parameter_address':
                win_thread_obj.set_Parameter_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'security_attributes':
                win_thread_obj.set_Security_Attributes(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'stack_size':
                win_thread_obj.set_Stack_Size(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
        return win_thread_obj

    @classmethod
    def dict_from_object(cls, win_thread_obj):
        """Parse and return a dictionary for a Windows Thread Object object"""
        win_thread_dict = {}
        if win_thread_obj.get_Thread_ID() is not None: win_thread_dict['thread_id'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Thread_ID())
        if win_thread_obj.get_Handle() is not None: win_thread_dict['handle'] = Win_Handle.dict_from_object(win_thread_obj.get_Handle())
        if win_thread_obj.get_Running_Status() is not None: win_thread_dict['running_status'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Running_Status())
        if win_thread_obj.get_Context() is not None: win_thread_dict['context'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Context())
        if win_thread_obj.get_Priority() is not None: win_thread_dict['priority'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Priority())
        if win_thread_obj.get_Creation_Flags() is not None: win_thread_dict['creation_flags'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Creation_Flags())
        if win_thread_obj.get_Creation_Time() is not None: win_thread_dict['creation_time'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Creation_Time())
        if win_thread_obj.get_Start_Address() is not None: win_thread_dict['start_address'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Start_Address())
        if win_thread_obj.get_Parameter_Address() is not None: win_thread_dict['parameter_address'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Parameter_Address())
        if win_thread_obj.get_Security_Attributes() is not None: win_thread_dict['security_attributes'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Security_Attributes())
        if win_thread_obj.get_Stack_Size() is not None: win_thread_dict['stack_size'] = Base_Object_Attribute.dict_from_object(win_thread_obj.get_Stack_Size())
        return win_thread_dict
