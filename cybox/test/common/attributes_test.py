import datetime
import unittest

from cybox.common.attributes import Attribute, String, Integer, DateTime
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
        self.assertRaises(NotImplementedError, a.to_obj)

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
        attr_dict = {
                        'value': "test_value",
                        'id': "test_a",
                        'idref': "test_b",
                        'datatype': "test_c",
                        'condition': "test_d",
                        'pattern_type': "test_e",
                        'regex_syntax': "test_f",
                        'start_range': "test_g",
                        'end_range': "test_h",
                        'value_set': ["test_i"],
                        'has_changed': "test_j",
                        'trend': "test_k",
                        'appears_random': "test_l",
                        'is_obfuscated': "test_m",
                        'obfuscation_algorithm_ref': "test_n",
                        'is_defanged': "test_o",
                        'defanging_algorithm_ref': "test_p",
                        'refanging_transform_type': "test_q",
                        'refanging_transform': "test_r",
                    }

        # Using `String` class explicity since the base `Attribute` class does
        # not define _get_binding_class()
        attr_obj = String.object_from_dict(attr_dict)
        attr_dict2 = String.dict_from_object(attr_obj)
        self.assertEqual(attr_dict, attr_dict2)

    def test_coerce_to_string(self):
        val = "abc1234"
        s = String(val)
        self.assertEqual(val, s.value)
        self.assertEqual(val, str(s))

    def test_coerce_to_int(self):
        val = 42
        i = Integer(val)
        self.assertEqual(val, i.value)
        self.assertEqual(val, int(i))


class TestDateTime(unittest.TestCase):

    def test_isodate(self):
        now = datetime.datetime.now()
        dt = DateTime(now)
        self.assertEqual(now.isoformat(), dt._serialize_value())

    def test_date_parse(self):
        dt = datetime.datetime(2012, 12, 31, 21, 13, 0)
        dt_str = "12-31-2012 09:13 PM"

        # Can build DateTime from a datetime
        cybox_dt = DateTime(dt)
        self.assertEqual(dt, cybox_dt.value)
        self.assertEqual(dt.isoformat(), str(cybox_dt))

        # Can build DateTime from a string
        cybox_dt2 = DateTime(dt_str)
        self.assertEqual(dt, cybox_dt2.value)
        self.assertEqual(dt.isoformat(), cybox_dt2._serialize_value())
        self.assertEqual(dt.isoformat(), str(cybox_dt2))


if __name__ == "__main__":
    unittest.main()
