# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object
from . import uri_object


class WhoisRegistrarInfoType(GeneratedsSuper):

    subclass = None
    superclass = None
    def __init__(self, Registrar_ID=None, Registrar_GUID=None, Name=None, Address=None, Email_Address=None, Phone_Number=None, Whois_Server=None, Referral_URL=None, Contacts=None):
        self.Registrar_ID = Registrar_ID
        self.Registrar_GUID = Registrar_GUID
        self.Name = Name
        self.Address = Address
        self.Email_Address = Email_Address
        self.Phone_Number = Phone_Number
        self.Whois_Server = Whois_Server
        self.Referral_URL = Referral_URL
        self.Contacts = Contacts
    def factory(*args_, **kwargs_):
        if WhoisRegistrarInfoType.subclass:
            return WhoisRegistrarInfoType.subclass(*args_, **kwargs_)
        else:
            return WhoisRegistrarInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Registrar_ID(self): return self.Registrar_ID
    def set_Registrar_ID(self, Registrar_ID): self.Registrar_ID = Registrar_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Registrar_GUID(self): return self.Registrar_GUID
    def set_Registrar_GUID(self, Registrar_GUID): self.Registrar_GUID = Registrar_GUID
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Address(self): return self.Address
    def set_Address(self, Address): self.Address = Address
    def get_Email_Address(self): return self.Email_Address
    def set_Email_Address(self, Email_Address): self.Email_Address = Email_Address
    def get_Phone_Number(self): return self.Phone_Number
    def set_Phone_Number(self, Phone_Number): self.Phone_Number = Phone_Number
    def get_Whois_Server(self): return self.Whois_Server
    def set_Whois_Server(self, Whois_Server): self.Whois_Server = Whois_Server
    def get_Referral_URL(self): return self.Referral_URL
    def set_Referral_URL(self, Referral_URL): self.Referral_URL = Referral_URL
    def get_Contacts(self): return self.Contacts
    def set_Contacts(self, Contacts): self.Contacts = Contacts
    def hasContent_(self):
        if (
            self.Registrar_ID is not None or
            self.Registrar_GUID is not None or
            self.Name is not None or
            self.Address is not None or
            self.Email_Address is not None or
            self.Phone_Number is not None or
            self.Whois_Server is not None or
            self.Referral_URL is not None or
            self.Contacts is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrarInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisRegistrarInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisRegistrarInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrarInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Registrar_ID is not None:
            self.Registrar_ID.export(lwrite, level, 'WhoisObj:', name_='Registrar_ID', pretty_print=pretty_print)
        if self.Registrar_GUID is not None:
            self.Registrar_GUID.export(lwrite, level, 'WhoisObj:', name_='Registrar_GUID', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WhoisObj:', name_='Name', pretty_print=pretty_print)
        if self.Address is not None:
            self.Address.export(lwrite, level, 'WhoisObj:', name_='Address', pretty_print=pretty_print)
        if self.Email_Address is not None:
            self.Email_Address.export(lwrite, level, 'WhoisObj:', name_='Email_Address', pretty_print=pretty_print)
        if self.Phone_Number is not None:
            self.Phone_Number.export(lwrite, level, 'WhoisObj:', name_='Phone_Number', pretty_print=pretty_print)
        if self.Whois_Server is not None:
            self.Whois_Server.export(lwrite, level, 'WhoisObj:', name_='Whois_Server', pretty_print=pretty_print)
        if self.Referral_URL is not None:
            self.Referral_URL.export(lwrite, level, 'WhoisObj:', name_='Referral_URL', pretty_print=pretty_print)
        if self.Contacts is not None:
            self.Contacts.export(lwrite, level, 'WhoisObj:', name_='Contacts', pretty_print=pretty_print)
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
        if nodeName_ == 'Registrar_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Registrar_ID(obj_)
        elif nodeName_ == 'Registrar_GUID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Registrar_GUID(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Address':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address(obj_)
        elif nodeName_ == 'Email_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Email_Address(obj_)
        elif nodeName_ == 'Phone_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Phone_Number(obj_)
        elif nodeName_ == 'Whois_Server':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Whois_Server(obj_)
        elif nodeName_ == 'Referral_URL':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Referral_URL(obj_)
        elif nodeName_ == 'Contacts':
            obj_ = WhoisContactsType.factory()
            obj_.build(child_)
            self.set_Contacts(obj_)
# end class WhoisRegistrarInfoType

class WhoisContactsType(GeneratedsSuper):
    """The WhoisContactsType represents a list of contacts (usually
    registrar or registrant) found in a Whois entry"""

    subclass = None
    superclass = None
    def __init__(self, Contact=None):
        if Contact is None:
            self.Contact = []
        else:
            self.Contact = Contact
    def factory(*args_, **kwargs_):
        if WhoisContactsType.subclass:
            return WhoisContactsType.subclass(*args_, **kwargs_)
        else:
            return WhoisContactsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Contact(self): return self.Contact
    def set_Contact(self, Contact): self.Contact = Contact
    def add_Contact(self, value): self.Contact.append(value)
    def insert_Contact(self, index, value): self.Contact[index] = value
    def hasContent_(self):
        if (
            self.Contact
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisContactsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisContactsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisContactsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisContactsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Contact_ in self.Contact:
            Contact_.export(lwrite, level, 'WhoisObj:', name_='Contact', pretty_print=pretty_print)
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
        if nodeName_ == 'Contact':
            obj_ = WhoisContactType.factory()
            obj_.build(child_)
            self.add_Contact(obj_)
# end class WhoisContactsType

class WhoisContactType(GeneratedsSuper):
    """The contact_type field specifies what type of contact this is. Only
    values from WhoisObj:RegistrarContactTypeEnum can be used."""

    subclass = None
    superclass = None
    def __init__(self, contact_type=None, Contact_ID=None, Name=None, Email_Address=None, Phone_Number=None, Fax_Number=None, Address=None, Organization=None, extensiontype_=None):
        self.contact_type = _cast(None, contact_type)
        self.Contact_ID = Contact_ID
        self.Name = Name
        self.Email_Address = Email_Address
        self.Fax_Number = Fax_Number
        self.Phone_Number = Phone_Number
        self.Address = Address
        self.Organization = Organization
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if WhoisContactType.subclass:
            return WhoisContactType.subclass(*args_, **kwargs_)
        else:
            return WhoisContactType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Contact_ID(self): return self.Contact_ID
    def set_Contact_ID(self, Contact_ID): self.Contact_ID = Contact_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Email_Address(self): return self.Email_Address
    def set_Email_Address(self, Email_Address): self.Email_Address = Email_Address
    def get_Phone_Number(self): return self.Phone_Number
    def set_Phone_Number(self, Phone_Number): self.Phone_Number = Phone_Number
    def get_Fax_Number(self): return self.Fax_Number
    def set_Fax_Number(self, Fax_Number): self.Fax_Number = Fax_Number
    def get_Address(self): return self.Address
    def set_Address(self, Address): self.Address = Address
    def get_Organization(self): return self.Organization
    def set_Organization(self, Organization): self.Organization = Organization
    def get_contact_type(self): return self.contact_type
    def set_contact_type(self, contact_type): self.contact_type = contact_type
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.Contact_ID is not None or
            self.Name is not None or
            self.Email_Address is not None or
            self.Phone_Number is not None or
            self.Fax_Number is not None or
            self.Address is not None or
            self.Organization is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisContactType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisContactType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisContactType'):
        if self.contact_type is not None:

            lwrite(' contact_type=%s' % (quote_attrib(self.contact_type), ))
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisContactType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Contact_ID is not None:
            self.Contact_ID.export(lwrite, level, 'WhoisObj:', name_='Contact_ID', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WhoisObj:', name_='Name', pretty_print=pretty_print)
        if self.Email_Address is not None:
            self.Email_Address.export(lwrite, level, 'WhoisObj:', name_='Email_Address', pretty_print=pretty_print)
        if self.Phone_Number is not None:
            self.Phone_Number.export(lwrite, level, 'WhoisObj:', name_='Phone_Number', pretty_print=pretty_print)
        if self.Fax_Number is not None:
            self.Fax_Number.export(lwrite, level, 'WhoisObj:', name_='Fax_Number', pretty_print=pretty_print)
        if self.Address is not None:
            self.Address.export(lwrite, level, 'WhoisObj:', name_='Address', pretty_print=pretty_print)
        if self.Organization is not None:
            self.Organization.export(lwrite, level, 'WhoisObj:', name_='Organization', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('contact_type', node)
        if value is not None:

            self.contact_type = value
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Contact_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Contact_ID(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Email_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Email_Address(obj_)
        elif nodeName_ == 'Phone_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Phone_Number(obj_)
        elif nodeName_ == 'Fax_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Fax_Number(obj_)
        elif nodeName_ == 'Address':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address(obj_)
        elif nodeName_ == 'Organization':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Organization(obj_)
# end class WhoisContactType

class WhoisStatusesType(GeneratedsSuper):
    """The WhoisStatusesType defines a list of WhoisStatusType objecst"""

    subclass = None
    superclass = None
    def __init__(self, Status=None):
        if Status is None:
            self.Status = []
        else:
            self.Status = Status
    def factory(*args_, **kwargs_):
        if WhoisStatusesType.subclass:
            return WhoisStatusesType.subclass(*args_, **kwargs_)
        else:
            return WhoisStatusesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def add_Status(self, value): self.Status.append(value)
    def insert_Status(self, index, value): self.Status[index] = value
    def validate_WhoisStatusType(self, value):
        # Validate type WhoisStatusType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Status
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisStatusesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisStatusesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisStatusesType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisStatusesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Status_ in self.Status:
            Status_.export(lwrite, level, 'WhoisObj:', name_='Status', pretty_print=pretty_print)
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
        if nodeName_ == 'Status':
            obj_ = WhoisStatusType.factory()
            obj_.build(child_)
            self.Status.append(obj_)
# end class WhoisStatusesType

class WhoisNameserversType(GeneratedsSuper):
    """The WhoisNameserversType defines a list of nameservers associated
    with a Whois entry"""

    subclass = None
    superclass = None
    def __init__(self, Nameserver=None):
        if Nameserver is None:
            self.Nameserver = []
        else:
            self.Nameserver = Nameserver
    def factory(*args_, **kwargs_):
        if WhoisNameserversType.subclass:
            return WhoisNameserversType.subclass(*args_, **kwargs_)
        else:
            return WhoisNameserversType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Nameserver(self): return self.Nameserver
    def set_Nameserver(self, Nameserver): self.Nameserver = Nameserver
    def add_Nameserver(self, value): self.Nameserver.append(value)
    def insert_Nameserver(self, index, value): self.Nameserver[index] = value
    def hasContent_(self):
        if (
            self.Nameserver
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisNameserversType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisNameserversType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisNameserversType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisNameserversType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Nameserver_ in self.Nameserver:
            Nameserver_.export(lwrite, level, 'WhoisObj:', name_='Nameserver', pretty_print=pretty_print)
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
        if nodeName_ == 'Nameserver':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.Nameserver.append(obj_)
# end class WhoisNameserversType

class WhoisRegistrantInfoType(WhoisContactType):

    subclass = None
    superclass = WhoisContactType
    def __init__(self, contact_type=None, Contact_ID=None, Name=None, Email_Address=None, Phone_Number=None, Fax_Number=None, Address=None,  Organization=None, Registrant_ID=None):
        super(WhoisRegistrantInfoType, self).__init__(contact_type, Contact_ID, Name, Email_Address, Phone_Number, Fax_Number, Address, Organization, )
        self.Registrant_ID = Registrant_ID
    def factory(*args_, **kwargs_):
        if WhoisRegistrantInfoType.subclass:
            return WhoisRegistrantInfoType.subclass(*args_, **kwargs_)
        else:
            return WhoisRegistrantInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Registrant_ID(self): return self.Registrant_ID
    def set_Registrant_ID(self, Registrant_ID): self.Registrant_ID = Registrant_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Registrant_ID is not None or
            super(WhoisRegistrantInfoType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrantInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisRegistrantInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisRegistrantInfoType'):
        super(WhoisRegistrantInfoType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisRegistrantInfoType')
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrantInfoType', fromsubclass_=False, pretty_print=True):
        super(WhoisRegistrantInfoType, self).exportChildren(lwrite, level, 'WhoisObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Registrant_ID is not None:
            self.Registrant_ID.export(lwrite, level, 'WhoisObj:', name_='Registrant_ID', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WhoisRegistrantInfoType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Registrant_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Registrant_ID(obj_)
        super(WhoisRegistrantInfoType, self).buildChildren(child_, node, nodeName_, True)
# end class WhoisRegistrantInfoType

class WhoisRegistrantsType(GeneratedsSuper):
    """The WhoisRegistrantsType represents a list of registrant information
    for a given Whois entry"""

    subclass = None
    superclass = None
    def __init__(self, Registrant=None):
        if Registrant is None:
            self.Registrant = []
        else:
            self.Registrant = Registrant
    def factory(*args_, **kwargs_):
        if WhoisRegistrantsType.subclass:
            return WhoisRegistrantsType.subclass(*args_, **kwargs_)
        else:
            return WhoisRegistrantsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Registrant(self): return self.Registrant
    def set_Registrant(self, Registrant): self.Registrant = Registrant
    def add_Registrant(self, value): self.Registrant.append(value)
    def insert_Registrant(self, index, value): self.Registrant[index] = value
    def hasContent_(self):
        if (
            self.Registrant
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrantsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisRegistrantsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisRegistrantsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisRegistrantsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Registrant_ in self.Registrant:
            Registrant_.export(lwrite, level, 'WhoisObj:', name_='Registrant', pretty_print=pretty_print)
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
        if nodeName_ == 'Registrant':
            obj_ = WhoisRegistrantInfoType.factory()
            obj_.build(child_)
            self.Registrant.append(obj_)
# end class WhoisRegistrantsType

class RegionalRegistryType(cybox_common.BaseObjectPropertyType):
    """The RegionalRegistryType specifies a Regional Internet Registry
    (RIR) for a given WHOIS entry. RIRs defined by the
    RegionalRegistryTypeEnum may be used, as well as those specified
    by a free form text string."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(RegionalRegistryType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if RegionalRegistryType.subclass:
            return RegionalRegistryType.subclass(*args_, **kwargs_)
        else:
            return RegionalRegistryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(RegionalRegistryType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='RegionalRegistryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RegionalRegistryType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='RegionalRegistryType'):
        super(RegionalRegistryType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RegionalRegistryType')
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='RegionalRegistryType', fromsubclass_=False, pretty_print=True):
        super(RegionalRegistryType, self).exportChildren(lwrite, level, 'WhoisObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RegionalRegistryType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class RegionalRegistryType

class WhoisStatusType(cybox_common.BaseObjectPropertyType):
    """The WhoisStatusType specifies a status for a domain as listed in its
    Whois entry. Only statuses defined by WhoisStatusTypeEnum can be
    used."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None, extensiontype_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(WhoisStatusType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, extensiontype_)
    def factory(*args_, **kwargs_):
        if WhoisStatusType.subclass:
            return WhoisStatusType.subclass(*args_, **kwargs_)
        else:
            return WhoisStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WhoisStatusType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisStatusType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisStatusType'):
        super(WhoisStatusType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisStatusType')
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisStatusType', fromsubclass_=False, pretty_print=True):
        super(WhoisStatusType, self).exportChildren(lwrite, level, 'WhoisObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WhoisStatusType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WhoisStatusType

class WhoisObjectType(cybox_common.ObjectPropertiesType):
    """The WhoisObjectType type is intended to characterize Whois
    information for a domain."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Lookup_Date=None, Domain_Name=None, Domain_ID=None, Server_Name=None, IP_Address=None, DNSSEC=None, Nameservers=None, Status=None, Updated_Date=None, Creation_Date=None, Expiration_Date=None, Regional_Internet_Registry=None, Sponsoring_Registrar=None, Registrar_Info=None, Registrants=None, Contact_Info=None, Remarks=None):
        super(WhoisObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Lookup_Date = Lookup_Date
        self.Domain_Name = Domain_Name
        self.Domain_ID = Domain_ID
        self.Server_Name = Server_Name
        self.IP_Address = IP_Address
        self.DNSSEC = DNSSEC
        self.Nameservers = Nameservers
        self.Status = Status
        self.Updated_Date = Updated_Date
        self.Creation_Date = Creation_Date
        self.Expiration_Date = Expiration_Date
        self.Regional_Internet_Registry = Regional_Internet_Registry
        self.Sponsoring_Registrar = Sponsoring_Registrar
        self.Registrar_Info = Registrar_Info
        self.Registrants = Registrants
        self.Contact_Info = Contact_Info
        self.Remarks = Remarks
    def factory(*args_, **kwargs_):
        if WhoisObjectType.subclass:
            return WhoisObjectType.subclass(*args_, **kwargs_)
        else:
            return WhoisObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Lookup_Date(self): return self.Lookup_Date
    def set_Lookup_Date(self, Lookup_Date): self.Lookup_Date = Lookup_Date
    def get_Domain_Name(self): return self.Domain_Name
    def set_Domain_Name(self, Domain_Name): self.Domain_Name = Domain_Name
    def get_Domain_ID(self): return self.Domain_ID
    def set_Domain_ID(self, Domain_ID): self.Domain_ID = Domain_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Server_Name(self): return self.Server_Name
    def set_Server_Name(self, Server_Name): self.Server_Name = Server_Name
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def get_DNSSEC(self): return self.DNSSEC
    def set_DNSSEC(self, DNSSEC): self.DNSSEC = DNSSEC
    def validate_WhoisDNSSECTypeEnum(self, value):
        # Validate type WhoisDNSSECTypeEnum, a restriction on xs:string.
        pass
    def get_Nameservers(self): return self.Nameservers
    def set_Nameservers(self, Nameservers): self.Nameservers = Nameservers
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def get_Updated_Date(self): return self.Updated_Date
    def set_Updated_Date(self, Updated_Date): self.Updated_Date = Updated_Date
    def validate_DateObjectPropertyType(self, value):
        # Validate type cybox_common.DateObjectPropertyType, a restriction on None.
        pass
    def get_Creation_Date(self): return self.Creation_Date
    def set_Creation_Date(self, Creation_Date): self.Creation_Date = Creation_Date
    def get_Expiration_Date(self): return self.Expiration_Date
    def set_Expiration_Date(self, Expiration_Date): self.Expiration_Date = Expiration_Date
    def get_Regional_Internet_Registry(self): return self.Regional_Internet_Registry
    def set_Regional_Internet_Registry(self, Regional_Internet_Registry): self.Regional_Internet_Registry = Regional_Internet_Registry
    def validate_RegionalRegistryType(self, value):
        # Validate type RegionalRegistryType, a restriction on None.
        pass
    def get_Sponsoring_Registrar(self): return self.Sponsoring_Registrar
    def set_Sponsoring_Registrar(self, Sponsoring_Registrar): self.Sponsoring_Registrar = Sponsoring_Registrar
    def get_Registrar_Info(self): return self.Registrar_Info
    def set_Registrar_Info(self, Registrar_Info): self.Registrar_Info = Registrar_Info
    def get_Registrants(self): return self.Registrants
    def set_Registrants(self, Registrants): self.Registrants = Registrants
    def get_Contact_Info(self): return self.Contact_Info
    def set_Contact_Info(self, Contact_Info): self.Contact_Info = Contact_Info
    def get_Remarks(self): return self.Remarks
    def set_Remarks(self, Remarks): self.Remarks = Remarks
    def hasContent_(self):
        if (
            self.Lookup_Date is not None or
            self.Domain_Name is not None or
            self.Domain_ID is not None or
            self.Server_Name is not None or
            self.IP_Address is not None or
            self.DNSSEC is not None or
            self.Nameservers is not None or
            self.Status is not None or
            self.Updated_Date is not None or
            self.Creation_Date is not None or
            self.Expiration_Date is not None or
            self.Regional_Internet_Registry is not None or
            self.Sponsoring_Registrar is not None or
            self.Registrar_Info is not None or
            self.Registrants is not None or
            self.Contact_Info is not None or
            self.Remarks is not None or
            super(WhoisObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WhoisObj:', name_='WhoisObjectType'):
        super(WhoisObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WhoisObjectType')
    def exportChildren(self, lwrite, level, namespace_='WhoisObj:', name_='WhoisObjectType', fromsubclass_=False, pretty_print=True):
        super(WhoisObjectType, self).exportChildren(lwrite, level, 'WhoisObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Lookup_Date is not None:
            self.Lookup_Date.export(lwrite, level, 'WhoisObj:', name_='Lookup_Date', pretty_print=pretty_print)
        if self.Domain_Name is not None:
            self.Domain_Name.export(lwrite, level, 'WhoisObj:', name_='Domain_Name', pretty_print=pretty_print)
        if self.Domain_ID is not None:
            self.Domain_ID.export(lwrite, level, 'WhoisObj:', name_='Domain_ID', pretty_print=pretty_print)
        if self.Server_Name is not None:
            self.Server_Name.export(lwrite, level, 'WhoisObj:', name_='Server_Name', pretty_print=pretty_print)
        if self.IP_Address is not None:
            self.IP_Address.export(lwrite, level, 'WhoisObj:', name_='IP_Address', pretty_print=pretty_print)
        if self.DNSSEC is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDNSSEC>%s</%sDNSSEC>%s' % ('WhoisObj:', self.gds_format_string(quote_xml(self.DNSSEC), input_name='DNSSEC'), 'WhoisObj:', eol_))
        if self.Nameservers is not None:
            self.Nameservers.export(lwrite, level, 'WhoisObj:', name_='Nameservers', pretty_print=pretty_print)
        if self.Status is not None:
            self.Status.export(lwrite, level, 'WhoisObj:', name_='Status', pretty_print=pretty_print)
        if self.Updated_Date is not None:
            self.Updated_Date.export(lwrite, level, 'WhoisObj:', name_='Updated_Date', pretty_print=pretty_print)
        if self.Creation_Date is not None:
            self.Creation_Date.export(lwrite, level, 'WhoisObj:', name_='Creation_Date', pretty_print=pretty_print)
        if self.Expiration_Date is not None:
            self.Expiration_Date.export(lwrite, level, 'WhoisObj:', name_='Expiration_Date', pretty_print=pretty_print)
        if self.Regional_Internet_Registry is not None:
            self.Regional_Internet_Registry.export(lwrite, level, 'WhoisObj:', name_='Regional_Internet_Registry', pretty_print=pretty_print)
        if self.Sponsoring_Registrar is not None:
            self.Sponsoring_Registrar.export(lwrite, level, 'WhoisObj:', name_='Sponsoring_Registrar', pretty_print=pretty_print)
        if self.Registrar_Info is not None:
            self.Registrar_Info.export(lwrite, level, 'WhoisObj:', name_='Registrar_Info', pretty_print=pretty_print)
        if self.Registrants is not None:
            self.Registrants.export(lwrite, level, 'WhoisObj:', name_='Registrants', pretty_print=pretty_print)
        if self.Contact_Info is not None:
            self.Contact_Info.export(lwrite, level, 'WhoisObj:', name_='Contact_Info', pretty_print=pretty_print)
        if self.Remarks is not None:
            self.Remarks.export(lwrite, level, 'WhoisObj:', name_='Remarks', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WhoisObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Lookup_Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Lookup_Date(obj_)
        elif nodeName_ == 'Domain_Name':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Domain_Name(obj_)
        elif nodeName_ == 'Domain_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Domain_ID(obj_)
        elif nodeName_ == 'Server_Name':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Server_Name(obj_)
        elif nodeName_ == 'IP_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
        elif nodeName_ == 'DNSSEC':
            DNSSEC = child_.text
            DNSSEC = self.gds_validate_string(DNSSEC, node, 'DNSSEC')
            self.DNSSEC = DNSSEC
        elif nodeName_ == 'Nameservers':
            obj_ = WhoisNameserversType.factory()
            obj_.build(child_)
            self.set_Nameservers(obj_)
        elif nodeName_ == 'Status':
            obj_ = WhoisStatusesType.factory()
            obj_.build(child_)
            self.set_Status(obj_)
        elif nodeName_ == 'Updated_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Updated_Date(obj_)
        elif nodeName_ == 'Creation_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Date(obj_)
        elif nodeName_ == 'Expiration_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Expiration_Date(obj_)
        elif nodeName_ == 'Regional_Internet_Registry':
            obj_ = RegionalRegistryType.factory()
            obj_.build(child_)
            self.set_Regional_Internet_Registry(obj_)
        elif nodeName_ == 'Sponsoring_Registrar':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sponsoring_Registrar(obj_)
        elif nodeName_ == 'Registrar_Info':
            obj_ = WhoisRegistrarInfoType.factory()
            obj_.build(child_)
            self.set_Registrar_Info(obj_)
        elif nodeName_ == 'Registrants':
            obj_ = WhoisRegistrantsType.factory()
            obj_.build(child_)
            self.set_Registrants(obj_)
        elif nodeName_ == 'Contact_Info':
            obj_ = WhoisContactType.factory()
            obj_.build(child_)
            self.set_Contact_Info(obj_)
        elif nodeName_ == 'Remarks':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Remarks(obj_)
        super(WhoisObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WhoisObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Email_Address': address_object.AddressObjectType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Domain_ID': cybox_common.StringObjectPropertyType,
    'Phone_Number': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'URI': uri_object.URIObjectType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Referral_URL': uri_object.URIObjectType,
    'Registrar_GUID': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Registrant_ID': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'IP_Address': address_object.AddressObjectType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Contributors': cybox_common.PersonnelType,
    'Expiration_Date': cybox_common.DateObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Server_Name': uri_object.URIObjectType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Domain_Name': uri_object.URIObjectType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Creation_Date': cybox_common.DateObjectPropertyType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Contact_ID': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Nameserver': uri_object.URIObjectType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Sponsoring_Registrar': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Libraries': cybox_common.LibrariesType,
    'Whois_Server': uri_object.URIObjectType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Updated_Date': cybox_common.DateObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Registrar_ID': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Whois_Entry'
        rootClass = WhoisObjectType
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
        rootTag = 'Whois_Entry'
        rootClass = WhoisObjectType
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
        rootTag = 'Whois_Entry'
        rootClass = WhoisObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Whois_Entry",
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
    "WhoisObjectType",
    "WhoisRegistrarInfoType",
    "WhoisContactsType",
    "WhoisContactType",
    "WhoisStatusType",
    "WhoisStatusesType",
    "WhoisNameserversType",
    "WhoisRegistrantInfoType",
    "WhoisRegistrantsType",
    "RegionalRegistryType"
    ]
