import cybox.utils as utils
import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.object import Object

class Associated_Object(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, associated_object_dict):
        """Create the Associated Object Python object representation from an input dictionary"""
        associated_obj = Object.object_from_dict(associated_object_dict,core_binding.AssociatedObjectType())
        for key, value in associated_object_dict.items():
            if key == 'association_type' and utils.test_value(value): associated_obj.set_association_type(value)
        return associated_obj

    @classmethod
    def dict_from_object(cls, associated_obj):
        """Parse and return a dictionary for an Associated Object"""
        associated_object_dict = Object.dict_from_object(associated_obj)
        if associated_obj.get_association_type() is not None: associated_object_dict['association_type'] = associated_obj.get_association_type()
        return associated_object_dict