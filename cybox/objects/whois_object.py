import cybox.bindings.whois_object as whois_binding

from cybox.common import ObjectProperties, String
from cybox.objects.uri_object import URI


class WhoisEntry(ObjectProperties):
    _XSI_NS = 'WhoisObj'
    _XSI_TYPE = 'WhoisObjectType'

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

        return whois_obj

    def to_dict(self):
        whois_dict = {}
        super(WhoisEntry, self).to_dict(whois_dict)

        if self.domain_name is not None:
            whois_dict['domain_name'] = self.domain_name.to_dict()
        if self.domain_id is not None:
            whois_dict['domain_id'] = self.domain_id.to_dict()

        return whois_dict

    @staticmethod
    def from_obj(whois_obj):
        if not whois_obj:
            return None

        whois = WhoisEntry()
        ObjectProperties.from_obj(whois_obj, whois)

        whois.domain_name = URI.from_obj(whois_obj.get_Domain_Name())
        whois.domain_id = String.from_obj(whois_obj.get_Domain_ID())

        return whois

    @staticmethod
    def from_dict(whois_dict):
        if not whois_dict:
            return None

        whois = WhoisEntry()
        ObjectProperties.from_dict(whois_dict, whois)

        whois.domain_name = URI.from_dict(whois_dict.get('domain_name'))
        whois.domain_id = String.from_dict(whois_dict.get('domain_id'))

        return whois
