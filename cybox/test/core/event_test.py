# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.core import Event
from cybox.test import EntityTestCase


class TestEvent(EntityTestCase, unittest.TestCase):
    klass = Event

    _full_dict = {
        'id': "example:Event-1",
        'idref': "example:Event-2",
        'type': u("Port Scan"),
        'description': u("This is a test event"),
        'observation_method': {'class': "Network"},
        'frequency': {'rate': 1.0},
        'actions': [
            {'idref': "example:Action-5"},
            {'idref': "example:Action-6"},
        ],
        # Once the choice is implemented, this won't work
        'event': [
            {'idref': "example:Event-A"},
            {'idref': "example:Event-B"},
        ]
    }

    def test_empty_recursive_event(self):
        e = Event()
        e.description = "Foo"
        e.event = None
        self.assertTrue(b"Foo" in e.to_xml())


if __name__ == "__main__":
    unittest.main()
