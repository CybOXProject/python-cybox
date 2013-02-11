import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.extracted_string import Extracted_String

class Extracted_String_List(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_list(cls, extracted_string_list):
        """Create the Extracted String List object representation from an input list of Extracted String dictionaries."""
        ex_string_list = common_binding.ExtractedStringsType()
        for ex_string in extracted_string_list:
            Extracted_String_object = Extracted_String.object_from_dict(ex_string)
            if Extracted_String_object.hasContent_():
                ex_string_list.add_String(Extracted_String_object)
        return ex_string_list

    @classmethod
    def list_from_object(cls, extracted_string_list_obj):
        """Parse and return a list of Extracted String dictionaries for an Extracted String List object"""
        ex_string_list = []
        for ex_string in extracted_string_list_obj.get_String():
            Extracted_String_dict = Extracted_String.dict_from_object(ex_string)
            ex_string_list.append(Extracted_String_dict)
        return ex_string_list
