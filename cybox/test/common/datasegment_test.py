# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import DataSegment
import cybox.test
from cybox.test import EntityTestCase


class TestByteRun(EntityTestCase, unittest.TestCase):
    klass = DataSegment

    _full_dict = {
        'data_format': "Hexadecimal",
        'data_size': {"value": '20', 'units': "Bytes"},
        'data_segment': '0001020304050607080910111213141516171819',
        'offset': 42,
        'search_distance': 100,
        'search_within': 50,
    }


if __name__ == "__main__":
    unittest.main()
