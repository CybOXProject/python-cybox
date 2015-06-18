# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.as_object as as_binding
from cybox.common import NonNegativeInteger, ObjectProperties, String


class AutonomousSystem(ObjectProperties):
    _binding = as_binding
    _binding_class = as_binding.ASObjectType
    _namespace = "http://cybox.mitre.org/objects#ASObject-1"
    _XSI_NS = "ASObj"
    _XSI_TYPE = "ASObjectType"

    number = fields.TypedField("Number", NonNegativeInteger)
    name = fields.TypedField("Name", String)
    handle = fields.TypedField("Handle", String)
    regional_internet_registry = fields.TypedField("Regional_Internet_Registry", String)

# Add alias for the "proper", but completely unhelpful name, "AS"
AS = AutonomousSystem
