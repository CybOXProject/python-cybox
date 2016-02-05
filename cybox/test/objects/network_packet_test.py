# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.bindings.cybox_core import parseString
from cybox.core import Observables
from cybox.objects.address_object import Address
from cybox.objects.network_packet_object import (ARP, EthernetInterface,
        ICMPv4Packet, ICMPv6Packet, IPv4Packet, IPv6Packet, NDP, NDPPrefixInfo,
        NDPLinkAddr, NetworkPacket, TCP, UDP)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestNetworkPacket(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkPacketObjectType"
    klass = NetworkPacket

    _full_dict = {
        'custom_properties': [
            {'name': "Prop1", 'description': "Property1", 'value': "Value1"},
            {'name': "Prop2", 'description': "Property2", 'value': "Value2"},
        ],
        'link_layer': {
            'physical_interface': {
                'ethernet': {'ethernet_header': {'checksum': "fa10"}},
            },
            'logical_protocols': {
                'arp_rarp': {'hardware_addr_type': "Ethernet(1)"},
                'ndp': {'icmpv6_header': {'checksum': "06BC"}},
            },
        },
        'internet_layer': {
            # These are tested thoroughly below
            'ipv4': {'ipv4_header': {'ip_version': "IPv4(4)"}},
            'icmpv4': {'icmpv4_header': {'type': "01"}},
            'ipv6': {'ipv6_header': {'ip_version': 'IPv6(6)'}},
            'icmpv6': {'icmpv6_header': {'type': "01"}},
        },
        'transport_layer': {
            'tcp': {'data': {'data_segment': "GET /index.html http/1.1"}},
            'udp': {'data': {'data_segment': "whois example.com"}},
        },
        'xsi:type': object_type,
    }

    # https://github.com/CybOXProject/python-cybox/issues/181
    def test_round_trip_xml(self):
        np = NetworkPacket.from_dict(self._full_dict)
        xml = Observables(np).to_xml(encoding=None)

        new_obj = Observables.from_obj(parseString(xml))
        new_dict = new_obj.observables[0].object_.properties.to_dict()

        self.maxDiff = None
        self.assertEqual(self._full_dict, new_dict)


class TestEthernetInterface(EntityTestCase, unittest.TestCase):
    klass = EthernetInterface

    _full_dict = {
        'ethernet_header': {
            'destination_mac_addr': {'address_value': u("00:11:22:33:44:55"),
                                        'category': Address.CAT_MAC,
                                        'xsi:type': 'AddressObjectType'},
            'source_mac_addr': {'address_value': u("aa:bb:cc:dd:ee:ff"),
                                'category': Address.CAT_MAC,
                                'xsi:type': 'AddressObjectType'},
            'type_or_length': {'length': u("1abf"),
                                'internet_layer_type': u("IPv4(0x0800)")},
            'checksum': u("fa10"),
        }
    }


class TestARP(EntityTestCase, unittest.TestCase):
    klass = ARP

    _full_dict = {
        'hardware_addr_type': u("Ethernet(1)"),
        'proto_addr_type': u("IPv4(0x0800)"),
        'hardware_addr_size': u("6"),
        'proto_addr_size': u("4"),
        'op_type': u("ARP request(1)"),
        'sender_hardware_addr': {'address_value': u("01:12:23:34:45:56"),
                                    'category': Address.CAT_MAC,
                                    'xsi:type': 'AddressObjectType'},
        'sender_protocol_addr': {'address_value': u("1.2.3.4"),
                                    'category': Address.CAT_IPV4,
                                    'xsi:type': 'AddressObjectType'},
        'recip_hardware_addr': {'address_value': u("a0:b0:c0:d0:e0:f0"),
                                'category': Address.CAT_MAC,
                                'xsi:type': 'AddressObjectType'},
        'recip_protocol_addr': {'address_value': u("9.10.11.12"),
                                'category': Address.CAT_IPV4,
                                'xsi:type': 'AddressObjectType'},
    }


class TestNDPLinkAddr(EntityTestCase, unittest.TestCase):
    klass = NDPLinkAddr
    _full_dict = {
        'length': u('14'),
        'link_layer_mac_addr': {'address_value': u("80:70:60:50:40:30"),
                                'category': Address.CAT_MAC,
                                'xsi:type': 'AddressObjectType'},
    }


class TestNDPPrefixInfo(EntityTestCase, unittest.TestCase):
    klass = NDPPrefixInfo

    _full_dict = {
        'link_flag': False,
        'addr_config_flag': True,
        'length': u("14"),
        'prefix_length': 7,
        'valid_lifetime': 123455,
        'preferred_lifetime': 1000,
        'prefix': {
            'ipv6_addr': {'address_value': u("2001:db8::ff00:42:832"),
                            'category': Address.CAT_IPV6,
                            'xsi:type': 'AddressObjectType'},
            'ip_addr_prefix': {'address_value': u("2001:0db8:85a3"),
                                    'category': Address.CAT_IPV6,
                                    'xsi:type': 'AddressObjectType'},
        }
    }


class TestNDP(EntityTestCase, unittest.TestCase):
    klass = NDP

    _full_dict = {
        'icmpv6_header': {
            'type': u("01"),
            'code': u("07"),
            'checksum': u("06BC"),
        },
        # This is normally a choice, but we can currently just check
        # them all at once. For X_link_addr, we are checking them above,
        # so we only use a length here.
        'router_solicitation': {
            'options': [{'src_link_addr': {'length': u("16")}}],
        },
        'router_advertisement': {
            'managed_address_config_flag': True,
            'other_config_flag': False,
            'cur_hop_limit': 16,
            'reachable_time': 1000,
            'retrans_timer': 5000,
            'options': {
                'src_link_addr': {'length': u("8")},
                'mtu': {'length': 8, 'mtu': 1500},
                'prefix_info': {'link_flag': True, 'length': u("44")},
            }
        },
        'neighbor_solicitation': {
            'target_ipv6_addr': {'address_value': u("2001:db99::ff00:832"),
                                    'category': Address.CAT_IPV6,
                                    'xsi:type': 'AddressObjectType'},
            'options': {'src_link_addr': {'length': u("99")}},
        },
        'neighbor_advertisement': {
            'router_flag': True,
            'solicited_flag': False,
            'override_flag': True,
            'target_ipv6_addr': {'address_value': u("::1"),
                                 'category': Address.CAT_IPV6,
                                 'xsi:type': 'AddressObjectType'},
            'options': {'target_link_addr': {'length': u("48")}},
        },
        'redirect': {
            'target_ipv6_addr': {'address_value': u("2001::1"),
                                    'category': Address.CAT_IPV6,
                                    'xsi:type': 'AddressObjectType'},
            'dest_ipv6_addr': {'address_value': u("2001::dd88:1"),
                                'category': Address.CAT_IPV6,
                                'xsi:type': 'AddressObjectType'},
            'options': {
                'target_link_addr': {'length': u("48")},
                'redirected_header': {
                    'length': u("77"),
                    'ipheader_and_data': '3bda4659ace',
                },
            },
        },
    }


class TestIPv4Packet(EntityTestCase, unittest.TestCase):
    klass = IPv4Packet

    _full_dict = {
        'ipv4_header': {
            'ip_version': u("IPv4(4)"),
            'header_length': 32,
            'dscp': u("5fc1"),
            'ecn': u("4ca6"),
            'total_length': u("ffff"),
            'identification': 10,
            'flags': {
                'reserved': 0,
                'do_not_fragment': u("donotfragment(1)"),
                'more_fragments': u("lastfragment(0)"),
            },
            'fragment_offset': u("7c"),
            'ttl': u("fa"),
            'protocol': u("TPC(6)"),
            'checksum': u("0fca"),
            'src_ipv4_addr': {'address_value': u("172.16.21.50"),
                            'category': Address.CAT_IPV4,
                            'xsi:type': 'AddressObjectType'},
            'dest_ipv4_addr': {'address_value': u("172.16.21.1"),
                            'category': Address.CAT_IPV4,
                            'xsi:type': 'AddressObjectType'},
            'option': [
                {'copy_flag': u("donotcopy(0)"), 'class': u("control(0)")},
                {'class': u("reserved(3)"), 'option': u("security(2)")},
            ]
        },
        'data': u("04fc3a3f67e4"),
    }


class TestICMPv4(EntityTestCase, unittest.TestCase):
    klass = ICMPv4Packet

    _full_dict = {
        'icmpv4_header': {
            'type': u("02"),
            'code': u("06"), 'checksum': u("06BC"), },
        'error_msg': {
            'destination_unreachable': {
                'destination_network_unreachable': True,
                'destination_host_unreachable': True,
                'destination_protocol_unreachable': True,
                'destination_port_unreachable': True,
                'fragmentation_required': {
                    'fragmentation_required': True,
                    'next_hop_mtu': u("a150"),
                },
                'source_route_failed': True,
                'destination_network_unknown': True,
                'destination_host_unknown': True,
                'source_host_isolated': True,
                'network_administratively_prohibited': True,
                'host_administratively_prohibited': True,
                'network_unreachable_for_tos': True,
                'host_unreachable_for_tos': True,
                'communication_administratively_prohibited': True,
                'host_precedence_violation': True,
                'precedence_cutoff_in_effect': True,
            },
            'source_quench': {
                'source_quench': True,
            },
            'redirect_message': {
                'network_redirect': True,
                'host_redirect': True,
                'tos_network_redirect': True,
                'tos_host_redirect': True,
                'ip_address': {'address_value': u("10.3.4.5"),
                                'category': Address.CAT_IPV4,
                                'xsi:type': 'AddressObjectType'},
            },
            'time_exceeded': {
                'ttl_exceeded_in_transit': True,
                'frag_reassembly_time_exceeded': True,
            },
            'error_msg_content': {
                'ip_header': {'ip_version': u("IPv4(4)")},
                'first_eight_bytes': u("0123456789abcdef"),
            },
        },
        'info_msg': {
            'echo_reply': {
                'echo_reply': True,
                'data': u("5f3dce41")
            },
            'echo_request': {
                'echo_request': True,
                'data': u("14ecd3f5")
            },
            'timestamp_request': {
                'timestamp': True,
                'originate_timestamp': 4567812,
            },
            'timestamp_reply': {
                'timestamp_reply': True,
                'originate_timestamp': 4567811,
                'receive_timestamp': 4567814,
                'transmit_timestamp': 4567819,
            },
            'address_mask_request': {
                'address_mask_request': True,
                'address_mask': {'address_value': u("255.255.0.0"),
                                    'category': Address.CAT_IPV4_NETMASK,
                                    'xsi:type': 'AddressObjectType'},
            },
            'address_mask_reply': {
                'address_mask_reply': True,
                'address_mask': {'address_value': u("255.255.255.0"),
                                    'category': Address.CAT_IPV4_NETMASK,
                                    'xsi:type': 'AddressObjectType'},
            },
            'info_msg_content': {
                'identifier': u("f198"),
                'sequence_number': u("1dc9"),
            },
        },
        'traceroute': {
            'outbound_packet_forward_success': True,
            'outbound_packet_no_route': True,
            'identifier': u("1234"),
            'outbound_hop_count': u("001f"),
            'return_hop_count': u("001c"),
            'output_link_speed': u("000f42f0"),
            'output_link_mtu': u("00000000"),
        },
    }


class TestIPv6(EntityTestCase, unittest.TestCase):
    klass = IPv6Packet

    _full_dict = {
        'ipv6_header': {
            'ip_version': u("IPv6(6)"),
            'traffic_class': u("ff"),
            'flow_label': u("abcde"),
            'payload_length': u("1000"),
            'next_header': u("TCP(6)"),
            'ttl': u('fa'),
            'src_ipv6_addr': {'address_value': u("2001:85a3::8a2e:370:734"),
                            'category': Address.CAT_IPV6,
                            'xsi:type': 'AddressObjectType'},
            'dest_ipv6_addr': {'address_value': u("2001:3a58::8a2e:370:734"),
                            'category': Address.CAT_IPV6,
                            'xsi:type': 'AddressObjectType'},
        },
        'ext_headers': [
            {
                'hop_by_hop_options': {
                    'next_header': u("IPv6routingheader(43)"),
                    'header_ext_len': u("1f"),
                    'option_data': [
                        {
                            'option_type': {
                                'do_not_recogn_action': u("skipoption(00)"),
                                'packet_change': u("change(1)"),
                                'option_byte': u("04"),
                            },
                            'option_data_len': u("0100"),
                            'pad1': {'octet': u("00")},
                            'padn': {'octet': u("01"),
                                        'option_data_length': 42,
                                        'option_data': 00}
                        },
                        {
                            'option_type': {'option_byte': u("02")},
                            'option_data_len': u("007f"),
                            'pad1': {'octet': u("00")},
                        },
                    ]
                },
            },
            {
                'routing': {
                    'next_header': u("IPv6routingheader(43)"),
                    'header_ext_len': 32,
                    'routing_type': u("4a"),
                    'segments_left': 13,
                    'type_specific_data': u("AAAAAAAA")
                },
            },
            {
                'fragment': {
                    'fragment_header': {
                        'next_header': u("IPv6routingheader(43)"),
                        'fragment_offset': u("01fb"),
                        'm_flag': u("lastfragment(0)"),
                        'identification': u("aa"),
                    },
                    'fragment': u("bc27648fbace")
                },
            },
            {
                'destination_options': [
                    {
                        'next_header': u("IPv6routingheader(43)"),
                        'header_ext_len': u("1f"),
                        'option_data': [
                            {
                                'option_data_len': u("0100"),
                                'pad1': {'octet': u("00")},
                            },
                            {
                                'option_type': {'option_byte': u("02")},
                            },
                        ]
                    },
                    {
                        'header_ext_len': u("1f"),
                    },
                ],
            },
            {
                'authentication_header': {
                    'next_header': u("IPv6routingheader(43)"),
                    'header_ext_len': u("1f"),
                    'security_parameters_index': u("deadbeef"),
                    'sequence_number': u("feedbacc"),
                    'authentication_data': u("abcd0123fedc4567"),
                },
            },
            {
                'encapsulating_security_payload': {
                    'security_parameters_index': u("deadbeef"),
                    'sequence_number': u("feedbacc"),
                    'payload_data': u("777788889999aaaa"),
                    'padding': u("0000000"),
                    'padding_len': u("7"),
                    'next_header': u("IPv6routingheader(43)"),
                    'authentication_data': u("abcd0123fedc4567"),
                },
            },
        ],
    }


class TestICMPv6(EntityTestCase, unittest.TestCase):
    klass = ICMPv6Packet

    _full_dict = {
        'icmpv6_header': {
            'type': u("02"),
            'code': u("06"),
            'checksum': u("06BC"),
        },
        'error_msg': {
            'destination_unreachable': {
                'no_route': True,
                'comm_prohibited': True,
                'beyond_scope': True,
                'address_unreachable': True,
                'port_unreachable': True,
                'src_addr_failed_policy': True,
                'reject_route': True,
            },
            'packet_too_big': {
                'packet_too_big': True,
                'mtu': u("1f00"),
            },
            'time_exceeded': {
                'hop_limit_exceeded': True,
                'fragment_reassem_time_exceeded': True,
            },
            'parameter_problem': {
                'erroneous_header_field': True,
                'unrecognized_next_header_type': True,
                'unrecognized_ipv6_option': True,
                'pointer': u("7fffaabb"),
            },
            'invoking_packet': u("0f1e2d3c4b5a9687"),
        },
        'info_msg': {
            'echo_request': {
                'echo_request': True,
                'data': u("2468ace0")
            },
            'echo_reply': {
                'echo_reply': True,
                'data': u("0eca8642")
            },
            'info_msg_content': {
                'identifier': u("f198"),
                'sequence_number': u("1dc9"),
            },
        },
    }


class TestTCP(EntityTestCase, unittest.TestCase):
    klass = TCP

    _full_dict = {
        'tcp_header': {
            'src_port': {'port_value': 1444,
                            'layer4_protocol': u('TCP'),
                            'xsi:type': 'PortObjectType'},
            'dest_port': {'port_value': 80,
                            'layer4_protocol': u('TCP'),
                            'xsi:type': 'PortObjectType'},
            'seq_num': u("148f3b44"),
            'ack_num': u("664d012a"),
            'data_offset': u("20"),
            'reserved': 1,
            'tcp_flags': {
                'ns': True,
                'cwr': True,
                'ece': True,
                'urg': True,
                'ack': True,
                'psh': True,
                'rst': True,
                'syn': True,
                'fin': True,
            },
            'window': u("1460"),
            'checksum': u("1fc1"),
            'urg_ptr': u("0001")
        },
        'options': u("010305"),
        'data': {
            'data_format': "Text",
            'data_size': {"value": u("100"), 'units': "Kilobytes"},
            'data_segment': u("A long, long time ago..."),
            'offset': 100,
            'search_distance': 200,
            'search_within': 40,
        }
    }


class TestUDP(EntityTestCase, unittest.TestCase):
    klass = UDP

    _full_dict = {
        'udp_header': {
            'srcport': {'port_value': 1664,
                            'layer4_protocol': u('UDP'),
                            'xsi:type': 'PortObjectType'},
            'destport': {'port_value': 53,
                            'layer4_protocol': u('UDP'),
                            'xsi:type': 'PortObjectType'},
            'length': 0x18,
            'checksum': u("1fc1"),
        },
        'data': {
            'data_format': "Hex",
            'data_size': {"value": u("16"), 'units': "Bytes"},
            'data_segment': u("000102030405060708090a0b0c0d0e0f"),
        }
    }


if __name__ == "__main__":
    unittest.main()
