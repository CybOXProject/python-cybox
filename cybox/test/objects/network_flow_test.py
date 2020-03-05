# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.network_flow_object import (
    BidirectionalRecord, IPFIXDataSet, IPFIXTemplateRecord, IPFIXDataRecord,
    IPFIXMessage, IPFIXSet, IPFIXMessageHeader, FlowDataRecord,
    FlowCollectionElement, OptionsDataRecord, OptionCollectionElement,
    IPFIXSetHeader, IPFIXOptionsTemplateRecord,
    IPFIXOptionsTemplateRecordHeader, IPFIXOptionsTemplateSet,
    IPFIXTemplateRecordFieldSpecifiers, IPFIXTemplateRecordHeader,
    IPFIXTemplateSet, NetflowV5Packet, NetflowV5FlowHeader,
    NetflowV5FlowRecord, NetflowV9DataFlowSet, NetflowV9PacketHeader,
    NetflowV9ExportPacket, NetflowV9OptionsTemplateFlowSet, NetflowV9Field,
    NetflowV9FlowSet, NetflowV9DataRecord, NetflowV9TemplateFlowSet,
    NetflowV9TemplateRecord, NetflowV9OptionsTemplateRecord, NetworkFlow,
    NetworkFlowLabel, NetworkLayerInfo, UnidirectionalRecord, SiLKRecord,
    SiLKSensorInfo, SiLKFlowAttributes, SiLKAddress, SiLKSensorClass,
    SiLKSensorDirection, YAFReverseFlow, YAFRecord, YAFFlow, YAFTCPFlow
)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.address_test import TestAddress
from cybox.test.objects.network_packet_test import TestTCPFlags
from cybox.test.objects.socket_address_test import TestSocketAddress


class TestNetworkFlowLabel(EntityTestCase, unittest.TestCase):
    klass = NetworkFlowLabel

    _full_dict = {
        'ingress_interface_index': 2,
        'egress_interface_index': 3,
        'src_socket_address': TestSocketAddress._full_dict,
        'dest_socket_address': TestSocketAddress._full_dict,
        'ip_protocol': 'TCP',
    }


class TestNetworkLayerInfo(EntityTestCase, unittest.TestCase):
    klass = NetworkLayerInfo

    _full_dict = {
        'src_socket_address': TestSocketAddress._full_dict,
        'dest_socket_address': TestSocketAddress._full_dict,
        'ip_protocol': 'TCP',
    }


class TestYAFTCPFlow(EntityTestCase, unittest.TestCase):
    klass = YAFTCPFlow

    _full_dict = {
        'tcp_sequence_number': 5,
        'initial_tcp_flags': TestTCPFlags._full_dict,
        'union_tcp_flags': u('0C'),
    }


class TestYAFFlow(EntityTestCase, unittest.TestCase):
    klass = YAFFlow

    _full_dict = {
        'flow_start_milliseconds': 1582060813,
        'flow_end_milliseconds': 1582060900,
        'octet_total_count': 144,
        'packet_total_count': 100,
        'flow_end_reason': u('0C'),
        'silk_app_label': 53,
        'payload_entropy': 34,
        'ml_app_label': u('0C'),
        'tcp_flow': TestYAFTCPFlow._full_dict,
        'vlan_id_mac_addr': TestAddress._full_dict,
        'passive_os_fingerprinting': {
            'description': u("The best platform"),
            'identifier': [
                u("value1")
            ]
        },
        'first_packet_banner': u('00'),
        'second_packet_banner': u('0A'),
        'n_bytes_payload': u('EC'),
    }


class TestYAFReverseFlow(EntityTestCase, unittest.TestCase):
    klass = YAFReverseFlow

    _full_dict = {
        'reverse_octet_total_count': 144,
        'reverse_packet_total_count': 100,
        'reverse_payload_entropy': 25,
        'reverse_flow_delta_milliseconds': 1356,
        'tcp_reverse_flow': TestYAFTCPFlow._full_dict,
        'reverse_vlan_id_mac_addr': TestAddress._full_dict,
        'reverse_passive_os_fingerprinting': {
            'description': u("The best platform"),
            'identifier': [
                u("value1")
            ]
        },
        'reverse_first_packet': u('00'),
        'reverse_n_bytes_payload': u('EC'),
    }


