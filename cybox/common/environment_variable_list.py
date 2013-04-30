import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.environment_variable import EnvironmentVariable

class EnvironmentVariableList(cybox.EntityList):
    _contained_type = EnvironmentVariable

    def __init__(self):
        super(EnvironmentVariableList, self).__init__()

    def to_obj(self):
        env_variable_list_obj = common_binding.EnvironmentVariableListType()
        for environment_variable_ in self:
            env_variable_list_obj.add_Environment_Variable(environment_variable_.to_obj())
        return env_variable_list_obj

    def to_list(self):
        return [env_variable.to_dict() for env_variable in self]

    @staticmethod
    def from_list(environment_variable_list):
        if not environment_variable_list:
            return None

        env_variable_list_ = EnvironmentVariableList()
        for environment_variable_dict in environment_variable_list:
            env_variable_list_.append(EnvironmentVariable.from_dict(environment_variable_dict))
        return env_variable_list_

    @staticmethod
    def from_obj(environment_variable_list_obj):
        if not environment_variable_list_obj:
            return None

        env_variable_list_ = EnvironmentVariableList()
        for environment_variable_obj in environment_variable_list_obj.get_Environment_Variable():
            env_variable_list_.append(EnvironmentVariable.from_obj(environment_variable_obj))
        return env_variable_list_
