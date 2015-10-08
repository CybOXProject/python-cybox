# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox import entities
from mixbox import idgen

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common.object_properties import ObjectPropertiesFactory, ObjectProperties
from cybox.common.vocabs import VocabString, VocabFactory
from cybox.common.vocabs import ObjectRelationship as Relationship


_EXTERNAL_CLASSES = {}  # Maps xsi:type values to binding


def add_external_class(klass, xsi_type):
    """Adds a class implementation to this binding's globals() dict.

    These classes can be used to implement Properties,
    Domain_Specific_Object_Properties, or Defined_Effect fields on an Object.

    Args:
        klass (class): Python class that implements the new type
        xsi_type (str): An xsi:type value corresponding to the `klass`.
    """
    _EXTERNAL_CLASSES[xsi_type] = klass


class ExternalTypeFactory(entities.EntityFactory):
    def entity_class(cls, key):
        return _EXTERNAL_CLASSES[key]


class Object(entities.Entity):
    """The CybOX Object element.

    Currently only supports the following data members:
    - id\_
    - idref
    - properties
    - related_objects
    - domain specific object properties
    """
    _binding = core_binding
    _binding_class = _binding.ObjectType
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, properties=None, type_=None):
        # TODO: Accept id_ as an argument
        super(Object, self).__init__()
        if properties:
            prefix = str(properties.__class__.__name__)
        else:
            prefix = "Object"
        self.id_ = idgen.create_id(prefix=prefix)
        self.idref = None
        self.properties = properties
        self.related_objects = []
        self.domain_specific_object_properties = None

    def __str__(self):
        return self.id_

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        if value and not isinstance(value, ObjectProperties):
            raise ValueError("Not a ObjectProperties")
        self._properties = value

        self._modify_childs_parent()

    def _modify_childs_parent(self):
        if self._properties:
            self._properties.parent = self

    def add_related(self, related, relationship, inline=True):
        if not isinstance(related, ObjectProperties):
            raise ValueError("Must be a ObjectProperties")
        r = RelatedObject(related, relationship=relationship, inline=inline)
        self.related_objects.append(r)

    def to_obj(self, ns_info=None):
        obj = super(Object, self).to_obj(ns_info=ns_info)

        if self.id_:
            obj.id = self.id_
        if self.idref:
            obj.idref = self.idref
        if self.properties:
            obj.Properties = self.properties.to_obj(ns_info=ns_info)
        if self.related_objects:
            relobj_obj = core_binding.RelatedObjectsType()
            for x in self.related_objects:
                relobj_obj.add_Related_Object(x.to_obj(ns_info=ns_info))
            obj.Related_Objects = relobj_obj
        if self.domain_specific_object_properties is not None:
            obj.Domain_Specific_Object_Properties = self.domain_specific_object_properties.to_obj(ns_info=ns_info)

        return obj

    def to_dict(self):
        obj_dict = super(Object, self).to_dict()

        if self.id_:
            obj_dict['id'] = self.id_
        if self.idref:
            obj_dict['idref'] = self.idref
        if self.properties:
            obj_dict['properties'] = self.properties.to_dict()
        if self.related_objects:
            obj_dict['related_objects'] = [x.to_dict() for x in
                                                self.related_objects]
        if self.domain_specific_object_properties is not None:
            obj_dict['domain_specific_object_properties'] = self.domain_specific_object_properties.to_dict()

        return obj_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(Object, cls).from_obj(cls_obj)

        obj.id_ = cls_obj.id
        obj.idref = cls_obj.idref
        obj.properties = ObjectPropertiesFactory.from_obj(cls_obj.Properties)
        obj.domain_specific_object_properties = ExternalTypeFactory.from_obj(cls_obj.Domain_Specific_Object_Properties)
        rel_objs = cls_obj.Related_Objects

        if rel_objs:
            obj.related_objects = [RelatedObject.from_obj(x) for x in rel_objs.Related_Object]

        if obj.id_:
            cybox.utils.cache_put(obj)

        return obj

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        obj = super(Object, cls).from_dict(cls_dict)

        obj.id_ = cls_dict.get('id')
        obj.idref = cls_dict.get('idref')
        obj.properties = ObjectPropertiesFactory.from_dict(cls_dict.get('properties'))
        obj.related_objects = [RelatedObject.from_dict(x) for x in cls_dict.get('related_objects', [])]
        obj.domain_specific_object_properties = ExternalTypeFactory.from_dict(cls_dict.get('domain_specific_object_properties'))

        if obj.id_:
            cybox.utils.cache_put(obj)

        return obj


class RelatedObject(Object):
    _binding = core_binding
    _binding_class = _binding.RelatedObjectType

    def __init__(self, *args, **kwargs):
        self.relationship = kwargs.pop('relationship', None)
        self._inline = kwargs.pop('inline', True)
        super(RelatedObject, self).__init__(*args, **kwargs)

        if not self._inline and self.properties:
            self.idref = self.properties.parent.id_

    def __str__(self):
        return "Related: " + super(RelatedObject, self).__str__()

    #TODO: make this a property somehow
    def get_properties(self):
        if self.properties:
            return self.properties
        elif self.idref:
            return cybox.utils.cache_get(self.idref).properties
        else:
            return None

    def _modify_childs_parent(self):
        if self._inline:
            super(RelatedObject, self)._modify_childs_parent()

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        if not value:
            self._relationship = None
        elif isinstance(value, VocabString):
            self._relationship = value
        else:
            self._relationship = Relationship(value)

    def to_obj(self, ns_info=None):
        relobj_obj = super(RelatedObject, self).to_obj(ns_info=ns_info)

        if not self._inline:
            relobj_obj.idref = self.idref

        if self.relationship:
            relobj_obj.Relationship = self.relationship.to_obj(ns_info=ns_info)

        return relobj_obj

    def to_dict(self):
        if self._inline:
            relobj_dict = super(RelatedObject, self).to_dict()
        else:
            relobj_dict = {'idref': self.idref}

        if self.relationship:
            relobj_dict['relationship'] = self.relationship.to_dict()

        return relobj_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        relobj = super(RelatedObject, cls).from_obj(cls_obj)
        relobj.relationship = VocabFactory.from_obj(cls_obj.Relationship)

        if relobj.idref:
            relobj._inline = True

        return relobj

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        relobj = super(RelatedObject, cls).from_dict(cls_dict)
        relobj.relationship = VocabFactory.from_dict(cls_dict.get('relationship'))

        if relobj.idref:
            relobj._inline = True

        return relobj


class DomainSpecificObjectProperties(entities.Entity):
    """The Cybox DomainSpecificObjectProperties base class."""

    _binding = core_binding
    _binding_class = _binding.DomainSpecificObjectPropertiesType

    # Override in subclass
    _XSI_TYPE = None
    _XSI_NS = None

    def to_obj(self, ns_info=None):
        obj = super(DomainSpecificObjectProperties, self).to_obj(ns_info=ns_info)
        obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

    def to_dict(self):
        d = super(DomainSpecificObjectProperties, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE
        return d


