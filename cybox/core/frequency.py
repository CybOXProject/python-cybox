# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding


class Frequency(cybox.Entity):
    _binding = core_binding
    _binding_class = core_binding.FrequencyType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    rate = cybox.TypedField("rate")
    units = cybox.TypedField("units")
    scale = cybox.TypedField("scale")
    trend = cybox.TypedField("trend")
