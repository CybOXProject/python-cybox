# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.domain_name_object as domainname_binding
from cybox.common import ObjectProperties, String


class DomainName(ObjectProperties):
    _binding = domainname_binding
    _binding_class = domainname_binding.DomainNameObjectType
    _namespace = "http://cybox.mitre.org/objects#DomainNameObject-1"
    _XSI_NS = "DomainNameObj"
    _XSI_TYPE = "DomainNameObjectType"

    type_ = cybox.TypedField("type_", key_name='type')
    value = cybox.TypedField("Value", String)
