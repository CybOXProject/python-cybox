# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.disk_partition_object as disk_partition_binding
from cybox.common import (DateTime, Integer, Name, ObjectProperties, String,
        UnsignedLong)


class DiskPartition(ObjectProperties):
    _binding = disk_partition_binding
    _binding_class = disk_partition_binding.DiskPartitionObjectType
    _namespace = "http://cybox.mitre.org/objects#DiskPartitionObject-2"
    _XSI_NS = "DiskPartitionObj"
    _XSI_TYPE = "DiskPartitionObjectType"

    created = fields.TypedField('Created', DateTime)
    device_name = fields.TypedField('Device_Name', Name)
    mount_point = fields.TypedField('Mount_Point', String)
    partition_id = fields.TypedField('Partition_ID', Integer)
    partition_length = fields.TypedField('Partition_Length', UnsignedLong)
    partition_offset = fields.TypedField('Partition_Offset', UnsignedLong)
    space_left = fields.TypedField('Space_Left', UnsignedLong)
    space_used = fields.TypedField('Space_Used', UnsignedLong)
    total_space = fields.TypedField('Total_Space', UnsignedLong)
    type_ = fields.TypedField('Type', String)
