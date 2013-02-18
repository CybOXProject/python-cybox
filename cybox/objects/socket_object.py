import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.socket_object_1_4 as socket_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.port_object import Port
from cybox.objects.address_object import Address

class Socket:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, socket_dict):
        """Create the Socket Object object representation from an input dictionary"""
        socket_obj = socket_binding.socket_objectType()
        socket_obj.set_anyAttributes_({'xsi:type' : 'socket_obj:socket_objectType'})
        
        for key, value in socket_dict.items():
            if key == 'is_blocking' and utils.test_value(value):
                socket_obj.set_is_blocking(value.get('value'))
            elif key == 'is_listening' and utils.test_value(value):
                socket_obj.set_is_listening(value.get('value'))
            elif key == 'address_family' and utils.test_value(value):
                socket_obj.set_Address_Family(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'domain' and utils.test_value(value):
                socket_obj.set_Domain(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'local_address':
                socket_address_obj = socket_binding.SocketAddressType()
                for local_address_key, local_address_value in value.items():
                    if local_address_key == 'ip_address' :
                        ip_address_obj = Address.create_from_dict(local_address_value)
                        if ip_address_obj.hasContent_() : socket_address_obj.set_IP_Address(ip_address_obj)
                    elif local_address_key == 'port' :
                        port_obj = Port.create_from_dict(local_address_value)
                        if port_obj.hasContent_() : socket_address_obj.set_Port(port_obj)
                if socket_address_obj.hasContent_() : socket_obj.set_Local_Address(socket_address_obj)
            elif key == 'options':
                socket_options_obj = cls.__socket_options_object_from_dict(value)
                if socket_options_obj.hasContent_() : socket_obj.set_Options(socket_options_obj)
            elif key == 'protocol' and utils.test_value(value):
                socket_obj.set_Protocol(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'remote_address' and utils.test_value(value):
                socket_address_obj = socket_binding.SocketAddressType()
                for remote_address_key, remote_address_value in value.items():
                    if remote_address_key == 'ip_address' :
                        ip_address_obj = Address.create_from_dict(remote_address_value)
                        if ip_address_obj.hasContent_() : socket_address_obj.set_IP_Address(ip_address_obj)
                    elif remote_address_key == 'port' :
                        port_obj = Port.create_from_dict(remote_address_value)
                        if port_obj.hasContent_() : socket_address_obj.set_Port(port_obj)
                if socket_address_obj.hasContent_() : socket_obj.set_Remote_Address(socket_address_obj)
            elif key == 'type' and utils.test_value(value):
                socket_obj.set_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))

        return socket_obj

    @classmethod
    def dict_from_object(cls, socket_obj):
        """Parse and return a dictionary for a Socket Object object"""
        socket_dict = {}
        if socket_obj.get_is_blocking() is not None: socket_dict['is_blocking'] = {'value' : socket_obj.get_is_blocking()}
        if socket_obj.get_is_listening() is not None: socket_dict['is_listening'] = {'value' : socket_obj.get_is_listening()}
        if socket_obj.get_Address_Family() is not None: socket_dict['address_family'] = Base_Object_Attribute.dict_from_object(socket_obj.get_Address_Family())
        if socket_obj.get_Domain() is not None: socket_dict['domain'] = Base_Object_Attribute.dict_from_object(socket_obj.get_Domain())
        if socket_obj.get_Local_Address() is not None:
            local_address_dict = {}
            if socket_obj.get_Local_Address().get_IP_Address() is not None:
                local_address_dict['ip_address'] = Address.dict_from_object(socket_obj.get_Local_Address().get_IP_Address())
            if socket_obj.get_Local_Address().get_Port() is not None:
                local_address_dict['port'] = Port.dict_from_object(socket_obj.get_Local_Address().get_Port())
        if socket_obj.get_Options() is not None: socket_dict['options'] = cls.__socket_options_dict_from_object(socket_obj.get_Options())
        if socket_obj.get_Protocol() is not None: Base_Object_Attribute.dict_from_object(socket_obj.get_Protocol())
        if socket_obj.get_Remote_Address() is not None:
            remote_address_dict = {}
            if socket_obj.get_Remote_Address().get_IP_Address() is not None:
                remote_address_dict['ip_address'] = Address.dict_from_object(socket_obj.get_Local_Address().get_IP_Address())
            if socket_obj.get_Remote_Address().get_Port() is not None:
                remote_address_dict['port'] = Port.dict_from_object(socket_obj.get_Local_Address().get_Port())
        if socket_obj.get_Type() is not None: Base_Object_Attribute.dict_from_object(socket_obj.get_Type())
        return socket_dict 

    @classmethod
    def __socket_options_object_from_dict(cls, socket_options_dict):
        socket_options_obj = socket_binding.SocketOptionsType()
        for key, value in socket_options_dict:
            if key == 'ip_multicast_if' and utils.test_value(value) :
                socket_options_obj.set_IP_MULTICAST_IF(value.get('value'))
            elif key == 'ip_multicast_if2' and utils.test_value(value) :
                socket_options_obj.set_IP_MULTICAST_IF2(value.get('value'))
            elif key == 'ip_multicast_loop' and utils.test_value(value) :
                socket_options_obj.set_IP_MULTICAST_LOOP(value.get('value'))
            elif key == 'ip_multicast_tos' and utils.test_value(value) :
                socket_options_obj.set_IP_MULTICAST_TOS(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'so_broadcast' and utils.test_value(value) :
                socket_options_obj.set_SO_BROADCAST(value.get('value'))
            elif key == 'so_conditional_accept' and utils.test_value(value) :
                socket_options_obj.set_SO_CONDITIONAL_ACCEPT(value.get('value'))
            elif key == 'so_keepalive' and utils.test_value(value) :
                socket_options_obj.set_SO_KEEPALIVE(value.get('value'))
            elif key == 'so_dontroute' and utils.test_value(value) :
                socket_options_obj.set_SO_DONTROUTE(value.get('value'))
            elif key == 'so_linger' and utils.test_value(value) :
                socket_options_obj.set_SO_LINGER(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_dontlinger' and utils.test_value(value) :
                socket_options_obj.set_SO_DONTLINGER(value.get('value'))
            elif key == 'so_oobinline' and utils.test_value(value) :
                socket_options_obj.set_SO_OOBINLINE(value.get('value'))
            elif key == 'so_rcvbuf' and utils.test_value(value) :
                socket_options_obj.set_SO_RCVBUF(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_group_priority' and utils.test_value(value) :
                socket_options_obj.set_SO_GROUP_PRIORITY(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_reuseaddr' and utils.test_value(value) :
                socket_options_obj.set_SO_REUSEADDR(value.get('value'))
            elif key == 'so_debug' and utils.test_value(value) :
                socket_options_obj.set_SO_DEBUG(value.get('value'))
            elif key == 'so_rcvtimeo' and utils.test_value(value) :
                socket_options_obj.set_SO_RCVTIMEO(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_sndbuf' and utils.test_value(value) :
                socket_options_obj.set_SO_SNDBUF(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_sndtimeo' and utils.test_value(value) :
                socket_options_obj.set_SO_SNDTIMEO(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_update_accept_context' and utils.test_value(value) :
                socket_options_obj.set_SO_UPDATE_ACCEPT_CONTEXT(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'so_timeout' and utils.test_value(value) :
                socket_options_obj.set_SO_TIMEOUT(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedIntegerObjectAttributeType(datatype='UnsignedInteger'),value))
            elif key == 'tcp_nodelay' and utils.test_value(value) :
                socket_options_obj.set_TCP_NODELAY(value.get('value'))
            return socket_options_obj

    @classmethod
    def __socket_options_dict_from_object(cls, socket_options_obj):
        socket_options_dict = {}
        if socket_options_obj.get_IP_MULTICAST_IF() is not None: socket_options_dict['ip_multicast_if']  = {'value' : socket_options_obj.get_IP_MULTICAST_IF()}
        if socket_options_obj.get_IP_MULTICAST_IF2() is not None: socket_options_dict['ip_multicast_if2']  = {'value' : socket_options_obj.get_IP_MULTICAST_IF2()}
        if socket_options_obj.get_IP_MULTICAST_LOOP() is not None: socket_options_dict['ip_multicast_loop']  = {'value' : socket_options_obj.get_IP_MULTICAST_LOOP()}
        if socket_options_obj.get_IP_TOS() is not None: socket_options_dict['ip_tos']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_IP_TOS())
        if socket_options_obj.get_SO_BROADCAST() is not None: socket_options_dict['so_broadcast']  = {'value' : socket_options_obj.get_SO_BROADCAST()}
        if socket_options_obj.get_SO_CONDITIONAL_ACCEPT() is not None: socket_options_dict['so_conditional_accept']  = {'value' : socket_options_obj.get_SO_CONDITIONAL_ACCEPT()}
        if socket_options_obj.get_SO_KEEPALIVE() is not None: socket_options_dict['so_keepalive']  = {'value' : socket_options_obj.get_SO_KEEPALIVE()}
        if socket_options_obj.get_SO_DONTROUTE() is not None: socket_options_dict['so_dontroute']  = {'value' : socket_options_obj.get_SO_DONTROUTE()}
        if socket_options_obj.get_SO_LINGER() is not None: socket_options_dict['so_linger']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_LINGER())
        if socket_options_obj.get_SO_DONTLINGER() is not None: socket_options_dict['so_dontlinger']  = {'value' : socket_options_obj.get_SO_DONTLINGER()}
        if socket_options_obj.get_SO_OOBINLINE() is not None: socket_options_dict['so_oobinline']  = {'value' : socket_options_obj.get_SO_OOBINLINE()}
        if socket_options_obj.get_SO_RCVBUF() is not None: socket_options_dict['so_rcvbuf']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_RCVBUF())
        if socket_options_obj.get_SO_GROUP_PRIORITY() is not None: socket_options_dict['so_group_priority']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_GROUP_PRIORITY())
        if socket_options_obj.get_SO_REUSEADDR() is not None: socket_options_dict['so_reuseaddr']  = {'value' : socket_options_obj.get_SO_REUSEADDR()}
        if socket_options_obj.get_SO_DEBUG() is not None: socket_options_dict['so_debug']  = {'value' : socket_options_obj.get_SO_DEBUG()}
        if socket_options_obj.get_SO_RCVTIMEO() is not None: socket_options_dict['so_rcvtimeo']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_RCVTIMEO())
        if socket_options_obj.get_SO_SNDBUF() is not None: socket_options_dict['so_sndbuf']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_SNDBUF())
        if socket_options_obj.get_SO_SNDTIMEO() is not None: socket_options_dict['so_sndtimeo']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_SNDTIMEO())
        if socket_options_obj.get_SO_UPDATE_ACCEPT_CONTEXT() is not None: socket_options_dict['so_update_accept_context']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_UPDATE_ACCEPT_CONTEXT())
        if socket_options_obj.get_SO_TIMEOUT() is not None: socket_options_dict['so_timeout']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_SO_TIMEOUT())
        if socket_options_obj.get_TCP_NODELAY() is not None: socket_options_dict['tcp_nodelay']  = Base_Object_Attribute.dict_from_object(socket_options_obj.get_TCP_NODELAY())
        return socket_options_dict