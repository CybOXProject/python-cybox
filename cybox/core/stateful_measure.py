import cybox.bindings.cybox_core_1_0 as core_binding
import cybox.core.structured_text as structured_text
import cybox.core.object as cybox_object

def create_from_dict(stateful_measure_dict):
    """Create the Stateful Measure Python object representation from an input dictionary"""
    pass

def parse_stateful_measure_into_dict(stateful_measure):
    """Parse and return a dictionary for a stateful measure"""
    stateful_measure_dict = {}
    if stateful_measure.get_name() is not None:
        stateful_measure_dict['name'] = stateful_measure.get_Name()
    if stateful_measure.get_has_changed() is not None:
        stateful_measure_dict['has_changed'] = stateful_measure.get_has_changed()
    if stateful_measure.get_Description() is not None:
        stateful_measure_dict['description'] = structured_text.parse_into_dict(stateful_measure.get_Description())
    if stateful_measure.get_Object() is not None:
        stateful_measure_dict['object'] = cybox_object.parse_into_dict(stateful_measure.get_Object())
    return stateful_measure_dict