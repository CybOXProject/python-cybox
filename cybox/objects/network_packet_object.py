# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.network_packet_object_1_1 as network_packet_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port

class Network_Packet(object):
    def __init__(self):
        pass

    @classmethod
    def object_from_dict(cls, network_packet_attributes):
        """Create the Network Packet Object object representation from an input dictionary"""
        pass

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for a Network Packet Object object"""
        defined_object_dict = {}
        if defined_object.get_Link_Layer() is not None:
            defined_object_dict['link_layer'] = cls.__parse_link_layer(defined_object.get_Link_Layer())
        if defined_object.get_Internet_Layer() is not None:
            defined_object_dict['internet_layer'] = cls.__parse_internet_layer(defined_object.get_Internet_Layer())
        if defined_object.get_Transport_Layer() is not None:
            defined_object_dict['transport_layer'] = cls.__parse_transport_layer(defined_object.get_Transport_Layer())
        return defined_object_dict

    @classmethod
    def __parse_link_layer(cls, link_layer):
        link_layer_dict = {}
        if link_layer.get_Physical_Interface() is not None:
            physical_interface = link_layer.get_Physical_Interface()
            physical_interface_dict = {}
            if physical_interface.get_Ethernet() is not None:
                ethernet = physical_interface.get_Ethernet()
                ethernet_dict = {}
                if ethernet.get_Ethernet_Header() is not None:
                    ethernet_header = ethernet.get_Ethernet_Header()
                    ethernet_header_dict = {}
                    if ethernet_header.get_Destination_MAC_Addr() is not None: ethernet_header_dict['destination_mac_addr'] = Address.dict_from_object(ethernet_header.get_Destination_MAC_Addr())
                    if ethernet_header.get_Source_MAC_Addr() is not None: ethernet_header_dict['source_mac_addr'] = Address.dict_from_object(ethernet_header.get_Source_MAC_Addr())
                    if ethernet_header.get_Type_Or_Length() is not None:
                        type_or_length = ethernet_header.get_Type_Or_Length()
                        type_or_length_dict = {}
                        if type_or_length.get_Length() is not None: type_or_length_dict['length'] = Base_Object_Attribute.dict_from_object(type_or_length.get_Length())
                        if type_or_length.get_Internet_Layer_Type() is not None: type_or_length_dict['internet_layer_type'] = Base_Object_Attribute.dict_from_object(type_or_length.get_Internet_Layer_Type())
                        ethernet_header_dict['type_or_length'] = type_or_length_dict
                    if ethernet_header.get_Checksum() is not None: ethernet_header['checksum'] = Base_Object_Attribute.dict_from_object(ethernet_header.get_Checksum())
                    ethernet_dict['ethernet_header'] = ethernet_header_dict
                physical_interface_dict['ethernet'] = ethernet_dict
            link_layer_dict['physical_interface'] = physical_interface_dict
        if link_layer.get_Logical_Protocols() is not None:
            logical_protocols = link_layer.get_Logical_Protocols()
            logical_protocols_dict = {}
            if logical_protocols.get_ARP_RARP() is not None:
                arp_rarp = logical_protocols.get_ARP_RARP()
                arp_rarp_dict = {}
                if arp_rarp.get_Hardware_Addr_Type() is not None: arp_rarp_dict['hardware_addr_type'] = Base_Object_Attribute.dict_from_object(arp_rarp.get_Hardware_Addr_Type())
                if arp_rarp.get_Proto_Addr_Type() is not None: arp_rarp_dict['proto_addr_type'] = Base_Object_Attribute.dict_from_object(arp_rarp.get_Proto_Addr_Type())
                if arp_rarp.get_Hardware_Addr_Size() is not None: arp_rarp_dict['hardware_addr_size'] = Base_Object_Attribute.dict_from_object(arp_rarp.get_Hardware_Addr_Size())
                if arp_rarp.get_Protol_Addr_Size() is not None: arp_rarp_dict['protol_addr_size'] = Base_Object_Attribute.dict_from_object(arp_rarp.get_Protol_Addr_Size())
                if arp_rarp.get_Op_Type() is not None: arp_rarp_dict['op_type'] = Base_Object_Attribute.dict_from_object(arp_rarp.get_Op_Type())
                if arp_rarp.get_Sender_Hardware_Addr() is not None: arp_rarp_dict['sender_hardware_addr'] = Address.dict_from_object(arp_rarp.get_Sender_Hardware_Addr())
                if arp_rarp.get_Sender_Protocol_Addr() is not None: arp_rarp_dict['sender_protocol_addr'] = Address.dict_from_object(arp_rarp.get_Sender_Protocol_Addr())
                if arp_rarp.get_Recip_Hardware_Addr() is not None: arp_rarp_dict['recip_hardware_addr'] = Address.dict_from_object(arp_rarp.get_Recip_Hardware_Addr())
                if arp_rarp.get_Recip_Protocol_Addr() is not None: arp_rarp_dict['recip_protocol_addr'] = Address.dict_from_object(arp_rarp.get_Recip_Protocol_Addr())
                logical_protocols_dict['arp_rarp'] = arp_rarp_dict
            if logical_protocols.get_NDP() is not None:
                ndp = logical_protocols.get_NDP()
                ndp_dict = {}
                if ndp.get_ICMPv6_Header() is not None:
                    icmp_header = ndp.get_ICMPv6_Header()
                    icmp_header_dict = {}
                    if icmp_header.get_Type() is not None: icmp_header_dict['type'] = Base_Object_Attribute.dict_from_object(icmp_header.get_Type())
                    if icmp_header.get_Code() is not None: icmp_header_dict['code'] = Base_Object_Attribute.dict_from_object(icmp_header.get_Code())
                    if icmp_header.get_Checksum() is not None: icmp_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(icmp_header.get_Checksum())
                    ndp_dict['icmpv6_header'] = icmp_header_dict
                if ndp.get_Router_Solicitation() is not None:
                    router_solicitation = ndp.get_Router_Solicitation()
                    router_solicitation_dict = {}
                    if router_solicitation.get_Options() is not None:
                        options = []
                        for option in router_solicitation.get_Options():
                            option_dict = {}
                            if option.get_Src_Link_Addr() is not None:
                                src_link_addr = option.get_Src_Link_Addr()
                                src_link_addr_dict = {}
                                if src_link_addr.get_Length() is not None: src_link_addr_dict['length'] = Base_Object_Attribute.dict_from_object(src_link_addr.get_Length())
                                if src_link_addr.get_Link_Layer_MAC_Addr() is not None: src_link_addr_dict['link_layer_mac_addr'] = Address.dict_from_object(src_link_addr.get_Link_Layer_MAC_Addr())
                                option_dict['src_link_addr'] = src_link_addr_dict
                            options.append(option_dict)
                        router_solicitation_dict['options'] = options
                    ndp_dict['router_solicitation'] = router_solicitation_dict
                if ndp.get_Router_Advertisement() is not None:
                    router_advertisment = ndp.get_Router_Advertisement()
                    router_advertisement_dict = {}
                    if router_advertisement.get_managed_address_config_flag() is not None: router_advertisement_dict['managed_address_config_flag'] = router_advertisement.get_managed_address_config_flag()
                    if router_advertisement.get_other_config_flag() is not None: router_advertisement_dict['other_config_flag'] = router_advertisement.get_other_config_flag()
                    if router_advertisement.get_Cur_Hop_Limit() is not None: router_advertisement_dict['cur_hop_limit'] = Base_Object_Attribute.dict_from_object(router_advertisement.get_Cur_Hop_Limit())
                    if router_advertisement.get_Router_Lifetime() is not None: router_advertisement_dict['router_lifetime'] = Base_Object_Attribute.dict_from_object(router_advertisement.get_Router_Lifetime())
                    if router_advertisement.get_Reachable_Time() is not None: router_advertisement_dict['reachable_time'] = Base_Object_Attribute.dict_from_object(router_advertisement.get_Reachable_Time())
                    if router_advertisement.get_Retrans_Timer is not None: router_advertisement_dict['retrans_timer'] = Base_Object_Attribute.dict_from_object(router_advertisement.get_Retrans_Timer())
                    if router_advertisement.get_Options() is not None:
                        options = router_advertisement.get_Options() 
                        options_dict = {} 
                        if options.get_Src_Link_Addr() is not None:
                            src_link_addr = options.get_Src_Link_Addr()
                            src_link_addr_dict = {}
                            if src_link_addr.get_Length() is not None: src_link_addr_dict['length'] = Base_Object_Attribute.dict_from_object(src_link_addr.get_Length())
                            if src_link_addr.get_Link_Layer_MAC_Addr() is not None: src_link_addr_dict['link_layer_mac_addr'] = Address.dict_from_object(src_link_addr.get_Link_Layer_MAC_Addr())
                            options_dict['src_link_addr'] = src_link_addr_dict
                        if options.get_MTU() is not None:
                            mtu = options.get_MTU()
                            mtu_dict = {}
                            if mtu.get_Length() is not None: mtu_dict['length'] = Base_Object_Attribute.dict_from_object(mtu.get_Length())
                            if mtu.get_MTU() is not None: mtu_dict['mtu'] = Base_Object_Attribute.dict_from_object(mtu.get_MTU())
                            options_dict['mtu'] = mtu_dict
                        if options.get_Prefix_Info() is not None:
                            prefix_info = options.get_Prefix_Info()
                            prefix_info_dict = {}
                            if prefix_info.get_link_flag() is not None: prefix_info_dict['link_flag'] = prefix_info.get_link_flag()
                            if prefix_info.get_addr_config_flag() is not None: prefix_info_dict['addr_config_flag'] = prefix_info.get_addr_config_flag()
                            if prefix_info.get_Length() is not None: prefix_info_dict['length'] = Base_Object_Attribute.dict_from_object(prefix_info.get_Length())
                            if prefix_info.get_Prefix_Length() is not None: prefix_info_dict['prefix_length'] = Base_Object_Attribute.dict_from_object(prefix_info.get_Prefix_Length())
                            if prefix_info.get_Valid_Lifetime() is not None: prefix_info_dict['valid_lifetime'] = Base_Object_Attribute.dict_from_object(prefix_info.get_Valid_Lifetime())
                            if prefix_info.get_Preferred_Lifetime() is not None: prefix_info_dict['preferred_lifetime'] = Base_Object_Attribute.dict_from_object(prefix_info.get_Preferred_Lifetime())
                            if prefix_info.get_Prefix() is not None: 
                                prefix = prefix_info.get_Prefix()
                                prefix_dict = {}
                                if prefix.get_IPv6_Addr() is not None: prefix_dict['ipv6_addr'] = Address.dict_from_object(prefix.get_IPv6_Addr())
                                if prefix.get_IP_Addr_Prefix() is not None: prefix_dict['ip_addr_prefix'] = Address.dict_from_object(prefix.get_IP_Addr_Prefix())
                                prefix_info_dict['prefix'] = prefix_dict
                            options_dict['prefix_info'] = prefix_info_dict
                        router_advertisement_dict['options'] = options_dict
                    ndp_dict['router_advertisement'] = router_advertisement_dict
                if ndp.get_Neighbor_Solicitation() is not None:
                    neighbor_solicitation = ndp.get_Neighbor_Solicitation()                            
                    neighbor_solicitation_dict = {}
                    if neighbor_solicitation.get_Target_IPv6_Addr() is not None: neighbor_solicitation_dict['target_ipv6_addr'] = Address.dict_from_object(neighbor_solicitation.get_Target_IPv6_Addr())
                    if neighbor_solicitation.get_Options() is not None:
                        options = neighbor_solicitation.get_Options()
                        options_dict = {}
                        if options.get_Src_Link_Addr() is not None:
                            src_link_addr = options.get_Src_Link_Addr()
                            src_link_addr_dict = {}
                            if src_link_addr.get_Length() is not None: src_link_addr_dict['length'] = Base_Object_Attribute.dict_from_object(src_link_addr.get_Length())
                            if src_link_addr.get_Link_Layer_MAC_Addr() is not None: src_link_addr_dict['link_layer_mac_addr'] = Address.dict_from_object(src_link_addr.get_Link_Layer_MAC_Addr())
                            options_dict['src_link_addr'] = src_link_addr_dict
                        neighbor_solicitation_dict['options'] = options_dict
                    ndp_dict['neighbor_solicitation'] = neighbor_solicitation_dict
                if ndp.get_Neighbor_Advertisement() is not None:
                    neighbor_advertisement = ndp.get_Neighbor_Advertisement()
                    neighbor_advertisement_dict = {}
                    if neighbor_advertisement.get_router_flag() is not None: neighbor_advertisement_dict['router_flag'] = neighbor_advertisement.get_router_flag()
                    if neighbor_advertisement.get_solicited_flag() is not None: neighbor_advertisement_dict['solicited_flag'] = neighbor_advertisement.get_solicited_flag()
                    if neighbor_advertisement.get_override_flag() is not None: neighbor_advertisement_dict['override_flag'] = neighbor_advertisement.get_override_flag()                        
                    if neighbor_advertisement.get_Target_IPv6_Addr() is not None: neighbor_advertisement_dict['target_ipv6_addr'] = Address.dict_from_object(neighbor_advertisement.get_Target_IPv6_Addr())
                    if neighbor_advertisement.get_Options() is not None:
                        options = neighbor_advertisement.get_Options()
                        options_dict = {}
                        if options.get_Target_Link_Addr() is not None:
                            target_link_addr = options.Target_Link_Addr()
                            target_link_addr_dict = {}
                            if target_link_addr.get_Length() is not None: target_link_addr_dict['length'] = Base_Object_Attribute.dict_from_object(target_link_addr.get_Length())
                            if target_link_addr.get_Link_Layer_MAC_Addr() is not None: target_link_addr_dict['link_layer_mac_addr'] = Address.dict_from_object(target_link_addr.get_Link_Layer_MAC_Addr())
                            options_dict['target_link_addr'] = target_link_addr_dict
                        neighbor_advertisement_dict['options'] = options_dict
                    ndp_dict['neighbor_advertisement'] = neighbor_advertisement_dict
                if ndp.get_Redirect() is not None:
                    redirect = ndp.get_Redirect()
                    redirect_dict = {}
                    if redirect.get_Target_IPv6_Addr() is not None: redirect_dict['target_ipv6_addr'] = Address.dict_from_object(redirect.get_Target_IPv6_Addr())
                    if redirect.get_Dest_IPv6_Addr() is not None: redirect_dict['dest_ipv6_addr'] = Address.dict_from_object(redirect.get_Dest_IPv6_Addr())
                    if redirect.get_Options() is not None:
                        options = redirect.get_Options()
                        options_dict = {}
                        if options.get_Target_Link_Addr() is not None:
                            target_link_addr = options.Target_Link_Addr()
                            target_link_addr_dict = {}
                            if target_link_addr.get_Length() is not None: target_link_addr_dict['length'] = Base_Object_Attribute.dict_from_object(target_link_addr.get_Length())
                            if target_link_addr.get_Link_Layer_MAC_Addr() is not None: target_link_addr_dict['link_layer_mac_addr'] = Address.dict_from_object(target_link_addr.get_Link_Layer_MAC_Addr())
                            options_dict['target_link_addr'] = target_link_addr_dict
                        if options.get_Redirected_Header() is not None:
                            redirected_header = options.get_Redirected_Header()
                            redirected_header_dict = {}
                            if redirected_header.get_Length() is not None: redirected_header_dict['length'] = Base_Object_Attribute.dict_from_object(redirected_header.get_Length())
                            if redirected_header.get_IPHeader_And_Data() is not None: redirected_header_dict['ipheader_and_data'] = Base_Object_Attribute.dict_from_object(redirected_header.get_IPHeader_And_Data())
                            options_dict['redirected_header'] = redirected_header_dict
                        redirect_dict['options'] = options_dict
                    ndp_dict['redirect'] = redirect_dict
                logical_protocols_dict['ndp'] = ndp_dict
            link_layer_dict['logical_protocols'] = logical_protocols_dict   
        return link_layer_dict

    @classmethod
    def __parse_internet_layer(cls, internet_layer):
        internet_layer_dict = {}
        if internet_layer.get_IPv4() is not None:
            ipv4 = internet_layer.get_IPv4()
            ipv4_dict = {}
            if ipv4.get_IPv4_Header() is not None:
                ipv4_header = ipv4.get_IPv4_Header()
                ipv4_header_dict = {}
                if ipv4_header.get_IP_Version() is not None: ipv4_header_dict['ip_version'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_IP_Version())
                if ipv4_header.get_Header_Length() is not None: ipv4_header_dict['header_length'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Header_Length())
                if ipv4_header.get_DSCP() is not None: ipv4_header_dict['dscp'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_DSCP())
                if ipv4_header.get_ECN() is not None: ipv4_header_dict['ecn'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_ECN())
                if ipv4_header.get_Total_Length() is not None: ipv4_header_dict['total_length'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Total_Length())
                if ipv4_header.get_Identification() is not None: ipv4_header_dict['identification'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Identification())
                if ipv4_header.get_Flags() is not None:
                    flags = ipv4_header.get_Flags()
                    flags_dict = {}
                    if flags.get_Reserved() is not None: flags_dict['reserved'] = Base_Object_Attribute.dict_from_object(flags.get_Reserved())
                    if flags.get_Do_Not_Fragment() is not None: flags_dict['do_not_fragment'] = Base_Object_Attribute.dict_from_object(flags.get_Do_Not_Fragment())
                    if flags.get_More_Fragments() is not None: flags_dict['more_fragments'] = Base_Object_Attribute.dict_from_object(flags.get_More_Fragments())
                    ipv4_header_dict['flags'] = flags_dict
                if ipv4_header.get_Fragment_Offset() is not None: ipv4_header_dict['fragment_offset'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Fragment_Offset())
                if ipv4_header.get_TTL() is not None: ipv4_header_dict['ttl'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_TTL())
                if ipv4_header.get_Protocol() is not None: ipv4_header_dict['protocol'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Protocol())
                if ipv4_header.get_Checksum() is not None: ipv4_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(ipv4_header.get_Checksum())
                if ipv4_header.get_Src_IPv4_Addr() is not None: ipv4_header_dict['src_ipv4_addr'] = Address.dict_from_object(ipv4_header.get_Src_IPv4_Addr())
                if ipv4_header.get_Dest_IPv4_Addr() is not None: ipv4_header_dict['dest_ipv4_addr'] = Address.dict_from_object(ipv4_header.get_Dest_IPv4_Addr())
                if ipv4_header.get_Option() is not None:
                    options = []
                    for option in ipv4_header.get_Option():
                        option_dict = {}
                        if option.get_Copy_Flag() is not None: option_dict['copy_flag'] = Base_Object_Attribute.dict_from_object(option.get_Copy_Flag())
                        if option.get_Class() is not None: option_dict['class'] = Base_Object_Attribute.dict_from_object(option.get_Class())
                        if option.get_Option() is not None: option_dict['option'] = Base_Object_Attribute.dict_from_object(option.get_Option())
                        options.append(option_dict)
                    ipv4_header_dict['options'] = options
                ipv4_dict['ipv4_header'] = ipv4_header_dict
            if ipv4.get_Data() is not None: ipv4_dict['data'] = Base_Object_Attribute.dict_from_object(ipv4.get_Data())
            internet_layer_dict['ipv4'] = ipv4_dict
        if internet_layer.get_ICMPv4() is not None:
            icmpv4 = internet_layer.get_ICMPv4()
            icmpv4_dict = {}
            if icmpv4.get_ICMPV4_Header() is not None:
                icmpv4_header = icmpv4.get_ICMPV4_Header()
                icmpv4_header_dict = {} 
                if icmpv4_header.get_Type() is not None: icmpv4_header_dict['type'] = Base_Object_Attribute.dict_from_object(icmpv4_header.get_Type())
                if icmpv4_header.get_Code() is not None: icmpv4_header_dict['code'] = Base_Object_Attribute.dict_from_object(icmpv4_header.get_Code())
                if icmpv4_header.get_Checksum() is not None: icmpv4_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(icmpv4_header.get_Checksum())
                icmpv4_dict['icmpv4_header'] = icmpv4_header_dict
            if icmpv4.get_Error_Msg() is not None:
                error_msg = icmpv4.get_Error_Msg()
                error_msg_dict = {}
                if error_msg.get_Destination_Unreachable() is not None:
                    dest_unreachable = error_msg.get_Destination_Unreachable()
                    dest_unreachable_dict = {}
                    if dest_unreachable.get_Destination_Network_Unreachable() is not None: dest_unreachable_dict['destination_network_unreachable'] =  dest_unreachable.get_Destination_Network_Unreachable()
                    if dest_unreachable.get_Destination_Host_Unreachable() is not None: dest_unreachable_dict['destination_host_unreachable'] =  dest_unreachable.get_Destination_Host_Unreachable()
                    if dest_unreachable.get_Destination_Protocol_Unreachable() is not None: dest_unreachable_dict['destination_protocol_unreachable'] =  dest_unreachable.get_Destination_Protocol_Unreachable()
                    if dest_unreachable.get_Destination_Port_Unreachable() is not None: dest_unreachable_dict['destination_port_unreachable'] =  dest_unreachable.get_Destination_Port_Unreachable()
                    if dest_unreachable.get_Fragmentation_Required() is not None:
                        frag_required = dest_unreachable.get_Fragmentation_Required()
                        frag_required_dict = {}
                        if frag_required.get_Fragmentation_Required() is not None: frag_required_dict['fragmentation_required'] = frag_required.get_Fragmentation_Required()
                        if frag_required.get_Next_Hop_MTU() is not None: frag_required_dict['next_hop_mtu'] = Base_Object_Attribute.dict_from_object(frag_required.get_Next_Hop_MTU())
                        dest_unreachable_dict['fragmentation_required'] = frag_required_dict
                    if dest_unreachable.get_Source_Route_Failed() is not None: dest_unreachable_dict['source_route_failed'] =  dest_unreachable.get_Source_Route_Failed()
                    if dest_unreachable.get_Destination_Network_Unknown() is not None: dest_unreachable_dict['destination_network_unknown'] =  dest_unreachable.get_Destination_Network_Unknown()
                    if dest_unreachable.get_Destination_Host_Unknown() is not None: dest_unreachable_dict['destination_host_unknown'] =  dest_unreachable.get_Destination_Host_Unknown()
                    if dest_unreachable.get_Source_Host_Isolated() is not None: dest_unreachable_dict['source_host_isolated'] =  dest_unreachable.get_Source_Host_Isolated()
                    if dest_unreachable.get_Network_Administratively_Prohibited() is not None: dest_unreachable_dict['network_administratively_prohibited'] =  dest_unreachable.get_Network_Administratively_Prohibited()
                    if dest_unreachable.get_Host_Administratively_Prohibited() is not None: dest_unreachable_dict['host_administratively_prohibited'] =  dest_unreachable.get_Host_Administratively_Prohibited()
                    if dest_unreachable.get_Network_Unreachable_For_TOS() is not None: dest_unreachable_dict['network_unreachable_for_tos'] =  dest_unreachable.get_Network_Unreachable_For_TOS()
                    if dest_unreachable.get_Host_Unreachable_For_TOS() is not None: dest_unreachable_dict['host_unreachable_for_tos'] =  dest_unreachable.get_Host_Unreachable_For_TOS()
                    if dest_unreachable.get_Communication_Adminstratively_Prohibited() is not None: dest_unreachable_dict['communication_administratively_prohibited'] =  dest_unreachable.get_Communication_Adminstratively_Prohibited()
                    if dest_unreachable.get_Host_Precedence_Violation() is not None: dest_unreachable_dict['host_precedence_violation'] =  dest_unreachable.get_Host_Precedence_Violation()
                    if dest_unreachable.get_Precedence_Cutoff_In_Effect() is not None: dest_unreachable_dict['precedence_cutoff_in_effect'] =  dest_unreachable.get_Precedence_Cutoff_In_Effect()
                    error_msg_dict['destination_unreachable'] = dest_unreachable_dict
                if error_msg.get_Source_Quench() is not None:
                    source_quench = error_msg.get_Source_Quench()
                    source_quench_dict = {}
                    if source_quench.get_Source_Quench() is not None: source_quench_dict['source_quench'] = source_quench.get_Source_Quench()
                    error_msg_dict['source_quench'] = source_quench_dict
                if error_msg.get_Redirect_Message() is not None:
                    redirect_message = error_msg.get_Redirect_Message()
                    redirect_message_dict = {}
                    if redirect_message.get_Network_Redirect() is not None: redirect_message_dict['network_redirect'] = redirect_message.get_Network_Redirect()
                    if redirect_message.get_Host_Redirect() is not None: redirect_message_dict['host_redirect'] = redirect_message.get_Host_Redirect()
                    if redirect_message.get_ToS_Network_Redirect() is not None: redirect_message_dict['tos_network_redirect'] = redirect_message.get_ToS_Network_Redirect()
                    if redirect_message.get_ToS_Host_Redirect() is not None: redirect_message_dict['tos_host_redirect'] = redirect_message.get_ToS_Host_Redirect()
                    if redirect_message.get_IP_Address() is not None: redirect_message_dict['ip_address'] = Address.dict_from_object(redirect_message.get_IP_Address())
                    error_msg_dict['redirect_message'] = redirect_message_dict
                if error_msg.get_Time_Exceeded() is not None:
                    time_exceeded = error_msg.get_Time_Exceeded()
                    time_exceeded_dict = {}
                    if time_exceeded.get_TTL_Exceeded_In_Transit() is not None: time_exceeded_dict['ttl_exceeded_in_transit'] = time_exceeded.get_TTL_Exceeded_In_Transit()
                    if time_exceeded.get_Frag_Reassembly_Time_Exceeded() is not None: time_exceeded_dict['frag_reassembly_time_exceeded'] = time_exceeded.get_Frag_Reassembly_Time_Exceeded()
                    error_msg_dict['time_exceeded'] = time_exceeded_dict
                icmpv4_dict['error_msg'] = error_msg_dict
            if icmpv4.get_Info_Msg() is not None:
                info_msg = icmpv4.get_Info_Msg()
                info_msg_dict = {}
                if info_msg.get_Echo_Reply() is not None:
                    echo_reply = info_msg.get_Echo_Reply()
                    echo_reply_dict = {}
                    if echo_reply.get_Echo_Reply() is not None: echo_reply_dict['echo_reply'] = echo_reply.get_Echo_Reply()
                    if echo_reply.get_Data() is not None: echo_reply_dict['data'] = Base_Object_Attribute.dict_from_object(echo_reply.get_Data())
                    info_msg_dict['echo_reply'] = echo_reply_dict
                if info_msg.get_Echo_Request() is not None:
                    echo_request = info_msg.get_Echo_Request()
                    echo_request_dict = {}
                    if echo_request.get_Echo_Request() is not None: echo_request_dict['echo_request'] = echo_request.get_Echo_Request()
                    if echo_request.get_Data() is not None: echo_request_dict['data'] = Base_Object_Attribute.dict_from_object(echo_request.get_Data())
                    info_msg_dict['echo_request'] = echo_request_dict
                if info_msg.get_Timestamp_Request() is not None:
                    timestamp_request = info_msg.get_Timestamp_Request()
                    timestamp_request_dict = {}
                    if timestamp_request.get_Timestamp() is not None: timestamp_request_dict['timestamp'] = timestamp_request.get_Timestamp()
                    if timestamp_request.get_Originate_Timestamp() is not None: timestamp_request_dict['originate_timestamp'] = Base_Object_Attribute.dict_from_object(timestamp_request.get_Originate_Timestamp())
                    info_msg_dict['timestamp_request'] = timestamp_request_dict
                if info_msg.get_Timestamp_Reply() is not None:
                    timestamp_reply = info_msg.get_Timestamp_Reply()
                    timestamp_reply_dict = {}
                    if timestamp_reply.get_Timestamp_Reply() is not None: timestamp_reply_dict['timestamp'] = timestamp_reply.get_Timestamp()
                    if timestamp_reply.get_Originate_Timestamp() is not None: timestamp_reply_dict['originate_timestamp'] = Base_Object_Attribute.dict_from_object(timestamp_reply.get_Originate_Timestamp())
                    if timestamp_reply.get_Receive_Timestamp() is not None: timestamp_reply_dict['receive_timestamp'] = Base_Object_Attribute.dict_from_object(timestamp_reply.get_Receive_Timestamp())
                    if timestamp_reply.get_Transmit_Timestamp() is not None: timestamp_reply_dict['transmit_timestamp'] = Base_Object_Attribute.dict_from_object(timestamp_reply.get_Transmit_Timestamp())
                    info_msg_dict['timestamp_reply'] = timestamp_reply_dict
                if info_msg.get_Address_Mask_Request() is not None:
                    address_mask_request = info_msg.get_Address_Mask_Request()
                    address_mask_request_dict = {}
                    if address_mask_request.get_Address_Mask_Request() is not None: address_mask_request_dict['address_mask_request'] = address_mask_request.get_Address_Mask_Request()
                    if address_mask_request.get_Address_Mask() is not None: address_mask_request_dict['address_mask'] = Address.dict_from_object(address_mask_request.get_Address_Mask())
                    info_msg_dict['address_mask_request'] = address_mask_request_dict
                if info_msg.get_Address_Mask_Reply() is not None:
                    address_mask_reply = info_msg.get_Address_Mask_Reply()
                    address_mask_reply_dict = {}
                    if address_mask_reply.get_Address_Mask_Reply() is not None: address_mask_reply_dict['address_mask_reply'] = address_mask_reply.get_Address_Mask_Reply()
                    if address_mask_reply.get_Address_Mask() is not None: address_mask_reply_dict['address_mask'] = Address.dict_from_object(address_mask_reply.get_Address_Mask())
                    info_msg_dict['address_mask_reply'] = address_mask_reply_dict
                if info_msg.get_Info_Msg_Content() is not None:
                    info_msg_content = info_msg.get_Info_Msg_Content()
                    info_msg_content_dict = {}
                    if info_msg_content.get_Identifier() is not None: info_msg_content_dict['identifier'] = Base_Object_Attribute.dict_from_object(info_msg_content.get_Identifier())
                    if info_msg_content.get_Sequence_Number() is not None: info_msg_content_dict['sequence_number'] = Base_Object_Attribute.dict_from_object(info_msg_content.get_Sequence_Number())
                    info_msg_dict['info_msg_content'] = info_msg_content_dict
                icmpv4_dict['info_msg'] = info_msg_dict
            if icmpv4.get_Traceroute() is not None:
                traceroute = icmpv4.get_Traceroute()
                traceroute_dict = {}
                if traceroute.get_Outbound_Packet_Forward_Success() is not None: traceroute_dict['outbound_packet_forward_success'] = traceroute.get_Outbound_Packet_Forward_Success()
                if traceroute.get_Outbound_Packet_no_Route() is not None: traceroute_dict['outbound_packet_no_route'] = traceroute.get_Outbound_Packet_no_Route()
                if traceroute.get_Identifier() is not None: traceroute_dict['identifier'] = Base_Object_Attribute.dict_from_object(traceroute.get_Identifier())
                if traceroute.get_Outbound_Hop_Count() is not None: traceroute_dict['outbound_hop_count'] = Base_Object_Attribute.dict_from_object(traceroute.get_Outbound_Hop_Count())
                if traceroute.get_Return_Hop_Count() is not None: traceroute_dict['return_hop_count'] = Base_Object_Attribute.dict_from_object(traceroute.get_Return_Hop_Count())
                if traceroute.get_Output_Link_Speed() is not None: traceroute_dict['output_link_speed'] = Base_Object_Attribute.dict_from_object(traceroute.get_Output_Link_Speed())
                if traceroute.get_Output_Link_MTU() is not None: traceroute_dict['output_link_mtu'] = Base_Object_Attribute.dict_from_object(traceroute.get_Output_Link_MTU())
                icmpv4_dict['traceroute'] = traceroute_dict
            internet_layer_dict['icmpv4'] = icmpv4_dict
        if internet_layer.get_IPv6() is not None:
            ipv6 = internet_layer.get_IPv6()
            ipv6_dict = {}
            if ipv6.get_IPv6_Header() is not None:
                ipv6_header = ipv6.get_IPv6_Header()
                ipv6_header_dict = {}
                if ipv6_header.get_IP_Version() is not None: ipv6_header_dict['ip_version'] = ipv6_header.get_IP_Version()
                if ipv6_header.get_Traffic_Class() is not None: ipv6_header_dict['traffic_class'] = Base_Object_Attribute.dict_from_object(ipv6_header.get_Traffic_Class())
                if ipv6_header.get_Flow_Label() is not None: ipv6_header_dict['flow_label'] = Base_Object_Attribute.dict_from_object(ipv6_header.get_Flow_Label())
                if ipv6_header.get_Payload_Length() is not None: ipv6_header_dict['payload_length'] = Base_Object_Attribute.dict_from_object(ipv6_header.get_Payload_Length())
                if ipv6_header.get_Next_Header() is not None: ipv6_header_dict['next_header'] = Base_Object_Attribute.dict_from_object(ipv6_header.get_Next_Header())
                if ipv6_header.get_TTL() is not None: ipv6_header_dict['ttl'] = Base_Object_Attribute.dict_from_object(ipv6_header.get_TTL())
                if ipv6_header.get_Src_IPv6_Addr() is not None: ipv6_header_dict['src_ipv6_addr'] = Address.dict_from_object(ipv6_header.get_Src_IPv6_Addr())
                if ipv6_header.get_Dest_IPv6_Addr() is not None: ipv6_header_dict['dest_ipv6_addr'] = Address.dict_from_object(ipv6_header.get_Dest_IPv6_Addr())
                ipv6_dict['ipv6_header'] = ipv6_header_dict
            if ipv6.get_Ext_Headers() is not None:
                ext_headers = []
                for ext_header in ipv6.get_Ext_Headers():
                    ext_header_dict = {}
                    if ext_header.get_Hop_by_Hop_Options() is not None:
                        hop_by_hop_options = ext_header.get_Hop_by_Hop_Options()
                        hop_by_hop_options_dict = {}
                        if hop_by_hop_options.get_Next_Header() is not None: hop_by_hop_options_dict['next_header'] = Base_Object_Attribute.dict_from_object(hop_by_hop_options.get_Next_Header())
                        if hop_by_hop_options.get_Header_Ext_Len() is not None: hop_by_hop_options_dict['header_ext_len'] = Base_Object_Attribute.dict_from_object(hop_by_hop_options.get_Header_Ext_Len())
                        if hop_by_hop_options.get_Option_Data() is not None:
                            option_data = []
                            for option in hop_by_hop_options.get_Option_Data():
                                option_dict = {}
                                if option.get_Option_Type() is not None: 
                                    option_type = option.get_Option_Type()
                                    option_type_dict = {}
                                    if option_type.get_Do_Not_Recogn_Action() is not None: option_type_dict['do_not_recogn_action'] = Base_Object_Attribute.dict_from_object(option_type.get_Do_Not_Recogn_Action())
                                    if option_type.get_Packet_Change() is not None: option_type_dict['packet_change'] = Base_Object_Attribute.dict_from_object(option_type.get_Packet_Change())
                                    if option_type.get_Option_Byte() is not None: option_type_dict['option_byte'] = Base_Object_Attribute.dict_from_object(option_type.get_Option_Byte())
                                    option_dict['option_type'] = option_type_dict
                                if option.get_Option_Data_Len() is not None: option_dict['option_data_len'] = Base_Object_Attribute.dict_from_object(option.get_Option_Data_Len())
                                if option.get_Pad1() is not None:
                                    pad1 = option.get_Pad1()
                                    pad1_dict = {}
                                    if pad1.get_Octet() is not None: pad1_dict['octet'] = Base_Object_Attribute.dict_from_object(pad1.get_Octet())
                                    option_dict['pad1'] = pad1_dict
                                if option.get_PadN() is not None:
                                    padn = option.get_PadN()
                                    padn_dict = {}
                                    if padn.get_Octet() is not None: padn_dict['octet'] = Base_Object_Attribute.dict_from_object(padn.get_Octet())
                                    if padn.get_Option_Data_Length() is not None: padn_dict['option_data_length'] = Base_Object_Attribute.dict_from_object(padn.get_Option_Data_Length())
                                    if padn.get_Option_Data() is not None: padn_dict['option_data'] = Base_Object_Attribute.dict_from_object(padn.get_Option_Data())
                                    option_dict['padn'] = padn_dict = {}
                                option_data.append[option_dict]
                            hop_by_hop_options_dict['option_data'] = option_data
                        ext_header_dict['hop_by_hop_options'] = hop_by_hop_options_dict
                    if ext_header.get_Routing() is not None:
                        routing = ext_header.get_Routing()
                        routing_dict = {}
                        if routing.get_Next_Header() is not None: routing_dict['next_header'] = Base_Object_Attribute.dict_from_object(routing.get_Next_Header())
                        if routing.get_Header_Ext_Len() is not None: routing_dict['header_ext_len'] = Base_Object_Attribute.dict_from_object(routing.get_Header_Ext_Len())
                        if routing.get_Routing_Type() is not None: routing_dict['routing_type'] = Base_Object_Attribute.dict_from_object(routing.get_Routing_Type())
                        if routing.get_Segments_Left() is not None: routing_dict['segments_left'] = Base_Object_Attribute.dict_from_object(routing.get_Segments_Left())
                        if routing.get_Type_Specific_Data() is not None: routing_dict['type_specific_data'] = Base_Object_Attribute.dict_from_object(routing.get_Type_Specific_Data())
                        ext_header_dict['routing'] = routing_dict
                    if ext_header.get_Fragment() is not None:
                        fragment = ext_header.get_Fragment()
                        fragment_dict = {}
                        if fragment.get_Fragment_Header() is not None:
                            fragment_header = fragment.get_Fragment_Header() 
                            fragment_header_dict = {}
                            if fragment_header.get_Next_Header() is not None: fragment_header_dict['next_header'] = Base_Object_Attribute.dict_from_object(fragment_header.get_Next_Header())
                            if fragment_header.get_Fragment_Offset() is not None: fragment_header_dict['fragment_offset'] = Base_Object_Attribute.dict_from_object(fragment_header.get_Fragment_Offset())
                            if fragment_header.get_M_Flag() is not None: fragment_header_dict['m_flag'] = Base_Object_Attribute.dict_from_object(fragment_header.get_M_Flag())
                            if fragment_header.get_Identification() is not None: fragment_header_dict['identification'] = Base_Object_Attribute.dict_from_object(fragment_header.get_Identification())
                            fragment_dict['fragment_header'] = fragment_header_dict
                        if fragment.get_Fragment() is not None: fragment_dict['fragment'] = Base_Object_Attribute.dict_from_object(fragment.get_Fragment())
                        ext_header_dict['fragment'] = fragment_dict
                    if ext_header.get_Destination_Options() is not None:
                        destination_options = []
                        for destination_option in ext_header.get_Destination_Options():
                            destination_option_dict = {}
                            if destination_option.get_Next_Header() is not None: destination_option_dict['next_header'] = Base_Object_Attribute.dict_from_object(destination_option.get_Next_Header())
                            if destination_option.get_Header_Ext_Len() is not None: destination_option_dict['header_ext_len'] = Base_Object_Attribute.dict_from_object(destination_option.get_Header_Ext_Len())
                            if destination_option.get_Option_Data() is not None: 
                                option_data = []
                                for option in destination_option.get_Option_Data():
                                    option_dict = {}
                                    if option.get_Option_Type() is not None: 
                                        option_type = option.get_Option_Type()
                                        option_type_dict = {}
                                        if option_type.get_Do_Not_Recogn_Action() is not None: option_type_dict['do_not_recogn_action'] = Base_Object_Attribute.dict_from_object(option_type.get_Do_Not_Recogn_Action())
                                        if option_type.get_Packet_Change() is not None: option_type_dict['packet_change'] = Base_Object_Attribute.dict_from_object(option_type.get_Packet_Change())
                                        if option_type.get_Option_Byte() is not None: option_type_dict['option_byte'] = Base_Object_Attribute.dict_from_object(option_type.get_Option_Byte())
                                        option_dict['option_type'] = option_type_dict
                                    if option.get_Option_Data_Len() is not None: option_dict['option_data_len'] = Base_Object_Attribute.dict_from_object(option.get_Option_Data_Len())
                                    if option.get_Pad1() is not None:
                                        pad1 = option.get_Pad1()
                                        pad1_dict = {}
                                        if pad1.get_Octet() is not None: pad1_dict['octet'] = Base_Object_Attribute.dict_from_object(pad1.get_Octet())
                                        option_dict['pad1'] = pad1_dict
                                    if option.get_PadN() is not None:
                                        padn = option.get_PadN()
                                        padn_dict = {}
                                        if padn.get_Octet() is not None: padn_dict['octet'] = Base_Object_Attribute.dict_from_object(padn.get_Octet())
                                        if padn.get_Option_Data_Length() is not None: padn_dict['option_data_length'] = Base_Object_Attribute.dict_from_object(padn.get_Option_Data_Length())
                                        if padn.get_Option_Data() is not None: padn_dict['option_data'] = Base_Object_Attribute.dict_from_object(padn.get_Option_Data())
                                        option_dict['padn'] = padn_dict = {}
                                    option_data.append[option_dict]
                                destination_option_dict['option_data'] = option_data
                            destination_options.append(destination_option_dict)
                        ext_header_dict['destination_options'] = destination_options
                    if ext_header.get_Authentication_Header() is not None:
                        authentication_header = ext_header.get_Authentication_Header()
                        authentication_header_dict = {}
                        if authentication_header.get_Next_Header() is not None: authentication_header_dict['next_header'] = Base_Object_Attribute.dict_from_object(authentication_header.get_Next_Header())
                        if authentication_header.get_Header_Ext_Len() is not None: authentication_header_dict['header_ext_len'] = Base_Object_Attribute.dict_from_object(authentication_header.get_Header_Ext_Len())
                        if authentication_header.get_Security_Parameters_Index() is not None: authentication_header_dict['security_parameters_index'] = Base_Object_Attribute.dict_from_object(authentication_header.get_Security_Parameters_Index())
                        if authentication_header.get_Sequence_Number() is not None: authentication_header_dict['sequence_number'] = Base_Object_Attribute.dict_from_object(authentication_header.get_Sequence_Number())
                        if authentication_header.get_Authenication_Data() is not None: authentication_header_dict['authenication_data'] = Base_Object_Attribute.dict_from_object(authentication_header.get_Authenication_Data())
                        ext_header_dict['authentication_header'] = authentication_header_dict
                    if ext_header.get_Excapsulating_Security_Payload() is not None:
                        excapsulating_security_payload = ext_header.get_Excapsulating_Security_Payload()
                        excapsulating_security_payload_dict = {}
                        if excapsulating_security_payload.get_Security_Parameters_Index() is not None: excapsulating_security_payload_dict['security_parameters_index'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Security_Parameters_Index())
                        if excapsulating_security_payload.get_Sequence_Number() is not None: excapsulating_security_payload_dict['sequence_number'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Sequence_Number())
                        if excapsulating_security_payload.get_Payload_Data() is not None: excapsulating_security_payload_dict['payload_data'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Payload_Data())
                        if excapsulating_security_payload.get_Padding() is not None: excapsulating_security_payload_dict['padding'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Padding())
                        if excapsulating_security_payload.get_Padding_Len() is not None: excapsulating_security_payload_dict['padding_len'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Padding_Len())
                        if excapsulating_security_payload.get_Next_Header() is not None: excapsulating_security_payload_dict['security_parameters_index'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Security_Parameters_Index())
                        if excapsulating_security_payload.get_Authenication_Data() is not None: excapsulating_security_payload_dict['authenication_data'] = Base_Object_Attribute.dict_from_object(excapsulating_security_payload.get_Authenication_Data())
                        ext_header_dict['excapsulating_security_payload'] = excapsulating_security_payload_dict
                    ext_headers.append(ext_header_dict)
                ipv6_dict['ext_headers'] = ext_headers
            internet_layer_dict['ipv6'] = ipv6_dict                                     
        if internet_layer.get_ICMPv6() is not None:
            icmpv6 = internet_layer.get_ICMPv6()
            icmpv6_dict = {}
            if icmpv6.get_ICMPv6_Header() is not None:
                icmpv6_header = icmpv6.get_ICMPv6_Header()
                icmpv6_header_dict = {}
                if icmpv6_header.get_Type() is not None: icmpv6_header_dict['type'] = Base_Object_Attribute.dict_from_object(icmpv6_header.get_Type())
                if icmpv6_header.get_Code() is not None: icmpv6_header_dict['code'] = Base_Object_Attribute.dict_from_object(icmpv6_header.get_Code())
                if icmpv6_header.get_Checksum() is not None: icmpv6_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(icmpv6_header.get_Checksum())
                icmpv6_dict['icmpv6_header'] = icmpv6_header_dict 
            if icmpv6.get_Error_Msg() is not None:
                error_msg = icmpv6.get_Error_Msg()
                error_msg_dict = {}
                if error_msg.get_Destination_Unreachable() is not None:
                    destination_unreachable = error_msg.get_Destination_Unreachable()
                    destination_unreachable_dict = {}
                    if destination_unreachable.get_No_Route() is not None: destination_unreachable_dict['no_route'] = destination_unreachable.get_No_Route()
                    if destination_unreachable.get_Comm_Prohibited() is not None: destination_unreachable_dict['comm_prohibited'] = destination_unreachable.get_Comm_Prohibited()
                    if destination_unreachable.get_Beyond_Scope() is not None: destination_unreachable_dict['beyond_scope'] = destination_unreachable.get_Beyond_Scope()
                    if destination_unreachable.get_Address_Unreachable() is not None: destination_unreachable_dict['address_unreachable'] = destination_unreachable.get_Address_Unreachable()
                    if destination_unreachable.get_Port_Unreachable() is not None: destination_unreachable_dict['port_unreachable'] = destination_unreachable.get_Port_Unreachable()
                    if destination_unreachable.get_Src_Addr_Failed_Policy() is not None: destination_unreachable_dict['src_addr_failed_policy'] = destination_unreachable.get_Src_Addr_Failed_Policy()
                    if destination_unreachable.get_Reject_Route() is not None: destination_unreachable_dict['reject_route'] = destination_unreachable.get_Reject_Route()
                    error_msg_dict['destination_unreachable'] = destination_unreachable_dict
                if error_msg.get_Packet_Too_Big() is not None:
                    packet_too_big = error_msg.get_Packet_Too_Big()
                    packet_too_big_dict = {}
                    if packet_too_big.get_Packet_Too_Big() is not None: packet_too_big_dict['packet_too_big'] = packet_too_big.get_Packet_Too_Big()
                    if packet_too_big.get_MTU() is not None: packet_too_big_dict['mtu'] = Base_Object_Attribute.dict_from_object(packet_too_big.get_MTU())
                    error_msg_dict['packet_too_big'] = packet_too_big_dict
                if error_msg.get_Time_Exceeded() is not None:
                    time_exceeded = error_msg.get_Time_Exceeded()
                    time_exceeded_dict = {}
                    if time_exceeded.get_Hop_Limit_Exceeded() is not None: time_exceeded_dict['hop_limit_exceeded'] = time_exceeded.get_Hop_Limit_Exceeded()
                    if time_exceeded.get_Fragment_Reassem_Time_Exceeded() is not None: time_exceeded_dict['fragment_reassem_time_exceeded'] = time_exceeded.get_Fragment_Reassem_Time_Exceeded()
                    error_msg_dict['time_exceeded'] = time_exceeded_dict
                if error_msg.get_Parameter_Problem() is not None:
                    parameter_problem = error_msg.get_Parameter_Problem()
                    parameter_problem_dict = {}
                    if parameter_problem.get_Erroneous_Header_Field() is not None: parameter_problem_dict['erroneous_header_field'] = parameter_problem.get_Erroneous_Header_Field()
                    if parameter_problem.get_Unrecognized_Next_Header_Type() is not None: parameter_problem_dict['unrecognized_next_header_type'] = parameter_problem.get_Unrecognized_Next_Header_Type() 
                    if parameter_problem.get_Unrecognized_IPv6_Option() is not None: parameter_problem_dict['unrecognized_ipv6_option'] = parameter_problem.get_Unrecognized_IPv6_Option()
                    if parameter_problem.get_Pointer() is not None: parameter_problem_dict['pointer'] = Base_Object_Attribute.dict_from_object(parameter_problem.get_Pointer())
                    error_msg_dict['parameter_problem'] = parameter_problem_dict
                if error_msg.get_Invoking_Packet() is not None: error_msg_dict['invoking_packet'] = Base_Object_Attribute.dict_from_object(error_msg.get_Invoking_Packet())
                icmpv6_dict['error_msg'] = error_msg_dict
            if icmpv6.get_Info_Msg() is not None:
                info_msg = icmpv6.get_Info_Msg()
                info_msg_dict = {}
                if info_msg.get_Echo_Request() is not None:
                    echo_request = info_msg.get_Echo_Request()
                    echo_request_dict = {}
                    if echo_request.get_Echo_Request() is not None: echo_request_dict['echo_request'] = echo_request.get_Echo_Request()
                    if echo_request.get_Data() is not None: echo_request_dict['data'] = Base_Object_Attribute.dict_from_object(echo_request.get_Data())
                    info_msg_dict['echo_request'] = echo_request_dict
                if info_msg.get_Echo_Reply() is not None:
                    echo_reply = info_msg.get_Echo_Reply()
                    echo_reply_dict = {}
                    if echo_reply.get_Echo_Reply() is not None: echo_reply_dict['echo_reply'] = echo_reply.get_Echo_Reply()
                    if echo_reply.get_Data() is not None: echo_reply_dict['data'] = Base_Object_Attribute.dict_from_object(echo_reply.get_Data())
                    info_msg_dict['echo_reply'] = echo_reply_dict
                if info_msg.get_Info_Msg_Content() is not None:
                    info_msg_content = info_msg.get_Info_Msg_Content()
                    info_msg_content_dict = {}
                    if info_msg_content.get_Identifier() is not None: info_msg_content_dict['identifier'] = Base_Object_Attribute.dict_from_object(info_msg_content.get_Identifier())
                    if info_msg_content.get_Sequence_Number() is not None: info_msg_content_dict['sequence_number'] = Base_Object_Attribute.dict_from_object(info_msg_content.get_Sequence_Number())
                    info_msg_dict['info_msg_content'] = info_msg_content_dict
                icmpv6_dict['info_msg'] = info_msg_dict    
            internet_layer_dict['icmpv6'] = icmpv6_dict    
        return internet_layer_dict

    @classmethod
    def __parse_transport_layer(cls, transport_layer):
        transport_layer_dict = {}
        if transport_layer.get_TCP() is not None:
            tcp = transport_layer.get_TCP()
            tcp_dict = {}
            if tcp.get_TCP_Header() is not None:
                tcp_header = tcp.get_TCP_Header()
                tcp_header_dict = {}
                if tcp_header.get_Src_Port() is not None: tcp_header_dict['src_port'] = Port.dict_from_object(tcp_header.get_Src_Port())
                if tcp_header.get_Dest_Port() is not None: tcp_header_dict['dest_port'] = Port.dict_from_object(tcp_header.get_Dest_Port())
                if tcp_header.get_Seq_Num() is not None: tcp_header_dict['seq_num'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Seq_Num())
                if tcp_header.get_ACK_Num() is not None: tcp_header_dict['ack_num'] = Base_Object_Attribute.dict_from_object(tcp_header.get_ACK_Num())
                if tcp_header.get_Data_Offset() is not None: tcp_header_dict['data_offset'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Data_Offset())
                if tcp_header.get_Reserved() is not None: tcp_header_dict['reserved'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Reserved())
                if tcp_header.get_TCP_Flags() is not None: 
                    tcp_flags = tcp_header.get_TCP_Flags()
                    tcp_flags_dict = {}
                    if tcp_flags.get_ns() is not None: tcp_flags_dict['ns'] = tcp_flags.get_ns()
                    if tcp_flags.get_cwr() is not None: tcp_flags_dict['cwr'] = tcp_flags.get_cwr()
                    if tcp_flags.get_ece() is not None: tcp_flags_dict['ece'] = tcp_flags.get_ece()
                    if tcp_flags.get_urg() is not None: tcp_flags_dict['urg'] = tcp_flags.get_urg()
                    if tcp_flags.get_ack() is not None: tcp_flags_dict['ack'] = tcp_flags.get_ack()
                    if tcp_flags.get_psh() is not None: tcp_flags_dict['psh'] = tcp_flags.get_psh()
                    if tcp_flags.get_rst() is not None: tcp_flags_dict['rst'] = tcp_flags.get_rst()
                    if tcp_flags.get_syn() is not None: tcp_flags_dict['syn'] = tcp_flags.get_syn()
                    if tcp_flags.get_fin() is not None: tcp_flags_dict['fin'] = tcp_flags.get_fin()
                    tcp_header_dict['tcp_flags'] = tcp_flags_dict
                if tcp_header.get_Window() is not None: tcp_header_dict['window'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Window())
                if tcp_header.get_Checksum() is not None: tcp_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Checksum())
                if tcp_header.get_Urg_Ptr() is not None: tcp_header_dict['urg_ptr'] = Base_Object_Attribute.dict_from_object(tcp_header.get_Urg_Ptr())
                tcp_dict['tcp_header'] = tcp_header_dict
            if tcp.get_Options() is not None: tcp_dict['options'] = Base_Object_Attribute.dict_from_object(tcp.get_Options())
            if tcp.get_Data() is not None: tcp_dict['data'] = utils.parse_data_segment_into_dict(tcp.get_Data())
            transport_layer_dict['tcp'] = tcp_dict
        if transport_layer.get_UDP() is not None:
            udp = transport_layer.get_UDP()
            udp_dict = {}
            if udp.get_UDP_Header() is not None:
                udp_header = udp.get_UDP_Header()
                udp_header_dict = {}
                if udp_header.get_SrcPort() is not None: udp_header_dict['srcport'] = Port.dict_from_object(udp_header.get_SrcPort())
                if udp_header.get_DestPort() is not None: udp_header_dict['destport'] = Port.dict_from_object(udp_header.get_DestPort())
                if udp_header.get_Length() is not None: udp_header_dict['length'] = Base_Object_Attribute.dict_from_object(udp_header.get_Length())
                if udp_header.get_Checksum() is not None: udp_header_dict['checksum'] = Base_Object_Attribute.dict_from_object(udp_header.get_Checksum())
                udp_dict['udp_header'] = udp_header_dict
            if udp.get_Data() is not None: udp_dict['data'] = utils.parse_data_segment_into_dict(udp.get_Data())
            transport_layer_dict['udp'] = udp_dict                                           
        return transport_layer_dict
