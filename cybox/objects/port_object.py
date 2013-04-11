import cybox.utils as utils
#import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.port_object_1_3 as port_binding
from cybox.common import DefinedObject, String, PositiveInteger

class Port(DefinedObject):
    _XSI_TYPE = "PortObjectType"

    def __init__(self):
        self.port_value = None
        self.layer4_protocol = None

    def to_obj(self):
        port_obj = port_binding.PortObjectType()
        port_obj.set_anyAttributes_({'xsi:type' : 'PortObj:PortObjectType'})

        if self.port_value is not None: port_obj.set_Port_Value(self.port_value.to_obj())
        if self.layer4_protocol is not None: port_obj.set_Layer4_Protocol(self.layer4_protocol.to_obj())

        return port_obj

    def to_dict(self):
        port_dict = {}

        if self.port_value is not None: port_dict['port_value'] = self.port_value.to_dict()
        if self.layer4_protocol is not None: port_doct['layer4_protocol'] = self.layer4_protocol.to_dict()
        port_dict['xsi:type'] = _XSI_TYPE

        return port_dict
    
    @staticmethod
    def from_dict(port_dict):
        if not port_dict:
            return None

        port_ = Port()
        port_.port_value = PositiveInteger.from_dict(port_dict.get('port_value'))
        port_.layer4_protocol = String.from_dict(port_dict.get('layer4_protocol'))

        return port_

    @staticmethod
    def from_obj(port_obj):
        if not port_obj:
            return None

        port_ = Port()
        port_.port_value = PositiveInteger.from_obj(port_obj.get_Port_Value())
        port_.layer4_protocol = String.from_obj(port_obj.get_Layer4_Protocol())

        return port_


