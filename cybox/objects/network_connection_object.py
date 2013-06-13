# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_connection_object as network_connection_binding
from cybox.objects.socket_address_object import SocketAddress
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.dns_query_object import DNSQuery
from cybox.common import ObjectProperties, String, DateTime

class NetworkConnection(ObjectProperties):
    _XSI_NS = "NetworkConnectionObj"
    _XSI_TYPE = "NetworkConnectionObjectType"

    def __init__(self):
        super(NetworkConnection, self).__init__()
        self.tls_used = None
        self.creation_time = None
        self.layer3_protocol = None
        self.layer4_protocol = None
        self.layer7_protocol = None
        self.source_socket_address = None
        self.source_tcp_state = None
        self.destination_socket_address = None
        self.destination_tcp_state = None
        self.layer7_connections = None

    def to_obj(self):
        network_connection_obj = network_connection_binding.NetworkConnectionObjectType()
        super(NetworkConnection, self).to_obj(network_connection_obj)

        if self.tls_used is not None : network_connection_obj.set_tls_used(self.tls_used)
        if self.creation_time is not None : network_connection_obj.set_Creation_Time(self.creation_time.to_obj())
        if self.layer3_protocol is not None : network_connection_obj.set_Layer3_Protocol(self.layer3_protocol.to_obj())
        if self.layer4_protocol is not None : network_connection_obj.set_Layer4_Protocol(self.layer4_protocol.to_obj())
        if self.layer7_protocol is not None : network_connection_obj.set_Layer7_Protocol(self.layer7_protocol.to_obj())
        if self.source_socket_address is not None : network_connection_obj.set_Source_Socket_Address(self.source_socket_address.to_obj())
        if self.source_tcp_state is not None : network_connection_obj.set_Source_TCP_State(self.source_tcp_state)
        if self.destination_socket_address is not None : network_connection_obj.set_Destination_Socket_Address(self.destination_socket_address.to_obj())
        if self.destination_tcp_state is not None : network_connection_obj.set_Destination_TCP_State(self.source_tcp_state)
        if self.layer7_connections is not None : network_connection_obj.set_Layer7_Connections(self.layer7_connections.to_obj())

        return network_connection_obj

    def to_dict(self):
        network_connection_dict = {}
        super(NetworkConnection, self).to_dict(network_connection_dict)

        if self.tls_used is not None : network_connection_dict['tls_used'] = self.tls_used
        if self.creation_time is not None : network_connection_dict['creation_time'] = self.creation_time.to_dict()
        if self.layer3_protocol is not None : network_connection_dict['layer3_protocol'] = self.layer3_protocol.to_dict()
        if self.layer4_protocol is not None : network_connection_dict['layer4_protocol'] = self.layer4_protocol.to_dict()
        if self.layer7_protocol is not None : network_connection_dict['layer7_protocol'] = self.layer7_protocol.to_dict()
        if self.source_socket_address is not None : network_connection_dict['source_socket_address'] = self.source_socket_address.to_dict()
        if self.source_tcp_state is not None : network_connection_dict['source_tcp_state'] = self.source_tcp_state
        if self.destination_socket_address is not None : network_connection_dict['destination_socket_address'] = self.destination_socket_address.to_dict()
        if self.destination_tcp_state is not None : network_connection_dict['destination_tcp_state'] = self.destination_tcp_state
        if self.layer7_connections is not None : network_connection_dict['layer7_connections'] = self.layer7_connections.to_dict()

        return network_connection_dict

    @staticmethod
    def from_dict(network_connection_dict):
        if not network_connection_dict:
            return None
        network_connection_ = NetworkConnection()
        network_connection_.tls_used = network_connection_dict.get('tls_used')
        network_connection_.creation_time = DateTime.from_dict(network_connection_dict.get('creation_time'))
        network_connection_.layer3_protocol = String.from_dict(network_connection_dict.get('layer3_protocol'))
        network_connection_.layer4_protocol = String.from_dict(network_connection_dict.get('layer4_protocol'))
        network_connection_.layer7_protocol = String.from_dict(network_connection_dict.get('layer7_protocol'))
        network_connection_.source_socket_address = SocketAddress.from_dict(network_connection_dict.get('source_socket_address'))
        network_connection_.source_tcp_state = network_connection_dict.get('source_tcp_state')
        network_connection_.destination_socket_address = SocketAddress.from_dict(network_connection_dict.get('destination_socket_address'))
        network_connection_.destination_tcp_state = network_connection_dict.get('destination_tcp_state')
        network_connection_.layer7_connections = Layer7Connections.from_dict(network_connection_dict.get('layer7_connections'))

        return network_connection_

    @staticmethod
    def from_obj(network_connection_obj):
        if not network_connection_obj:
            return None
        network_connection_ = NetworkConnection()
        network_connection_.tls_used = network_connection_obj.get_tls_used()
        network_connection_.creation_time = DateTime.from_obj(network_connection_obj.get_Creation_Time())
        network_connection_.layer3_protocol = String.from_obj(network_connection_obj.get_Layer3_Protocol())
        network_connection_.layer4_protocol = String.from_obj(network_connection_obj.get_Layer4_Protocol())
        network_connection_.layer7_protocol = String.from_obj(network_connection_obj.get_Layer7_Protocol())
        network_connection_.source_socket_address = SocketAddress.from_obj(network_connection_obj.get_Source_Socket_Address())
        network_connection_.source_tcp_state = network_connection_obj.get_Source_TCP_State()
        network_connection_.destination_socket_address = SocketAddress.from_obj(network_connection_obj.get_Destination_Socket_Address())
        network_connection_.destination_tcp_state = network_connection_obj.get_Destination_TCP_State()
        network_connection_.layer7_connections = Layer7Connections.from_obj(network_connection_obj.get_Layer7_Connections())

        return network_connection_

class Layer7Connections(cybox.Entity):

    def __init__(self):
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
