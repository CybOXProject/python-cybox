# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.arp_cache_object import ARPCache

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestARPCache(ObjectTestCase, unittest.TestCase):
    object_type = "ARPCacheObjectType"
    klass = ARPCache

    _full_dict = {
        'arp_cache_entry': [
            {
                'ip_address': {
                    'address_value': u"100.200.100.1",
                    'xsi:type': 'AddressObjectType'
                }, 
                'physical_address': u"100.200.100.1",
                'type': u"Test",
                'network_interface': {
                    'adapter': u'eth0',
                    'description': u'a test'
                }
            },
            {
                'ip_address': {
                    'address_value': u"100.200.100.2",
                    'xsi:type': 'AddressObjectType'
                }, 
                'physical_address': u"100.200.100.2",
                'type': u"Test 2",
                'network_interface': {
                    'adapter': u'eth2',
                    'description': u'a test 2'
                }
            }
        ],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
