import maec_bundle_3_0 as maecbundle
import cybox.library_object_1_3 as cybox_library_object

class library_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, library_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.id, type_="Module")
        libobject = cybox_library_object.LibraryObjectType()
        libobject.set_anyAttributes_({'xsi:type' : 'LibraryObj:LibraryObjectType'})
        
        for key, value in library_attributes.items():
            if key == 'name' and self.__value_test(value):
                libobject.set_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'path' and self.__value_test(value):
                libobject.set_Path(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'size' and self.__value_test(value):
                libobject.set_Size(maecbundle.cybox_common_types_1_0.UnsignedLongObjectAttributeType(valueOf_=maecbundle.quote_xml(value)))
            elif key == 'version' and self.__value_test(value):
                libobject.set_Version(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
            elif key == 'type' and self.__value_test(value):
                if value == 'static':
                    libobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Static"))
                elif value == 'dynamic':
                    libobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Dynamic"))
                elif value == 'remote':
                    libobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Remote"))
                elif value == 'shared':
                    libobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Shared"))
                elif value == 'other':
                    libobject.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_="Other"))
            elif (key == 'base_address' or key == 'address') and self.__value_test(value):
                libobject.set_Base_Address(maecbundle.cybox_common_types_1_0.HexBinaryObjectAttributeType(valueOf_=value));
            elif key == 'association' and self.__value_test(value):
                cybox_object.set_association_type(value)
        
        if libobject.hasContent_():
            cybox_object.set_Defined_Object(libobject)
        
        return cybox_object