import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.library_object_1_3 as library_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class library_object:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, library_attributes):
        """Create the Library Object object representation from an input dictionary"""
        libobject = library_object_binding.LibraryObjectType()
        libobject.set_anyAttributes_({'xsi:type' : 'LibraryObj:LibraryObjectType'})
        
        for key, value in library_attributes.items():
            if key == 'name' and common_methods.test_value(value): libobject.set_Name(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'path' and common_methods.test_value(value): libobject.set_Path(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'size' and common_methods.test_value(value): libobject.set_Size(baseobjectattribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'),value))
            elif key == 'version' and common_methods.test_value(value): libobject.set_Version(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'type' and common_methods.test_value(value): libobject.set_Type(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'base_address' and common_methods.test_value(value): libobject.set_Base_Address(baseobjectattribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
        return cybox_object

    @classmethod
    def dict_from_object(cls, object):
        """Parse and return a dictionary for a Library Object object"""
        object_dictionary = {}
        if object.get_Name() is not None: object_dictionary['name'] = baseobjectattribute.dict_from_object(object.get_Name())
        if object.get_Path() is not None: object_dictionary['path'] = baseobjectattribute.dict_from_object(object.get_Path())
        if object.get_Size() is not None: object_dictionary['size'] = baseobjectattribute.dict_from_object(object.get_Size())
        if object.get_Type() is not None: object_dictionary['type'] = baseobjectattribute.dict_from_object(object.get_Type())
        if object.get_Version() is not None: object_dictionary['version'] = baseobjectattribute.dict_from_object(object.get_Version())
        if object.get_Base_Address() is not None: object_dictionary['base_address'] = baseobjectattribute.dict_from_object(object.get_Base_Address())
        return object_dictionary
                                                            
