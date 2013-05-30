# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.dns_record_object as dns_record_binding
from cybox.common.structured_text import StructuredText
from cybox.objects.uri_object import URI
from cybox.objects.address_object import Address
from cybox.common import ObjectProperties, String, Integer, HexBinary

class DNSRecord(ObjectProperties):
    _XSI_NS = "DNSRecordObj"
    _XSI_TYPE = "DNSRecordObjectType"

    def __init__(self):
        super(DNSRecord, self).__init__()
        self.description = None
        self.domain_name = None
        self.ip_address = None
        self.address_class = None
        self.entry_type = None
        self.record_name = None
        self.record_type = None
        self.ttl = None
        self.flags = None
        self.data_length = None
        self.record_data = None

    def to_obj(self):
        dns_record_obj = dns_record_binding.DNSRecordObjectType()
        super(DNSRecord, self).to_obj(dns_record_obj)

        if self.description is not None: dns_record_obj.set_Description(self.description.to_obj())
        if self.domain_name is not None: dns_record_obj.set_Domain_Name(self.domain_name.to_obj())
        if self.ip_address is not None: dns_record_obj.set_IP_Address(self.ip_address.to_obj())
        if self.address_class is not None: dns_record_obj.set_Address_Class(self.address_class.to_obj())
        if self.entry_type is not None: dns_record_obj.set_Entry_Type(self.entry_type.to_obj())
        if self.record_name is not None: dns_record_obj.set_Record_Name(self.record_name.to_obj())
        if self.record_type is not None: dns_record_obj.set_Record_Type(self.record_type.to_obj())
        if self.ttl is not None: dns_record_obj.set_TTL(self.ttl.to_obj())
        if self.flags is not None: dns_record_obj.set_Flags(self.flags.to_obj())
        if self.data_length is not None: dns_record_obj.set_Data_Length(self.data_length.to_obj())
        if self.record_data is not None: dns_record_obj.set_Record_Data(self.record_data)

        return dns_record_obj

    def to_dict(self):
        dns_record_dict = {}
        super(DNSRecord, self).to_dict(dns_record_dict)

        if self.description is not None: dns_record_dict['description'] = self.description.to_dict()
        if self.domain_name is not None: dns_record_dict['domain_name'] = self.domain_name.to_dict()
        if self.ip_address is not None: dns_record_dict['ip_address'] = self.ip_address.to_dict()
        if self.address_class is not None: dns_record_dict['address_class'] = self.address_class.to_dict()
        if self.entry_type is not None: dns_record_dict['entry_type'] = self.entry_type.to_dict()
        if self.record_name is not None: dns_record_dict['record_name'] = self.record_name.to_dict()
        if self.record_type is not None: dns_record_dict['record_type'] = self.record_type.to_dict()
        if self.ttl is not None: dns_record_dict['ttl'] = self.ttl.to_dict()
        if self.flags is not None: dns_record_dict['flags'] = self.flags.to_dict()
        if self.data_length is not None: dns_record_dict['data_length'] = self.data_length.to_dict()
        if self.record_data is not None: dns_record_dict['record_data'] = self.record_data

        return dns_record_dict
    
    @staticmethod
    def from_dict(dns_record_dict):
        if not dns_record_dict:
            return None

        dns_record_ = DNSRecord()
        dns_record_.description = StructuredText.from_dict(dns_record_dict.get('description'))
        dns_record_.domain_name = URI.from_dict(dns_record_dict.get('domain_name'))
        dns_record_.ip_address = Address.from_dict(dns_record_dict.get('ip_address'))
        dns_record_.address_class = String.from_dict(dns_record_dict.get('address_class'))
        dns_record_.entry_type = String.from_dict(dns_record_dict.get('entry_type'))
        dns_record_.record_name = String.from_dict(dns_record_dict.get('record_name'))
        dns_record_.record_type = String.from_dict(dns_record_dict.get('record_type'))
        dns_record_.ttl = Integer.from_dict(dns_record_dict.get('record_type'))
        dns_record_.flags = HexBinary.from_dict(dns_record_dict.get('flags'))
        dns_record_.data_length = Integer.from_dict(dns_record_dict.get('data_length'))
        dns_record_.record_data = dns_record_dict.get('record_data')

        return dns_record_

    @staticmethod
    def from_obj(dns_record_obj):
        if not dns_record_obj:
            return None

        dns_record_ = DNSRecord()
        dns_record_.description = StructuredText.from_obj(dns_record_obj.get_Description())
        dns_record_.domain_name = URI.from_obj(dns_record_obj.get_Domain_Name())
        dns_record_.ip_address = Address.from_obj(dns_record_obj.get_IP_Address())
        dns_record_.address_class = String.from_obj(dns_record_obj.get_Address_Class())
        dns_record_.entry_type = String.from_obj(dns_record_obj.get_Entry_Type())
        dns_record_.record_name = String.from_obj(dns_record_obj.get_Record_Name())
        dns_record_.record_type = String.from_obj(dns_record_obj.get_Record_Type())
        dns_record_.ttl = Integer.from_obj(dns_record_obj.get_TTL())
        dns_record_.flags = HexBinary.from_obj(dns_record_obj.get_Flags())
        dns_record_.data_length = Integer.from_obj(dns_record_obj.get_Length())
        dns_record_.record_data = dns_record_obj.get_Record_Data()

        return dns_record_
