# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object


class AttachmentsType(GeneratedsSuper):
    """The AttachmenstType captures a list of attachments for an email
    message."""

    subclass = None
    superclass = None
    def __init__(self, File=None):
        if File is None:
            self.File = []
        else:
            self.File = File
    def factory(*args_, **kwargs_):
        if AttachmentsType.subclass:
            return AttachmentsType.subclass(*args_, **kwargs_)
        else:
            return AttachmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File(self): return self.File
    def set_File(self, File): self.File = File
    def add_File(self, value): self.File.append(value)
    def insert_File(self, index, value): self.File[index] = value
    def hasContent_(self):
        if (
            self.File
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='AttachmentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttachmentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='AttachmentsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='AttachmentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for File_ in self.File:
            File_.export(lwrite, level, 'EmailMessageObj:', name_='File', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'File':
            obj_ = AttachmentReferenceType.factory()
            obj_.build(child_)
            self.File.append(obj_)
# end class AttachmentsType

class EmailHeaderType(GeneratedsSuper):
    """The EmailHeaderType captures a representation of a standard email
    header."""

    subclass = None
    superclass = None
    def __init__(self, Received_Lines=None, To=None, CC=None, BCC=None, From=None, Subject=None, In_Reply_To=None, Date=None, Message_ID=None, Sender=None, Reply_To=None, Errors_To=None, Boundary=None, Content_Type=None, MIME_Version=None, Precedence=None, User_Agent=None, X_Mailer=None, X_Originating_IP=None, X_Priority=None):
        self.Received_Lines = Received_Lines
        self.To = To
        self.CC = CC
        self.BCC = BCC
        self.From = From
        self.Subject = Subject
        self.In_Reply_To = In_Reply_To
        self.Date = Date
        self.Message_ID = Message_ID
        self.Sender = Sender
        self.Reply_To = Reply_To
        self.Errors_To = Errors_To
        self.Boundary = Boundary
        self.Content_Type = Content_Type
        self.MIME_Version = MIME_Version
        self.Precedence = Precedence
        self.User_Agent = User_Agent
        self.X_Mailer = X_Mailer
        self.X_Originating_IP = X_Originating_IP
        self.X_Priority = X_Priority
    def factory(*args_, **kwargs_):
        if EmailHeaderType.subclass:
            return EmailHeaderType.subclass(*args_, **kwargs_)
        else:
            return EmailHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Received_Lines(self): return self.Received_Lines
    def set_Received_Lines(self, Received_Lines): self.Received_Lines = Received_Lines
    def get_To(self): return self.To
    def set_To(self, To): self.To = To
    def get_CC(self): return self.CC
    def set_CC(self, CC): self.CC = CC
    def get_BCC(self): return self.BCC
    def set_BCC(self, BCC): self.BCC = BCC
    def get_From(self): return self.From
    def set_From(self, From): self.From = From
    def get_Subject(self): return self.Subject
    def set_Subject(self, Subject): self.Subject = Subject
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_In_Reply_To(self): return self.In_Reply_To
    def set_In_Reply_To(self, In_Reply_To): self.In_Reply_To = In_Reply_To
    def get_Date(self): return self.Date
    def set_Date(self, Date): self.Date = Date
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Message_ID(self): return self.Message_ID
    def set_Message_ID(self, Message_ID): self.Message_ID = Message_ID
    def get_Sender(self): return self.Sender
    def set_Sender(self, Sender): self.Sender = Sender
    def get_Reply_To(self): return self.Reply_To
    def set_Reply_To(self, Reply_To): self.Reply_To = Reply_To
    def get_Errors_To(self): return self.Errors_To
    def set_Errors_To(self, Errors_To): self.Errors_To = Errors_To
    def get_Boundary(self): return self.Boundary
    def set_Boundary(self, Boundary): self.Boundary = Boundary
    def get_Content_Type(self): return self.Content_Type
    def set_Content_Type(self, Content_Type): self.Content_Type = Content_Type
    def get_MIME_Version(self): return self.MIME_Version
    def set_MIME_Version(self, MIME_Version): self.MIME_Version = MIME_Version
    def get_Precedence(self): return self.Precedence
    def set_Precedence(self, Precedence): self.Precedence = Precedence
    def get_User_Agent(self): return self.User_Agent
    def set_User_Agent(self, User_Agent): self.User_Agent = User_Agent
    def get_X_Mailer(self): return self.X_Mailer
    def set_X_Mailer(self, X_Mailer): self.X_Mailer = X_Mailer
    def get_X_Originating_IP(self): return self.X_Originating_IP
    def set_X_Originating_IP(self, X_Originating_IP): self.X_Originating_IP = X_Originating_IP
    def get_X_Priority(self): return self.X_Priority
    def set_X_Priority(self, X_Priority): self.X_Priority = X_Priority
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Received_Lines is not None or
            self.To is not None or
            self.CC is not None or
            self.BCC is not None or
            self.From is not None or
            self.Subject is not None or
            self.In_Reply_To is not None or
            self.Date is not None or
            self.Message_ID is not None or
            self.Sender is not None or
            self.Reply_To is not None or
            self.Errors_To is not None or
            self.Boundary is not None or
            self.Content_Type is not None or
            self.MIME_Version is not None or
            self.Precedence is not None or
            self.User_Agent is not None or
            self.X_Mailer is not None or
            self.X_Originating_IP is not None or
            self.X_Priority is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='EmailHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Received_Lines is not None:
            self.Received_Lines.export(lwrite, level, 'EmailMessageObj:', name_='Received_Lines', pretty_print=pretty_print)
        if self.To is not None:
            self.To.export(lwrite, level, 'EmailMessageObj:', name_='To', pretty_print=pretty_print)
        if self.CC is not None:
            self.CC.export(lwrite, level, 'EmailMessageObj:', name_='CC', pretty_print=pretty_print)
        if self.BCC is not None:
            self.BCC.export(lwrite, level, 'EmailMessageObj:', name_='BCC', pretty_print=pretty_print)
        if self.From is not None:
            self.From.export(lwrite, level, 'EmailMessageObj:', name_='From', pretty_print=pretty_print)
        if self.Subject is not None:
            self.Subject.export(lwrite, level, 'EmailMessageObj:', name_='Subject', pretty_print=pretty_print)
        if self.In_Reply_To is not None:
            self.In_Reply_To.export(lwrite, level, 'EmailMessageObj:', name_='In_Reply_To', pretty_print=pretty_print)
        if self.Date is not None:
            self.Date.export(lwrite, level, 'EmailMessageObj:', name_='Date', pretty_print=pretty_print)
        if self.Message_ID is not None:
            self.Message_ID.export(lwrite, level, 'EmailMessageObj:', name_='Message_ID', pretty_print=pretty_print)
        if self.Sender is not None:
            self.Sender.export(lwrite, level, 'EmailMessageObj:', name_='Sender', pretty_print=pretty_print)
        if self.Reply_To is not None:
            self.Reply_To.export(lwrite, level, 'EmailMessageObj:', name_='Reply_To', pretty_print=pretty_print)
        if self.Errors_To is not None:
            self.Errors_To.export(lwrite, level, 'EmailMessageObj:', name_='Errors_To', pretty_print=pretty_print)
        if self.Boundary is not None:
            self.Boundary.export(lwrite, level, 'EmailMessageObj:', name_='Boundary', pretty_print=pretty_print)
        if self.Content_Type is not None:
            self.Content_Type.export(lwrite, level, 'EmailMessageObj:', name_='Content_Type', pretty_print=pretty_print)
        if self.MIME_Version is not None:
            self.MIME_Version.export(lwrite, level, 'EmailMessageObj:', name_='MIME_Version', pretty_print=pretty_print)
        if self.Precedence is not None:
            self.Precedence.export(lwrite, level, 'EmailMessageObj:', name_='Precedence', pretty_print=pretty_print)
        if self.User_Agent is not None:
            self.User_Agent.export(lwrite, level, 'EmailMessageObj:', name_='User_Agent', pretty_print=pretty_print)
        if self.X_Mailer is not None:
            self.X_Mailer.export(lwrite, level, 'EmailMessageObj:', name_='X_Mailer', pretty_print=pretty_print)
        if self.X_Originating_IP is not None:
            self.X_Originating_IP.export(lwrite, level, 'EmailMessageObj:', name_='X_Originating_IP', pretty_print=pretty_print)
        if self.X_Priority is not None:
            self.X_Priority.export(lwrite, level, 'EmailMessageObj:', name_='X_Priority', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Received_Lines':
            obj_ = EmailReceivedLineListType.factory()
            obj_.build(child_)
            self.set_Received_Lines(obj_)
        elif nodeName_ == 'To':
            obj_ = EmailRecipientsType.factory()
            obj_.build(child_)
            self.set_To(obj_)
        elif nodeName_ == 'CC':
            obj_ = EmailRecipientsType.factory()
            obj_.build(child_)
            self.set_CC(obj_)
        elif nodeName_ == 'BCC':
            obj_ = EmailRecipientsType.factory()
            obj_.build(child_)
            self.set_BCC(obj_)
        elif nodeName_ == 'From':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_From(obj_)
        elif nodeName_ == 'Subject':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Subject(obj_)
        elif nodeName_ == 'In_Reply_To':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_In_Reply_To(obj_)
        elif nodeName_ == 'Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Date(obj_)
        elif nodeName_ == 'Message_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Message_ID(obj_)
        elif nodeName_ == 'Sender':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Sender(obj_)
        elif nodeName_ == 'Reply_To':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Reply_To(obj_)
        elif nodeName_ == 'Errors_To':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Errors_To(obj_)
        elif nodeName_ == 'Boundary':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Boundary(obj_)
        elif nodeName_ == 'Content_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Type(obj_)
        elif nodeName_ == 'MIME_Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_MIME_Version(obj_)
        elif nodeName_ == 'Precedence':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Precedence(obj_)
        elif nodeName_ == 'User_Agent':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Agent(obj_)
        elif nodeName_ == 'X_Mailer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Mailer(obj_)
        elif nodeName_ == 'X_Originating_IP':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_X_Originating_IP(obj_)
        elif nodeName_ == 'X_Priority':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Priority(obj_)
# end class EmailHeaderType

class EmailRecipientsType(GeneratedsSuper):
    """The EmailRecipientsType captures a list of recipients for an email
    message."""

    subclass = None
    superclass = None
    def __init__(self, Recipient=None):
        if Recipient is None:
            self.Recipient = []
        else:
            self.Recipient = Recipient
    def factory(*args_, **kwargs_):
        if EmailRecipientsType.subclass:
            return EmailRecipientsType.subclass(*args_, **kwargs_)
        else:
            return EmailRecipientsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Recipient(self): return self.Recipient
    def set_Recipient(self, Recipient): self.Recipient = Recipient
    def add_Recipient(self, value): self.Recipient.append(value)
    def insert_Recipient(self, index, value): self.Recipient[index] = value
    def hasContent_(self):
        if (
            self.Recipient
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailRecipientsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailRecipientsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='EmailRecipientsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailRecipientsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Recipient_ in self.Recipient:
            Recipient_.export(lwrite, level, 'EmailMessageObj:', name_='Recipient', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Recipient':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.Recipient.append(obj_)
# end class EmailRecipientsType

class LinksType(GeneratedsSuper):
    """The LinksType captures a list of URIs, representing the links
    contained in the message."""

    subclass = None
    superclass = None
    def __init__(self, Link=None):
        if Link is None:
            self.Link = []
        else:
            self.Link = Link
    def factory(*args_, **kwargs_):
        if LinksType.subclass:
            return LinksType.subclass(*args_, **kwargs_)
        else:
            return LinksType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Link(self): return self.Link
    def set_Link(self, Link): self.Link = Link
    def add_Link(self, value): self.Link.append(value)
    def insert_Link(self, index, value): self.Link[index] = value
    def hasContent_(self):
        if (
            self.Link
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='LinksType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LinksType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='LinksType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='LinksType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Link_ in self.Link:
            Link_.export(lwrite, level, 'EmailMessageObj:', name_='Link', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Link':
            obj_ = LinkReferenceType.factory()
            obj_.build(child_)
            self.Link.append(obj_)
# end class LinksType

class EmailReceivedLineType(GeneratedsSuper):
    """The EmailReceivedLineType captures a single 'Received' line in an
    email message header."""
    subclass = None
    superclass = None
    def __init__(self, From=None, By=None, Via=None, With=None, For=None, ID=None, Timestamp=None):
        self.From = From
        self.By = By
        self.Via = Via
        self.With = With
        self.For = For
        self.ID = ID
        self.Timestamp = Timestamp
    def factory(*args_, **kwargs_):
        if EmailReceivedLineType.subclass:
            return EmailReceivedLineType.subclass(*args_, **kwargs_)
        else:
            return EmailReceivedLineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_From(self): return self.From
    def set_From(self, From): self.From = From
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_By(self): return self.By
    def set_By(self, By): self.By = By
    def get_Via(self): return self.Via
    def set_Via(self, Via): self.Via = Via
    def get_With(self): return self.With
    def set_With(self, With): self.With = With
    def get_For(self): return self.For
    def set_For(self, For): self.For = For
    def get_ID(self): return self.ID
    def set_ID(self, ID): self.ID = ID
    def get_Timestamp(self): return self.Timestamp
    def set_Timestamp(self, Timestamp): self.Timestamp = Timestamp
    def hasContent_(self):
        if (
            self.From is not None or
            self.By is not None or
            self.Via is not None or
            self.With is not None or
            self.For is not None or
            self.ID is not None or
            self.Timestamp is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailReceivedLineType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailReceivedLineType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='EmailReceivedLineType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailReceivedLineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.From is not None:
            self.From.export(lwrite, level, 'EmailMessageObj:', name_='From', pretty_print=pretty_print)
        if self.By is not None:
            self.By.export(lwrite, level, 'EmailMessageObj:', name_='By', pretty_print=pretty_print)
        if self.Via is not None:
            self.Via.export(lwrite, level, 'EmailMessageObj:', name_='Via', pretty_print=pretty_print)
        if self.With is not None:
            self.With.export(lwrite, level, 'EmailMessageObj:', name_='With', pretty_print=pretty_print)
        if self.For is not None:
            self.For.export(lwrite, level, 'EmailMessageObj:', name_='For', pretty_print=pretty_print)
        if self.ID is not None:
            self.ID.export(lwrite, level, 'EmailMessageObj:', name_='ID', pretty_print=pretty_print)
        if self.Timestamp is not None:
            self.Timestamp.export(lwrite, level, 'EmailMessageObj:', name_='Timestamp', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'From':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_From(obj_)
        elif nodeName_ == 'By':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_By(obj_)
        elif nodeName_ == 'Via':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Via(obj_)
        elif nodeName_ == 'With':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_With(obj_)
        elif nodeName_ == 'For':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_For(obj_)
        elif nodeName_ == 'ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ID(obj_)
        elif nodeName_ == 'Timestamp':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Timestamp(obj_)
# end class EmailReceivedLineType

class EmailReceivedLineListType(GeneratedsSuper):
    """The EmailReceivedLineListType captures a list of 'Received' lines in
    an email message header."""

    subclass = None
    superclass = None
    def __init__(self, Received=None):
        if Received is None:
            self.Received = []
        else:
            self.Received = Received
    def factory(*args_, **kwargs_):
        if EmailReceivedLineListType.subclass:
            return EmailReceivedLineListType.subclass(*args_, **kwargs_)
        else:
            return EmailReceivedLineListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Received(self): return self.Received
    def set_Received(self, Received): self.Received = Received
    def add_Received(self, value): self.Received.append(value)
    def insert_Received(self, index, value): self.Received[index] = value
    def hasContent_(self):
        if (
            self.Received
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailReceivedLineListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailReceivedLineListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='EmailReceivedLineListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailReceivedLineListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Received_ in self.Received:
            Received_.export(lwrite, level, 'EmailMessageObj:', name_='Received', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Received':
            obj_ = EmailReceivedLineType.factory()
            obj_.build(child_)
            self.Received.append(obj_)
# end class EmailReceivedLineListType

class AttachmentReferenceType(GeneratedsSuper):
    """The AttachmentReferenceType specifies a reference to an Object
    defined elsewhere in the document which characterizes an
    attachment included in the email message.The object_reference
    field specifies a reference to an file-oriented (i.e., the File
    Object or one its derivations such as the Windows File Object)
    Object defined elsewhere in the document, via its id."""

    subclass = None
    superclass = None
    def __init__(self, object_reference=None):
        self.object_reference = _cast(None, object_reference)
        pass
    def factory(*args_, **kwargs_):
        if AttachmentReferenceType.subclass:
            return AttachmentReferenceType.subclass(*args_, **kwargs_)
        else:
            return AttachmentReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_object_reference(self): return self.object_reference
    def set_object_reference(self, object_reference): self.object_reference = object_reference
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='AttachmentReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttachmentReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='AttachmentReferenceType'):
        if self.object_reference is not None:

            lwrite(' object_reference=%s' % (quote_attrib(self.object_reference), ))
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='AttachmentReferenceType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('object_reference', node)
        if value is not None:

            self.object_reference = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AttachmentReferenceType

class LinkReferenceType(GeneratedsSuper):
    """The LinkReferenceType specifies a reference to a URI Object defined
    elsewhere in the document which characterizes a hyperlink
    embedded in the body of the email message.The object_reference
    field specifies a reference to a URI Object defined elsewhere in
    the document, via its id."""

    subclass = None
    superclass = None
    def __init__(self, object_reference=None):
        self.object_reference = _cast(None, object_reference)
        pass
    def factory(*args_, **kwargs_):
        if LinkReferenceType.subclass:
            return LinkReferenceType.subclass(*args_, **kwargs_)
        else:
            return LinkReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_object_reference(self): return self.object_reference
    def set_object_reference(self, object_reference): self.object_reference = object_reference
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='LinkReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LinkReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='LinkReferenceType'):
        if self.object_reference is not None:

            lwrite(' object_reference=%s' % (quote_attrib(self.object_reference), ))
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='LinkReferenceType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('object_reference', node)
        if value is not None:

            self.object_reference = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class LinkReferenceType

class EmailMessageObjectType(cybox_common.ObjectPropertiesType):
    """The EmailMessageObjectType type is intended to characterize an
    individual email message."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Header=None, Email_Server=None, Raw_Body=None, Raw_Header=None, Attachments=None, Links=None):
        super(EmailMessageObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Header = Header
        self.Email_Server = Email_Server
        self.Raw_Body = Raw_Body
        self.Raw_Header = Raw_Header
        self.Attachments = Attachments
        self.Links = Links
    def factory(*args_, **kwargs_):
        if EmailMessageObjectType.subclass:
            return EmailMessageObjectType.subclass(*args_, **kwargs_)
        else:
            return EmailMessageObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Header(self): return self.Header
    def set_Header(self, Header): self.Header = Header
    def get_Email_Server(self): return self.Email_Server
    def set_Email_Server(self, Email_Server): self.Email_Server = Email_Server
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Raw_Body(self): return self.Raw_Body
    def set_Raw_Body(self, Raw_Body): self.Raw_Body = Raw_Body
    def get_Raw_Header(self): return self.Raw_Header
    def set_Raw_Header(self, Raw_Header): self.Raw_Header = Raw_Header
    def get_Attachments(self): return self.Attachments
    def set_Attachments(self, Attachments): self.Attachments = Attachments
    def get_Links(self): return self.Links
    def set_Links(self, Links): self.Links = Links
    def hasContent_(self):
        if (
            self.Header is not None or
            self.Email_Server is not None or
            self.Raw_Body is not None or
            self.Raw_Header is not None or
            self.Attachments is not None or
            self.Links is not None or
            super(EmailMessageObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailMessageObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailMessageObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='EmailMessageObj:', name_='EmailMessageObjectType'):
        super(EmailMessageObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='EmailMessageObjectType')
    def exportChildren(self, lwrite, level, namespace_='EmailMessageObj:', name_='EmailMessageObjectType', fromsubclass_=False, pretty_print=True):
        super(EmailMessageObjectType, self).exportChildren(lwrite, level, 'EmailMessageObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Header is not None:
            self.Header.export(lwrite, level, 'EmailMessageObj:', name_='Header', pretty_print=pretty_print)
        if self.Email_Server is not None:
            self.Email_Server.export(lwrite, level, 'EmailMessageObj:', name_='Email_Server', pretty_print=pretty_print)
        if self.Raw_Body is not None:
            if self.Raw_Body.get_valueOf_() is not None:
                value = self.Raw_Body.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Body.set_valueOf_(value)
            self.Raw_Body.export(lwrite, level, 'EmailMessageObj:', name_='Raw_Body', pretty_print=pretty_print)
        if self.Raw_Header is not None:
            if self.Raw_Header.get_valueOf_() is not None:
                value = self.Raw_Header.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Header.set_valueOf_(value)
            self.Raw_Header.export(lwrite, level, 'EmailMessageObj:', name_='Raw_Header', pretty_print=pretty_print)
        if self.Attachments is not None:
            self.Attachments.export(lwrite, level, 'EmailMessageObj:', name_='Attachments', pretty_print=pretty_print)
        if self.Links is not None:
            self.Links.export(lwrite, level, 'EmailMessageObj:', name_='Links', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(EmailMessageObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Header':
            obj_ = EmailHeaderType.factory()
            obj_.build(child_)
            self.set_Header(obj_)
        elif nodeName_ == 'Email_Server':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Email_Server(obj_)
        elif nodeName_ == 'Raw_Body':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Body(obj_)
        elif nodeName_ == 'Raw_Header':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Header(obj_)
        elif nodeName_ == 'Attachments':
            obj_ = AttachmentsType.factory()
            obj_.build(child_)
            self.set_Attachments(obj_)
        elif nodeName_ == 'Links':
            obj_ = LinksType.factory()
            obj_.build(child_)
            self.set_Links(obj_)
        super(EmailMessageObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class EmailMessageObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Dependencies': cybox_common.DependenciesType,
    'By': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'SubDatum': cybox_common.MetadataType,
    'Sender': address_object.AddressObjectType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Subject': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'From': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'For': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Import': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Raw_Body': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'X_Priority': cybox_common.PositiveIntegerObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'X_Mailer': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'In_Reply_To': cybox_common.StringObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'MIME_Version': cybox_common.StringObjectPropertyType,
    'Boundary': cybox_common.StringObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Timestamp': cybox_common.DateTimeObjectPropertyType,
    'Message_ID': cybox_common.StringObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Recipient': address_object.AddressObjectType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Errors_To': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Precedence': cybox_common.StringObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'X_Originating_IP': address_object.AddressObjectType,
    'Email_Server': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Reply_To': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'With': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'ID': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Email_Message'
        rootClass = EmailMessageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Email_Message'
        rootClass = EmailMessageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Email_Message'
        rootClass = EmailMessageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Email_Message",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "EmailMessageObjectType",
    "AttachmentsType",
    "EmailHeaderType",
    "EmailRecipientsType",
    "LinksType",
    "EmailReceivedLineType",
    "EmailReceivedLineListType",
    "AttachmentReferenceType",
    "LinkReferenceType"
    ]
