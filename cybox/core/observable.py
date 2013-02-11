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

class Observables(cybox.Entity):
    """The root CybOX Observables object.

    Observable_Package_Source and Pools are not currently supported.
    """

    def __init__(self):
        # Assume major_verion and minor_version are immutable for now
        self._major_version = 1
        self._minor_version = 0
        self.observables = []

    def add_observable(self, observable):
        self.observables.append(observable)

    def to_obj(self):
        observable_list = [x.to_obj() for x in self.observables]
        return core_binding.ObservablesType(
                                cybox_major_version=self._major_version,
                                cybox_minor_version=self._minor_version,
                                Observable=observable_list)

    def to_dict(self):
        return {
                    'major_version': self._major_version,
                    'minor_version': self._minor_version,
                    'observables': [x.to_dict() for x in self.observables]
               }

    @staticmethod
    def from_obj(observables_obj):
        #TODO: look at major_version and minor_version
        obs = Observables()
        # get_Observable() actually returns a list
        for o in obserservables_obj.get_Observable():
            obs.add_observable(Observable.from_obj(o))

        return obs

    @staticmethod
    def from_dict(observables_dict):
        #TODO: look at major_version and minor_version
        obs = Observables()
        for o in obserservables_dict.get("observable"):
            obs.add_observable(Observable.from_dict(o))

        return obs

    @classmethod
    def object_from_dict(cls, observables_dict):
        """Create the Observables Python object representation from an input dictionary"""
        return cls.from_dict(observables_dict).to_obj()

    @classmethod
    def dict_from_object(cls, observables):
        """Parse the observables into a dictionary-esque representation"""
        return cls.from_obj(observables).to_dict()
