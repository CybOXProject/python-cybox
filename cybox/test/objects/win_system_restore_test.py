# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_system_restore_object import WinSystemRestore

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinSystemRestore(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsSystemRestoreObjectType"
    klass = WinSystemRestore

    _full_dict = {
        'restore_point_description': u("restore desc"),
        'restore_point_full_path': u("restore path"),
        'acl_change_username': u("username"),
        'restore_point_name': u("pont name"),
        'restore_point_type': u("point type"),
        'backup_file_name': u("backup name"),
        'acl_change_sid': u("an SID"),
        'changelog_entry_flags': u("entry flags"),
        'changelog_entry_sequence_number': 1234,
        # TODO: add 'created'
        'file_attributes': u("RWX"),
        'new_file_name': u("New name"),
        'original_file_name': u("original file name"),
        'original_short_file_name': u("org fname"),
        'process_name': u("A process name"),
        'change_event': u("some event"),
        'changelog_entry_type': u("entry type"),
        'registry_hive_list': [
            u("hive 1"),
            u("hive 2")
        ],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
