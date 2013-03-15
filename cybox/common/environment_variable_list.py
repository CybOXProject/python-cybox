import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.environment_variable import EnvironmentVariable

class EnvironmentVariableList(object):
    def __init__(self):
        self.environment_variables = []

    def add_environment_variable(self, environment_variable):
        self.environment_variables.append(environment_variable)

    def to_obj(self):
        env_variable_list_obj = common_binding.EnvironmentVariableListType()
        for environment_variable_obj in self.environment_variables:
            env_variable_list_obj.add_Environment_Variable(environment_variable_obj.to_obj())
        return env_variable_list_obj


    def to_list(self):
        env_variable_list = []
        for environment_variable_obj in self.environment_variables:
            env_variable_list.append(environment_variable_obj.to_dict())
        return env_variable_list

    @staticmethod
    def from_list(environment_variable_list):
        if not environment_variable_list:
            return None

        env_variable_list_ = EnvironmentVariableList()
        for environment_variable_dict in environment_variable_list:
            env_variable_list_.add_environment_variable(EnvironmentVariable.from_dict(environment_variable_dict))
        return env_variable_list_

    @staticmethod
    def from_obj(environment_variable_list_obj):
        if not environment_variable_list_obj:
            return None

        env_variable_list_ = EnvironmentVariableList()
        for environment_variable_obj in environment_variable_list_obj.get_Environment_Variable():
            env_variable_list_.add_environment_variable(EnvironmentVariable.from_obj(environment_variable_obj))
        return env_variable_list_