# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.file_object import File, FilePath, Packer, SymLinksList

from cybox.common import Hash, String
from cybox.compat import long
import cybox.test
from cybox.test import EntityTestCase
from cybox.test.common.hash_test import (EMPTY_MD5, EMPTY_SHA1, EMPTY_SHA224,
        EMPTY_SHA256, EMPTY_SHA384, EMPTY_SHA512)
from cybox.test.objects import ObjectTestCase


class TestFilePath(unittest.TestCase):

    def setUp(self):
        self.path = "C:\\WINDOWS\\system32\\"
        self.path_bytes = b"C:\\WINDOWS\\system32\\"

    def test_round_trip(self):
        fp = FilePath(self.path)
        fp.fully_qualified = True

        fp2 = cybox.test.round_trip(fp, FilePath)
        self.assertEqual(fp.to_dict(), fp2.to_dict())

    def test_xml_output(self):
        fp = FilePath(self.path)

        self.assertTrue(self.path_bytes in fp.to_xml())


class TestFile(ObjectTestCase, unittest.TestCase):
    object_type = "FileObjectType"
    klass = File

    _full_dict = {
        'is_packed': False,
        'is_masqueraded': True,
        'file_name': u("example.txt"),
        'file_path': {'value': u("C:\\Temp"),
                      'fully_qualified': True},
        'device_path': u("\\Device\\CdRom0"),
        'full_path': u("C:\\Temp\\example.txt"),
        'file_extension': u("txt"),
        'size_in_bytes': { 'apply_condition': 'ANY', 'condition':'InclusiveBetween', 'value': [long(1023), long(1024)] },
        'magic_number': u("D0CF11E0"),
        'file_format': u("ASCII Text"),
        'hashes': [
            {
                'type': Hash.TYPE_MD5,
                'simple_hash_value': u("0123456789abcdef0123456789abcdef")
            }
        ],
        'digital_signatures': [
            {
                'certificate_issuer': u("Microsoft"),
                'certificate_subject': u("Notepad"),
            }
        ],
        'modified_time': "2010-11-06T02:02:02+08:00",
        'accessed_time': "2010-11-07T02:03:02+09:00",
        'created_time': "2010-11-08T02:04:02+10:00",
        'user_owner': u("sballmer"),
        'packer_list': [
            {
                'name': u("UPX"),
                'version': u("3.91"),
            }
        ],
        'peak_entropy': 7.454352453,
        'sym_links': [u("../link_destination")],
        'byte_runs': [{'offset': 16, 'byte_run_data': u("1A2B3C4D")}],
        'extracted_features': {
            'strings': [{'string_value': u("string from the file")}],
        },
        'encryption_algorithm': u("RC4"),
        'compression_method': u("deflate"),
        'compression_version': u("1.0"),
        'compression_comment': u("This has been compressed"),
        'xsi:type': object_type,
    }

    def test_filepath_is_none(self):
        # This would throw an exception at one point. Should be fixed now.
        a = File.from_dict({'file_name': 'abcd.dll'})

    def test_get_hashes(self):
        f = File()
        f.add_hash(Hash(EMPTY_MD5))
        f.add_hash(Hash(EMPTY_SHA1))
        f.add_hash(Hash(EMPTY_SHA224))
        f.add_hash(Hash(EMPTY_SHA256))
        f.add_hash(Hash(EMPTY_SHA384))
        f.add_hash(Hash(EMPTY_SHA512))

        self.assertEqual(EMPTY_MD5, f.md5)
        self.assertEqual(EMPTY_SHA1, f.sha1)
        self.assertEqual(EMPTY_SHA224, f.sha224)
        self.assertEqual(EMPTY_SHA256, f.sha256)
        self.assertEqual(EMPTY_SHA384, f.sha384)
        self.assertEqual(EMPTY_SHA512, f.sha512)

    def test_set_hashes(self):
        f = File()
        f.md5 = EMPTY_MD5
        f.sha1 = EMPTY_SHA1
        f.sha224 = EMPTY_SHA224
        f.sha256 = EMPTY_SHA256
        f.sha384 = EMPTY_SHA384
        f.sha512 = EMPTY_SHA512

        self.assertEqual(EMPTY_MD5, f.md5)
        self.assertEqual(EMPTY_SHA1, f.sha1)
        self.assertEqual(EMPTY_SHA224, f.sha224)
        self.assertEqual(EMPTY_SHA256, f.sha256)
        self.assertEqual(EMPTY_SHA384, f.sha384)
        self.assertEqual(EMPTY_SHA512, f.sha512)

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

    def test_file_name_delimiter(self):
        f = File()
        f.file_name = ["foo", "bar"]
        f.file_name.delimiter = "^^"
        self.assertTrue(b"foo^^bar" in f.to_xml())


class TestPacker(EntityTestCase, unittest.TestCase):
    klass = Packer

    _full_dict = {
        'name': u("CrazyPack"),
        'version': u("2.0.1"),
        'entry_point': u("EB0FA192"),
        'signature': u("xxCrAzYpAcKxx"),
        'type': u("Protector"),
        'ep_jump_codes': {
            'depth': 2,
            'opcodes': u("A B C")
        },
        'detected_entrypoint_signatures': [
              {
                  'name': u("test 1"),
                  'type' : u('type 1')
              },
              {
                  'name': u("test 2"),
                  'type' : u('type 2')
              }
        ],
    }


class TestSymLinksList(EntityTestCase, unittest.TestCase):
    klass = SymLinksList

    _full_dict = [
            "C:\\Temp\\Recent\\link_destination",
            "C:\\Temp\\Recent\\link_destination2",
    ]

if __name__ == "__main__":
    unittest.main()
