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

        u = URI(v, t)
        uri2 = round_trip(u, URI, output=False)

        self.assertEqual(uri2.value, v)
        self.assertEqual(uri2.type_, t)

    def test_round_trip2(self):
        uri_dict = {'value': "http://www.example.com",
                    'type': URI.TYPE_URL,
                    'xsi:type': URI._XSI_TYPE}
        uri_obj = URI.object_from_dict(uri_dict)
        uri_dict2 = URI.dict_from_object(uri_obj)
        self.assertEqual(uri_dict, uri_dict2)

    def test_no_type(self):
        uri_dict = {'value': "http://www.example.com",
                    'xsi:type': URI._XSI_TYPE}
        uri_obj = URI.object_from_dict(uri_dict)
        uri_dict2 = URI.dict_from_object(uri_obj)
        self.assertEqual(uri_dict, uri_dict2)


if __name__ == "__main__":
    unittest.main()
