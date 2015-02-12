# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.dns_query_object as dns_query_binding
from cybox.common import DateTime, ObjectProperties, String, HexBinary
from cybox.objects.uri_object import URI
from cybox.objects.dns_record_object import DNSRecord


class DNSResourceRecords(cybox.EntityList):
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSResourceRecordsType
    _binding_var = "Resource_Record"
    _contained_type = DNSRecord
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"


class DNSQuestion(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSQuestionType

    qname = cybox.TypedField("QName", URI)
    qtype = cybox.TypedField("QType", String)
    qclass = cybox.TypedField("QClass", String)


class DNSQuery(ObjectProperties):
    _binding = dns_query_binding
    _binding_class = dns_query_binding.DNSQueryObjectType
    _namespace = "http://cybox.mitre.org/objects#DNSQueryObject-2"
    _XSI_NS = "DNSQueryObj"
    _XSI_TYPE = "DNSQueryObjectType"

    successful = cybox.TypedField("successful")
    transaction_id = cybox.TypedField("Transaction_ID", HexBinary)
    question = cybox.TypedField("Question", DNSQuestion)
    answer_resource_records = cybox.TypedField("Answer_Resource_Records",
            DNSResourceRecords)
    authority_resource_records = cybox.TypedField("Authority_Resource_Records",
            DNSResourceRecords)
    additional_records = cybox.TypedField("Additional_Records",
            DNSResourceRecords)
    date_ran = cybox.TypedField("Date_Ran", DateTime)
    service_used = cybox.TypedField("Service_Used", String)
