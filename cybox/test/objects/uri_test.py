# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import AnyURI
from cybox.objects.uri_object import URI
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestURI(unittest.TestCase, ObjectTestCase):
    object_type = "URIObjectType"
    klass = URI

    def test_round_trip(self):
        v = AnyURI("http://www.example.com")
        t = URI.TYPE_URL

        u = URI(v, t)
        uri2 = cybox.test.round_trip(u)

        #TODO: Make this really pass
        self.assertEqual(uri2.value.value, v.value)
        self.assertEqual(uri2.type_, t)

    def test_round_trip_dict(self):
        uri_dict = {'value': "http://www.example.com",
                    'type': URI.TYPE_URL,
                    'xsi:type': URI._XSI_TYPE}
        uri_dict2 = cybox.test.round_trip_dict(URI, uri_dict)
        self.assertEqual(uri_dict, uri_dict2)

    def test_no_type(self):
        uri_dict = {'value': "http://www.example.com",
                    'xsi:type': URI._XSI_TYPE}
        uri_obj = URI.object_from_dict(uri_dict)
        uri_dict2 = URI.dict_from_object(uri_obj)
        self.assertEqual(uri_dict, uri_dict2)

    def test_round_trip_without_xsi_type(self):
        uri_dict = {'value': "http://www.example.com",
                    'type': URI.TYPE_URL}
        uri_dict2 = cybox.test.round_trip_dict(URI, uri_dict)
        cybox.test.assert_equal_ignore(uri_dict, uri_dict2, ['xsi:type'])

    def test4(self):
        uri_dict = {'value': "http://www.example.com"}
        uri_dict2 = cybox.test.round_trip_dict(URI, uri_dict)
        cybox.test.assert_equal_ignore(uri_dict, uri_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
