# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.core import Event, Observable
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

    def test_observable_from_dict_with_event(self):
        data = {
            'event': {
                'type': {
                    'xsi:type': 'cyboxVocabs:EventTypeVocab-1.0.1',
                    'value': 'DHCP',
                }
            }
        }
        obs = Observable.from_dict(data)
        assert obs.event.type_ == 'DHCP'



if __name__ == "__main__":
    unittest.main()
