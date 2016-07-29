# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_event_log_object import WinEventLog
from cybox.test.objects import ObjectTestCase


class TestWinEventLog(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsEventLogObjectType"
    klass = WinEventLog

    _full_dict = {
        'eid': 4000000,
        'type': u"warning",
        'log': u"Bad things that happened",
        'message': u"Something bad happened",
        'category_num': 43,
        'category': u"Things that go bump in the night",
        'generation_time': "2014-10-05T07:14:21+00:00",
        'source': u"Under the bed",
        'machine': u"apple",
        'user': u"Timmy",
        'blob': u"d234b6LKJSBLKB2453452",
        'correlation_activity_id': u"abc123",
        'correlation_related_activity_id': u"def456",
        'execution_process_id': u"ghi789",
        'execution_thread_id': u"jkl0ab",
        'index': 123456789,
        'reserved': 0x654c664c,
        'unformatted_message_list': [
            u"I looked under the bed",
            u"and saw",
            u"a monster",
         ],
        'write_time': "2014-10-05T08:14:21+00:00",
        'xsi:type': "WindowsEventLogObjectType",
    }

    # https://github.com/CybOXProject/python-cybox/issues/267
    def test_type(self):
        log = WinEventLog()
        log.type_ = "Success"
        self.assertTrue(b"Success" in log.to_xml())


if __name__ == "__main__":
    unittest.main()
