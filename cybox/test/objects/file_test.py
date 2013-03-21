import unittest

from cybox.objects.file_object import File, FilePath
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase

class TestFilePath(unittest.TestCase):

    def test_round_trip(self):
        fp = FilePath("C:\\WINDOWS\\system32\\")
        fp.fully_qualified = True

        fp2 = round_trip(fp, FilePath)
        self.assertEqual(fp.to_dict(), fp2.to_dict())

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


if __name__ == "__main__":
    unittest.main()
