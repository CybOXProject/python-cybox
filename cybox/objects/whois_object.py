# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.whois_object as whois_binding

import cybox
from cybox.common import ObjectProperties, BaseProperty, String, DateTime, Date
from cybox.objects.address_object import Address, EmailAddress
from cybox.objects.uri_object import URI
from cybox import TypedField


class WhoisNameservers(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisNameserversType
    _binding_var = "Nameserver"
    _contained_type = URI
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisStatus(BaseProperty):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisStatusType
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    datatype = "string"


class WhoisStatuses(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisStatusesType
    _binding_var = "Status"
    _contained_type = WhoisStatus
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisContact(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"

    contact_id = TypedField("Contact_ID", String)
    contact_type = TypedField("Contact_Type", String)
    name = TypedField("Name", String)
    address = TypedField("Address", String)
    email_address = TypedField("Email_Address", Address)
    phone_number = TypedField("Phone_Number", String)


    def __init__(self):
        super(WhoisContact, self).__init__()

    def to_dict(self, contact_dict=None):
        if contact_dict is None:
            contact_dict = {}

        if self.contact_type is not None:
            contact_dict['contact_type'] = self.contact_type
        if self.contact_id is not None:
            contact_dict['contact_id'] = self.contact_id.to_dict()
        if self.name is not None:
            contact_dict['name'] = self.name.to_dict()
        if self.email_address is not None:
            contact_dict['email_address'] = self.email_address.to_dict()
        if self.phone_number is not None:
            contact_dict['phone_number'] = self.phone_number.to_dict()
        if self.address is not None:
            contact_dict['address'] = self.address.to_dict()

        return contact_dict

    @staticmethod
    def from_dict(contact_dict, contact=None):
        if not contact_dict:
            return None

        if contact is None:
            contact = WhoisContact()

        contact.contact_type = contact_dict.get('contact_type')
        contact.contact_id = String.from_dict(contact_dict.get('contact_id'))
        contact.name = String.from_dict(contact_dict.get('name'))
        contact.email_address = EmailAddress.from_dict(contact_dict.get('email_address'))
        contact.phone_number = String.from_dict(contact_dict.get('phone_number'))
        contact.address = String.from_dict(contact_dict.get('address'))

        return contact


class WhoisContacts(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisContactsType
    _binding_var = "Contact"
    _contained_type = WhoisContact
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisRegistrant(WhoisContact):
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrantInfoType

    registrant_id = TypedField("Registrant_ID", String)

    def __init__(self):
        super(WhoisRegistrant, self).__init__()

    def to_dict(self):
        registrant_dict = {}

        super(WhoisRegistrant, self).to_dict(registrant_dict)
        if self.registrant_id is not None:
            registrant_dict['registrant_id'] = self.registrant_id.to_dict()

        return registrant_dict

    @staticmethod
    def from_dict(registrant_dict):
        if registrant_dict is None:
            return None

        registrant = WhoisRegistrant()
        WhoisContact.from_dict(registrant_dict, registrant)

        registrant.registrant_id = String.from_dict(registrant_dict.get('registrant_id'))

        return registrant


class WhoisRegistrants(cybox.EntityList):
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrantsType
    _binding_var = "Registrant"
    _contained_type = WhoisRegistrant
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"


class WhoisRegistrar(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    _binding = whois_binding
    _binding_class = whois_binding.WhoisRegistrarInfoType

    registrar_id = TypedField("Registrar_ID", String)
    registrar_guid = TypedField("Registrar_GUID", String)
    name = TypedField("Name", String)
    address = TypedField("Address", String)
    email_address = TypedField("Email_Address", Address)
    phone_number = TypedField("Phone_Number", String)
    whois_server = TypedField("Whois_Server", URI)
    referral_url = TypedField("Referral_URL", URI)
    contacts = TypedField("Contacts", WhoisContacts)

    def __init__(self):
        super(WhoisRegistrar, self).__init__()

    def to_dict(self):
        registrar_dict = {}

        if self.registrar_id is not None:
            registrar_dict['registrar_id'] = self.registrar_id.to_dict()
        if self.registrar_guid is not None:
            registrar_dict['registrar_guid'] = self.registrar_guid.to_dict()
        if self.name is not None:
            registrar_dict['name'] = self.name.to_dict()
        if self.address is not None:
            registrar_dict['address'] = self.address.to_dict()
        if self.email_address is not None:
            registrar_dict['email_address'] = self.email_address.to_dict()
        if self.phone_number is not None:
            registrar_dict['phone_number'] = self.phone_number.to_dict()
        if self.whois_server is not None:
            registrar_dict['whois_server'] = self.whois_server.to_dict()
        if self.referral_url is not None:
            registrar_dict['referral_url'] = self.referral_url.to_dict()
        if self.contacts:
            registrar_dict['contacts'] = self.contacts.to_list()

        return registrar_dict

    @staticmethod
    def from_dict(registrar_dict):
        if not registrar_dict:
            return None

        registrar = WhoisRegistrar()

        registrar.registrar_id = String.from_dict(registrar_dict.get('registrar_id'))
        registrar.registrar_guid = String.from_dict(registrar_dict.get('registrar_guid'))
        registrar.name = String.from_dict(registrar_dict.get('name'))
        registrar.address = String.from_dict(registrar_dict.get('address'))
        registrar.email_address = Address.from_dict(registrar_dict.get('email_address'), Address.CAT_EMAIL)
        registrar.phone_number = String.from_dict(registrar_dict.get('phone_number'))
        registrar.whois_server = URI.from_dict(registrar_dict.get('whois_server'))
        registrar.referral_url = URI.from_dict(registrar_dict.get('referral_url'))
        registrar.contacts = WhoisContacts.from_list(registrar_dict.get('contacts'))

        return registrar



class WhoisEntry(ObjectProperties):
    _namespace = "http://cybox.mitre.org/objects#WhoisObject-2"
    _XSI_NS = 'WhoisObj'
    _XSI_TYPE = 'WhoisObjectType'
    _binding = whois_binding
    _binding_class = whois_binding.WhoisObjectType
    
    contact_info = TypedField("Contact_Info", WhoisContact)
    domain_name = TypedField("Domain_Name", URI)
    domain_id = TypedField("Domain_ID", String)
    server_name = TypedField("Server_Name", URI)
    ip_address = TypedField("IP_Address", Address)
    dnssec = TypedField("DNSSEC", String)
    nameservers = TypedField("Nameservers", WhoisNameservers)
    status = TypedField("Status", WhoisStatuses)
    updated_date = TypedField("Updated_Date", Date)
    creation_date = TypedField("Creation_Date", Date)
    expiration_date = TypedField("Expiration_Date", Date)
    regional_internet_registry = TypedField("Regional_Internet_Registry", String)
    sponsoring_registrar = TypedField("Sponsoring_Registrar", String)
    registrar_info = TypedField("Registrar_Info", WhoisRegistrar)
    registrants = TypedField("Registrants", WhoisRegistrants)

    DNSSEC_SIGNED = "Signed"
    DNSSEC_UNSIGNED = "Unsigned"

    def __init__(self):
        super(WhoisEntry, self).__init__()

    def to_dict(self):
        whois_dict = {}
        super(WhoisEntry, self).to_dict(whois_dict)

        if self.domain_name is not None:
            whois_dict['domain_name'] = self.domain_name.to_dict()
        if self.domain_id is not None:
            whois_dict['domain_id'] = self.domain_id.to_dict()
        if self.server_name is not None:
            whois_dict['server_name'] = self.server_name.to_dict()
        if self.ip_address is not None:
            whois_dict['ip_address'] = self.ip_address.to_dict()
        if self.dnssec is not None:
            whois_dict['dnssec'] = self.dnssec
        if self.nameservers:
            whois_dict['nameservers'] = self.nameservers.to_list()
        if self.status:
            whois_dict['status'] = self.status.to_list()
        if self.updated_date is not None:
            whois_dict['updated_date'] = self.updated_date.to_dict()
        if self.creation_date is not None:
            whois_dict['creation_date'] = self.creation_date.to_dict()
        if self.expiration_date is not None:
            whois_dict['expiration_date'] = self.expiration_date.to_dict()
        if self.regional_internet_registry is not None:
            whois_dict['regional_internet_registry'] = self.regional_internet_registry.to_dict()
        if self.sponsoring_registrar is not None:
            whois_dict['sponsoring_registrar'] = self.sponsoring_registrar.to_dict()
        if self.registrar_info is not None:
            whois_dict['registrar_info'] = self.registrar_info.to_dict()
        if self.registrants is not None:
            whois_dict['registrants'] = self.registrants.to_list()
        if self.contact_info is not None:
            whois_dict['contact_info'] = self.contact_info.to_dict()

        return whois_dict

    @staticmethod
    def from_dict(whois_dict):
        if not whois_dict:
            return None

        whois = WhoisEntry()
        ObjectProperties.from_dict(whois_dict, whois)

        whois.domain_name = URI.from_dict(whois_dict.get('domain_name'))
        whois.domain_id = String.from_dict(whois_dict.get('domain_id'))
        whois.server_name = URI.from_dict(whois_dict.get('server_name'))
        whois.ip_address = Address.from_dict(whois_dict.get('ip_address'), Address.CAT_IPV4)
        whois.dnssec = whois_dict.get('dnssec')
        whois.nameservers = WhoisNameservers.from_list(whois_dict.get('nameservers'))
        whois.status = WhoisStatuses.from_list(whois_dict.get('status'))
        whois.updated_date = DateTime.from_dict(whois_dict.get('updated_date'))
        whois.creation_date = DateTime.from_dict(whois_dict.get('creation_date'))
        whois.expiration_date = DateTime.from_dict(whois_dict.get('expiration_date'))
        whois.regional_internet_registry = String.from_dict(whois_dict.get('regional_internet_registry'))
        whois.sponsoring_registrar = String.from_dict(whois_dict.get('sponsoring_registrar'))
        whois.registrar_info = WhoisRegistrar.from_dict(whois_dict.get('registrar_info'))
        whois.registrants = WhoisRegistrants.from_list(whois_dict.get('registrants'))
        whois.contact_info = WhoisContact.from_dict(whois_dict.get('contact_info'))

        return whois

