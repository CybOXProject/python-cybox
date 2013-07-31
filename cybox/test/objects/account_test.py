# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.account_object import Account
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestAccount(unittest.TestCase, ObjectTestCase):
    object_type = "AccountObjectType"
    klass = Account

    def test_round_trip(self):
        account_dict = {
                            'disabled': False,
                            'locked_out': True,
                            'description': 'An account',
                            'domain': 'ADMIN',
                            'xsi:type': 'AccountObjectType'
                       }
        account_dict2 = cybox.test.round_trip_dict(Account, account_dict)
        self.assertEqual(account_dict, account_dict2)


if __name__ == "__main__":
    unittest.main()
