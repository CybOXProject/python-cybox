# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.cybox_common as common_binding

class Base_Object_Attribute(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, element_object, element_values):
        """Create the BaseObjectAttributeType object representation from an input dictionary"""
        if isinstance(element_values, dict):
            for key, value in element_values.items():
                if key == 'id': element_object.set_id(value)
                elif key == 'idref': element_object.set_idref(value)
                elif key == 'datatype': element_object.set_datatype(value)
                elif key == 'condition': element_object.set_condition(value)
                elif key == 'pattern_type': element_object.set_pattern_type(value)
                elif key == 'regex_syntax': element_object.set_regex_syntax(value)
                elif key == 'start_range': element_object.set_start_range(value)
                elif key == 'end_range': element_object.set_end_range(value)
                elif key == 'value_set': element_object.set_value_set(value)
                elif key == 'has_changed': element_object.set_has_changed(value)
                elif key == 'trend': element_object.set_trend(value)
                elif key == 'appears_random': element_object.set_appears_random(value)
                elif key == 'is_obfuscated': element_object.set_is_obfuscated(value)
                elif key == 'obfuscation_algorithm_ref': element_object.set_obfuscation_algorithm_ref(value)
                elif key == 'is_defanged': element_object.set_is_defanged(value)
                elif key == 'defanging_algorithm_ref': element_object.set_defanging_algorithm_ref(value)
                elif key == 'refanging_transform_type': element_object.set_refanging_transform_type(value)
                elif key == 'refanging_transform': element_object.set_refanging_transform(value)
                elif key == 'value': element_object.set_valueOf_(value)
        else:
            element_object.set_valueOf_(element_values)
        return element_object

    @classmethod
    def dict_from_object(cls, element):
        """Parse and return a dictionary for the BaseObjectAttributeType"""
        element_dict = {}
        if element.get_id() is not None: element_dict['id'] = element.get_id()
        if element.get_idref() is not None: element_dict['idref'] = element.get_idref()
        if element.get_datatype() is not None: element_dict['datatype'] = element.get_datatype()
        if element.get_condition() is not None: element_dict['condition'] = element.get_condition()
        if element.get_pattern_type() is not None: element_dict['pattern_type'] = element.get_pattern_type()
        if element.get_regex_syntax() is not None: element_dict['regex_syntax'] = element.get_regex_syntax()
        if element.get_start_range() is not None: element_dict['start_range'] = element.get_start_range()
        if element.get_end_range() is not None: element_dict['end_range'] = element.get_end_range()
        if element.get_value_set() is not None: element_dict['value_set'] = element.get_value_set()
        if element.get_has_changed() is not None: element_dict['has_changed'] = element.get_has_changed()
        if element.get_trend() is not None: element_dict['trend'] = element.get_trend()
        if element.get_appears_random() is not None: element_dict['appears_random'] = element.get_appears_random()
        if element.get_is_obfuscated() is not None: element_dict['is_obfuscated'] = element.get_is_obfuscated()
        if element.get_obfuscation_algorithm_ref() is not None: element_dict['obfuscation_algorithm_ref'] = element.get_obfuscation_algorithm_ref()
        if element.get_is_defanged() is not None: element_dict['is_defanged'] = element.get_is_defanged()
        if element.get_defanging_algorithm_ref() is not None: element_dict['defanging_algorithm_ref'] = element.get_defanging_algorithm_ref()
        if element.get_refanging_transform_type() is not None: element_dict['refanging_transform_type'] = element.get_refanging_transform_type()
        if element.get_refanging_transform() is not None: element_dict['refanging_transform'] = element.get_refanging_transform()
        if element.get_valueOf_() is not None: element_dict['value'] = element.get_valueOf_()
        return element_dict
