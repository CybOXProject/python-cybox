# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_network_route_entry_object import WinNetworkRouteEntry

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinNetworkRouteEntry(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsNetworkRouteEntryObjectType"
    klass = WinNetworkRouteEntry

    _full_dict = {
        'nl_route_protocol': u("A protocol"),
        'nl_route_origin': u("An origin"),
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
