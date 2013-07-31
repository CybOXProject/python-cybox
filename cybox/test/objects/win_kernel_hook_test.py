# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.address_object import Address
from cybox.objects.win_kernel_hook_object import WinKernelHook
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestWinKernelHook(unittest.TestCase, ObjectTestCase):
    object_type = "WindowsKernelHookObjectType"
    klass = WinKernelHook

    def test_round_trip(self):
        hook_dict = {
                        'digital_signature_hooking': {
                                'signature_exists': True,
                                'signature_verified': False,
                                'signature_description': "Sig of hooking code",
                            },
                        'digital_signature_hooked': {
                                'signature_verified': True,
                                'signature_description': "Sig of hooked code",
                            },
                        'hooking_address': 0xc001d1ce,
                        'hook_description': "A powerful left hook",
                        'hooked_function': "DoSomeStuff",
                        'hooked_module': "Some Module",
                        'hooking_module': "Another Module",
                        'type': "Instruction_Hooking",
                        'xsi:type': 'WindowsKernelHookObjectType'
                    }
        hook_dict2 = cybox.test.round_trip_dict(WinKernelHook, hook_dict)
        self.maxDiff = None
        self.assertEqual(hook_dict, hook_dict2)


if __name__ == "__main__":
    unittest.main()
