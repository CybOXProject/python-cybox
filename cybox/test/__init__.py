# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import json
import unittest

import cybox.bindings as bindings
from cybox import Entity, EntityList, TypedField
import cybox.bindings.cybox_core as core_binding
from cybox.core import Observables
import cybox.utils


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
        print "Class: ", klass
        print "-" * 40

    # 1. cybox.Entity -> dict/list
    if list_:
        d = o.to_list()
    else:
        d = o.to_dict()

    # 2. dict/list -> JSON string
    json_string = json.dumps(d)

    if output:
        print(json_string)
        print "-" * 40

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
    xml_string = o2.to_xml(encoding=bindings.ExternalEncoding)

    if not isinstance(xml_string, unicode):
        xml_string = xml_string.decode(bindings.ExternalEncoding)

    if output:
        print(xml_string)
        print "-" * 40

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
    """A base class for testing CybOX Entities"""

    def setUp(self):
        self.assertNotEqual(self.klass, None)
        self.assertNotEqual(self._full_dict, None)

    def test_round_trip_dict(self):
        # Don't run this test on the base class
        if type(self) == type(EntityTestCase):
            return

        dict2 = round_trip_dict(self.klass, self._full_dict)
        self.maxDiff = None
        self.assertEqual(self._full_dict, dict2)

    def test_round_trip(self):
        # Don't run this test on the base class
        if type(self) == type(EntityTestCase):
            return

        ent = self.klass.from_dict(self._full_dict)
        ent2 = round_trip(ent, output=True)

        #TODO: eventually we want to test the objects are the same, but for
        # now, just make sure there aren't any errors.


class TestTypedField(unittest.TestCase):

    def test_names(self):
        # The actual type is not important for this test
        a = TypedField("Some_Field", None)
        self.assertEqual("Some_Field", a.name)
        self.assertEqual("some_field", a.key_name)
        self.assertEqual("some_field", a.attr_name)

        a = TypedField("From", None)
        self.assertEqual("From", a.name)
        self.assertEqual("from", a.key_name)
        self.assertEqual("from_", a.attr_name)


class TestEntityList(unittest.TestCase):

    def test_remove(self):

        class Foo(Entity):
            name = TypedField("Name", None)

            def __init__(self, name):
                super(Foo, self).__init__()
                self.name = name

            def __str__(self):
                return self.name

        class FooList(EntityList):
            _contained_type = Foo

        foo1 = Foo("Alpha")
        foo2 = Foo("Beta")
        foo3 = Foo("Gamma")

        foolist = FooList(foo1, foo2, foo3)

        self.assertEqual(3, len(foolist))

        for f in list(foolist):
            self.assertTrue(f in foolist)
            if f.name == "Beta":
                foolist.remove(f)
                self.assertEqual(f, Foo("Beta"))
                self.assertFalse(f is Foo("Beta"))

        self.assertEqual(2, len(foolist))


if __name__ == "__main__":
    unittest.main()
