# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.semaphore_object import Semaphore
from cybox.test.objects import ObjectTestCase


class TestSemaphore(ObjectTestCase, unittest.TestCase):
    object_type = "SemaphoreObjectType"
    klass = Semaphore

    _full_dict = {
        'named': False,
        'current_count': 100,
        'maximum_count': 250,
        'name': "A Test",
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
