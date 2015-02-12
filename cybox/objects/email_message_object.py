# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.email_message_object as email_message_binding
from cybox.common import ObjectProperties, String, PositiveInteger, DateTime
from cybox.objects.address_object import Address, EmailAddress


class AttachmentReference(cybox.ObjectReference):
    _binding = email_message_binding
    _binding_class = email_message_binding.AttachmentReferenceType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class LinkReference(cybox.ObjectReference):
    _binding = email_message_binding
    _binding_class = email_message_binding.LinkReferenceType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class Attachments(cybox.ReferenceList):
    _binding = email_message_binding
    _binding_class = email_message_binding.AttachmentsType
    _binding_var = "File"
    _contained_type = AttachmentReference
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'


class Links(cybox.ReferenceList):
    _binding = email_message_binding
    _binding_class = email_message_binding.LinksType
    _binding_var = "Link"
    _contained_type = LinkReference
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'


class EmailRecipients(cybox.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailRecipientsType
    _binding_var = 'Recipient'
    _contained_type = EmailAddress
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'

    #EmailRecipients allows you to pass recipients via the constructor
    _try_cast = True


class ReceivedLine(cybox.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailReceivedLineType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"

    from_ = cybox.TypedField("From", String)
    by = cybox.TypedField("By", String)
    via = cybox.TypedField("Via", String)
    with_ = cybox.TypedField("With", String)
    for_ = cybox.TypedField("For", String)
    id_ = cybox.TypedField("ID", String)
    timestamp = cybox.TypedField("Timestamp", DateTime)

    # TODO: write function to try to parse a single string into this structure.


class ReceivedLineList(cybox.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailReceivedLineListType
    _binding_var = "Received"
    _contained_type = ReceivedLine
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class EmailHeader(cybox.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailHeaderType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"

    received_lines = cybox.TypedField("Received_Lines", ReceivedLineList)
    to = cybox.TypedField("To", EmailRecipients)
    cc = cybox.TypedField("CC", EmailRecipients)
    bcc = cybox.TypedField("BCC", EmailRecipients)
    from_ = cybox.TypedField("From", EmailAddress)
    subject = cybox.TypedField("Subject", String)
    in_reply_to = cybox.TypedField("In_Reply_To", String)
    date = cybox.TypedField("Date", DateTime)
    message_id = cybox.TypedField("Message_ID", String)
    sender = cybox.TypedField("Sender", EmailAddress)
    reply_to = cybox.TypedField("Reply_To", EmailAddress)
    errors_to = cybox.TypedField("Errors_To", String)
    boundary = cybox.TypedField("Boundary", String)
    content_type = cybox.TypedField("Content_Type", String)
    mime_version = cybox.TypedField("MIME_Version", String)
    precedence = cybox.TypedField("Precedence", String)
    user_agent = cybox.TypedField("User_Agent", String)
    x_mailer = cybox.TypedField("X_Mailer", String)
    x_originating_ip = cybox.TypedField("X_Originating_IP", Address)
    x_priority = cybox.TypedField("X_Priority", PositiveInteger)


class EmailMessage(ObjectProperties):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailMessageObjectType
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    _XSI_NS = "EmailMessageObj"
    _XSI_TYPE = "EmailMessageObjectType"

    header = cybox.TypedField("Header", EmailHeader)
    email_server = cybox.TypedField("Email_Server", String)
    raw_body = cybox.TypedField("Raw_Body", String)
    raw_header = cybox.TypedField("Raw_Header", String)
    attachments = cybox.TypedField("Attachments", Attachments)
    links = cybox.TypedField("Links", Links)

    # TODO: make an equivalent to "TypedField" for "Shortcuts"
    # Shortcut properties
    @property
    def to(self):
        return self.header.to

    @to.setter
    def to(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.to = value

    @property
    def from_(self):
        return self.header.from_

    @from_.setter
    def from_(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.from_ = value

    @property
    def subject(self):
        return self.header.subject

    @subject.setter
    def subject(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.subject = value

    @property
    def date(self):
        return self.header.date

    @date.setter
    def date(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.date = value

    @property
    def message_id(self):
        return self.header.message_id

    @message_id.setter
    def message_id(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.message_id = value

    @property
    def sender(self):
        return self.header.sender

    @sender.setter
    def sender(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.sender = value

    @property
    def reply_to(self):
        return self.header.reply_to

    @reply_to.setter
    def reply_to(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.reply_to = value

    @property
    def x_originating_ip(self):
        if not self.header:
            return None
        return self.header.x_originating_ip

    @x_originating_ip.setter
    def x_originating_ip(self, value):
        if not self.header:
            self.header = EmailHeader()
        self.header.x_originating_ip = value
