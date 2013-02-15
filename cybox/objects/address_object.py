import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.address_object_1_2 as address_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Address(object):
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, address_attributes):
        """Create the Address Object object representation from an input dictionary"""
        addrobject = address_binding.AddressObjectType()
        addrobject.set_anyAttributes_({'xsi:type' : 'AddressObj:AddressObjectType'})
        
        for key, value in address_attributes.items():
            if key == 'category' and utils.test_value(value):
                addrobject.set_category(value)
            elif key == 'ext_category' and utils.test_value(value):
                addrobject.set_Ext_Category(value)
            elif key == 'vlan_name' and utils.test_value(value):
                addrobject.set_VLAN_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'vlan_num' and utils.test_value(value):
                addrobject.set_VLAN_Num(Base_Object_Attribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'is_source' and utils.test_value(value):
                addrobject.set_is_source(value)
            elif key == 'is_destination' and utils.test_value(value):
                addrobject.set_is_destination(value)
            elif key == 'address_value' and utils.test_value(value):
                addrobject.set_Address_Value(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
        return addrobject

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for an Address Object object"""
        defined_object_dict = {}
        
        if defined_object.get_category() is not None:
            defined_object_dict['category'] = defined_object.get_category()
        if defined_object.get_is_source() is not None:
            defined_object_dict['is_source'] = defined_object.get_is_source()
        if defined_object.get_is_destination() is not None:
            defined_object_dict['is_destination'] = defined_object.get_is_destination()
        if defined_object.get_Address_Value() is not None:
            defined_object_dict['address_value'] = Base_Object_Attribute.dict_from_object(defined_object.get_Address_Value())
        if defined_object.get_Ext_Category() is not None:
            defined_object_dict['ext_category'] = Base_Object_Attribute.dict_from_object(defined_object.get_Ext_Category())
        if defined_object.get_VLAN_Name() is not None:
            defined_object_dict['vlan_name'] = Base_Object_Attribute.dict_from_object(defined_object.get_VLAN_Name())
        if defined_object.get_VLAN_Num() is not None:
            defined_object_dict['vlan_num'] = Base_Object_Attribute.dict_from_object(defined_object.get_VLAN_Num())
        return defined_object_dict
