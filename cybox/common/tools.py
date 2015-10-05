# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities

import cybox.bindings.cybox_common as common_binding
from cybox.common import HashList, StructuredText, VocabString
from cybox.common.vocabs import ToolType  # noqa


class ToolInformation(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, tool_name = None, tool_vendor = None):
        super(ToolInformation, self).__init__()
        # TODO: Implement items commented out below.
        self.id_ = None
        self.idref = None
        self.name = tool_name
        self.type_ = []
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

    @property
    def tool_hashes(self):
        if self._tool_hashes is None:
            self._tool_hashes = HashList()
        return self._tool_hashes

    @tool_hashes.setter
    def tool_hashes(self, value):
        self._tool_hashes = value

    def to_obj(self, ns_info=None):
        toolinfo_obj = super(ToolInformation, self).to_obj(ns_info=ns_info)

        if self.id_ is not None:
            toolinfo_obj.id = self.id_
        if self.idref is not None:
            toolinfo_obj.idref = self.idref
        if self.name is not None:
            toolinfo_obj.Name = self.name
        if self.type_:
            toolinfo_obj.Type = [x.to_obj(ns_info=ns_info) for x in self.type_]
        if self.description is not None:
            toolinfo_obj.Description = self.description.to_obj(ns_info=ns_info)

        if self.vendor is not None:
            toolinfo_obj.Vendor = self.vendor
        if self.version is not None:
            toolinfo_obj.Version = self.version
        if self.service_pack is not None:
            toolinfo_obj.Service_Pack = self.service_pack

        if self.tool_hashes:
            toolinfo_obj.Tool_Hashes = self.tool_hashes.to_obj(ns_info=ns_info)

        return toolinfo_obj

    def to_dict(self):
        toolinfo_dict = super(ToolInformation, self).to_dict()

        if self.id_ is not None:
            toolinfo_dict['id'] = self.id_
        if self.idref is not None:
            toolinfo_dict['idref'] = self.idref
        if self.name is not None:
            toolinfo_dict['name'] = self.name
        if self.type_:
            toolinfo_dict['type'] = [x.to_dict() for x in self.type_]
        if self.description is not None:
            toolinfo_dict['description'] = self.description.to_dict()

        if self.vendor is not None:
            toolinfo_dict['vendor'] = self.vendor
        if self.version is not None:
            toolinfo_dict['version'] = self.version
        if self.service_pack is not None:
            toolinfo_dict['service_pack'] = self.service_pack

        if self.tool_hashes:
            toolinfo_dict['tool_hashes'] = self.tool_hashes.to_list()

        return toolinfo_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        toolinfo = super(ToolInformation, cls).from_obj(cls_obj)

        toolinfo.id_ = cls_obj.id
        toolinfo.idref = cls_obj.idref
        toolinfo.name = cls_obj.Name
        toolinfo.type_ = [VocabString.from_obj(x) for x in cls_obj.Type]
        toolinfo.description = StructuredText.from_obj(cls_obj.Description)

        toolinfo.vendor = cls_obj.Vendor
        toolinfo.version = cls_obj.Version
        toolinfo.service_pack = cls_obj.Service_Pack

        toolinfo.tool_hashes = HashList.from_obj(cls_obj.Tool_Hashes)

        return toolinfo

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        toolinfo = super(ToolInformation, cls).from_dict(cls_dict)
        toolinfo.id_ = cls_dict.get('id')
        toolinfo.idref = cls_dict.get('idref')
        toolinfo.name = cls_dict.get('name')
        toolinfo.type_ = [VocabString.from_dict(x) for x in cls_dict.get('type', [])]
        toolinfo.description = StructuredText.from_dict(cls_dict.get('description'))
        toolinfo.vendor = cls_dict.get('vendor')
        toolinfo.version = cls_dict.get('version')
        toolinfo.service_pack = cls_dict.get('service_pack')

        toolinfo.tool_hashes = HashList.from_list(cls_dict.get('tool_hashes'))

        return toolinfo


class ToolInformationList(entities.EntityList):
    _binding_class = common_binding.ToolsInformationType
    _binding_var = "Tool"
    _contained_type = ToolInformation
    _namespace = 'http://cybox.mitre.org/common-2'
