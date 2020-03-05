# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_process_object import MemorySectionList, StartupInfo, WinProcess
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.memory_test import TestMemory
from cybox.test.objects.win_handle_test import TestWinHandle


class TestMemorySectionList(EntityTestCase, unittest.TestCase):
    klass = MemorySectionList

    _full_dict = [
        TestMemory._full_dict,
        TestMemory._full_dict
    ]


class TestStartupInfo(EntityTestCase, unittest.TestCase):
    klass = StartupInfo

    _full_dict = {
        'lpdesktop': u('Desktop Title'),
        'lptitle': u('Program Title'),
        'dwx': 0,
        'dwy': 0,
        'dwxsize': 800,
        'dwysize': 600,
        'dwxcountchars': 800,
        'dwycountchars': 600,
        'dwfillattribute': 1,
        'dwflags': 0,
        'wshowwindow': 1,
        'hstdinput': TestWinHandle._full_dict,
        'hstdoutput': TestWinHandle._full_dict,
        'hstderror': TestWinHandle._full_dict,
    }


class TestWinProcess(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsProcessObjectType"
    klass = WinProcess

    _full_dict = {
        'aslr_enabled': True,
        'dep_enabled': False,
        'priority': u('normal'),
        'section_list': TestMemorySectionList._full_dict,
        'security_id': u("S-1-5-21-3623811015-3361044348-30300820-1013"),
        'startup_info': TestStartupInfo._full_dict,
        'security_type': u("SidTypeUser"),
        'window_title': u('Example Title'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
