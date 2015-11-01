# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import HashList, StructuredText
from cybox.common.vocabs import VocabField, ToolType


class ToolInformation(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType
    _namespace = 'http://cybox.mitre.org/common-2'

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    name = fields.TypedField("Name")
    type_ = VocabField("Type", ToolType, multiple=True)
    description = fields.TypedField("Description", StructuredText)
    vendor = fields.TypedField("Vendor")
    version = fields.TypedField("Version")
    service_pack = fields.TypedField("Service_Pack")
    tool_hashes = fields.TypedField("Tool_Hashes", HashList)

    def __init__(self, tool_name=None, tool_vendor=None):
        super(ToolInformation, self).__init__()
        # TODO: Implement items commented out below.
        self.name = tool_name
        self.description = None
        #self.references = None
        self.vendor = tool_vendor
        self.version = None
        self.service_pack = None
        #self.tool_specific_data = None
        self.tool_hashes = None
        #self.tool_configuration = None
        #self.execution_environment = None
        #self.errors = None
        #self.metadata = []


class ToolInformationList(entities.EntityList):
    _binding_class = common_binding.ToolsInformationType
    _namespace = 'http://cybox.mitre.org/common-2'
    tool = fields.TypedField("Tool", ToolInformation, multiple=True)