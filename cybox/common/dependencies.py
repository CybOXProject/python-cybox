# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.structured_text import StructuredText


class Dependency(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DependencyType
    _namespace = 'http://cybox.mitre.org/common-2'

    dependency_type = fields.TypedField("Dependency_Type")
    dependency_description = fields.TypedField("Dependency_Description", StructuredText)


class Dependencies(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DependenciesType
    _namespace = 'http://cybox.mitre.org/common-2'

    dependency = fields.TypedField("Dependency", Dependency, multiple=True)
