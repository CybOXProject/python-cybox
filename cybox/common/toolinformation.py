import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common import HashList

class Tool_Information(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, tool_information_dict):
        """Create the ToolInformation object representation from an input dictionary"""
        tool_information_obj = common_types_binding.ToolInformationType()
        for key, value in tool_information_dict.items():
            if key == 'id' and utils.test_value(value) : tool_information_obj.set_id(value)
            elif key == 'idref' and utils.test_value(value) : tool_information_obj.set_idref(value)
            elif key == 'description': pass
            elif key == 'vendor' and utils.test_value(value): tool_information_obj.set_Vendor(value)
            elif key == 'name' and utils.test_value(value): tool_information_obj.set_Name(value)  
            elif key == 'version' and utils.test_value(value): tool_information_obj.set_Version(value)
            elif key == 'service_pack' and utils.test_value(value): tool_information_obj.set_Service_Pack(value)
            elif key == 'tool-specific_data' : pass
            elif key == 'tool_hashes':
                hashes_obj = HashList.object_from_dict(value)
                if hashes_obj.hasContent_() : tool_information_obj.set_Tool_Hashes(hashes_obj)
            elif key == 'tool_configuration' : pass
            elif key == 'execution_environment' : pass
            elif key == 'errors' : pass
            elif key == 'metadata' : pass
        return tool_information_obj

    @classmethod
    def dict_from_object(cls, measuresource_obj):
        """Parse and return a dictionary for a ToolInformation object"""
        tool_information_dict = {}
        return tool_information_dict

class Tool_Information_List(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, tools_information_list):
        """Create the ToolsInformation object representation from an input list of ToolInformation dictionaries"""
        tools_information_obj = common_types_binding.ToolsInformationType()
        for tool_information_dict in tools_information_list:
            tool_information_obj = Tool_Information.object_from_dict(tool_information_dict)
            if tool_information_obj.hasContent_() : tools_information_obj.add_Tool(tool_information_obj)
        return tools_information_obj

    @classmethod
    def list_from_object(cls, measuresource_obj):
        """Parse and return a list of ToolInformation dictionaries for a ToolsInformation object"""
        tools_information_list = []
        return tools_information_list
