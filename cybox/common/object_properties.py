# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils
import cybox.bindings.cybox_common as common_binding

from .properties import String


class Property(String):
    _binding_class = common_binding.PropertyType

    def __init__(self):
        super(Property, self).__init__()
        self.name = None
        self.description = None

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        property_obj = super(Property, self).to_obj(return_obj=return_obj, ns_info=ns_info)
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

    @staticmethod
    def from_dict(property_dict):
        if not property_dict:
            return None
        prop = Property()
        prop._populate_from_dict(property_dict)
        prop.name = property_dict.get('name')
        prop.description = property_dict.get('description')
        return prop

    @staticmethod
    def from_obj(property_obj):
        if not property_obj:
            return None
        prop = Property()
        prop._populate_from_obj(property_obj)
        prop.name = property_obj.name
        prop.description = property_obj.description
        return prop


class CustomProperties(cybox.EntityList):
    _binding = common_binding
    _binding_class = common_binding.CustomPropertiesType
    _binding_var = "Property"
    _contained_type = Property
    _namespace = 'http://cybox.mitre.org/common-2'


class ObjectProperties(cybox.Entity):
    """The Cybox ObjectProperties base class."""

    object_reference = cybox.TypedField("object_reference")
    custom_properties = cybox.TypedField("Custom_Properties", CustomProperties)

    def __init__(self):
        super(ObjectProperties, self).__init__()
        self.parent = None
        self.custom_properties = None

    @property
    def parent(self):
        if not self._parent:
            self._parent = cybox.core.Object(self)
        return self._parent

    @parent.setter
    def parent(self, value):
        if value and not isinstance(value, cybox.core.Object):
            raise ValueError("Must be an Object")
        self._parent = value

    def add_related(self, related, relationship, inline=True):
        self.parent.add_related(related, relationship, inline)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        # TODO: Hack until all ObjectProperties use TypedField
        if return_obj is None:
            return super(ObjectProperties, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.object_reference is not None:
            return_obj.object_reference = self.object_reference
        if self.custom_properties is not None:
            return_obj.Custom_Properties = self.custom_properties.to_obj(ns_info=ns_info)

        self._finalize_obj(return_obj)

    def _finalize_obj(self, partial_obj=None):
        """Add xsi_type to the binding object."""

        partial_obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

    def to_dict(self, partial_dict=None):
        # TODO: Hack until all ObjectProperties use TypedField
        if partial_dict is None:
            return super(ObjectProperties, self).to_dict()

        if self.object_reference is not None:
            partial_dict['object_reference'] = self.object_reference
        if self.custom_properties is not None:
            partial_dict['custom_properties'] = self.custom_properties.to_list()

        self._finalize_dict(partial_dict)

    def _finalize_dict(self, partial_dict=None):
        """Add xsi:type to the dictionary."""

        partial_dict['xsi:type'] = self._XSI_TYPE

    @classmethod
    def from_obj(cls, defobj_obj, defobj=None):
        # This is a bit of a hack. If this is being called directly on the
        # ObjectProperties class, then we don't know the xsi_type of the
        # ObjectProperties, so we need to look it up. Otherwise, if this is
        # being called on a particular subclass of ObjectProperties (for
        # example, Address), we can skip directly to the cybox.Entity
        # implementation.
        if cls is not ObjectProperties:
            return super(ObjectProperties, cls()).from_obj(defobj_obj)

        if not defobj_obj:
            return None

        if not defobj:
            xsi_type = defobj_obj.xsi_type
            if not xsi_type:
                raise ValueError("Object has no xsi:type")
            type_value = xsi_type.split(':')[1]

            # Find the class that can parse this type.
            klass = cybox.utils.get_class_for_object_type(type_value)
            defobj = klass.from_obj(defobj_obj)

        defobj.object_reference = defobj_obj.object_reference
        defobj.custom_properties = CustomProperties.from_obj(defobj_obj.Custom_Properties)

        return defobj

    @classmethod
    def from_dict(cls, defobj_dict, defobj=None):
        # Also a hack. See comment on from_obj
        if cls is not ObjectProperties:
            return super(ObjectProperties, cls()).from_dict(defobj_dict)

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
