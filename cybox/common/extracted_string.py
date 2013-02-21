import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common.hashlist import Hash_List

class Extracted_String(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, extracted_string_dict):
        """Create the Extracted String object representation from an input dictionary"""
        extracted_string_object = common_types_binding.ExtractedStringType()
        for key, value in extracted_string_dict.items():
            if key == 'encoding' : 
                extracted_string_object.set_encoding(value.get('value'))
            elif key == 'string_value' : 
                extracted_string_object.set_String_Value(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'hashes' : 
                extracted_string_object.set_Hashes(Hash_List.object_from_dict(value))
            elif key == 'address' : 
                extracted_string_object.set_Address(Base_Object_Attribute.object_from_dict(common_types_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'length' : 
                extracted_string_object.set_Length(Base_Object_Attribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'),value))
            elif key == 'language' : 
                extracted_string_object.set_Language(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'english_translation' : 
                extracted_string_object.set_English_Translation(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))

        return extracted_string_object

    @classmethod
    def dict_from_object(cls, extracted_string_obj):
        """Parse and return a dictionary for an Extracted String object"""
        extracted_string_dict = {}
        if extracted_string_obj.get_encoding() is not None: extracted_string_dict['encoding'] = {'value' : element.get_encoding()}
        if extracted_string_obj.get_String_Value() is not None: extracted_string_dict['string_value'] = Base_Object_Attribute.dict_from_object(defined_object.get_String_Value())
        if extracted_string_obj.get_Hashes() is not None: extracted_string_dict['hashes'] = hashlist.dict_from_object(element.get_Hashes())
        if extracted_string_obj.get_Address() is not None: extracted_string_dict['address'] = Base_Object_Attribute.dict_from_object(defined_object.get_Address())
        if extracted_string_obj.get_Length() is not None: extracted_string_dict['length'] = Base_Object_Attribute.dict_from_object(defined_object.get_Length())
        if extracted_string_obj.get_Language() is not None: extracted_string_dict['language'] = Base_Object_Attribute.dict_from_object(defined_object.get_Language())
        if extracted_string_obj.get_English_Translation() is not None: extracted_string_dict['english_translation'] = Base_Object_Attribute.dict_from_object(defined_object.get_English_Translation())
        return extracted_string_dict