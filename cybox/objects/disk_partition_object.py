# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.disk_partition_object as disk_partition_binding
from cybox.common import ObjectProperties, String, Integer, Name, UnsignedLong, DateTime

class DiskPartition(ObjectProperties):
    _binding = disk_partition_binding
    _binding_class = disk_partition_binding.DiskPartitionObjectType
    _namespace = "http://cybox.mitre.org/objects#DiskPartitionObject-2"
    _XSI_NS = "DiskPartitionObj"
    _XSI_TYPE = "DiskPartitionObjectType"

    created = cybox.TypedField('Created', String)
    device_name = cybox.TypedField('Device_Name', Name)
    mount_point = cybox.TypedField('Mount_Point', String)
    partition_id = cybox.TypedField('Partition_ID', Integer)
    partition_length = cybox.TypedField('Partition_Length', UnsignedLong)
    partition_offset = cybox.TypedField('Partition_Offset', UnsignedLong)
    space_left = cybox.TypedField('Space_Left', UnsignedLong)
    space_used = cybox.TypedField('Space_Used', UnsignedLong)
    total_space = cybox.TypedField('Total_Space', UnsignedLong)
    type = cybox.TypedField('Type', UnsignedLong)