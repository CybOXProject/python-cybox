# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.network_route_object import NetRoute

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestNetworkRoute(ObjectTestCase, unittest.TestCase):
    object_type = "NetRouteObjectType"
    klass = NetRoute

    _full_dict = {
        'is_ipv6': False,
        'is_autoconfigure_address': True,
        'is_immortal': False,
        'is_loopback': False,
        'is_publish': True,
        'description': "A description",
        'preferred_lifetime': u("P10D"),
        'valid_lifetime': u("P5D"),
        'route_age': u("P1D"),
        #'network_route_entries': [],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
