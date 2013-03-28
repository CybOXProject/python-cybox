import cybox
import cybox.bindings.email_message_object_1_2 as email_message_binding
from cybox.common import DefinedObject, String, PositiveInteger, DateTime
from cybox.objects.file_object import File
from cybox.objects.uri_object import URI
from cybox.objects.address_object import Address, EmailAddress


class EmailRecipients(cybox.Entity):
    def __init__(self, *args):
        self.recipients = []
        for arg in args:
            self.add(arg)

    def add(self, recipient):
        if recipient is not None and not isinstance(recipient, Address):
            if isinstance(recipient, basestring):
                recipient = EmailAddress(recipient)
            else:
                msg = "Cannot convert {} (type {}) to an Address"
                raise ValueError(msg.format(recipient, type(recipient)))
        self.recipients.append(recipient)

    def __nonzero__(self):
        return bool(self.recipients)

    __bool__ = __nonzero__

    def to_obj(self):
        recipients_obj = email_message_binding.EmailRecipientsType()
        for recipient in self.recipients:
            recipients_obj.add_Recipient(recipient.to_obj())
        return recipients_obj

    def to_dict(self):
        return [r.to_dict() for r in self.recipients]

    @staticmethod
    def from_obj(recipients_obj):
        r = EmailRecipients()
        if recipients_obj is not None:
            r.recipients = [Address.from_obj(a)
                                for a in recipients_obj.get_Recipient()]
        return r

    @staticmethod
    def from_dict(recipients_dict):
        if not recipients_dict:
            return None

        # recipients_dict should really be a list, not a dict
        r = EmailRecipients()
        if recipients_dict is not None:
            r.recipients = [Address.from_dict(a, Address.CAT_EMAIL)
                                for a in recipients_dict]
        return r


class EmailHeader(cybox.Entity):
    def __init__(self):
        self.to = None
        self.cc = None
        self.bcc = None
        self.from_ = None
        self.subject = None
        self.in_reply_to = None
        self.date = None
        self.message_id = None
        self.sender = None
        self.reply_to = None
        self.errors_to = None

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
    def from_(self):
        return self._from

    @from_.setter
    def from_(self, value):
        if value is not None and not isinstance(value, Address):
            value = EmailAddress(value)
        self._from = value

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._subject = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if value is not None and not isinstance(value, DateTime):
            value = DateTime(value)
        self._date = value

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._message_id = value

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        if value is not None and not isinstance(value, Address):
            value = EmailAddress(value)
        self._sender = value

    def to_obj(self):
        header_obj = email_message_binding.EmailHeaderType()

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

        return header_obj

    def to_dict(self):
        header_dict = {}

        if self.to:
            header_dict['to'] = self.to.to_dict()
        if self.cc:
            header_dict['cc'] = self.cc.to_dict()
        if self.bcc:
            header_dict['bcc'] = self.bcc.to_dict()
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

        return header_dict

    @staticmethod
    def from_obj(header_obj):
        header = EmailHeader()

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

        return header

    @staticmethod
    def from_dict(header_dict):
        header = EmailHeader()

        header.to = EmailRecipients.from_dict(header_dict.get('to'))
        header.cc = EmailRecipients.from_dict(header_dict.get('cc'))
        header.bcc = EmailRecipients.from_dict(header_dict.get('bcc'))
        header.from_ = Address.from_dict(header_dict.get('from'), Address.CAT_EMAIL)
        header.subject = String.from_dict(header_dict.get('subject'))
        header.in_reply_to = String.from_dict(header_dict.get('in_reply_to'))
        header.date = DateTime.from_dict(header_dict.get('date'))
        header.message_id = String.from_dict(header_dict.get('message_id'))
        header.sender = Address.from_dict(header_dict.get('sender'), Address.CAT_EMAIL)
        header.reply_to = Address.from_dict(header_dict.get('reply_to'), Address.CAT_EMAIL)
        header.errors_to = String.from_dict(header_dict.get('errors_to'))

        return header


