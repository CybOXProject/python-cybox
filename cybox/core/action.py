# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import VocabString, StructuredText, MeasureSource
from cybox.core import ActionReference, AssociatedObject


class Action(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self):
        super(Action, self).__init__()
        self.id = None
        self.idref = None
        self.type = None
        self.name = None
        self.ordinal_position = None
        self.action_status = None
        self.context = None
        self.timestamp = None
        self.description = None
        self.action_aliases = []
        self.action_arguments = ActionArguments()
        self.discovery_method = None
        self.associated_objects = AssociatedObjects()
        self.relationships = ActionRelationships()
        self.frequency = None
        
    def to_obj(self, action_obj = None):
        if action_obj == None:
            action_obj = core_binding.ActionType()
        if self.id is not None: action_obj.set_id(self.id)
        if self.idref is not None: action_obj.set_idref(self.idref)
        if self.ordinal_position is not None: action_obj.set_ordinal_position(self.ordinal_position)
        if self.action_status is not None: action_obj.set_action_status(self.action_status)
        if self.context is not None: action_obj.set_context(self.context)
        if self.timestamp is not None: action_obj.set_timestamp(self.timestamp)
        if self.type is not None: action_obj.set_Type(self.type.to_obj())
        if self.name is not None: action_obj.set_Name(self.name.to_obj())
        if self.description is not None: action_obj.set_Description(self.description.to_obj())
        if len(self.action_aliases) > 0:
            action_aliases_obj = core_binding.ActionAliasesType()
            for action_alias in self.action_aliases:
                action_aliases_obj.add_Action_Alias(action_alias)
            action_obj.set_Action_Aliases(action_aliases_obj)
        if len(self.action_arguments) > 0: action_obj.set_Action_Arguments(self.action_arguments.to_obj())
        if self.discovery_method is not None: action_obj.set_Discovery_Method(self.discovery_method.to_obj())
        if len(self.associated_objects) > 0: action_obj.set_Associated_Objects(self.associated_objects.to_obj())
        if len(self.relationships) > 0: action_obj.set_Relationships(self.relationships.to_obj())
        if self.frequency is not None: action_obj.set_Frequency(self.frequency.to_obj())
        
        return action_obj

    def to_dict(self):
        action_dict = {}
        if self.id is not None: action_dict['id'] = self.id
        if self.idref is not None: action_dict['idref'] = self.idref
        if self.ordinal_position is not None: action_dict['ordinal_position'] = self.ordinal_position
        if self.action_status is not None: action_dict['action_status'] = self.action_status
        if self.context is not None: action_dict['context'] = self.context
        if self.timestamp is not None: action_dict['timestamp'] = self.timestamp
        if self.type is not None: action_dict['type'] = self.type.to_dict()
        if self.name is not None: action_dict['name'] = self.name.to_dict()
        if self.description is not None: action_dict['description'] = self.description.to_dict()
        if len(self.action_aliases) > 0: action_dict['action_aliases'] = [x for x in self.action_aliases]
        if len(self.action_arguments) > 0: action_dict['action_arguments'] = self.action_arguments.to_list()
        if self.discovery_method is not None: action_dict['discovery_method'] = self.discovery_method.to_dict()
        if len(self.associated_objects) > 0: action_dict['associated_objects'] = self.associated_objects.to_list()
        if len(self.relationships) > 0: action_dict['relationships'] = self.relationships.to_list()
        if self.frequency is not None: action_dict['frequency'] = self.frequency.to_dict()
        return action_dict

    @staticmethod
    def from_dict(action_dict, action_cls = None):
        if not action_dict:
            return None
        if action_cls == None:
            action_cls = Action()
        action_ = action_cls
        action_.id = action_dict.get('id')
        action_.idref = action_dict.get('idref')
        action_.ordinal_position = action_dict.get('ordinal_position')
        action_.action_status = action_dict.get('action_status')
        action_.context = action_dict.get('context')
        action_.timestamp = action_dict.get('timestamp')
        action_.type = VocabString.from_dict(action_dict.get('type'))
        action_.name = VocabString.from_dict(action_dict.get('name'))
        action_.description = StructuredText.from_dict(action_dict.get('description'))
        action_.action_aliases = action_dict.get('action_aliases', [])
        action_.action_arguments = ActionArguments.from_list(action_dict.get('action_arguments', []))
        action_.discovery_method = MeasureSource.from_dict(action_dict.get('discovery_method'))
        action_.associated_objects = AssociatedObjects.from_list(action_dict.get('associated_objects', []))
        action_.relationships = ActionRelationships.from_list(action_dict.get('relationships', []))
        #action_.frequency = Frequency.from_dict(action_dict.get('frequency')) #TODO: add support
        return action_

    @staticmethod
    def from_obj(action_obj, action_cls = None):
        if not action_obj:
            return None
        if action_cls == None:
            action_cls = Action()
        action_ = action_cls
        action_.id = action_obj.get_id()
        action_.idref = action_obj.get_idref()
        action_.ordinal_position = action_obj.get_ordinal_position()
        action_.action_status = action_obj.get_action_status()
        action_.context = action_obj.get_context()
        action_.timestamp = action_obj.get_timestamp()
        action_.type = VocabString.from_obj(action_obj.get_Type())
        action_.name = VocabString.from_obj(action_obj.get_Name())
        action_.description = StructuredText.from_obj(action_obj.get_Description())
        if action_obj.get_Action_Arguments() is not None: action_.action_arguments = ActionArguments.from_obj(action_obj.get_Action_Arguments())
        action_.discovery_method = MeasureSource.from_obj(action_obj.get_Discovery_Method())
        if action_obj.get_Associated_Objects() is not None : action_.associated_objects = AssociatedObjects.from_obj(action_obj.get_Associated_Objects())
        if action_obj.get_Relationships() is not None : action_.relationships = ActionRelationships.from_obj(action_obj.get_Relationships())
        #action_.frequency = Frequency.from_dict(action_dict.get('frequency')) #TODO: add support
        if action_obj.get_Action_Aliases() is not None :
            action_.action_aliases = action_obj.get_Action_Aliases().get_Action_Alias()
        return action_


