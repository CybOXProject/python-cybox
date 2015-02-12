# -*- coding: utf-8 -*-
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

import cybox.bindings as bindings
from cybox.common import Contributor, String, MeasureSource
from cybox.core import Observable
from cybox.objects.code_object import Code, CodeSegmentXOR
from cybox.objects.whois_object import WhoisEntry
from cybox.test import round_trip

UNICODE_STR = u"❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂"


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

    def test_quote_xml(self):
        s = bindings.quote_xml(UNICODE_STR)
        self.assertEqual(s, UNICODE_STR)

    def test_quote_attrib(self):
        """Tests that the stix.bindings.quote_attrib method works properly
        on unicode inputs.

        Note:
            The quote_attrib method (more specifically, saxutils.quoteattr())
            adds quotation marks around the input data, so we need to strip
            the leading and trailing chars to test effectively
        """
        s = bindings.quote_attrib(UNICODE_STR)
        s = s[1:-1]
        self.assertEqual(s, UNICODE_STR)

    def test_quote_attrib_int(self):
        i = 65536
        s = bindings.quote_attrib(i)
        self.assertEqual(u'"65536"', s)

    def test_quote_attrib_bool(self):
        b = True
        s = bindings.quote_attrib(b)
        self.assertEqual(u'"True"', s)

    def test_quote_xml_int(self):
        i = 65536
        s = bindings.quote_xml(i)
        self.assertEqual(unicode(i), s)

    def test_quote_xml_bool(self):
        b = True
        s = bindings.quote_xml(b)
        self.assertEqual(unicode(b), s)

    def test_quote_xml_encoded(self):
        encoding = bindings.ExternalEncoding
        encoded = UNICODE_STR.encode(encoding)
        quoted = bindings.quote_xml(encoded)
        self.assertEqual(UNICODE_STR, quoted)

    def test_quote_attrib_encoded(self):
        encoding = bindings.ExternalEncoding
        encoded = UNICODE_STR.encode(encoding)
        quoted = bindings.quote_attrib(encoded)[1:-1]
        self.assertEqual(UNICODE_STR, quoted)

    def test_quote_xml_zero(self):
        i = 0
        s = bindings.quote_xml(i)
        self.assertEqual(unicode(i), s)

    def test_quote_attrib_zero(self):
        i = 0
        s = bindings.quote_attrib(i)
        self.assertEqual(u'"0"', s)

    def test_quote_xml_none(self):
        i = None
        s = bindings.quote_xml(i)
        self.assertEqual(u'', s)

    def test_quote_attrib_none(self):
        i = None
        s = bindings.quote_attrib(i)
        self.assertEqual(u'""', s)

    def test_quote_attrib_empty(self):
        i = ''
        s = bindings.quote_attrib(i)
        self.assertEqual(u'""', s)

    def test_quote_xml_empty(self):
        i = ''
        s = bindings.quote_xml(i)
        self.assertEqual(u'', s)

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
        self.assertTrue(isinstance(xml, unicode))
        self.assertTrue(UNICODE_STR in xml)

if __name__ == "__main__":
    unittest.main()
