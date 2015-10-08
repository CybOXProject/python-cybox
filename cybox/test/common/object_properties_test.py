# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.common import ObjectProperties, Property
from cybox.common.object_properties import ObjectPropertiesFactory
from cybox.objects.address_object import Address
from cybox.test import EntityTestCase


class TestProperty(EntityTestCase, unittest.TestCase):
    klass = Property

    _full_dict = {
        'id': "example:Property-1",
        'name': "FilePurpose",
        'description': "The purpose of the file",
        'value': u("Certificate"),
    }


class TestObjectProperties(EntityTestCase, unittest.TestCase):
    klass = Address

    _full_dict = {
        'object_reference': "cybox:address-1",
        'category': Address.CAT_IPV4,
        'xsi:type': Address._XSI_TYPE,
    }

    def test_empty_dict(self):
        self.assertEqual(None, ObjectPropertiesFactory.from_dict({}))

    def test_no_xsi_type(self):
        # d does not have the required 'xsi:type' key.
        d = {'key': 'value'}

        self.assertRaises(ValueError, ObjectPropertiesFactory.from_dict, d)

    def test_detect_address(self):
        d = {'xsi:type': Address._XSI_TYPE}

        obj = ObjectPropertiesFactory.from_dict(d)

        self.assertTrue(isinstance(obj, ObjectProperties))
        self.assertTrue(isinstance(obj, Address))


if __name__ == "__main__":
    unittest.main()
