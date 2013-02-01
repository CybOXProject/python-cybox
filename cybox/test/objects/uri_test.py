import unittest

from cybox.objects.uri_object import Uri
from cybox.test.objects import round_trip


class TestUri(unittest.TestCase):

    def test_round_trip(self):
        v = "http://www.example.com"
        t = Uri.TYPE_URL

        u = Uri()
        u.value = v
        u.type_ = t

        uri2 = round_trip(u, Uri, output=False)

        self.assertEqual(uri2.value, v)
        self.assertEqual(uri2.type_, t)

if __name__ == "__main__":
    unittest.main()
