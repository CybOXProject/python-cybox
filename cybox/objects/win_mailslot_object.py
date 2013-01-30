import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_mailslot_object_1_2 as win_mailslot_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.objects.win_handle_object import win_handle_object

class win_mailslot_object:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, mailslot_attributes):
        """Create the Win Mailslot Object object representation from an input dictionary"""
        mailslot_obj = win_mailslot_binding.WindowsMailslotObjectType()
        mailslot_obj.set_anyAttributes_({'xsi:type' : 'WinMailslotObj:WindowsMailslotObjectType'})
        
        for key, value in mailslot_attributes.items():
            if key == 'name' and common_methods.test_value(value):
                mailslot_obj.set_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'max_message_size' and common_methods.test_value(value):
                mailslot_obj.set_Max_Message_Size(baseobjectattribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'read_timeout' and common_methods.test_value(value):
                mailslot_obj.set_Read_Timeout(baseobjectattribute.object_from_dict(common_types_binding.NonNegativeIntegerObjectAttributeType(datatype='NonNegativeInteger'),value))
            elif key == 'security_attributes' and common_methods.test_value(value):
                mailslot_obj.set_Security_Attributes(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'handle':
                mailslot_obj.set_Handle(win_handle_object.create_list_from_dict(value))

        if mailslot_obj.hasContent_():
            cybox_object.set_Defined_Object(mailslot_obj)
        
        return mailslot_obj

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Win Mailslot Object object"""
        defined_object_dict = {}
        if defined_object.get_Handle() is not None: defined_object_dict['handle'] = win_handle_object.parse_list_into_dict(defined_object.get_Handle())
        if defined_object.get_Max_Message_Size() is not None: defined_object_dict['max_message_size'] = baseobjectattribute.dict_from_object(defined_object.get_Max_Message_Size())
        if defined_object.get_Name() is not None: defined_object_dict['name'] = baseobjectattribute.dict_from_object(defined_object.get_Name())
        if defined_object.get_Read_Timeout() is not None: defined_object_dict['read_timeout'] = baseobjectattribute.dict_from_object(defined_object.get_Read_Timeout())
        if defined_object.get_Security_Attributes() is not None: defined_object_dict['security_attributes'] = baseobjectattribute.dict_from_object(defined_object.get_Security_Attributes())
        return defined_object_dict