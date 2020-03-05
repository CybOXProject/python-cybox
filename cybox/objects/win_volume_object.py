# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.win_volume_object as win_volume_binding
from cybox.objects.volume_object import Volume
from cybox.common import BaseProperty, String


class WindowsDrive(BaseProperty):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsDriveType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"

    TYPE_DRIVE_UNKNOWN = "DRIVE_UNKNOWN"
    TYPE_DRIVE_NO_ROOT_DIR = "DRIVE_NO_ROOT_DIR"
    TYPE_DRIVE_REMOVABLE = "DRIVE_REMOVABLE"
    TYPE_DRIVE_FIXED = "DRIVE_FIXED"
    TYPE_DRIVE_REMOTE = "DRIVE_REMOTE"
    TYPE_DRIVE_CDROM = "DRIVE_CDROM"
    TYPE_DRIVE_RAMDISK = "DRIVE_RAMDISK"


class WindowsVolumeAttribute(BaseProperty):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeAttributeType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"

    TYPE_READ_ONLY = "ReadOnly"
    TYPE_HIDDEN = "Hidden"
    TYPE_NO_DEFAULT_DRIVE_LETTER = "NoDefaultDriveLetter"
    TYPE_SHADOW_COPY = "ShadowCopy"


class WindowsVolumeAttributesList(entities.EntityList):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeAttributesListType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"

    attribute = fields.TypedField("Attribute", WindowsVolumeAttribute, multiple=True)


class WinVolume(Volume):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"
    _XSI_NS = "WinVolumeObj"
    _XSI_TYPE = "WindowsVolumeObjectType"

    attributes_list = fields.TypedField("Attributes_List", WindowsVolumeAttributesList)
    drive_letter = fields.TypedField("Drive_Letter", String)
    drive_type = fields.TypedField("Drive_Type", WindowsDrive)
