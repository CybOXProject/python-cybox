# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
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

    def __init__(self, *args):
        super(EmailRecipients, self).__init__()
        for arg in args:
            if isinstance(arg, list):
                self.extend(arg)
            else:
                self.append(arg)


class ReceivedLine(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"
    _binding = email_message_binding
    _binding_class = email_message_binding.EmailReceivedLineType

    from_ = cybox.TypedField("From", String)
    by = cybox.TypedField("By", String)
    with_ = cybox.TypedField("With", String)
    for_ = cybox.TypedField("For", String)
    id_ = cybox.TypedField("ID", String)
    timestamp = cybox.TypedField("Timestamp", DateTime)

    __vars__ = (from_, by, with_, for_, id_, timestamp)

    # TODO: write function to try to parse a single string into this structure.


class ReceivedLineList(cybox.EntityList):
    _binding_class = email_message_binding.EmailReceivedLineListType
    _binding_var = "Received"
    _contained_type = ReceivedLine
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"


class EmailHeader(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#EmailMessageObject-2"

    from_ = cybox.TypedField("From", EmailAddress)
    subject = cybox.TypedField("Subject", String)
    date = cybox.TypedField("Date", DateTime)
    message_id = cybox.TypedField("Message_ID", String)
    sender = cybox.TypedField("Sender", EmailAddress)

    def __init__(self):
        self.received_lines = None
        self.to = None
        self.cc = None
        self.bcc = None

        self.in_reply_to = None

        self.reply_to = None
        self.errors_to = None
        self.boundary = None
        self.content_type = None
        self.mime_version = None
        self.precedence = None
        self.user_agent = None
        self.x_mailer = None
        self.x_originating_ip = None
        self.x_priority = None

    @property
    def received_lines(self):
        return self._received_lines

    @received_lines.setter
    def received_lines(self, value):
        if value is not None and not isinstance(value, ReceivedLineList):
            value = ReceivedLineList(value)
        self._received_lines = value

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):
        if value is not None and not isinstance(value, EmailRecipients):
            value = EmailRecipients(value)
        self._to = value

    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        if value is not None and not isinstance(value, EmailRecipients):
            value = EmailRecipients(value)
        self._cc = value

    @property
    def bcc(self):
        return self._bcc

    @bcc.setter
    def bcc(self, value):
        if value is not None and not isinstance(value, EmailRecipients):
            value = EmailRecipients(value)
        self._bcc = value

    @property
    def x_originating_ip(self):
        return self._x_originating_ip

    @x_originating_ip.setter
    def x_originating_ip(self, value):
        if value is not None and not isinstance(value, Address):
            value = Address(value, category=Address.CAT_IPV4)
        self._x_originating_ip = value

    def to_obj(self):
        header_obj = email_message_binding.EmailHeaderType()

        if self.received_lines:
            header_obj.set_Received_Lines(self.received_lines.to_obj())
        if self.to:
            header_obj.set_To(self.to.to_obj())
        if self.cc:
            header_obj.set_CC(self.cc.to_obj())
        if self.bcc:
            header_obj.set_BCC(self.bcc.to_obj())
        if self.from_:
            header_obj.set_From(self.from_.to_obj())
        if self.subject:
            header_obj.set_Subject(self.subject.to_obj())
        if self.in_reply_to:
            header_obj.set_In_Reply_To(self.in_reply_to.to_obj())
        if self.date:
            header_obj.set_Date(self.date.to_obj())
        if self.message_id:
            header_obj.set_Message_ID(self.message_id.to_obj())
        if self.sender:
            header_obj.set_Sender(self.sender.to_obj())
        if self.reply_to:
            header_obj.set_Reply_To(self.reply_to.to_obj())
        if self.errors_to:
            header_obj.set_Errors_To(self.errors_to.to_obj())
        if self.boundary:
            header_obj.set_Boundary(self.boundary.to_obj())
        if self.content_type:
            header_obj.set_Content_Type(self.content_type.to_obj())
        if self.mime_version:
            header_obj.set_MIME_Version(self.mime_version.to_obj())
        if self.precedence:
            header_obj.set_Precedence(self.precedence.to_obj())
        if self.user_agent:
            header_obj.set_User_Agent(self.user_agent.to_obj())
        if self.x_mailer:
            header_obj.set_X_Mailer(self.x_mailer.to_obj())
        if self.x_originating_ip:
            header_obj.set_X_Originating_IP(self.x_originating_ip.to_obj())
        if self.x_priority:
            header_obj.set_X_Priority(self.x_priority.to_obj())

        return header_obj

    def to_dict(self):
        header_dict = {}

        if self.received_lines:
            header_dict['received_lines'] = self.received_lines.to_list()
        if self.to:
            header_dict['to'] = self.to.to_list()
        if self.cc:
            header_dict['cc'] = self.cc.to_list()
        if self.bcc:
            header_dict['bcc'] = self.bcc.to_list()
        if self.from_:
            header_dict['from'] = self.from_.to_dict()
        if self.subject:
            header_dict['subject'] = self.subject.to_dict()
        if self.in_reply_to:
            header_dict['in_reply_to'] = self.in_reply_to.to_dict()
        if self.date:
            header_dict['date'] = self.date.to_dict()
        if self.message_id:
            header_dict['message_id'] = self.message_id.to_dict()
        if self.sender:
            header_dict['sender'] = self.sender.to_dict()
        if self.reply_to:
            header_dict['reply_to'] = self.reply_to.to_dict()
        if self.errors_to:
            header_dict['errors_to'] = self.errors_to.to_dict()
        if self.boundary:
            header_dict['boundary'] = self.boundary.to_dict()
        if self.content_type:
            header_dict['content_type'] = self.content_type.to_dict()
        if self.mime_version:
            header_dict['mime_version'] = self.mime_version.to_dict()
        if self.precedence:
            header_dict['precedence'] = self.precedence.to_dict()
        if self.user_agent:
            header_dict['user_agent'] = self.user_agent.to_dict()
        if self.x_mailer:
            header_dict['x_mailer'] = self.x_mailer.to_dict()
        if self.x_originating_ip:
            header_dict['x_originating_ip'] = self.x_originating_ip.to_dict()
        if self.x_priority:
            header_dict['x_priority'] = self.x_priority.to_dict()

        return header_dict

    @staticmethod
    def from_obj(header_obj):
        if not header_obj:
            return None

        header = EmailHeader()

        header.received_lines = ReceivedLineList.from_obj(header_obj.get_Received_Lines())
        header.to = EmailRecipients.from_obj(header_obj.get_To())
        header.cc = EmailRecipients.from_obj(header_obj.get_CC())
        header.bcc = EmailRecipients.from_obj(header_obj.get_BCC())
        header.from_ = Address.from_obj(header_obj.get_From())
        header.subject = String.from_obj(header_obj.get_Subject())
        header.in_reply_to = String.from_obj(header_obj.get_In_Reply_To())
        header.date = DateTime.from_obj(header_obj.get_Date())
        header.message_id = String.from_obj(header_obj.get_Message_ID())
        header.sender = Address.from_obj(header_obj.get_Sender())
        header.reply_to = Address.from_obj(header_obj.get_Reply_To())
        header.errors_to = String.from_obj(header_obj.get_Errors_To())
        header.boundary = String.from_obj(header_obj.get_Boundary())
        header.content_type = String.from_obj(header_obj.get_Content_Type())
        header.mime_version = String.from_obj(header_obj.get_MIME_Version())
        header.precedence = String.from_obj(header_obj.get_Precedence())
        header.user_agent = String.from_obj(header_obj.get_User_Agent())
        header.x_mailer = String.from_obj(header_obj.get_X_Mailer())
        header.x_originating_ip = Address.from_obj(header_obj.get_X_Originating_IP())
        header.x_priority = PositiveInteger.from_obj(header_obj.get_X_Priority())

        return header

    @staticmethod
    def from_dict(header_dict):
        if not header_dict:
            return None

        header = EmailHeader()

        header.received_lines = ReceivedLineList.from_list(header_dict.get('received_lines'))
        header.to = EmailRecipients.from_list(header_dict.get('to'))
        header.cc = EmailRecipients.from_list(header_dict.get('cc'))
        header.bcc = EmailRecipients.from_list(header_dict.get('bcc'))
        header.from_ = EmailAddress.from_dict(header_dict.get('from'))
        header.subject = String.from_dict(header_dict.get('subject'))
        header.in_reply_to = String.from_dict(header_dict.get('in_reply_to'))
        header.date = DateTime.from_dict(header_dict.get('date'))
        header.message_id = String.from_dict(header_dict.get('message_id'))
        header.sender = EmailAddress.from_dict(header_dict.get('sender'))
        header.reply_to = EmailAddress.from_dict(header_dict.get('reply_to'))
        header.errors_to = String.from_dict(header_dict.get('errors_to'))
        header.boundary = String.from_dict(header_dict.get('boundary'))
        header.content_type = String.from_dict(header_dict.get('content_type'))
        header.mime_version = String.from_dict(header_dict.get('mime_version'))
        header.precedence = String.from_dict(header_dict.get('precedence'))
        header.user_agent = String.from_dict(header_dict.get('user_agent'))
        header.x_mailer = String.from_dict(header_dict.get('x_mailer'))
        header.x_originating_ip = Address.from_dict(header_dict.get('x_originating_ip'), Address.CAT_IPV4)
        header.x_priority = PositiveInteger.from_dict(header_dict.get('x_priority'))

        return header


class EmailMessage(ObjectProperties):
    _namespace = 'http://cybox.mitre.org/objects#EmailMessageObject-2'
    _XSI_NS = "EmailMessageObj"
    _XSI_TYPE = "EmailMessageObjectType"

    def __init__(self):
        super(EmailMessage, self).__init__()

        self.header = None
        self.email_server = None
        self.raw_body = None
        self.raw_header = None
        self.attachments = None
        self.links = None

    @property
    def email_server(self):
        return self._email_server

    @email_server.setter
    def email_server(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._email_server = value

    @property
    def raw_body(self):
        return self._raw_body

    @raw_body.setter
    def raw_body(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._raw_body = value

    @property
    def raw_header(self):
        return self._raw_header

    @raw_header.setter
    def raw_header(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._raw_header = value

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

    def to_obj(self):
        email_obj = email_message_binding.EmailMessageObjectType()
        super(EmailMessage, self).to_obj(email_obj)

        if self.header:
            email_obj.set_Header(self.header.to_obj())
        if self.email_server:
            email_obj.set_Email_Server(self.email_server.to_obj())
        if self.raw_body:
            email_obj.set_Raw_Body(self.raw_body.to_obj())
        if self.raw_header:
            email_obj.set_Raw_Header(self.raw_header.to_obj())
        if self.attachments:
            email_obj.set_Attachments(self.attachments.to_obj())
        if self.links:
            email_obj.set_Links(self.links.to_obj())

        return email_obj

    def to_dict(self):
        email_dict = {}
        super(EmailMessage, self).to_dict(email_dict)

        if self.header:
            email_dict['header'] = self.header.to_dict()
        if self.email_server:
            email_dict['email_server'] = self.email_server.to_dict()
        if self.raw_body:
            email_dict['raw_body'] = self.raw_body.to_dict()
        if self.raw_header:
            email_dict['raw_header'] = self.raw_header.to_dict()
        if self.attachments:
            email_dict['attachments'] = self.attachments.to_list()
        if self.links:
            email_dict['links'] = self.links.to_list()

        return email_dict

    @staticmethod
    def from_obj(message_obj):
        message = EmailMessage()
        ObjectProperties.from_obj(message_obj, message)

        message.header = EmailHeader.from_obj(message_obj.get_Header())
        message.email_server = String.from_obj(message_obj.get_Email_Server())
        message.raw_body = String.from_obj(message_obj.get_Raw_Body())
        message.raw_header = String.from_obj(message_obj.get_Raw_Header())
        message.attachments = Attachments.from_obj(message_obj.get_Attachments())
        message.links = Links.from_obj(message_obj.get_Links())

        return message

    @staticmethod
    def from_dict(message_dict):
        message = EmailMessage()
        ObjectProperties.from_dict(message_dict, message)

        message.header = EmailHeader.from_dict(message_dict.get('header'))
        message.email_server = String.from_dict(message_dict.get('email_server'))
        message.raw_body = String.from_dict(message_dict.get('raw_body'))
        message.raw_header = String.from_dict(message_dict.get('raw_header'))
        message.attachments = Attachments.from_list(message_dict.get('attachments'))
        message.links = Links.from_list(message_dict.get('links'))

        return message
