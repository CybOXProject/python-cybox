# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import datetime

from mixbox import entities
from mixbox import fields

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import StructuredText, MeasureSource
from cybox.common.vocabs import VocabField
from cybox.core import ActionReference, AssociatedObject, Frequency

from cybox.common.vocabs import ActionName, ActionType
from cybox.common.vocabs import ActionArgumentName as ArgumentName


class ActionAliases(entities.EntityList):
    _binding = core_binding
    _binding_class = core_binding.ActionAliasesType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    action_alias = fields.TypedField("Action_Alias", cybox.Unicode, multiple=True)


class ActionArgument(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionArgumentType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    argument_name = VocabField("Argument_Name", ArgumentName)
    argument_value = fields.TypedField("Argument_Value")


class ActionArguments(entities.EntityList):
    _binding_class = core_binding.ActionArgumentsType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    action_argument = fields.TypedField("Action_Argument", ActionArgument, multiple=True)


class AssociatedObjects(entities.EntityList):
    _binding_class = core_binding.AssociatedObjectsType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    associated_object = fields.TypedField("Associated_Object", AssociatedObject, multiple=True)

class ActionRelationship(entities.Entity):
    _binding = core_binding
    _binding_class = _binding.ActionRelationshipType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    type = VocabField("Type", ActionType)
    action_references = fields.TypedField("Action_Reference", ActionReference, multiple=True)


class ActionRelationships(entities.EntityList):
    _binding_class = core_binding.ActionRelationshipsType
    _binding_var = "Relationship"
    _contained_type = ActionRelationship
    _namespace = 'http://cybox.mitre.org/cybox-2'
    relationship = fields.TypedField("Relationship", ActionRelationship, multiple=True)

class Action(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    id_ = fields.TypedField("id")
    idref = fields.TypedField("idref")
    ordinal_position = fields.TypedField("ordinal_position")
    action_status = fields.TypedField("action_status")
    context = fields.TypedField("context")
    timestamp = fields.DateTimeField("timestamp")
    type_ = VocabField("Type", ActionType)
    name = VocabField("Name", ActionName)
    description = fields.TypedField("Description", StructuredText)
    action_aliases = fields.TypedField("Action_Aliases", ActionAliases)
    action_arguments = fields.TypedField("Action_Arguments", ActionArguments)
    discovery_method = fields.TypedField("Discovery_Method", MeasureSource)
    associated_objects = fields.TypedField("Associated_Objects", AssociatedObjects)
    relationships = fields.TypedField("Relationships", ActionRelationships)
    frequency = fields.TypedField("Frequency", Frequency)


class Actions(entities.EntityList):
    _binding_class = core_binding.ActionsType
    _namespace = 'http://cybox.mitre.org/cybox-2'
    action = fields.TypedField("Action", Action, multiple=True)