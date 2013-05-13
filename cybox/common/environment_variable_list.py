# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.environment_variable import EnvironmentVariable

class EnvironmentVariableList(cybox.EntityList):
    _contained_type = EnvironmentVariable
    _binding_class = common_binding.EnvironmentVariableListType

    def __init__(self):
        super(EnvironmentVariableList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Environment_Variable(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Environment_Variable()
