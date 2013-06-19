# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils
import cybox.bindings.cybox_common as common_binding
from cybox.common import String

class ObjectProperties(cybox.Entity):
    """The Cybox ObjectProperties base class."""

    def __init__(self):
        self.object_reference = None
        self.parent = None
        self.custom_properties = None

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
        """Populate an existing bindings object.

        Note that this is different than to_obj() on most other CybOX types.
        """
        if not partial_obj:
            raise NotImplementedError()

        partial_obj.set_xsi_type("%s:%s" % (self._XSI_NS, self._XSI_TYPE))
        if self.object_reference is not None:
            partial_obj.set_object_reference(self.object_reference)
        if self.custom_properties is not None:
            partial_obj.set_Custom_Properties(self.custom_properties.to_obj())

    def to_dict(self, partial_dict=None):
        """Populate an existing dictionary.

        Note that this is different than to_dict() on most other CybOX types.
        """
        if partial_dict is None:
            raise NotImplementedError()

        partial_dict['xsi:type'] = self._XSI_TYPE
        if self.object_reference is not None:
            partial_dict['object_reference'] = self.object_reference
        if self.custom_properties is not None:
            partial_dict['custom_properties'] = self.custom_properties.to_list()

    @staticmethod
    def from_obj(defobj_obj, defobj=None):
        if not defobj_obj:
            return None

        if not defobj:
            xsi_type = defobj_obj.get_xsi_type()
            if not xsi_type:
                raise ValueError("Object has no xsi:type")
            type_value = xsi_type.split(':')[1]

            # Find the class that can parse this type.
            klass = cybox.utils.get_class_for_object_type(type_value)
            defobj = klass.from_obj(defobj_obj)

        defobj.object_reference = defobj_obj.get_object_reference()
        defobj.custom_properties = CustomProperties.from_obj(defobj_obj.get_Custom_Properties())

        return defobj

    @staticmethod
    def from_dict(defobj_dict, defobj=None):
        if not defobj_dict:
            return None

        if not defobj:
            xsi_type = defobj_dict.get('xsi:type')
            if not xsi_type:
                raise ValueError('dictionary does not have xsi:type key')

            klass = cybox.utils.get_class_for_object_type(xsi_type)
            defobj = klass.from_dict(defobj_dict)

        defobj.object_reference = defobj_dict.get('object_reference')
        defobj.custom_properties = CustomProperties.from_list(defobj_dict.get('custom_properties'))

        return defobj

class Property(String):
    def __init__(self):
        super(Property, self).__init__()
        self.name = None
        self.description = None

    def to_obj(self):
        property_obj = super(Property, self).to_obj()
        if self.name is not None : property_obj.set_name(self.name)
        if self.description is not None : property_obj.set_description(self.name)
        return property_obj

    def to_dict(self):
        property_dict = super(Property, self).to_dict()
        if self.name is not None : property_dict['name'] = self.name
        if self.description is not None : property_dict['description'] = self.description
        return property_dict
    
    @staticmethod
    def from_dict(property_dict):
        if not property_dict:
            return None
        property_ = Property()
        property_._populate_from_dict(property_dict)
        property_.name = property_dict.get('name')
        property_.description = property_dict.get('description')
        return property_

    @staticmethod
    def from_obj(property_obj):
        if not property_obj:
            return None
        property_ = Property()
        property_._populate_from_obj(property_obj)
        property_.name = property_obj.get_name()
        property_.description = property_obj.get_description()
        return property_
         
    def _get_binding_class(self):
        return common_binding.PropertyType

class CustomProperties(cybox.EntityList):
    _contained_type = Property
    _binding_class = common_binding.CustomPropertiesType

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Property(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Property()