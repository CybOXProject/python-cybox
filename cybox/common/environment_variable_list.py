# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.environment_variable import EnvironmentVariable


class EnvironmentVariableList(cybox.EntityList):
    _binding_class = common_binding.EnvironmentVariableListType
    _binding_var = "Environment_Variable"
    _contained_type = EnvironmentVariable
    _namespace = 'http://cybox.mitre.org/common-2'
