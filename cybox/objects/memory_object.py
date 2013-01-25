import maec_bundle_3_0 as maecbundle
import cybox.memory_object_1_2 as cybox_memory_object

class memory_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, memory_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='Memory Page')
        mem_object = cybox_memory_object.MemoryObjectType()
        mem_object.set_anyAttributes_({'xsi:type' : 'MemoryObj:MemoryObjectType'})
        #set object attributes
        for key,value in memory_attributes.items():
            if key == 'address' and self.__value_test(value):
                mem_object.set_Region_Start_Address(maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(datatype='hexBinary', valueOf_=maecbundle.quote_xml(value)))
            if key == 'size' and self.__value_test(value):
                mem_object.set_Region_Size(maecbundle.cybox_common_types_1_0.UnsignedLongObjectAttributeType(datatype='UnsignedLong', valueOf_=value))
            elif key == 'association':
                cybox_object.set_association_type(value)
                
        if mem_object.hasContent_():
            cybox_object.set_Defined_Object(mem_object)
        
        return cybox_object