import maec_bundle_3_0 as maecbundle
import cybox.win_user_account_object_1_3 as cybox_win_user_object

class win_user_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, user_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Other') #change type to User once added to CybOX object type enum
        user_obj = cybox_win_user_object.WindowsUserAccountObjectType()
        user_obj.set_anyAttributes_({'xsi:type' : 'WinUserAccountObj:WindowsUserAccountObjectType'})
        
        for key, value in user_attributes.items():
            if key == 'username' and self.__value_test(value):
                user_obj.set_Username(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if user_obj.hasContent_():
            cybox_object.set_Defined_Object(user_obj)
        
        return cybox_object