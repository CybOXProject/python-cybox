# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.cybox_common as common_types_binding
from cybox.common import VocabString, Personnel, ToolInformationList, StructuredText, Time, ObjectProperties


class MeasureSource(cybox.Entity):
    def __init__(self):
        self.class_ = None
        self.source_type = None
        self.name = None
        self.information_source_type = None
        self.tool_type = None
        self.description = None
        self.contributors = None
        self.time = None
        self.tools = None
        self.platform = None
        self.system = None
        self.instance = None

    def to_obj(self):
        measure_source_obj = common_types_binding.MeasureSourceType()
        if self.class_ is not None : measure_source_obj.set_class(self.class_)
        if self.source_type is not None : measure_source_obj.set_source_type(self.source_type)
        if self.name is not None : measure_source_obj.set_name(self.name)
        if self.information_source_type is not None : measure_source_obj.set_Information_Source_Type(self.information_source_type.to_obj())
        if self.tool_type is not None : measure_source_obj.set_Tool_Type(self.tool_type.to_obj())
        if self.description is not None : measure_source_obj.set_Description(self.description.to_obj())
        if self.contributors is not None : measure_source_obj.set_Contributors(self.contributors.to_obj())
        if self.time is not None : measure_source_obj.set_Time(self.time.to_obj())
        if self.tools is not None : measure_source_obj.set_Tools(self.tools.to_obj())
        if self.platform is not None : measure_source_obj.set_Platform(self.platform.to_obj())
        if self.system is not None : measure_source_obj.set_System(self.system.to_obj())
        if self.instance is not None : measure_source_obj.set_Instance(self.instance.to_obj())
        return measure_source_obj

    def to_dict(self):
        measure_source_dict = {}
        if self.class_ is not None : measure_source_dict['class'] = self.class_
        if self.source_type is not None : measure_source_dict['source_type'] = self.source_type
        if self.name is not None : measure_source_dict['name'] = self.name
        if self.information_source_type is not None : measure_source_dict['information_source_type'] = self.information_source_type.to_dict()
        if self.tool_type is not None : measure_source_dict['tool_type'] = self.tool_type.to_dict()
        if self.description is not None : measure_source_dict['description'] = self.description.to_dict()
        if self.contributors is not None : measure_source_dict['contributors'] = self.contributors.to_dict()
        if self.time is not None : measure_source_dict['time'] = self.time.to_dict()
        if self.tools is not None : measure_source_dict['tools'] = self.tools.to_list()
        if self.platform is not None :measure_source_dict['platform'] = self.platform.to_dict()
        if self.system is not None : measure_source_dict['system'] = self.system.to_dict()
        if self.instance is not None : measure_source_dict['instance'] = self.instance.to_dict()
        return measure_source_dict

    @staticmethod
    def from_dict(measure_source_dict):
        if not measure_source_dict:
            return None
        measure_source_ = MeasureSource()
        measure_source_.class_ = measure_source_dict.get('class')
        measure_source_.source_type = measure_source_dict.get('source_type')
        measure_source_.name = measure_source_dict.get('name')
        measure_source_.information_source_type = VocabString.from_dict(measure_source_dict.get('information_source_type'))
        measure_source_.tool_type = VocabString.from_dict(measure_source_dict.get('tool_type'))
        measure_source_.description = StructuredText.from_dict(measure_source_dict.get('description'))
        measure_source_.contributors = Personnel.from_list(measure_source_dict.get('contributors'))
        measure_source_.time = Time.from_dict(measure_source_dict.get('time'))
        measure_source_.tools = ToolInformationList.from_list(measure_source_dict.get('tools'))
        measure_source_.platform = None #TODO: add support
        measure_source_.system = ObjectProperties.from_dict(measure_source_dict.get('system'))
        measure_source_.instance = ObjectProperties.from_dict(measure_source_dict.get('instance'))
        return measure_source_

    @staticmethod
    def from_obj(measure_source_obj):
        if not measure_source_obj:
            return None
        measure_source_ = MeasureSource()
        measure_source_.class_ = measure_source_obj.get_class()
        measure_source_.source_type = measure_source_obj.get_source_type()
        measure_source_.name = measure_source_obj.get_name()
        measure_source_.information_source_type = VocabString.from_obj(measure_source_obj.get_Information_Source_Type())
        measure_source_.tool_type = VocabString.from_obj(measure_source_obj.get_Tool_Type())
        measure_source_.description = StructuredText.from_obj(measure_source_obj.get_Description())
        measure_source_.contributors = Personnel.from_obj(measure_source_obj.get_Contributors())
        measure_source_.time = Time.from_obj(measure_source_obj.get_Time())
        measure_source_.tools = ToolInformationList.from_obj(measure_source_obj.get_Tools())
        measure_source_.platform = None #TODO: add support
        measure_source_.system = ObjectProperties.from_obj(measure_source_obj.get_System())
        measure_source_.instance = ObjectProperties.from_obj(measure_source_obj.get_Instance())
        return measure_source_
