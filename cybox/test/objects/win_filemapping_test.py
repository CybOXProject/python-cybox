# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.win_filemapping_object import WinFilemapping
from cybox.test.objects import ObjectTestCase


class TestWinFilemapping(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsFilemappingObjectType"
    klass = WinFilemapping

    _full_dict = {
        'handle': {
            'id': 1234,
            'name': u("MyHandle"),
            'type': u("Window"),
            'object_address': long(0xdeadbeef),
            'access_mask': long(0x70000000),
            'pointer_count': long(3),
            'xsi:type': "WindowsHandleObjectType",
        },
        'file_handle': {
            'id': 5678,
            'name': u("MyHandle2"),
            'type': u("Window"),
            'object_address': long(0xbeadbeef),
            'access_mask': long(0x90009000),
            'pointer_count': long(9),
            'xsi:type': "WindowsHandleObjectType",
        },
        'security_attributes': u("Attributes go here"),
        'name': "A mapping name",
        'maximum_size': 1000,
        'actual_size': 250,
        'page_protection_value': "a protection value",
        'page_protection_attribute': [
            "a protection attribute",
            "another attribute"
        ],
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
