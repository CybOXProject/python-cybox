# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import ObjectProperties
from cybox.objects.address_object import Address
from cybox.test import EntityTestCase


class TestObjectProperties(EntityTestCase, unittest.TestCase):
    klass = Address

    _full_dict = {
        'object_reference': "cybox:address-1",
        'category': Address.CAT_IPV4,
        'xsi:type': Address._XSI_TYPE,
    }

    def test_empty_dict(self):
        self.assertEqual(None, ObjectProperties.from_dict({}))

    def test_no_xsi_type(self):
        # d does not have the required 'xsi:type' key.
        d = {'key': 'value'}

        self.assertRaises(ValueError, ObjectProperties.from_dict, d)

    def test_detect_address(self):
        d = {'xsi:type': Address._XSI_TYPE}

        obj = ObjectProperties.from_dict(d)

        self.assertTrue(isinstance(obj, ObjectProperties))
        self.assertTrue(isinstance(obj, Address))


if __name__ == "__main__":
    unittest.main()
