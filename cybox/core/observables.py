import cybox.bindings.cybox_core_1_0 as core_binding
import cybox.core.observable as observable

def create_from_dict(observables_dict):
    """Create the Observables Python object representation from an input dictionary"""
    pass

def parse_into_dict(observables):
    """Parse the observables into a dictionary-esque representation"""
    observables_list = []
    for observable in observables.get_Observable():
        observables_list.append(observable.parse_into_dict(observable))
    return observables_list