class ActionArgument(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self):
        super(ActionArgument, self).__init__()
        self.argument_name = None
        self.argument_value = None

    def to_obj(self):
        action_argument_obj = core_binding.ActionArgumentType()
        if self.argument_name is not None: action_argument_obj.set_Argument_Name(self.argument_name.to_obj())
        if self.argument_value is not None: action_argument_obj.set_Argument_Value(self.argument_value)
        return action_argument_obj

    def to_dict(self):
        action_argument_dict = {}
        if self.argument_name is not None: action_argument_dict['argument_name'] = self.argument_name.to_dict()
        if self.argument_value is not None: action_argument_dict['argument_value'] = self.argument_value
        return action_argument_dict

    @staticmethod
    def from_dict(action_argument_dict):
        if not action_argument_dict:
            return None
        action_argument_ = ActionArgument()
        action_argument_.argument_name = VocabString.from_dict(action_argument_dict.get('argument_name'))
        action_argument_.argument_value = action_argument_dict.get('argument_value')
        return action_argument_

    @classmethod
    def from_obj(action_argument_obj):
        if not action_argument_obj:
            return None
        action_argument_ = ActionArgument()
        action_argument_.argument_name = VocabString.from_obj(action_argument_obj.get_Argument_Name())
        action_argument_.argument_value = action_argument_obj.get_Argument_Value()
        return action_argument_


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
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self):
        super(ActionRelationship, self).__init__()
        self.type = None
        self.action_references = []

    def to_obj(self):
        action_relationship_obj = core_binding.ActionRelationshipType()
        if self.type is not None : action_relationship_obj.set_Type(self.type.to_obj())
        if len(self.action_references) > 0:
            for action_reference in self.action_references: action_relationship_obj.add_Action_Reference(action_reference.to_obj())
        return action_relationship_obj

    def to_dict(self):
        action_relationship_dict = {}
        if self.type is not None : action_relationship_dict['type'] = self.type.to_dict()
        if len(self.action_references) > 0:
            action_reference_list = []
            for action_reference in self.action_references: action_reference_list.append(action_reference.to_dict())
            action_relationship_dict['action_references'] = action_reference_list
        return action_relationship_dict

    @staticmethod
    def from_dict(action_relationship_dict):
        if not action_relationship_dict:
            return None
        action_relationship_ = ActionRelationship()
        action_relationship_.type = VocabString.from_dict(action_relationship_dict.get('type'))
        action_relationship_.action_references = [ActionReference.from_dict(x) for x in action_relationship_dict.get('action_references')]
        return action_relationship_

    @staticmethod
    def from_obj(action_relationship_obj):
        if not action_relationship_obj:
            return None
        action_relationship_ = ActionRelationship()
        action_relationship_.type = VocabString.from_obj(action_relationship_obj.get_Type())
        action_relationship_.action_references = [ActionReference.from_obj(x) for x in action_relationship_obj.get_Action_Reference()]
        return action_relationship_


class ActionRelationships(cybox.EntityList):
    _binding_class = core_binding.RelationshipsType
    _binding_var = "Relationship"
    _contained_type = ActionRelationship
    _namespace = 'http://cybox.mitre.org/cybox-2'
