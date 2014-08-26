# -*- coding: utf-8 -*-
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

from cybox.common import Contributor, String, MeasureSource
from cybox.core import Observable
from cybox.objects.code_object import Code, CodeSegmentXOR
from cybox.objects.whois_object import WhoisEntry
from cybox.test import round_trip

UNICODE_STR = u"❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂"


class EncodingTests(unittest.TestCase):
    """Tests for the cybox.utils.IDGenerator class."""

    def test_double_encode(self):
        s = String(UNICODE_STR)
        s2 = round_trip(s)

    def test_contributor(self):
        c = Contributor()
        c.name = UNICODE_STR
        c.role = UNICODE_STR
        c.email = UNICODE_STR
        c.phone = UNICODE_STR
        c.organization = UNICODE_STR
        c2 = round_trip(c)

    def test_observable(self):
        o = Observable()
        o.title = UNICODE_STR
        o2 = round_trip(o)

    def test_code(self):
        cs = Code()
        cs.code_segment_xor = CodeSegmentXOR()
        cs.code_segment_xor.xor_pattern = UNICODE_STR
        cs2 = round_trip(cs)
        self.assertEqual(cs.to_dict(), cs2.to_dict())

    def test_measure_source(self):
        o = MeasureSource()
        o.name = UNICODE_STR
        o2 = round_trip(o)

    def test_whois(self):
        o = WhoisEntry()
        o.dnssec = UNICODE_STR
        o2 = round_trip(o)


if __name__ == "__main__":
    unittest.main()
