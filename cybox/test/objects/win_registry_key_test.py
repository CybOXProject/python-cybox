# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.compat import long
from cybox.objects.win_registry_key_object import WinRegistryKey
from cybox.test.objects import ObjectTestCase


class TestWinRegistryKey(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsRegistryKeyObjectType"
    klass = WinRegistryKey

    _full_dict = {
        'key': u("\\SOFTWARE\\Microsoft\\Windows\\Windows Error Reporting"),
        'hive': u("HKEY_LOCAL_MACHINE"),
        'number_values': 6,
        'values': [
            {
                'name': u("Disabled"),
                'data': u("1"),
                'datatype': u("REG_DWORD"),
                'byte_runs': [{'length': 1, 'byte_run_data': u("A")}],
            },
            {
                'name': u("ErrorPort"),
                'data': u("\\WindowsErrorReportingServicePort"),
                'datatype': u("REG_SZ"),
            },
        ],
        'modified_time': u("2013-08-08T15:15:15-04:00"),
        'creator_username': u("gback"),
        'handle_list': [
            {
                'name': u("RegHandle"),
                'pointer_count': long(1),
                'type': u("RegistryKey"),
                'xsi:type': u('WindowsHandleObjectType'),
            },
        ],
        'number_subkeys': 1,
        'subkeys': [
            {
                'key': u("Consent"),
                'number_values': 1,
                'values': [
                    {
                        'name': u("NewUserDefaultConsent"),
                        'data': u("1"),
                        'datatype': u("REG_DWORD"),
                    },
                ],
                'xsi:type': 'WindowsRegistryKeyObjectType',
            },
        ],
        'byte_runs': [
            {'length': 4, 'byte_run_data': u("z!%f")},
            {'offset': 0x1000, 'length': 8, 'byte_run_data': u("%40V.,2@")},
        ],
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
