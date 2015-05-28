# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.common import String
from cybox.objects.address_object import Address, EmailAddress
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestAddress(ObjectTestCase, unittest.TestCase):
    object_type = "AddressObjectType"
    klass = Address

    _full_dict = {
        'address_value': u("1.2.3.4"),
        'category': Address.CAT_IPV4,
        'is_destination': True,
        'is_source': False,
        'is_spoofed' : True,
        'vlan_name': u("VLAN0"),
        'vlan_num': 0,
        'xsi:type': object_type,
    }

    def test_round_trip(self):
        email = "test@example.com"
        category = Address.CAT_EMAIL

        addr = Address()
        addr.address_value = email
        addr.category = category
        addr.is_spoofed = True

        addr2 = cybox.test.round_trip(addr)

        self.assertEqual(addr.to_dict(), addr2.to_dict())

        # Explicitly check these fields
        self.assertEqual(category, addr2.category)
        self.assertEqual(email, str(addr2))

    def test_unicode(self):
        a = u("\u00fc\u00f1\u00ed\u00e7ode@example.com")
        addr = Address(a, Address.CAT_EMAIL)
        addr2 = cybox.test.round_trip(addr)
        self.assertEqual(addr.to_dict(), addr2.to_dict())


class TestEmailAddress(unittest.TestCase):

    def test_create_email_address(self):
        a = "test@example.com"

        addr = EmailAddress(a)
        self.assertTrue(isinstance(addr, EmailAddress))
        self.assertTrue(isinstance(addr, Address))

        addr_dict = {'address_value': a, 'category': Address.CAT_EMAIL}

        cybox.test.assert_equal_ignore(addr.to_dict(), addr_dict, ['xsi:type'])
        self.assertNotEqual(addr.to_dict(), addr_dict)

    def test_istypeof(self):
        a = "test@example.com"

        addr1 = EmailAddress(a)
        self.assertTrue(Address.istypeof(addr1))
        self.assertTrue(EmailAddress.istypeof(addr1))

        # Address with no category set
        addr2 = Address(a)
        self.assertTrue(Address.istypeof(addr2))
        self.assertFalse(EmailAddress.istypeof(addr2))

        # Even though the isinstance check fails, the istypeof check should
        # succeed
        addr2.category = Address.CAT_EMAIL
        self.assertTrue(Address.istypeof(addr2))
        self.assertTrue(EmailAddress.istypeof(addr2))
        self.assertFalse(isinstance(addr2, EmailAddress))

        # Address with category set to something other than CAT_EMAIL
        addr2.category = Address.CAT_IPV4
        self.assertTrue(Address.istypeof(addr2))
        self.assertFalse(EmailAddress.istypeof(addr2))


if __name__ == "__main__":
    unittest.main()
