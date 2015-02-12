# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.win_kernel_object import WinKernel

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestWinKernel(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsKernelObjectType"
    klass = WinKernel

    _full_dict = {
        'idt': [
            {
                'type_attr': "897987987d9c87de",
                'offset_high': "78675b67a576e",
                'offset_low': "3543c5d3e43a5",
                'offset_middle': "abcde142897",
                'selector': "edcba1412"
            },
            {
                'type_attr': "897987987d9c87de11111",
                'offset_high': "78675b67a576e11111",
                'offset_low': "3543c5d3e43a511111",
                'offset_middle': "abcde14289711111",
                'selector': "edcba141211111"
            }
        ],
        'ssdt': [
            {
                'hooked': False,
                'service_table_base': "a86dc86b6e",
                'service_counter_table_base': "098b89e098dc809a",
                'number_of_services': 2,
                'argument_table_base': "809a09ad890c89ee14124"
            }, 
            {
                'hooked': True,
                'service_table_base': "a86dc86b6e11111",
                'service_counter_table_base': "098b89e098dc809a11111",
                'number_of_services': 3,
                'argument_table_base': "809a09ad890c89ee1412411111"
            }
        ],
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
