# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.account_object as account_binding
from cybox.common import ObjectProperties, String, DateTime


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
    creation_date = cybox.TypedField("Creation_Date", DateTime)
    modified_date = cybox.TypedField("Modified_Date", DateTime)
    last_accessed_time = cybox.TypedField("Last_Accessed_Time", DateTime)
