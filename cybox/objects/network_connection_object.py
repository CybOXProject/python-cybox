# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_connection_object as network_connection_binding
from cybox.common import ObjectProperties, String, DateTime
from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.dns_query_object import DNSQuery


class Layer7Connections(cybox.Entity):
    _binding = network_connection_binding
    _binding_class = network_connection_binding.Layer7ConnectionsType
    _namespace = "http://cybox.mitre.org/objects#NetworkConnectionObject-2"

    http_session = cybox.TypedField("HTTP_Session", HTTPSession)
    dns_query = cybox.TypedField("DNS_Query", DNSQuery, multiple=True)


class NetworkConnection(ObjectProperties):
    _binding = network_connection_binding
    _binding_class = network_connection_binding.NetworkConnectionObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkConnectionObject-2"
    _XSI_NS = "NetworkConnectionObj"
    _XSI_TYPE = "NetworkConnectionObjectType"

    tls_used = cybox.TypedField('tls_used')
    creation_time = cybox.TypedField('Creation_Time', DateTime)
    layer3_protocol = cybox.TypedField('Layer3_Protocol', String)
    layer4_protocol = cybox.TypedField('Layer4_Protocol', String)
    layer7_protocol = cybox.TypedField('Layer7_Protocol', String)
    source_socket_address = cybox.TypedField('Source_Socket_Address',
                                             SocketAddress)
    source_tcp_state = cybox.TypedField('Source_TCP_State')
    destination_socket_address = cybox.TypedField('Destination_Socket_Address',
                                                  SocketAddress)
    destination_tcp_state = cybox.TypedField('Destination_TCP_State')
    layer7_connections = cybox.TypedField('Layer7_Connections',
                                          Layer7Connections)
