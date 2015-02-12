# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.volume_object as volume_binding
from cybox.common import ObjectProperties, String, DateTime, UnsignedLong, PositiveInteger, UnsignedInteger

class FileSystemFlagList(cybox.EntityList):
    _binding = volume_binding
    _binding_class = volume_binding.FileSystemFlagListType
    _binding_var = "File_System_Flag"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#VolumeObject-2"

class Volume(ObjectProperties):
    _binding = volume_binding
    _binding_class = volume_binding.VolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#VolumeObject-2"
    _XSI_NS = "VolumeObj"
    _XSI_TYPE = "VolumeObjectType"

    is_mounted = cybox.TypedField('is_mounted')
    name = cybox.TypedField('Name', String)
    device_path = cybox.TypedField('Device_Path', String)
    file_system_type = cybox.TypedField('File_System_Type', String)
    total_allocation_units = cybox.TypedField('Total_Allocation_Units', UnsignedLong)
    sectors_per_allocation_unit = cybox.TypedField('Sectors_Per_Allocation_Unit', UnsignedInteger)
    bytes_per_sector = cybox.TypedField('Bytes_Per_Sector', PositiveInteger)
    actual_available_allocation_units = cybox.TypedField('Actual_Available_Allocation_Units', UnsignedLong)
    creation_time = cybox.TypedField('Creation_Time', DateTime)
    file_system_flag_list = cybox.TypedField('File_System_Flag_List', FileSystemFlagList)
    serial_number = cybox.TypedField('Serial_Number', String)
