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
        self.assertEqual(self.generator.create_id(), "cybox:guid-1")
        self.assertEqual(self.generator.create_id(), "cybox:guid-2")
        self.assertEqual(self.generator.create_id(), "cybox:guid-3")

    def test_namespace(self):
        ns = "NAMESPACE"
        self.generator.namespace = ns
        self.assertEqual(self.generator.create_id(), ns + ":guid-1")

    def test_prefix(self):
        prefix = "some_object"
        id_ = self.generator.create_id(prefix)
        self.assertEqual(id_, "cybox:" + prefix + "-1")

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
        self.assertEqual(cybox.utils.create_id(), "cybox:guid-1")

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

    def test_missing_module(self):
        self.assertRaises(ImportError,
                          cybox.utils.get_class_for_object_type,
                          "!!MissingModule")

    def test_missing_class(self):
        self.assertRaises(AttributeError,
                          cybox.utils.get_class_for_object_type,
                          "!!BadClassName")

if __name__ == "__main__":
    unittest.main()
