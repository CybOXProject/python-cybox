# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_pipe_object import WinPipe
from cybox.test.objects import ObjectTestCase


class TestWinPipe(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsPipeObjectType"
    klass = WinPipe

    _full_dict = {
        'name': u("pipe1"),
        'named': True,
        'default_time_out': 30,
        'handle': {
            'type': u("Pipe"),
            'object_address': 0xdeadbeef,
            'access_mask': 0x70000000,
            'pointer_count': 3,
            'xsi:type': "WindowsHandleObjectType",
        },
        'in_buffer_size': 1024,
        'max_instances': 10,
        'open_mode': "0000ffff",
        'out_buffer_size': 2048,
        'pipe_mode': "0000ccff",
        'security_attributes': u("SECRET!"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
