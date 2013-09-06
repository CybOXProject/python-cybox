# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Hash, String
from cybox.objects.file_object import File, FilePath, Packer
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.common.hash_test import EMPTY_MD5, EMPTY_SHA1, EMPTY_SHA256
from cybox.test.objects import ObjectTestCase


class TestFilePath(unittest.TestCase):

    def setUp(self):
        self.path = "C:\\WINDOWS\\system32\\"

    def test_round_trip(self):
        fp = FilePath(self.path)
        fp.fully_qualified = True

        fp2 = cybox.test.round_trip(fp, FilePath)
        self.assertEqual(fp.to_dict(), fp2.to_dict())

    def test_xml_output(self):
        fp = FilePath(self.path)

        self.assertTrue(self.path in fp.to_xml())


class TestFile(ObjectTestCase, unittest.TestCase):
    object_type = "FileObjectType"
    klass = File

    _full_dict = {
        'is_packed': False,
        'file_name': "example.txt",
        'file_path': {'value': "C:\\Temp",
                    'fully_qualified': True},
        'device_path': "\\Device\\CdRom0",
        'full_path': "C:\\Temp\\example.txt",
        'file_extension': "txt",
        'size_in_bytes': 1024,
        'magic_number': "D0CF11E0",
        'file_format': "ASCII Text",
        'hashes': [
            {
                'type': Hash.TYPE_MD5,
                'simple_hash_value': "0123456789abcdef0123456789abcdef"
            }
        ],
        'modified_time': "2010-11-06T02:02:02+08:00",
        'accessed_time': "2010-11-07T02:03:02+09:00",
        'created_time': "2010-11-08T02:04:02+10:00",
        'xsi:type': object_type,
    }

    def test_filepath_is_none(self):
        # This would throw an exception at one point. Should be fixed now.
        a = File.from_dict({'file_name': 'abcd.dll'})

    def test_get_hashes(self):
        f = File()
        f.add_hash(Hash(EMPTY_MD5))
        f.add_hash(Hash(EMPTY_SHA1))
        f.add_hash(Hash(EMPTY_SHA256))

        self.assertEqual(EMPTY_MD5, f.md5)
        self.assertEqual(EMPTY_SHA1, f.sha1)
        self.assertEqual(EMPTY_SHA256, f.sha256)

    def test_set_hashes(self):
        f = File()
        f.md5 = EMPTY_MD5
        f.sha1 = EMPTY_SHA1
        f.sha256 = EMPTY_SHA256

        self.assertEqual(EMPTY_MD5, f.md5)
        self.assertEqual(EMPTY_SHA1, f.sha1)
        self.assertEqual(EMPTY_SHA256, f.sha256)

    def test_add_hash_string(self):
        s = "ffffffffffffffffffff"
        f = File()
        f.add_hash(s)

        h = f.hashes[0]
        self.assertEqual(s, str(h.simple_hash_value))
        self.assertEqual(Hash.TYPE_OTHER, h.type_)

    def test_fields(self):
        f = File()
        f.file_name = "blah.exe"
        self.assertEqual(String, type(f.file_name))

        f.file_path = "C:\\Temp"
        self.assertEqual(FilePath, type(f.file_path))

    def test_fields_not_shared(self):
        # In a previous version of TypedFields, all objects of the same type
        # shared a single value of each field. Obviously this was a mistake.
        f = File()
        f.file_name = "README.txt"
        self.assertEqual("README.txt", f.file_name)

        f2 = File()
        self.assertEqual(None, f2.file_name)


class TestPacker(EntityTestCase, unittest.TestCase):
    klass = Packer

    _full_dict = {
        'name': "CrazyPack",
        'version': "2.0.1",
        'entry_point': "EB0FA192",
        'signature': "xxCrAzYpAcKxx",
        'type': "Protector",
    }

if __name__ == "__main__":
    unittest.main()
