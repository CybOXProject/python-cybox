# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_process_object import FileDescriptorList, UnixProcess, UnixProcessStatus
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestFileDescriptorList(EntityTestCase, unittest.TestCase):
    klass = FileDescriptorList

    _full_dict = [
        [345, 1345],
    ]


class TestUnixProcessStatus(EntityTestCase, unittest.TestCase):
    klass = UnixProcessStatus

    _full_dict = {
        'current_status': u('Running'),
        'timestamp': '2001-01-01T06:56:50+04:00',
        'xsi:type': 'UnixProcessObj:UnixProcessStatusType',
    }


class TestUnixProcess(ObjectTestCase, unittest.TestCase):
    object_type = "UnixProcessObjectType"
    klass = UnixProcess

    _full_dict = {
        'open_file_descriptor_list': TestFileDescriptorList._full_dict,
        'status': TestUnixProcessStatus._full_dict,
        'ruid': 3485,
        'priority': 20,
        'session_id': 2345,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
