# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "2.1.0.9"

import collections
import inspect
import json
from StringIO import StringIO

import cybox.bindings as bindings
import cybox.utils.idgen
from cybox.utils import Namespace, META

def get_xmlns_string(ns_set):
    """Build a string with 'xmlns' definitions for every namespace in ns_set.

    Args:
        ns_set (iterable): set of Namespace objects
    """
    xmlns_format = 'xmlns:{0.prefix}="{0.name}"'
    return "\n\t".join([xmlns_format.format(x) for x in ns_set])


def get_schemaloc_string(ns_set):
    """Build a "schemaLocation" string for every namespace in ns_set.

    Args:
        ns_set (iterable): set of Namespace objects
    """
    schemaloc_format = '{0.name} {0.schema_location}'
    # Only include schemas that have a schema_location defined (for instance,
    # 'xsi' does not.
    return " ".join([schemaloc_format.format(x) for x in ns_set
                     if x.schema_location])


class Entity(object):
    """Base class for all classes in the Cybox SimpleAPI."""

    # By default (unless a particular subclass states otherwise), try to "cast"
    # invalid objects to the correct class using the constructor. Entity
    # subclasses should either provide a "sane" constructor or set this to
    # False.
    _try_cast = True

    def __init__(self):
        self._fields = {}

    @classmethod
    def _get_vars(cls):
        var_list = []
        for (name, obj) in inspect.getmembers(cls, inspect.isdatadescriptor):
            if isinstance(obj, TypedField):
                var_list.append(obj)

        return var_list

    def __eq__(self, other):
        # This fixes some strange behavior where an object isn't equal to
        # itself
        if other is self:
            return True

        # I'm not sure about this, if we want to compare exact classes or if
        # various subclasses will also do (I think not), but for now I'm going
        # to assume they must be equal. - GTB
        if self.__class__ != other.__class__:
            return False

        var_list = self.__class__._get_vars()

        # If there are no TypedFields, assume this class hasn't been
        # "TypedField"-ified, so we don't want these to inadvertently return
        # equal.
        if not var_list:
            return False

        for f in var_list:
            if not f.comparable:
                continue
            if getattr(self, f.attr_name) != getattr(other, f.attr_name):
                return False

        return True

    def __ne__(self, other):
        return not self == other


    def _collect_ns_info(self, ns_info=None):
        if not ns_info:
            return
        ns_info.collect(self)


    def to_obj(self, return_obj=None, ns_info=None):
        """Convert to a GenerateDS binding object.

        Subclasses can override this function.

        Returns:
            An instance of this Entity's ``_binding_class`` with properties
            set from this Entity.
        """
        self._collect_ns_info(ns_info)

        entity_obj = self._binding_class()

        vars = {}
        for klass in self.__class__.__mro__:
            if klass is Entity:
                break
            vars.update(klass.__dict__.iteritems())

        for name, field in vars.iteritems():
            if isinstance(field, TypedField):
                val = getattr(self, field.attr_name)

                if field.multiple:
                    if val:
                        val = [x.to_obj(return_obj=return_obj, ns_info=ns_info) for x in val]
                    else:
                        val = []
                elif isinstance(val, Entity):
                    val = val.to_obj(return_obj=return_obj, ns_info=ns_info)

                setattr(entity_obj, field.name, val)

        self._finalize_obj(entity_obj)
        return entity_obj

    def _finalize_obj(self, entity_obj):
        """Subclasses can define additional items in the binding object.

        `entity_obj` should be modified in place.
        """
        pass

    def to_dict(self):
        """Convert to a ``dict``

        Subclasses can override this function.

        Returns:
            Python dict with keys set from this Entity.
        """
        entity_dict = {}
        vars = {}
        for klass in self.__class__.__mro__:
            if klass is Entity:
                break
            vars.update(klass.__dict__.iteritems())

        for name, field in vars.iteritems():
            if isinstance(field, TypedField):
                val = getattr(self, field.attr_name)

                if field.multiple:
                    if val:
                        val = [x.to_dict() for x in val]
                    else:
                        val = []
                elif isinstance(val, Entity):
                    val = val.to_dict()

                # Only add non-None objects or non-empty lists
                if val is not None and val != []:
                    entity_dict[field.key_name] = val

        self._finalize_dict(entity_dict)

        return entity_dict

    def _finalize_dict(self, entity_dict):
        """Subclasses can define additional items in the dictionary.

        `entity_dict` should be modified in place.
        """
        pass

    @classmethod
    def from_obj(cls, cls_obj=None):
        if not cls_obj:
            return None

        entity = cls()

        for field in cls._get_vars():
            val = getattr(cls_obj, field.name)
            if field.type_:
                if field.multiple and val is not None:
                    val = [field.type_.from_obj(x) for x in val]
                else:
                    val = field.type_.from_obj(val)
            setattr(entity, field.attr_name, val)

        return entity

    @classmethod
    def from_dict(cls, cls_dict=None):
        if cls_dict is None:
            return None

        entity = cls()

        # Shortcut if an actual dict is not provided:
        if not isinstance(cls_dict, dict):
            value = cls_dict
            # Call the class's constructor
            try:
                return cls(value)
            except TypeError:
                raise TypeError("Could not instantiate a %s from a %s: %s" %
                                (cls, type(value), value))

        for field in cls._get_vars():
            val = cls_dict.get(field.key_name)
            if field.type_:
                if issubclass(field.type_, EntityList):
                    val = field.type_.from_list(val)
                elif field.multiple:
                    if val is not None:
                        val = [field.type_.from_dict(x) for x in val]
                    else:
                        val = []
                else:
                    val = field.type_.from_dict(val)
            else:
                if field.multiple and not val:
                    val = []
            setattr(entity, field.attr_name, val)

        return entity

    def to_xml(self, include_namespaces=True, namespace_dict=None,
               pretty=True, encoding='utf-8'):
        """Serializes a :class:`Entity` instance to an XML string.

        The default character encoding is ``utf-8`` and can be set via the
        `encoding` parameter. If `encoding` is ``None``, a unicode string
        is returned.

        Args:
            include_namespaces (bool): whether to include xmlns and
                xsi:schemaLocation attributes on the root element. Set to true by
                default.
            namespace_dict (dict): mapping of additional XML namespaces to
                prefixes
            pretty (bool): whether to produce readable (``True``) or compact
                (``False``) output. Defaults to ``True``.
            encoding: The output character encoding. Default is ``utf-8``. If
                `encoding` is set to ``None``, a unicode string is returned.

        Returns:
            An XML string for this
            :class:`Entity` instance. Default character encoding is ``utf-8``.

        """
        namespace_def = ""

        if include_namespaces:
            namespace_def = self._get_namespace_def(namespace_dict)

        if not pretty:
            namespace_def = namespace_def.replace('\n\t', ' ')


        with bindings.save_encoding(encoding):
            sio = StringIO()
            self.to_obj().export(
                sio.write,
                0,
                namespacedef_=namespace_def,
                pretty_print=pretty
            )

        s = unicode(sio.getvalue()).strip()

        if encoding:
            return s.encode(encoding)

        return s

    def to_json(self):
        """Export an object as a JSON String."""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_doc):
        """Parse a JSON string and build an entity."""
        try:
            d = json.load(json_doc)
        except AttributeError: # catch the read() error
            d = json.loads(json_doc)

        return cls.from_dict(d)

    def _get_namespace_def(self, additional_ns_dict=None):
        # copy necessary namespaces

        namespaces = self._get_namespaces()

        if additional_ns_dict:
            for ns, prefix in additional_ns_dict.iteritems():
                namespaces.update([Namespace(ns, prefix)])

        # TODO: For now, always add the ID namespace. Later we can figure out
        # how to intelligently do it only when necessary
        namespaces.update([cybox.utils.idgen._get_generator().namespace])

        # if there are any other namepaces, include xsi for "schemaLocation"
        if namespaces:
            namespaces.update([META.lookup_prefix('xsi')])

        if not namespaces:
            return ""

        namespaces = sorted(namespaces, key=str)

        return ('\n\t' + get_xmlns_string(namespaces) +
                '\n\txsi:schemaLocation="' + get_schemaloc_string(namespaces) +
                '"')

    def _get_namespaces(self, recurse=True):
        nsset = set()

        # Get all _namespaces for parent classes
        namespaces = [x._namespace for x in self.__class__.__mro__
                      if hasattr(x, '_namespace')]

        nsset.update([META.lookup_namespace(ns) for ns in namespaces])

        #In case of recursive relationships, don't process this item twice
        self.touched = True
        if recurse:
            for x in self._get_children():
                if not hasattr(x, 'touched'):
                    nsset.update(x._get_namespaces())
        del self.touched

        return nsset

    def _get_children(self):
        #TODO: eventually everything should be in _fields, not the top level
        # of vars()
        for k, v in vars(self).items() + self._fields.items():
            if isinstance(v, Entity):
                yield v
            elif isinstance(v, list):
                for item in v:
                    if isinstance(item, Entity):
                        yield item

    @classmethod
    def istypeof(cls, obj):
        """Check if `cls` is the type of `obj`

        In the normal case, as implemented here, a simple isinstance check is
        used. However, there are more complex checks possible. For instance,
        EmailAddress.istypeof(obj) checks if obj is an Address object with
        a category of Address.CAT_EMAIL
        """
        return isinstance(obj, cls)

    @classmethod
    def object_from_dict(cls, entity_dict):
        """Convert from dict representation to object representation."""
        return cls.from_dict(entity_dict).to_obj()

    @classmethod
    def dict_from_object(cls, entity_obj):
        """Convert from object representation to dict representation."""
        return cls.from_obj(entity_obj).to_dict()


