# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import date, datetime
import unittest

from cybox.common import DateWithPrecision, DateTimeWithPrecision
import cybox.test


class TestDateWithPrecision(cybox.test.EntityTestCase, unittest.TestCase):
    klass = DateWithPrecision
    _full_dict = {
        'value': "2014-01-01",
        'precision': 'month',
    }

    def test_shortcut_dict_representation(self):
        """If precision is the default value, to_dict should return a string"""
        date_str = "2013-11-17"
        d = DateWithPrecision()
        d.precision = "day"
        d.value = date_str

        self.assertEqual(str, type(d.to_dict()))
        self.assertEqual(date, type(d.value))
        self.assertEqual(date_str, d.to_dict())

        d2 = cybox.test.round_trip(d, output=True)
        self.assertEqual(d.to_dict(), d2.to_dict())

    def test_construction(self):
        d = DateWithPrecision()
        d.precision = "month"
        d.value = "2014-01-01"

        self.assertEqual(self._full_dict, d.to_dict())

class TestDateTimeWithPrecision(cybox.test.EntityTestCase, unittest.TestCase):
    klass = DateTimeWithPrecision
    _full_dict = {
        'value': "2014-02-04T08:21:33",
        'precision': 'hour',
    }

    def test_shortcut_dict_representation(self):
        """If precision is the default value, to_dict should return a string"""
        date_str = "2013-11-17T01:03:05"
        d = DateTimeWithPrecision()
        d.precision = "second"
        d.value = date_str

        self.assertEqual(str, type(d.to_dict()))
        self.assertEqual(datetime, type(d.value))
        self.assertEqual(date_str, d.to_dict())

        d2 = cybox.test.round_trip(d, output=True)
        self.assertEqual(d.to_dict(), d2.to_dict())

    def test_construction(self):
        d = DateTimeWithPrecision()
        d.precision = "hour"
        d.value = datetime(2014, 2, 4, 8, 21, 33)

        self.assertEqual(self._full_dict, d.to_dict())


if __name__ == "__main__":
    unittest.main()
