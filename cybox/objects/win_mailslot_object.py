# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_mailslot_object_1_2 as win_mailslot_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.win_handle_object import Win_Handle_List

class Win_Mailslot:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_mailslot_dict):
        """Create the Win Mailslot Object object representation from an input dictionary"""
        win_mailslot_obj = win_mailslot_binding.WindowsMailslotObjectType()
        win_mailslot_obj.set_anyAttributes_({'xsi:type' : 'WinMailslotObj:WindowsMailslotObjectType'})
        
        for key, value in win_mailslot_dict.items():
            if key == 'name' and utils.test_value(value):
                win_mailslot_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'max_message_size' and utils.test_value(value):
                win_mailslot_obj.set_Max_Message_Size(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'read_timeout' and utils.test_value(value):
                win_mailslot_obj.set_Read_Timeout(Base_Object_Attribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'security_attributes' and utils.test_value(value):
                win_mailslot_obj.set_Security_Attributes(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'handle':
                win_mailslot_obj.set_Handle(Win_Handle_List.object_from_list(value))
        
        return win_mailslot_obj

    @classmethod
    def dict_from_object(cls, win_mailslot_obj):
        """Parse and return a dictionary for a Win Mailslot Object object"""
        win_mailslot_dict = {}
        if win_mailslot_obj.get_Handle() is not None: win_mailslot_dict['handle'] = Win_Handle_List.list_from_object(win_mailslot_obj.get_Handle())
        if win_mailslot_obj.get_Max_Message_Size() is not None: win_mailslot_dict['max_message_size'] = Base_Object_Attribute.dict_from_object(win_mailslot_obj.get_Max_Message_Size())
        if win_mailslot_obj.get_Name() is not None: win_mailslot_dict['name'] = Base_Object_Attribute.dict_from_object(win_mailslot_obj.get_Name())
        if win_mailslot_obj.get_Read_Timeout() is not None: win_mailslot_dict['read_timeout'] = Base_Object_Attribute.dict_from_object(win_mailslot_obj.get_Read_Timeout())
        if win_mailslot_obj.get_Security_Attributes() is not None: win_mailslot_dict['security_attributes'] = Base_Object_Attribute.dict_from_object(win_mailslot_obj.get_Security_Attributes())
        return win_mailslot_dict
