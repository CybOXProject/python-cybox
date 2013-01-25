import maec_bundle_3_0 as maecbundle
import cybox.win_mailslot_object_1_2 as cybox_win_mailslot_object

class win_mailslot_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, mailslot_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Mailslot')
        mailslot_obj = cybox_win_mailslot_object.WindowsMailslotObjectType()
        mailslot_obj.set_anyAttributes_({'xsi:type' : 'WinMailslotObj:WindowsMailslotObjectType'})
        
        for key, value in mailslot_attributes.items():
            if key == 'name' or key == 'filename' and self.__value_test(value):
                mailslot_obj.set_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if mailslot_obj.hasContent_():
            cybox_object.set_Defined_Object(mailslot_obj)
        
        return cybox_object
