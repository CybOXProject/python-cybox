# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields
from mixbox.vendor import six

import cybox.bindings.email_message_object as email_message_binding
from cybox.common import ObjectProperties, String, PositiveInteger, DateTime
from cybox.objects.address_object import Address, EmailAddress


class _Reference(object):
    """Mixin class for AttachmentReference and LinkReference.

    By providing the __init__ constructor, it allows passing in IDs (as
    strings) where otherwise building a new object would be required.

    For example, instead of:
        uri = URI("http://www.example.com")
        links = Links()

        linkref = LinkReference()
        linkref.object_reference = uri.parent.id_
        links.append(linkref)

    You can do:
        uri = URI("http://www.example.com")
        links = Links()
        links.append(uri.parent.id_)
    """

    object_reference = fields.TypedField("object_reference")

    def __init__(self, object_reference=None):
        super(_Reference, self).__init__()
        self.object_reference = object_reference


class _ReferenceList(object):
    """Mixin class that allows _References to be added to a list."""

    def _fix_value(self, value):
        if isinstance(value, six.string_types):
            return self._contained_type(value)


class AttachmentReference(_Reference, entities.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.AttachmentReferenceType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class LinkReference(_Reference, entities.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.LinkReferenceType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class Attachments(_ReferenceList, entities.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.AttachmentsType
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    file = fields.TypedField("File", AttachmentReference, multiple=True)


class Links(_ReferenceList, entities.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.LinksType
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    link = fields.TypedField("Link", LinkReference, multiple=True)


class EmailRecipients(entities.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailRecipientsType
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    _try_cast = True # EmailRecipients allows you to pass recipients via the constructor
    recipient = fields.TypedField("Recipient", EmailAddress, multiple=True)


class ReceivedLine(entities.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailReceivedLineType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"

    from_ = fields.TypedField("From", String)
    by = fields.TypedField("By", String)
    via = fields.TypedField("Via", String)
    with_ = fields.TypedField("With", String)
    for_ = fields.TypedField("For", String)
    id_ = fields.TypedField("ID", String)
    timestamp = fields.TypedField("Timestamp", DateTime)

    # TODO: write function to try to parse a single string into this structure.


class ReceivedLineList(entities.EntityList):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailReceivedLineListType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"
    received = fields.TypedField("Received", ReceivedLine, multiple=True)


class EmailHeader(entities.Entity):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailHeaderType
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"

    received_lines = fields.TypedField("Received_Lines", ReceivedLineList)
    to = fields.TypedField("To", EmailRecipients)
    cc = fields.TypedField("CC", EmailRecipients)
    bcc = fields.TypedField("BCC", EmailRecipients)
    from_ = fields.TypedField("From", EmailAddress)
    subject = fields.TypedField("Subject", String)
    in_reply_to = fields.TypedField("In_Reply_To", String)
    date = fields.TypedField("Date", DateTime)
    message_id = fields.TypedField("Message_ID", String)
    sender = fields.TypedField("Sender", EmailAddress)
    reply_to = fields.TypedField("Reply_To", EmailAddress)
    errors_to = fields.TypedField("Errors_To", String)
    boundary = fields.TypedField("Boundary", String)
    content_type = fields.TypedField("Content_Type", String)
    mime_version = fields.TypedField("MIME_Version", String)
    precedence = fields.TypedField("Precedence", String)
    user_agent = fields.TypedField("User_Agent", String)
    x_mailer = fields.TypedField("X_Mailer", String)
    x_originating_ip = fields.TypedField("X_Originating_IP", Address)
    x_priority = fields.TypedField("X_Priority", PositiveInteger)


class EmailMessage(ObjectProperties):
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailMessageObjectType
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    _XSI_NS = "EmailMessageObj"
    _XSI_TYPE = "EmailMessageObjectType"

    header = fields.TypedField("Header", EmailHeader)
    email_server = fields.TypedField("Email_Server", String)
    raw_body = fields.TypedField("Raw_Body", String)
    raw_header = fields.TypedField("Raw_Header", String)
    attachments = fields.TypedField("Attachments", Attachments)
    links = fields.TypedField("Links", Links)

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
