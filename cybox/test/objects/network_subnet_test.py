# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.network_subnet_object import NetworkSubnet

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestNetworkSubnet(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkSubnetObjectType"
    klass = NetworkSubnet

    _full_dict = {
        'name': "A test subnet",
        'description': "Test subnet",
        'number_of_ip_addresses': 2,
        #'routes': [],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
