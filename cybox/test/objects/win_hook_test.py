# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_hook_object import WinHook

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinHook(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsHookObjectType"
    klass = WinHook

    _full_dict = {
        'type': u("Test Hook"),
        #TODO: add 'handle'
        'hooking_function_name': u("test_function"),
        #TODO: add 'hooking_module'
        'thread_id': 2,
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
