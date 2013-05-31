# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.port_object as port_binding
from cybox.common import ObjectProperties, String, PositiveInteger


class Port(ObjectProperties):
    _XSI_NS = "PortObj"
    _XSI_TYPE = "PortObjectType"

    def __init__(self):
        super(Port, self).__init__()
        self.port_value = None
        self.layer4_protocol = None

    def to_obj(self):
        port_obj = port_binding.PortObjectType()
        super(Port, self).to_obj(port_obj)

        if self.port_value is not None:
            port_obj.set_Port_Value(self.port_value.to_obj())
        if self.layer4_protocol is not None:
            port_obj.set_Layer4_Protocol(self.layer4_protocol.to_obj())

        return port_obj

    def to_dict(self):
        port_dict = {}
        super(Port, self).to_dict(port_dict)

        if self.port_value is not None:
            port_dict['port_value'] = self.port_value.to_dict()
        if self.layer4_protocol is not None:
            port_dict['layer4_protocol'] = self.layer4_protocol.to_dict()

        return port_dict

    @staticmethod
    def from_dict(port_dict):
        if not port_dict:
            return None

        port = Port()
        ObjectProperties.from_dict(port_dict, port)

        port.port_value = PositiveInteger.from_dict(port_dict.get('port_value'))
        port.layer4_protocol = String.from_dict(port_dict.get('layer4_protocol'))

        return port

    @staticmethod
    def from_obj(port_obj):
        if not port_obj:
            return None

        port = Port()
        ObjectProperties.from_obj(port_obj, port)

        port.port_value = PositiveInteger.from_obj(port_obj.get_Port_Value())
        port.layer4_protocol = String.from_obj(port_obj.get_Layer4_Protocol())

        return port
