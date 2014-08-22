# -*- coding: utf-8 -*-
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

from cybox.common import Contributor, String
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
        c.to_xml()
        raise ValueError


if __name__ == "__main__":
    unittest.main()
