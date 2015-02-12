# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import ExtractedStrings, ObjectProperties, String


class Imports(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.ImportsType
    _binding_var = "Import"
    _contained_type = String
    _namespace = 'http://cybox.mitre.org/common-2'


class Functions(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.FunctionsType
    _binding_var = "Function"
    _contained_type = String
    _namespace = 'http://cybox.mitre.org/common-2'


class CodeSnippets(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CodeSnippetsType
    _binding_var = "Code_Snippet"
    _contained_type = ObjectProperties
    _namespace = 'http://cybox.mitre.org/common-2'


class ExtractedFeatures(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExtractedFeaturesType
    _namespace = 'http://cybox.mitre.org/common-2'

    strings = cybox.TypedField("Strings", ExtractedStrings)
    imports = cybox.TypedField("Imports", Imports)
    functions = cybox.TypedField("Functions", Functions)
    code_snippets = cybox.TypedField("Code_Snippets", CodeSnippets)
