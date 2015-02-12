# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import Contributor
from cybox.test import EntityTestCase


class TestContributor(EntityTestCase, unittest.TestCase):
    klass = Contributor

    _full_dict = {
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


if __name__ == "__main__":
    unittest.main()
