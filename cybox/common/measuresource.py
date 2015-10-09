# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common.object_properties import ObjectPropertiesFactory, ObjectProperties
from cybox.common import (Personnel, PlatformSpecification, StructuredText,
    Time, ToolInformationList, ToolType)
from cybox.common.vocabs import InformationSourceType, VocabField


class MeasureSource(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.MeasureSourceType
    _namespace = 'http://cybox.mitre.org/common-2'

    class_ = fields.TypedField("classxx", key_name="class")
    source_type = fields.TypedField("source_type")
    name = fields.TypedField("name")
    sighting_count = fields.TypedField("sighting_count")
    information_source_type = VocabField("Information_Source_Type", InformationSourceType)
    tool_type = VocabField("Tool_Type", ToolType)
    description = fields.TypedField("Description", StructuredText)
    contributors = fields.TypedField("Contributors", Personnel)
    time = fields.TypedField("Time", Time)
    tools = fields.TypedField("Tools", ToolInformationList)
    platform = fields.TypedField("Platform", PlatformSpecification)
    system = fields.TypedField("System", ObjectProperties, factory=ObjectPropertiesFactory)
    instance = fields.TypedField("Instance", ObjectProperties, factory=ObjectPropertiesFactory)
