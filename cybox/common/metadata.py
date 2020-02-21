# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding


class Metadata(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.MetadataType
    _namespace = 'http://cybox.mitre.org/common-2'

    type_ = fields.TypedField("type_", key_name="type")
    value = fields.TypedField("Value")
    subdatum = fields.TypedField("SubDatum", type_="cybox.common.metadata.Metadata", multiple=True)
