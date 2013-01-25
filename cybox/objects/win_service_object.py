import maec_bundle_3_0 as maecbundle
import cybox.win_service_object_1_3 as cybox_win_service_object

class win_service_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, service_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Service/Daemon')
        serv_object = cybox_win_service_object.WindowsServiceObjectType()
        serv_object.set_anyAttributes_({'xsi:type' : 'WinServiceObj:WindowsServiceObjectType'})
        
        for key, value in service_attributes.items():
            if key == 'service_name' and self.__value_test(value):
                serv_object.set_Service_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'display_name' and self.__value_test(value):
                serv_object.set_Display_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'startup_type' and self.__value_test(value):
                serv_object.set_Startup_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'service_type' and self.__value_test(value):
                serv_object.set_Service_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'started_as' and self.__value_test(value):
                serv_object.set_Started_As(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'service_status' and self.__value_test(value):
                serv_object.set_Service_Status(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'filename':
                continue #revisit
            elif key == 'controlcode' and self.__value_test(value):
                send_control_effect = maecbundle.cybox_core_1_0.SendControlCodeEffectType(effect_type='ControlCode_Sent', Control_Code=value)
                send_control_effect.set_extensiontype_('cybox:SendControlCodeEffectType')
                cybox_object.set_Defined_Effect(send_control_effect)
            elif key == 'effect':
                effect_type = value.get('type')
                if effect_type == 'state change':
                    state_change_effect = self.__create_state_change_effect(value.get('new_defined_object'))
                    cybox_object.set_Defined_Effect(send_control_effect)
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if serv_object.hasContent_():        
            cybox_object.set_Defined_Object(serv_object)
        
        return cybox_object  