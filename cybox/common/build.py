# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.compilers import Compilers
from cybox.common.configuration_settings import ConfigurationSettings
from cybox.common.libraries import Libraries
from cybox.common.platform_specification import PlatformSpecification
from cybox.common.time import DateTimeWithPrecision


class BuildUtility(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.BuildUtilityType
    _namespace = 'http://cybox.mitre.org/common-2'

    build_utility_name = fields.TypedField("Build_Utility_Name")
    build_utility_platform_specification = fields.TypedField("Build_Utility_Platform_Specification", PlatformSpecification)


class BuildConfiguration(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.BuildConfigurationType
    _namespace = 'http://cybox.mitre.org/common-2'

    configuration_setting_description = fields.TypedField("Configuration_Setting_Description", multiple=True)
    configuration_settings = fields.TypedField("Configuration_Settings", ConfigurationSettings)


class BuildInformation(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.BuildInformationType
    _namespace = 'http://cybox.mitre.org/common-2'

    build_id = fields.TypedField("Build_ID")
    build_project = fields.TypedField("Build_Project")
    build_utility = fields.TypedField("Build_Utility", BuildUtility)
    build_version = fields.TypedField("Build_Version")
    build_label = fields.TypedField("Build_Label")
    compilers = fields.TypedField("Compilers", Compilers)
    compilation_date = fields.TypedField("Compilation_Date", DateTimeWithPrecision)
    build_configuration = fields.TypedField("Build_Configuration", BuildConfiguration)
    build_script = fields.TypedField("Build_Script")
    libraries = fields.TypedField("Libraries", Libraries)
    build_output_log = fields.TypedField("Build_Output_Log")
