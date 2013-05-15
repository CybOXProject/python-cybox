# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

import cybox.utils


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
        ns = "NAMESPACE"
        self.generator.namespace = ns
        self.assertEqual(self.generator.create_id(), ns + ":guid-1")

    def test_prefix(self):
        prefix = "some_object"
        id_ = self.generator.create_id(prefix)
        self.assertEqual(id_, "example:" + prefix + "-1")

    def test_invalid_method(self):
        self.assertRaises(cybox.utils.InvalidMethodError,
                          cybox.utils.IDGenerator,
                          "cybox",
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
        ns = "NAMESPACE"
        cybox.utils.set_id_namespace(ns)
        self.assertEqual(cybox.utils.create_id(), ns + ":guid-1")

    def test_prefix(self):
        prefix = "some_object"
        id_ = cybox.utils.create_id(prefix)
        # The namespace may be different, but the prefix and ID should be the
        # same.
        self.assertEqual(id_.split(":")[1],  prefix + "-1")


class ObjectTypeTest(unittest.TestCase):

    def test_unknown_object(self):
        self.assertRaises(cybox.utils.UnknownObjectTypeError,
                          cybox.utils.get_class_for_object_type,
                          "!!BadType")

    def test_missing_api_class(self):
        self.assertRaises(cybox.utils.UnknownObjectTypeError,
                          cybox.utils.get_class_for_object_type,
                          "!!MissingAPIClass")

    def test_missing_module(self):
        self.assertRaises(ImportError,
                          cybox.utils.get_class_for_object_type,
                          "!!MissingModule")

    def test_missing_class(self):
        self.assertRaises(AttributeError,
                          cybox.utils.get_class_for_object_type,
                          "!!BadClassName")


class NormalizationTest(unittest.TestCase):

    def test_encode_decode_lists(self):
        a = "A long, long, time ago"
        b = "A long&comma; long&comma; time ago"
        c = ["A long", "long", "time ago"]
        d = "A long,long,time ago"

        self.assertEqual(cybox.utils.normalize_to_xml(a), b)
        self.assertEqual(cybox.utils.normalize_to_xml(c), d)
        self.assertEqual(cybox.utils.denormalize_from_xml(a), c)
        self.assertEqual(cybox.utils.denormalize_from_xml(b), a)


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
