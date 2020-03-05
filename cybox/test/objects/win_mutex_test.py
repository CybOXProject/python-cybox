# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_mutex_object import WinMutex
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.win_handle_test import TestWinHandle


class TestWinMutex(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsMutexObjectType"
    klass = WinMutex

    _full_dict = {
        'handle': TestWinHandle._full_dict,
        'security_attributes': u("S-1-5-21-3623811015-3361044348-30300820-1013"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
