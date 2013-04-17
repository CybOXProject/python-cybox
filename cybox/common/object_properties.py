import cybox


class DefinedObject(cybox.Entity):
    """The Cybox DefinedObject base class."""

    def __init__(self):
        self.object_reference = None
        self.parent = None

    @property
    def parent(self):
        if not self._parent:
            self._parent = cybox.core.object.Object(self)
        return self._parent

    @parent.setter
    def parent(self, value):
        if value and not isinstance(value, cybox.core.object.Object):
            raise ValueError("Must be an Object")
        self._parent = value

    def add_related(self, related, relationship, inline=True):
        self.parent.add_related(related, relationship, inline)

    def to_obj(self, partial_obj=None):
        raise NotImplementedError()

    def _populate_obj(self, obj):
        if self.object_reference is not None:
            obj.set_object_reference(self.object_reference)

    def to_dict(self):
        raise NotImplementedError()

    def _populate_dict(self, dict_):
        if self.object_reference is not None:
            dict_['object_reference'] = self.object_reference
        dict_['xsi:type'] = self._XSI_TYPE

    @staticmethod
    def from_obj(defobj_obj):
        if not defobj_obj:
            return None
        any_attributes = defobj_obj.get_anyAttributes_()
        xsi_type = any_attributes.get('{http://www.w3.org/2001/XMLSchema-instance}type')
        if not xsi_type:
            raise ValueError("Object has no xsi:type")
        type_value = xsi_type.split(':')[1]

        # Find the class that can parse this type.
        klass = cybox.utils.get_class_for_object_type(type_value)

        return klass.from_obj(defobj_obj)

    def _populate_from_obj(self, obj):
        self.object_reference = obj.get_object_reference()

    @staticmethod
    def from_dict(defobj_dict):
        if not defobj_dict:
            return None

        xsi_type = defobj_dict.get('xsi:type', None)
        if not xsi_type:
            raise ValueError('dictionary does not have xsi:type key')

        klass = cybox.utils.get_class_for_object_type(xsi_type)
        defobj = klass.from_dict(defobj_dict)

        return defobj

    def _populate_from_dict(self, dict_):
        self.object_reference = dict_.get('object_reference')
