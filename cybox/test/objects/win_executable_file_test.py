# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_executable_file_object import WinExecutableFile
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.win_handle_test import TestWinHandle


class TestGlobalFlag(EntityTestCase, unittest.TestCase):
    klass = GlobalFlag


class TestWinExecutableFile(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsExecutableFileObjectType"
    klass = WinExecutableFile

    _full_dict = {
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
