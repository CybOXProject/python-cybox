# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import VocabString, StructuredText, MeasureSource
from cybox.core import ActionReference, AssociatedObject, Frequency


class ActionType(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ActionTypeVocab-1.0'


class ActionName(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ActionNameVocab-1.1'


class ActionAliases(cybox.EntityList):
    _binding = core_binding
    _binding_class = core_binding.ActionAliasesType
    _binding_var = "Action_Alias"
    _contained_type = cybox.Unicode
    _namespace = 'http://cybox.mitre.org/cybox-2'


class ArgumentName(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ActionArgumentNameVocab-1.0'


class ActionArgument(cybox.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionArgumentType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    argument_name = cybox.TypedField("Argument_Name", ArgumentName)
    argument_value = cybox.TypedField("Argument_Value")


class ActionArguments(cybox.EntityList):
    _binding_class = core_binding.ActionArgumentsType
    _binding_var = "Action_Argument"
    _contained_type = ActionArgument
    _namespace = 'http://cybox.mitre.org/cybox-2'


class AssociatedObjects(cybox.EntityList):
    _binding_class = core_binding.AssociatedObjectsType
    _binding_var = "Associated_Object"
    _contained_type = AssociatedObject
    _namespace = 'http://cybox.mitre.org/cybox-2'


class ActionRelationship(cybox.Entity):
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self):
        super(ActionRelationship, self).__init__()
        self.type = None
        self.action_references = []

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        action_relationship_obj = core_binding.ActionRelationshipType()
        if self.type is not None : action_relationship_obj.Type = self.type.to_obj(ns_info=ns_info)
        if len(self.action_references) > 0:
            for action_reference in self.action_references: action_relationship_obj.add_Action_Reference(action_reference.to_obj(ns_info=ns_info))
        return action_relationship_obj

    def to_dict(self):
        action_relationship_dict = {}
        if self.type is not None : action_relationship_dict['type'] = self.type.to_dict()
        if len(self.action_references) > 0:
            action_reference_list = []
            for action_reference in self.action_references: action_reference_list.append(action_reference.to_dict())
            action_relationship_dict['action_reference'] = action_reference_list
        return action_relationship_dict

    @staticmethod
    def from_dict(action_relationship_dict):
        if not action_relationship_dict:
            return None
        action_relationship_ = ActionRelationship()
        action_relationship_.type = ActionType.from_dict(action_relationship_dict.get('type'))
        action_relationship_.action_references = [ActionReference.from_dict(x) for x in action_relationship_dict.get('action_reference', [])]
        return action_relationship_

    @staticmethod
    def from_obj(action_relationship_obj):
        if not action_relationship_obj:
            return None
        action_relationship_ = ActionRelationship()
        action_relationship_.type = ActionType.from_obj(action_relationship_obj.Type)
        action_relationship_.action_references = [ActionReference.from_obj(x) for x in action_relationship_obj.Action_Reference]
        return action_relationship_


class ActionRelationships(cybox.EntityList):
    _binding_class = core_binding.ActionRelationshipsType
    _binding_var = "Relationship"
    _contained_type = ActionRelationship
    _namespace = 'http://cybox.mitre.org/cybox-2'


class Action(cybox.Entity):
    _binding = core_binding
    _binding_class = core_binding.ActionType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    id_ = cybox.TypedField("id")
    idref = cybox.TypedField("idref")
    ordinal_position = cybox.TypedField("ordinal_position")
    action_status = cybox.TypedField("action_status")
    context = cybox.TypedField("context")
    timestamp = cybox.TypedField("timestamp")

    type_ = cybox.TypedField("Type", ActionType)
    name = cybox.TypedField("Name", ActionName)
    description = cybox.TypedField("Description", StructuredText)
    action_aliases = cybox.TypedField("Action_Aliases", ActionAliases)
    action_arguments = cybox.TypedField("Action_Arguments", ActionArguments)
    discovery_method = cybox.TypedField("Discovery_Method", MeasureSource)
    associated_objects = cybox.TypedField("Associated_Objects",
            AssociatedObjects)
    relationships = cybox.TypedField("Relationships", ActionRelationships)
    frequency = cybox.TypedField("Frequency", Frequency)


class Actions(cybox.EntityList):
    _binding_class = core_binding.ActionsType
    _binding_var = "Action"
    _contained_type = Action
    _namespace = 'http://cybox.mitre.org/cybox-2'
