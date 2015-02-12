# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import ObjectProperties, VocabString


def add_external_class(klass, name=None):
    """Adds a class implementation to this binding's globals() dict.

    These classes can be used to implement Properties,
    Domain_Specific_Object_Properties, or Defined_Effect fields on an Object.

    Args:
        klass (class): Python class that implements the new type
        name (str): The name of the class, as it will appear in XML documents
            to be parsed.  Defaults to ``klass.__name__``.
    """

    if name is None:
        name = klass.__name__

    module = sys.modules[__name__]
    setattr(module, name, klass)


class Object(cybox.Entity):
    """The CybOX Object element.

    Currently only supports the following data members:
    - id\_
    - idref
    - properties
    - related_objects
    """
    _binding = core_binding
    _namespace = 'http://cybox.mitre.org/cybox-2'

    def __init__(self, properties=None, type_=None):
        # TODO: Accept id_ as an argument
        super(Object, self).__init__()
        if properties:
            prefix = str(properties.__class__.__name__)
        else:
            prefix = "Object"
        self.id_ = cybox.utils.create_id(prefix=prefix)
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

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if return_obj == None:
            obj = core_binding.ObjectType()
        else:
            obj = return_obj

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
        obj_dict = {}
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

    @staticmethod
    def from_obj(object_obj, obj=None):
        if not object_obj:
            return None

        if not obj:
            obj = Object()

        obj.id_ = object_obj.id
        obj.idref = object_obj.idref
        obj.properties = ObjectProperties.from_obj(object_obj.Properties)
        obj.domain_specific_object_properties = DomainSpecificObjectProperties.from_obj(object_obj.Domain_Specific_Object_Properties)
        rel_objs = object_obj.Related_Objects
        if rel_objs:
            obj.related_objects = [RelatedObject.from_obj(x) for x in
                                   rel_objs.Related_Object]

        if obj.id_:
            cybox.utils.cache_put(obj)

        return obj

    @staticmethod
    def from_dict(object_dict, obj=None):
        if not object_dict:
            return None

        if not obj:
            obj = Object()

        obj.id_ = object_dict.get('id')
        obj.idref = object_dict.get('idref')
        obj.properties = ObjectProperties.from_dict(
                                    object_dict.get('properties'))
        obj.related_objects = [RelatedObject.from_dict(x) for x in
                                        object_dict.get('related_objects', [])]
        obj.domain_specific_object_properties = DomainSpecificObjectProperties.from_dict(object_dict.get('domain_specific_object_properties'))

        if obj.id_:
            cybox.utils.cache_put(obj)

        return obj


class Relationship(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ObjectRelationshipVocab-1.1'


class RelatedObject(Object):

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
            try:
                return cybox.utils.cache_get(self.idref).properties
            except cybox.utils.CacheMiss:
                raise
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
        if value and not isinstance(value, Relationship):
            value = Relationship(value)
        self._relationship = value

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        relobj_obj = core_binding.RelatedObjectType()

        if self._inline:
            super(RelatedObject, self).to_obj(return_obj=relobj_obj, ns_info=ns_info)
        else:
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

    @staticmethod
    def from_obj(relobj_obj):
        if not relobj_obj:
            return None

        relobj = RelatedObject()
        Object.from_obj(relobj_obj, relobj)
        relobj.relationship = Relationship.from_obj(relobj_obj.Relationship)

        if relobj.idref:
            relobj._inline = True

        return relobj

    @staticmethod
    def from_dict(relobj_dict):
        if not relobj_dict:
            return None

        relobj = RelatedObject()
        Object.from_dict(relobj_dict, relobj)
        relobj.relationship = Relationship.from_dict(relobj_dict.get('relationship'))

        if relobj.idref:
            relobj._inline = True

        return relobj


class DomainSpecificObjectProperties(cybox.Entity):
    """The Cybox DomainSpecificObjectProperties base class."""

    def to_obj(self, return_obj=None, ns_info=None):
        """Populate an existing bindings object.

        Note that this is different than to_obj() on most other CybOX types.
        """
        if not return_obj:
            raise NotImplementedError()

        self._collect_ns_info(ns_info)
        return_obj.xsi_type = "%s:%s" % (self._XSI_NS, self._XSI_TYPE)

    def to_dict(self, partial_dict=None):
        """Populate an existing dictionary.

        Note that this is different than to_dict() on most other CybOX types.
        """
        if partial_dict is None:
            raise NotImplementedError()

        partial_dict['xsi:type'] = self._XSI_TYPE

    @staticmethod
    def from_obj(domain_specific_properties_obj):
        if not domain_specific_properties_obj:
            return None

        xsi_type = domain_specific_properties_obj.xsi_type
        if not xsi_type:
            raise ValueError("Object has no xsi:type")

        # Find the class that can parse this type.
        klass_name = xsi_type.split(':')[1].rstrip('Type')
        klass = globals()[klass_name]
        dom_obj = klass.from_obj(domain_specific_properties_obj)

        return dom_obj

    @staticmethod
    def from_dict(domain_specific_properties_dict):
        if not domain_specific_properties_dict:
            return None

        xsi_type = defobj_dict.get('xsi:type')
        if not xsi_type:
            raise ValueError('dictionary does not have xsi:type key')

        # Find the class that can parse this type.
        klass_name = xsi_type.split(':')[1].rstrip('Type')
        klass = globals()[klass_name]
        dom_obj = klass.from_dict(domain_specific_properties_dict)

        return dom_obj