class TestYAFRecord(EntityTestCase, unittest.TestCase):
    klass = YAFRecord

    _full_dict = {
        'flow': TestYAFFlow._full_dict,
        'reverse_flow': TestYAFReverseFlow._full_dict,
    }


class TestIPFIXSetHeader(EntityTestCase, unittest.TestCase):
    klass = IPFIXSetHeader

    _full_dict = {
        'set_id': 35,
        'length': 100,
    }


class TestIPFIXDataRecord(EntityTestCase, unittest.TestCase):
    klass = IPFIXDataRecord

    _full_dict = {
        'field_value': [
            u('value1'),
            u('value2'),
        ]
    }


class TestIPFIXMessageHeader(EntityTestCase, unittest.TestCase):
    klass = IPFIXMessageHeader

    _full_dict = {
        'version': u('A0'),
        'byte_length': u('FEAC'),
        'export_timestamp': 1582060823,
        'sequence_number': 19382,
        'observation_domain_id': 245,
    }


class TestIPFIXTemplateRecordFieldSpecifiers(EntityTestCase, unittest.TestCase):
    klass = IPFIXTemplateRecordFieldSpecifiers

    _full_dict = {
        'enterprise_bit': True,
        'information_element_id': 'Something',
        'field_length': '128395',
        'enterprise_number': '1.3.6.1.4.1',
    }


class TestIPFIXTemplateRecordHeader(EntityTestCase, unittest.TestCase):
    klass = IPFIXTemplateRecordHeader

    _full_dict = {
        'template_id': 556,
        'field_count': 'FF452'
    }


class TestIPFIXOptionsTemplateRecordHeader(EntityTestCase, unittest.TestCase):
    klass = IPFIXOptionsTemplateRecordHeader

    _full_dict = {
        'template_id': 160,
        'field_count': 'BF45',
        'scope_field_count': 15,
    }


class TestIPFIXDataSet(EntityTestCase, unittest.TestCase):
    klass = IPFIXDataSet

    _full_dict = {
        'set_header': TestIPFIXSetHeader._full_dict,
        'data_record': [
            TestIPFIXDataRecord._full_dict
        ],
        'padding': u('0C'),
    }


class TestIPFIXOptionsTemplateRecord(EntityTestCase, unittest.TestCase):
    klass = IPFIXOptionsTemplateRecord

    _full_dict = {
        'options_template_record_header': TestIPFIXOptionsTemplateRecordHeader._full_dict,
        'field_specifier': [
            TestIPFIXTemplateRecordFieldSpecifiers._full_dict
        ]
    }


class TestIPFIXOptionsTemplateSet(EntityTestCase, unittest.TestCase):
    klass = IPFIXOptionsTemplateSet

    _full_dict = {
        'set_header': TestIPFIXSetHeader._full_dict,
        'options_template_record': [
            TestIPFIXOptionsTemplateRecord._full_dict
        ],
        'padding': u('C0')
    }


class TestIPFIXTemplateRecord(EntityTestCase, unittest.TestCase):
    klass = IPFIXTemplateRecord

    _full_dict = {
        'template_record_header': TestIPFIXTemplateRecordHeader._full_dict,
        'field_specifier': [
            TestIPFIXTemplateRecordFieldSpecifiers._full_dict
        ]
    }


class TestIPFIXTemplateSet(EntityTestCase, unittest.TestCase):
    klass = IPFIXTemplateSet

    _full_dict = {
        'set_header': TestIPFIXSetHeader._full_dict,
        'template_record': [
            TestIPFIXTemplateRecord._full_dict
        ],
        'padding': u('FE')
    }


class TestIPFIXSet(EntityTestCase, unittest.TestCase):
    klass = IPFIXSet

    _full_dict = {
        'template_set': TestIPFIXTemplateSet._full_dict,
        'options_template_set': TestIPFIXOptionsTemplateSet._full_dict,
        'data_set': TestIPFIXDataSet._full_dict,
    }


