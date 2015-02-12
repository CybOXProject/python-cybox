# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_kernel_hook_object import WinKernelHook
from cybox.test.objects import ObjectTestCase


class TestWinKernelHook(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsKernelHookObjectType"
    klass = WinKernelHook

    _full_dict = {
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
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
