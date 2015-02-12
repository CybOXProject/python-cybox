# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_prefetch_object as win_prefetch_binding
from cybox.objects.device_object import Device
from cybox.objects.win_volume_object import WinVolume
from cybox.common import String, DateTime, Long, ObjectProperties


class AccessedFileList(cybox.EntityList):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.AccessedFileListType
    _binding_var = "Accessed_File"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    
class AccessedDirectoryList(cybox.EntityList):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.AccessedDirectoryListType
    _binding_var = "Accessed_Directory"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    
class Volume(cybox.EntityList):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.VolumeType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    
    volumeitem = cybox.TypedField("VolumeItem", WinVolume)
    deviceitem = cybox.TypedField("DeviceItem", Device)

class WinPrefetch(ObjectProperties):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.WindowsPrefetchObjectType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    _XSI_NS = "WinPrefetchObj"
    _XSI_TYPE = "WindowsPrefetchObjectType"

    application_file_name = cybox.TypedField("Application_File_Name", String)
    prefetch_hash = cybox.TypedField("Prefetch_Hash", String)
    times_executed = cybox.TypedField("Times_Executed", Long)
    first_run = cybox.TypedField("First_Run", DateTime)
    last_run = cybox.TypedField("Last_Run", DateTime)
    volume = cybox.TypedField("Volume", WinVolume)
    accessed_file_list = cybox.TypedField("Accessed_File_List", AccessedFileList)
    accessed_directory_list = cybox.TypedField("Accessed_Directory_List", AccessedDirectoryList)
