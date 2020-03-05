# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.url_history_object import URLHistory, URLHistoryEntry
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestUrlHistoryEntry(EntityTestCase, unittest.TestCase):
    klass = URLHistoryEntry

    _full_dict = {
        'url': {
            'value': u('http://www.example.com/index.html'),
            'type': 'URL',
            'xsi:type': 'URIObjectType',
        },
        'hostname': {
            'hostname_value': u('www.example.com'),
            'xsi:type': 'HostnameObjectType',
        },
        'referrer_url': {
            'value': u('http://www.example2.com/index.html'),
            'type': 'URL',
            'xsi:type': 'URIObjectType',
        },
        'page_title': u('An example on URLHistoryEntry'),
        'user_profile_name': u('Default'),
        'visit_count': 5,
        'manually_entered_count': 1,
        'modification_datetime': '2001-01-01T06:56:50+04:00',
        'expiration_datetime': '2001-01-01T06:56:50+04:00',
        'first_visit_datetime': '2001-01-01T06:56:50+04:00',
        'last_visit_datetime': '2001-01-05T06:56:50+04:00',
    }


class TestUrlHistory(ObjectTestCase, unittest.TestCase):
    object_type = "URLHistoryObjectType"
    klass = URLHistory

    _full_dict = {
        'browser_information': {
            'name': 'Google Chrome (64-bit)',
            'vendor': 'Google',
            'version': '80.0.3987.106'
        },
        'url_history_entry': [
            TestUrlHistoryEntry._full_dict
        ],
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
