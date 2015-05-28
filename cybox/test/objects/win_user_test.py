# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_user_object import WinUser
from cybox.test.objects import ObjectTestCase


class TestWinUser(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsUserAccountObjectType"
    klass = WinUser

    _full_dict = {
        # Account-specific fields
        'disabled': False,
        'domain': u('ADMIN'),
        # UserAccount-specific fields
        'password_required': True,
        'full_name': u("Steve Ballmer"),
        'group_list': [{'name': u("LocalAdministrators")}],
        'home_directory': u("C:\\\\Users\\\\ballmer\\\\"),
        'last_login': "2011-05-12T07:14:01+07:00",
        'privilege_list': [
                {'user_right': u("SeDebugPrivilege")}
            ],
        'username': u("ballmer"),
        'user_password_age': u("P180D"),
        # WinUser-specific fields
        'security_id': u("S-1-5-21-3623811015-3361044348-30300820-1013"),
        'security_type': u("SidTypeUser"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
