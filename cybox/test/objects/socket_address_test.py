# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.address_object import Address
from cybox.objects.socket_address_object import SocketAddress
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestSocketAddress(ObjectTestCase, unittest.TestCase):
    object_type = "SocketAddressObjectType"
    klass = SocketAddress

    _full_dict = {
        'ip_address': {
            'category': Address.CAT_IPV4,
            'address_value': "192.168.1.1",
            'xsi:type': "AddressObjectType"
        },
        'port': {
            'port_value': 80,
            'layer4_protocol': "TCP",
            'xsi:type': "PortObjectType"
        },
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
