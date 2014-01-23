# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import VocabString
import cybox.test
from cybox.utils import normalize_to_xml


class TestVocabString(unittest.TestCase):

    def test_plain(self):
        a = VocabString("test_value")
        self.assertTrue(a.is_plain())

    def test_round_trip(self):
        vocab_dict = {
                        'value': "test_value",
                        'vocab_name': "test_a",
                        'vocab_reference': "test_b",

                        'condition': "test_d",
                        # Leave out apply_condition since value is not a list.
                        'bit_mask': "test_1",
                        'pattern_type': "test_e",
                        'regex_syntax': "test_f",
                        'has_changed': "test_j",
                        'trend': "test_k",
                     }

        vocab_dict2 = cybox.test.round_trip_dict(VocabString, vocab_dict)
        cybox.test.assert_equal_ignore(vocab_dict, vocab_dict2, ['xsi:type'])

    def test_round_trip_list(self):
        vocab_dict = {
                        'value': ['Value1', 'Value2', 'Value3'],
                        'condition': "Equals",
                        'apply_condition': "ALL",
                     }

        vocab_dict2 = cybox.test.round_trip_dict(VocabString, vocab_dict)
        cybox.test.assert_equal_ignore(vocab_dict, vocab_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
