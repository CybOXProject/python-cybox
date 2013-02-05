import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.personnel import Personnel
from cybox.common.toolinformation import Tool_Information_List

class Measure_Source(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, measure_source_dict):
        """Create the MeasureSource object representation from an input dictionary"""
        measure_source_obj = common_types_binding.MeasureSourceType()
        for key, value in measure_source_dict.items():
            if key == 'class' and utils.test_value(value): measure_source_obj.set_class(value)
            elif key == 'source_type' and utils.test_value(value): measure_source_obj.set_source_type(value)
            elif key == 'tool_type' and utils.test_value(value): measure_source_obj.set_tool_type(value)
            elif key == 'information_source_type' and utils.test_value(value): measure_source_obj.set_information_source_type(value)
            elif key == 'name' and utils.test_value(value): measure_source_obj.set_name(value)
            elif key == 'description' : pass
            elif key == 'contributors' : 
                personnel_obj = Personnel.object_from_dict(value)
                if personnel_obj.hasContent_() : measure_source_obj.set_Contributors()
            elif key == 'time' : pass
            elif key == 'tools' : 
                tools_information_obj = Tool_Information_List.object_from_list(value)
                if tools_information_obj.hasContent_() : measure_source_obj.set_Tools(tools_information_obj)
            elif key == 'platform' : pass
            elif key == 'system' : pass
            elif key == 'instance' : pass
        return measure_source_obj

    @classmethod
    def dict_from_object(cls, measure_source_obj):
        """Parse and return a dictionary for a MeasureSource object"""
        measure_source_dict = {}

        return measure_source_dict
