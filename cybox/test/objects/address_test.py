import unittest

from cybox.objects.address_object import Address
from cybox.test.objects import round_trip, ObjectTestCase


class TestAddress(unittest.TestCase, ObjectTestCase):
    object_type = "AddressObjectType"
    klass = Address

    def test_round_trip(self):
        v = "test@example.com"
        c = Address.CAT_EMAIL

        a = Address()
        a.address_value = v
        a.category = c

        addr2 = round_trip(a, Address, output=False)

        self.assertEqual(addr2.address_value, v)
        self.assertEqual(addr2.category, c)

if __name__ == "__main__":
    unittest.main()
