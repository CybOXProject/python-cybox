# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import String, StructuredText


class PlatformIdentifier(String):
    _binding = common_binding
    _binding_class = _binding.PlatformIdentifierType
    _namespace = 'http://cybox.mitre.org/common-2'

    system = fields.TypedField("system")
    system_ref = fields.TypedField("system_ref")


class PlatformSpecification(entities.Entity):
    """CybOX Common PlatformSpecification object representation"""
    _namespace = 'http://cybox.mitre.org/common-2'
    _binding = common_binding
    _binding_class = _binding.PlatformSpecificationType

    description = fields.TypedField("Description", StructuredText)
    identifiers = fields.TypedField("Identifier", PlatformIdentifier, multiple=True)
