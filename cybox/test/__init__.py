# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import json
import logging
import unittest
import collections

from mixbox.binding_utils import ExternalEncoding
from mixbox.entities import Entity
from mixbox.vendor import six

import cybox.utils

logger = logging.getLogger(__name__)


def assert_equal_ignore(item1, item2, ignore_keys=None):
    """Recursively compare two dictionaries, ignoring differences in some keys.
    """
    if not ignore_keys:
        ignore_keys = []

    if isinstance(item1, dict) and isinstance(item2, dict):
        item1keys = set(item1.keys())
        item2keys = set(item2.keys())
        ignore = set(ignore_keys)
        compare_keys = (item1keys | item2keys) - ignore
        for k in compare_keys:
            assert k in item1, "Item 1 is missing %s" % k
            assert k in item2, "Item 2 is missing %s" % k
            assert_equal_ignore(item1.get(k), item2.get(k), ignore_keys)
    elif isinstance(item1, list) and isinstance(item2, list):
        assert len(item1) == len(item2), "Lists are of different lengths"
        for (x, y) in zip(item1, item2):
            assert_equal_ignore(x, y, ignore_keys)
    else:
        assert item1 == item2, "%s != %s" % (item1, item2)


def assert_entity_equals(entity, other, name=None, stack=None):
    """Assert all of the TypedFields in two Entities are equal."""
    # Shorten the lines.
    is_entity      = lambda x: isinstance(x, Entity)
    is_mutableseq  = lambda x: isinstance(x, collections.MutableSequence)

    if stack is None:
        stack = []

    if name is not None:
        stack.append(name)

    if is_entity(entity) and is_entity(other):
        for name, var in entity.typed_fields_with_attrnames():
            assert_entity_equals(
                var.__get__(entity),
                var.__get__(other),
                name=name,
                stack=stack
            )
    elif is_mutableseq(entity) and is_mutableseq(other):
        # "multiple" TypedFields store their contents in mutable sequences.
        assert len(entity) == len(other)
        for x, y in zip(entity, other):
            assert_entity_equals(x, y, None, stack=stack)
    else:
        assert entity == other, "(%s) %r != %r stack=%s" % (name, entity, other, stack)

    if name is not None and stack:
        stack.pop()

def round_trip(o, output=False, list_=False):
    """ Performs all eight conversions to verify import/export functionality.

    1. cybox.Entity -> dict/list
    2. dict/list -> JSON string
    3. JSON string -> dict/list
    4. dict/list -> cybox.Entity
    5. cybox.Entity -> Bindings Object
    6. Bindings Object -> XML String
    7. XML String -> Bindings Object
    8. Bindings object -> cybox.Entity

    It returns the final object, so tests which call this function can check to
    ensure it was not modified during any of the transforms.
    """

    klass = o.__class__
    if output:
        logger.debug("Class: {0}".format(klass))
        logger.debug("-" * 40)

    # 1. cybox.Entity -> dict/list
    if list_:
        d = o.to_list()
    else:
        d = o.to_dict()

    # 2. dict/list -> JSON string
    json_string = json.dumps(d)

    if output:
        logger.debug(json_string)
        logger.debug("-" * 40)

    # Before parsing the JSON, make sure the cache is clear
    cybox.utils.cache_clear()

    # 3. JSON string -> dict/list
    d2 = json.loads(json_string)

    # 4. dict/list -> cybox.Entity
    if list_:
        o2 = klass.from_list(d2)
    else:
        o2 = klass.from_dict(d2)

    # 5. cybox.Entity -> Bindings Object
    xobj = o2.to_obj()

    # 6. Bindings Object -> XML String
    xml_string = o2.to_xml(encoding=ExternalEncoding)

    # Explicitly check to see if it's a Unicode string before trying to decode
    # it.
    if not isinstance(xml_string, six.text_type):
        xml_string = xml_string.decode(ExternalEncoding)

    if output:
        logger.debug(xml_string)
        logger.debug("-" * 40)

    # Before parsing the XML, make sure the cache is clear
    cybox.utils.cache_clear()

    #7. XML String -> Bindings Object
    xobj2 = klass._binding.parseString(xml_string)

    # 8. Bindings object -> cybox.Entity
    o3 = klass.from_obj(xobj2)

    return o3


def round_trip_dict(cls, dict_):
    obj = cls.object_from_dict(dict_)
    dict2 = cls.dict_from_object(obj)

    return dict2


def round_trip_list(cls, list_):
    obj = cls.object_from_list(list_)
    list2 = cls.list_from_object(obj)

    return list2


class EntityTestCase(object):
    """A mixin class for testing CybOX Entities"""

    def setUp(self):
        self.assertNotEqual(self.klass, None)
        self.assertNotEqual(self._full_dict, None)

    def test_round_trip_dict(self):
        # Round_trip_dict doesn't start or end with Python objects (obviously),
        # so this is a less than ideal test.
        dict2 = round_trip_dict(self.klass, self._full_dict)
        self.maxDiff = None
        self.assertEqual(self._full_dict, dict2)

    def test_round_trip(self):
        # This is a better test, even though we start from a dictionary, and
        # can only compare the dict representations right now.
        ent = self.klass.from_dict(self._full_dict)
        ent2 = round_trip(ent, output=True)
        self.maxDiff = None
        # For now, the only way to compare two entity representations is to
        # compare the dictionary output to the original dictionary.
        self.assertEqual(self._full_dict, ent2.to_dict())

    def test_round_trip_entity(self):
        # This is a better test, even though we start from a dictionary, and
        # can only compare the dict representations right now.
        ent = self.klass.from_dict(self._full_dict)
        ent2 = round_trip(ent, output=True)
        assert_entity_equals(ent, ent2)

    # TODO: Assert to_xml() on two round-tripped entities are identical.


if __name__ == "__main__":
    unittest.main()
