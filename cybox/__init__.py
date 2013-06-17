# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "2.0.0b3"

import collections
import json
from StringIO import StringIO

from cybox.utils import NamespaceParser, META


def get_xmlns_string(ns_set):
    """Build a string with 'xmlns' definitions for every namespace in ns_set.

    Arguments:
    - ns_set: a set (or other iterable) of Namespace objects
    """
    xmlns_format = 'xmlns:{0.prefix}="{0.name}"'
    return "\n\t".join([xmlns_format.format(x) for x in ns_set])


def get_schemaloc_string(ns_set):
    """Build a "schemaLocation" string for every namespace in ns_set.

    Arguments:
    - ns_set: a set (or other iterable) of Namespace objects
    """
    schemaloc_format = '{0.name} {0.schema_location}'
    # Only include schemas that have a schema_location defined (for instance,
    # 'xsi' does not.
    return " ".join([schemaloc_format.format(x) for x in ns_set
                     if x.schema_location])


class Entity(object):
    """Base class for all classes in the Cybox SimpleAPI."""

    def to_xml(self, include_namespaces=False):
        """Export an object as an XML String"""

        if include_namespaces:
            namespace_def = self._get_namespace_def()
        else:
            namespace_def = ""

        s = StringIO()
        self.to_obj().export(s, 0, namespacedef_=namespace_def)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    def _get_namespace_def(self):
        # copy necessary namespaces
        namespaces = self._get_namespaces()

        # if there are any other namepaces, include xsi for "schemaLocation"
        if namespaces:
            namespaces.update([META.lookup_prefix('xsi')])

        if not namespaces:
            return ""

        return ('\n\t' + get_xmlns_string(namespaces) +
                '\n\txsi:schemaLocation="' + get_schemaloc_string(namespaces) +
                '"')

    def _get_namespaces(self, recurse=True):
        ns = set()

        try:
            ns.update([META.lookup_namespace(self._namespace)])
        # TODO: Remove this 'except' once every class has defined a _namespace
        except AttributeError:
            pass

        #In case of recursive relationships, don't process this item twice
        self.touched = True
        if recurse:
            for x in self._get_children():
                if not hasattr(x, 'touched'):
                    ns.update(x._get_namespaces())

        del self.touched

        #print self.__class__, "-", ns
        return ns

    def _get_children(self):
        for k, v in vars(self).items():
            if isinstance(v, Entity):
                yield v
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, Entity):
                        yield item

    @classmethod
    def object_from_dict(cls, entity_dict):
        """Convert from dict representation to object representation."""
        return cls.from_dict(entity_dict).to_obj()

    @classmethod
    def dict_from_object(cls, entity_obj):
        """Convert from object representation to dict representation."""
        return cls.from_obj(entity_obj).to_dict()


class EntityList(collections.MutableSequence, Entity):
    _contained_type = object

    def __init__(self):
        self._inner = []

    def __getitem__(self, key):
        return self._inner.__getitem__(key)

    def __setitem__(self, key, value):
        if not self._is_valid(value):
            value = self._try_fix_value(value)
        self._inner.__setitem__(key, value)

    def __delitem__(self, key):
        self._inner.__delitem__(key)

    def __len__(self):
        return len(self._inner)

    def insert(self, idx, value):
        if not self._is_valid(value):
            value = self._try_fix_value(value)
        self._inner.insert(idx, value)

    def _is_valid(self, value):
        """Check if this is a valid object to add to the list.

        If the function is not overridden, only objects of type
        _contained_type can be added.
        """
        return isinstance(value, self._contained_type)

    def _try_fix_value(self, value):
        new_value = self._fix_value(value)
        if not new_value:
            raise ValueError("Can't put '%s' (%s) into a %s" %
                (value, type(value), self.__class__))
        return new_value

    def _fix_value(self, value):
        """Attempt to coerce value into the correct type.

        Subclasses should define this function.
        """
        pass

    @staticmethod
    def _set_list(binding_object, list_):
        """Call the proper method on the binding object to set its value.

        In general, these should be of the form:
            binding_object.set_<something>(list_)

        Since <something> differs fromt class to class, this cannot be done
        generically.
        """
        raise NotImplementedError

    @staticmethod
    def _get_list(binding_object):
        """Call the proper method on the binding object to get its value.

        In general, these should be of the form:
            return binding_object.get_<something>()

        Since <something> differs fromt class to class, this cannot be done
        generically.
        """
        raise NotImplementedError

    # The next four functions can be overridden, but otherwise define the
    # default behavior, for EntityList subclasses which define _contained_type,
    # _binding_class, _get_list, and _set_list

    def to_obj(self, object_type=None):
        tmp_list = [x.to_obj() for x in self]

        if not object_type:
            list_obj = self._binding_class()
        else:
            list_obj = object_type
        self._set_list(list_obj, tmp_list)

        return list_obj

    def to_list(self):
        return [h.to_dict() for h in self]

    @classmethod
    def from_obj(cls, list_obj, list_class=None):
        if not list_obj:
            return None

        if not list_class:
            list_ = cls()
        else:
            list_ = list_class

        for item in cls._get_list(list_obj):
            list_.append(cls._contained_type.from_obj(item))

        return list_

    @classmethod
    def from_list(cls, list_list, list_class=None):
        if not isinstance(list_list, list):
            return None

        if not list_class:
            list_ = cls()
        else:
            return None

        for item in list_list:
            list_.append(cls._contained_type.from_dict(item))

        return list_

    @classmethod
    def object_from_list(cls, entitylist_list):
        """Convert from list representation to object representation."""
        return cls.from_list(entitylist_list).to_obj()

    @classmethod
    def list_from_object(cls, entitylist_obj):
        """Convert from object representation to list representation."""
        return cls.from_obj(entitylist_obj).to_list()


class ObjectReference(Entity):
    _binding_class = None

    def __init__(self, object_reference=None):
        self.object_reference = object_reference

    def to_obj(self):
        obj = self._binding_class()

        obj.set_object_reference(self.object_reference)

        return obj

    def to_dict(self):
        return {'object_reference': self.object_reference}

    @classmethod
    def from_obj(cls, ref_obj):
        if not ref_obj:
            return None

        ref = cls()
        ref.object_reference = ref_obj.get_object_reference()

        return ref

    @classmethod
    def from_dict(cls, ref_dict):
        if not ref_dict:
            return None

        ref = cls()
        ref.object_reference = ref_dict.get('object_reference')

        return ref


class ReferenceList(EntityList):

    def _fix_value(self, value):
        if isinstance(value, basestring):
            return self._contained_type(value)


class TypedField(object):

    def __init__(self, name, type_, try_cast=True):
        self.name = name
        self.type_ = type_
        self.try_cast = try_cast

    def __get__(self, instance, owner):
        # TODO: move this to cybox.Entity constructor
        if not hasattr(instance, "_fields"):
            instance._fields = {}
        return instance._fields.get(self.name)

    def __set__(self, instance, value):
        # TODO: move this to cybox.Entity constructor
        if not hasattr(instance, "_fields"):
            instance._fields = {}

        if value is not None and not isinstance(value, self.type_):
            if self.try_cast:
                value = self.type_(value)
            else:
                raise ValueError("%s must be a %s, not a %s" %
                                    (self.__name__, self.type_, type(value)))
        instance._fields[self.name] = value
