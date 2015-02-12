# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""CybOX Action Reference Class"""

import cybox
import cybox.bindings.cybox_core as cybox_core_binding


class ActionReference(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, action_id=None):
        super(ActionReference, self).__init__()
        self.action_id = action_id

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        action_reference_obj = cybox_core_binding.ActionReferenceType()
        if self.action_id is not None:
            action_reference_obj.action_id = self.action_id
        return action_reference_obj

    def to_dict(self):
        action_reference_dict = {}
        if self.action_id is not None:
            action_reference_dict['action_id'] = self.action_id
        return action_reference_dict

    @staticmethod
    def from_dict(action_reference_dict):
        if not action_reference_dict:
            return None
        action_reference_ = ActionReference()
        action_reference_.action_id = action_reference_dict.get('action_id')
        return action_reference_

    @staticmethod
    def from_obj(action_reference_obj):
        if not action_reference_obj:
            return None
        action_reference_ = ActionReference()
        action_reference_.action_id = action_reference_obj.action_id
        return action_reference_
