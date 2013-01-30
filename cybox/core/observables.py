import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.observable import observable

class observables(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, observables_dict):
        """Create the Observables Python object representation from an input dictionary"""
        pass

    @classmethod
    def dict_from_object(cls, observables):
        """Parse the observables into a dictionary-esque representation"""
        observables_list = []
        for observable in observables.get_Observable():
            observables_list.append(observable.dict_from_object(observable))
        return observables_list