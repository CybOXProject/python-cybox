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

    def __init__(self):
        super(Property, self).__init__()
        self.name = None
        self.description = None

    def to_obj(self, ns_info=None):
        property_obj = super(Property, self).to_obj(ns_info=ns_info)
        if self.name is not None:
            property_obj.name = self.name
        if self.description is not None:
            property_obj.description = self.description
        return property_obj

    def to_dict(self):
        property_dict = super(Property, self).to_dict()
        if self.name is not None:
            property_dict['name'] = self.name
        if self.description is not None:
            property_dict['description'] = self.description
        return property_dict

    def is_plain(self):
        """Whether the Property can be represented as a single value."""
        return (
            self.name is None and
            self.description is None and
            super(Property, self).is_plain()
        )

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        prop = super(Property, cls).from_dict(cls_dict)
        prop.name = cls_dict.get('name')
        prop.description = cls_dict.get('description')

        return prop

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        prop = super(Property, cls).from_obj(cls_obj)
        prop.name = cls_obj.name
        prop.description = cls_obj.description
        return prop


class CustomProperties(entities.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CustomPropertiesType
    _binding_var = "Property"
    _contained_type = Property
    _namespace = 'http://cybox.mitre.org/common-2'


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
        self.custom_properties = None

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

        # if self.object_reference is not None:
        #     obj.object_reference = self.object_reference
        # if self.custom_properties is not None:
        #     obj.Custom_Properties = self.custom_properties.to_obj(ns_info=ns_info)
        if self._XSI_TYPE and self._XSI_NS:
            obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

        return obj

    # def _finalize_obj(self, partial_obj=None):
    #     """Add xsi_type to the binding object."""
    #
    #     # The _XSI_NS and _XSI_TYPE are set by concrete implementations.
    #     partial_obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

    def to_dict(self):
        d = super(ObjectProperties, self).to_dict()

        # if self.object_reference is not None:
        #     d['object_reference'] = self.object_reference
        # if self.custom_properties is not None:
        #     d['custom_properties'] = self.custom_properties.to_list()
        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        return d

    # def _finalize_dict(self, partial_dict=None):
    #     """Add xsi:type to the dictionary."""
    #
    #     partial_dict['xsi:type'] = self._XSI_TYPE

    # @classmethod
    # def from_obj(cls, cls_obj):
    #     # This is a bit of a hack. If this is being called directly on the
    #     # ObjectProperties class, then we don't know the xsi_type of the
    #     # ObjectProperties, so we need to look it up. Otherwise, if this is
    #     # being called on a particular subclass of ObjectProperties (for
    #     # example, Address), we can skip directly to the entities.Entity
    #     # implementation.
    #     if not cls_obj:
    #         return None
    #
    #     defobj = super(ObjectProperties, cls).from_obj(cls_obj)
    #     defobj.object_reference = cls_obj.object_reference
    #     defobj.custom_properties = CustomProperties.from_obj(cls_obj.Custom_Properties)
    #
    #     return defobj
    #
    # @classmethod
    # def from_dict(cls, cls_dict):
    #     if not cls_dict:
    #         return None
    #
    #     defobj = super(ObjectProperties, cls).from_dict(cls_dict)
    #     defobj.object_reference = cls_dict.get('object_reference')
    #     defobj.custom_properties = CustomProperties.from_list(cls_dict.get('custom_properties'))
    #
    #     return defobj
