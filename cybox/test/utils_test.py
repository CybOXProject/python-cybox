import unittest

import cybox.utils

class IDGeneratorTest(unittest.TestCase):
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
        with self.assertRaises(cybox.utils.InvalidMethodError):
            self.generator.method = "invalid method"


if __name__ == "__main__":
    unittest.main()
