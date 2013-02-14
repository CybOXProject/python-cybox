import cybox.utils as utils
import cybox.bindings.cybox_core_1_0 as core_binding
import cybox.core.structured_text as Structured_Text
from cybox.core.defined_object import Defined_Object
from cybox.common.measuresource import Measure_Source

class Object(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, object_dict, cybox_obj = None):
        """Create the Object Python object representation from an input dictionary"""
        if cybox_obj == None:
            cybox_obj = core_binding.ObjectType()
        for key, value in object_dict.items():
            if key == 'id' and utils.test_value(value): cybox_obj.set_id(value)
            elif key == 'idref' and utils.test_value(value): cybox_obj.set_idref(value)
            elif key == 'type' and utils.test_value(value): cybox_obj.set_type(value)
            elif key == 'object_state' and utils.test_value(value): cybox_obj.set_object_state(value)
            elif key == 'description' : pass
            elif key == 'defined_object' : cybox_obj.set_Defined_Object(value)
                #defined_obj = Defined_Object.object_from_dict(value)
                #if defined_obj.hasContent_() : cybox_obj.set_Defined_Object(defined_obj)
            elif key == 'domain-specific_object_attributes': pass
            elif key == 'custom_attributes' : pass
            elif key == 'related_objects':
                pass
            elif key == 'defined_effect' :
                pass
            elif key == 'discovery_method':
                measure_source_obj = Measure_Source.object_from_dict(value)
                if measure_source_obj.hasContent_() : cybox_obj.set_Discovery_Method(measure_source_obj)
        return cybox_obj

    @classmethod
    def dict_from_object(cls, object):
        """Parse and return a dictionary for an Object"""
        object_dict = {}
        if object.get_id() is not None:
            object_dict['id'] = object.get_id()
        if object.get_idref() is not None:
            object_dict['idref'] = object.get_idref()
        if object.get_type() is not None:
            object_dict['type'] = object.get_type()
        if object.get_object_state() is not None:
            object_dict['object_state'] = object.get_object_state()
        if object.get_Description() is not None:
            object_dict['description'] = Structured_Text.dict_from_object(object.get_Description())
        if object.get_Defined_Object() is not None:
            object_dict['defined_object'] = defined_object.dict_from_object(object.get_Defined_Object())
        #TODO - add rest of object components
        return object_dict