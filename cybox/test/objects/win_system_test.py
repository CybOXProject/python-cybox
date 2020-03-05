# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_system_object import GlobalFlag, GlobalFlagList, WinSystem
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.win_handle_test import TestWinHandle


class TestGlobalFlag(EntityTestCase, unittest.TestCase):
    klass = GlobalFlag

    _full_dict = {
        'abbreviation': u('tst'),
        'destination': u('C:/TEST'),
        'hexadecimal_value': u('0x1'),
        'symbolic_name': u('somesymbol'),
    }


class TestGlobalFlagList(EntityTestCase, unittest.TestCase):
    klass = GlobalFlagList

    _full_dict = [
        TestGlobalFlag._full_dict,
        TestGlobalFlag._full_dict,
    ]


class TestWinSystem(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsSystemObjectType"
    klass = WinSystem

    _full_dict = {
        'domain': [u('WORKINGGROUP')],
        'global_flag_list': TestGlobalFlagList._full_dict,
        'netbios_name': u('joe.local'),
        'open_handle_list': [TestWinHandle._full_dict],
        'product_id': u('00330-80000-00000-AA880'),
        'product_name': u('Windows 10'),
        'registered_organization': u('Fabrikam'),
        'registered_owner': u('Joe'),
        'windows_directory': u('C:\\WINDOWS'),
        'windows_system_directory': u('C:\\WINDOWS\\system32'),
        'windows_temp_directory': u('C:\\TEMP'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
