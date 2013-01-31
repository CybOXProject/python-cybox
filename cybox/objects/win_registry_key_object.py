import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.mutex_object_1_3 as mutex_binding
import cybox.win_registry_key_object_1_3 as win_registry_object
from cybox.common.baseobjectattribute import baseobjectattribute


class Registry_Key:
    def __init__(self, id):
        self.id = id
        
    @classmethod
    def object_from_dict(cls, registry_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Key/Key Group')
        reg_object = win_registry_object.WindowsRegistryKeyObjectType()
        reg_object.set_anyAttributes_({'xsi:type' : 'WinRegistryKeyObj:WindowsRegistryKeyObjectType'})
        registry_value = win_registry_object.RegistryValueType()
        #set object attributes
        for key, value in registry_attributes.items():
            if key == 'hive' and self.__value_test(value):
                reg_object.set_Hive(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'key' and self.__value_test(value):
                reg_object.set_Key(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'value' and self.__value_test(value):
                registry_value.set_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'valuedata' and self.__value_test(value):
                registry_value.set_Data(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'valuedatatype' and self.__value_test(value):
                registry_value.set_Datatype(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String',valueOf_=maecbundle.quote_xml(value)))
            elif key == 'association':
                cybox_object.set_association_type(value)
                
        if registry_value.hasContent_():
            reg_values = win_registry_object.RegistryValuesType()
            reg_values.add_Value(registry_value)
            reg_object.set_Values(reg_values)
        
        if reg_object.hasContent_():    
            cybox_object.set_Defined_Object(reg_object)
        
        return cybox_object