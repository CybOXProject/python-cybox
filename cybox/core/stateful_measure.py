import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.common.structured_text import Structured_Text
from cybox.core.object import Object

class StatefulMeasure(cybox.Entity):
    """CybOX StatefulMeasure

    Only implements a contained Object for now.
    """
    def __init__(self):
        self.object_ = None

    def to_obj(self):
        sm_obj = core_binding.StatefulMeasureType()
        sm_obj.set_Object(self.object_.to_obj())
        return sm_obj

    def to_dict(self):
        return {'object': self.object_.to_dict()}

    @staticmethod
    def from_obj(statefulmeasure_obj):
        sm = StatefulMeasure()
        sm.object_ = Object.from_obj(statefulmeasure_obj.get_Object())
        return sm

    @staticmethod
    def from_dict(statefulmeasure_dict):
        sm = StatefulMeasure()
        sm.object_ = Object.from_dict(statefulmeasure_obj.get('object'))
        return sm

    @classmethod
    def object_from_dict(cls, statefulmeasure_dict):
        """Create the Stateful Measure Python object representation from an input dictionary"""
        return cls.from_dict(statefulmeasure_dict).to_obj()

    @classmethod
    def dict_from_object(cls, stateful_measure_obj):
        """Parse and return a dictionary for a stateful measure"""
        return cls.from_obj(stateful_measure_obj).to_dict()
#        stateful_measure_dict = {}
#        if stateful_measure.get_name() is not None:
#            stateful_measure_dict['name'] = stateful_measure_obj.get_Name()
#        if stateful_measure.get_has_changed() is not None:
#            stateful_measure_dict['has_changed'] = stateful_measure_obj.get_has_changed()
#        if stateful_measure.get_Description() is not None:
#            stateful_measure_dict['description'] = stateful_measure_obj.dict_from_object(stateful_measure.get_Description())
#        if stateful_measure.get_Object() is not None:
#            stateful_measure_dict['object'] = Object.dict_from_object(stateful_measure.get_Object())
#        return stateful_measure_dict
