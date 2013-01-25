import maec_bundle_3_0 as maecbundle
import cybox.win_network_share_object_1_3 as cybox_win_network_share_object

class win_network_share_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, share_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Other') #change type to Network Share once added to CybOX object type enum
        share_obj = cybox_win_network_share_object.WindowsNetworkShareObjectType()
        share_obj.set_anyAttributes_({'xsi:type' : 'WinNetworkShareObj:WindowsNetworkShareObjectType'})
        
        for key, value in share_attributes.items():
            if key == 'netname' and self.__value_test(value):
                share_obj.set_Netname(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'local_path' and self.__value_test(value):
                share_obj.set_Local_Path(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'type' and self.__value_test(value):
                share_obj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
      
        if share_obj.hasContent_():
            cybox_object.set_Defined_Object(share_obj)
        
        return cybox_object