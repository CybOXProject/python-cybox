# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_handle_object import WinHandle
from cybox.test.objects import ObjectTestCase


class TestWinHandle(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsHandleObjectType"
    klass = WinHandle

    _full_dict = {
        'id': 1234,
        'name': "MyHandle",
        'type': "Window",
        'object_address': 0xdeadbeef,
        'access_mask': 0x70000000,
        'pointer_count': 3,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
