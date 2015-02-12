# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import String


class EnvironmentVariable(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self):
        super(EnvironmentVariable, self).__init__()
        self.name = None
        self.value = None

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        environment_variable_obj = common_binding.EnvironmentVariableType()

        if self.name is not None: environment_variable_obj.Name = self.name.to_obj(ns_info=ns_info)
        if self.value is not None: environment_variable_obj.Value = self.value.to_obj(ns_info=ns_info)

        return environment_variable_obj

    def to_dict(self):
        environment_variable_dict = {}

        if self.name is not None: environment_variable_dict['name'] = self.name.to_dict()
        if self.value is not None: environment_variable_dict['value'] = self.value.to_dict()

        return environment_variable_dict

    @staticmethod
    def from_dict(environment_variable_dict):
        if not environment_variable_dict:
            return None

        environment_variable_ = EnvironmentVariable()
        environment_variable_.name = String.from_dict(environment_variable_dict.get('name'))
        environment_variable_.value = String.from_dict(environment_variable_dict.get('value'))

        return environment_variable_

    @staticmethod
    def from_obj(environment_variable_obj):
        if not environment_variable_obj:
            return None

        environment_variable_ = EnvironmentVariable()
        environment_variable_.name = String.from_obj(environment_variable_obj.Name)
        environment_variable_.value = String.from_obj(environment_variable_obj.Value)

        return environment_variable_


class EnvironmentVariableList(cybox.EntityList):
    _binding_class = common_binding.EnvironmentVariableListType
    _binding_var = "Environment_Variable"
    _contained_type = EnvironmentVariable
    _namespace = 'http://cybox.mitre.org/common-2'
