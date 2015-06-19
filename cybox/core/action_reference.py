# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""CybOX Action Reference Class"""

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_core as core_binding


class ActionReference(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionReferenceType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    action_id = fields.TypedField("action_id")

    def __init__(self, action_id=None):
        super(ActionReference, self).__init__()
        self.action_id = action_id
