import unittest

from cybox.objects.file_object import File
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestFile(unittest.TestCase, ObjectTestCase):
    object_type = "FileObjectType"
    klass = File


    def test_filepath_is_none(self):
        # This would throw an exception at one point. Should be fixed now.
        a = File.from_dict({'file_name': 'abcd.dll'})


    def test_round_trip(self):
        pass


if __name__ == "__main__":
    unittest.main()
