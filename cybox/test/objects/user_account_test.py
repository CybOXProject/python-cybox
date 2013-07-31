# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.user_account_object import UserAccount
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestUserAccount(unittest.TestCase, ObjectTestCase):
    object_type = "UserAccountObjectType"
    klass = UserAccount

    def test_round_trip(self):
        account_dict = {
                            # Account-specific fields
                            'disabled': False,
                            'locked_out': True,
                            'description': u'An account',
                            'domain': u'ADMIN',
                            # UserAccount-specific fields
                            # (cannot test group_list of privilege_list since
                            # they are abstract)
                            'password_required': True,
                            'full_name': u"Guido van Rossum",
                            'home_directory': u"/home/guido/",
                            'last_login': "2001-01-01T06:56:50+04:00",
                            'script_path': u"/bin/bash",
                            'username': u"guido",
                            'user_password_age': u"P90D",
                            'xsi:type': 'UserAccountObjectType',
                       }
        account_dict2 = cybox.test.round_trip_dict(UserAccount, account_dict)
        self.assertEqual(account_dict, account_dict2)


if __name__ == "__main__":
    unittest.main()
