# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.socket_address_object as socket_address_binding 
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port
from cybox.common import ObjectProperties

class SocketAddress(ObjectProperties):
    _XSI_NS = "SocketAddressObj"
    _XSI_TYPE = "SocketAddressObjectType"

    def __init__(self):
        super(SocketAddress, self).__init__()
        self.ip_address = None
        self.port = None

    def to_obj(self):
        socket_address_obj = socket_address_binding.SocketAddressObjectType()
        super(SocketAddress, self).to_obj(socket_address_obj)

        if self.ip_address is not None: socket_address_obj.set_IP_Address(self.ip_address.to_obj())
        if self.port is not None: socket_address_obj.set_Port(self.port.to_obj())

        return socket_address_obj

    def to_dict(self):
        socket_address_dict = {}
        super(SocketAddress, self).to_dict(socket_address_dict)

        if self.ip_address is not None: port_dict['ip_address'] = self.ip_address.to_dict()
        if self.port is not None: port_doct['port'] = self.port.to_dict()

        return socket_address_dict
    
    @staticmethod
    def from_dict(socket_address_dict):
        if not socket_address_dict:
            return None

        socket_address_ = SocketAddress()
        socket_address_.ip_address = Address.from_dict(socket_address_dict.get('ip_address'))
        socket_address_.port = Port.from_dict(socket_address_dict.get('port'))

        return socket_address_

    @staticmethod
    def from_obj(socket_address_obj):
        if not socket_address_obj:
            return None

        socket_address_ = SocketAddress()
        socket_address_.ip_address = Address.from_obj(socket_address_obj.get_IP_Address())
        socket_address_.port = Port.from_obj(socket_address_obj.get_Port())

        return socket_address_