class OptionalHeader(cybox.Entity):
    def __init__(self):
        self.boundary = None
        self.content_type = None
        self.mime_version = None
        self.precedence = None
        self.x_mailer = None
        self.x_originating_ip = None
        self.x_priority = None

    @property
    def x_originating_ip(self):
        return self._x_originating_ip

    @x_originating_ip.setter
    def x_originating_ip(self, value):
        if value is not None and not isinstance(value, Address):
            value = Address(value, category=Address.CAT_IPV4)
        self._x_originating_ip = value

    def to_obj(self):
        opt_header_obj = email_message_binding.EmailOptionalHeaderType()

        if self.boundary:
            opt_header_obj.set_Boundary(self.boundary.to_obj())
        if self.content_type:
            opt_header_obj.set_Content_Type(self.content_type.to_obj())
        if self.mime_version:
            opt_header_obj.set_MIME_Version(self.mime_version.to_obj())
        if self.precedence:
            opt_header_obj.set_Precedence(self.precedence.to_obj())
        if self.x_mailer:
            opt_header_obj.set_X_Mailer(self.x_mailer.to_obj())
        if self.x_originating_ip:
            opt_header_obj.set_X_Originating_IP(self.x_originating_ip.to_obj())
        if self.x_priority:
            opt_header_obj.set_X_Priority(self.x_priority.to_obj())

        return opt_header_obj

    def to_dict(self):
        opt_header_dict = {}

        if self.boundary:
            opt_header_dict['boundary'] = self.boundary.to_dict()
        if self.content_type:
            opt_header_dict['content_type'] = self.content_type.to_dict()
        if self.mime_version:
            opt_header_dict['mime_version'] = self.mime_version.to_dict()
        if self.precedence:
            opt_header_dict['precedence'] = self.precedence.to_dict()
        if self.x_mailer:
            opt_header_dict['x_mailer'] = self.x_mailer.to_dict()
        if self.x_originating_ip:
            opt_header_dict['x_originating_ip'] = self.x_originating_ip.to_dict()
        if self.x_priority:
            opt_header_dict['x_priority'] = self.x_priority.to_dict()

        return opt_header_dict

    @staticmethod
    def from_obj(opt_header_obj):
        if not opt_header_obj:
            return None

        opt_header = OptionalHeader()

        opt_header.boundary = String.from_obj(opt_header_obj.get_Boundary())
        opt_header.content_type = String.from_obj(opt_header_obj.get_Content_Type())
        opt_header.mime_version = String.from_obj(opt_header_obj.get_MIME_Version())
        opt_header.precedence = String.from_obj(opt_header_obj.get_Precedence())
        opt_header.x_mailer = String.from_obj(opt_header_obj.get_X_Mailer())
        opt_header.x_originating_ip = Address.from_obj(opt_header_obj.get_X_Originating_IP())
        opt_header.x_priority = PositiveInteger.from_obj(opt_header_obj.get_X_Priority())

        return opt_header

    @staticmethod
    def from_dict(opt_header_dict):
        if not opt_header_dict:
            return None

        opt_header = OptionalHeader()

        opt_header.boundary = String.from_dict(opt_header_dict.get('boundary'))
        opt_header.content_type = String.from_dict(opt_header_dict.get('content_type'))
        opt_header.mime_version = String.from_dict(opt_header_dict.get('mime_version'))
        opt_header.precedence = String.from_dict(opt_header_dict.get('precedence'))
        opt_header.x_mailer = String.from_dict(opt_header_dict.get('x_mailer'))
        opt_header.x_originating_ip = Address.from_dict(opt_header_dict.get('x_originating_ip'), Address.CAT_IPV4)
        opt_header.x_priority = PositiveInteger.from_dict(opt_header_dict.get('x_priority'))

        return opt_header


