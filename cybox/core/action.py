import cybox
import cybox.utils as utils
import cybox.bindings.cybox_core_1_0 as core_binding
#import cybox.core.structured_text as Structured_Text
#from cybox.common.measuresource import Measure_Source
#from cybox.common.baseobjectattribute import Base_Object_Attribute
#from cybox.common.measuresource import Measure_Source
from cybox.core.associated_object import AssociatedObject

class Action(cybox.Entity):
    def __init__(self):
        self.id = None
        self.idref = None
        self.type = None
        self.name = None
        self.undefined_name = None
        self.ordinal_position = None
        self.action_status = None
        self.context = None
        self.network_protocol = None
        self.timestamp = None
        self.description = None
        self.action_aliases = []
        self.action_arguments = []
        self.discovery_method = None
        self.associated_objects = []
        self.relationships = []
        self.frequency = None
        
    def to_obj(self, action_obj = None):
        if action_obj == None:
            action_obj = core_binding.ActionType()
        if self.id is not None: action_obj.set_id(self.id)
        if self.idref is not None: action_obj.set_idref(self.idref)
        if self.type is not None: action_obj.set_type(self.type)
        if self.name is not None: action_obj.set_name(self.name)
        if self.undefined_name is not None: action_obj.set_undefined_name(self.undefined_name)
        if self.ordinal_position is not None: action_obj.set_ordinal_position(self.ordinal_position)
        if self.action_status is not None: action_obj.set_action_status(self.action_status)
        if self.context is not None: action_obj.set_context(self.context)
        if self.network_protocol is not None: action_obj.set_network_protocol(self.network_protocol)
        if self.timestamp is not None: action_obj.set_timestamp(self.timestamp)
        if self.description is not None: action_obj.set_description(self.description.to_obj())
        if len(self.action_aliases) > 0:
            action_aliases_obj = core_binding.ActionAliasesType()
            for action_alias in self.action_aliases:
                action_aliases_obj.add_Action_Alias(action_alias)
            action_obj.set_Action_Aliases(action_aliases_obj)
        if len(self.action_arguments) > 0:
            action_arguments_obj = core_binding.ActionArgumentsType()
            for action_argument in self.action_arguments:
                action_arguments_obj.add_Action_Argument(action_argument.to_obj())
            action_obj.set_Action_Arguments(action_arguments_obj)
        if self.discovery_method is not None: action_obj.set_Discovery_Method(self.discovery_method.to_obj())
        if len(self.associated_objects) > 0: 
            associated_objects_obj = core_binding.AssociatedObjectsType()
            for associated_object in self.associated_objects:
                associated_objects_obj.add_Associated_Object(associated_object.to_obj())
            action_obj.set_Associated_Objects(associated_objects_obj)
        if len(self.relationships) > 0:
            relationships_obj = core_binding.RelationshipsType()
            for relationship in self.relationships:
                relationships_obj.add_Relationship(relationship.to_obj())
            action_obj.set_Relationships(relationships_obj)
        if self.frequency is not None: action_obj.set_Frequency(self.frequency.to_obj())
        
        return action_obj

    def to_dict(self):
        action_dict = {}
        return action_dict

    def from_obj(action_obj):
        pass

    @staticmethod
    def from_dict(action_dict, action_cls = None):
        if not action_dict:
            return None
        if action_cls == None:
            action_cls = Action()
        action_ = action_cls
        action_.id = action_dict.get('id')
        action_.idref = action_dict.get('id')
        action_.type = action_dict.get('type')
        action_.name = action_dict.get('name')
        action_.undefined_name = action_dict.get('undefined_name')
        action_.ordinal_position = action_dict.get('ordinal_position')
        action_.action_status = action_dict.get('action_status')
        action_.context = action_dict.get('context')
        action_.network_protocol = action_dict.get('network_protocol')
        action_.timestamp = action_dict.get('timestamp')
        #action_.description = StructuredText.from_dict(action.get('description'))
        action_.action_aliases = action_dict.get('action_aliases', [])
        action_.action_arguments = [ActionArgument.from_dict(x) for x in action_dict.get('action_arguments', [])]
        #action_.discovery_method = MeasureSource.from_dict(action_dict.get('discovery_method'))
        action_.associated_objects = [AssociatedObject.from_dict(x) for x in action_dict.get('associated_objects', [])]
        action_.relationships = [ActionRelationship.from_dict(x) for x in action_dict.get('relationships', [])]
        #action_.frequency = Frequency.from_dict(action_dict.get('frequency'))
        return action_

    @staticmethod
    def from_obj(action_obj):
        pass

class ActionArgument(cybox.Entity):
    def __init__(self):
        self.defined_argument_name = None
        self.undefined_argument_name = None
        self.argument_value = None

    def to_obj(self):
        action_argument_obj = core_binding.ActionArgumentType()
        if self.defined_argument_name is not None: action_argument_obj.set_defined_argument_name(self.defined_argument_name)
        if self.undefined_argument_name is not None: action_argument_obj.set_undefined_argument_name(self.undefined_argument_name)
        if self.argument_value is not None: action_argument_obj.set_argument_value(self.argument_value)
        return action_argument_obj

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(action_argument_dict):
        if not action_argument_dict:
            return None
        action_argument_ = ActionArgument()
        action_argument_.defined_argument_name = action_argument_dict.get('defined_argument_name')
        action_argument_.undefined_argument_name = action_argument_dict.get('undefined_argument_name')
        action_argument_.argument_value = action_argument_dict.get('argument_value')
        return action_argument_

    @classmethod
    def from_obj(action_argument_obj):
        pass

class ActionRelationship(cybox.Entity):
    def __init__(self):
        self.type = None
        self.action_references = []

    def to_obj(self):
        action_relationship_obj = core_binding.ActionRelationshipType()
        if self.type is not None: action_relationship_obj.set_type_(self.type)
        if self.action_references is not None: 
            for action_reference in self.action_references:
                action_relationship_obj.add_Action_Reference(core_binding.ActionReferenceType(action_id=action_reference))

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(action_relationship_dict):
        if not action_relationship_dict:
            return None
        action_relationship_ = ActionRelationship()
        action_relationship_.type = action_relationship_dict.get('type')
        action_relationship_.action_references = action_relationship_dict.get('action_references')
        return action_relationship_

    @staticmethod
    def from_obj(action_relationship_obj):
        pass