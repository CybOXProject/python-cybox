# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_event_object import WinEvent
from cybox.test.objects import ObjectTestCase


class TestWinThread(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsEventObjectType"
    klass = WinEvent

    _full_dict = {
        'name': u"Object Open",
        'handle': {
                'name': u"Event Handle",
                'type': u"Event",
                'xsi:type': "WindowsHandleObjectType",
            },
        'type': u"Success",
        'xsi:type': "WindowsEventObjectType",
    }


if __name__ == "__main__":
    unittest.main()
