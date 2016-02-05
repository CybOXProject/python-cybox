# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.volume_object as volume_binding
from cybox.common import ObjectProperties, String, DateTime, UnsignedLong, PositiveInteger, UnsignedInteger


class FileSystemFlagList(entities.EntityList):
    _binding = volume_binding
    _binding_class = volume_binding.FileSystemFlagListType
    _namespace = "http://cybox.mitre.org/objects#VolumeObject-2"
    file_system_flag = fields.TypedField("File_System_Flag", String, multiple=True)


class Volume(ObjectProperties):
    _binding = volume_binding
    _binding_class = volume_binding.VolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#VolumeObject-2"
    _XSI_NS = "VolumeObj"
    _XSI_TYPE = "VolumeObjectType"

    is_mounted = fields.TypedField('is_mounted')
    name = fields.TypedField('Name', String)
    device_path = fields.TypedField('Device_Path', String)
    file_system_type = fields.TypedField('File_System_Type', String)
    total_allocation_units = fields.TypedField('Total_Allocation_Units', UnsignedLong)
    sectors_per_allocation_unit = fields.TypedField('Sectors_Per_Allocation_Unit', UnsignedInteger)
    bytes_per_sector = fields.TypedField('Bytes_Per_Sector', PositiveInteger)
    actual_available_allocation_units = fields.TypedField('Actual_Available_Allocation_Units', UnsignedLong)
    creation_time = fields.TypedField('Creation_Time', DateTime)
    file_system_flag_list = fields.TypedField('File_System_Flag_List', FileSystemFlagList)
    serial_number = fields.TypedField('Serial_Number', String)
