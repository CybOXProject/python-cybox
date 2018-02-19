# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Location
import cybox.test


class TestLocation(cybox.test.EntityTestCase, unittest.TestCase):
    klass = Location
    _full_dict = {
        'name': "Bedford, MA",
        'id': "example:12345",
    }
