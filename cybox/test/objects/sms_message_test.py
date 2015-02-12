# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.sms_message_object import SMSMessage

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestSMSMessage(ObjectTestCase, unittest.TestCase):
    object_type = "SMSMessageObjectType"
    klass = SMSMessage

    _full_dict = {
        'is_premium': False,
        'sender_phone_number': '903-5768',
        'recipient_phone_number': '867-5309',
        'body': "Just a body",
        'length': 100,
        'size': 150,
        'encoding': "sample encoding",
        'bits_per_character': 8,
        'user_data_header': "abc3298edf",
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
