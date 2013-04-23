import unittest

from cybox.common import StructuredText
import cybox.test


class TestStructuredText(unittest.TestCase):

    def test_round_trip(self):
        text = StructuredText()
        text.value = "<h1>A heading</h1>"
        text.structuring_format = "HTML"

        text2 = cybox.test.round_trip(text)
        self.assertEqual(text.to_dict(), text2.to_dict())

    def test_plain(self):
        text = StructuredText.from_dict("a string")

        text2 = cybox.test.round_trip(text)
        self.assertEqual(text.to_dict(), text2.to_dict())

        text_dict = {'value': "a string"}
        text3 = StructuredText.from_dict(text_dict)

        self.assertEqual(text.to_dict(), text3.to_dict())


if __name__ == "__main__":
    unittest.main()
