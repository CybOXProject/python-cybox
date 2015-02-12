# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_mailslot_object import WinMailslot
from cybox.test.objects import ObjectTestCase


class TestWinMailslot(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsMailslotObjectType"
    klass = WinMailslot

    _full_dict = {
        'handle': {
            'name': "First Mailslot Handle",
            'type': "Mailslot",
            'xsi:type': "WindowsHandleObjectType",
        },
        'max_message_size': 1024,
        'name': "My Mailslot",
        'read_timeout': 2000,
        'security_attributes': "SecAttributes",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
