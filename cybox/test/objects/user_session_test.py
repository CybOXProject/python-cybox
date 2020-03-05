# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.user_session_object import UserSession
from cybox.test.objects import ObjectTestCase


class TestUserSession(ObjectTestCase, unittest.TestCase):
    object_type = "UserSessionObjectType"
    klass = UserSession

    _full_dict = {
        'effective_group': 'dev',
        'effective_group_id': '500',
        'effective_user': 'user-1',
        'effective_user_id': '25',
        'login_time': "2001-01-01T06:56:50+04:00",
        'logout_time': "2001-01-02T06:56:50+04:00",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
