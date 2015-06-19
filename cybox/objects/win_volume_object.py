# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_volume_object as win_volume_binding
from cybox.objects.volume_object import Volume
from cybox.common import String


class WindowsVolumeAttributesList(entities.EntityList):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeAttributesListType
    _binding_var = "Attribute"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"


class WinVolume(Volume):
    _binding = win_volume_binding
    _binding_class = win_volume_binding.WindowsVolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#WinVolumeObject-2"
    _XSI_NS = "WinVolumeObj"
    _XSI_TYPE = "WindowsVolumeObjectType"

    attributes_list = fields.TypedField("Attributes_List", WindowsVolumeAttributesList)
    drive_letter = fields.TypedField("Drive_Letter", String)
    drive_Type = fields.TypedField("Drive_Type", String)
