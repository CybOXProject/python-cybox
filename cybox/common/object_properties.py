# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
import cybox.objects

from .properties import String


class Property(String):
    _binding = common_binding
    _binding_class = _binding.PropertyType

    name = fields.TypedField("name")
    description = fields.TypedField("description")

    def is_plain(self):
        """Whether the Property can be represented as a single value."""
        return (
            self.name is None and
            self.description is None and
            super(Property, self).is_plain()
        )


class CustomProperties(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CustomPropertiesType
    _namespace = 'http://cybox.mitre.org/common-2'
    property_ = fields.TypedField("Property", Property, multiple=True)


class ObjectPropertiesFactory(entities.EntityFactory):
    @classmethod
    def objkey(cls, obj):
        xsi_type = obj.xsi_type

        if not xsi_type:
            raise ValueError("No xsi:type found on ObjectProperties instance.")

        return xsi_type.split(":")[1]

    @classmethod
    def entity_class(cls, key):
        if not key:
            raise ValueError("Must provide an xsi:type key for ObjectProperties.")
        return cybox.objects.get_class_for_object_type(key)


class ObjectProperties(entities.Entity):
    """The Cybox ObjectProperties base class."""
    _XSI_TYPE = None
    _XSI_NS   = None
    _binding = common_binding
    _binding_class = _binding.ObjectPropertiesType

    object_reference = fields.TypedField("object_reference")
    custom_properties = fields.TypedField("Custom_Properties", CustomProperties)

    def __init__(self):
        super(ObjectProperties, self).__init__()
        self.parent = None

    @property
    def parent(self):
        import cybox.core

        if not self._parent:
            self._parent = cybox.core.Object(self)
        return self._parent

    @parent.setter
    def parent(self, value):
        import cybox.core

        if value and not isinstance(value, cybox.core.Object):
            raise ValueError("Must be an Object")
        self._parent = value

    def add_related(self, related, relationship, inline=True):
        self.parent.add_related(related, relationship, inline)

    def to_obj(self, ns_info=None):
        obj = super(ObjectProperties, self).to_obj(ns_info=ns_info)

        if self._XSI_TYPE and self._XSI_NS:
            obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

        return obj

    def to_dict(self):
        d = super(ObjectProperties, self).to_dict()

        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        return d
