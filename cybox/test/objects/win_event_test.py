# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_event_object import WinEvent
from cybox.test.objects import ObjectTestCase


class TestWinEvent(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsEventObjectType"
    klass = WinEvent

    _full_dict = {
        'name': u("Object Open"),
        'handle': {
                'name': u("Event Handle"),
                'type': u("Event"),
                'xsi:type': "WindowsHandleObjectType",
            },
        'type': u("Success"),
        'xsi:type': "WindowsEventObjectType",
    }

    # https://github.com/CybOXProject/python-cybox/issues/213
    def test_object_construction(self):
        event = WinEvent()
        event.name = "Object Open"
        event.type_ = "Success"

        # Before #213 was solved, these would raise exceptions because the
        # `type_` was called `type`
        d = event.to_dict()  # Should not raise.
        self.assertEqual("Success", d['type'])
        o = event.to_xml()  # Should not raise.
        self.assertTrue(b"Success" in o)


if __name__ == "__main__":
    unittest.main()
