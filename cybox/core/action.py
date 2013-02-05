import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_binding
import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.common.measuresource import Measure_Source

class Action(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, action_dict):
        """Create the Action object representation from an input dictionary"""
        action_obj = core_binding.ActionType()
        for key, value in action_dict.items():
            if key == 'id' and utils.test_value(value): action_obj.set_id(value)
            elif key == 'idref' and utils.test_value(value): action_obj.set_idref(value)
            elif key == 'type' and utils.test_value(value): action_obj.set_type(value)
            elif key == 'name' and utils.test_value(value): action_obj.set_name(value)
            elif key == 'undefined_name' and utils.test_value(value): action_obj.set_undefined_name(value)
            elif key == 'ordinal_position' and utils.test_value(value): action_obj.set_ordinal_position(value)
            elif key == 'action_status' and utils.test_value(value): action_obj.set_action_status(value)
            elif key == 'context' and utils.test_value(value) : action_obj.set_context(value)
            elif key == 'network_protocol' and utils.test_value(value) : action_obj.set_network_protocol(value)
            elif key == 'timestamp' and utils.test_value(value) : action_obj.set_timestamp()
            elif key == 'description' : pass
            elif key == 'action_aliases' :
                action_aliases_obj = core_binding.ActionAliasesType()
                for action_alias in value:
                    if utils.test_value(action_alias) : action_aliases_obj.add_Action_Alias(action_alias)
                if action_aliases_obj.hasContent_() : action_obj.set_Action_Aliases(action_aliases_obj)
            elif key == 'action_arguments':
                action_arguments_obj = core_binding.ActionArgumentsType()
                for action_argument_dict in value:
                    action_argument_obj = cls.__action_argument_obj_from_dict(action_argument_dict)
                    if action_argument_obj.hasContent_() : action_arguments_obj.add_Action_Argument(action_argument_obj)
                if action_arguments_obj.hasContent_() : action_obj.set_Action_Arguments(action_arguments)
            elif key == 'discovery_method':
                measure_source_obj = Measure_Source.object_from_dict(value)
                if measure_source_obj.hasContent_() : action_obj.set_Discovery_Method(measure_source_obj)
            elif key == 'associated_objects':
                associated_objs = core_binding.AssociatedObjectsType()
                for associated_obj in value:
                    associated_objs.add_Associated_Object(associated_obj)
                if associated_objs.hasContent_() : action_obj.set_Associated_Objects(associated_objs)
            elif key == 'relationships':
                relationships_obj = core_binding.RelationshipsType()
                for relationship_dict in value:
                    relationships_obj.add_Relationship(cls.__action_relationship_obj_from_dict(relationship_dict))
            elif key == 'frequency': pass
        return action_obj

    @classmethod
    def dict_from_object(cls, action_obj):
        """Parse and return a dictionary for an Action object"""
        action_dict = {}
        return action_dict
      
    @classmethod
    def __action_argument_obj_from_dict(cls, action_argument_dict):
        action_argument_obj = core_binding.ActionArgumentType()
        for key, value in action_argument_dict.items():
            if key == 'defined_argument_name' and utils.test_value(value): action_argument_obj.set_defined_argument_name(value)
            elif key == 'undefined_argument_name' and utils.test_value(value): action_argument_obj.set_undefined_argument_name(value)
            elif key == 'argument_value' and utils.test_value(value): action_argument_obj.set_argument_value(value)
        return action_argument_obj
    
    @classmethod
    def __action_argument_dict_from_obj(cls, action_argument_obj):
        action_argument_dict = {}
        if action_argument_obj.get_defined_argument_name() is not None: action_argument_dict['defined_argument_name'] = action_argument_obj.get_defined_argument_name()
        if action_argument_obj.get_undefined_argument_name() is not None: action_argument_dict['undefined_argument_name'] = action_argument_obj.get_undefined_argument_name()
        if action_argument_obj.get_argument_value() is not None: action_argument_dict['argument_value'] = action_argument_obj.get_argument_value()
        return action_argument_dict

    @classmethod
    def __action_relationship_obj_from_dict(cls, action_relationship_dict):
        action_relationship_obj = core_binding.ActionRelationshipType()
        for key, value in action_relationship_dict.items():
            if key == 'type' and utils.test_value(value) : action_relationship_obj.set_type(value)
            if key == 'action_references':
                for action_reference in action_references:
                    action_reference_obj = core_binding.ActionReferenceType()
                    for action_reference_key, action_reference_value in action_reference.items():
                        if action_reference_key == 'action_id' and utils.test_value(action_reference_value):
                            action_reference_obj.set_action_id(value)
                    action_relationship_obj.add_Action_Reference(action_reference_obj)
        return action_relationship_obj

    @classmethod
    def __action_relationship_dict_from_obj(cls, action_relationship_obj):
        pass