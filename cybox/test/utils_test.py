# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import DEFAULT_DELIM as DELIM
import cybox.utils


class NormalizationTest(unittest.TestCase):

    def test_encode_decode_lists(self):
        a = "A long##comma##long##comma##time ago"
        b = ["A long", "long", "time ago"]

        self.assertEqual(cybox.utils.denormalize_from_xml(a, DELIM), b)
        self.assertEqual(cybox.utils.normalize_to_xml(b, DELIM), a)

    def test_delimiter_not_allowed_in_value(self):
        string = "test string with a ##comma## in it"
        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          string, DELIM)

    def test_normalize_string_with_nondefault_delimiter(self):
        s = cybox.utils.normalize_to_xml([1, 2, 3], ",")
        self.assertEqual("1,2,3", s)

        s = cybox.utils.normalize_to_xml([1, 2, 3], "-")
        self.assertEqual("1-2-3", s)

        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          [1, 2, 3], "1")

        s = cybox.utils.normalize_to_xml(['a', 'b', 'c'], ",")
        self.assertEqual("a,b,c", s)

        self.assertRaises(ValueError, cybox.utils.normalize_to_xml,
                          ['a,b', 'b,c', 'c,d'], ",")


class TestDictCache(unittest.TestCase):

    def test_id_incrementing(self):
        d = cybox.utils.DictCache()
        self.assertEqual(0, d.put("a"))
        self.assertEqual(1, d.put("b"))
        self.assertEqual(3, d.put("c", 3))
        self.assertEqual(2, d.put("d"))
        self.assertEqual(4, d.put("e"))

    def test_id_incrementing(self):
        d = cybox.utils.DictCache()
        self.assertEqual(0, d.count())

        d.put("a")
        d.put("b")
        d.put("c")
        self.assertEqual(3, d.count())

        d.clear()
        self.assertEqual(0, d.count())

if __name__ == "__main__":
    unittest.main()
