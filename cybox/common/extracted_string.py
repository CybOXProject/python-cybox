# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import (
    vocabs, String, HexBinary, PositiveInteger, HashList
)
from cybox.common.vocabs import CharacterEncoding


class ExtractedString(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExtractedStringType
    _namespace = 'http://cybox.mitre.org/common-2'

    encoding = vocabs.VocabField("Encoding", CharacterEncoding)
    string_value = fields.TypedField("String_Value", String)
    byte_string_value = fields.TypedField("Byte_String_Value", HexBinary)
    hashes = fields.TypedField("Hashes", HashList)
    address = fields.TypedField("Address", HexBinary)
    length = fields.TypedField("Length", PositiveInteger)
    language = fields.TypedField("Language", String)
    english_translation = fields.TypedField("English_Translation", String)

    def __init__(self, string_value=None):
        super(ExtractedString, self).__init__()
        self.string_value = string_value


class ExtractedStrings(entities.EntityList):
    _binding_class = common_binding.ExtractedStringsType
    _namespace = 'http://cybox.mitre.org/common-2'
    extracted_string = fields.TypedField("String", ExtractedString, multiple=True)