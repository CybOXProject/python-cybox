# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_network_route_entry_object import UnixNetworkRouteEntry
from cybox.test.objects import ObjectTestCase


class TestUnixNetworkRouteEntry(ObjectTestCase, unittest.TestCase):
    object_type = "UnixNetworkRouteEntryObjectType"
    klass = UnixNetworkRouteEntry

    _full_dict = {
        'flags': u('UG'),
        'mss': 0,
        'ref': 345,
        'use': 1642,
        'window': 518,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
