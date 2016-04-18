# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import logging
import unittest

from mixbox.vendor.six import u

from cybox.common import Hash, HashList, HashName, HexBinary
import cybox.test

logger = logging.getLogger(__name__)

EMPTY_MD5 = u("d41d8cd98f00b204e9800998ecf8427e")
EMPTY_SHA1 = u("da39a3ee5e6b4b0d3255bfef95601890afd80709")
EMPTY_SHA224 = u("d14a028c2a3a2bc9476102bb288234c415a2b01f828ea62ac5b3e42f")
EMPTY_SHA256 = \
        u("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
EMPTY_SHA384 = u(
        "38b060a751ac96384cd9327eb1b1e36a21fdb71114be0743"
        "4c0cc7bf63f6e1da274edebfe76f65fbd51ad2f14898b95b")
EMPTY_SHA512 = u(
        "cf83e1357eefb8bdf1542850d66d8007d620e4050b5715dc83f4a921d36ce9ce"
        "47d0d13c5d85f2b0ff8318d2877eec2f63b931bd47417a81a538327af927da3e")

TEST_HASH_LIST = [
    {'simple_hash_value': EMPTY_MD5,
        'type': Hash.TYPE_MD5},
    {'simple_hash_value': EMPTY_SHA1,
        'type': Hash.TYPE_SHA1},
    {'simple_hash_value': EMPTY_SHA224,
        'type': Hash.TYPE_SHA224},
    {'simple_hash_value': EMPTY_SHA256,
        'type': Hash.TYPE_SHA256},
    {'simple_hash_value': EMPTY_SHA384,
        'type': Hash.TYPE_SHA384},
    {'simple_hash_value': EMPTY_SHA512,
        'type': Hash.TYPE_SHA512},
]


class TestHash(unittest.TestCase):

    def setUp(self):
        self.md5 = HexBinary(EMPTY_MD5)
        self.sha1 = HexBinary(EMPTY_SHA1)
        self.sha224 = HexBinary(EMPTY_SHA224)
        self.sha256 = HexBinary(EMPTY_SHA256)
        self.sha384 = HexBinary(EMPTY_SHA384)
        self.sha512 = HexBinary(EMPTY_SHA512)

    def test_autotype(self):
        h = Hash()
        h.simple_hash_value = "0123456789abcdef0123456789abcdef"
        self.assertEqual(h.type_, Hash.TYPE_MD5)
        h.type_ = Hash.TYPE_OTHER
        self.assertEqual(h.type_, Hash.TYPE_OTHER)
        h.simple_hash_value = "0123456789abcdef0123456789abcdef"
        self.assertEqual(h.type_, Hash.TYPE_OTHER)

        h2 = Hash()
        h2.type_ = Hash.TYPE_OTHER
        h2.simple_hash_value = "0123456789abcdef0123456789abcdef"
        self.assertEqual(h2.type_, Hash.TYPE_OTHER)

    def test_autotype_md5(self):
        """32-character hash is assumed to be MD5"""
        h = Hash(EMPTY_MD5)
        self.assertEqual(h.type_, Hash.TYPE_MD5)

        h2 = Hash(self.md5)
        self.assertEqual(h2.type_, Hash.TYPE_MD5)

    def test_autotype_sha1(self):
        """40-character hash is assumed to be SHA-1"""
        h = Hash(EMPTY_SHA1)
        self.assertEqual(h.type_, Hash.TYPE_SHA1)

        h2 = Hash(self.sha1)
        self.assertEqual(h2.type_, Hash.TYPE_SHA1)

    def test_autotype_sha224(self):
        """56-character hash is assumed to be SHA-224"""
        h = Hash(EMPTY_SHA224)
        self.assertEqual(h.type_, Hash.TYPE_SHA224)

        h2 = Hash(self.sha224)
        self.assertEqual(h2.type_, Hash.TYPE_SHA224)

    def test_autotype_sha256(self):
        """64-character hash is assumed to be SHA-256"""
        h = Hash(EMPTY_SHA256)
        self.assertEqual(h.type_, Hash.TYPE_SHA256)

        h2 = Hash(self.sha256)
        self.assertEqual(h2.type_, Hash.TYPE_SHA256)

    def test_autotype_sha384(self):
        """96-character hash is assumed to be SHA-384"""
        h = Hash(EMPTY_SHA384)
        self.assertEqual(h.type_, Hash.TYPE_SHA384)

        h2 = Hash(self.sha384)
        self.assertEqual(h2.type_, Hash.TYPE_SHA384)

    def test_autotype_sha512(self):
        """128-character hash is assumed to be SHA-512"""
        h = Hash(EMPTY_SHA512)
        self.assertEqual(h.type_, Hash.TYPE_SHA512)

        h2 = Hash(self.sha512)
        self.assertEqual(h2.type_, Hash.TYPE_SHA512)

    def test_autotype_other(self):
        """Hash of unknown length is assigned TYPE_OTHER"""
        h = Hash("0123456789abcdef")
        self.assertEqual(h.type_, Hash.TYPE_OTHER)

    def test_round_trip(self):
        t = HashName(Hash.TYPE_MD5)

        h = Hash(self.md5, t)

        hash2 = cybox.test.round_trip(h)

        self.assertEqual(hash2.simple_hash_value, self.md5)
        #TODO: make this really pass
        self.assertEqual(hash2.type_.value, t.value)

    def test_round_trip2(self):
        hash_dict = {'simple_hash_value': EMPTY_MD5,
                     'type': Hash.TYPE_MD5}
        hash_obj = Hash.object_from_dict(hash_dict)
        hash_dict2 = Hash.dict_from_object(hash_obj)
        self.assertEqual(hash_dict, hash_dict2)

    def test_xml_output(self):
        h = Hash(self.md5)
        h2 = cybox.test.round_trip(h)
        self.assertEqual(str(h2), EMPTY_MD5)

        s = h2.to_xml()
        self.assertTrue(EMPTY_MD5.encode("utf-8") in s)

    def test_constructor(self):
        s = HexBinary(EMPTY_MD5)
        h = Hash(s)

    def test_exact_hash(self):
        h = Hash(EMPTY_MD5, exact=True)
        self.assertEqual("Equals", h.simple_hash_value.condition)
        self.assertEqual("Equals", h.type_.condition)


class TestHashList(unittest.TestCase):

    def test_round_trip(self):
        hashlist_list = TEST_HASH_LIST
        hashlist_obj = HashList.object_from_list(hashlist_list)
        hashlist_list2 = HashList.list_from_object(hashlist_obj)
        self.assertEqual(hashlist_list, hashlist_list2)

    def test_hash_lookup(self):
        h = HashList()
        self.assertEqual(None, h.md5)
        self.assertEqual(None, h.sha1)
        self.assertEqual(None, h.sha224)
        self.assertEqual(None, h.sha256)
        self.assertEqual(None, h.sha384)
        self.assertEqual(None, h.sha512)


if __name__ == "__main__":
    unittest.main()
