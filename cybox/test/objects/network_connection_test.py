# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.address_object import Address
from cybox.objects.network_connection_object import (Layer7Connections,
        NetworkConnection)
from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestNetworkConnection(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkConnectionObjectType"
    klass = NetworkConnection

    _full_dict = {
        'tls_used': False,
        'creation_time': "2013-07-30T02:02:02+04:00",
        'layer3_protocol': u("IPV4"),
        'layer4_protocol': u("TCP"),
        'layer7_protocol': u("HTTP"),
        'source_socket_address': {
            'ip_address': {
                'category': Address.CAT_IPV4,
                'address_value': u("192.168.1.1"),
                'xsi:type': "AddressObjectType",
            },
            'port': {
                'port_value': 4567,
                'layer4_protocol': u("TCP"),
                'xsi:type': "PortObjectType",
            },
            'xsi:type': "SocketAddressObjectType",
        },
        'source_tcp_state': u("UNKNOWN"),
        'destination_socket_address': {
            'ip_address': {
                'category': Address.CAT_IPV4,
                'address_value': u("192.168.1.50"),
                'xsi:type': "AddressObjectType",
            },
            'port': {
                'port_value': 80,
                'layer4_protocol': u("TCP"),
                'xsi:type': "PortObjectType",
            },
            'xsi:type': "SocketAddressObjectType",
        },
        'destination_tcp_state': u("UNKNOWN"),
        'layer7_connections': {
            'http_session': {
                'object_reference': "example:ABC-1",
                'xsi:type': "HTTPSessionObjectType",
            }
        },
        'xsi:type': object_type,
    }

    # https://github.com/CybOXProject/python-cybox/issues/184
    def test_tcp_states(self):
        nc = NetworkConnection()
        nc.source_tcp_state = "LISTEN"
        nc.destination_tcp_state = "ESTABLISHED"

        nc2 = round_trip(nc)
        self.assertEqual(nc.to_dict(), nc2.to_dict())


class TestLayer7Connections(EntityTestCase, unittest.TestCase):
    klass = Layer7Connections

    _full_dict = {
        'http_session': {
            'object_reference': "example:ABC-1",
            'xsi:type': "HTTPSessionObjectType",
        },
        'dns_query': [
            {
                'question': {
                    'qname': {
                        'value': u("www.example.com"),
                        'xsi:type': "URIObjectType",
                    },
                    'qtype': u("A"),
                    'qclass': u("IN"),
                },
                'successful': True,
                'xsi:type': "DNSQueryObjectType",
            },
            {
                'question': {
                    'qname': {
                        'value': u("www.example2.com"),
                        'xsi:type': "URIObjectType",
                    },
                    'qtype': u("CNAME"),
                },
                'successful': False,
                'xsi:type': "DNSQueryObjectType",
            },
        ]
    }


if __name__ == "__main__":
    unittest.main()
