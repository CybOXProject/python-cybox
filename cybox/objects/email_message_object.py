import cybox
import cybox.bindings.email_message_object_1_2 as email_message_binding
from cybox.common import String, PositiveInteger, DateTime
from cybox.objects.file_object import File
from cybox.objects.uri_object import URI
from cybox.objects.address_object import Address

class EmailRecipients(cybox.Entity):
    def __init__(self):
        self.recipients = []

    def add(self, recipient):
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


class EmailMessage(cybox.Entity):
    def __init__(self):
        self.attachments = []
        self.links = []
        self.header = None
        #self.optional_header = None
        self.email_server = None
        self.raw_body = None
        self.raw_header = None

    def to_obj(self):
        email_obj = email_message_binding.EmailMessageObjectType()

        email_obj.set_anyAttributes_({'xsi:type' : 'EmailMessageObj:EmailMessageObjectType'})
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
        # TODO: OptionalHeader
        if self.email_server:
            email_obj.set_Email_Server(self.email_server.to_obj())
        if self.raw_body:
            email_obj.set_Raw_Body(self.raw_body.to_obj())
        if self.raw_header:
            email_obj.set_Raw_Header(self.raw_header.to_obj())

        return email_obj

    def to_dict(self):
        email_dict = {}
        if self.attachments:
            email_dict['attachments'] = [a.to_dict() for a in self.attachments]
        if self.links:
            email_dict['links'] = [l.to_dict() for l in self.links]
        email_dict['header'] = self.header.to_dict()
        # TODO: OptionalHeader
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
        # TODO: OptionalHeader
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
        # TODO: OptionalHeader
        message.email_server = String.from_dict(message_dict.get('email_server'))
        message.raw_body = String.from_dict(message_dict.get('raw_body'))
        message.raw_header = String.from_dict(message_dict.get('raw_header'))

        return message


#    @classmethod
#    def object_from_dict(cls, email_attributes):
#        """Create the Email Message Object object representation from an input dictionary"""
#            if key == 'optional_header':
#                header = email_message_binding.EmailHeaderType()
#                for headername, headervalue in value.items():
#                    if headername == 'boundary':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype="String"), headervalue))
#                    if headername == 'content_type':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype="String"), headervalue))
#                    if headername == 'mime_version':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype="String"), headervalue))
#                    if headername == 'precedence':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype="String"), headervalue))
#                    if headername == 'x_mailer':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype="String"), headervalue))
#                    if headername == 'x_originating_ip':
#                        header.set_Message_ID(Address.object_from_dict(headervalue))
#                    if headername == 'x_priority':
#                        header.set_Message_ID(Base_Object_Attribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype="PositiveInt"), headervalue))
#                emailobj.set_Optional_Header(header)
#
#    @classmethod
#    def dict_from_object(cls, defined_object):
#        """Parse and return a dictionary for an Email Message Object object"""
#        if defined_object.get_Optional_Header() is not None:
#            defined_object_dict['optional_header'] = {}
#            header = defined_object.get_Optional_Header()
#            if defined_object.get_Boundary() is not None:
#                defined_object_dict['optional_header']['boundary'] = Base_Object_Attribute.dict_from_object(defined_object.get_Boundary())
#            if defined_object.get_Content_Type() is not None:
#                defined_object_dict['optional_header']['content_type'] = Base_Object_Attribute.dict_from_object(defined_object.get_Content_Type())
#            if defined_object.get_MIME_Version() is not None:
#                defined_object_dict['optional_header']['mime_version'] = Base_Object_Attribute.dict_from_object(defined_object.get_MIME_Version())
#            if defined_object.get_Precedence() is not None:
#                defined_object_dict['optional_header']['precedence'] = Base_Object_Attribute.dict_from_object(defined_object.get_Precedence())
#            if defined_object.get_X_Mailer() is not None:
#                defined_object_dict['optional_header']['x_mailer'] = Base_Object_Attribute.dict_from_object(defined_object.get_Subject())
#            if defined_object.get_X_Originating_IP() is not None:
#                defined_object_dict['header']['x_originating_ip'] = Address.dict_from_object(defined_object.get_X_Originating_IP())
#            if defined_object.get_X_Priority() is not None:
#                defined_object_dict['optional_header']['x_priority'] = Base_Object_Attribute.dict_from_object(defined_object.get_X_Priority())
#        return defined_object_dict
#
#
