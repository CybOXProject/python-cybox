# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_mailslot_object import WinMailslot
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestWinMailslot(unittest.TestCase, ObjectTestCase):
    object_type = "WindowsMailslotObjectType"
    klass = WinMailslot

    def test_round_trip(self):
        slot_dict = {
                        'handle': [
                            {
                                'name': "First Mailslot Handle",
                                'type': "Mailslot",
                                'xsi:type': "WindowsHandleObjectType",
                            },
                            {
                                'name': "Second Mailslot Handle",
                                'xsi:type': "WindowsHandleObjectType",
                            },
                        ],
                        'max_message_size': 1024,
                        'name': "My Mailslot",
                        'read_timeout': 2000,
                        'security_attributes': "SecAttributes",
                        'xsi:type': "WindowsMailslotObjectType",
                    }
        slot_dict2 = cybox.test.round_trip_dict(WinMailslot, slot_dict)
        self.maxDiff = None
        self.assertEqual(slot_dict, slot_dict2)


if __name__ == "__main__":
    unittest.main()
