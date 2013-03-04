import unittest

from cybox.common.attributes import HashName, SimpleHashValue
from cybox.common.hash import Hash, HashList
from cybox.test import round_trip

EMPTY_MD5 = 'd41d8cd98f00b204e9800998ecf8427e'
EMPTY_SHA1 = 'adc83b19e793491b1c6ea0fd8b46cd9f32e592fc'
EMPTY_SHA256 = \
        '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'


class TestHash(unittest.TestCase):

    def test_autotype_md5(self):
        """32-character hash is assumed to be MD5"""
        h = Hash(EMPTY_MD5)
        self.assertEqual(h.type_, Hash.TYPE_MD5)

    def test_autotype_sha1(self):
        """40-character hash is assumed to be SHA-1"""
        h = Hash(EMPTY_SHA1)
        self.assertEqual(h.type_, Hash.TYPE_SHA1)

    def test_autotype_sha256(self):
        """64-character hash is assumed to be SHA-256"""
        h = Hash(EMPTY_SHA256)
        self.assertEqual(h.type_, Hash.TYPE_SHA256)

    def test_autotype_other(self):
        """Hash of unknown length is assigned TYPE_OTHER"""
        h = Hash("0123456789abcdef")
        self.assertEqual(h.type_, Hash.TYPE_OTHER)

    def test_round_trip(self):
        v = SimpleHashValue(EMPTY_MD5)
        t = HashName(Hash.TYPE_MD5)

        h = Hash(v, t)

        hash2 = round_trip(h, Hash, output=True)

        self.assertEqual(hash2.simple_hash_value, v)
        self.assertEqual(hash2.type_, t)

    def test_round_trip2(self):
        hash_dict = {'simple_hash_value': EMPTY_MD5,
                     'type': Hash.TYPE_MD5}
        hash_obj = Hash.object_from_dict(hash_dict)
        hash_dict2 = Hash.dict_from_object(hash_obj)
        self.assertEqual(hash_dict, hash_dict2)


class TestHashList(unittest.TestCase):

    def test_round_trip(self):
        hashlist_dict = [
                            {'simple_hash_value': EMPTY_MD5,
                             'type': Hash.TYPE_MD5},
                            {'simple_hash_value': EMPTY_SHA1,
                             'type': Hash.TYPE_SHA1},
                            {'simple_hash_value': EMPTY_SHA256,
                             'type': Hash.TYPE_SHA256},
                        ]
        hashlist_obj = HashList.object_from_dict(hashlist_dict)
        hashlist_dict2 = HashList.dict_from_object(hashlist_obj)
        self.assertEqual(hashlist_dict, hashlist_dict2)


if __name__ == "__main__":
    unittest.main()
