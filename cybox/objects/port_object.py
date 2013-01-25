import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.port_object_1_3 as port_binding

class port_object(object):
    def __init__(self):
        pass
    
    @classmethod
    def create_from_dict(cls, port_attributes):
        portobj = port_binding.PortObjectType()
        portobj.set_anyAttributes_({'xsi:type' : 'PortObj:PortObjectType'})
        for key, value in port_attributes.items():
            if key == 'port_value' and common_methods.test_value(value):
                portobj.set_Port_Value(common_methods.create_element_from_dict(cybox_common.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'),value))
            elif key == 'layer4_protocol' and common_methods.test_value(value):
                portobj.set_Layer4_Protocol(common_methods.create_element_from_dict(cybox_common.StringObjectAttributeType(datatype='String'),value))
        return portobj

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        if defined_object_dict == None:
            defined_object_dict = {}
        if defined_object.get_Port_Value() is not None:
            defined_object_dict['port_value'] = common_methods.parse_element_into_dict(defined_object.get_Port_Value())
        if defined_object.get_Layer4_Protocol() is not None:
            defined_object_dict['layer4_protocol'] = common_methods.parse_element_into_dict(defined_object.get_Layer4_Protocol())
        return defined_object_dict


