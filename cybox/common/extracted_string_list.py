import cybox.bindings.cybox_common_types_1_0 as common_binding
from cybox.common.extracted_string import extracted_string

class extracted_string_list(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, extracted_string_list_attributes):
        """Create the Extracted String List object representation from an input dictionary"""
        ex_string_list = common_binding.ExtractedStringsType()
        for ex_string in extracted_string_list_attributes:
            extracted_string_object = extracted_string.create_from_dict(ex_string)
            if extracted_string_object.hasContent_():
                ex_string_list.add_String(extracted_string_object)
        return ex_string_list

    @classmethod
    def parse_into_dict(cls, element):
        """Parse and return a dictionary for a Extracted String List object"""
        ex_string_list = []
        for ex_string in element.get_String():
            extracted_string_dict = extracted_string.parse_into_dict(ex_string)
            ex_string_list.append(extracted_string_dict)
        return ex_string_list
