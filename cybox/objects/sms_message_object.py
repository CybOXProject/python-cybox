# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.sms_message_object as sms_binding
from cybox.common import ObjectProperties, HexBinary, String, DateTime, Integer, PositiveInteger


class SMSMessage(ObjectProperties):
    _binding = sms_binding
    _binding_class = sms_binding.SMSMessageObjectType
    _namespace = 'http://cybox.mitre.org/objects#SMSMessageObject-1'
    _XSI_NS = 'SMSMessageObj'
    _XSI_TYPE = "SMSMessageObjectType"

    is_premium = fields.TypedField("is_premium")
    sender_phone_number = fields.TypedField("Sender_Phone_Number", String)
    recipient_phone_number = fields.TypedField("Recipient_Phone_Number", String)
    sent_datetime = fields.TypedField("Sent_DateTime", DateTime)
    body = fields.TypedField("Body", String)
    length = fields.TypedField("Length", Integer)
    size = fields.TypedField("Size", Integer)
    encoding = fields.TypedField("Encoding", String)
    bits_per_character = fields.TypedField("Bits_Per_Character", PositiveInteger)
    user_data_header = fields.TypedField("User_Data_Header", HexBinary)
