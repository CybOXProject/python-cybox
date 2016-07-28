# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import datetime
import unittest

from mixbox.vendor import six
from mixbox.vendor.six import u

from cybox.common import (BaseProperty, DateTime, Integer, Long,
        NonNegativeInteger, PositiveInteger, String, UnsignedInteger,
        UnsignedLong, BINDING_CLASS_MAPPING, DEFAULT_DELIM)
import cybox.test
from cybox.utils import normalize_to_xml


NUMERIC_TYPES = (Integer, PositiveInteger, UnsignedInteger, NonNegativeInteger,
                 Long, UnsignedLong)


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
        s = String([u("string,1"), u("string,1"), u("string,3")])
        s2 = cybox.test.round_trip(s)
        self.assertEqual(s, s2)

    def test_delimiter(self):
        s = String(["string1", "string2"])
        s.delimiter = "##delim##"
        self.assertTrue(b"##comma##" not in s.to_xml())
        self.assertTrue(b"string1##delim##string2" in s.to_xml())

    def test_integer(self):
        i = Integer(42)
        self.assertEqual(i.datatype, "int")
        self.assertEqual(i.value, 42)

    def test_unicode_string(self):
        s = u("A Unicode \ufffd string")
        string = String(s)

        unicode_string = six.text_type(string)
        self.assertEqual(s, unicode_string)
        self.assertEqual(s.encode("utf-8"), unicode_string.encode("utf-8"))
        self.assertTrue(s.encode("utf-8") in string.to_xml())

    # def test_cannot_create_abstract_obj(self):
    #     a = BaseProperty()
    #     self.assertRaises(AttributeError, a.to_obj)

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
        # Cannot have an id and idref set at the same time.,
                        # 'idref': "test_b",
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
        self.assertEqual(val, six.text_type(s))

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

    def test_values(self):
        i = Integer()
        self.assertEqual([], i.values)

        i = Integer(1)
        self.assertEqual([1], i.values)

        i = Integer([2])
        self.assertEqual([2], i.values)

        i = Integer([3, 4])
        self.assertEqual([3, 4], i.values)


class TestEmptyNumerics(unittest.TestCase):

    def test_empty_numeric_value(self):
        # Integer, Long, UnsignedLong, PositiveInteger

        for cls in NUMERIC_TYPES:
            # Rather than importing from cybox.bindings directly, just
            # reference the corresponding _binding_class.
            binding_obj = cls._binding_class()

            # Set value to an empty string
            binding_obj.valueOf_ = ''

            obj = cls.from_obj(binding_obj)

            self.assertTrue(obj.value is None)


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
        self.assertEqual(now.isoformat(), dt.to_obj().valueOf_)

    def test_parse_datetime(self):
        cybox_dt = DateTime(self.dt)
        self.assertEqual(self.dt, cybox_dt.value)
        self.assertEqual(self.dt.isoformat(), six.text_type(cybox_dt))

    def test_parse_date_string(self):
        cybox_dt2 = DateTime(self.dt_str)
        self.assertEqual(self.dt, cybox_dt2.value)
        self.assertEqual(self.dt.isoformat(), cybox_dt2.serialized_value)
        self.assertEqual(self.dt.isoformat(), six.text_type(cybox_dt2))

    def test_list_dates(self):
        dt = DateTime([self.dt, self.dt, self.dt])
        self.assertEqual(3, len(dt.value))
        expected = "{0}{1}{0}{1}{0}".format(self.dt.isoformat(), DEFAULT_DELIM)
        actual = normalize_to_xml(dt.serialized_value, DEFAULT_DELIM)
        self.assertEqual(expected, actual)


class TestApplyCondition(unittest.TestCase):
    """Make sure that the @apply_condition attribute is set at the right times.

    If the @condition attribute is set, meaning it is part of a pattern, and
    the value is a list, the @apply_condition should be set, even if it is
    the default value ("ANY").
    """

    def test_instance_single(self):
        s = String("foo")
        # @apply_condition should not be set on instances.
        self.assertFalse(b'apply_condition' in s.to_xml())

    def test_instance_multiple(self):
        s = String(["foo", "bar", "baz"])
        # @apply_condition should not be set on instances.
        self.assertFalse(b'apply_condition' in s.to_xml())

    def test_instance_multiple_all(self):
        s = String(["foo", "bar", "baz"])
        s.apply_condition = "ALL"
        # Even though we set it, this is not a pattern so @apply_condition
        # shouldn't be output.
        self.assertFalse(b'apply_condition' in s.to_xml())

    def test_pattern_single(self):
        s = String("foo")
        s.condition = "Equals"
        # @apply_condition should not be set if the value is not a list.
        self.assertFalse(b'apply_condition' in s.to_xml())

    def test_pattern_multiple(self):
        s = String(["foo", "bar", "baz"])
        s.condition = "Equals"
        # @apply_condition should be set when there is a @condition and the
        # value is a list.
        self.assertTrue(b'apply_condition="ANY"' in s.to_xml())

    def test_pattern_multiple_all(self):
        s = String(["foo", "bar", "baz"])
        s.condition = "Equals"
        s.apply_condition = "ALL"
        # If we change @apply_condition from the default, it should match
        # that value.
        self.assertTrue(b'apply_condition="ALL"' in s.to_xml())

if __name__ == "__main__":
    unittest.main()
