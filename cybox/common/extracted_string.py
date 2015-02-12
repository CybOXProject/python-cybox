# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import String, HexBinary, PositiveInteger, HashList, VocabString


class CharacterEncoding(VocabString):
    _XSI_TYPE = 'cyboxVocabs:CharacterEncodingVocab-1.0'


class ExtractedString(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExtractedStringType
    _namespace = 'http://cybox.mitre.org/common-2'

    encoding = cybox.TypedField("Encoding", CharacterEncoding)
    string_value = cybox.TypedField("String_Value", String)
    byte_string_value = cybox.TypedField("Byte_String_Value", String)
    hashes = cybox.TypedField("Hashes", HashList)
    address = cybox.TypedField("Address", HexBinary)
    length = cybox.TypedField("Length", PositiveInteger)
    language = cybox.TypedField("Language", String)
    english_translation = cybox.TypedField("English_Translation", String)

    def __init__(self, string_value=None):
        super(ExtractedString, self).__init__()
        self.string_value = string_value


class ExtractedStrings(cybox.EntityList):
    _binding_class = common_binding.ExtractedStringsType
    _binding_var = "String"
    _contained_type = ExtractedString
    _namespace = 'http://cybox.mitre.org/common-2'
