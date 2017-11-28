# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.unix_user_account_object import UnixUserAccount
from cybox.test.objects import ObjectTestCase


class TestUnixUserAccount(ObjectTestCase, unittest.TestCase):
    object_type = "UnixUserAccountObjectType"
    klass = UnixUserAccount

    _full_dict = {
        # Account-specific fields
        'disabled': False,
        'locked_out': True,
        'description': u('An UNIX account'),
        'domain': u('ADMIN'),
        'group_list': [
            {
                'group_id': 12345,
                'xsi:type': 'UnixGroupType'
            }
        ],
        'privilege_list': [
            {
                'permissions_mask': u("rwx"),
                'xsi:type': 'UnixPrivilegeType'
            }
        ],
        'password_required': True,
        'full_name': u("Guido van Rossum"),
        'home_directory': u("/home/guido/"),
        'last_login': "2001-01-01T06:56:50+04:00",
        'script_path': u("/bin/bash"),
        'username': u("guido"),
        'user_password_age': u("P90D"),
        # UnixUser-specific fields
        'group_id': 123,
        'user_id': 7874,
        'login_shell': u("/etc/profile"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
