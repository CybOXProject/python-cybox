# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import ObjectProperties
from cybox.objects.address_object import Address
import cybox.test


class TestObjectProperties(unittest.TestCase):

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

    def test_object_reference(self):
        d = {
            'object_reference': "cybox:address-1",
            'category': Address.CAT_IPV4,
            'xsi:type': Address._XSI_TYPE,
        }
        d2 = cybox.test.round_trip_dict(Address, d)
        self.assertEqual(d, d2)


if __name__ == "__main__":
    unittest.main()
