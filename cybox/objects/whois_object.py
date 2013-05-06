import cybox.bindings.whois_object as whois_binding

import cybox
from cybox.common import ObjectProperties, BaseProperty, String, DateTime
from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI


class Nameservers(cybox.EntityList):
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

        if self.sponsoring_registrar is not None:
            whois_obj.set_Sponsoring_Registrar(self.sponsoring_registrar.to_obj())

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

        if self.sponsoring_registrar is not None:
            whois_dict['sponsoring_registrar'] = self.sponsoring_registrar.to_dict()

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
        whois.nameservers = Nameservers.from_obj(whois_obj.get_Nameservers())
        whois.status = WhoisStatuses.from_obj(whois_obj.get_Status())
        whois.updated_date = DateTime.from_obj(whois_obj.get_Updated_Date())
        whois.creation_date = DateTime.from_obj(whois_obj.get_Creation_Date())
        whois.expiration_date = DateTime.from_obj(whois_obj.get_Expiration_Date())

        whois.sponsoring_registrar = String.from_obj(whois_obj.get_Sponsoring_Registrar())

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
        whois.nameservers = Nameservers.from_list(whois_dict.get('nameservers'))
        whois.status = WhoisStatuses.from_list(whois_dict.get('status'))
        whois.updated_date = DateTime.from_dict(whois_dict.get('updated_date'))
        whois.creation_date = DateTime.from_dict(whois_dict.get('creation_date'))
        whois.expiration_date = DateTime.from_dict(whois_dict.get('expiration_date'))

        whois.sponsoring_registrar = String.from_dict(whois_dict.get('sponsoring_registrar'))

        return whois
