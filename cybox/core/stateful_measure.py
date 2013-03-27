import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
#from cybox.common.structured_text import StructuredText
from cybox.common import DefinedObject
from cybox.core.object import Object


class StatefulMeasure(cybox.Entity):
    """CybOX StatefulMeasure

    Only implements a contained Object for now.
    """
    def __init__(self, object_=None):
        # If not a CybOX Object, try to coerce to one
        if object_:
            if isinstance(object_, DefinedObject):
                object_ = object_.parent
            elif not isinstance(object_, Object):
                raise ValueError("Unexpected type: %s" % type(object_))
        self.object_ = object_

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
        sm.object_ = Object.from_dict(statefulmeasure_dict.get('object'))
        return sm

#    @classmethod
#    def dict_from_object(cls, stateful_measure_obj):
#        """Parse and return a dictionary for a stateful measure"""
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
