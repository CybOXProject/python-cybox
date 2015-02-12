# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import cybox
import cybox.bindings.network_packet_object as network_packet_binding
from cybox.common import (DataSegment, HexBinary, Integer, ObjectProperties,
        PositiveInteger, String, UnsignedInteger)
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port


class TypeLength(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TypeLengthType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice
    length = cybox.TypedField("Length", HexBinary)
    internet_layer_type = cybox.TypedField("Internet_Layer_Type", String)


class EthernetHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EthernetHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_mac_addr = cybox.TypedField("Destination_MAC_Addr", Address)
    source_mac_addr = cybox.TypedField("Source_MAC_Addr", Address)
    type_or_length = cybox.TypedField("Type_Or_Length", TypeLength)
    checksum = cybox.TypedField("Checksum", HexBinary)


class EthernetInterface(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EthernetInterfaceType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ethernet_header = cybox.TypedField("Ethernet_Header", EthernetHeader)


class PhysicalInterface(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PhysicalInterfaceType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ethernet = cybox.TypedField("Ethernet", EthernetInterface)


class ARP(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ARPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    hardware_addr_type = cybox.TypedField("Hardware_Addr_Type", String)
    proto_addr_type = cybox.TypedField("Proto_Addr_Type", String)
    hardware_addr_size = cybox.TypedField("Hardware_Addr_Size", HexBinary)
    proto_addr_size = cybox.TypedField("Proto_Addr_Size", HexBinary)
    op_type = cybox.TypedField("Op_Type", String)
    sender_hardware_addr = cybox.TypedField("Sender_Hardware_Addr", Address)
    sender_protocol_addr = cybox.TypedField("Sender_Protocol_Addr", Address)
    recip_hardware_addr = cybox.TypedField("Recip_Hardware_Addr", Address)
    recip_protocol_addr = cybox.TypedField("Recip_Protocol_Addr", Address)


class _ICMPHeader(cybox.Entity):
    """Abstract Type"""
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    type_ = cybox.TypedField("Type", HexBinary)
    code = cybox.TypedField("Code", HexBinary)
    checksum = cybox.TypedField("Checksum", HexBinary)


class ICMPv4Header(_ICMPHeader):
    _binding_class = network_packet_binding.ICMPv4HeaderType


class ICMPv6Header(_ICMPHeader):
    _binding_class = network_packet_binding.ICMPv6HeaderType


class NDPLinkAddr(cybox.Entity):
    """Abstract Type"""
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPLinkAddrType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = cybox.TypedField("Length", Integer)
    link_layer_mac_addr = cybox.TypedField("Link_Layer_MAC_Addr", Address)


class RouterSolicitationOptions(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterSolicitationOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_link_addr = cybox.TypedField("Src_Link_Addr", NDPLinkAddr)


class RouterSolicitation(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterSolicitationType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    options = cybox.TypedField("Options", RouterSolicitationOptions,
                               multiple=True)


class NDPMTU(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPMTUType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = cybox.TypedField("Length", Integer)
    mtu = cybox.TypedField("MTU", Integer)


class Prefix(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PrefixType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    ipv6_addr = cybox.TypedField("IPv6_Addr", Address)
    ip_addr_prefix = cybox.TypedField("IP_Addr_Prefix", Address)


class NDPPrefixInfo(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPPrefixInfoType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    link_flag = cybox.TypedField("link_flag")
    addr_config_flag = cybox.TypedField("addr_config_flag")
    length = cybox.TypedField("Length", Integer)
    prefix_length = cybox.TypedField("Prefix_Length", Integer)
    valid_lifetime = cybox.TypedField("Valid_Lifetime", Integer)
    preferred_lifetime = cybox.TypedField("Preferred_Lifetime", Integer)
    prefix = cybox.TypedField("Prefix", Prefix)


class RouterAdvertisementOptions(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterAdvertisementOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    src_link_addr = cybox.TypedField("Src_Link_Addr", NDPLinkAddr)
    mtu = cybox.TypedField("MTU", NDPMTU)
    prefix_info = cybox.TypedField("Prefix_Info", NDPPrefixInfo)


class RouterAdvertisement(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterAdvertisementType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    managed_address_config_flag = \
            cybox.TypedField("managed_address_config_flag")
    other_config_flag = cybox.TypedField("other_config_flag")
    cur_hop_limit = cybox.TypedField("Cur_Hop_Limit", Integer)
    router_lifetime = cybox.TypedField("Router_Lifetime", Integer)
    reachable_time = cybox.TypedField("Reachable_Time", Integer)
    retrans_timer = cybox.TypedField("Retrans_Timer", Integer)
    options = cybox.TypedField("Options", RouterAdvertisementOptions)


class NeighborSolicitationOptions(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborSolicitationOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_link_addr = cybox.TypedField("Src_Link_Addr", NDPLinkAddr)


class NeighborSolicitation(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborSolicitationType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_ipv6_addr = cybox.TypedField("Target_IPv6_Addr", Address)
    options = cybox.TypedField("Options", NeighborSolicitationOptions)


class NeighborOptions(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_link_addr = cybox.TypedField("Target_Link_Addr", NDPLinkAddr)


class NeighborAdvertisement(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborAdvertisementType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    router_flag = cybox.TypedField("router_flag")
    solicited_flag = cybox.TypedField("solicited_flag")
    override_flag = cybox.TypedField("override_flag")
    target_ipv6_addr = cybox.TypedField("Target_IPv6_Addr", Address)
    options = cybox.TypedField("Options", NeighborOptions)


class NDPRedirectedHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPRedirectedHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = cybox.TypedField("Length", Integer)
    ipheader_and_data = cybox.TypedField("IPHeader_And_Data", HexBinary)


class RedirectOptions(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_link_addr = cybox.TypedField("Target_Link_Addr", NDPLinkAddr)
    redirected_header = cybox.TypedField("Redirected_Header",
                                         NDPRedirectedHeader)


class Redirect(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RedirectType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_ipv6_addr = cybox.TypedField("Target_IPv6_Addr", Address)
    dest_ipv6_addr = cybox.TypedField("Dest_IPv6_Addr", Address)
    options = cybox.TypedField("Options", RedirectOptions)


class NDP(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv6_header = cybox.TypedField("ICMPv6_Header", ICMPv6Header)

    #TODO: choice between these 5
    router_solicitation = cybox.TypedField("Router_Solicitation",
                                           RouterSolicitation)
    router_advertisement = cybox.TypedField("Router_Advertisement",
                                            RouterAdvertisement)
    neighbor_solicitation = cybox.TypedField("Neighbor_Solicitation",
                                             NeighborSolicitation)
    neighbor_advertisement = cybox.TypedField("Neighbor_Advertisement",
                                              NeighborAdvertisement)
    redirect = cybox.TypedField("Redirect", Redirect)


class LogicalProtocol(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.LogicalProtocolType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    arp_rarp = cybox.TypedField("ARP_RARP", ARP)
    ndp = cybox.TypedField("NDP", NDP)


class LinkLayer(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.LinkLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    physical_interface = cybox.TypedField("Physical_Interface",
                                                            PhysicalInterface)
    logical_protocls = cybox.TypedField("Logical_Protocols", LogicalProtocol)


class IPv4Flags(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4FlagsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    reserved = cybox.TypedField("Reserved", Integer)
    do_not_fragment = cybox.TypedField("Do_Not_Fragment", String)
    more_fragments = cybox.TypedField("More_Fragments", String)

    def __init__(self):
        super(IPv4Flags, self).__init__()
        self.reserved = Integer(0)


class IPv4Option(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4OptionType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    copy_flag = cybox.TypedField("Copy_Flag", String)
    class_ = cybox.TypedField("Class", String)
    option = cybox.TypedField("Option", String)


class IPv4Header(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4HeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_version = cybox.TypedField("IP_Version", String)
    header_length = cybox.TypedField("Header_Length", Integer)
    dscp = cybox.TypedField("DSCP", HexBinary)
    ecn = cybox.TypedField("ECN", HexBinary)
    total_length = cybox.TypedField("Total_Length", HexBinary)
    identification = cybox.TypedField("Identification", PositiveInteger)
    flags = cybox.TypedField("Flags", IPv4Flags)
    fragment_offset = cybox.TypedField("Fragment_Offset", HexBinary)
    ttl = cybox.TypedField("TTL", HexBinary)
    protocol = cybox.TypedField("Protocol", String)
    checksum = cybox.TypedField("Checksum", HexBinary)
    src_ipv4_addr = cybox.TypedField("Src_IPv4_Addr", Address)
    dest_ipv4_addr = cybox.TypedField("Dest_IPv4_Addr", Address)
    option = cybox.TypedField("Option", IPv4Option, multiple=True)


class IPv4Packet(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ipv4_header = cybox.TypedField("IPv4_Header", IPv4Header)
    data = cybox.TypedField("Data", HexBinary)


class FragmentationRequired(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentationRequiredType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    fragmentation_required = cybox.TypedField("Fragmentation_Required")
    next_hop_mtu = cybox.TypedField("Next_Hop_MTU", HexBinary)


class ICMPv4DestinationUnreachable(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4DestinationUnreachableType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    destination_network_unreachable = \
            cybox.TypedField("Destination_Network_Unreachable")
    destination_host_unreachable = \
            cybox.TypedField("Destination_Host_Unreachable")
    destination_protocol_unreachable = \
            cybox.TypedField("Destination_Protocol_Unreachable")
    destination_port_unreachable = \
            cybox.TypedField("Destination_Port_Unreachable")
    fragmentation_required = cybox.TypedField("Fragmentation_Required",
                                             FragmentationRequired)
    source_route_failed = cybox.TypedField("Source_Route_Failed")
    destination_network_unknown = \
            cybox.TypedField("Destination_Network_Unknown")
    destination_host_unknown = cybox.TypedField("Destination_Host_Unknown")
    source_host_isolated = cybox.TypedField("Source_Host_Isolated")
    network_administratively_prohibited = \
            cybox.TypedField("Network_Administratively_Prohibited")
    host_administratively_prohibited = \
            cybox.TypedField("Host_Administratively_Prohibited")
    network_unreachable_for_tos = \
            cybox.TypedField("Network_Unreachable_For_TOS")
    host_unreachable_for_tos = \
            cybox.TypedField("Host_Unreachable_For_TOS")
    communication_administratively_prohibited = \
            cybox.TypedField("Communication_Administratively_Prohibited")
    host_precedence_violation = cybox.TypedField("Host_Precedence_Violation")
    precedence_cutoff_in_effect = \
            cybox.TypedField("Precedence_Cutoff_In_Effect")


class ICMPv4SourceQuench(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4SourceQuenchType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    source_quench = cybox.TypedField("Source_Quench")


class ICMPv4RedirectMessage(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4RedirectMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice of first 4
    network_redirect = cybox.TypedField("Network_Redirect")
    host_redirect = cybox.TypedField("Host_Redirect")
    tos_network_redirect = cybox.TypedField("ToS_Network_Redirect")
    tos_host_redirect = cybox.TypedField("ToS_Host_Redirect")

    ip_address = cybox.TypedField("IP_Address", Address)


class ICMPv4TimeExceeded(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimeExceededType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice
    ttl_exceeded_in_transit = cybox.TypedField("TTL_Exceeded_In_Transit")
    frag_reassembly_time_exceeded = \
            cybox.TypedField("Frag_Reassembly_Time_Exceeded")


class ICMPv4ErrorMessageContent(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4ErrorMessageContentType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_header = cybox.TypedField("IP_Header", IPv4Header)
    first_eight_bytes = cybox.TypedField("First_Eight_Bytes", HexBinary)


class ICMPv4ErrorMessage(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4ErrorMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_unreachable = cybox.TypedField("Destination_Unreachable",
                                                ICMPv4DestinationUnreachable)
    source_quench = cybox.TypedField("Source_Quench", ICMPv4SourceQuench)
    redirect_message = cybox.TypedField("Redirect_Message",
                                        ICMPv4RedirectMessage)
    time_exceeded = cybox.TypedField("Time_Exceeded", ICMPv4TimeExceeded)
    error_msg_content = cybox.TypedField("Error_Msg_Content",
                                        ICMPv4ErrorMessageContent)


class _ICMPEchoReply(cybox.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    echo_reply = cybox.TypedField("Echo_Reply")
    data = cybox.TypedField("Data", HexBinary)


class _ICMPEchoRequest(cybox.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    echo_request = cybox.TypedField("Echo_Request")
    data = cybox.TypedField("Data", HexBinary)


class ICMPv4EchoReply(_ICMPEchoReply):
    _binding_class = network_packet_binding.ICMPv4EchoReplyType


class ICMPv4EchoRequest(_ICMPEchoRequest):
    _binding_class = network_packet_binding.ICMPv4EchoRequestType


class ICMPv6EchoReply(_ICMPEchoReply):
    _binding_class = network_packet_binding.ICMPv6EchoReplyType


class ICMPv6EchoRequest(_ICMPEchoRequest):
    _binding_class = network_packet_binding.ICMPv6EchoRequestType


class ICMPv4TimestampRequest(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimestampRequestType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    timestamp = cybox.TypedField("Timestamp")
    originate_timestamp = cybox.TypedField("Originate_Timestamp",
                                           UnsignedInteger)


class ICMPv4TimestampReply(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimestampReplyType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    timestamp_reply = cybox.TypedField("Timestamp_Reply")
    originate_timestamp = cybox.TypedField("Originate_Timestamp",
                                           UnsignedInteger)
    receive_timestamp = cybox.TypedField("Receive_Timestamp",
                                         UnsignedInteger)
    transmit_timestamp = cybox.TypedField("Transmit_Timestamp",
                                          UnsignedInteger)


class ICMPv4AddressMaskRequest(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4AddressMaskRequestType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    address_mask_request = cybox.TypedField("Address_Mask_Request")
    address_mask = cybox.TypedField("Address_Mask", Address)


class ICMPv4AddressMaskReply(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4AddressMaskReplyType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    address_mask_reply = cybox.TypedField("Address_Mask_Reply")
    address_mask = cybox.TypedField("Address_Mask", Address)


class _ICMPInfoMessageContent(cybox.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    identifier = cybox.TypedField("Identifier", HexBinary)
    sequence_number = cybox.TypedField("Sequence_Number", HexBinary)


class ICMPv4InfoMessageContent(_ICMPInfoMessageContent):
    _binding_class = network_packet_binding.ICMPv4InfoMessageContentType


class ICMPv6InfoMessageContent(_ICMPInfoMessageContent):
    _binding_class = network_packet_binding.ICMPv6InfoMessageContentType


class ICMPv4InfoMessage(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4InfoMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 6
    echo_reply = cybox.TypedField("Echo_Reply", ICMPv4EchoReply)
    echo_request = cybox.TypedField("Echo_Request", ICMPv4EchoRequest)
    timestamp_request = cybox.TypedField("Timestamp_Request",
                                         ICMPv4TimestampRequest)
    timestamp_reply = cybox.TypedField("Timestamp_Reply", ICMPv4TimestampReply)
    address_mask_request = cybox.TypedField("Address_Mask_Request",
                                            ICMPv4AddressMaskRequest)
    address_mask_reply = cybox.TypedField("Address_Mask_Reply",
                                          ICMPv4AddressMaskReply)

    info_msg_content = cybox.TypedField("Info_Msg_Content",
                                        ICMPv4InfoMessageContent)


class ICMPv4Traceroute(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TracerouteType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    outbound_packet_forward_success = \
            cybox.TypedField("Outbound_Packet_Forward_Success")
    outbound_packet_no_route = cybox.TypedField("Outbound_Packet_no_Route")
    identifier = cybox.TypedField("Identifier", HexBinary)
    outbound_hop_count = cybox.TypedField("Outbound_Hop_Count", HexBinary)
    return_hop_count = cybox.TypedField("Return_Hop_Count", HexBinary)
    output_link_speed = cybox.TypedField("Output_Link_Speed", HexBinary)
    output_link_mtu = cybox.TypedField("Output_Link_MTU", HexBinary)


class ICMPv4Packet(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv4_header = cybox.TypedField("ICMPv4_Header", ICMPv4Header)

    # TODO: choice between these 3
    error_msg = cybox.TypedField("Error_Msg", ICMPv4ErrorMessage)
    info_msg = cybox.TypedField("Info_Msg", ICMPv4InfoMessage)
    traceroute = cybox.TypedField("Traceroute", ICMPv4Traceroute)


class IPv6Header(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6HeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_version = cybox.TypedField("IP_Version", String)
    traffic_class = cybox.TypedField("Traffic_Class", HexBinary)
    flow_label = cybox.TypedField("Flow_Label", HexBinary)
    payload_length = cybox.TypedField("Payload_Length", HexBinary)
    next_header = cybox.TypedField("Next_Header", String)
    ttl = cybox.TypedField("TTL", PositiveInteger)
    src_ipv6_addr = cybox.TypedField("Src_IPv6_Addr", Address)
    dest_ipv6_addr = cybox.TypedField("Dest_IPv6_Addr", Address)


class IPv6Option(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6OptionType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    do_not_recogn_action = cybox.TypedField("Do_Not_Recogn_Action", String)
    packet_change = cybox.TypedField("Packet_Change", String)
    option_byte = cybox.TypedField("Option_Byte", HexBinary)


class Pad1(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.Pad1Type
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    octet = cybox.TypedField("Octet", HexBinary)


class PadN(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PadNType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    octet = cybox.TypedField("Octet", HexBinary)
    option_data_length = cybox.TypedField("Option_Data_Length", Integer)
    option_data = cybox.TypedField("Option_Data", Integer)


class OptionData(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.OptionDataType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    option_type = cybox.TypedField("Option_Type", IPv6Option)
    option_data_len = cybox.TypedField("Option_Data_Len", HexBinary)

    #TODO: choice
    pad1 = cybox.TypedField("Pad1", Pad1)
    padn = cybox.TypedField("PadN", PadN)


class _IPv6ExtHeader(cybox.Entity):
    """Shared by a couple types"""
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = cybox.TypedField("Next_Header", String)
    header_ext_len = cybox.TypedField("Header_Ext_Len", HexBinary)
    option_data = cybox.TypedField("Option_Data", OptionData, multiple=True)


class HopByHopOptions(_IPv6ExtHeader):
    _binding_class = network_packet_binding.HopByHopOptionsType


class Routing(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RoutingType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = cybox.TypedField("Next_Header", String)
    header_ext_len = cybox.TypedField("Header_Ext_Len", Integer)
    routing_type = cybox.TypedField("Routing_Type", HexBinary)
    segments_left = cybox.TypedField("Segments_Left", Integer)
    type_specific_data = cybox.TypedField("Type_Specific_Data", String)


class FragmentHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = cybox.TypedField("Next_Header", HexBinary)
    fragment_offset = cybox.TypedField("Fragment_Offset", HexBinary)
    m_flag = cybox.TypedField("M_Flag", String)
    identification = cybox.TypedField("Identification", HexBinary)


class Fragment(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    fragment_header = cybox.TypedField("Fragment_Header", FragmentHeader)
    fragment = cybox.TypedField("Fragment", HexBinary)


class DestinationOptions(_IPv6ExtHeader):
    _binding_class = network_packet_binding.DestinationOptionsType


class AuthenticationHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.AuthenticationHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = cybox.TypedField("Next_Header", String)
    header_ext_len = cybox.TypedField("Header_Ext_Len", HexBinary)
    security_parameters_index = cybox.TypedField("Security_Parameters_Index",
                                                 HexBinary)
    sequence_number = cybox.TypedField("Sequence_Number", HexBinary)
    Authentication_Data = cybox.TypedField("Authentication_Data", HexBinary)


class EncapsulatingSecurityPayload(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EncapsulatingSecurityPayloadType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    security_parameters_index = cybox.TypedField("Security_Parameters_Index",
                                                 HexBinary)
    sequence_number = cybox.TypedField("Sequence_Number", HexBinary)
    payload_data = cybox.TypedField("Payload_Data", HexBinary)
    padding = cybox.TypedField("Padding", HexBinary)
    padding_len = cybox.TypedField("Padding_Len", HexBinary)
    next_header = cybox.TypedField("Next_Header", String)
    authentication_data = cybox.TypedField("Authentication_Data", HexBinary)


class IPv6ExtHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6ExtHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    hop_by_hop_options = cybox.TypedField("Hop_by_Hop_Options",
                                          HopByHopOptions)
    routing = cybox.TypedField("Routing", Routing)
    fragment = cybox.TypedField("Fragment", Fragment)
    destination_options = cybox.TypedField("Destination_Options",
                                            DestinationOptions, multiple=True)
    authentication_header = cybox.TypedField("Authentication_Header",
                                             AuthenticationHeader)
    encapsulating_security_payload = cybox.TypedField("Encapsulating_Security_Payload", EncapsulatingSecurityPayload)


class IPv6Packet(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ipv6_header = cybox.TypedField("IPv6_Header", IPv6Header)
    data = cybox.TypedField("Data", HexBinary)
    ext_headers = cybox.TypedField("Ext_Headers", IPv6ExtHeader, multiple=True)


class ICMPv6DestinationUnreachable(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6DestinationUnreachableType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    no_route = cybox.TypedField("No_Route")
    comm_prohibited = cybox.TypedField("Comm_Prohibited")
    beyond_scope = cybox.TypedField("Beyond_Scope")
    address_unreachable = cybox.TypedField("Address_Unreachable")
    port_unreachable = cybox.TypedField("Port_Unreachable")
    src_addr_failed_policy = cybox.TypedField("Src_Addr_Failed_Policy")
    reject_route = cybox.TypedField("Reject_Route")


class ICMPv6PacketTooBig(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6PacketTooBigType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    packet_too_big = cybox.TypedField("Packet_Too_Big")
    mtu = cybox.TypedField("MTU", HexBinary)


class ICMPv6TimeExceeded(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6TimeExceededType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    hop_limit_exceeded = cybox.TypedField("Hop_Limit_Exceeded")
    fragment_reassem_time_exceeded = \
            cybox.TypedField("Fragment_Reassem_Time_Exceeded")


class ICMPv6ParameterProblem(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6ParameterProblemType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 3
    erroneous_header_field = cybox.TypedField("Erroneous_Header_Field")
    unrecognized_next_header_type = \
            cybox.TypedField("Unrecognized_Next_Header_Type")
    unrecognized_ipv6_option = cybox.TypedField("Unrecognized_IPv6_Option")

    pointer = cybox.TypedField("Pointer", HexBinary)


class ICMPv6ErrorMessage(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6ErrorMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_unreachable = cybox.TypedField("Destination_Unreachable",
                                                ICMPv6DestinationUnreachable)
    packet_too_big = cybox.TypedField("Packet_Too_Big", ICMPv6PacketTooBig)
    time_exceeded = cybox.TypedField("Time_Exceeded", ICMPv6TimeExceeded)
    parameter_problem = cybox.TypedField("Parameter_Problem",
                                         ICMPv6ParameterProblem)
    invoking_packet = cybox.TypedField("Invoking_Packet", HexBinary)


class ICMPv6InfoMessage(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6InfoMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 2
    echo_request = cybox.TypedField("Echo_Request", ICMPv6EchoRequest)
    echo_reply = cybox.TypedField("Echo_Reply", ICMPv6EchoReply)

    info_msg_content = cybox.TypedField("Info_Msg_Content",
                                        ICMPv6InfoMessageContent)


class ICMPv6Packet(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv6_header = cybox.TypedField("ICMPv6_Header", ICMPv6Header)
    error_msg = cybox.TypedField("Error_Msg", ICMPv6ErrorMessage)
    info_msg = cybox.TypedField("Info_Msg", ICMPv6InfoMessage)


class InternetLayer(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.InternetLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    ipv4 = cybox.TypedField("IPv4", IPv4Packet)
    icmpv4 = cybox.TypedField("ICMPv4", ICMPv4Packet)
    ipv6 = cybox.TypedField("IPv6", IPv6Packet)
    icmpv6 = cybox.TypedField("ICMPv6", ICMPv6Packet)


class TCPFlags(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPFlagsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ns = cybox.TypedField("ns")
    cwr = cybox.TypedField("cwr")
    ece = cybox.TypedField("ece")
    urg = cybox.TypedField("urg")
    ack = cybox.TypedField("ack")
    psh = cybox.TypedField("psh")
    rst = cybox.TypedField("rst")
    syn = cybox.TypedField("syn")
    fin = cybox.TypedField("fin")


class TCPHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_port = cybox.TypedField("Src_Port", Port)
    dest_port = cybox.TypedField("Dest_Port", Port)
    seq_num = cybox.TypedField("Seq_Num", HexBinary)
    ack_num = cybox.TypedField("ACK_Num", HexBinary)
    data_offset = cybox.TypedField("Data_Offset", HexBinary)
    reserved = cybox.TypedField("Reserved", HexBinary)
    tcp_flags = cybox.TypedField("TCP_Flags", TCPFlags)
    window = cybox.TypedField("Window", HexBinary)
    checksum = cybox.TypedField("Checksum", HexBinary)
    urg_ptr = cybox.TypedField("Urg_Ptr", HexBinary)


class TCP(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    tcp_header = cybox.TypedField("TCP_Header", TCPHeader)
    options = cybox.TypedField("Options", HexBinary)
    data = cybox.TypedField("Data", DataSegment)


class UDPHeader(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.UDPHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    srcport = cybox.TypedField("SrcPort", Port)
    destport = cybox.TypedField("DestPort", Port)
    length = cybox.TypedField("Length", Integer)
    checksum = cybox.TypedField("Checksum", HexBinary)


class UDP(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.UDPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    udp_header = cybox.TypedField("UDP_Header", UDPHeader)
    data = cybox.TypedField("Data", DataSegment)


class TransportLayer(cybox.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TransportLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    tcp = cybox.TypedField("TCP", TCP)
    udp = cybox.TypedField("UDP", UDP)


class NetworkPacket(ObjectProperties):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NetworkPacketObjectType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"
    _XSI_NS = "PacketObj"
    _XSI_TYPE = "NetworkPacketObjectType"

    link_layer = cybox.TypedField("Link_Layer", LinkLayer)
    internet_layer = cybox.TypedField("Internet_Layer", InternetLayer)
    transport_layer = cybox.TypedField("Transport_Layer", TransportLayer)
