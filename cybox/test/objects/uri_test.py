import unittest

from cybox.common import AnyURI
from cybox.objects.uri_object import URI
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestURI(unittest.TestCase, ObjectTestCase):
    object_type = "URIObjectType"
    klass = URI

    def test_round_trip(self):
        v = AnyURI("http://www.example.com")
        t = URI.TYPE_URL

        u = URI()
        u.value = v
        u.type_ = t

        uri2 = round_trip(u, URI, output=False)

        self.assertEqual(uri2.value, v)
        self.assertEqual(uri2.type_, t)

if __name__ == "__main__":
    unittest.main()
