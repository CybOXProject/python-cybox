import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.structured_text import Structured_Text
from cybox.core.object import Object  

class stateful_measure(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, stateful_measure_dict):
        """Create the Stateful Measure Python object representation from an input dictionary"""
        pass

    @classmethod
    def dict_from_object(cls, stateful_measure_obj):
        """Parse and return a dictionary for a stateful measure"""
        stateful_measure_dict = {}
        if stateful_measure.get_name() is not None:
            stateful_measure_dict['name'] = stateful_measure_obj.get_Name()
        if stateful_measure.get_has_changed() is not None:
            stateful_measure_dict['has_changed'] = stateful_measure_obj.get_has_changed()
        if stateful_measure.get_Description() is not None:
            stateful_measure_dict['description'] = stateful_measure_obj.dict_from_object(stateful_measure.get_Description())
        if stateful_measure.get_Object() is not None:
            stateful_measure_dict['object'] = Object.dict_from_object(stateful_measure.get_Object())
        return stateful_measure_dict