class TestIPFIXMessage(EntityTestCase, unittest.TestCase):
    klass = IPFIXMessage

    _full_dict = {
        'message_header': TestIPFIXMessageHeader._full_dict,
        'set': [
            TestIPFIXSet._full_dict
        ]
    }


class TestNetflowV5FlowRecord(EntityTestCase, unittest.TestCase):
    klass = NetflowV5FlowRecord

    _full_dict = {
        'nexthop_ipv4_addr': TestAddress._full_dict,
        'packet_count': 50,
        'byte_count': 123448,
        'sysuptime_start': 1582060823,
        'sysuptime_end': 1582060824,
        'padding1': u('0'),
        'tcp_flags': u('02'),
        'src_autonomous_system': 2,
        'dest_autonomous_system': 1,
        'src_ip_mask_bit_count': u('0'),
        'dest_ip_mask_bit_count': u('0'),
        'padding2': u('0'),
    }


class TestNetflowV5FlowHeader(EntityTestCase, unittest.TestCase):
    klass = NetflowV5FlowHeader

    _full_dict = {
        'version': u('05'),
        'count': 2,
        'sys_up_time': 1582060823,
        'unix_secs': 345,
        'unix_nsecs': 348,
        'flow_sequence': 55,
        'engine_type': u('Some Engine'),
        'engine_id': 4523,
        'sampling_interval': u('CE'),
    }


class TestNetflowV5Packet(EntityTestCase, unittest.TestCase):
    klass = NetflowV5Packet

    _full_dict = {
        'flow_header': TestNetflowV5FlowHeader._full_dict,
        'flow_record': [
            TestNetflowV5FlowRecord._full_dict
        ]
    }


class TestOptionCollectionElement(EntityTestCase, unittest.TestCase):
    klass = OptionCollectionElement

    _full_dict = {
        'option_record_field_value': [
            u('Some Value2')
        ]
    }


class TestFlowCollectionElement(EntityTestCase, unittest.TestCase):
    klass = FlowCollectionElement

    _full_dict = {
        'flow_record_field_value': [
            u('Some String')
        ]
    }


class TestFlowDataRecord(EntityTestCase, unittest.TestCase):
    klass = FlowDataRecord

    _full_dict = {
        'flow_record_collection_element': [
            TestFlowCollectionElement._full_dict
        ]
    }


class TestOptionsDataRecord(EntityTestCase, unittest.TestCase):
    klass = OptionsDataRecord

    _full_dict = {
        'scope_field_value': u('Some Value'),
        'option_record_collection_element': [
            TestOptionCollectionElement._full_dict
        ]
    }


class TestNetflowV9PacketHeader(EntityTestCase, unittest.TestCase):
    klass = NetflowV9PacketHeader

    _full_dict = {
        'version': u('09'),
        'record_count': 20,
        'sys_up_time': 1582060823,
        'unix_secs': 34,
        'sequence_number': 553242,
        'source_id': u('312E'),
    }


class TestNetflowV9DataRecord(EntityTestCase, unittest.TestCase):
    klass = NetflowV9DataRecord

    _full_dict = {
        'flow_data_record': [
            TestFlowDataRecord._full_dict
        ],
        'options_data_record': [
            TestOptionsDataRecord._full_dict
        ],
    }


class TestNetflowV9DataFlowSet(EntityTestCase, unittest.TestCase):
    klass = NetflowV9DataFlowSet

    _full_dict = {
        'flow_set_id_template_id': 2,
        'length': 10,
        'data_record': [
            TestNetflowV9DataRecord._full_dict
        ],
        'padding': u('DE'),
    }


class TestNetflowV9TemplateRecord(EntityTestCase, unittest.TestCase):
    klass = NetflowV9TemplateRecord

    _full_dict = {
        'template_id': 2345,
        'field_count': 110,
        'field_type': u(NetflowV9Field.TERM_IN_BYTES),
        'field_length': u('FF'),
    }


class TestNetflowV9TemplateFlowSet(EntityTestCase, unittest.TestCase):
    klass = NetflowV9TemplateFlowSet

    _full_dict = {
        'flow_set_id': u('AA'),
        'length': 100,
        'template_record': [
            TestNetflowV9TemplateRecord._full_dict
        ],
    }


