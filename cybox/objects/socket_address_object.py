# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.socket_address_object as socket_address_binding
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port
from cybox.objects.hostname_object import Hostname
from cybox.common import ObjectProperties


class SocketAddress(ObjectProperties):
    _binding = socket_address_binding
    _binding_class = socket_address_binding.SocketAddressObjectType
    _namespace = "http://cybox.mitre.org/objects#SocketAddressObject-1"
    _XSI_NS = "SocketAddressObj"
    _XSI_TYPE = "SocketAddressObjectType"

    #TODO: make sure this is an IPV4 or IPV6 Address
    #TODO: choice between ip_address and hostname
    ip_address = fields.TypedField("IP_Address", Address)
    hostname = fields.TypedField("Hostname", Hostname)
    port = fields.TypedField("Port", Port)
