import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.memory_object_1_2 as memory_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.hashlist import Hash_List

class Memory:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, memory_attributes):
        """Create the Memory Object object representation from an input dictionary"""
        mem_object = memory_binding.MemoryObjectType()
        mem_object.set_anyAttributes_({'xsi:type' : 'MemoryObj:MemoryObjectType'})
        for key,value in memory_attributes.items():
            if key == 'is_injected' and utils.test_value(value): mem_object.set_is_injected(value.get('value'))
            elif key == 'is_mapped' and utils.test_value(value): mem_object.set_is_mapped(value.get('value'))
            elif key == 'is_protected' and utils.test_value(value): mem_object.set_is_injected(value.get('value'))
            elif key == 'region_start_address' and utils.test_value(value):
                mem_object.set_Region_Start_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'region_size' and utils.test_value(value):
                mem_object.set_Region_Size(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'),value))            
            elif key == 'name' and utils.test_value(value):
                mem_object.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))          
            elif key == 'hashes':
                mem_object.set_Hashes(Hash_List.object_from_dict(value))

        return mem_object

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Memory Object object"""
        defined_object_dict = {}
        if defined_object.get_is_injected() is not None: defined_object_dict['is_injected'] = {'value' : defined_object.get_is_injected()}
        if defined_object.get_is_mapped() is not None: defined_object_dict['is_mapped'] = {'value' : defined_object.get_is_mapped()}
        if defined_object.get_is_protected() is not None: defined_object_dict['is_protected'] = {'value' : defined_object.get_is_protected()}
        if defined_object.get_Hashes() is not None: defined_object_dict['hashes'] = Hash_List.dict_from_object(defined_object.get_Hashes())
        if defined_object.get_Name() is not None: defined_object_dict['name'] = Base_Object_Attribute.dict_from_object(defined_object.get_Name())
        if defined_object.get_Region_Size() is not None: defined_object_dict['region_size'] = Base_Object_Attribute.dict_from_object(defined_object.get_Region_Size())
        if defined_object.get_Region_Start_Address() is not None: defined_object_dict['region_start_address'] = Base_Object_Attribute.dict_from_object(defined_object.get_Region_Start_Address())
        return defined_object_dict