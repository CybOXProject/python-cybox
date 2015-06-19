# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.domain_name_object as domainname_binding
from cybox.common import ObjectProperties, String


class DomainName(ObjectProperties):
    _binding = domainname_binding
    _binding_class = domainname_binding.DomainNameObjectType
    _namespace = "http://cybox.mitre.org/objects#DomainNameObject-1"
    _XSI_NS = "DomainNameObj"
    _XSI_TYPE = "DomainNameObjectType"

    type_ = fields.TypedField("type_", key_name='type')
    value = fields.TypedField("Value", String)
