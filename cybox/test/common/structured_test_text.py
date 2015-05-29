# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import text_type, u

from cybox.common import StructuredText
import cybox.test


class TestStructuredText(cybox.test.EntityTestCase, unittest.TestCase):
    klass = StructuredText
    _full_dict = {
        'value': u("<html><p>WARNING \u26A0: Here is some structured text."),
        'structuring_format': "HTML",
    }

    def test_round_trip_manual(self):
        text = StructuredText()
        text.value = "some text"
        text.structuring_format = "plain"

        text2 = cybox.test.round_trip(text)
        self.assertEqual(text.to_dict(), text2.to_dict())

    def test_plain(self):
        text = StructuredText.from_dict("a string")

        text2 = cybox.test.round_trip(text)
        self.assertEqual(text.to_dict(), text2.to_dict())

        text_dict = {'value': "a string"}
        text3 = StructuredText.from_dict(text_dict)

        self.assertEqual(text.to_dict(), text3.to_dict())

    def test_unicode(self):
        text = self.klass.from_dict(self._full_dict)
        # This should not raise any errors
        self.assertTrue(b"WARNING" in text_type(text).encode('utf-8'))


if __name__ == "__main__":
    unittest.main()
