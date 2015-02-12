# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.network_route_entry_object import NetworkRouteEntry

from cybox.test import EntityTestCase, round_trip
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
            'address_value': u"1.2.3.4", 
            'xsi:type': 'AddressObjectType'
        },
        'origin': {
            'address_value': u"1.2.3.4", 
            'xsi:type': 'AddressObjectType'
        },
        'netmask': {
            'address_value': u"1.2.3.4", 
            'xsi:type': 'AddressObjectType'
        },
        'gateway_address': {
            'address_value': u"1.2.3.4", 
            'xsi:type': 'AddressObjectType'
        },
        'metric': 1234L,
        'type': u"A type",
        'protocol': u"A protocol",
        'interface': u"An interface",
        #'preferred_lifetime' = cybox.TypedField("Preferred_Lifetime", Duration)
        #'valid_lifetime' = cybox.TypedField("Valid_Lifetime", Duration)
        #'route_age' = cybox.TypedField("Route_Age", Duration)
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
