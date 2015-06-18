# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_network_share_object import WinNetworkShare
from cybox.test.objects import ObjectTestCase


class TestWinNetworkShare(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsNetworkShareObjectType"
    klass = WinNetworkShare

    _full_dict = {
        'access_read': True,
        'access_write': False,
        'access_create': True,
        'access_exec': False,
        'access_delete': True,
        'access_atrib': False,
        'access_perm': True,
        'access_all': False,
        'current_uses': 1,
        'local_path': u("Z:/"),
        'max_uses': 10,
        'netname': u("shared drive"),
        'type': u("Folder"),
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
