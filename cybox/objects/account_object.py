# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.account_object as account_binding
from cybox.common import ObjectProperties, String, DateTime
from cybox.common.vocabs import VocabField


class StructuredAuthenticationMechanism(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.StructuredAuthenticationMechanismType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"

    description = fields.TypedField("Description", String)


class Authentication(entities.Entity):
    _binding = account_binding
    _binding_class = account_binding.AuthenticationType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"

    authentication_type = VocabField("Authentication_Type")
    authentication_data = fields.TypedField("Authentication_Data", String)
    authentication_token_protection_mechanism = VocabField("Authentication_Token_Protection_Mechanism")
    structured_authentication_mechanism = fields.TypedField("Structured_Authentication_Mechanism", StructuredAuthenticationMechanism)


class Account(ObjectProperties):
    _binding = account_binding
    _binding_class = account_binding.AccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"

    disabled = fields.TypedField("disabled")
    locked_out = fields.TypedField("locked_out")
    description = fields.TypedField("Description", String)
    domain = fields.TypedField("Domain", String)
    authentication = fields.TypedField("Authentication", Authentication, multiple=True)
    creation_date = fields.TypedField("Creation_Date", DateTime)
    modified_date = fields.TypedField("Modified_Date", DateTime)
    last_accessed_time = fields.TypedField("Last_Accessed_Time", DateTime)
 
