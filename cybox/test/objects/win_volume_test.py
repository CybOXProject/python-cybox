# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_volume_object import WinVolume, WindowsVolumeAttributesList
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestWinVolumeAttributesList(EntityTestCase, unittest.TestCase):
    klass = WindowsVolumeAttributesList

    _full_dict = [
        u('ReadOnly'),
        u('Hidden')
    ]


class TestWinVolume(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsVolumeObjectType"
    klass = WinVolume

    _full_dict = {
        'attributes_list': TestWinVolumeAttributesList._full_dict,
        'drive_letter': u('D'),
        'drive_type': u('DRIVE_REMOVABLE'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
