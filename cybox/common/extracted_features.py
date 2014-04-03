# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
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

    def __init__(self):
        super(ExtractedFeatures, self).__init__()
        self.strings = None
        self.imports = None
        self.functions = None
        self.code_snippets = None

    def to_obj(self):
        extracted_features_obj = common_binding.ExtractedFeaturesType()
        if self.strings is not None : extracted_features_obj.set_Strings(self.strings.to_obj())
        if self.imports is not None : extracted_features_obj.set_Imports(self.imports.to_obj())
        if self.functions is not None : extracted_features_obj.set_Functions(self.functions.to_obj())
        if self.code_snippets is not None : extracted_features_obj.set_Code_Snippets(self.code_snippets.to_obj())
        return extracted_features_obj

    def to_dict(self):
        extracted_features_dict = {}
        if self.strings is not None : extracted_features_dict['strings'] = self.strings.to_list()
        if self.imports is not None : extracted_features_dict['imports'] = self.imports.to_list()
        if self.functions is not None : extracted_features_dict['functions'] = self.functions.to_list()
        if self.code_snippets is not None : extracted_features_dict['code_snippets'] = self.code_snippets.to_list()
        return extracted_features_dict
        
    @staticmethod
    def from_dict(extracted_features_dict):
        if not extracted_features_dict:
            return None
        extracted_features_ = ExtractedFeatures()
        extracted_features_.strings = ExtractedStrings.from_list(extracted_features_dict.get('strings'))
        extracted_features_.imports = Imports.from_list(extracted_features_dict.get('imports'))
        extracted_features_.functions = Functions.from_list(extracted_features_dict.get('functions'))
        extracted_features_.code_snippets = CodeSnippets.from_list(extracted_features_dict.get('code_snippets'))
        return extracted_features_
        
    @staticmethod
    def from_obj(extracted_features_obj):
        if not extracted_features_obj:
            return None
        extracted_features_ = ExtractedFeatures()
        extracted_features_.strings = ExtractedStrings.from_obj(extracted_features_obj.get_Strings())
        extracted_features_.imports = Imports.from_obj(extracted_features_obj.get_Imports())
        extracted_features_.functions = Functions.from_obj(extracted_features_obj.get_Functions())
        extracted_features_.code_snippets = CodeSnippets.from_obj(extracted_features_obj.get_Code_Snippets())
        return extracted_features_
