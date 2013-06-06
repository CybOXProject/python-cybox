# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_types_binding
from cybox.common.extracted_string import ExtractedString

class ExtractedStrings(cybox.EntityList):
    _contained_type = ExtractedString
    _binding_class = common_types_binding.ExtractedStringsType

    def __init__(self):
        super(ExtractedStrings, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_String(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_String()