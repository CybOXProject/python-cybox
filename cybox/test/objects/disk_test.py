# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.disk_object import Disk
from cybox.test.objects import ObjectTestCase


class TestDisk(ObjectTestCase, unittest.TestCase):
    object_type = "DiskObjectType"
    klass = Disk

    _full_dict = {
        'disk_name': u"A disk",
        'disk_size': 12345678,
        'free_space': 1234567,
        'partition_list': [
            {
                'device_name': "A partition",
                'xsi:type': "DiskPartitionObjectType",
            },
            {
                'device_name': "B partition",
                'xsi:type': "DiskPartitionObjectType",
            },
        ],
        'type': "Fixed",
        'xsi:type': object_type,
    }

    # https://github.com/CybOXProject/python-cybox/issues/267
    def test_type(self):
        disk = Disk()
        disk.type_ = "Fixed"
        self.assertTrue(b"Fixed" in disk.to_xml())


if __name__ == "__main__":
    unittest.main()
