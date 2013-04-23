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

        self.assertTrue(isinstance(ObjectProperties.from_dict(d), ObjectProperties))
        self.assertTrue(isinstance(ObjectProperties.from_dict(d), Address))

    def test_object_reference(self):
        d = {'object_reference': "cybox:address-1",
             'category': Address.CAT_IPV4}

        d2 = cybox.test.round_trip_dict(Address, d)
        print d2

        self.assertNotEqual(d, d2)
        cybox.test.assert_equal_ignore(d, d2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
