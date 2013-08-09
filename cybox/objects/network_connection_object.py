# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_connection_object as network_connection_binding
from cybox.common import ObjectProperties, String, DateTime
from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.dns_query_object import DNSQuery

# TODO: convert Layer7Connections to new style (requires TypedFields to allow
# multiples)

class Layer7Connections(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#NetworkConnectionObject-2"

    def __init__(self):
        super(Layer7Connections, self).__init__()
        self.http_session = None
        self.dns_queries = []

    def to_obj(self):
        layer7_connections_obj = network_connection_binding.Layer7ConnectionsType()

        if self.http_session is not None: layer7_connections_obj.set_HTTP_Session(self.http_session.to_obj())
        if len(self.dns_queries) > 0:
            for query in self.dns_queries:
                layer7_connections_obj.add_DNS_Query(query.to_obj())

        return layer7_connections_obj

    def to_dict(self):
        layer7_connections_dict = {}

        if self.http_session is not None: layer7_connections_dict['http_session'] = self.http_session.to_dict()
        if len(self.dns_queries) > 0:
            layer7_connections_dict['dns_queries'] = [dns_query.to_dict() for dns_query in self.dns_queries]

        return layer7_connections_dict

    @staticmethod
    def from_dict(layer7_connections_dict):
        if not layer7_connections_dict:
            return None
        layer7_connections_ = Layer7Connections()
        layer7_connections_.http_session = HTTPSession.from_dict(layer7_connections_dict.get('http_session'))
        if layer7_connections_dict.get('dns_queries') is not None:
            layer7_connections_.dns_queries = [DNSQuery.from_dict(x) for x in layer7_connections_dict.get('dns_queries', [])]
        return layer7_connections_

    @staticmethod
    def from_obj(layer7_connections_obj):
        if not layer7_connections_obj:
            return None
        layer7_connections_ = Layer7Connections()
        layer7_connections_.http_session = HTTPSession.from_obj(layer7_connections_obj.get_HTTP_Session())
        layer7_connections_.dns_queries = [DNSQuery.from_obj(x) for x in layer7_connections_obj.get_DNS_Query()]
        return layer7_connections_


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
    source_tcp_state = cybox.TypedField('source_tcp_state')
    destination_socket_address = cybox.TypedField('Destination_Socket_Address',
                                                  SocketAddress)
    destination_tcp_state = cybox.TypedField('destination_tcp_state')
    layer7_connections = cybox.TypedField('Layer7_Connections',
                                          Layer7Connections)

