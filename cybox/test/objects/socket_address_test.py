# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.address_object import Address
from cybox.objects.socket_address_object import SocketAddress
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestSocketAddress(unittest.TestCase, ObjectTestCase):
    object_type = "SocketAddressObjectType"
    klass = SocketAddress

    def test_round_trip(self):
        socket_dict = {'ip_address': {'category': Address.CAT_IPV4,
                                      'address_value': "192.168.1.1",
                                      'xsi:type': "AddressObjectType"},
                       'port': {'port_value': 80,
                                'layer4_protocol': "TCP",
                                'xsi:type': "PortObjectType"},
                       'xsi:type': 'SocketAddressObjectType'
                      }
        socket_dict2 = cybox.test.round_trip_dict(SocketAddress, socket_dict)
        self.maxDiff = None
        self.assertEqual(socket_dict, socket_dict2)


if __name__ == "__main__":
    unittest.main()
