# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.network_socket_object as network_socket_binding
from cybox.objects.socket_address_object import SocketAddress
from cybox.common import ObjectProperties, String, UnsignedInteger, NonNegativeInteger


class SocketOptions(entities.Entity):
    _binding = network_socket_binding
    _binding_class = network_socket_binding.SocketOptionsType
    _namespace = "http://cybox.mitre.org/objects#NetworkSocketObject-2"

    ip_multicast_if = fields.TypedField("IP_MULTICAST_IF", String)
    ip_multicast_if2 = fields.TypedField("IP_MULTICAST_IF2", String)
    ip_multicast_loop = fields.TypedField("IP_MULTICAST_LOOP")
    ip_tos = fields.TypedField("IP_TOS", String)
    so_broadcast = fields.TypedField("SO_BROADCAST")
    so_conditional_accept = fields.TypedField("SO_CONDITIONAL_ACCEPT")
    so_keepalive = fields.TypedField("SO_KEEPALIVE")
    so_dontroute = fields.TypedField("SO_DONTROUTE")
    so_linger = fields.TypedField("SO_LINGER", UnsignedInteger)
    so_dontlinger = fields.TypedField("SO_DONTLINGER")
    so_oobinline = fields.TypedField("SO_OOBINLINE")
    so_rcvbuf =  fields.TypedField("SO_RCVBUF", UnsignedInteger)
    so_group_priority = fields.TypedField("SO_GROUP_PRIORITY", UnsignedInteger)
    so_reuseaddr = fields.TypedField("SO_REUSEADDR")
    so_debug = fields.TypedField("SO_DEBUG")
    so_rcvtimeo = fields.TypedField("SO_RCVTIMEO", UnsignedInteger)
    so_sndbuf = fields.TypedField("SO_SNDBUF", UnsignedInteger)
    so_sndtimeo = fields.TypedField("SO_SNDTIMEO", UnsignedInteger)
    so_update_accept_context = fields.TypedField("SO_UPDATE_ACCEPT_CONTEXT", UnsignedInteger)
    so_timeout = fields.TypedField("SO_TIMEOUT", UnsignedInteger)
    tcp_nodelay = fields.TypedField("TCP_NODELAY")


class NetworkSocket(ObjectProperties):
    _binding = network_socket_binding
    _binding_class = network_socket_binding.NetworkSocketObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkSocketObject-2"
    _XSI_NS = "NetworkSocketObj"
    _XSI_TYPE = "NetworkSocketObjectType"

    is_blocking = fields.TypedField("is_blocking")
    is_listening = fields.TypedField("is_listening")
    address_family = fields.TypedField("Address_Family", String)
    domain = fields.TypedField("Domain", String)
    local_address = fields.TypedField("Local_Address", SocketAddress)
    options = fields.TypedField("Options", SocketOptions)
    protocol = fields.TypedField("Protocol", String)
    remote_address = fields.TypedField("Remote_Address", SocketAddress)
    type_ = fields.TypedField("Type", String)
    socket_descriptor = fields.TypedField("Socket_Descriptor", NonNegativeInteger)
