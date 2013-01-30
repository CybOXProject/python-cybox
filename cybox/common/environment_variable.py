import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class environment_variable(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, environment_variable_attributes):
        """Create the Environment Variable object representation from an input dictionary"""
        environment_variable_object = common_binding.EnvironmentVariableType()
        for key, value in environment_variable_attributes.items():
            if key == 'name' : 
                environment_variable_object.set_Name(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'value' : 
                environment_variable_object.set_Value(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
        return environment_variable_object

    @classmethod
    def dict_from_object(cls, element):
        """Parse and return a dictionary for an Environment Variable object"""
        element_dict = {}
        if element.get_Name() is not None: element_dict['name'] = baseobjectattribute.dict_from_object(defined_object.get_Name())
        if element.get_Value() is not None: element_dict['value'] = baseobjectattribute.dict_from_object(defined_object.get_Value())
        return element_dict