# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.win_semaphore_object import WinSemaphore
from cybox.test.objects import ObjectTestCase


class TestWinSemaphore(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsSemaphoreObjectType"
    klass = WinSemaphore

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
        'security_attributes': u("Attributes go here"),
        'named': False,
        'current_count': 100,
        'maximum_count': 250,
        'name': u("A Test"),
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
