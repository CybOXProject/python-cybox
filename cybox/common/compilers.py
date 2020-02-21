# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.platform_specification import PlatformSpecification


class CompilerInformalDescription(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.CompilerInformalDescriptionType
    _namespace = 'http://cybox.mitre.org/common-2'

    compiler_name = fields.TypedField("Compiler_Name")
    compiler_version = fields.TypedField("Compiler_Version")


class Compiler(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.CompilerType
    _namespace = 'http://cybox.mitre.org/common-2'

    compiler_informal_description = fields.TypedField("Compiler_Informal_Description", CompilerInformalDescription)
    compiler_platform_specification = fields.TypedField("Compiler_Platform_Specification", PlatformSpecification)


class Compilers(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.CompilersType
    _namespace = 'http://cybox.mitre.org/common-2'

    compiler = fields.TypedField("Compiler", Compiler, multiple=True)
