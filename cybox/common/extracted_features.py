# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.object_properties import ObjectProperties, ObjectPropertiesFactory
from cybox.common import ExtractedStrings, String


class Imports(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.ImportsType
    _namespace = 'http://cybox.mitre.org/common-2'
    import_ = fields.TypedField("Import", String, multiple=True)


class Functions(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.FunctionsType
    _namespace = 'http://cybox.mitre.org/common-2'
    function = fields.TypedField("Function", String, multiple=True)


class CodeSnippets(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CodeSnippetsType
    _namespace = 'http://cybox.mitre.org/common-2'
    code_snippet = fields.TypedField("Code_Snippet", ObjectProperties, factory=ObjectPropertiesFactory, multiple=True)


class ExtractedFeatures(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExtractedFeaturesType
    _namespace = 'http://cybox.mitre.org/common-2'

    strings = fields.TypedField("Strings", ExtractedStrings)
    imports = fields.TypedField("Imports", Imports)
    functions = fields.TypedField("Functions", Functions)
    code_snippets = fields.TypedField("Code_Snippets", CodeSnippets)
