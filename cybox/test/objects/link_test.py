# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.link_object import Link
from cybox.objects.uri_object import URI
from cybox.test.objects import ObjectTestCase


class TestLink(ObjectTestCase, unittest.TestCase):
    object_type = "LinkObjectType"
    klass = Link

    _full_dict = {
        'value': u("http://www.example.com"),
        'type': URI.TYPE_URL,
        'url_label': u("Click Here!"),
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
