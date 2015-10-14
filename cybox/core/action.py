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
    _binding_var = "Action_Alias"
    _contained_type = cybox.Unicode
    _namespace = 'http://cybox.mitre.org/cybox-2'


class ActionArgument(entities.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionArgumentType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    argument_name = VocabField("Argument_Name", ArgumentName)
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

    type = VocabField("Type", ActionType)
    action_references = fields.TypedField("Action_Reference", ActionReference, multiple=True)


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
    timestamp = fields.DateTimeField("timestamp")
    type_ = VocabField("Type", ActionType)
    name = VocabField("Name", ActionName)
    description = fields.TypedField("Description", StructuredText)
    action_aliases = fields.TypedField("Action_Aliases", ActionAliases)
    action_arguments = fields.TypedField("Action_Arguments", ActionArguments)
    discovery_method = fields.TypedField("Discovery_Method", MeasureSource)
    associated_objects = fields.TypedField("Associated_Objects",
            AssociatedObjects)
    relationships = fields.TypedField("Relationships", ActionRelationships)
    frequency = fields.TypedField("Frequency", Frequency)


class Actions(entities.EntityList):
    _binding_class = core_binding.ActionsType
    _binding_var = "Action"
    _contained_type = Action
    _namespace = 'http://cybox.mitre.org/cybox-2'
