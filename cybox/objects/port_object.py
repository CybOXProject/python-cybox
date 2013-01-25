import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.port_object_1_3 as port_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute

class port_object(object):
    def __init__(self):
        pass
    
    @classmethod
    def create_from_dict(cls, port_attributes):
        """Create the Port Object object representation from an input dictionary"""
        portobj = port_object_binding.PortObjectType()
        portobj.set_anyAttributes_({'xsi:type' : 'PortObj:PortObjectType'})
        for key, value in port_attributes.items():
            if key == 'port_value' and common_methods.test_value(value):
                portobj.set_Port_Value(baseobjectattribute.create_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'),value))
            elif key == 'layer4_protocol' and common_methods.test_value(value):
                portobj.set_Layer4_Protocol(baseobjectattribute.create_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
        return portobj

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        """Parse and return a dictionary for an Port Object object"""
        if defined_object_dict == None:
            defined_object_dict = {}
        if defined_object.get_Port_Value() is not None:
            defined_object_dict['port_value'] = baseobjectattribute.parse_into_dict(defined_object.get_Port_Value())
        if defined_object.get_Layer4_Protocol() is not None:
            defined_object_dict['layer4_protocol'] = baseobjectattribute.parse_into_dict(defined_object.get_Layer4_Protocol())
        return defined_object_dict


