# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.account_object as account_binding
from cybox.common import ObjectProperties, String


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
