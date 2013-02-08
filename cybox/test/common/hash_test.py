import unittest

from cybox.common.hash import Hash
from cybox.test.objects import round_trip


class TestHash(unittest.TestCase):

    def test_round_trip(self):
        m = "d41d8cd98f00b204e9800998ecf8427e"
        t = Hash.TYPE_MD5

        h = Hash()
        h.type_ = t
        h.simple_hash_value = m

        hash2 = round_trip(h, Hash, output=True)

        self.assertEqual(hash2.value, m)
        self.assertEqual(hash2.type_, t)

if __name__ == "__main__":
    unittest.main()

