# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import ExtractedStrings, ObjectProperties, String


class Imports(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.ImportsType
    _binding_var = "Import"
    _contained_type = String
    _namespace = 'http://cybox.mitre.org/common-2'


class Functions(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.FunctionsType
    _binding_var = "Function"
    _contained_type = String
    _namespace = 'http://cybox.mitre.org/common-2'


class CodeSnippets(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CodeSnippetsType
    _binding_var = "Code_Snippet"
    _contained_type = ObjectProperties
    _namespace = 'http://cybox.mitre.org/common-2'


class ExtractedFeatures(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExtractedFeaturesType
    _namespace = 'http://cybox.mitre.org/common-2'

    strings = fields.TypedField("Strings", ExtractedStrings)
    imports = fields.TypedField("Imports", Imports)
    functions = fields.TypedField("Functions", Functions)
    code_snippets = fields.TypedField("Code_Snippets", CodeSnippets)
