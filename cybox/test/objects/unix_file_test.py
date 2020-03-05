# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_file_object import UnixFile, UnixFilePermissions
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestUnixFilePermissions(EntityTestCase, unittest.TestCase):
    klass = UnixFilePermissions
    _full_dict = {
        'suid': True,
        'sgid': False,
        'uread': True,
        'uwrite': True,
        'uexec': True,
        'gread': True,
        'gwrite': False,
        'gexec': False,
        'oread': True,
        'owrite': False,
        'oexec': False,
    }


class TestUnixFile(ObjectTestCase, unittest.TestCase):
    object_type = "UnixFileObjectType"
    klass = UnixFile

    _full_dict = {
        'group_owner': u('samplegroup'),
        'inode': 6755399441071048,
        'type': u('regularfile'),
        'permissions': TestUnixFilePermissions._full_dict,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
