import cybox
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common import HashList

class ToolInformation(cybox.Entity):
    def __init__(self):
        self.id = None
        self.idref = None
        self.description = None
        self.vendor = None
        self.name = None
        self.version = None
        self.service_pack = None
        self.tool_specific_data = None
        self.tool_hashes = None
        self.tool_configuration = None
        self.execution_environment = None
        self.errors = None
        self.metadata = []

    def to_obj(self):
        tool_information_obj = common_types_binding.ToolInformationType()
        if self.id is not None : tool_information_obj.set_id(self.id)
        if self.idref is not None : tool_information_obj.set_idref(self.idref)
        if self.description is not None : pass
        if self.name is not None : tool_information_obj.set_Name(self.name)
        if self.version is not None : tool_information_obj.set_Version(self.version)
        if self.service_pack is not None : tool_information_obj.set_Service_Pack(self.service_pack)
        if self.tool_specific_data is not None : pass
        if self.tool_hashes is not None : tool_information_obj.set_Tool_Hashes(self.tool_hashes.to_obj())
        if self.tool_configuration is not None : pass
        if self.execution_environment is not None : pass
        if self.errors is not None : pass
        if len(self.metadata) > 0 : pass
        return tool_information_obj

    def to_dict(self):
        pass

    @staticmethod
    def from_dict(tool_information_dict):
        if not tool_information_dict:
            return None
        tool_information_ = ToolInformation()
        tool_information_.id = tool_information_dict.get('id')
        tool_information_.idref = tool_information_dict.get('idref')
        #tool_information_.description = tool_information_dict.get('description')
        tool_information_.vendor = tool_information_dict.get('vendor')
        tool_information_.name = tool_information_dict.get('name')
        tool_information_.name = tool_information_dict.get('version')
        tool_information_.service_pack = tool_information_dict.get('service_pack')
        #tool_information_.tool_specific_data = tool_information_dict.get('tool-specific_data')
        tool_information_.tool_hashes = HashList.from_list(tool_information_dict.get('tool_hashes'))
        #tool_information_.tool_configuration = tool_information_dict.get('tool_configuration')
        #tool_information_.execution_environment = tool_information_dict.get('execution_environment')
        #tool_information_.errors = tool_information_dict.get('errors')
        #tool_information_.metadata = tool_information_dict.get('metadata')
        return tool_information_

    @staticmethod
    def from_obj(tool_information_obj):
        pass

class ToolInformationList(object):
    def __init__(self):
        self.tool_list = []

    def to_obj(self):
        tools_information_obj = common_types_binding.ToolsInformationType()
        for tool in self.tool_list:
            tools_information_obj.add_Tool(tool.to_obj())
        return tools_information_obj

    def to_dict(self):
        pass

    @staticmethod
    def from_list(tools_list):
        if not tools_list:
            return None
        tools_list_ = ToolInformationList()
        tools_list_.tool_list = [ToolInformation.from_dict(x) for x in tools_list]
        return tools_list_

    @staticmethod
    def from_obj(tools_obj):
        pass
