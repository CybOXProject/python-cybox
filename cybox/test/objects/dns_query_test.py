# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import uuid

from cybox.objects.dns_query_object import DNSQuestion
import cybox.test


class TestQuestion(unittest.TestCase):

    def test_round_trip(self):
        question_dict = {
                            'qname': {'value': "www.example.com"},
                            'qtype': "A",
                            'qclass': "IN",
                        }

        question_dict2 = cybox.test.round_trip_dict(DNSQuestion, question_dict)
        cybox.test.assert_equal_ignore(question_dict, question_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
