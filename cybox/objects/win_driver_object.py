import maec_bundle_3_0 as maecbundle
import cybox.win_driver_object_1_2 as cybox_win_driver_object

class Win_Driver:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, driver_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Other') #change type to driver once CybOX type enum is updated
        driver_obj = cybox_win_driver_object.WindowsDriverObjectType()
        driver_obj.set_anyAttributes_({'xsi:type' : 'WinDriverObj:WindowsDriverObjectType'})
        
        for key, value in driver_attributes.items():
            if (key == 'name' or key == 'filename') and self.__value_test(value):
                driver_obj.set_Driver_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if driver_obj.hasContent_():
            cybox_object.set_Defined_Object(driver_obj)
        
        return cybox_object