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
        u('Provides infrastructure support for deploying Store applications. This service is started on demand and if disabled Store applications will not be deployed to the system, and may not function properly.'),
        u('Description 2'),
    ]


class TestWinService(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsServiceObjectType"
    klass = WinService

    _full_dict = {
        'service_dll_signature_exists': True,
        'service_dll_signature_verified': True,
        'description_list': TestServiceDescriptionList._full_dict,
        'display_name': u('AppXSvc'),
        'group_name': u('appx'),
        'service_name': u('AppX Deployment Service (AppXSVC)'),
        'service_dll': u('appxsvc.dll'),
        'service_dll_certificate_issuer': u('Microsoft Corporation'),
        'service_dll_certificate_subject': u('Frabrikam'),
        'service_dll_hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5}
        ],
        'service_dll_signature_description': u('Something'),
        'startup_command_line': u('C:\WINDOWS\system32\svchost.exe -k wsappx -p'),
        'startup_type': u('SERVICE_AUTO_START'),
        'service_status': u('SERVICE_PAUSED'),
        'service_type': u('SERVICE_KERNEL_DRIVER'),
        'started_as': u('Local Service'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
