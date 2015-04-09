# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import (vocabs, ObjectProperties, Personnel,
        PlatformSpecification, StructuredText, Time, ToolInformationList,
        ToolType)
from cybox.common.vocabs import InformationSourceType


class MeasureSource(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.MeasureSourceType
    _namespace = 'http://cybox.mitre.org/common-2'

    class_ = cybox.TypedField("classxx", key_name="class")
    source_type = cybox.TypedField("source_type")
    name = cybox.TypedField("name")
    sighting_count = cybox.TypedField("sighting_count")
    information_source_type = vocabs.VocabField("Information_Source_Type",
                                                InformationSourceType)
    tool_type = vocabs.VocabField("Tool_Type", ToolType)
    description = cybox.TypedField("Description", StructuredText)
    contributors = cybox.TypedField("Contributors", Personnel)
    time = cybox.TypedField("Time", Time)
    tools = cybox.TypedField("Tools", ToolInformationList)
    platform = cybox.TypedField("Platform", PlatformSpecification)
    system = cybox.TypedField("System", ObjectProperties)
    instance = cybox.TypedField("Instance", ObjectProperties)
