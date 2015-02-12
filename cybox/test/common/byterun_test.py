# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import ByteRun, ByteRuns, Hash
import cybox.test
from cybox.test import EntityTestCase


class TestByteRun(EntityTestCase, unittest.TestCase):
    klass = ByteRun

    _full_dict = {
        'offset': 1000,
        'file_system_offset': 1024,
        'image_offset': 512,
        'length': 10,
        'hashes': [{'type': Hash.TYPE_MD5,
                    'simple_hash_value':
                        '0123456789abcdef0123456789abcdef'}],
        'byte_run_data': "helloworld",
    }


class TestByteRuns(unittest.TestCase):

    def test_round_trip(self):
        byteruns_list = [
                        {'byte_run_data': "a",
                         'length': 1},
                        {'byte_run_data': "blahblah",
                         'length': 8},
                        {'byte_run_data': "aeiou",
                         'length': 5},
                      ]
        byteruns_list2 = cybox.test.round_trip_list(ByteRuns, byteruns_list)
        self.assertEqual(byteruns_list, byteruns_list2)

if __name__ == "__main__":
    unittest.main()
