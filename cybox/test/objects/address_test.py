# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import String
from cybox.objects.address_object import Address, EmailAddress
import cybox.test


class TestAddress(unittest.TestCase, cybox.test.objects.ObjectTestCase):
    object_type = "AddressObjectType"
    klass = Address

    def test_round_trip(self):
        email = "test@example.com"
        v = String(email)
        c = Address.CAT_EMAIL

        a = Address()
        a.address_value = v
        a.category = c

        addr2 = cybox.test.round_trip(a)

        #TODO: Make this really pass
        self.assertEqual(addr2.address_value.value, v.value)
        self.assertEqual(addr2.category, c)

        self.assertEqual(email, str(addr2))

    def test_round_trip_dict(self):
        addr_dict = {'address_value': "1.2.3.4",
                     'category': Address.CAT_IPV4,
                     'is_destination': True,
                     'is_source': False}

        addr_dict2 = cybox.test.round_trip_dict(Address, addr_dict)

        cybox.test.assert_equal_ignore(addr_dict, addr_dict2, ['xsi:type'])
        self.assertNotEqual(addr_dict, addr_dict2)


class TestEmailAddress(unittest.TestCase):

    def test_create_email_address(self):
        a = "test@example.com"

        addr = EmailAddress(a)
        self.assertTrue(isinstance(addr, EmailAddress))
        self.assertTrue(isinstance(addr, Address))

        addr_dict = {'address_value': a, 'category': Address.CAT_EMAIL}

        cybox.test.assert_equal_ignore(addr.to_dict(), addr_dict, ['xsi:type'])
        self.assertNotEqual(addr.to_dict(), addr_dict)


if __name__ == "__main__":
    unittest.main()
