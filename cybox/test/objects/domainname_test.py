# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.domain_name_object import DomainName
from cybox.test.objects import ObjectTestCase


class TestDomainName(ObjectTestCase, unittest.TestCase):
    object_type = "DomainNameObjectType"
    klass = DomainName

    _full_dict = {
        'type': u("FQDN"),
        'value': "www.example.com",
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
