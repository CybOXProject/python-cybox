import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
#from cybox.core.structured_text import structured_text
from cybox.core.stateful_measure import StatefulMeasure

class Observable(cybox.Entity):
    """A single Observable.

    Note that StatefulMeasure is the only supported property now.
    """

    def __init__(self):
        self.stateful_measure = None
        self.id_ = cybox.utils.create_id()

    def to_obj(self):
        sm = self.stateful_measure.to_obj()
        return core_binding.ObservableType(id=self.id_, Stateful_Measure=sm)

    def to_dict(self):
        return {
                'id': self.id_,
                'stateful_measure': self.stateful_measure.to_dict(),
               }

    @staticmethod
    def from_obj(observable_obj):
        obs = Observable()
        obs.id_ = observable_obj.get_id()
        sm_obj = observable_obj.get_Stateful_Measure()
        obs.stateful_measure = StatefulMeasure.from_obj(sm_obj)
        return obs

    @staticmethod
    def from_dict(observable_dict):
        obs = Observable()
        obs.id_ = observable_dict.get('id')
        sm_dict = observable_dict.get_obj.get_Stateful_Measure()
        obs.stateful_measure = StatefulMeasure.from_obj(sm_obj)
        return obs

    @classmethod
    def object_from_dict(cls, observable_dict):
        """Create the Observable Python object representation from an input dictionary"""
        return cls.from_dict(observable_dict).to_obj()

    @classmethod
    def dict_from_object(cls, observable):
        """Parse the observable into a dictionary-esque representation"""
        return cls.from_obj(observable).to_dict()
#        observable_dict = {}
#        if observable.get_id() is not None:
#            observable_dict['id'] = observable.get_id()
#        if observable.get_idref() is not None:
#            observable_dict['idref'] = observable.get_idref()
#        if observable.get_Title() is not None:
#            observable_dict['title'] = observable.get_Title()
#        if observable.get_Description() is not None:
#            observable_dict['description'] = structured_text.dict_from_object(observable.get_Description())
#        if observable.get_Stateful_Measure() is not None:
#            observable_dict['stateful_measure'] = stateful_measure.dict_from_object(observable.get_Stateful_Measure())
#        #TODO - add rest of observable components
#        return observable_dict
