# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox import entities
from mixbox import fields

from cybox.objects.address_object import Address


class DummyEntity(entities.Entity):

    var1 = fields.TypedField("Var1")
    var2 = fields.TypedField("Var2", comparable=False)


class ComparatorTest(unittest.TestCase):

    def setUp(self):
        self.a1 = Address("someone@example.org")
        self.a2 = Address("someone@example.org")
        self.a3 = self.a1
        self.a4 = Address("someone_else@example.org")

    def test_equal(self):
        # Equal but not the same object
        self.assertEqual(self.a1, self.a2)
        self.assertTrue(self.a1 is not self.a2)

    def test_same(self):
        # The same object, by two different names, should compare as equal.
        self.assertEqual(self.a1, self.a3)
        self.assertTrue(self.a1 is self.a3)

    def test_not_equal(self):
        self.assertNotEqual(self.a1, self.a4)

    def test_other_properties(self):
        # We can set other properties (besides TypedFields) and they still
        # compare equal.
        self.a1.blah = True
        self.a2.blah = False
        self.assertEqual(self.a1, self.a2)

        # But if we set one of the TypedFields, they are no longer equal.
        self.a1.is_source = True
        self.assertNotEqual(self.a1, self.a2)

        self.a2.is_source = True
        self.assertEqual(self.a1, self.a2)

    def test_non_comparable_fields(self):
        ent1 = DummyEntity()
        ent2 = DummyEntity()

        ent1.var1 = "blah"
        ent2.var1 = "blah"

        # var2 is not comparable, so this should not affect the equality check.
        ent1.var2 = "blah2"
        ent2.var2 = "blah3"
        self.assertEqual(ent1, ent2)


if __name__ == "__main__":
    unittest.main()
