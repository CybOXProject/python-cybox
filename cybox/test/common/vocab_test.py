import unittest

from cybox.common.vocabs import VocabString
import cybox.test
from cybox.utils import normalize_to_xml


class TestVocabString(unittest.TestCase):

    def test_plain(self):
        a = VocabString("test_value")
        self.assertTrue(a.is_plain())

    def test_round_trip(self):
        attr_dict = {
                        'value': "test_value",
                        'vocab_name': "test_a",
                        'vocab_reference': "test_b",

                        'condition': "test_d",
                        'apply_condition': "test_0",
                        'bit_mask': "test_1",
                        'pattern_type': "test_e",
                        'regex_syntax': "test_f",
                        'has_changed': "test_j",
                        'trend': "test_k",
                    }

        attr_obj = VocabString.object_from_dict(attr_dict)
        attr_dict2 = VocabString.dict_from_object(attr_obj)
        cybox.test.assert_equal_ignore(attr_dict, attr_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
