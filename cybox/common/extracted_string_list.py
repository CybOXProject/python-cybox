import cybox
import cybox.bindings.cybox_common as common_types_binding
from cybox.common.extracted_string import ExtractedString

class ExtractedStringList(cybox.EntityList):
    _contained_type = ExtractedString

    def __init__(self):
        super(ExtractedStringList, self).__init__()

    def _fix_value(self, value):
        # If the user tries to put a string into a list, convert it to an ExtractedString.
        if isinstance(value, basestring):
            return ExtractedString(value)

    def to_obj(self):
        ex_string_list_obj = common_types_binding.ExtractedStringsType()
        for extracted_string_ in self:
            ex_string_list_obj.add_String(extracted_string_.to_obj())
        return ex_string_list_obj

    def to_list(self):
        return [ex_string.to_dict() for ex_string in self]

    @staticmethod
    def from_list(extracted_string_list):
        if not extracted_string_list:
            return None

        extracted_string_list_ = ExtractedStringList()
        for extracted_string_dict in extracted_string_list:
            extracted_string_list.append(ExtractedString.from_dict(extracted_string_dict))
        return extracted_string_list_

    @staticmethod
    def from_obj(extracted_string_list_obj):
        if not extracted_string_list_obj:
            return None

        extracted_string_list_ = ExtractedStringList()
        for extracted_string_obj in extracted_string_list_obj.get_String():
            extracted_string_list_.append(ExtractedString.from_obj(extracted_string_obj))
        return extracted_string_list_
