import unittest

from cybox.common.attributes import Attribute, String, Integer
from cybox.test import round_trip

class TestAttribute(unittest.TestCase):

    def test_plain(self):
        a = Attribute("test_value")
        self.assertTrue(a.is_plain())

    def test_string(self):
        s = String("test_string")
        self.assertTrue(s.datatype, "String")
        self.assertTrue(s.value, "test_string")

    def test_integer(self):
        i = Integer(42)
        self.assertTrue(i.datatype, "Integer")
        self.assertTrue(i.value, 42)

    def test_cannot_create_abstract_obj(self):
        a = Attribute()
        with self.assertRaises(NotImplementedError):
            a.to_obj()

    def test_valueset_single(self):
        value = "somevalue"
        a = Attribute()
        a.value_set = value
        self.assertEqual(len(a.value_set), 1)
        self.assertEqual(a.value_set, [value])

    def test_valueset_list(self):
        value = ['aaa', 'bbb', 'ccc']
        a = Attribute()
        a.value_set = value
        self.assertEqual(len(a.value_set), 3)
        self.assertEqual(a.value_set, ['aaa', 'bbb', 'ccc'])

    def test_valueset_delimited_string(self):
        value = "aaa,bbb,ccc"
        a = Attribute()
        a.value_set = value
        self.assertEqual(len(a.value_set), 3)
        self.assertEqual(a.value_set, ['aaa', 'bbb', 'ccc'])

    def test_valueset_trailing_delimiter(self):
        value = "aaa,bbb,ccc,"
        a = Attribute()
        a.value_set = value
        self.assertEqual(len(a.value_set), 4)
        self.assertEqual(a.value_set, ['aaa', 'bbb', 'ccc', ''])

    def test_round_trip(self):
        s = String()

        s.value = "test_value"
        s.id_ = "test_a"
        s.idref = "test_b"
        s.datatype = "test_c"
        s.condition = "test_d"
        s.pattern_type = "test_e"
        s.regex_syntax = "test_f"
        s.start_range = "test_g"
        s.end_range = "test_h"
        s.value_set = "test_i"
        s.has_changed = "test_j"
        s.trend = "test_k"
        s.appears_random = "test_l"
        s.is_obfuscated = "test_m"
        s.obfuscation_algorithm_ref = "test_n"
        s.is_defanged = "test_o"
        s.defanging_algorithm_ref = "test_p"
        s.refanging_transform_type = "test_q"
        s.refanging_transform = "test_r"

        s2 = round_trip(s, String, output=True)

        s_dict = s.to_dict()
        s2_dict = s2.to_dict()
        print s_dict
        print s2_dict
        self.assertEqual(s_dict, s2_dict)

if __name__ == "__main__":
    unittest.main()