class TestNetflowV9OptionsTemplateRecord(EntityTestCase, unittest.TestCase):
    klass = NetflowV9OptionsTemplateRecord

    _full_dict = {
        'template_id': 341,
        'option_scope_length': u('A4'),
        'option_length': u('2'),
        'scope_field_type': u('Scope Type'),
        'scope_field_length': u('E0'),
        'option_field_type': u('IN_BYTES(1)'),
        'option_field_length': u('B0'),
    }


class TestNetflowV9OptionsTemplateFlowSet(EntityTestCase, unittest.TestCase):
    klass = NetflowV9OptionsTemplateFlowSet

    _full_dict = {
        'flow_set_id': u('01'),
        'length': 10,
        'options_template_record': [
            TestNetflowV9OptionsTemplateRecord._full_dict
        ],
        'padding': u('AB'),
    }


class TestNetflowV9FlowSet(EntityTestCase, unittest.TestCase):
    klass = NetflowV9FlowSet

    _full_dict = {
        'template_flow_set': TestNetflowV9TemplateFlowSet._full_dict,
        'options_template_flow_set': TestNetflowV9OptionsTemplateFlowSet._full_dict,
        'data_flow_set': TestNetflowV9DataFlowSet._full_dict,
    }


class TestNetflowV9ExportPacket(EntityTestCase, unittest.TestCase):
    klass = NetflowV9ExportPacket

    _full_dict = {
        'packet_header': TestNetflowV9PacketHeader._full_dict,
        'flow_set': [
            TestNetflowV9FlowSet._full_dict
        ]
    }


class TestSiLKSensorInfo(EntityTestCase, unittest.TestCase):
    klass = SiLKSensorInfo

    _full_dict = {
        'sensor_id': u('2349'),
        'class': u(SiLKSensorClass.TERM_ALL),
        'type': u(SiLKSensorDirection.TERM_IN),
    }


class TestSiLKRecord(EntityTestCase, unittest.TestCase):
    klass = SiLKRecord

    _full_dict = {
        'packet_count': 55,
        'byte_count': 12800,
        'tcp_flags': u('B9'),
        'start_time': 1582060823,
        'duration': 100,
        'end_time': 1582060923,
        'sensor_info': TestSiLKSensorInfo._full_dict,
        'icmp_type': 6,
        'icmp_code': 2,
        'router_next_hop_ip': TestAddress._full_dict,
        'initial_tcp_flags': TestTCPFlags._full_dict,
        'session_tcp_flags': u('3'),
        'flow_attributes': u(SiLKFlowAttributes.TERM_F),
        'flow_application': u('My Flow Application'),
        'src_ip_type': u(SiLKAddress.TERM_INTERNAL),
        'dest_ip_type': u(SiLKAddress.TERM_EXTERNAL),
        'src_country_code': u('US'),
        'dest_country_code': u('US'),
        'src_mapname': u('some value1'),
        'dest_mapname': u('some value2'),
    }


class TestUnidirectionalRecord(EntityTestCase, unittest.TestCase):
    klass = UnidirectionalRecord

    _full_dict = {
        'ipfix_message': TestIPFIXMessage._full_dict,
        'netflowv9_export_packet': TestNetflowV9ExportPacket._full_dict,
        'netflowv5_packet': TestNetflowV5Packet._full_dict,
        'silk_record': TestSiLKRecord._full_dict,
    }


class TestBidirectionalRecord(EntityTestCase, unittest.TestCase):
    klass = BidirectionalRecord

    _full_dict = {
        'yaf_record': TestYAFRecord._full_dict
    }


class TestNetworkFlow(ObjectTestCase, unittest.TestCase):
    object_type = "NetworkFlowObjectType"
    klass = NetworkFlow

    _full_dict = {
        'network_flow_label': TestNetworkFlowLabel._full_dict,
        'unidirectional_flow_record': TestUnidirectionalRecord._full_dict,
        'bidirectional_flow_record': TestBidirectionalRecord._full_dict,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
