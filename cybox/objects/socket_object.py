import maec_bundle_3_0 as maecbundle
import cybox.socket_object_1_4 as cybox_socket_object

class socket_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, socket_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.id, type_='Socket')
        socketobj = cybox_socket_object.SocketObjectType()
        socketobj.set_anyAttributes_({'xsi:type' : 'SocketObj:SocketObjectType'})
        remote_address = cybox_socket_object.SocketAddressType()
        local_address = cybox_socket_object.SocketAddressType()
        
        for key, value in socket_attributes.items():
            if key == 'address_family' and self.__value_test(value):
                if value == "unspecified":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_UNSPEC'))
                elif value == "berkeley" or value == "ipv4":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_INET'))
                elif value == "ipv6":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_INET6'))
                elif value == "ipx":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_IPX'))
                elif value == "netbios":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_NETBIOS'))
                elif value == "appletalk":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_APPLETALK'))
                elif value == "irda":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_IRDA'))
                elif value == "bth":
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='AF_BTH'))
                elif "af_" in value:
                    socketobj.set_Address_Family(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=value))
            elif key == "domain" and self.__value_test(value):
                if value == "local":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_LOCAL'))
                elif value == "unix":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_UNIX'))
                elif value == "inet" or value == "ipv4" or value == "ip":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_INET'))
                elif value == "file":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_FILE'))
                elif value == "ax.25":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_AX25'))
                elif value == "ipx":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_IPX'))
                elif value == "ipv6":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_INET6'))
                elif value == "appletalk":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_APPLETALK'))
                elif value == "netrom":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_NETROM'))
                elif value == "bridge":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_BRIDGE'))
                elif value == "atmpvc":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ATMPVC'))
                elif value == "x.25":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_X25'))
                elif value == "rose":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ROSE'))
                elif value == "key":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_KEY'))
                elif value == "security":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_SECURITY'))
                elif value == "netbeui":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_NETBEUI'))
                elif value == "netlink":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_NETLINK'))
                elif value == "route":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ROUTE'))
                elif value == "decnet":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_DECNET'))
                elif value == "packet":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_PACKET'))
                elif value == "ash":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ASH'))
                elif value == "econet":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ECONET'))
                elif value == "atmsvc":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_ATMSVC'))
                elif value == "sna":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_SNA'))
                elif value == "irda":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_IRDA'))
                elif value == "pppox":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_PPPOX'))
                elif value == "wanpipe":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_WANPIPE'))
                elif value == "bluetooth":
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='PF_BLUETOOTH'))
                elif 'pf_' in value:
                    socketobj.set_Domain(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=value))
            elif key == 'options':
                options = cybox_socket_object.SocketOptionsType()
                for op_key, op_value in value.items():
                    # TODO: populate options
                    pass
                socketobj.set_Options(options)
            elif key == 'protocol' and self.__value_test(value):
                if value == 'icmp':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_ICMP'))
                elif value == 'icmpv6':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_ICMPV6'))
                elif value == 'igmp':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_IGMP'))
                elif value == 'udp':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_TCP'))
                elif value == 'tcp':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_UDP'))
                elif value == 'rm':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='IPPROTO_ICMP'))
                elif value == 'bluetooth':
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='BTHPROTO_RFCOMM'))
                elif 'proto_' in value:
                    socketobj.set_Protocol(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=value))
            elif key == 'type' and self.__value_test(value):
                if value == 'tcp':
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='SOCK_STREAM'))
                elif value == 'udp':
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='SOCK_DGRAM'))
                elif value == 'raw':
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='SOCK_RAW'))
                elif value == 'rdm':
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='SOCK_RDM'))
                elif value == 'congestion control':
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_='SOCK_SEQPACKET'))
                elif 'sock_' in value:
                    socketobj.set_Type(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=value))
            elif key == 'remote_port' and self.__value_test(value):
                if value != '0':
                    port = cybox_socket_object.port_object_1_3.PortObjectType()
                    port.set_Port_Value(maecbundle.cybox_common_types_1_0.PositiveIntegerObjectAttributeType(datatype='PositiveInteger', valueOf_=maecbundle.quote_xml(value)))
                    remote_address.set_Port(port)
            elif key == 'remote_address' and self.__value_test(value):
                ip_address = cybox_socket_object.address_object_1_2.AddressObjectType(category='ipv4-addr')
                ip_address.set_Address_Value(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
                remote_address.set_IP_Address(ip_address)
            elif key == 'local_port' and self.__value_test(value):
                if value != '0':
                    port = cybox_socket_object.port_object_1_3.PortObjectType()
                    port.set_Port_Value(maecbundle.cybox_common_types_1_0.PositiveIntegerObjectAttributeType(datatype='PositiveInteger', valueOf_=maecbundle.quote_xml(value)))
                    local_address.set_Port(port)
            elif key == 'local_address' and self.__value_test(value):
                ip_address = cybox_socket_object.address_object_1_2.AddressObjectType(category='ipv4-addr')
                ip_address.set_Address_Value(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='String', valueOf_=maecbundle.quote_xml(value)))
                local_address.set_IP_Address(ip_address)
            elif key == 'is_listening' and self.__value_test(value):
                socketobj.set_is_listening(value)
            elif key == 'is_blocking' and self.__value_test(value):
                socketobj.set_is_blocking(value)
            elif key == 'association' and self.__value_test(value):
                cybox_object.set_association_type(value)
        if remote_address.hasContent_():
            socketobj.set_Remote_Address(remote_address)
        if local_address.hasContent_():
            socketobj.set_Local_Address(local_address)
            
        if socketobj.hasContent_():
            cybox_object.set_Defined_Object(socketobj)
        
        return cybox_object