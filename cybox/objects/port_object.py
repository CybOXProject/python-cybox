import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.port_object_1_3 as port_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Port(object):
    def __init__(self):
        pass
    
    @classmethod
    def object_from_dict(cls, port_dict):
        """Create the Port Object object representation from an input dictionary"""
        port_obj = port_binding.PortObjectType()
        port_obj.set_anyAttributes_({'xsi:type' : 'PortObj:PortObjectType'})
        for key, value in port_dict.items():
            if key == 'port_value' and utils.test_value(value):
                port_obj.set_Port_Value(Base_Object_Attribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'),value))
            elif key == 'layer4_protocol' and utils.test_value(value):
                port_obj.set_Layer4_Protocol(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
        return port_obj

    @classmethod
    def dict_from_object(cls, port_obj):
        """Parse and return a dictionary for an Port Object object"""
        port_dict = {}
        if port_obj.get_Port_Value() is not None:
            port_dict['port_value'] = Base_Object_Attribute.dict_from_object(port_obj.get_Port_Value())
        if port_obj.get_Layer4_Protocol() is not None:
            port_dict['layer4_protocol'] = Base_Object_Attribute.dict_from_object(port_obj.get_Layer4_Protocol())
        return port_dict


