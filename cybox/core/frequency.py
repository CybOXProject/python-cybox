# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_core as core_binding


class Frequency(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.FrequencyType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    rate = fields.TypedField("rate")
    units = fields.TypedField("units")
    scale = fields.TypedField("scale")
    trend = fields.TypedField("trend")
