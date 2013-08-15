# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Hash, HashList, HashName, HexBinary
import cybox.test

EMPTY_MD5 = u"d41d8cd98f00b204e9800998ecf8427e"
EMPTY_SHA1 = u"adc83b19e793491b1c6ea0fd8b46cd9f32e592fc"
EMPTY_SHA256 = \
        u"01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"

TEST_HASH_LIST = [
    {'simple_hash_value': EMPTY_MD5,
        'type': Hash.TYPE_MD5},
    {'simple_hash_value': EMPTY_SHA1,
        'type': Hash.TYPE_SHA1},
    {'simple_hash_value': EMPTY_SHA256,
        'type': Hash.TYPE_SHA256},
]


class TestHash(unittest.TestCase):

    def setUp(self):
        self.md5 = HexBinary(EMPTY_MD5)
        self.sha1 = HexBinary(EMPTY_SHA1)
        self.sha256 = HexBinary(EMPTY_SHA256)

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

    def test_autotype_sha256(self):
        """64-character hash is assumed to be SHA-256"""
        h = Hash(EMPTY_SHA256)
        self.assertEqual(h.type_, Hash.TYPE_SHA256)

        h2 = Hash(self.sha256)
        self.assertEqual(h2.type_, Hash.TYPE_SHA256)

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
        self.assertTrue(EMPTY_MD5 in s)

    def test_constructor(self):
        s = HexBinary(EMPTY_MD5)
        h = Hash(s)

    def test_exact_hash(self):
        h = Hash(EMPTY_MD5, exact=True)
        self.assertEqual("Equals", h.simple_hash_value.condition)


class TestHashList(unittest.TestCase):

    def test_round_trip(self):
        hashlist_list = TEST_HASH_LIST
        hashlist_obj = HashList.object_from_list(hashlist_list)
        hashlist_list2 = HashList.list_from_object(hashlist_obj)
        self.assertEqual(hashlist_list, hashlist_list2)

    def test_namespace_count(self):
        h = HashList()
        h.append(EMPTY_MD5)
        h.append(EMPTY_SHA1)
        h.append(EMPTY_SHA256)
        print h.to_xml()

        ns_list = cybox.test.round_trip(h, list_=True)._get_namespaces()
        print ns_list

        # Only "common" and "vocabs" should be here. "xsi" is only added later
        self.assertEqual(2, len(ns_list))


if __name__ == "__main__":
    unittest.main()
