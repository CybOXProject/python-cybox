# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.dns_cache_object import DNSCache, DNSCacheEntry
from cybox.test.objects import ObjectTestCase


class TestAccount(ObjectTestCase, unittest.TestCase):
    object_type = "DNSCacheObjectType"
    klass = DNSCache

    _full_dict = {
        'xsi:type': object_type,
        'dns_cache_entry': [
            {
                'ttl': 60,
                'dns_entry': {
                    'description': "First test",
                    'data_length': 1024,
                    'xsi:type': 'DNSRecordObjectType'
                }
            },
            {
                'ttl': 16,
                'dns_entry': {
                    'description': "Second test",
                    'data_length': 1565,
                    'record_name': "A record name",
                    'xsi:type': 'DNSRecordObjectType'
                }
            },
        ]
    }


if __name__ == "__main__":
    unittest.main()
