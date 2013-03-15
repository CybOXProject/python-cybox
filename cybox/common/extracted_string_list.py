import cybox.bindings.cybox_common_types_1_0 as common_types_binding
from cybox.common.extracted_string import ExtractedString

class ExtractedStringList(object):
    def __init__(self):
        self.strings = []

    def add(self, extracted_string):
        self.strings.apend(extracted_string)

    def to_obj(self):
        ex_string_list_obj = common_types_binding.ExtractedStringsType()
        for string_obj in self.strings:
            ex_string_list_obj.add_String(string_obj.to_Obj())
        return ex_string_list_obj

    def to_list(self):
        ex_string_list = []
        for string_obj in self.strings:
            ex_string_list.append(string_obj.to_dict())
        return ex_string_list

    @staticmethod
    def from_list(extracted_string_list):
        if not extracted_string_list:
            return None

        extracted_string_list_ = ExtractedStringList()
        for extracted_string_dict in extracted_string_list:
            extracted_string_list_.add(ExtractedString.from_dict(extracted_string_dict))
        return extracted_string_list_

    @staticmethod
    def from_obj(extracted_string_list_obj):
        if not extracted_string_list_obj:
            return None

        extracted_string_list_ = ExtractedStringList()
        for extracted_string_obj in extracted_string_list_obj.get_String():
            extracted_string_list_.add(ExtractedString.from_obj(extracted_string_obj))
        return extracted_string_list_
