# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.dns_record_object import DNSRecord
from cybox.test.objects import ObjectTestCase
from cybox.test.objects.address_test import TestAddress
from cybox.test.objects.uri_test import TestURI


class TestDNSRecord(ObjectTestCase, unittest.TestCase):
    object_type = "DNSRecordObjectType"
    klass = DNSRecord

    _full_dict = {
        'description': 'A description of this object',
        'domain_name': TestURI._full_dict,
        'queried_date': '2001-01-01T06:56:50+04:00',
        'ip_address': TestAddress._full_dict,
        'address_class': 'IPv4',
        'entry_type': 'SRV',
        'record_name': u('vc.example.com'),
        'record_type': 'DNS',
        'ttl': 14400,
        'flags': u('10'),
        'data_length': 13200,
        'record_data': u('Some Record Data'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
