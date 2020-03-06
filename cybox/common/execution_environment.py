# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.object_properties import ObjectPropertiesFactory, ObjectProperties
from cybox.common.time import DateTimeWithPrecision


class ExecutionEnvironment(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ExecutionEnvironmentType
    _namespace = 'http://cybox.mitre.org/common-2'

    system = fields.TypedField("System", ObjectProperties, factory=ObjectPropertiesFactory)
    user_account_info = fields.TypedField("User_Account_Info", ObjectProperties, factory=ObjectPropertiesFactory)
    command_line = fields.TypedField("Command_Line")
    start_time = fields.TypedField("Start_Time", DateTimeWithPrecision)
