# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.unix_volume_object as unix_volume_binding
from cybox.objects.volume_object import Volume
from cybox.common import String


class UnixVolume(Volume):
    _binding = unix_volume_binding
    _binding_class = unix_volume_binding.UnixVolumeObjectType
    _namespace = "http://cybox.mitre.org/objects#UnixVolumeObject-2"
    _XSI_NS = "UnixVolumeObj"
    _XSI_TYPE = "UnixVolumeObjectType"

    mount_point = fields.TypedField("Mount_Point", String)
    options = fields.TypedField("Options", String)
