# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.address_object import Address
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
                    'address_value': u("100.200.100.1"),
                    'category': Address.CAT_IPV4,
                    'xsi:type': 'AddressObjectType'
                },
                'physical_address': u("100.200.100.1"),
                'physical_address': u("00:22:44:66:88:aa"),
                'type': u("Test"),
                'network_interface': {
                    'adapter': u('eth0'),
                    'description': u('a test')
                }
            },
            {
                'ip_address': {
                    'address_value': u("100.200.100.2"),
                    'category': Address.CAT_IPV4,
                    'xsi:type': 'AddressObjectType'
                },
                'physical_address': u("01:23:45:67:89:ab"),
                'type': u("Test 2"),
                'network_interface': {
                    'adapter': u('eth2'),
                    'description': u('a test 2')
                }
            }
        ],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
