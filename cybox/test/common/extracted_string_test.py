# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import ExtractedString, Hash
from cybox.test import EntityTestCase

STRING = u"This is a string"

class TestExtractedString(EntityTestCase, unittest.TestCase):
    klass = ExtractedString

    _full_dict = {
        'encoding': u"UTF-8",
        'string_value': STRING,
        'byte_string_value': unicode(STRING.encode('hex')),
        'hashes': [{'type': Hash.TYPE_MD5}],
        'address': u"1a2b",
        'length': len(STRING),
        'language': u"English",
        'english_translation': STRING,
    }


if __name__ == "__main__":
    unittest.main()
