# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.pipe_object import Pipe
from cybox.test.objects import ObjectTestCase


class TestPipe(ObjectTestCase, unittest.TestCase):
    object_type = "PipeObjectType"
    klass = Pipe

    _full_dict = {
        'name': u("pipe1"),
        'named': True,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
