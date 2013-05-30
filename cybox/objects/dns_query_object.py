# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.dns_query_object as dns_query_binding
from cybox.objects.uri_object import URI
from cybox.objects.dns_record_object import DNSRecord
from cybox.common import ObjectProperties, String, DateTime

class DNSQuery(ObjectProperties):
    _XSI_NS = "DNSQueryObj"
    _XSI_TYPE = "DNSQueryObjectType"

    def __init__(self):
        super(DNSQuery, self).__init__()
        self.successful = None
        self.question = None
        self.answer_resource_records = None
        self.authority_resource_records = None
        self.additional_records = None
        self.date_ran = None
        self.service_used = None

    def to_obj(self):
        dns_query_obj = dns_query_binding.DNSQueryObjectType()
        super(DNSQuery, self).to_obj(dns_query_obj)

        if self.successful is not None: dns_query_obj.set_successful(self.successful)
        if self.question is not None: dns_query_obj.set_Question(self.question.to_obj())
        if self.answer_resource_records is not None: dns_query_obj.set_Answer_Resource_Records(self.answer_resource_records.to_obj())
        if self.authority_resource_records is not None: dns_query_obj.set_Authority_Resource_Records(self.authority_resource_records.to_obj())
        if self.additional_records is not None: dns_query_obj.set_Additional_Records(self.additional_records.to_obj())
        if self.date_ran is not None: dns_query_obj.set_Date_Ran(self.date_ran.to_obj())
        if self.service_used is not None: dns_query_obj.set_Service_Used(self.service_used.to_obj())

        return dns_query_obj

    def to_dict(self):
        dns_query_dict = {}
        super(DNSQuery, self).to_dict(dns_query_dict)

        if self.successful is not None: dns_query_dict['successful'] = self.successful
        if self.question is not None: dns_query_dict['question'] = self.question.to_dict()
        if self.answer_resource_records is not None: dns_query_dict['answer_resource_records'] = self.answer_resource_records.to_dict()
        if self.authority_resource_records is not None: dns_query_dict['authority_resource_records'] = self.authority_resource_records.to_dict()
        if self.additional_records is not None: dns_query_dict['additional_records'] = self.additional_records.to_dict()
        if self.date_ran is not None: dns_query_dict['date_ran'] = self.date_ran.to_dict()
        if self.service_used is not None: dns_query_dict['service_used'] = self.service_used.to_dict()

        return dns_query_dict
    
    @staticmethod
    def from_dict(dns_query_dict):
        if not dns_query_dict:
            return None

        dns_query_ = DNSQuery()
        dns_query_.successful = dns_query_dict.get('successful')
        dns_query_.question = DNSQuestion.from_dict(dns_query_dict.get('question'))
        dns_query_.answer_resource_records = DNSResourceRecords.from_list(dns_query_dict.get('answer_resource_records'))
        dns_query_.authority_resource_records = DNSResourceRecords.from_list(dns_query_dict.get('authority_resource_records'))
        dns_query_.additional_records = DNSResourceRecords.from_list(dns_query_dict.get('additional_records'))
        dns_query_.date_ran = DateTime.from_dict(dns_query_dict.get('date_ran'))
        dns_query_.service_used = String.from_dict(dns_query_dict.get('service_used'))

        return dns_query_

    @staticmethod
    def from_obj(dns_query_obj):
        if not dns_query_obj:
            return None

        dns_query_ = DNSQuery()
        dns_query_.successful = dns_query_obj.get_successful()
        dns_query_.question = DNSQuestion.from_obj(dns_query_obj.get_Question())
        dns_query_.answer_resource_records = DNSResourceRecords.from_obj(dns_query_obj.get_Answer_Resource_Records())
        dns_query_.authority_resource_records = DNSResourceRecords.from_obj(dns_query_obj.get_Authority_Resource_Records())
        dns_query_.additional_records = DNSResourceRecords.from_obj(dns_query_obj.get_Additional_Records())
        dns_query_.date_ran = DateTime.from_obj(dns_query_obj.get_Date_Ran())
        dns_query_.service_used = String.from_obj(dns_query_obj.get_Service_Used())

        return dns_query_

class DNSQuestion(cybox.Entity):
    def __init__(self):
        self.qname = None
        self.qtype = None
        self.qclass = None

    def to_obj(self):
        dns_question_obj = dns_query_binding.DNSQuestionType()

        if self.qname is not None : dns_question_obj.set_QName(self.qname.to_obj())
        if self.qtype is not None : dns_question_obj.set_QType(self.qtype.to_obj())
        if self.qclass is not None : dns_question_obj.set_QClass(self.qclass.to_obj())

        return dns_question_obj

    def to_dict(self):
        dns_question_dict = {}

        if self.qname is not None : dns_question_dict['qname'] = self.qname.to_dict()
        if self.qtype is not None : dns_question_dict['qtype'] = self.qtype.to_dict()
        if self.qclass is not None : dns_question_dict['qclass'] = self.qclass.to_dict()

        return dns_question_dict

    @staticmethod
    def from_dict(dns_question_dict):
        if not dns_question_dict:
            return None
        dns_question_ = DNSQuestion()
        dns_question_.qname = URI.from_dict(dns_question_dict.get('qname'))
        dns_question_.qtype = String.from_dict(dns_question_dict.get('qtype'))
        dns_question_.qclass = String.from_dict(dns_question_dict.get('qclass'))
        return dns_question_dict

    @staticmethod
    def from_obj(dns_question_obj):
        if not dns_question_obj:
            return None
        dns_question_ = DNSQuestion()
        dns_question_.qname = URI.from_obj(dns_question_obj.get_QName())
        dns_question_.qtype = String.from_obj(dns_question_obj.get_QType())
        dns_question_.qclass = String.from_obj(dns_question_obj.get_QClass())
        return dns_question_dict

class DNSResourceRecords(cybox.EntityList):
    _binding_class = dns_query_binding.DNSResourceRecordsType
    _contained_type = DNSRecord

    def __init__(self):
        super(DNSResourceRecords, self).__init__()
    
    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Resource_Record(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Resource_Record()
