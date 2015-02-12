# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.account_object import Account
from cybox.test.objects import ObjectTestCase


class TestAccount(ObjectTestCase, unittest.TestCase):
    object_type = "AccountObjectType"
    klass = Account

    _full_dict = {
        'disabled': False,
        'locked_out': True,
        'description': 'An account',
        'domain': 'ADMIN',
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
