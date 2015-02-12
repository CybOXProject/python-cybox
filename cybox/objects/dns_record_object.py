# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.dns_record_object as dns_record_binding
from cybox.common import (Integer, HexBinary, ObjectProperties, String,
        StructuredText, DateTime)
from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI


class DNSRecord(ObjectProperties):
    _binding = dns_record_binding
    _binding_class = dns_record_binding.DNSRecordObjectType
    _namespace = 'http://cybox.mitre.org/objects#DNSRecordObject-2'
    _XSI_NS = "DNSRecordObj"
    _XSI_TYPE = "DNSRecordObjectType"

    description = cybox.TypedField("Description", StructuredText)
    domain_name = cybox.TypedField("Domain_Name", URI)
    queried_date = cybox.TypedField("Queried_Date", DateTime)
    ip_address = cybox.TypedField("IP_Address", Address)
    address_class = cybox.TypedField("Address_Class", String)
    entry_type = cybox.TypedField("Entry_Type", String)
    record_name = cybox.TypedField("Record_Name", String)
    record_type = cybox.TypedField("Record_Type", String)
    ttl = cybox.TypedField("TTL", Integer)
    flags = cybox.TypedField("Flags", HexBinary)
    data_length = cybox.TypedField("Data_Length", Integer)
    record_data = cybox.TypedField("Record_Data")
