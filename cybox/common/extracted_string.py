# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_types_binding
from cybox.common import String, HexBinary, PositiveInteger, HashList, VocabString


class ExtractedString(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, string_value = None):
        super(ExtractedString, self).__init__()
        self.encoding = None
        self.string_value = string_value
        self.byte_string_value = None
        self.hashes = None
        self.address = None
        self.length = None
        self.language = None
        self.english_translation = None

    def to_obj(self):
        extracted_string_object = common_types_binding.ExtractedStringType()

        if self.encoding is not None: extracted_string_object.set_encoding(self.encoding.to_obj())
        if self.string_value is not None: extracted_string_object.set_String_Value(self.string_value.to_obj())
        if self.byte_string_value is not None: extracted_string_object.set_Byte_String_Value(self.byte_string_value.to_obj())
        if self.hashes is not None: extracted_string_object.set_Hashes(self.hashes.to_obj())
        if self.address is not None: extracted_string_object.set_Address(self.address.to_obj())
        if self.length is not None: extracted_string_object.set_Length(self.length.to_obj())
        if self.language is not None: extracted_string_object.set_Language(self.language.to_obj())
        if self.english_translation is not None: extracted_string_object.set_English_Translation(self.english_translation.to_obj())

        return extracted_string_object

    def to_dict(self):
        extracted_string_dict = {}

        if self.encoding is not None: extracted_string_dict['encoding'] = self.encoding.to_dict()
        if self.string_value is not None: extracted_string_dict['string_value'] = self.string_value.to_dict()
        if self.byte_string_value is not None: extracted_string_dict['byte_string_value'] = self.byte_string_value.to_dict()
        if self.hashes is not None: extracted_string_dict['hashes'] = self.hashes.to_list()
        if self.address is not None: extracted_string_dict['encoding'] = self.encoding.to_dict()
        if self.length is not None: extracted_string_dict['length'] = self.length.to_dict()
        if self.language is not None: extracted_string_dict['language'] = self.language.to_dict()
        if self.english_translation is not None: extracted_string_dict['english_translation'] = self.english_translation.to_dict()

        return extracted_string_dict

    @staticmethod
    def from_dict(extracted_string_dict):
        if not extracted_string_dict:
            return None

        extracted_string_ = ExtractedString()
        extracted_string_.encoding = VocabString.from_dict(extracted_string_dict.get('encoding'))
        extracted_string_.string_value = String.from_dict(extracted_string_dict.get('string_value'))
        extracted_string_.byte_string_value = HexBinary.from_dict(extracted_string_dict.get('byte_string_value'))
        extracted_string_.hashes = HashList.from_list(extracted_string_dict.get('hashes'))
        extracted_string_.address = HexBinary.from_dict(extracted_string_dict.get('address'))
        extracted_string_.length = PositiveInteger.from_dict(extracted_string_dict.get('length'))
        extracted_string_.language = String.from_dict(extracted_string_dict.get('language'))
        extracted_string_.english_translation = String.from_dict(extracted_string_dict.get('english_translation'))

        return extracted_string_

    @staticmethod
    def from_obj(extracted_string_obj):
        if not extracted_string_obj:
            return None

        extracted_string_ = ExtractedString()
        extracted_string_.encoding = VocabString.from_obj(extracted_string_obj.get_Encoding())
        extracted_string_.string_value = String.from_obj(extracted_string_obj.get_String_Value())
        extracted_string_.byte_string_value = HexBinary.from_obj(extracted_string_obj.get_Byte_String_Value())
        extracted_string_.hashes = HashList.from_obj(extracted_string_obj.get_Hashes())
        extracted_string_.address = HexBinary.from_obj(extracted_string_obj.get_Address())
        extracted_string_.length = PositiveInteger.from_obj(extracted_string_obj.get_Length())
        extracted_string_.language = String.from_obj(extracted_string_obj.get_Language())
        extracted_string_.english_translation = String.from_obj(extracted_string_obj.get_English_Translation())

        return extracted_string_


class ExtractedStrings(cybox.EntityList):
    _binding_class = common_types_binding.ExtractedStringsType
    _binding_var = "String"
    _contained_type = ExtractedString
    _namespace = 'http://cybox.mitre.org/common-2'
