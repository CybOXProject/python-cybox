# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects import _ObjectMetadata, UnknownObjectType


class ObjectTypeTest(unittest.TestCase):

    def setUp(self):
        obj_list = [
            ("!!MissingAPIClass", None, None, None, None),
            ("!!MissingModule", 'some.nonexistent.module', None, None, None),
            ("!!BadClassName", 'cybox.NonexistentClass', None, None, None),
        ]
        self.meta = _ObjectMetadata(obj_list)

    def test_unknown_object(self):
        self.assertRaises(UnknownObjectType,
                          self.meta.get_class_for_object_type,
                          "!!BadType")

    def test_missing_api_class(self):
        self.assertRaises(UnknownObjectType,
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


if __name__ == "__main__":
    unittest.main()
