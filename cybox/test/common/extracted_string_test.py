# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import binascii
import unittest

from cybox.common import ExtractedString, Hash
from cybox.compat import str
from cybox.test import EntityTestCase

STRING = u"This is a string"
HEX_STRING = str(binascii.hexlify(STRING.encode("ascii")))

class TestExtractedString(EntityTestCase, unittest.TestCase):
    klass = ExtractedString

    _full_dict = {
        'encoding': u"UTF-8",
        'string_value': STRING,
        'byte_string_value': HEX_STRING,
        'hashes': [{'type': Hash.TYPE_MD5}],
        'address': u"1a2b",
        'length': len(STRING),
        'language': u"English",
        'english_translation': STRING,
    }


if __name__ == "__main__":
    unittest.main()
