# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.account_object as account_binding
from cybox.common import ObjectProperties, String, DateTime, VocabString

class StructuredAuthenticationMechanism(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.StructuredAuthenticationMechanismType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"
    
    description = cybox.TypedField("Description", String)   
    
class Authentication(cybox.Entity):
    _binding = account_binding
    _binding_class = account_binding.AuthenticationType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"
    
    authentication_type = cybox.TypedField("Authentication_Type", VocabString)
    authentication_data = cybox.TypedField("Authentication_Data", String)
    authentication_token_protection_mechanism = cybox.TypedField("Authentication_Token_Protection_Mechanism", VocabString)
    structured_authentication_mechanism = cybox.TypedField("Structured_Authentication_Mechanism", StructuredAuthenticationMechanism)

class Account(ObjectProperties):
    _binding = account_binding
    _binding_class = account_binding.AccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#AccountObject-2'
    _XSI_NS = "AccountObj"
    _XSI_TYPE = "AccountObjectType"

    disabled = cybox.TypedField("disabled")
    locked_out = cybox.TypedField("locked_out")
    description = cybox.TypedField("Description", String)
    domain = cybox.TypedField("Domain", String)
    authentication = cybox.TypedField("Authentication", Authentication, multiple=True)
    creation_date = cybox.TypedField("Creation_Date", DateTime)
    modified_date = cybox.TypedField("Modified_Date", DateTime)
    last_accessed_time = cybox.TypedField("Last_Accessed_Time", DateTime)
 
