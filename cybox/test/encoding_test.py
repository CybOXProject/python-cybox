# -*- coding: utf-8 -*-
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

from mixbox.vendor import six
from mixbox.vendor.six import u

from cybox.common import Contributor, String, MeasureSource
from cybox.core import Observable
from cybox.objects.code_object import Code, CodeSegmentXOR
from cybox.objects.whois_object import WhoisEntry
from cybox.test import round_trip

#UNICODE_STR = six.u("❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂")
if six.PY2:
    UNICODE_STR = u(r'\u2764 \u264e \u2600 \u2605 \u2602 \u265e \u262f \
        \u262d \u2622 \u20ac\u260e\u2691 \u2744\u266b\u2702')
else:
    UNICODE_STR = '\u2764 \u264e \u2600 \u2605 \u2602 \u265e \u262f \
        \u262d \u2622 \u20ac\u260e\u2691 \u2744\u266b\u2702'

class EncodingTests(unittest.TestCase):

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

    def test_to_xml_utf16_encoded(self):
        encoding = 'utf-16'
        o = Observable()
        o.title = UNICODE_STR
        xml = o.to_xml(encoding=encoding)
        self.assertTrue(UNICODE_STR in xml.decode(encoding))

    def test_to_xml_default_encoded(self):
        o = Observable()
        o.title = UNICODE_STR
        xml = o.to_xml()
        self.assertTrue(UNICODE_STR in xml.decode('utf-8'))

    def test_to_xml_no_encoding(self):
        o = Observable()
        o.title = UNICODE_STR
        xml = o.to_xml(encoding=None)
        self.assertTrue(isinstance(xml, six.text_type))
        self.assertTrue(UNICODE_STR in xml)

if __name__ == "__main__":
    unittest.main()
