# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.network_packet_object as network_packet_binding
from cybox.common import (DataSegment, HexBinary, Integer, ObjectProperties,
        PositiveInteger, String, UnsignedInteger)
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port


class TypeLength(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TypeLengthType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice
    length = fields.TypedField("Length", HexBinary)
    internet_layer_type = fields.TypedField("Internet_Layer_Type", String)


class EthernetHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EthernetHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_mac_addr = fields.TypedField("Destination_MAC_Addr", Address)
    source_mac_addr = fields.TypedField("Source_MAC_Addr", Address)
    type_or_length = fields.TypedField("Type_Or_Length", TypeLength)
    checksum = fields.TypedField("Checksum", HexBinary)


class EthernetInterface(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EthernetInterfaceType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ethernet_header = fields.TypedField("Ethernet_Header", EthernetHeader)


class PhysicalInterface(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PhysicalInterfaceType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ethernet = fields.TypedField("Ethernet", EthernetInterface)


class ARP(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ARPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    hardware_addr_type = fields.TypedField("Hardware_Addr_Type", String)
    proto_addr_type = fields.TypedField("Proto_Addr_Type", String)
    hardware_addr_size = fields.TypedField("Hardware_Addr_Size", HexBinary)
    proto_addr_size = fields.TypedField("Proto_Addr_Size", HexBinary)
    op_type = fields.TypedField("Op_Type", String)
    sender_hardware_addr = fields.TypedField("Sender_Hardware_Addr", Address)
    sender_protocol_addr = fields.TypedField("Sender_Protocol_Addr", Address)
    recip_hardware_addr = fields.TypedField("Recip_Hardware_Addr", Address)
    recip_protocol_addr = fields.TypedField("Recip_Protocol_Addr", Address)


class _ICMPHeader(entities.Entity):
    """Abstract Type"""
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    type_ = fields.TypedField("Type", HexBinary)
    code = fields.TypedField("Code", HexBinary)
    checksum = fields.TypedField("Checksum", HexBinary)


class ICMPv4Header(_ICMPHeader):
    _binding_class = network_packet_binding.ICMPv4HeaderType


class ICMPv6Header(_ICMPHeader):
    _binding_class = network_packet_binding.ICMPv6HeaderType


class NDPLinkAddr(entities.Entity):
    """Abstract Type"""
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPLinkAddrType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = fields.TypedField("Length", HexBinary)
    link_layer_mac_addr = fields.TypedField("Link_Layer_MAC_Addr", Address)


class RouterSolicitationOptions(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterSolicitationOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_link_addr = fields.TypedField("Src_Link_Addr", NDPLinkAddr)


class RouterSolicitation(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterSolicitationType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    options = fields.TypedField("Options", RouterSolicitationOptions,
                               multiple=True)


class NDPMTU(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPMTUType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = fields.TypedField("Length", Integer)
    mtu = fields.TypedField("MTU", Integer)


class Prefix(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PrefixType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    ipv6_addr = fields.TypedField("IPv6_Addr", Address)
    ip_addr_prefix = fields.TypedField("IP_Addr_Prefix", Address)


class NDPPrefixInfo(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPPrefixInfoType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    link_flag = fields.TypedField("link_flag")
    addr_config_flag = fields.TypedField("addr_config_flag")
    length = fields.TypedField("Length", HexBinary)
    prefix_length = fields.TypedField("Prefix_Length", Integer)
    valid_lifetime = fields.TypedField("Valid_Lifetime", Integer)
    preferred_lifetime = fields.TypedField("Preferred_Lifetime", Integer)
    prefix = fields.TypedField("Prefix", Prefix)


class RouterAdvertisementOptions(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterAdvertisementOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    src_link_addr = fields.TypedField("Src_Link_Addr", NDPLinkAddr)
    mtu = fields.TypedField("MTU", NDPMTU)
    prefix_info = fields.TypedField("Prefix_Info", NDPPrefixInfo)


class RouterAdvertisement(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RouterAdvertisementType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    managed_address_config_flag = \
            fields.TypedField("managed_address_config_flag")
    other_config_flag = fields.TypedField("other_config_flag")
    cur_hop_limit = fields.TypedField("Cur_Hop_Limit", Integer)
    router_lifetime = fields.TypedField("Router_Lifetime", Integer)
    reachable_time = fields.TypedField("Reachable_Time", Integer)
    retrans_timer = fields.TypedField("Retrans_Timer", Integer)
    options = fields.TypedField("Options", RouterAdvertisementOptions)


class NeighborSolicitationOptions(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborSolicitationOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_link_addr = fields.TypedField("Src_Link_Addr", NDPLinkAddr)


class NeighborSolicitation(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborSolicitationType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_ipv6_addr = fields.TypedField("Target_IPv6_Addr", Address)
    options = fields.TypedField("Options", NeighborSolicitationOptions)


class NeighborOptions(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_link_addr = fields.TypedField("Target_Link_Addr", NDPLinkAddr)


class NeighborAdvertisement(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NeighborAdvertisementType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    router_flag = fields.TypedField("router_flag")
    solicited_flag = fields.TypedField("solicited_flag")
    override_flag = fields.TypedField("override_flag")
    target_ipv6_addr = fields.TypedField("Target_IPv6_Addr", Address)
    options = fields.TypedField("Options", NeighborOptions)


class NDPRedirectedHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPRedirectedHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    length = fields.TypedField("Length", HexBinary)
    ipheader_and_data = fields.TypedField("IPHeader_And_Data", HexBinary)


class RedirectOptions(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RedirectOptionsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_link_addr = fields.TypedField("Target_Link_Addr", NDPLinkAddr)
    redirected_header = fields.TypedField("Redirected_Header",
                                          NDPRedirectedHeader)


class Redirect(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RedirectType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    target_ipv6_addr = fields.TypedField("Target_IPv6_Addr", Address)
    dest_ipv6_addr = fields.TypedField("Dest_IPv6_Addr", Address)
    options = fields.TypedField("Options", RedirectOptions)


class NDP(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NDPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv6_header = fields.TypedField("ICMPv6_Header", ICMPv6Header)

    #TODO: choice between these 5
    router_solicitation = fields.TypedField("Router_Solicitation",
                                           RouterSolicitation)
    router_advertisement = fields.TypedField("Router_Advertisement",
                                            RouterAdvertisement)
    neighbor_solicitation = fields.TypedField("Neighbor_Solicitation",
                                             NeighborSolicitation)
    neighbor_advertisement = fields.TypedField("Neighbor_Advertisement",
                                              NeighborAdvertisement)
    redirect = fields.TypedField("Redirect", Redirect)


class LogicalProtocol(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.LogicalProtocolType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    arp_rarp = fields.TypedField("ARP_RARP", ARP)
    ndp = fields.TypedField("NDP", NDP)


class LinkLayer(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.LinkLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    physical_interface = fields.TypedField("Physical_Interface", PhysicalInterface)
    logical_protocols = fields.TypedField("Logical_Protocols", LogicalProtocol)


class IPv4Flags(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4FlagsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    reserved = fields.TypedField("Reserved", Integer)
    do_not_fragment = fields.TypedField("Do_Not_Fragment", String)
    more_fragments = fields.TypedField("More_Fragments", String)

    def __init__(self):
        super(IPv4Flags, self).__init__()
        self.reserved = Integer(0)


class IPv4Option(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4OptionType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    copy_flag = fields.TypedField("Copy_Flag", String)
    class_ = fields.TypedField("Class", String)
    option = fields.TypedField("Option", String)


class IPv4Header(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4HeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_version = fields.TypedField("IP_Version", String)
    header_length = fields.TypedField("Header_Length", Integer)
    dscp = fields.TypedField("DSCP", HexBinary)
    ecn = fields.TypedField("ECN", HexBinary)
    total_length = fields.TypedField("Total_Length", HexBinary)
    identification = fields.TypedField("Identification", PositiveInteger)
    flags = fields.TypedField("Flags", IPv4Flags)
    fragment_offset = fields.TypedField("Fragment_Offset", HexBinary)
    ttl = fields.TypedField("TTL", HexBinary)
    protocol = fields.TypedField("Protocol", String)
    checksum = fields.TypedField("Checksum", HexBinary)
    src_ipv4_addr = fields.TypedField("Src_IPv4_Addr", Address)
    dest_ipv4_addr = fields.TypedField("Dest_IPv4_Addr", Address)
    option = fields.TypedField("Option", IPv4Option, multiple=True)


class IPv4Packet(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv4PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ipv4_header = fields.TypedField("IPv4_Header", IPv4Header)
    data = fields.TypedField("Data", HexBinary)


class FragmentationRequired(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentationRequiredType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    fragmentation_required = fields.TypedField("Fragmentation_Required")
    next_hop_mtu = fields.TypedField("Next_Hop_MTU", HexBinary)


class ICMPv4DestinationUnreachable(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4DestinationUnreachableType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    destination_network_unreachable = \
            fields.TypedField("Destination_Network_Unreachable")
    destination_host_unreachable = \
            fields.TypedField("Destination_Host_Unreachable")
    destination_protocol_unreachable = \
            fields.TypedField("Destination_Protocol_Unreachable")
    destination_port_unreachable = \
            fields.TypedField("Destination_Port_Unreachable")
    fragmentation_required = fields.TypedField("Fragmentation_Required",
                                             FragmentationRequired)
    source_route_failed = fields.TypedField("Source_Route_Failed")
    destination_network_unknown = \
            fields.TypedField("Destination_Network_Unknown")
    destination_host_unknown = fields.TypedField("Destination_Host_Unknown")
    source_host_isolated = fields.TypedField("Source_Host_Isolated")
    network_administratively_prohibited = \
            fields.TypedField("Network_Administratively_Prohibited")
    host_administratively_prohibited = \
            fields.TypedField("Host_Administratively_Prohibited")
    network_unreachable_for_tos = \
            fields.TypedField("Network_Unreachable_For_TOS")
    host_unreachable_for_tos = \
            fields.TypedField("Host_Unreachable_For_TOS")
    communication_administratively_prohibited = \
            fields.TypedField("Communication_Administratively_Prohibited")
    host_precedence_violation = fields.TypedField("Host_Precedence_Violation")
    precedence_cutoff_in_effect = \
            fields.TypedField("Precedence_Cutoff_In_Effect")


class ICMPv4SourceQuench(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4SourceQuenchType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    source_quench = fields.TypedField("Source_Quench")


class ICMPv4RedirectMessage(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4RedirectMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice of first 4
    network_redirect = fields.TypedField("Network_Redirect")
    host_redirect = fields.TypedField("Host_Redirect")
    tos_network_redirect = fields.TypedField("ToS_Network_Redirect")
    tos_host_redirect = fields.TypedField("ToS_Host_Redirect")

    ip_address = fields.TypedField("IP_Address", Address)


class ICMPv4TimeExceeded(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimeExceededType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    # TODO: choice
    ttl_exceeded_in_transit = fields.TypedField("TTL_Exceeded_In_Transit")
    frag_reassembly_time_exceeded = \
            fields.TypedField("Frag_Reassembly_Time_Exceeded")


class ICMPv4ErrorMessageContent(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4ErrorMessageContentType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_header = fields.TypedField("IP_Header", IPv4Header)
    first_eight_bytes = fields.TypedField("First_Eight_Bytes", HexBinary)


class ICMPv4ErrorMessage(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4ErrorMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_unreachable = fields.TypedField("Destination_Unreachable",
                                                ICMPv4DestinationUnreachable)
    source_quench = fields.TypedField("Source_Quench", ICMPv4SourceQuench)
    redirect_message = fields.TypedField("Redirect_Message",
                                        ICMPv4RedirectMessage)
    time_exceeded = fields.TypedField("Time_Exceeded", ICMPv4TimeExceeded)
    error_msg_content = fields.TypedField("Error_Msg_Content",
                                        ICMPv4ErrorMessageContent)


class _ICMPEchoReply(entities.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    echo_reply = fields.TypedField("Echo_Reply")
    data = fields.TypedField("Data", HexBinary)


class _ICMPEchoRequest(entities.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    echo_request = fields.TypedField("Echo_Request")
    data = fields.TypedField("Data", HexBinary)


class ICMPv4EchoReply(_ICMPEchoReply):
    _binding_class = network_packet_binding.ICMPv4EchoReplyType


class ICMPv4EchoRequest(_ICMPEchoRequest):
    _binding_class = network_packet_binding.ICMPv4EchoRequestType


class ICMPv6EchoReply(_ICMPEchoReply):
    _binding_class = network_packet_binding.ICMPv6EchoReplyType


class ICMPv6EchoRequest(_ICMPEchoRequest):
    _binding_class = network_packet_binding.ICMPv6EchoRequestType


class ICMPv4TimestampRequest(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimestampRequestType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    timestamp = fields.TypedField("Timestamp")
    originate_timestamp = fields.TypedField("Originate_Timestamp",
                                           UnsignedInteger)


class ICMPv4TimestampReply(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TimestampReplyType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    timestamp_reply = fields.TypedField("Timestamp_Reply")
    originate_timestamp = fields.TypedField("Originate_Timestamp",
                                           UnsignedInteger)
    receive_timestamp = fields.TypedField("Receive_Timestamp",
                                         UnsignedInteger)
    transmit_timestamp = fields.TypedField("Transmit_Timestamp",
                                          UnsignedInteger)


class ICMPv4AddressMaskRequest(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4AddressMaskRequestType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    address_mask_request = fields.TypedField("Address_Mask_Request")
    address_mask = fields.TypedField("Address_Mask", Address)


class ICMPv4AddressMaskReply(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4AddressMaskReplyType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    address_mask_reply = fields.TypedField("Address_Mask_Reply")
    address_mask = fields.TypedField("Address_Mask", Address)


class _ICMPInfoMessageContent(entities.Entity):
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    identifier = fields.TypedField("Identifier", HexBinary)
    sequence_number = fields.TypedField("Sequence_Number", HexBinary)


class ICMPv4InfoMessageContent(_ICMPInfoMessageContent):
    _binding_class = network_packet_binding.ICMPv4InfoMessageContentType


class ICMPv6InfoMessageContent(_ICMPInfoMessageContent):
    _binding_class = network_packet_binding.ICMPv6InfoMessageContentType


class ICMPv4InfoMessage(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4InfoMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 6
    echo_reply = fields.TypedField("Echo_Reply", ICMPv4EchoReply)
    echo_request = fields.TypedField("Echo_Request", ICMPv4EchoRequest)
    timestamp_request = fields.TypedField("Timestamp_Request",
                                         ICMPv4TimestampRequest)
    timestamp_reply = fields.TypedField("Timestamp_Reply", ICMPv4TimestampReply)
    address_mask_request = fields.TypedField("Address_Mask_Request",
                                            ICMPv4AddressMaskRequest)
    address_mask_reply = fields.TypedField("Address_Mask_Reply",
                                          ICMPv4AddressMaskReply)

    info_msg_content = fields.TypedField("Info_Msg_Content",
                                        ICMPv4InfoMessageContent)


class ICMPv4Traceroute(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4TracerouteType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    outbound_packet_forward_success = \
            fields.TypedField("Outbound_Packet_Forward_Success")
    outbound_packet_no_route = fields.TypedField("Outbound_Packet_no_Route")
    identifier = fields.TypedField("Identifier", HexBinary)
    outbound_hop_count = fields.TypedField("Outbound_Hop_Count", HexBinary)
    return_hop_count = fields.TypedField("Return_Hop_Count", HexBinary)
    output_link_speed = fields.TypedField("Output_Link_Speed", HexBinary)
    output_link_mtu = fields.TypedField("Output_Link_MTU", HexBinary)


class ICMPv4Packet(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv4PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv4_header = fields.TypedField("ICMPv4_Header", ICMPv4Header)

    # TODO: choice between these 3
    error_msg = fields.TypedField("Error_Msg", ICMPv4ErrorMessage)
    info_msg = fields.TypedField("Info_Msg", ICMPv4InfoMessage)
    traceroute = fields.TypedField("Traceroute", ICMPv4Traceroute)


class IPv6Header(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6HeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ip_version = fields.TypedField("IP_Version", String)
    traffic_class = fields.TypedField("Traffic_Class", HexBinary)
    flow_label = fields.TypedField("Flow_Label", HexBinary)
    payload_length = fields.TypedField("Payload_Length", HexBinary)
    next_header = fields.TypedField("Next_Header", String)
    ttl = fields.TypedField("TTL", HexBinary)
    src_ipv6_addr = fields.TypedField("Src_IPv6_Addr", Address)
    dest_ipv6_addr = fields.TypedField("Dest_IPv6_Addr", Address)


class IPv6Option(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6OptionType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    do_not_recogn_action = fields.TypedField("Do_Not_Recogn_Action", String)
    packet_change = fields.TypedField("Packet_Change", String)
    option_byte = fields.TypedField("Option_Byte", HexBinary)


class Pad1(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.Pad1Type
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    octet = fields.TypedField("Octet", HexBinary)


class PadN(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.PadNType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    octet = fields.TypedField("Octet", HexBinary)
    option_data_length = fields.TypedField("Option_Data_Length", Integer)
    option_data = fields.TypedField("Option_Data", Integer)


class OptionData(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.OptionDataType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    option_type = fields.TypedField("Option_Type", IPv6Option)
    option_data_len = fields.TypedField("Option_Data_Len", HexBinary)

    #TODO: choice
    pad1 = fields.TypedField("Pad1", Pad1)
    padn = fields.TypedField("PadN", PadN)


class _IPv6ExtHeader(entities.Entity):
    """Shared by a couple types"""
    _binding = network_packet_binding
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = fields.TypedField("Next_Header", String)
    header_ext_len = fields.TypedField("Header_Ext_Len", HexBinary)
    option_data = fields.TypedField("Option_Data", OptionData, multiple=True)


class HopByHopOptions(_IPv6ExtHeader):
    _binding_class = network_packet_binding.HopByHopOptionsType


class Routing(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.RoutingType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = fields.TypedField("Next_Header", String)
    header_ext_len = fields.TypedField("Header_Ext_Len", Integer)
    routing_type = fields.TypedField("Routing_Type", HexBinary)
    segments_left = fields.TypedField("Segments_Left", Integer)
    type_specific_data = fields.TypedField("Type_Specific_Data", String)


class FragmentHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = fields.TypedField("Next_Header", HexBinary)
    fragment_offset = fields.TypedField("Fragment_Offset", HexBinary)
    m_flag = fields.TypedField("M_Flag", String)
    identification = fields.TypedField("Identification", HexBinary)


class Fragment(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.FragmentType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    fragment_header = fields.TypedField("Fragment_Header", FragmentHeader)
    fragment = fields.TypedField("Fragment", HexBinary)


class DestinationOptions(_IPv6ExtHeader):
    _binding_class = network_packet_binding.DestinationOptionsType


class AuthenticationHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.AuthenticationHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    next_header = fields.TypedField("Next_Header", String)
    header_ext_len = fields.TypedField("Header_Ext_Len", HexBinary)
    security_parameters_index = fields.TypedField("Security_Parameters_Index",
                                                 HexBinary)
    sequence_number = fields.TypedField("Sequence_Number", HexBinary)
    authentication_data = fields.TypedField("Authentication_Data", HexBinary)


class EncapsulatingSecurityPayload(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.EncapsulatingSecurityPayloadType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    security_parameters_index = fields.TypedField("Security_Parameters_Index",
                                                 HexBinary)
    sequence_number = fields.TypedField("Sequence_Number", HexBinary)
    payload_data = fields.TypedField("Payload_Data", HexBinary)
    padding = fields.TypedField("Padding", HexBinary)
    padding_len = fields.TypedField("Padding_Len", HexBinary)
    next_header = fields.TypedField("Next_Header", String)
    authentication_data = fields.TypedField("Authentication_Data", HexBinary)


class IPv6ExtHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6ExtHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    hop_by_hop_options = fields.TypedField("Hop_by_Hop_Options", HopByHopOptions)
    routing = fields.TypedField("Routing", Routing)
    fragment = fields.TypedField("Fragment", Fragment)
    destination_options = fields.TypedField("Destination_Options", DestinationOptions, multiple=True)
    authentication_header = fields.TypedField("Authentication_Header", AuthenticationHeader)
    encapsulating_security_payload = fields.TypedField("Encapsulating_Security_Payload", EncapsulatingSecurityPayload)


class IPv6Packet(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.IPv6PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ipv6_header = fields.TypedField("IPv6_Header", IPv6Header)
    data = fields.TypedField("Data", HexBinary)
    ext_headers = fields.TypedField("Ext_Headers", IPv6ExtHeader, multiple=True)


class ICMPv6DestinationUnreachable(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6DestinationUnreachableType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    no_route = fields.TypedField("No_Route")
    comm_prohibited = fields.TypedField("Comm_Prohibited")
    beyond_scope = fields.TypedField("Beyond_Scope")
    address_unreachable = fields.TypedField("Address_Unreachable")
    port_unreachable = fields.TypedField("Port_Unreachable")
    src_addr_failed_policy = fields.TypedField("Src_Addr_Failed_Policy")
    reject_route = fields.TypedField("Reject_Route")


class ICMPv6PacketTooBig(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6PacketTooBigType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    packet_too_big = fields.TypedField("Packet_Too_Big")
    mtu = fields.TypedField("MTU", HexBinary)


class ICMPv6TimeExceeded(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6TimeExceededType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    hop_limit_exceeded = fields.TypedField("Hop_Limit_Exceeded")
    fragment_reassem_time_exceeded = \
            fields.TypedField("Fragment_Reassem_Time_Exceeded")


class ICMPv6ParameterProblem(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6ParameterProblemType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 3
    erroneous_header_field = fields.TypedField("Erroneous_Header_Field")
    unrecognized_next_header_type = \
            fields.TypedField("Unrecognized_Next_Header_Type")
    unrecognized_ipv6_option = fields.TypedField("Unrecognized_IPv6_Option")

    pointer = fields.TypedField("Pointer", HexBinary)


class ICMPv6ErrorMessage(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6ErrorMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    destination_unreachable = fields.TypedField("Destination_Unreachable",
                                                ICMPv6DestinationUnreachable)
    packet_too_big = fields.TypedField("Packet_Too_Big", ICMPv6PacketTooBig)
    time_exceeded = fields.TypedField("Time_Exceeded", ICMPv6TimeExceeded)
    parameter_problem = fields.TypedField("Parameter_Problem",
                                         ICMPv6ParameterProblem)
    invoking_packet = fields.TypedField("Invoking_Packet", HexBinary)


class ICMPv6InfoMessage(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6InfoMessageType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice of first 2
    echo_request = fields.TypedField("Echo_Request", ICMPv6EchoRequest)
    echo_reply = fields.TypedField("Echo_Reply", ICMPv6EchoReply)

    info_msg_content = fields.TypedField("Info_Msg_Content",
                                        ICMPv6InfoMessageContent)


class ICMPv6Packet(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.ICMPv6PacketType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    icmpv6_header = fields.TypedField("ICMPv6_Header", ICMPv6Header)
    error_msg = fields.TypedField("Error_Msg", ICMPv6ErrorMessage)
    info_msg = fields.TypedField("Info_Msg", ICMPv6InfoMessage)


class InternetLayer(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.InternetLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    #TODO: choice
    ipv4 = fields.TypedField("IPv4", IPv4Packet)
    icmpv4 = fields.TypedField("ICMPv4", ICMPv4Packet)
    ipv6 = fields.TypedField("IPv6", IPv6Packet)
    icmpv6 = fields.TypedField("ICMPv6", ICMPv6Packet)


class TCPFlags(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPFlagsType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    ns = fields.TypedField("ns")
    cwr = fields.TypedField("cwr")
    ece = fields.TypedField("ece")
    urg = fields.TypedField("urg")
    ack = fields.TypedField("ack")
    psh = fields.TypedField("psh")
    rst = fields.TypedField("rst")
    syn = fields.TypedField("syn")
    fin = fields.TypedField("fin")


class TCPHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    src_port = fields.TypedField("Src_Port", Port)
    dest_port = fields.TypedField("Dest_Port", Port)
    seq_num = fields.TypedField("Seq_Num", HexBinary)
    ack_num = fields.TypedField("ACK_Num", HexBinary)
    data_offset = fields.TypedField("Data_Offset", HexBinary)
    reserved = fields.TypedField("Reserved", Integer)
    tcp_flags = fields.TypedField("TCP_Flags", TCPFlags)
    window = fields.TypedField("Window", HexBinary)
    checksum = fields.TypedField("Checksum", HexBinary)
    urg_ptr = fields.TypedField("Urg_Ptr", HexBinary)


class TCP(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TCPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    tcp_header = fields.TypedField("TCP_Header", TCPHeader)
    options = fields.TypedField("Options", HexBinary)
    data = fields.TypedField("Data", DataSegment)


class UDPHeader(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.UDPHeaderType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    srcport = fields.TypedField("SrcPort", Port)
    destport = fields.TypedField("DestPort", Port)
    length = fields.TypedField("Length", Integer)
    checksum = fields.TypedField("Checksum", HexBinary)


class UDP(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.UDPType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    udp_header = fields.TypedField("UDP_Header", UDPHeader)
    data = fields.TypedField("Data", DataSegment)


class TransportLayer(entities.Entity):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.TransportLayerType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"

    tcp = fields.TypedField("TCP", TCP)
    udp = fields.TypedField("UDP", UDP)


class NetworkPacket(ObjectProperties):
    _binding = network_packet_binding
    _binding_class = network_packet_binding.NetworkPacketObjectType
    _namespace = "http://cybox.mitre.org/objects#PacketObject-2"
    _XSI_NS = "PacketObj"
    _XSI_TYPE = "NetworkPacketObjectType"

    link_layer = fields.TypedField("Link_Layer", LinkLayer)
    internet_layer = fields.TypedField("Internet_Layer", InternetLayer)
    transport_layer = fields.TypedField("Transport_Layer", TransportLayer)
