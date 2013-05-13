# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_socket_object as network_socket_binding
from cybox.objects.socket_address_object import SocketAddress
from cybox.common import ObjectProperties, String, UnsignedInteger

class NetworkSocket(ObjectProperties):
    _XSI_NS = "NetworkSocketObj"
    _XSI_TYPE = "NetworkSocketObjectType"

    def __init__(self):
        super(NetworkSocket, self).__init__()
        self.is_blocking = None
        self.is_listening = None
        self.address_family = None
        self.domain = None
        self.local_address = None
        self.options = None
        self.protocol = None
        self.remote_address = None
        self.type = None

    def to_obj(self):
        network_socket_obj = network_socket_binding.NetworkSocketObjectType()
        network_socket_obj.set_xsi_type(self._XSI_NS + ':' + self._XSI_TYPE)
        if self.is_blocking is not None : network_socket_obj.set_is_blocking(self.is_blocking)
        if self.is_listening is not None : network_socket_obj.set_is_listening(self.is_listening)
        if self.address_family is not None : network_socket_obj.set_Address_Family(self.address_family.to_obj())
        if self.domain is not None : network_socket_obj.set_Domain(self.domain.to_obj())
        if self.local_address is not None : network_socket_obj.set_Local_Address(self.local_address.to_obj())
        if self.options is not None : network_socket_obj.set_Options(self.options.to_obj())
        if self.protocol is not None : network_socket_obj.set_Protocol(self.protocol.to_obj())
        if self.remote_address is not None : network_socket_obj.set_Remote_Address(self.remote_address.to_obj())
        if self.type is not None : network_socket_obj.set_Type(self.type.to_obj())
        return network_socket_obj

    def to_dict(self):
        network_socket_dict = {}
        if self.is_blocking is not None : network_socket_dict['is_blocking'] = self.is_blocking
        if self.is_listening is not None : network_socket_dict['is_listening'] = self.is_listening
        if self.address_family is not None : network_socket_dict['address_family'] = self.address_family.to_dict()
        if self.domain is not None : network_socket_dict['domain'] = self.address_family.to_dict()
        if self.local_address is not None : network_socket_dict['local_address'] = self.local_address.to_dict()
        if self.options is not None : network_socket_dict['options'] = self.options.to_dict()
        if self.protocol is not None : network_socket_dict['protocol'] = self.protocol.to_dict()
        if self.remote_address is not None : network_socket_dict['remote_address'] = self.remote_address.to_dict()
        if self.type is not None : network_socket_dict['type'] = self.type.to_dict()
        return network_socket_dict

    def from_dict(network_socket_dict):
        if not network_socket_dict:
            return None
        network_socket_ = NetworkSocket()
        network_socket_.is_blocking = network_socket_dict.get('is_blocking')
        network_socket_.is_listening = network_socket_dict.get('is_listening')
        network_socket_.address_family = String.from_dict(network_socket_dict.get('address_family'))
        network_socket_.domain = String.from_dict(network_socket_dict.get('domain'))
        network_socket_.local_address = SocketAddress.from_dict(network_socket_dict.get('local_address'))
        network_socket_.options = SocketOptions.from_dict(network_socket_dict.get('options'))
        network_socket_.protocol = String.from_dict(network_socket_dict.get('protocol'))
        network_socket_.remote_address = SocketAddress.from_dict(network_socket_dict.get('remote_address'))
        network_socket_.type = String.from_dict(network_socket_dict.get('type'))
        return network_socket_

    def from_obj(network_socket_obj):
        if not network_socket_obj:
            return None
        network_socket_ = NetworkSocket()
        network_socket_.is_blocking = network_socket_obj.get_is_blocking()
        network_socket_.is_listening = network_socket_obj.get_is_listening()
        network_socket_.address_family = String.from_obj(network_socket_obj.get_Address_Family())
        network_socket_.domain = String.from_obj(network_socket_obj.get_Domain())
        network_socket_.local_address = SocketAddress.from_obj(network_socket_obj.get_Local_Address())
        network_socket_.options = SocketOptions.from_obj(network_socket_obj.get_Options())
        network_socket_.protocol = String.from_obj(network_socket_obj.get_Protocol())
        network_socket_.remote_address = SocketAddress.from_obj(network_socket_obj.get_Remote_Address())
        network_socket_.type = String.from_obj(network_socket_obj.get_Type())
        return network_socket_

