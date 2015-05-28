# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.address_object import Address
from cybox.objects.socket_address_object import SocketAddress
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestSocketAddress(ObjectTestCase, unittest.TestCase):
    object_type = "SocketAddressObjectType"
    klass = SocketAddress

    _full_dict = {
        # Normally only one out of IP_Address and Hostname is allowed,
        # but we don't enforce that, so we can test both here.
        'ip_address': {
            'category': Address.CAT_IPV4,
            'address_value': u("192.168.1.1"),
            'xsi:type': "AddressObjectType"
        },
        'hostname': {
            'is_domain_name': True,
            'hostname_value': u("www.example.com"),
            'xsi:type': "HostnameObjectType"
        },
        'port': {
            'port_value': 80,
            'layer4_protocol': u("TCP"),
            'xsi:type': "PortObjectType"
        },
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
