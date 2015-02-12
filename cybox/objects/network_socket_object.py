# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_socket_object as network_socket_binding
from cybox.objects.socket_address_object import SocketAddress
from cybox.common import ObjectProperties, String, UnsignedInteger, NonNegativeInteger

class SocketOptions(cybox.Entity):
    _binding = network_socket_binding
    _binding_class = network_socket_binding.SocketOptionsType
    _namespace = "http://cybox.mitre.org/objects#NetworkSocketObject-2"

    ip_multicast_if = cybox.TypedField("IP_MULTICAST_IF", String)
    ip_multicast_if2 = cybox.TypedField("IP_MULTICAST_IF2", String)
    ip_multicast_loop = cybox.TypedField("IP_MULTICAST_LOOP")
    ip_tos = cybox.TypedField("IP_TOS", String)
    so_broadcast = cybox.TypedField("SO_BROADCAST")
    so_conditional_accept = cybox.TypedField("SO_CONDITIONAL_ACCEPT")
    so_keepalive = cybox.TypedField("SO_KEEPALIVE")
    so_dontroute = cybox.TypedField("SO_DONTROUTE")
    so_linger = cybox.TypedField("SO_LINGER", UnsignedInteger)
    so_dontlinger = cybox.TypedField("SO_DONTLINGER")
    so_oobinline = cybox.TypedField("SO_OOBINLINE")
    so_rcvbuf =  cybox.TypedField("SO_RCVBUF", UnsignedInteger)
    so_group_priority = cybox.TypedField("SO_GROUP_PRIORITY", UnsignedInteger)
    so_reuseaddr = cybox.TypedField("SO_REUSEADDR")
    so_debug = cybox.TypedField("SO_DEBUG")
    so_rcvtimeo = cybox.TypedField("SO_RCVTIMEO", UnsignedInteger)
    so_sndbuf = cybox.TypedField("SO_SNDBUF", UnsignedInteger)
    so_sndtimeo = cybox.TypedField("SO_SNDTIMEO", UnsignedInteger)
    so_update_accept_context = cybox.TypedField("SO_UPDATE_ACCEPT_CONTEXT", UnsignedInteger)
    so_timeout = cybox.TypedField("SO_TIMEOUT", UnsignedInteger)
    tcp_nodelay = cybox.TypedField("TCP_NODELAY")

class NetworkSocket(ObjectProperties):
    _binding = network_socket_binding
    _binding_class = network_socket_binding.NetworkSocketObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkSocketObject-2"
    _XSI_NS = "NetworkSocketObj"
    _XSI_TYPE = "NetworkSocketObjectType"

    is_blocking = cybox.TypedField("is_blocking")
    is_listening = cybox.TypedField("is_listening")
    address_family = cybox.TypedField("Address_Family", String)
    domain = cybox.TypedField("Domain", String)
    local_address = cybox.TypedField("Local_Address", SocketAddress)
    options = cybox.TypedField("Options", SocketOptions)
    protocol = cybox.TypedField("Protocol", String)
    remote_address = cybox.TypedField("Remote_Address", SocketAddress)
    type_ = cybox.TypedField("Type", String)
    socket_descriptor = cybox.TypedField("Socket_Descriptor", NonNegativeInteger)


