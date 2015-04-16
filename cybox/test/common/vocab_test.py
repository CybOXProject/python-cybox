# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import HashName, VocabString
from cybox.common.vocabs import HashName
import cybox.test
from cybox.utils import normalize_to_xml


class TestVocabString(unittest.TestCase):

    def test_plain(self):
        a = VocabString("test_value")
        self.assertTrue(a.is_plain())

    def test_is_plain_hashname(self):
        md5 = HashName("MD5")
        self.assertTrue(md5.is_plain())

    def test_is_plain_hashname(self):
        md5 = HashName("MD5")
        md5.xsi_type = "Some Other xsi:type"
        self.assertFalse(md5.is_plain())

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

    # https://github.com/CybOXProject/python-cybox/issues/158
    def test_xsi_type_unicode(self):
        string = u"test\u2010value"
        vocab_dict = {
                        'value': string,
                        'condition': u"Equals",
                        'xsi:type': u"some_xsi_type",
                     }

        vocab_dict2 = cybox.test.round_trip_dict(VocabString, vocab_dict)
        self.assertEqual(vocab_dict, vocab_dict2)
        xml = VocabString.from_dict(vocab_dict).to_xml()
        string_utf8 = string.encode("utf-8")
        self.assertTrue(string_utf8 in xml)

    def test_round_trip_list(self):
        vocab_dict = {
                        'value': ['Value1', 'Value2', 'Value3'],
                        'condition': "Equals",
                        'apply_condition': "ALL",
                        'vocab_name': "Test",
                     }

        vocab_dict2 = cybox.test.round_trip_dict(VocabString, vocab_dict)
        cybox.test.assert_equal_ignore(vocab_dict, vocab_dict2, ['xsi:type'])

    def test_add_bad_value(self):
        from cybox.common import Hash

        h = Hash()
        self.assertRaises(
            ValueError,
            setattr,
            h,
            'type_',
            "BAD VALUE"
        )

    def test_add_vocabstring(self):
        from cybox.common import Hash
        from cybox.common.vocabs import ActionName

        action = ActionName(ActionName.TERM_ADD_USER)
        h = Hash()
        h.type_ = action

        self.assertEqual(action, h.type_)

    def test_to_dict(self):
        from cybox.common.vocabs import ActionName
        d = ActionName(ActionName.TERM_ADD_USER).to_dict()
        self.assertEqual(d['xsi:type'], ActionName._XSI_TYPE)
        self.assertEqual(d['value'], ActionName.TERM_ADD_USER)


class HashNameTests(unittest.TestCase):

    def test_hash_name_vocabulary(self):
        # Test for using the @add_allowed_values decorator.
        self.assertEqual(8, len(HashName._ALLOWED_VALUES))


if __name__ == "__main__":
    unittest.main()
