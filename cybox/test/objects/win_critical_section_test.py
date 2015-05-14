# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_critical_section_object import WinCriticalSection
from cybox.test.objects import ObjectTestCase


class TestWinCriticalSection(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsCriticalSectionObjectType"
    klass = WinCriticalSection

    _full_dict = {
        'address': u("deadbeef"),
        'spin_count': 12345,
        'xsi:type': object_type
    }


if __name__ == "__main__":
    unittest.main()
