# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.common import AnyURI
from cybox.objects.uri_object import URI
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestURI(ObjectTestCase, unittest.TestCase):
    object_type = "URIObjectType"
    klass = URI

    _full_dict = {
        'value': "http://www.example.com",
        'type': URI.TYPE_URL,
        'xsi:type': object_type,
    }

    def test_round_trip(self):
        uri_str = "http://www.example.com"
        t = URI.TYPE_URL

        uri = URI(AnyURI(uri_str), t)
        uri2 = cybox.test.round_trip(uri)

        self.assertEqual(uri.to_dict(), uri2.to_dict())

        self.assertEqual(uri_str, str(uri2))
        self.assertEqual(t, uri2.type_)

    def test_unicode(self):
        unicode_uri = u("www.\u0395\u03a7\u0391\u039c\u03a1LE.com")
        uri = URI(unicode_uri, URI.TYPE_DOMAIN)
        uri2 = cybox.test.round_trip(uri)
        self.assertEqual(uri.to_dict(), uri2.to_dict())

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
