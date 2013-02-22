import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.network_connection_object_1_0 as network_connection_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port
from cybox.objects.http_session_object import HTTP_Session

class Network_Connection(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, network_connection_attributes):
        """Create the Network Connection Object object representation from an input dictionary"""
        network_connection_obj = network_connection_binding.NetworkConnectionType()
        for key, value in network_connection_attributes.items():
            if key == 'tls_used' and utils.test_value(value):
                network_connection_obj.set_tls_used(value.get('value'))
            elif key == 'layer3_protocol' and utils.test_value(value):
                network_connection_obj.set_Layer3_Protocol(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'layer4_protocol' and utils.test_value(value):
                network_connection_obj.set_Layer4_Protocol(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'layer7_protocol' and utils.test_value(value):
                network_connection_obj.set_Layer7_Protocol(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'local_ip_address':
                network_connection_obj.set_Local_IP_Address(Address.object_from_dict(value))
            elif key == 'local_port': 
                network_connection_obj.set_Local_Port(Port.object_from_dict(value))
            elif key == 'remote_ip_address':
                network_connection_obj.set_Remote_IP_Address(Address.object_from_dict(value))
            elif key == 'remote_port': 
                network_connection_obj.set_Local_Port(Port.object_from_dict(value))
            elif key == 'layer7_connections':
                layer7_conn_object = network_connection_binding.Layer7ConnectionsType()
                if value.get('http_session') is not None: layer7_conn_object.set_HTTP_Session(HTTP_Session.object_from_dict(value.get('http_session')))
                if layer7_conn_object.hasContent_() : network_connection_obj.set_Layer7_Connections(layer7_conn_object)
        return network_connection_obj

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Network Connection Object object"""
        defined_object_dict = {}
        if defined_object.get_tls_used() is not None: defined_object_dict['tls_used'] = {'value' : defined_object.get_tls_used()}
        if defined_object.get_Layer3_Protocol() is not None: defined_object_dict['layer3_protocol'] = Base_Object_Attribute.dict_from_object(defined_object.get_Layer3_Protocol())
        if defined_object.get_Layer4_Protocol() is not None: defined_object_dict['layer4_protocol'] = Base_Object_Attribute.dict_from_object(defined_object.get_Layer4_Protocol())
        if defined_object.get_Layer7_Protocol() is not None: defined_object_dict['layer7_protocol'] = Base_Object_Attribute.dict_from_object(defined_object.get_Layer7_Protocol())
        if defined_object.get_Local_IP_Address() is not None: defined_object_dict['local_ip_address'] = Address.dict_from_object(defined_object.get_Local_IP_Address())
        if defined_object.get_Local_Port() is not None: defined_object_dict['local_port'] = Port.dict_from_object(defined_object.get_Local_Port())
        if defined_object.get_Remote_IP_Address() is not None: defined_object_dict['remote_ip_address'] = Address.dict_from_object(defined_object.get_Remote_IP_Address())
        if defined_object.get_Remote_Port() is not None: defined_object_dict['remote_port'] = Port.dict_from_object(defined_object.get_Remote_Port())
        if defined_object.get_Layer7_Connections() is not None:
            layer7_conn = defined_object.get_Layer7_Connections()
            layer7_conn_dict = {}
            if layer7_conn.get_HTTP_Session() is not None: layer7_conn_dict['http_session'] = HTTP_Session.dict_from_object(layer7_conn.get_HTTP_Session())
            defined_object_dict['layer7_connections'] = layer7_conn_dict
        return defined_object_dict
