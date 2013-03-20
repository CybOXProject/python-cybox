import unittest

from cybox.common import String
from cybox.objects.address_object import Address, EmailAddress
from cybox.objects.email_message_object import (EmailMessage, EmailRecipients,
                                                OptionalHeader)
from cybox.test import round_trip
from cybox.test.objects import ObjectTestCase


class TestEmailRecipients(unittest.TestCase):
    def setUp(self):
        self.email1 = "victim1@target.com"
        self.email2 = "victim2@target.com"

    # Five different ways to build an EmailRecipients list

    def test_list(self):
        recips = EmailRecipients(Address(self.email1, Address.CAT_EMAIL),
                                 Address(self.email2, Address.CAT_EMAIL))
        self._compare(recips)

    def test_list2(self):
        recips = EmailRecipients(EmailAddress(self.email1),
                                 EmailAddress(self.email2))
        self._compare(recips)

    def test_list3(self):
        recips = EmailRecipients(self.email1, self.email2)
        self._compare(recips)

    def test_list4(self):
        recips = EmailRecipients()
        recips.add(self.email1)
        recips.add(self.email2)
        self._compare(recips)

    def test_list5(self):
        recips = EmailRecipients()
        recips.add(EmailAddress(self.email1))
        recips.add(EmailAddress(self.email2))
        self._compare(recips)

    def _compare(self, recips):
        recips2 = round_trip(recips, EmailRecipients)
        self.assertEqual(2, len(recips2.recipients))

        recips_dict = recips2.to_dict()
        self.assertEqual(recips_dict[0]['category'], Address.CAT_EMAIL)
        self.assertEqual(recips_dict[0]['address_value'], self.email1)
        self.assertEqual(recips_dict[1]['category'], Address.CAT_EMAIL)
        self.assertEqual(recips_dict[1]['address_value'], self.email2)

    def test_invalid_recip_type(self):
        for a in [dict(a=1), 1, True, list('123')]:
            self.assertRaises(ValueError, EmailRecipients, a)

class TestOptionalHeader(unittest.TestCase):
    def test_roundtrip(self):
        d = {
              'boundary': "----MIME_BOUNDARY------",
              'content_type': "mime/multi-part",
              'mime_version': "1.0",
              'precedence': "High",
              'x_mailer': "Outlook Express",
              'x_originating_ip': {'address_value': "1.2.3.4",
                                   'category': "ipv4-addr",
                                   'xsi:type': Address._XSI_TYPE},
              'x_priority': 3,
            }
        self.maxDiff = None
        o = OptionalHeader.from_dict(d)
        o2 = round_trip(o, OptionalHeader)
        d2 = o2.to_dict()
        self.assertEqual(d, d2)


class TestEmailMessage(unittest.TestCase, ObjectTestCase):
    object_type = "EmailMessageObjectType"
    klass = EmailMessage

    def test_roundtrip_basic(self):
        msg_dict = {'header': {
                                'from': "sender@domain.org",
                                'to': ["recip@victim.org"],
                                'subject': "Howdy!"
                               },
                     'raw_body': "This is a test. This is only a test.",
                    }
        msg_obj = EmailMessage.object_from_dict(msg_dict)
        msg_dict2 = EmailMessage.dict_from_object(msg_obj)

        # Don't want to compare dictionaries directly since email addresses
        # will have been expanded to full dictionaries with "address_value"
        # and "category"
        self.assertEqual(msg_dict2['header']['from']['address_value'],
                         msg_dict['header']['from'])
        self.assertEqual(msg_dict2['header']['to'][0]['address_value'],
                         msg_dict['header']['to'][0])
        self.assertEqual(msg_dict2['header']['subject'],
                         msg_dict['header']['subject'])
        self.assertEqual(msg_dict2['raw_body'],
                         msg_dict['raw_body'])
        self.assertEqual(msg_dict2['xsi:type'], EmailMessage._XSI_TYPE)

        # Make sure extra keys didn't sneak into the output.
        self.assertFalse('attachments' in msg_dict2)
        self.assertFalse('optional_header' in msg_dict2)
        self.assertFalse('email_server' in msg_dict2)
        self.assertFalse('raw_header' in msg_dict2)
        self.assertFalse('cc' in msg_dict2['header'])
        self.assertFalse('bcc' in msg_dict2['header'])
        self.assertFalse('in_reply_to' in msg_dict2['header'])
        self.assertFalse('date' in msg_dict2['header'])
        self.assertFalse('message_id' in msg_dict2['header'])
        self.assertFalse('sender' in msg_dict2['header'])
        self.assertFalse('reply_to' in msg_dict2['header'])
        self.assertFalse('errors_to' in msg_dict2['header'])

    def test_from_date(self):
        date_str = "Thu, 14 Feb 2013 11:28:42 -0500"
        isoformat = "2013-02-14T11:28:42-05:00"

        d = {'header': {'date': date_str}}
        msg = EmailMessage.from_dict(d)
        self.assertEqual(msg.date._serialize_value(), isoformat)


if __name__ == "__main__":
    unittest.main()
