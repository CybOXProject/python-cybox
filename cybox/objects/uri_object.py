# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields
from mixbox.vendor import six

import cybox.bindings.uri_object as uri_binding
from cybox.common import ObjectProperties, AnyURI


@six.python_2_unicode_compatible
class URI(ObjectProperties):
    _binding = uri_binding
    _binding_class = uri_binding.URIObjectType
    _namespace = 'http://cybox.mitre.org/objects#URIObject-2'
    _XSI_NS = 'URIObj'
    _XSI_TYPE = "URIObjectType"

    TYPE_URL = "URL"
    TYPE_GENERAL = "General URN"
    TYPE_DOMAIN = "Domain Name"

    TYPES = (TYPE_URL, TYPE_GENERAL, TYPE_DOMAIN)

    value = fields.TypedField("Value", AnyURI)
    type_ = fields.TypedField("type_", key_name="type")

    def __init__(self, value=None, type_=None):
        super(URI, self).__init__()
        self.value = value
        self.type_ = type_

    def __str__(self):
        return six.text_type(self.value)
