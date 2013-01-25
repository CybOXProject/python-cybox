import common_methods
import cybox.cybox_common_types_1_0 as cybox_common
import cybox.network_connectio_object_1_0 as cybox_network_connection_object
from address_object import address_object as address_obj
from port_object import port_object as port_obj
from http_session_object import http_session_object as http_session_obj

class network_connection_object(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, network_connection_attributes):
        pass

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict):
        if defined_object.get_tls_used() is not None: defined_object_dict['tls_used'] = defined_object.get_tls_used()
        if defined_object.get_Layer3_Protocol() is not None: defined_object_dict['layer3_protocol'] = common_methods.parse_object_attribute_type(defined_object.get_Layer3_Protocol())
        if defined_object.get_Layer4_Protocol() is not None: defined_object_dict['layer4_protocol'] = common_methods.parse_object_attribute_type(defined_object.get_Layer4_Protocol())
        if defined_object.get_Layer7_Protocol() is not None: defined_object_dict['layer7_protocol'] = common_methods.parse_object_attribute_type(defined_object.get_Layer7_Protocol())
        if defined_object.get_Local_IP_Address() is not None: defined_object_dict['local_ip_address'] = address_obj.parse_into_dict(defined_object.get_Local_IP_Address())
        if defined_object.get_Local_Port() is not None: defined_object_dict['local_port'] = port_obj.parse_into_dict(defined_object.get_Local_Port())
        if defined_object.get_Remote_IP_Address() is not None: defined_object_dict['remote_ip_address'] = address_obj.parse_into_dict(defined_object.get_Remote_IP_Address())
        if defined_object.get_Remote_Port() is not None: defined_object_dict['remote_port'] = port_obj.parse_into_dict(defined_object.get_Remote_Port())
        if defined_object.get_Layer7_Connections() is not None:
            layer7_conn = defined_object.get_Layer7_Connections()
            layer7_conn_dict = {}
            if layer7_conn.get_HTTP_Session() is not None: layer7_conn_dict['http_session'] = http_session_obj.parse_into_dict(layer7_conn.get_HTTP_Session())
            defined_object_dict['layer7_connections'] = layer7_conn_dict
        return defined_object_dict