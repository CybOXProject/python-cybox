# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.system_object import (BIOSInfo, DHCPServerList,
                                         IPGatewayList, IPInfo,
                                         IPInfoList, NetworkInterface,
                                         NetworkInterfaceList, OS, System)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.address_test import TestAddress


class TestDHCPServerList(EntityTestCase, unittest.TestCase):
    klass = DHCPServerList

    _full_dict = [
        TestAddress._full_dict,
    ]


class TestIPGatewayList(EntityTestCase, unittest.TestCase):
    klass = IPGatewayList

    _full_dict = [
        TestAddress._full_dict,
    ]


class TestIPInfo(EntityTestCase, unittest.TestCase):
    klass = IPInfo

    _full_dict = {
        'ip_address': TestAddress._full_dict,
        'subnet_mask': TestAddress._full_dict,
    }


class TestIPInfoList(EntityTestCase, unittest.TestCase):
    klass = IPInfoList

    _full_dict = [
        TestIPInfo._full_dict,
    ]


class TestOS(EntityTestCase, unittest.TestCase):
    klass = OS

    _full_dict = {
        'bitness': '64-bit',
        'build_number': '14393.693',
        'environment_variable_list': [
            {'name': 'TEMP', 'value': 'C:/TEMP'},
        ],
        'install_date': '2001-01-01',
        'patch_level': '10',
        'platform': {
            'description': u('A Windows platform'),
            'identifier': [
                u('Windows')
            ],
        },
    }


class TestBIOSInfo(EntityTestCase, unittest.TestCase):
    klass = BIOSInfo

    _full_dict = {
        'bios_date': '2001-01-01',
        'bios_version': u('A19'),
        'bios_manufacturer': u('Fabrikam'),
        'bios_release_date': '2001-01-01',
        'bios_serial_number': u('7GHX44'),
    }


class TestNetworkInterface(EntityTestCase, unittest.TestCase):
    klass = NetworkInterface

    _full_dict = {
        'adapter': u('I350-T2V2'),
        'description': u('Test Network Interface'),
        'dhcp_lease_expires': '2001-01-01T06:56:50+04:00',
        'dhcp_lease_obtained': '2001-01-01T06:56:50+04:00',
        'dhcp_server_list': TestDHCPServerList._full_dict,
        'ip_gateway_list': TestIPGatewayList._full_dict,
        'ip_list': TestIPInfoList._full_dict,
        'mac': u('30:65:EC:6F:C4:58'),
    }


class TestNetworkInterfaceList(EntityTestCase, unittest.TestCase):
    klass = NetworkInterfaceList

    _full_dict = [
        TestNetworkInterface._full_dict,
        TestNetworkInterface._full_dict,
    ]


class TestSystem(ObjectTestCase, unittest.TestCase):
    object_type = "SystemObjectType"
    klass = System

    _full_dict = {
        'available_physical_memory': 3814697265600,
        'bios_info': TestBIOSInfo._full_dict,
        'date': '2001-01-01',
        'hostname': u('johndoe.frabikam.org'),
        'local_time': '06:56:50+04:00',
        'network_interface_list': TestNetworkInterfaceList._full_dict,
        'os': TestOS._full_dict,
        'processor': u('Intel Pentium II'),
        'processor_architecture': u('32-bit'),
        'system_time': '06:56:50+04:00',
        'timezone_dst': u('EDT'),
        'timezone_standard': u('GMT'),
        'total_physical_memory': 4000787030016,
        'uptime': u('3600'),
        'username': u('johndoe'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
