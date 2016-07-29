# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_prefetch_object as win_prefetch_binding
from cybox.objects.device_object import Device
from cybox.objects.win_volume_object import WinVolume
from cybox.common import String, DateTime, Long, ObjectProperties


class AccessedFileList(entities.EntityList):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.AccessedFileListType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    accessed_file = fields.TypedField("Accessed_File", String, multiple=True)


class AccessedDirectoryList(entities.EntityList):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.AccessedDirectoryListType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    accessed_directory = fields.TypedField("Accessed_Directory", String, multiple=True)


class Volume(entities.Entity):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.VolumeType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"

    volumeitem = fields.TypedField("VolumeItem", WinVolume, multiple=True)
    deviceitem = fields.TypedField("DeviceItem", Device, multiple=True)


class WinPrefetch(ObjectProperties):
    _binding = win_prefetch_binding
    _binding_class = win_prefetch_binding.WindowsPrefetchObjectType
    _namespace = "http://cybox.mitre.org/objects#WinPrefetchObject-2"
    _XSI_NS = "WinPrefetchObj"
    _XSI_TYPE = "WindowsPrefetchObjectType"

    application_file_name = fields.TypedField("Application_File_Name", String)
    prefetch_hash = fields.TypedField("Prefetch_Hash", String)
    times_executed = fields.TypedField("Times_Executed", Long)
    first_run = fields.TypedField("First_Run", DateTime)
    last_run = fields.TypedField("Last_Run", DateTime)
    volume = fields.TypedField("Volume", WinVolume)
    accessed_file_list = fields.TypedField("Accessed_File_List", AccessedFileList)
    accessed_directory_list = fields.TypedField("Accessed_Directory_List", AccessedDirectoryList)
