# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.domain_name_object as domainname_binding
from cybox.common import String

class DomainName(ObjectProperties):
    _binding = domainname_binding
    _binding_class = domainname_binding.DomainNameObjectType
    _namespace = "http://cybox.mitre.org/objects#DomainNameObject-1"
    _XSI_NS = "DomainNameObj"
    _XSI_TYPE = "DomainNameObjectType"

    type = cybox.TypedField("type")
    value = cybox.TypedField("Value", String)
