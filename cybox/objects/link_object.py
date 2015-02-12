# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.link_object as link_binding
from cybox.objects.uri_object import URI
from cybox.common import ObjectProperties, String

class Link(URI):
    _binding = link_binding
    _binding_class = link_binding.LinkObjectType
    _namespace = "http://cybox.mitre.org/objects#LinkObject-1"
    _XSI_NS = "LinkObj"
    _XSI_TYPE = "LinkObjectType"

    url_label = cybox.TypedField("URL_Label", String)