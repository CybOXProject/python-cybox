# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Contributor
import cybox.test


class TestContributor(unittest.TestCase):

    def test_round_trip(self):
        contrib_dict = {
                        'role': "Lead Tester",
                        'name': "Marty McFly",
                        'email': "marty@mcfly.com",
                        'phone': "(123) 456-7890",
                        'organization': "Doc Brown Enterprises(tm)",
                        'date': {
                            'start_date': "1955-11-05",
                            'end_date': "1985-11-05",
                        },
                        'contribution_location': "Hill Valley, CA",
                       }
        contrib_dict2 = cybox.test.round_trip_dict(Contributor, contrib_dict)
        self.assertEqual(contrib_dict, contrib_dict2)


if __name__ == "__main__":
    unittest.main()
