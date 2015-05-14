# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.win_file_object import WinFile, Stream
from cybox.test.common.hash_test import EMPTY_MD5
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestStream(EntityTestCase, unittest.TestCase):
    klass = Stream
    _full_dict = {'hashes': [{'type': u("MD5"),
                              'simple_hash_value': EMPTY_MD5}],
                  'name': u("StreamB"),
                  'size_in_bytes': 204}


class TestWinFile(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsFileObjectType"
    klass = WinFile

    _full_dict = {
        # File fields (only a few are included)
        'file_name': u("example.doc"),
        'full_path': u("C:\\Temp\\example.doc"),
        'file_extension': u("doc"),
        'size_in_bytes': long(1024),
        'magic_number': u("D0CF11E0"),

        # WinFile-specific fields
        'filename_accessed_time': "2012-05-12T07:14:02+07:00",
        'filename_created_time': "2012-05-17T09:28:04+07:00",
        'filename_modified_time': "2012-06-12T11:15:12+07:00",
        'drive': u("C:"),
        'security_id': u("S-1-5-21-3623958015-3361044348-30300820-1013"),
        'security_type': u("SidTypeFile"),
        'stream_list': [{'name': u("StreamA")},
                        {'hashes': [{'type': u("MD5"),
                                     'simple_hash_value': EMPTY_MD5}],
                         'name': u("StreamB")}],

        # WinFile-specific implementations of abstract types.
        'file_attributes_list': [u("Hidden"), u("System"), u("Temporary")],
        'permissions': {
            'full_control': False,
            'modify': True,
            'read': True,
            'read_and_execute': False,
            'write': False,
        },

        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
