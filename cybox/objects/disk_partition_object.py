# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox
import cybox.bindings.disk_partition_object as disk_partition_binding
from cybox.common import ObjectProperties, String, Integer, Name, UnsignedLong, DateTime

class DiskPartition(ObjectProperties):
    _binding = disk_partition_binding
    _binding_class = disk_partition_binding.DiskPartitionObjectType
    _namespace = "http://cybox.mitre.org/objects#DiskPartitionObject-2"
    _XSI_NS = "DiskPartitionObj"
    _XSI_TYPE = "DiskPartitionObjectType"

    created = fields.TypedField('Created', String)
    device_name = fields.TypedField('Device_Name', Name)
    mount_point = fields.TypedField('Mount_Point', String)
    partition_id = fields.TypedField('Partition_ID', Integer)
    partition_length = fields.TypedField('Partition_Length', UnsignedLong)
    partition_offset = fields.TypedField('Partition_Offset', UnsignedLong)
    space_left = fields.TypedField('Space_Left', UnsignedLong)
    space_used = fields.TypedField('Space_Used', UnsignedLong)
    total_space = fields.TypedField('Total_Space', UnsignedLong)
    type = fields.TypedField('Type', UnsignedLong)
