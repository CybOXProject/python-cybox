# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import DEFAULT_DELIM as DELIM
import cybox.utils

TEST_NS = cybox.utils.Namespace("http://some.namespace.com", "NAMESPACE")


class IDGeneratorMinimalTest(unittest.TestCase):

    def test_id(self):
        # Make sure we can create an ID with a minimum of effort.

        # TODO: actually delete the module and reimport it to make sure there
        # is nothing left over from another test.
        self.assertNotEqual(cybox.utils.create_id(), "")


class IDGeneratorTest(unittest.TestCase):
    """Tests for the cybox.utils.IDGenerator class."""

    def setUp(self):
        method = cybox.utils.IDGenerator.METHOD_INT
        self.generator = cybox.utils.IDGenerator(method=method)

    def test_incrementing_ids(self):
        self.assertEqual(self.generator.create_id(), "example:guid-1")
        self.assertEqual(self.generator.create_id(), "example:guid-2")
        self.assertEqual(self.generator.create_id(), "example:guid-3")

    def test_namespace(self):
        self.generator.namespace = TEST_NS
        self.assertEqual(self.generator.create_id(),
                         TEST_NS.prefix + ":guid-1")

    def test_prefix(self):
        prefix = "some_object"
        id_ = self.generator.create_id(prefix)
        self.assertEqual(id_, "example:" + prefix + "-1")

    def test_invalid_method(self):
        self.assertRaises(cybox.utils.InvalidMethodError,
                          cybox.utils.IDGenerator,
                          TEST_NS,
                          "invalid method")


class IDGeneratorModuleTest(unittest.TestCase):
    """Tests for the cybox.utils module's IDGenerator"""

    def setUp(self):
        # Reset the generator's count before each test
        cybox.utils.set_id_method(cybox.utils.IDGenerator.METHOD_INT)
        gen = cybox.utils.idgen._get_generator()
        gen.next_int = 1

    def test_int_method(self):
        self.assertEqual(cybox.utils.create_id(), "example:guid-1")

    def test_namespace(self):
        cybox.utils.set_id_namespace(TEST_NS)
        self.assertEqual(cybox.utils.create_id(),
                         TEST_NS.prefix + ":guid-1")

    def test_prefix(self):
        prefix = "some_object"
        id_ = cybox.utils.create_id(prefix)
        # The namespace may be different, but the prefix and ID should be the
        # same.
        self.assertEqual(id_.split(":")[1],  prefix + "-1")


class ObjectTypeTest(unittest.TestCase):

    def setUp(self):
        obj_list = [
            ("!!MissingAPIClass", None, None, None, None),
            ("!!MissingModule", 'some.nonexistent.module', None, None, None),
            ("!!BadClassName", 'cybox.NonexistentClass', None, None, None),
        ]
        self.meta = cybox.utils.nsparser.Metadata([], obj_list)

    def test_unknown_object(self):
        self.assertRaises(cybox.utils.UnknownObjectType,
                          self.meta.get_class_for_object_type,
                          "!!BadType")

    def test_missing_api_class(self):
        self.assertRaises(cybox.utils.UnknownObjectType,
                          self.meta.get_class_for_object_type,
                          "!!MissingAPIClass")

    def test_missing_module(self):
        self.assertRaises(ImportError,
                          self.meta.get_class_for_object_type,
                          "!!MissingModule")

    def test_missing_class(self):
        self.assertRaises(AttributeError,
                          self.meta.get_class_for_object_type,
                          "!!BadClassName")


class NormalizationTest(unittest.TestCase):

    def test_encode_decode_lists(self):
        a = "A long##comma##long##comma##time ago"
        b = ["A long", "long", "time ago"]

        self.assertEqual(cybox.utils.denormalize_from_xml(a, DELIM), b)
        self.assertEqual(cybox.utils.normalize_to_xml(b, DELIM), a)

    def test_delimiter_not_allowed_in_value(self):
        string = "test string with a ##comma## in it"
        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          string, DELIM)

    def test_normalize_string_with_nondefault_delimiter(self):
        s = cybox.utils.normalize_to_xml([1, 2, 3], ",")
        self.assertEqual("1,2,3", s)

        s = cybox.utils.normalize_to_xml([1, 2, 3], "-")
        self.assertEqual("1-2-3", s)

        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          [1, 2, 3], "1")

        s = cybox.utils.normalize_to_xml(['a', 'b', 'c'], ",")
        self.assertEqual("a,b,c", s)

        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          ['a,b', 'b,c', 'c,d'], ",")


class TestDictCache(unittest.TestCase):

    def test_id_incrementing(self):
        d = cybox.utils.DictCache()
        self.assertEqual(0, d.put("a"))
        self.assertEqual(1, d.put("b"))
        self.assertEqual(3, d.put("c", 3))
        self.assertEqual(2, d.put("d"))
        self.assertEqual(4, d.put("e"))

    def test_id_incrementing(self):
        d = cybox.utils.DictCache()
        self.assertEqual(0, d.count())

        d.put("a")
        d.put("b")
        d.put("c")
        self.assertEqual(3, d.count())

        d.clear()
        self.assertEqual(0, d.count())

if __name__ == "__main__":
    unittest.main()
