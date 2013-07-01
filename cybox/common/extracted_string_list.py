# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_types_binding
from cybox.common.extracted_string import ExtractedString


class ExtractedStrings(cybox.EntityList):
    _binding_class = common_types_binding.ExtractedStringsType
    _binding_var = "String"
    _contained_type = ExtractedString
    _namespace = 'http://cybox.mitre.org/common-2'
