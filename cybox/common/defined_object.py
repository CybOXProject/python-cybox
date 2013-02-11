import cybox
import cybox.bindings.cybox_core_1_0 as core_binding


class DefinedObject(cybox.Entity):
    """
    The Cybox DefinedObject base class.

    """

    def to_obj(self):
        #TODO: subclasses should save xsi-type
        raise NotImplementedError()

    def to_dict(self):
        #TODO: subclasses should save xsi-type
        raise NotImplementedError()

    @staticmethod
    def from_obj(defobj_obj):
        any_attributes = defined_object.get_anyAttributes_()
        xsi_type = any_attributes.get('{http://www.w3.org/2001/XMLSchema-instance}type')
        if not xsi_type:
            raise ValueError("Object has no xsi-type")
        type_value = xsi_type.split(':')[1]

        # Find the class that can parse this type.
        klass = cybox.utils.get_class_for_object_type(type_value)

        return klass.from_obj(defobj_obj)

    @staticmethod
    def from_dict(defobj_dict):
        obj_type = defobj_dict.get('object-type')
        if not xsi_type:
            raise ValueError("Dictionary has no xsi-type")
        klass = cybox.utils.get_class_for_object_type(obj_type)

        print defobj_dict
        print klass
        return klass.from_dict(defobj_dict)

    @classmethod
    def object_from_dict(cls, defined_object_dict):
        """Create the Defined Object Python object representation from an input dictionary"""
        return cls.from_dict(defined_object_dict).to_obj()

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a defined object"""
        return cls.from_obj(defined_object).to_dict()
#        defined_object_dict = {}
#        any_attributes = defined_object.get_anyAttributes_()
#        for key, value in any_attributes.items():
#            if key == '{http://www.w3.org/2001/XMLSchema-instance}type':
#                type_value = value.split(':')[1]
#                defined_object_dict['xsi:type'] = type_value
#                object_type = core_binding.defined_objects.get(type_value).get('binding_name').split('_object')[0] + '_object'
#                defined_object_dict['object_type'] = object_type
#                object_api = globals().get(object_type)
#                try:
#                    return getattr(object_api, 'dict_from_object')(defined_object, defined_object_dict)
#                except AttributeError:
#                    return defined_object_dict
