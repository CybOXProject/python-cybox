# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_service_object import ServiceDescriptionList, WinService
from cybox.test import EntityTestCase
from cybox.test.common.hash_test import EMPTY_MD5
from cybox.test.objects import ObjectTestCase


class TestServiceDescriptionList(EntityTestCase, unittest.TestCase):
    klass = ServiceDescriptionList

    _full_dict = [
        'Description 1',
        'Description 2',
    ]


class TestWinService(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsServiceObjectType"
    klass = WinService

    _full_dict = {
        'service_dll_signature_exists': '',
        'service_dll_signature_verified': '',
        'description_list': TestServiceDescriptionList._full_dict,
        'display_name': '',
        'group_name': '',
        'service_name': '',
        'service_dll': '',
        'service_dll_certificate_issuer': '',
        'service_dll_certificate_subject': '',
        'service_dll_hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5}
        ],
        'service_dll_signature_description': '',
        'startup_command_line': '',
        'startup_type': '',
        'service_status': '',
        'service_type': '',
        'started_as': '',
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