class EmailMessage(DefinedObject):
    _XSI_TYPE = "EmailMessageObjectType"

    def __init__(self):
        super(EmailMessage, self).__init__()
        self.attachments = []
        self.links = []
        self.header = EmailHeader()
        self.optional_header = None
        self.email_server = None
        self.raw_body = None
        self.raw_header = None

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
        self.header.to = value

    @property
    def from_(self):
        return self.header.from_

    @from_.setter
    def from_(self, value):
        self.header.from_ = value

    @property
    def subject(self):
        return self.header.subject

    @subject.setter
    def subject(self, value):
        self.header.subject = value

    @property
    def date(self):
        return self.header.date

    @date.setter
    def date(self, value):
        self.header.date = value

    @property
    def message_id(self):
        return self.header.message_id

    @message_id.setter
    def message_id(self, value):
        self.header.message_id = value

    @property
    def sender(self):
        return self.header.sender

    @sender.setter
    def sender(self, value):
        self.header.sender = value

    @property
    def reply_to(self):
        return self.header.reply_to

    @reply_to.setter
    def reply_to(self, value):
        self.header.reply_to = value

    @property
    def x_originating_ip(self):
        if not self.optional_header:
            return None
        return self.optional_header.x_originating_ip

    @x_originating_ip.setter
    def x_originating_ip(self, value):
        if not self.optional_header:
            self.optional_header = OptionalHeader()
        self.optional_header.x_originating_ip = value

    def to_obj(self):
        email_obj = email_message_binding.EmailMessageObjectType()

        email_obj.set_anyAttributes_({'xsi:type': 'EmailMessageObj:EmailMessageObjectType'})
        if self.attachments:
            attachments_obj = email_message_binding.AttachmentsType()
            for file_ in self.attachments:
                attachments_obj.add_File(file_.to_obj())
            email_obj.set_Attachments(attachments_obj)
        if self.links:
            links_obj = email_message_binding.LinksType()
            for uri in self.links:
                links_obj.add_Link(uri.to_obj())
            email_obj.set_Links(links_obj)
        email_obj.set_Header(self.header.to_obj())
        if self.optional_header:
            email_obj.set_Optional_Header(self.optional_header.to_obj())
        if self.email_server:
            email_obj.set_Email_Server(self.email_server.to_obj())
        if self.raw_body:
            email_obj.set_Raw_Body(self.raw_body.to_obj())
        if self.raw_header:
            email_obj.set_Raw_Header(self.raw_header.to_obj())

        return email_obj

    def to_dict(self):
        email_dict = {}
        super(EmailMessage, self)._populate_dict(email_dict)

        if self.attachments:
            email_dict['attachments'] = [a.to_dict() for a in self.attachments]
        if self.links:
            email_dict['links'] = [l.to_dict() for l in self.links]
        email_dict['header'] = self.header.to_dict()
        if self.optional_header:
            email_dict['optional_header'] = self.optional_header.to_dict()
        if self.email_server:
            email_dict['email_server'] = self.email_server.to_dict()
        if self.raw_body:
            email_dict['raw_body'] = self.raw_body.to_dict()
        if self.raw_header:
            email_dict['raw_header'] = self.raw_header.to_dict()

        return email_dict

    @staticmethod
    def from_obj(message_obj):
        message = EmailMessage()

        attachments = message_obj.get_Attachments()
        if attachments:
            for attachment in attachments.get_File():
                message.attachments.append(File.from_obj(attachment))

        links = message_obj.get_Links()
        if links:
            for link in links.get_Link():
                message.links.append(URI.from_obj(link))

        message.header = EmailHeader.from_obj(message_obj.get_Header())
        message.optional_header = OptionalHeader.from_obj(message_obj.get_Optional_Header())
        message.email_server = String.from_obj(message_obj.get_Email_Server())
        message.raw_body = String.from_obj(message_obj.get_Raw_Body())
        message.raw_header = String.from_obj(message_obj.get_Raw_Header())

        return message

    @staticmethod
    def from_dict(message_dict):
        message = EmailMessage()

        for attachment in message_dict.get('attachments', []):
            message.attachments.append(File.from_dict(attachment))
        for link in message_dict.get('links', []):
            message.links.append(URI.from_dict(link))
        message.header = EmailHeader.from_dict(message_dict.get('header'))
        message.optional_header = OptionalHeader.from_dict(message_dict.get('optional_header'))
        message.email_server = String.from_dict(message_dict.get('email_server'))
        message.raw_body = String.from_dict(message_dict.get('raw_body'))
        message.raw_header = String.from_dict(message_dict.get('raw_header'))

        return message
