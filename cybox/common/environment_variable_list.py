import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.environment_variable import environment_variable

class environment_variable_list(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, environment_variable_list_attributes):
        """Create the Environment Variable List object representation from an input dictionary"""
        env_variable_list = common_binding.EnvironmentVariableListType()
        for env_variable in environment_variable_list_attributes:
            environment_variable_object = environment_variable.create_from_dict(env_variable)
            if environment_variable_object.hasContent_():
                env_variable_list.add_Environment_Variable(environment_variable_object)
        return env_variable_list

    @classmethod
    def parse_into_dict(cls, element):
        """Parse and return a dictionary for a Environment Variable List object"""
        env_variable_list = []
        for env_variable in element.get_Environment_Variable():
            env_variable_dict = environment_variable.parse_into_dict(env_variable)
            env_variable_list.append(env_variable_dict)
        return env_variable_list
