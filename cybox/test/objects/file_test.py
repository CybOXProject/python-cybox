import unittest

from cybox.common import Hash, String
from cybox.objects.file_object import File, FilePath
from cybox.test import round_trip
from cybox.test.common.hash_test import EMPTY_MD5, EMPTY_SHA1, EMPTY_SHA256
from cybox.test.objects import ObjectTestCase


class TestFilePath(unittest.TestCase):

    def setUp(self):
        self.path = "C:\\WINDOWS\\system32\\"

    def test_round_trip(self):
        fp = FilePath(self.path)
        fp.fully_qualified = True

        fp2 = round_trip(fp, FilePath)
        self.assertEqual(fp.to_dict(), fp2.to_dict())

    def test_xml_output(self):
        fp = FilePath(self.path)

        self.assertTrue(self.path in fp.to_xml())


class TestFile(unittest.TestCase, ObjectTestCase):
    object_type = "FileObjectType"
    klass = File

    def test_filepath_is_none(self):
        # This would throw an exception at one point. Should be fixed now.
        a = File.from_dict({'file_name': 'abcd.dll'})

    def test_round_trip(self):
        file_dict = {'file_name': "example.txt",
                     'xsi:type': File._XSI_TYPE}
        file_obj = File.object_from_dict(file_dict)
        file_dict2 = File.dict_from_object(file_obj)
        self.assertEqual(file_dict, file_dict2)

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


if __name__ == "__main__":
    unittest.main()
