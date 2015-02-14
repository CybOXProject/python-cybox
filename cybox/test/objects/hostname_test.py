# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.hostname_object import Hostname
from cybox.test.objects import ObjectTestCase


class TestHostname(ObjectTestCase, unittest.TestCase):
    object_type = "HostnameObjectType"
    klass = Hostname

    _full_dict = {
        'is_domain_name': True,
        'hostname_value': "www.example.com",
        'naming_system': ["DNS", "NETBIOS"],
        'xsi:type': object_type,
    }

    def test_missing_naming_system(self):
        hn = Hostname.from_dict({'hostname_value': "www.example2.com"})
        self.assertTrue(b"www.example2.com" in hn.to_xml())

if __name__ == "__main__":
    unittest.main()
