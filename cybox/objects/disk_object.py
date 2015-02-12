# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.disk_object as disk_binding
from cybox.objects.disk_partition_object import DiskPartition
from cybox.common import ObjectProperties, String, UnsignedLong

class PartitionList(cybox.EntityList):
    _binding = disk_binding
    _binding_class = disk_binding.PartitionListType
    _binding_var = "Partition"
    _contained_type = DiskPartition
    _namespace = "http://cybox.mitre.org/objects#DiskObject-2"

class Disk(ObjectProperties):
    _binding = disk_binding
    _binding_class = disk_binding.DiskObjectType
    _namespace = "http://cybox.mitre.org/objects#DiskObject-2"
    _XSI_NS = "DiskObj"
    _XSI_TYPE = "DiskObjectType"

    disk_name = cybox.TypedField('Disk_Name', String)
    disk_size = cybox.TypedField('Disk_Size', UnsignedLong)
    free_space = cybox.TypedField('Free_Space', UnsignedLong)
    partition_list = cybox.TypedField('Partition_List', PartitionList)
    type = cybox.TypedField('Type', String)

