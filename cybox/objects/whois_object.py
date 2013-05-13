# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.whois_object as whois_binding

import cybox
from cybox.common import ObjectProperties, BaseProperty, String, DateTime
from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI


class WhoisNameservers(cybox.EntityList):
    _binding_class = whois_binding.WhoisNameserversType
    _contained_type = URI

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Nameserver(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Nameserver()


class WhoisStatus(BaseProperty):
    def __init__(self, *args, **kwargs):
        BaseProperty.__init__(self, *args, **kwargs)
        self.datatype = "string"

    def _get_binding_class(self):
        return whois_binding.WhoisStatusType


class WhoisStatuses(cybox.EntityList):
    _binding_class = whois_binding.WhoisStatusesType
    _contained_type = WhoisStatus

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Status(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Status()


class WhoisEntry(ObjectProperties):
    _XSI_NS = 'WhoisObj'
    _XSI_TYPE = 'WhoisObjectType'

    DNSSEC_SIGNED = "Signed"
    DNSSEC_UNSIGNED = "Unsigned"

    def __init__(self):
        super(WhoisEntry, self).__init__()

        self.domain_name = None
        self.domain_id = None
        self.server_name = None
        self.ip_address = None
        self.dnssec = None
        self.nameservers = None
        self.status = None
        self.updated_date = None
        self.creation_date = None
        self.expiration_date = None
        self.regional_internet_registry = None
        self.sponsoring_registrar = None
        self.registrar_info = None
        self.registrants = None
        self.contact_info = None

    def to_obj(self):
        whois_obj = whois_binding.WhoisObjectType()
        super(WhoisEntry, self).to_obj(whois_obj)

        if self.domain_name is not None:
            whois_obj.set_Domain_Name(self.domain_name.to_obj())
        if self.domain_id is not None:
            whois_obj.set_Domain_ID(self.domain_id.to_obj())
        if self.server_name is not None:
            whois_obj.set_Server_Name(self.server_name.to_obj())
        if self.ip_address is not None:
            whois_obj.set_IP_Address(self.ip_address.to_obj())
        if self.dnssec is not None:
            whois_obj.set_DNSSEC(self.dnssec)
        if self.nameservers:
            whois_obj.set_Nameservers(self.nameservers.to_obj())
        if self.status:
            whois_obj.set_Status(self.status.to_obj())
        if self.updated_date is not None:
            whois_obj.set_Updated_Date(self.updated_date.to_obj())
        if self.creation_date is not None:
            whois_obj.set_Creation_Date(self.creation_date.to_obj())
        if self.expiration_date is not None:
            whois_obj.set_Expiration_Date(self.expiration_date.to_obj())
        if self.regional_internet_registry is not None:
            whois_obj.set_Regional_Internet_Registry(self.regional_internet_registry.to_obj())
        if self.sponsoring_registrar is not None:
            whois_obj.set_Sponsoring_Registrar(self.sponsoring_registrar.to_obj())
        if self.registrar_info is not None:
            whois_obj.set_Registrar_Info(self.registrar_info.to_obj())
        if self.registrants is not None:
            whois_obj.set_Registrants(self.registrants.to_obj())
        if self.contact_info is not None:
            whois_obj.set_Contact_Info(self.contact_info.to_obj())

        return whois_obj

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
    def from_obj(whois_obj):
        if not whois_obj:
            return None

        whois = WhoisEntry()
        ObjectProperties.from_obj(whois_obj, whois)

        whois.domain_name = URI.from_obj(whois_obj.get_Domain_Name())
        whois.domain_id = String.from_obj(whois_obj.get_Domain_ID())
        whois.server_name = URI.from_obj(whois_obj.get_Server_Name())
        whois.ip_address = Address.from_obj(whois_obj.get_IP_Address())
        whois.dnssec = whois_obj.get_DNSSEC()
        whois.nameservers = WhoisNameservers.from_obj(whois_obj.get_Nameservers())
        whois.status = WhoisStatuses.from_obj(whois_obj.get_Status())
        whois.updated_date = DateTime.from_obj(whois_obj.get_Updated_Date())
        whois.creation_date = DateTime.from_obj(whois_obj.get_Creation_Date())
        whois.expiration_date = DateTime.from_obj(whois_obj.get_Expiration_Date())
        whois.regional_internet_registry = String.from_obj(whois_obj.get_Regional_Internet_Registry())
        whois.sponsoring_registrar = String.from_obj(whois_obj.get_Sponsoring_Registrar())
        whois.registrar_info = WhoisRegistrar.from_obj(whois_obj.get_Registrar_Info())
        whois.registrants = WhoisRegistrants.from_obj(whois_obj.get_Registrants())
        whois.contact_info = WhoisContact.from_obj(whois_obj.get_Contact_Info())

        return whois

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


class WhoisContact(cybox.Entity):

    def __init__(self):
        self.contact_type = None
        self.contact_id = None
        self.name = None
        self.email_address = None
        self.phone_number = None
        self.address = None

    def to_obj(self, contact_obj=None):
        if contact_obj is None:
            contact_obj = whois_binding.WhoisContactType()

        if self.contact_type is not None:
            contact_obj.set_contact_type(self.contact_type)
        if self.contact_id is not None:
            contact_obj.set_Contact_ID(self.contact_id.to_obj())
        if self.name is not None:
            contact_obj.set_Name(self.name.to_obj())
        if self.email_address is not None:
            contact_obj.set_Email_Address(self.email_address.to_obj())
        if self.phone_number is not None:
            contact_obj.set_Phone_Number(self.phone_number.to_obj())
        if self.address is not None:
            contact_obj.set_Address(self.address.to_obj())

        return contact_obj

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
    def from_obj(contact_obj, contact=None):
        if not contact_obj:
            return None

        if contact is None:
            contact = WhoisContact()

        contact.contact_type = contact_obj.get_contact_type()
        contact.contact_id = String.from_obj(contact_obj.get_Contact_ID())
        contact.name = String.from_obj(contact_obj.get_Name())
        contact.email_address = Address.from_obj(contact_obj.get_Email_Address())
        contact.phone_number = String.from_obj(contact_obj.get_Phone_Number())
        contact.address = String.from_obj(contact_obj.get_Address())

        return contact

    @staticmethod
    def from_dict(contact_dict, contact=None):
        if not contact_dict:
            return None

        if contact is None:
            contact = WhoisContact()

        contact.contact_type = contact_dict.get('contact_type')
        contact.contact_id = String.from_dict(contact_dict.get('contact_id'))
        contact.name = String.from_dict(contact_dict.get('name'))
        contact.email_address = Address.from_dict(contact_dict.get('email_address'), Address.CAT_EMAIL)
        contact.phone_number = String.from_dict(contact_dict.get('phone_number'))
        contact.address = String.from_dict(contact_dict.get('address'))

        return contact


class WhoisContacts(cybox.EntityList):
    _binding_class = whois_binding.WhoisContactsType
    _contained_type = WhoisContact

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Contact(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Contact()


class WhoisRegistrant(WhoisContact):

    def __init__(self):
        super(WhoisRegistrant, self).__init__()
        self.registrant_id = None

    def to_obj(self):
        registrant_obj = whois_binding.WhoisRegistrantInfoType()

        super(WhoisRegistrant, self).to_obj(registrant_obj)
        if self.registrant_id is not None:
            registrant_obj.set_Registrant_ID(self.registrant_id.to_obj())

        return registrant_obj

    def to_dict(self):
        registrant_dict = {}

        super(WhoisRegistrant, self).to_dict(registrant_dict)
        if self.registrant_id is not None:
            registrant_dict['registrant_id'] = self.registrant_id.to_dict()

        return registrant_dict

    @staticmethod
    def from_obj(registrant_obj):
        if not registrant_obj:
            return None

        registrant = WhoisRegistrant()
        WhoisContact.from_obj(registrant_obj, registrant)

        registrant.registrant_id = String.from_obj(registrant_obj.get_Registrant_ID())

        return registrant

    @staticmethod
    def from_dict(registrant_dict):
        if registrant_dict is None:
            return None

        registrant = WhoisRegistrant()
        WhoisContact.from_dict(registrant_dict, registrant)

        registrant.registrant_id = String.from_dict(registrant_dict.get('registrant_id'))

        return registrant


class WhoisRegistrants(cybox.EntityList):
    _binding_class = whois_binding.WhoisRegistrantsType
    _contained_type = WhoisRegistrant

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Registrant(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Registrant()


class WhoisRegistrar(cybox.Entity):

    def __init__(self):
        self.registrar_id = None
        self.registrar_guid = None
        self.name = None
        self.address = None
        self.email_address = None
        self.phone_number = None
        self.whois_server = None
        self.referral_url = None
        self.contacts = None

    def to_obj(self):
        registrar_obj = whois_binding.WhoisRegistrarInfoType()

        if self.registrar_id is not None:
            registrar_obj.set_Registrar_ID(self.registrar_id.to_obj())
        if self.registrar_guid is not None:
            registrar_obj.set_Registrar_GUID(self.registrar_guid.to_obj())
        if self.name is not None:
            registrar_obj.set_Name(self.name.to_obj())
        if self.address is not None:
            registrar_obj.set_Address(self.address.to_obj())
        if self.email_address is not None:
            registrar_obj.set_Email_Address(self.email_address.to_obj())
        if self.phone_number is not None:
            registrar_obj.set_Phone_Number(self.phone_number.to_obj())
        if self.whois_server is not None:
            registrar_obj.set_Whois_Server(self.whois_server.to_obj())
        if self.referral_url is not None:
            registrar_obj.set_Referral_URL(self.referral_url.to_obj())
        if self.contacts:
            registrar_obj.set_Contacts(self.contacts.to_obj())

        return registrar_obj

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
    def from_obj(registrar_obj):
        if not registrar_obj:
            return None

        registrar = WhoisRegistrar()

        registrar.registrar_id = String.from_obj(registrar_obj.get_Registrar_ID())
        registrar.registrar_guid = String.from_obj(registrar_obj.get_Registrar_GUID())
        registrar.name = String.from_obj(registrar_obj.get_Name())
        registrar.address = String.from_obj(registrar_obj.get_Address())
        registrar.email_address = Address.from_obj(registrar_obj.get_Email_Address())
        registrar.phone_number = String.from_obj(registrar_obj.get_Phone_Number())
        registrar.whois_server = URI.from_obj(registrar_obj.get_Whois_Server())
        registrar.referral_url = URI.from_obj(registrar_obj.get_Referral_URL())
        registrar.contacts = WhoisContacts.from_obj(registrar_obj.get_Contacts())

        return registrar

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
