# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.library_object import Library
from cybox.test.objects import ObjectTestCase


class TestLibrary(ObjectTestCase, unittest.TestCase):
    object_type = "LibraryObjectType"
    klass = Library

    _full_dict = {
        'name': u('libc'),
        'path': u('/lib/x86_64-linux-gnu/'),
        'size': 28000,
        'type': u('Dynamic'),
        'version': u('2.19'),
        'base_address': u('0x7ffff7bcf000'),
        # 'extracted_features': '',
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
