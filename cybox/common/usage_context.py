# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.structured_text import StructuredText


class UsageContextAssumptions(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.UsageContextAssumptionsType
    _namespace = 'http://cybox.mitre.org/common-2'

    usage_context_assumption = fields.TypedField("Usage_Context_Assumption", StructuredText, multiple=True)
