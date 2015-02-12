# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_prefetch_object import WinPrefetch

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinPrefetch(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsPrefetchObjectType"
    klass = WinPrefetch

    _full_dict = {
        'application_file_name': u"A file name",
        'prefetch_hash': u"A hash",
        'times_executed': 14,
        #'first_run' = cybox.TypedField("First_Run", DateTime)
        #'last_run' = cybox.TypedField("Last_Run", DateTime)
        #'volume' = cybox.TypedField("Volume", VolumeType)
        #'accessed_file_list' = cybox.TypedField("Accessed_File_List", AccessedFileListType)
        #'accessed_directory_list' = cybox.TypedField("Accessed_Directory_List", AccessedDirectoryListType)        
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
