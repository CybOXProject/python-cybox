import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.common.hashlist import hashlist

class extracted_string(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, extracted_string_attributes):
        """Create the Extracted String object representation from an input dictionary"""
        extracted_string_object = common_types_binding.ExtractedStringType()
        for key, value in extracted_string_attributes.items():
            if key == 'encoding' : 
                extracted_string_object.set_encoding(value.get('value'))
            elif key == 'string_value' : 
                extracted_string_object.set_String_Value(baseobjectattribute.create_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'hashes' : 
                extracted_string_object.set_Hashes(hashlist.create_from_dict(value))
            elif key == 'address' : 
                extracted_string_object.set_Address(baseobjectattribute.create_from_dict(common_binding.HexBinaryObjectAttributeType(datatype='hexBinary'),value))
            elif key == 'length' : 
                extracted_string_object.set_Length(baseobjectattribute.create_from_dict(common_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'),value))
            elif key == 'language' : 
                extracted_string_object.set_Language(baseobjectattribute.create_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'english_translation' : 
                extracted_string_object.set_English_Translation(baseobjectattribute.create_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))

        return extracted_string_object

    @classmethod
    def parse_into_dict(cls, element):
        """Parse and return a dictionary for an Extracted String object"""
        element_dict = {}
        if element.get_encoding() is not None: element_dict['encoding'] = {'value' : element.get_encoding()}
        if element.get_String_Value() is not None: element_dict['string_value'] = baseobjectattribute.parse_into_dict(defined_object.get_String_Value())
        if element.get_Hashes() is not None: element_dict['hashes'] = hashlist.parse_into_dict(element.get_Hashes())
        if element.get_Address() is not None: element_dict['address'] = baseobjectattribute.parse_into_dict(defined_object.get_Address())
        if element.get_Length() is not None: element_dict['length'] = baseobjectattribute.parse_into_dict(defined_object.get_Length())
        if element.get_Language() is not None: element_dict['language'] = baseobjectattribute.parse_into_dict(defined_object.get_Language())
        if element.get_English_Translation() is not None: element_dict['english_translation'] = baseobjectattribute.parse_into_dict(defined_object.get_English_Translation())
        return element_dict