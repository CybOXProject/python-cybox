# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.custom_object as custom_binding
from cybox.common import ObjectProperties, String, StructuredText

class Custom(ObjectProperties):
    _binding = custom_binding
    _binding_class = custom_binding.CustomObjectType
    _namespace = "http://cybox.mitre.org/objects#CustomObject-1"
    _XSI_NS = "CustomObj"
    _XSI_TYPE = "CustomObjectType"

    custom_name = cybox.TypedField('custom_name')
    description = cybox.TypedField("Description", StructuredText)
