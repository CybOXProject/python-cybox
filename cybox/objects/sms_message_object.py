# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.sms_message_object as sms_binding
from cybox.common import ObjectProperties, HexBinary, String, DateTime, Integer, PositiveInteger


class SMSMessage(ObjectProperties):
    _binding = sms_binding
    _binding_class = sms_binding.SMSMessageObjectType
    _namespace = 'http://cybox.mitre.org/objects#SMSMessageObject-1'
    _XSI_NS = 'SMSMessageObj'
    _XSI_TYPE = "SMSMessageObjectType"

    is_premium = cybox.TypedField("is_premium")
    sender_phone_number = cybox.TypedField("Sender_Phone_Number", String)
    recipient_phone_number = cybox.TypedField("Recipient_Phone_Number", String)
    sent_datetime = cybox.TypedField("Sent_DateTime", DateTime)
    body = cybox.TypedField("Body", String)
    length = cybox.TypedField("Length", Integer)
    size = cybox.TypedField("Size", Integer)
    encoding = cybox.TypedField("Encoding", String)
    bits_per_character = cybox.TypedField("Bits_Per_Character", PositiveInteger)
    user_data_header = cybox.TypedField("User_Data_Header", HexBinary)
