# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_volume_object import UnixVolume
from cybox.test.objects import ObjectTestCase


class TestUnixVolume(ObjectTestCase, unittest.TestCase):
    object_type = "UnixVolumeObjectType"
    klass = UnixVolume

    _full_dict = {
        'is_mounted': True,
        'name': u('sda'),
        'mount_point': u('/boot/efi'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
