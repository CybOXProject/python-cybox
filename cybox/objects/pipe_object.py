import maec_bundle_3_0 as maecbundle
import cybox.win_pipe_object_1_2 as cybox_win_pipe_object

class pipe_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, pipe_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id())
        pipeobj = cybox_win_pipe_object.WindowsPipeObjectType(named='True')
        pipeobj.set_anyAttributes_({'xsi:type' : 'WinPipeObj:WindowsPipeObjectType'})
        cybox_object.set_type('Pipe')
        
        for key, value in pipe_attributes.items():
            if (key == 'name' or key == 'filename') and self.__value_test(value):
                pipeobj.set_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'controlcode' and self.__value_test(value):
                send_control_effect = maecbundle.cybox_core_1_0.SendControlCodeEffectType(effect_type='ControlCode_Sent', Control_Code=value)
                send_control_effect.set_extensiontype_('cybox:SendControlCodeEffectType')
                cybox_object.set_Defined_Effect(send_control_effect)
            elif key == 'effect':
                effect = self.__create_data_effect(value, value.get('type'))
                if effect != None and effect.hasContent_():
                    cybox_object.set_Defined_Effect(effect)
            elif key == 'association':
                cybox_object.set_association_type(value)

        if pipeobj.hasContent_():
            cybox_object.set_Defined_Object(pipeobj)

        return cybox_object