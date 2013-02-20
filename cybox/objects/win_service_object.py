import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.common.hashlist as hashlist
import cybox.bindings.win_service_object_1_3 as win_service_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Service:
    def __init__(self, id):
        self.id = id
        
    @classmethod
    def object_from_dict(cls, service_attributes):
        serv_object = win_service_binding.WindowsServiceObjectType()
        serv_object.set_anyAttributes_({'xsi:type' : 'WinServiceObj:WindowsServiceObjectType'})
        
        for key, value in service_attributes.items():
            if key == 'service_name' and utils.test_value(value):
                serv_object.set_Service_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'display_name' and utils.test_value(value):
                serv_object.set_Display_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'group_name' and utils.test_value(value):
                serv_object.set_Group_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'startup_type' and utils.test_value(value):
                serv_object.set_Startup_Type(Base_Object_Attribute.object_from_dict(win_service_binding.ServiceModeType(), value))
            elif key == 'service_type' and utils.test_value(value):
                serv_object.set_Service_Type(Base_Object_Attribute.object_from_dict(win_service_binding.ServiceType(), value))
            elif key == 'started_as' and utils.test_value(value):
                serv_object.set_Started_As(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_status' and utils.test_value(value):
                serv_object.set_Service_Status(Base_Object_Attribute.object_from_dict(win_service_binding.ServiceStatusType(), value))
            elif key == 'startup_command_line' and utils.test_value(value):
                serv_object.set_Startup_Command_Line(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_dll' and utils.test_value(value):
                serv_object.set_Service_DLL(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_dll_signature_description' and utils.test_value(value):
                serv_object.set_Service_DLL_Signature_Description(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_dll_signature_exists' and utils.test_value(value):
                serv_object.set_service_dll_signature_exists(value)
            elif key == 'service_dll_signature_verified' and utils.test_value(value):
                serv_object.set_service_dll_signature_verified(value)
            elif key == 'service_dll_certificate_issuer' and utils.test_value(value):
                serv_object.set_Service_DLL_Certificate_Issuer(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_dll_certificate_subject' and utils.test_value(value):
                serv_object.set_Service_DLL_Certificate_Subject(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'display_name' and utils.test_value(value):
                serv_object.set_Display_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'service_dll_hashes' and utils.test_value(value):
                serv_object.set_Service_DLL_Hashes(hashlist.Hash_List.object_from_dict(value))
            elif key == 'description_list' and utils.test_value(value):
                desc_list = win_service_binding.ServiceDescriptionListType()
                for desc in value:
                    desc_list.add_Description(desc)
                serv_object.set_Description_List(desc_list)
            
            #elif key == 'controlcode' and utils.test_value(value):
            #    send_control_effect = cybox_core_binding.SendControlCodeEffectType(effect_type='ControlCode_Sent', Control_Code=value)
            #    send_control_effect.set_extensiontype_('cybox:SendControlCodeEffectType')
            #    cybox_object.set_Defined_Effect(send_control_effect)
            #elif key == 'effect':
            #    effect_type = value.get('type')
            #    if effect_type == 'state change':
            #        state_change_effect = self.__create_state_change_effect(value.get('new_defined_object'))
            #        cybox_object.set_Defined_Effect(send_control_effect)

        
        return serv_object  