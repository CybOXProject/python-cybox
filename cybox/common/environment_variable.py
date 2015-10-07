# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities

import cybox.bindings.cybox_common as common_binding
from cybox.common import String


class EnvironmentVariable(entities.Entity):
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self):
        super(EnvironmentVariable, self).__init__()
        self.name = None
        self.value = None

    def to_obj(self, ns_info=None):
        environment_variable_obj = super(EnvironmentVariable, self).to_obj(ns_info=ns_info)

        if self.name is not None:
            environment_variable_obj.Name = self.name.to_obj(ns_info=ns_info)

        if self.value is not None:
            environment_variable_obj.Value = self.value.to_obj(ns_info=ns_info)

        return environment_variable_obj

    def to_dict(self):
        environment_variable_dict = {}

        if self.name is not None: environment_variable_dict['name'] = self.name.to_dict()
        if self.value is not None: environment_variable_dict['value'] = self.value.to_dict()

        return environment_variable_dict

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        environment_variable_ = super(EnvironmentVariable, cls).from_dict(cls_dict)
        environment_variable_.name = String.from_dict(cls_dict.get('name'))
        environment_variable_.value = String.from_dict(cls_dict.get('value'))

        return environment_variable_

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        environment_variable_ = super(EnvironmentVariable, cls).from_obj(cls_obj)
        environment_variable_.name = String.from_obj(cls_obj.Name)
        environment_variable_.value = String.from_obj(cls_obj.Value)

        return environment_variable_


class EnvironmentVariableList(entities.EntityList):
    _binding_class = common_binding.EnvironmentVariableListType
    _binding_var = "Environment_Variable"
    _contained_type = EnvironmentVariable
    _namespace = 'http://cybox.mitre.org/common-2'
