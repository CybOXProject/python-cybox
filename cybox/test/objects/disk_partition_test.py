# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.disk_partition_object import DiskPartition
from cybox.test.objects import ObjectTestCase


class TestDiskPartition(ObjectTestCase, unittest.TestCase):
    object_type = "DiskPartitionObjectType"
    klass = DiskPartition

    _full_dict = {
        'created': "2007-10-05T07:14:21+00:00",
        'device_name': u"C partition",
        'mount_point': u"C:",
        'partition_id': 8,
        'partition_length': 5000000,
        'partition_offset': 1000000,
        'space_left': 50000,
        'space_used': 50001,
        'total_space': 100001,
        'type': "PARTITION_FAT_12",
        'xsi:type': object_type,
    }

    # https://github.com/CybOXProject/python-cybox/issues/267
    def test_type(self):
        partition = DiskPartition()
        partition.type_ = "PARTITION_FAT32"
        self.assertTrue(b"PARTITION_FAT32" in partition.to_xml())


if __name__ == "__main__":
    unittest.main()