class Unicode(Entity):
    """Shim class to allow xs:string's in EntityList"""

    def __init__(self, value):
        super(Unicode, self).__init__()
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = unicode(value)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)
        return self.value

    def to_dict(self):
        return self.value

    @staticmethod
    def from_obj(cls_obj):
        return Unicode(cls_obj)

    from_dict = from_obj


class EntityList(collections.MutableSequence, Entity):
    _contained_type = object

    # Don't try to cast list types (yet)
    _try_cast = False

    def __init__(self, *args):
        super(EntityList, self).__init__()
        self._inner = []

        for arg in args:
            if isinstance(arg, list):
                self.extend(arg)
            else:
                self.append(arg)

    def __getitem__(self, key):
        return self._inner.__getitem__(key)

    def __setitem__(self, key, value):
        if not self._is_valid(value):
            value = self._fix_value(value)
        self._inner.__setitem__(key, value)

    def __delitem__(self, key):
        self._inner.__delitem__(key)

    def __len__(self):
        return len(self._inner)

    def insert(self, idx, value):
        if not self._is_valid(value):
            value = self._fix_value(value)
        self._inner.insert(idx, value)

    def _is_valid(self, value):
        """Check if this is a valid object to add to the list.

        Subclasses can override this function, but it's probably better to
        modify the istypeof function on the _contained_type.
        """
        return self._contained_type.istypeof(value)

    def _fix_value(self, value):
        """Attempt to coerce value into the correct type.

        Subclasses can override this function.
        """
        try:
            new_value = self._contained_type(value)
        except:
            raise ValueError("Can't put '%s' (%s) into a %s" %
                (value, type(value), self.__class__))
        return new_value

    # The next four functions can be overridden, but otherwise define the
    # default behavior for EntityList subclasses which define the following
    # class-level members:
    # - _binding_class
    # - _binding_var
    # - _contained_type

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        tmp_list = [x.to_obj(return_obj=return_obj, ns_info=ns_info) for x in self]

        list_obj = self._binding_class()

        setattr(list_obj, self._binding_var, tmp_list)

        return list_obj

    def to_list(self):
        return [h.to_dict() for h in self]

    # Alias the `to_list` function as `to_dict`
    to_dict = to_list

    @classmethod
    def from_obj(cls, list_obj):
        if not list_obj:
            return None

        list_ = cls()

        for item in getattr(list_obj, cls._binding_var):
            list_.append(cls._contained_type.from_obj(item))

        return list_

    @classmethod
    def from_list(cls, list_list):
        if not isinstance(list_list, list):
            return None

        list_ = cls()

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
        super(ObjectReference, self).__init__()
        self.object_reference = object_reference

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        obj = self._binding_class()
        obj.object_reference = self.object_reference

        return obj

    def to_dict(self):
        return {'object_reference': self.object_reference}

    @classmethod
    def from_obj(cls, ref_obj):
        if not ref_obj:
            return None

        ref = cls()
        ref.object_reference = ref_obj.object_reference

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

    def __init__(self, name, type_=None, callback_hook=None, key_name=None,
                 comparable=True, multiple=False):
        """
        Create a new field.

        - `name` is the name of the field in the Binding class
        - `type_` is the type that objects assigned to this field must be.
          If `None`, no type checking is performed.
        - `key_name` is only needed if the desired key for the dictionary
          representation is differen than the lower-case version of `name`
        - `comparable` (boolean) - whether this field should be considered
          when checking Entities for equality. Default is True. If false, this
          field is not considered
        - `multiple` (boolean) - Whether multiple instances of this field can
          exist on the Entity.
        """
        self.name = name
        self.type_ = type_
        self.callback_hook = callback_hook
        self._key_name = key_name
        self.comparable = comparable
        self.multiple = multiple

    def __get__(self, instance, owner):
        # If we are calling this on a class, we want the actual Field, not its
        # value
        if not instance:
            return self

        return instance._fields.get(self.name, [] if self.multiple else None)

    def __set__(self, instance, value):
        if ((value is not None) and (self.type_ is not None) and
                (not self.type_.istypeof(value))):
            if self.multiple and isinstance(value, list):
                # TODO: if a list, check if each item in the list is the
                # correct type.
                pass
            elif self.type_._try_cast:
                value = self.type_(value)
            else:
                raise ValueError("%s must be a %s, not a %s" %
                                    (self.name, self.type_, type(value)))
        instance._fields[self.name] = value

        if self.callback_hook:
            self.callback_hook(instance)

    def __str__(self):
        return self.attr_name

    @property
    def key_name(self):
        if self._key_name:
            return self._key_name
        else:
            return self.name.lower()

    @property
    def attr_name(self):
        """The name of this field as an attribute name.

        This is identical to the key_name, unless the key name conflicts with
        a builtin Python keyword, in which case a single underscore is
        appended.

        This should match the name given to the TypedField class variable (see
        examples below), but this is not enforced.

        Examples:
            data = cybox.TypedField("Data", String)
            from_ = cybox.TypedField("From", String)
        """

        attr = self.key_name
        # TODO: expand list with other Python keywords
        if attr in ('from', 'class', 'type', 'with', 'for', 'id', 'type',
                'range'):
            attr = attr + "_"
        return attr
