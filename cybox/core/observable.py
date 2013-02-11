import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.structured_text import Structured_Text
from cybox.core.stateful_measure import Stateful_Measure

class Observable(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, observable_dict):
        """Create the Observable Python object representation from an input dictionary"""
        pass

    @classmethod
    def dict_from_object(cls, observable_obj):
        """Parse the observable into a dictionary-esque representation"""
        observable_dict = {}
        if observable.get_id() is not None:
            observable_dict['id'] = observable_obj.get_id()
        if observable.get_idref() is not None:
            observable_dict['idref'] = observable_obj.get_idref()
        if observable.get_Title() is not None:
            observable_dict['title'] = observable_obj.get_Title()
        if observable.get_Description() is not None:
            observable_dict['description'] = Structured_Text.dict_from_object(observable_obj.get_Description())
        if observable.get_Stateful_Measure() is not None:
            observable_dict['stateful_measure'] = Stateful_Measure.dict_from_object(observable_obj.get_Stateful_Measure())
        #TODO - add rest of observable components
        return observable_dict