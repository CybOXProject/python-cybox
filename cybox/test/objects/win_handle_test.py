# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_handle_object import WinHandle
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestWinHandle(unittest.TestCase, ObjectTestCase):
    object_type = "WindowsHandleObjectType"
    klass = WinHandle

    def test_round_trip(self):
        handle_dict = {
                        'id': 1234,
                        'name': "MyHandle",
                        'type': "Window",
                        'object_address': 0xdeadbeef,
                        'access_mask': 0x70000000,
                        'pointer_count': 3,
                        'xsi:type': 'WindowsHandleObjectType'
                      }
        handle_dict2 = cybox.test.round_trip_dict(WinHandle, handle_dict)
        self.assertEqual(handle_dict, handle_dict2)


if __name__ == "__main__":
    unittest.main()
