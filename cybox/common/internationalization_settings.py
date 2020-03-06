# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding


class InternalStrings(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.InternalStringsType
    _namespace = 'http://cybox.mitre.org/common-2'

    key = fields.TypedField("Key")
    content = fields.TypedField("Content")


class InternationalizationSettings(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.InternationalizationSettingsType
    _namespace = 'http://cybox.mitre.org/common-2'

    internal_strings = fields.TypedField("Internal_Strings", InternalStrings, multiple=True)
