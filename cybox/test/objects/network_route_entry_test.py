# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.address_object import Address
from cybox.objects.network_route_entry_object import NetworkRouteEntry
from cybox.test.objects import ObjectTestCase


class TestNetworkRouteEntry(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkRouteEntryObjectType"
    klass = NetworkRouteEntry

    _full_dict = {
        'is_ipv6': False,
        'is_autoconfigure_address': True,
        'is_immortal': False,
        'is_loopback': False,
        'is_publish': True,
        'destination_address': {
            'address_value': u("1.2.3.4"),
            'category': Address.CAT_IPV4,
            'xsi:type': 'AddressObjectType'
        },
        'origin': {
            'address_value': u("1.2.3.4"),
            'category': Address.CAT_IPV4,
            'xsi:type': 'AddressObjectType'
        },
        'netmask': {
            'address_value': u("1.2.3.4"),
            'category': Address.CAT_IPV4,
            'xsi:type': 'AddressObjectType'
        },
        'gateway_address': {
            'address_value': u("1.2.3.4"),
            'category': Address.CAT_IPV4,
            'xsi:type': 'AddressObjectType'
        },
        'metric': long(1234),
        'type': u("A type"),
        'protocol': u("A protocol"),
        'interface': u("An interface"),
        'preferred_lifetime': u("P7D"),
        'valid_lifetime': u("P2D"),
        'route_age': u("P3D"),
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
