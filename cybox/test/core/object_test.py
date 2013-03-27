import unittest

from cybox.core import Object, RelatedObject, Observables
from cybox.objects.address_object import Address
from cybox.objects.email_message_object import EmailMessage


class ObjectTest(unittest.TestCase):
    pass


class RelatedObjectTest(unittest.TestCase):

    def test_add_related_object(self):
        e = EmailMessage()

        a = Address("192.168.1.1", Address.CAT_IPV4)

        e.add_related(a, "Received_From")

        self.assertEqual(1, len(e.parent.related_objects))
        self.assertEqual(a, e.parent.related_objects[0].defined_object)

if __name__ == "__main__":
    unittest.main()
