# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.process_object import (ArgumentList, ChildPIDList,
                                          ImageInfo, NetworkConnectionList,
                                          PortList, Process)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.network_connection_test import TestNetworkConnection
from cybox.test.objects.port_test import TestPort


class TestChildPIDList(EntityTestCase, unittest.TestCase):
    klass = ChildPIDList

    _full_dict = [
        22500,
        915,
    ]


class TestPortList(EntityTestCase, unittest.TestCase):
    klass = PortList

    _full_dict = [
        TestPort._full_dict,
        TestPort._full_dict,
    ]


class TestNetworkConnectionList(EntityTestCase, unittest.TestCase):
    klass = NetworkConnectionList

    _full_dict = [
        TestNetworkConnection._full_dict,
        TestNetworkConnection._full_dict,
    ]


class TestArgumentList(EntityTestCase, unittest.TestCase):
    klass = ArgumentList

    _full_dict = [
        u('-p'),
        u('-d')
    ]


class TestImageInfo(EntityTestCase, unittest.TestCase):
    klass = ImageInfo

    _full_dict = {
        'file_name': 'testproc.bin',
        'command_line': 'testproc.bin -p -d',
        'current_directory': '/test',
        'path': '/home/some_path',
    }


class TestProcess(ObjectTestCase, unittest.TestCase):
    object_type = "ProcessObjectType"
    klass = Process

    _full_dict = {
        'pid': 512,
        'name': u('testproc'),
        'creation_time': '2001-01-01T06:56:50+04:00',
        'parent_pid': 1024,
        'child_pid_list': TestChildPIDList._full_dict,
        'image_info': TestImageInfo._full_dict,
        'argument_list': TestArgumentList._full_dict,
        'environment_variable_list': [
            {'name': 'TEMP', 'value': 'C:/TEMP'},
        ],
        'kernel_time': u('293457969'),
        'port_list': TestPortList._full_dict,
        'network_connection_list': TestNetworkConnectionList._full_dict,
        'start_time': '2001-01-01T06:56:50+04:00',
        'username': u('jondoe'),
        'user_time': u('120'),
        # 'extracted_features': '',
        'is_hidden': True,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
