# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_pipe_object import UnixPipe
from cybox.test.objects import ObjectTestCase


class TestUnixPipe(ObjectTestCase, unittest.TestCase):
    object_type = "UnixPipeObjectType"
    klass = UnixPipe

    _full_dict = {
        'name': u("unix-pipe1"),
        'permission_mode': "0000ccff",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
