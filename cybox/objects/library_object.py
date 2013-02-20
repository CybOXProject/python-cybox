import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.library_object_1_3 as library_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Library:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, library_attributes):
        """Create the Library Object object representation from an input dictionary"""
        libobject = library_binding.LibraryObjectType()
        libobject.set_anyAttributes_({'xsi:type' : 'LibraryObj:LibraryObjectType'})
        
        for key, value in library_attributes.items():
            if key == 'name' and utils.test_value(value): libobject.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'path' and utils.test_value(value): libobject.set_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'size' and utils.test_value(value): libobject.set_Size(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'),value))
            elif key == 'version' and utils.test_value(value): libobject.set_Version(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'type' and utils.test_value(value): libobject.set_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'base_address' and utils.test_value(value): libobject.set_Base_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
        return libobject

    @classmethod
    def dict_from_object(cls, object):
        """Parse and return a dictionary for a Library Object object"""
        object_dictionary = {}
        if object.get_Name() is not None: object_dictionary['name'] = Base_Object_Attribute.dict_from_object(object.get_Name())
        if object.get_Path() is not None: object_dictionary['path'] = Base_Object_Attribute.dict_from_object(object.get_Path())
        if object.get_Size() is not None: object_dictionary['size'] = Base_Object_Attribute.dict_from_object(object.get_Size())
        if object.get_Type() is not None: object_dictionary['type'] = Base_Object_Attribute.dict_from_object(object.get_Type())
        if object.get_Version() is not None: object_dictionary['version'] = Base_Object_Attribute.dict_from_object(object.get_Version())
        if object.get_Base_Address() is not None: object_dictionary['base_address'] = Base_Object_Attribute.dict_from_object(object.get_Base_Address())
        return object_dictionary
                                                            
