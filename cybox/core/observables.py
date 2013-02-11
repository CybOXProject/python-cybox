import cybox
import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.observable import Observable

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
