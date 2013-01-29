import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class environment_variable(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, environment_variable_attributes):
        """Create the Environment Variable object representation from an input dictionary"""
        environment_variable_object = common_binding.EnvironmentVariableType()
        for key, value in environment_variable_attributes.items():
            if key == 'name' : 
                environment_variable_object.set_Name(baseobjectattribute.create_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'value' : 
                environment_variable_object.set_Value(baseobjectattribute.create_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
        return environment_variable_object

    @classmethod
    def parse_into_dict(cls, element):
        """Parse and return a dictionary for an Environment Variable object"""
        element_dict = {}
        if element.get_Name() is not None: element_dict['name'] = baseobjectattribute.parse_into_dict(defined_object.get_Name())
        if element.get_Value() is not None: element_dict['value'] = baseobjectattribute.parse_into_dict(defined_object.get_Value())
        return element_dict