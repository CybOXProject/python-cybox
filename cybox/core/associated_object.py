import cybox.utils as utils
import cybox.bindings.cybox_core_1_0 as core_binding
from cybox.core.object import Object

class AssociatedObject(Object):

    """The CybOX Associated Object element.

    Currently only supports the id, association_type and DefinedObject properties
    """
    superclass = Object
    def __init__(self, type_=None, association_type_=None, defined_object=None):
        super(AssociatedObject, self).__init__(type_, defined_object)
        self.association_type_ = association_type_
        
    def to_obj(self):
        obj = super(AssociatedObject, self).to_obj(core_binding.AssociatedObjectType())
        obj.set_association_type(self.association_type_)
        return obj

    def to_dict(self):
        object_dict = super(AssociatedObject, self).to_dict()
        object_dict['association_type'] = self.association_type_
        return object_dict

    @staticmethod
    def from_obj(object_obj):
        if not object_obj:
            return None
        obj = Object.from_obj(object_obj, AssociatedObject())
        obj.association_type_ = object_obj.get_association_type()
        return obj

    @staticmethod
    def from_dict(object_dict):
        if not object_dict:
            return None
        obj = Object.from_dict(object_dict, AssociatedObject())
        obj.association_type_ = object_dict.get('association_type', None)
        return obj


    #@classmethod
    #def object_from_dict(cls, associated_object_dict):
    #    """Create the Associated Object Python object representation from an input dictionary"""
    #    associated_obj = Object.object_from_dict(associated_object_dict,core_binding.AssociatedObjectType())
    #    for key, value in associated_object_dict.items():
    #        if key == 'association_type' and utils.test_value(value): associated_obj.set_association_type(value)
    #    return associated_obj

    #@classmethod
    #def dict_from_object(cls, associated_obj):
    #    """Parse and return a dictionary for an Associated Object"""
    #    associated_object_dict = Object.dict_from_object(associated_obj)
    #    if associated_obj.get_association_type() is not None: associated_object_dict['association_type'] = associated_obj.get_association_type()
    #    return associated_object_dict