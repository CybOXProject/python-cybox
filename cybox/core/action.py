# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import datetime

from mixbox import entities
from mixbox import fields
from mixbox.dates import parse_datetime, serialize_datetime

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import vocabs, VocabString, StructuredText, MeasureSource
from cybox.core import ActionReference, AssociatedObject, Frequency

from cybox.common.vocabs import ActionName, ActionType
from cybox.common.vocabs import ActionArgumentName as ArgumentName


class ActionAliases(entities.EntityList):
    _binding = core_binding
    _binding_class = core_binding.ActionAliasesType
    _binding_var = "Action_Alias"
    _contained_type = cybox.Unicode
    _namespace = 'http://cybox.mitre.org/cybox-2'


class ActionArgument(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionArgumentType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    argument_name = vocabs.VocabField("Argument_Name", ArgumentName)
    argument_value = fields.TypedField("Argument_Value")


class ActionArguments(entities.EntityList):
    _binding_class = core_binding.ActionArgumentsType
    _binding_var = "Action_Argument"
    _contained_type = ActionArgument
    _namespace = 'http://cybox.mitre.org/cybox-2'


class AssociatedObjects(entities.EntityList):
    _binding_class = core_binding.AssociatedObjectsType
    _binding_var = "Associated_Object"
    _contained_type = AssociatedObject
    _namespace = 'http://cybox.mitre.org/cybox-2'


class ActionRelationship(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.ActionRelationshipType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self):
        super(ActionRelationship, self).__init__()
        self.type = None
        self.action_references = []

    def to_obj(self, ns_info=None):
        action_relationship_obj = super(ActionRelationship, self).to_obj(ns_info=ns_info)

        if self.type is not None : action_relationship_obj.Type = self.type.to_obj(ns_info=ns_info)
        if len(self.action_references) > 0:
            for action_reference in self.action_references: action_relationship_obj.add_Action_Reference(action_reference.to_obj(ns_info=ns_info))
        return action_relationship_obj

    def to_dict(self):
        action_relationship_dict = super(ActionRelationship, self).to_dict()

        if self.type is not None : action_relationship_dict['type'] = self.type.to_dict()
        if len(self.action_references) > 0:
            action_reference_list = []
            for action_reference in self.action_references: action_reference_list.append(action_reference.to_dict())
            action_relationship_dict['action_reference'] = action_reference_list
        return action_relationship_dict

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None
        
        action_relationship_ = super(ActionRelationship, cls).from_dict(cls_dict)
        action_relationship_.type = VocabString.from_dict(cls_dict.get('type'))
        action_relationship_.action_references = [ActionReference.from_dict(x) for x in cls_dict.get('action_reference', [])]
        return action_relationship_

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        action_relationship_ = super(ActionRelationship, cls).from_obj(cls_obj)
        action_relationship_.type = VocabString.from_obj(cls_obj.Type)
        action_relationship_.action_references = [ActionReference.from_obj(x) for x in cls_obj.Action_Reference]
        return action_relationship_


class ActionRelationships(entities.EntityList):
    _binding_class = core_binding.ActionRelationshipsType
    _binding_var = "Relationship"
    _contained_type = ActionRelationship
    _namespace = 'http://cybox.mitre.org/cybox-2'


class Action(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    id_ = fields.TypedField("id")
    idref = fields.TypedField("idref")
    ordinal_position = fields.TypedField("ordinal_position")
    action_status = fields.TypedField("action_status")
    context = fields.TypedField("context")
    timestamp = fields.TypedField("timestamp")

    type_ = vocabs.VocabField("Type", ActionType)
    name = vocabs.VocabField("Name", ActionName)
    description = fields.TypedField("Description", StructuredText)
    action_aliases = fields.TypedField("Action_Aliases", ActionAliases)
    action_arguments = fields.TypedField("Action_Arguments", ActionArguments)
    discovery_method = fields.TypedField("Discovery_Method", MeasureSource)
    associated_objects = fields.TypedField("Associated_Objects",
            AssociatedObjects)
    relationships = fields.TypedField("Relationships", ActionRelationships)
    frequency = fields.TypedField("Frequency", Frequency)

    def to_dict(self):
        d = super(Action, self).to_dict()
        # Don't add an empty timestamp if there isn't already one.
        if 'timestamp' in d:
            d['timestamp'] = serialize_datetime(d['timestamp'])
        return d

    @classmethod
    def from_dict(cls, action_dict):
        action = super(Action, cls).from_dict(action_dict)
        action.timestamp = parse_datetime(action.timestamp)
        return action


class Actions(entities.EntityList):
    _binding_class = core_binding.ActionsType
    _binding_var = "Action"
    _contained_type = Action
    _namespace = 'http://cybox.mitre.org/cybox-2'
