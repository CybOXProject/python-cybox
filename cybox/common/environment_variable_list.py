import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.environment_variable import Environment_Variable

class Environment_Variable_List(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, environment_variable_list):
        """Create the Environment Variable List object representation from an input list of Environment Variable dictionaries."""
        env_variable_list = common_binding.EnvironmentVariableListType()
        for env_variable in environment_variable_list:
            Environment_Variable_object = Environment_Variable.object_from_dict(env_variable)
            if Environment_Variable_object.hasContent_():
                env_variable_list.add_Environment_Variable(Environment_Variable_object)
        return env_variable_list

    @classmethod
    def list_from_object(cls, environment_variable_list_obj):
        """Parse and return a list of Enviroment Variable dictionaries for a Environment Variable List object."""
        env_variable_list = []
        for env_variable in environment_variable_list_obj.get_Environment_Variable():
            env_variable_dict = Environment_Variable.dict_from_object(env_variable)
            env_variable_list.append(env_variable_dict)
        return env_variable_list