class SocketOptions(cybox.Entity):
    def __init__(self):
        super(SocketOptions, self).__init__()
        self.ip_multicast_if = None
        self.ip_multicast_if2 = None
        self.ip_multicast_loop = None
        self.ip_tos = None
        self.so_broadcast = None
        self.so_conditional_accept = None
        self.so_keepalive = None
        self.so_dontroute = None
        self.so_linger = None
        self.so_dontlinger = None
        self.so_oobinline = None
        self.so_rcvbuf = None
        self.so_group_priority = None
        self.so_reuseaddr = None
        self.so_debug = None
        self.so_rcvtimeo = None
        self.so_sndbuf = None
        self.so_sndtimeo = None
        self.so_update_accept_context = None
        self.so_timeout = None
        self.tcp_nodelay = None

    def to_obj(self):
        socket_options_obj = network_socket_binding.SocketOptionsType()
        if ip_multicast_if is not None : socket_options_obj.set_IP_MULTICAST_IF(self.ip_multicast_if.to_obj())
        if ip_multicast_if2 is not None : socket_options_obj.set_IP_MULTICAST_IF2(self.ip_multicast_if2.to_obj())
        if ip_multicast_loop is not None : socket_options_obj.set_IP_MULTICAST_LOOP(self.ip_multicast_loop)
        if ip_tos is not None : socket_options_obj.set_IP_TOS(self.ip_tos.to_obj())
        if so_broadcast is not None : socket_options_obj.set_IP_BROADCAST(self.ip_tos)
        if so_conditional_accept is not None : socket_options_obj.set_SO_CONDITIONAL_ACCEPT(self.so_conditional_accept)
        if so_keepalive is not None : socket_options_obj.set_SO_KEEPALIVE(self.so_keepalive)
        if so_dontroute is not None : socket_options_obj.set_SO_DONTROUTE(self.so_dontroute)
        if so_linger is not None : socket_options_obj.set_SO_LINGER(self.so_linger.to_obj())
        if so_dontlinger is not None : socket_options_obj.set_SO_DONTLINGER(self.so_dontlinger)
        if so_oobinline is not None : socket_options_obj.set_SO_OOBINLINE(self.so_oobinline)
        if so_rcvbuf is not None : socket_options_obj.set_SO_RCVBUF(self.so_rcvbuf.to_obj())
        if so_group_priority is not None : socket_options_obj.set_SO_GROUP_PRIORITY(self.so_group_priority.to_obj())
        if so_reuseaddr is not None : socket_options_obj.set_SO_REUSEADDR(self.so_reuseaddr)
        if so_debug is not None : socket_options_obj.set_SO_DEBUG(self.so_debug)
        if so_rcvtimeo is not None : socket_options_obj.set_SO_RCVTIMEO(self.so_rcvtimeo.to_obj())
        if so_sndbuf is not None : socket_options_obj.set_SO_SNDBUF(self.so_sndbuf.to_obj())
        if so_sndtimeo is not None : socket_options_obj.set_SO_SNDTIMEO(self.so_sndtimeo.to_obj())
        if so_update_accept_context is not None : socket_options_obj.set_SO_UPDATE_ACCEPT_CONTEXT(self.so_update_accept_context.to_obj())
        if so_timeout is not None : socket_options_obj.set_SO_TIMEOUT(self.so_timeout.to_obj())
        if tcp_nodelay is not None : socket_options_obj.set_TCP_NODELAY(self.tcp_nodelay)
        return socket_options_obj

    def to_dict(self):
        socket_options_dict = {}
        if ip_multicast_if is not None : socket_options_dict['ip_multicast_if'] = self.ip_multicast_if.to_dict()
        if ip_multicast_if2 is not None : socket_options_dict['ip_multicast_if2'] = self.ip_multicast_if2.to_dict()
        if ip_multicast_loop is not None : socket_options_dict['ip_multicast_loop'] = self.ip_multicast_loop
        if ip_tos is not None : socket_options_dict['ip_tos'] = self.ip_tos.to_dict()
        if so_broadcast is not None : socket_options_dict['so_broadcast'] = self.so_broadcast
        if so_conditional_accept is not None : socket_options_dict['so_conditional_accept'] = self.so_conditional_accept
        if so_keepalive is not None : socket_options_dict['so_keepalive'] = self.so_keepalive
        if so_dontroute is not None : socket_options_dict['so_dontroute'] = self.so_dontroute
        if so_linger is not None : socket_options_dict['so_linger'] = self.so_linger.to_dict()
        if so_dontlinger is not None : socket_options_dict['so_dontlinger'] = self.so_dontlinger
        if so_oobinline is not None : socket_options_dict['so_oobinline'] = self.so_oobinline
        if so_rcvbuf is not None : socket_options_dict['so_rcvbuf'] = self.so_rcvbuf.to_dict()
        if so_group_priority is not None : socket_options_dict['so_group_priority'] = self.so_group_priority.to_dict()
        if so_reuseaddr is not None : socket_options_dict['so_reuseaddr'] = self.so_reuseaddr
        if so_debug is not None : socket_options_dict['so_debug'] = self.so_debug
        if so_rcvtimeo is not None : socket_options_dict['so_rcvtimeo'] = self.so_rcvtimeo.to_dict()
        if so_sndbuf is not None : socket_options_dict['so_sndbuf'] = self.so_sndbuf.to_dict()
        if so_sndtimeo is not None : socket_options_dict['so_sndtimeo'] = self.so_sndtimeo.to_dict()
        if so_update_accept_context is not None : socket_options_dict['so_update_accept_context'] = self.so_update_accept_context.to_dict()
        if so_timeout is not None : socket_options_dict['so_timeout'] = self.so_timeout.to_dict()
        if tcp_nodelay is not None : socket_options_dict['tcp_nodelay'] = self.tcp_nodelay
        return socket_options_dict

    @staticmethod
    def from_dict(socket_options_dict):
        if not socket_options_dict:
            return None
        socket_options_ = SocketOptions()
        socket_options_.ip_multicast_if = String.from_dict(socket_options_dict.get('ip_multicast_if'))
        socket_options_.ip_multicast_if2 = String.from_dict(socket_options_dict.get('ip_multicast_if2'))
        socket_options_.ip_multicast_loop = socket_options_dict.get('ip_multicast_loop')
        socket_options_.ip_tos = String.from_dict(socket_options_dict.get('ip_tos'))
        socket_options_.so_broadcast = socket_options_dict.get('so_broadcast')
        socket_options_.so_conditional_accept = socket_options_dict.get('so_conditional_accept')
        socket_options_.so_keepalive = socket_options_dict.get('so_keepalive')
        socket_options_.so_dontroute = socket_options_dict.get('so_dontroute')
        socket_options_.so_linger = UnsignedInteger.from_dict(socket_options_dict.get('so_linger'))
        socket_options_.so_dontlinger = socket_options_dict.get('so_dontlinger')
        socket_options_.so_oobinline = socket_options_dict.get('so_oobinline')
        socket_options_.so_rcvbuf = UnsignedInteger.from_dict(socket_options_dict.get('so_rcvbuf'))
        socket_options_.so_group_priority = UnsignedInteger.from_dict(socket_options_dict.get('so_group_priority'))
        socket_options_.so_reuseaddr = socket_options_dict.get('so_reuseaddr')
        socket_options_.so_debug = socket_options_dict.get('so_debug')
        socket_options_.so_rcvtimeo = UnsignedInteger.from_dict(socket_options_dict.get('so_rcvtimeo'))
        socket_options_.so_sndbuf = UnsignedInteger.from_dict(socket_options_dict.get('so_sndbuf'))
        socket_options_.so_sndtimeo = UnsignedInteger.from_dict(socket_options_dict.get('so_sndtimeo'))
        socket_options_.so_update_accept_context = UnsignedInteger.from_dict(socket_options_dict.get('so_update_accept_context'))
        socket_options_.so_timeout = UnsignedInteger.from_dict(socket_options_dict.get('so_timeout'))
        socket_options_.tcp_nodelay = socket_options_dict.get('tcp_nodelay')
        return socket_options_

    @staticmethod
    def from_obj(socket_options_obj):
        if not socket_options_obj:
            return None
        socket_options_ = SocketOptions()
        socket_options_.ip_multicast_if = String.from_obj(socket_options_obj.get_IP_MULTICAST_IF())
        socket_options_.ip_multicast_if2 = String.from_obj(socket_options_obj.get_IP_MULTICAST_IF2())
        socket_options_.ip_multicast_loop = socket_options_obj.get_IP_MULTICAST_LOOP()
        socket_options_.ip_tos = String.from_obj(socket_options_obj.get_IP_TOS())
        socket_options_.so_broadcast = socket_options_obj.get_SO_BROADCAST()
        socket_options_.so_conditional_accept = socket_options_obj.get_SO_CONDITIONAL_ACCEPT()
        socket_options_.so_keepalive = socket_options_obj.get_SO_KEEPALIVE()
        socket_options_.so_dontroute = socket_options_obj.get_SO_DONTROUTE()
        socket_options_.so_linger = UnsignedInteger.from_obj(socket_options_obj.get_SO_LINGER())
        socket_options_.so_dontlinger = socket_options_obj.get_SO_DONTLINGER()
        socket_options_.so_oobinline = socket_options_obj.get_SO_OOBINLINE()
        socket_options_.so_rcvbuf = UnsignedInteger.from_obj(socket_options_obj.get_SO_RCVBUF())
        socket_options_.so_group_priority = UnsignedInteger.from_obj(socket_options_obj.get_SO_GROUP_PRIORITY())
        socket_options_.so_reuseaddr = socket_options_obj.get_SO_REUSEADDR()
        socket_options_.so_debug = socket_options_obj.get_SO_DEBUG()
        socket_options_.so_rcvtimeo = UnsignedInteger.from_obj(socket_options_obj.get_SO_RCVTIMEO())
        socket_options_.so_sndbuf = UnsignedInteger.from_obj(socket_options_obj.get_SO_SNDBUF())
        socket_options_.so_sndtimeo = UnsignedInteger.from_obj(socket_options_obj.get_SO_SNDTIMEO())
        socket_options_.so_update_accept_context = UnsignedInteger.from_obj(socket_options_obj.get_UPDATE_ACCEPT_CONTEXT())
        socket_options_.so_timeout = UnsignedInteger.from_obj(socket_options_obj.get_SO_TIMEOUT())
        socket_options_.tcp_nodelay = socket_options_obj.get_TCP_NODELAY()
        return socket_options_
