# Copyright (c) 2010, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import (
    CompensationModel, Errors, ExecutionEnvironment, HashList, Metadata,
    StructuredText
)
from cybox.common.vocabs import VocabField, ToolType


class ToolSpecificDataFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        return cybox.lookup_extension(key, default=ToolSpecificData)


class ToolSpecificData(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolSpecificDataType
    _namespace = 'http://cybox.mitre.org/common-2'
    _XSI_TYPE = None    # overridden by subclasses

    def to_dict(self):
        d = super(ToolSpecificData, self).to_dict()

        if self._XSI_TYPE:
            d["xsi:type"] = self._XSI_TYPE

        return d

    @staticmethod
    def lookup_class(xsi_type):
        return cybox.lookup_extension(xsi_type, default=ToolSpecificData)


class ToolReference(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolReferenceType
    _namespace = 'http://cybox.mitre.org/common-2'

    TERM_DOCUMENTATION = "Documentation"
    TERM_SOURCE = "Source"
    TERM_DOWNLOAD = "Download"
    TERM_EXECUTE = "Execute"
    TERM_OTHER = "Other"

    reference_type = fields.TypedField("reference_type")
    value = fields.TypedField("valueOf_", key_name="value")


class ToolReferences(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolReferencesType
    _namespace = 'http://cybox.mitre.org/common-2'

    reference = fields.TypedField("Reference", ToolReference, multiple=True)


class ToolConfiguration(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolConfigurationType
    _namespace = 'http://cybox.mitre.org/common-2'

    configuration_settings = fields.TypedField("Configuration_Settings")
    dependencies = fields.TypedField("Dependencies")
    usage_context_assumptions = fields.TypedField("Usage_Context_Assumptions")
    internationalization_settings = fields.TypedField("Internationalization_Settings")
    build_information = fields.TypedField("Build_Information")


class ToolInformation(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType
    _namespace = 'http://cybox.mitre.org/common-2'

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    name = fields.TypedField("Name")
    type_ = VocabField("Type", ToolType, multiple=True)
    description = fields.TypedField("Description", StructuredText)
    references = fields.TypedField("References", ToolReferences)
    vendor = fields.TypedField("Vendor")
    version = fields.TypedField("Version")
    service_pack = fields.TypedField("Service_Pack")
    tool_specific_data = fields.TypedField("Tool_Specific_Data", ToolSpecificData, factory=ToolSpecificDataFactory)
    tool_hashes = fields.TypedField("Tool_Hashes", HashList)
    tool_configuration = fields.TypedField("Tool_Configuration", ToolConfiguration)
    execution_environment = fields.TypedField("Execution_Environment", ExecutionEnvironment)
    errors = fields.TypedField("Errors", Errors)
    metadata = fields.TypedField("Metadata", Metadata, multiple=True)
    compensation_model = fields.TypedField("Compensation_Model", CompensationModel)

    def __init__(self, tool_name=None, tool_vendor=None):
        super(ToolInformation, self).__init__()
        self.name = tool_name
        self.vendor = tool_vendor


class ToolInformationList(entities.EntityList):
    _binding_class = common_binding.ToolsInformationType
    _namespace = 'http://cybox.mitre.org/common-2'

    tool = fields.TypedField("Tool", ToolInformation, multiple=True)
