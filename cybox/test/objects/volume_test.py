# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.volume_object import FileSystemFlagList, Volume
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestFileSystemFlagList(EntityTestCase, unittest.TestCase):
    klass = FileSystemFlagList

    _full_dict = [
        u('FILE_UNICODE_ON_DISK'),
        u('FILE_CASE_SENSITIVE_SEARCH'),
    ]


class TestVolume(ObjectTestCase, unittest.TestCase):
    object_type = "VolumeObjectType"
    klass = Volume

    _full_dict = {
        'is_mounted': True,
        'name': u('sda'),
        'device_path': u('/dev/sda'),
        'file_system_type': u('ext4'),
        'total_allocation_units': 4000787030016,
        'sectors_per_allocation_unit': 976754646,
        'bytes_per_sector': 512,
        'actual_available_allocation_units': 3814697265600,
        'creation_time': '2001-01-01T06:56:50+04:00',
        'file_system_flag_list': TestFileSystemFlagList._full_dict,
        'serial_number': u('WD-WCC4E4LA4965'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
