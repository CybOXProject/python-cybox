# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import datetime
import unittest

from cybox.common import (BaseProperty, DateTime, Integer, Long,
        PositiveInteger, String, UnsignedLong, BINDING_CLASS_MAPPING)
import cybox.test
from cybox.utils import normalize_to_xml


class TestBaseProperty(unittest.TestCase):

    def test_create_all(self):
        for PropertyClass in BINDING_CLASS_MAPPING.values():
            prop = PropertyClass()

    def test_plain(self):
        a = BaseProperty("test_value")
        self.assertTrue(a.is_plain())

    def test_string(self):
        s = String("test_string")
        self.assertEqual(s.datatype, "string")
        self.assertEqual(s.value, "test_string")

    def test_string_with_comma(self):
        s = String("test_string,")
        s2 = cybox.test.round_trip(s)
        self.assertEqual(s, s2)

    def test_list_of_strings_with_comma(self):
        s = String([u"string,1", u"string,1", u"string,3"])
        s2 = cybox.test.round_trip(s)
        self.assertEqual(s, s2)

    def test_integer(self):
        i = Integer(42)
        self.assertEqual(i.datatype, "integer")
        self.assertEqual(i.value, 42)

    def test_unicode_string(self):
        s = u"A Unicode \ufffd string"
        string = String(s)
        self.assertEqual(s, unicode(string))
        self.assertEqual(s.encode("utf-8"), str(string))

    def test_cannot_create_abstract_obj(self):
        a = BaseProperty()
        self.assertRaises(AttributeError, a.to_obj)

    def test_conditions_equal(self):
        a = BaseProperty()
        b = BaseProperty()
        self.assertEqual(a.condition, None)
        self.assertEqual(b.condition, None)
        self.assertTrue(BaseProperty._conditions_equal(a, b))

        a.condition = "Equals"
        # a.condition = "Equals", b.condition = None
        self.assertFalse(BaseProperty._conditions_equal(a, b))

        b.condition = "Equals"
        # a.condition = "Equals", b.condition = "Equals"
        self.assertTrue(BaseProperty._conditions_equal(a, b))

        a.apply_condition = "ALL"
        # a.apply_condition = "ALL", b.apply_condition = None
        self.assertFalse(BaseProperty._conditions_equal(a, b))

        a.apply_condition = "ANY"
        # a.apply_condition = "ANY", b.apply_condition = None
        self.assertTrue(BaseProperty._conditions_equal(a, b))

        b.apply_condition = "ALL"
        # a.apply_condition = "ANY", b.apply_condition = "ALL"
        self.assertFalse(BaseProperty._conditions_equal(a, b))

        a.apply_condition = "ALL"
        # a.apply_condition = "ALL", b.apply_condition = "ALL"
        self.assertTrue(BaseProperty._conditions_equal(a, b))

    def test_round_trip(self):
        prop_dict = {
                        'value': "test_value",
                        'id': "test_a",
                        'idref': "test_b",
        # TODO: Make this pass
        #                'datatype': "test_c",
                        'appears_random': "test_l",
                        'is_obfuscated': "test_m",
                        'obfuscation_algorithm_ref': "test_n",
                        'is_defanged': "test_o",
                        'defanging_algorithm_ref': "test_p",
                        'refanging_transform_type': "test_q",
                        'refanging_transform': "test_r",

                        'condition': "Equals",
                        # Take out apply_condition since 'value' is not a list.
                        #'apply_condition': "test_0",
                        'bit_mask': "test_1",
                        'pattern_type': "test_e",
                        'regex_syntax': "test_f",
                        'has_changed': "test_j",
                        'trend': "test_k",
                    }

        # Using `String` class explicity since the `BaseProperty` class does
        # not define _binding_class
        prop_dict2 = cybox.test.round_trip_dict(String, prop_dict)
        self.assertEqual(prop_dict, prop_dict2)

    def test_round_trip_list(self):
        prop_dict = {
                        'value': ['alpha', 'beta', 'gamma'],
                        'condition': "Equals",
                        'apply_condition': "ALL",
                    }
        prop_dict2 = cybox.test.round_trip_dict(String, prop_dict)
        self.assertEqual(prop_dict, prop_dict2)

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

    def test_numerics(self):
        p = PositiveInteger(42)
        p2 = cybox.test.round_trip(p)
        self.assertEqual(p.to_dict(), p2.to_dict())

        i = Integer(42)
        i2 = cybox.test.round_trip(i)
        self.assertEqual(i.to_dict(), i2.to_dict())

        u = UnsignedLong(42)
        u2 = cybox.test.round_trip(u)
        self.assertEqual(u.to_dict(), u2.to_dict())

        u3 = UnsignedLong("42")
        self.assertEqual(u3.value, 42)
        self.assertNotEqual(u3.value, "42")
        self.assertEqual(u3.to_dict(), u.to_dict())

    def test_list_numerics(self):
        i = Integer([1, 2, 3])
        i2 = Integer.from_dict({'value': ['1', '2', '3']})
        self.assertEqual(i.to_dict(), i2.to_dict())


class TestHexadecimal(unittest.TestCase):

    def test_parse_int(self):
        self._test_class(Integer)

    def test_parse_long(self):
        self._test_class(Long)

    def test_parse_unsigned_long(self):
        self._test_class(UnsignedLong)

    def _test_class(self, cls):
        i = cls(0xdeadbeef)
        i2 = cls(3735928559)
        i3 = cls('0xdeadbeef')
        i4 = cls('3735928559')

        self.assertEqual(i, i2)
        self.assertEqual(i, i3)
        self.assertEqual(i, i4)


class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.dt = datetime.datetime(2012, 12, 31, 21, 13, 0)
        self.dt_str = "12-31-2012 09:13 PM"

    def test_isodate(self):
        now = datetime.datetime.now()
        dt = DateTime(now)
        self.assertEqual(now.isoformat(), dt.serialized_value)

    def test_parse_datetime(self):
        cybox_dt = DateTime(self.dt)
        self.assertEqual(self.dt, cybox_dt.value)
        self.assertEqual(self.dt.isoformat(), str(cybox_dt))

    def test_parse_date_string(self):
        cybox_dt2 = DateTime(self.dt_str)
        self.assertEqual(self.dt, cybox_dt2.value)
        self.assertEqual(self.dt.isoformat(), cybox_dt2.serialized_value)
        self.assertEqual(self.dt.isoformat(), str(cybox_dt2))

    def test_list_dates(self):
        dt = DateTime([self.dt, self.dt, self.dt])
        self.assertEqual(3, len(dt.value))
        expected = "{0},{0},{0}".format(self.dt.isoformat())
        actual = normalize_to_xml(dt.serialized_value)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
