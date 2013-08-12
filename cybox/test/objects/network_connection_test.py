# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.address_object import Address
from cybox.objects.network_connection_object import (Layer7Connections,
        NetworkConnection)
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestNetworkConnection(unittest.TestCase, ObjectTestCase):
    object_type = "NetworkConnectionObjectType"
    klass = NetworkConnection

    def test_round_trip(self):
        conn_dict = {
                        'tls_used': False,
                        'creation_time': "2013-07-30T02:02:02+04:00",
                        'layer3_protocol': "IPV4",
                        'layer4_protocol': "TCP",
                        'layer7_protocol': "HTTP",
                        'source_socket_address': {
                            'ip_address': {
                                'category': Address.CAT_IPV4,
                                'address_value': "192.168.1.1"
                            },
                            'port': {
                                'port_value': 4567,
                                'layer4_protocol': "TCP"
                            },
                        },
                        'source_tcp_state': "UNKNOWN",
                        'destination_socket_address': {
                            'ip_address': {
                                'category': Address.CAT_IPV4,
                                'address_value': "192.168.1.50"
                            },
                            'port': {
                                'port_value': 80,
                                'layer4_protocol': "TCP"
                            },
                        },
                        'destination_tcp_state': "UNKNOWN",
                        'layer7_connections': {
                            'http_session': {
                                'object_reference': "example:ABC-1",
                            }
                        }
        }
        conn_dict2 = cybox.test.round_trip_dict(NetworkConnection, conn_dict)
        cybox.test.assert_equal_ignore(conn_dict, conn_dict2, ['xsi:type'])


class TestLayer7Connections(unittest.TestCase):

    def test_round_trip(self):
        conns_dict = {
                        'http_session': {
                            'object_reference': "example:ABC-1",
                        },
                        'dns_query': [
                            {
                                'question': {
                                    'qname': {'value': u"www.example.com"},
                                    'qtype': u"A",
                                    'qclass': u"IN",
                                },
                                'successful': True
                            },
                            {
                                'question': {
                                    'qname': {'value': u"www.example2.com"},
                                    'qtype': u"CNAME",
                                },
                                'successful': False
                            },
                        ]
        }
        conns_dict2 = cybox.test.round_trip_dict(Layer7Connections, conns_dict)
        self.maxDiff = None
        cybox.test.assert_equal_ignore(conns_dict, conns_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
