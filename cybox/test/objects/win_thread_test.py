# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_thread_object import WinThread
from cybox.test.objects import ObjectTestCase


class TestWinThread(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsThreadObjectType"
    klass = WinThread

    _full_dict = {
        'thread_id': 1234,
        'handle': {
                'name': u("Thread Handle"),
                'type': u("Thread"),
                'xsi:type': "WindowsHandleObjectType",
            },
        'running_status': u("Ready"),
        'context': u("My Context"),
        'priority': 15,
        'creation_flags': u("FFF0"),
        'creation_time': "2013-07-31T14:08:10+05:00",
        'start_address': u("00400000"),
        'parameter_address': u("01234567"),
        'security_attributes': u("Some Attributes"),
        'stack_size': 0x1000,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
