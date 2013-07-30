# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.socket_address_object as socket_address_binding
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port
from cybox.common import ObjectProperties


class SocketAddress(ObjectProperties):
    _binding = socket_address_binding
    _binding_class = socket_address_binding.SocketAddressObjectType
    _namespace = "http://cybox.mitre.org/objects#SocketAddressObject-1"
    _XSI_NS = "SocketAddressObj"
    _XSI_TYPE = "SocketAddressObjectType"

    #TODO: make sure this is an IPV4 or IPV6 Address
    ip_address = cybox.TypedField("IP_Address", Address)
    port = cybox.TypedField("Port", Port)
