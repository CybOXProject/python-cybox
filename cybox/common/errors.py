# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding


class ErrorInstances(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ErrorInstancesType
    _namespace = 'http://cybox.mitre.org/common-2'

    error_instance = fields.TypedField("Error_Instance", multiple=True)


class Error(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ErrorType
    _namespace = 'http://cybox.mitre.org/common-2'

    error_type = fields.TypedField("Error_Type")
    error_count = fields.TypedField("Error_Count")
    error_instances = fields.TypedField("Error_Instances", ErrorInstances)


class Errors(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ErrorsType
    _namespace = 'http://cybox.mitre.org/common-2'

    error = fields.TypedField("Error", Error, multiple=True)
