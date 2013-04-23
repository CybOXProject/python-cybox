import unittest

from cybox.core import Object, RelatedObject
from cybox.objects.address_object import Address
from cybox.objects.email_message_object import EmailMessage
import cybox.test


class ObjectTest(unittest.TestCase):

    def test_id_autoset(self):
        o = Object()
        self.assertNotEqual(o.id_, None)

    def test_id_prefix(self):
        a = Address()
        o = Object(a)
        self.assertTrue("Address" in o.id_)

    def test_round_trip(self):
        o = Object()
        o.idref = "example:a1"
        o.properties = Address("1.2.3.4", Address.CAT_IPV4)
        o2 = cybox.test.round_trip(o)

        self.assertEqual(o.to_dict(), o2.to_dict())


class RelatedObjectTest(unittest.TestCase):

    def test_add_related_object(self):
        e = EmailMessage()

        a = Address("192.168.1.1", Address.CAT_IPV4)

        e.add_related(a, "Received_From")

        self.assertEqual(1, len(e.parent.related_objects))
        self.assertEqual(a, e.parent.related_objects[0].properties)

if __name__ == "__main__":
    unittest.main()
