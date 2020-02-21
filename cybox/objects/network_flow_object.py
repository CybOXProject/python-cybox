# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.network_flow_object as network_flow_binding
from cybox.common import (
    BaseProperty, HexBinary, Integer, ObjectProperties, PlatformSpecification,
    PositiveInteger, String
)
from cybox.objects.address_object import Address
from cybox.objects.network_packet_object import TCPFlags
from cybox.objects.socket_address_object import SocketAddress


class NetflowV5FlowRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV5FlowRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    nexthop_ipv4_addr = fields.TypedField("Nexthop_IPv4_Addr", Address)
    packet_count = fields.TypedField("Packet_Count", Integer)
    byte_count = fields.TypedField("Byte_Count", Integer)
    sysuptime_start = fields.TypedField("SysUpTime_Start", Integer)
    sysuptime_end = fields.TypedField("SysUpTime_End", Integer)
    padding1 = fields.TypedField("Padding1", HexBinary)
    tcp_flags = fields.TypedField("TCP_Flags", HexBinary)
    src_autonomous_system = fields.TypedField("Src_Autonomous_System", Integer)
    dest_autonomous_system = fields.TypedField("Dest_Autonomous_System", Integer)
    src_ip_mask_bit_count = fields.TypedField("Src_IP_Mask_Bit_Count", String)
    dest_ip_mask_bit_count = fields.TypedField("Dest_IP_Mask_Bit_Count", String)
    padding2 = fields.TypedField("Padding2", HexBinary)


class NetflowV5FlowHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV5FlowHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    version = fields.TypedField("Version", HexBinary)
    count = fields.TypedField("Count", Integer)
    sys_up_time = fields.TypedField("Sys_Up_Time", Integer)
    unix_secs = fields.TypedField("Unix_Secs", Integer)
    unix_nsecs = fields.TypedField("Unix_Nsecs", Integer)
    flow_sequence = fields.TypedField("Flow_Sequence", Integer)
    engine_type = fields.TypedField("Engine_Type", String)
    engine_id = fields.TypedField("Engine_ID", Integer)
    sampling_interval = fields.TypedField("Sampling_Interval", HexBinary)

    def __init__(self):
        super(NetflowV5FlowHeader, self).__init__()
        self.version = "05"


class NetflowV5Packet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV5PacketType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_header = fields.TypedField("Flow_Header", NetflowV5FlowHeader)
    flow_record = fields.TypedField("Flow_Record", NetflowV5FlowRecord, multiple=True)


class NetflowV9PacketHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9PacketHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    version = fields.TypedField("Version", HexBinary)
    record_count = fields.TypedField("Record_Count", Integer)
    sys_up_time = fields.TypedField("Sys_Up_Time", Integer)
    unix_secs = fields.TypedField("Unix_Secs", Integer)
    sequence_number = fields.TypedField("Sequence_Number", Integer)
    source_id = fields.TypedField("Source_ID", HexBinary)

    def __init__(self, version=None):
        super(NetflowV9PacketHeader, self).__init__()
        self.version = version or "09"


class NetflowV9ScopeField(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9ScopeFieldType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_SYSTEM = "System(1)"
    TERM_INTERFACE = "Interface(2)"
    TERM_LINE_CARD = "LineCard(3)"
    TERM_CACHE = "Cache(4)"
    TERM_TEMPLATE = "Template(5)"


class NetflowV9Field(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9FieldType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_IN_BYTES = "IN_BYTES(1)"
    TERM_IN_PKTS = "IN_PKTS(2)"
    TERM_FLOWS = "FLOWS(3)"
    TERM_PROTOCOL = "PROTOCOL(4)"
    TERM_TOS = "SRC_TOS(5)"
    TERM_TCP_FLAGS = "TCP_FLAGS(6)"
    TERM_L4_SRC_PORT = "L4_SRC_PORT(7)"
    TERM_IPV4_SRC_ADDR = "IPV4_SRC_ADDR(8)"
    TERM_SRC_MASK = "SRC_MASK(9)"
    TERM_INPUT_SNMP = "INPUT_SNMP(10)"
    TERM_L4_DST_PORT= "L4_DST_PORT(11)"
    TERM_IPV4_DST_ADDR = "IPV4_DST_ADDR(12)"
    TERM_DST_MASK= "DST_MASK(13)"
    TERM_OUTPUT_SNMP = "OUTPUT_SNMP(14)"
    TERM_IPV4_NEXT_HOP = "IPV4_NEXT_HOP(15)"
    TERM_SRC_AS = "SRC_AS(16)"
    TERM_DST_AS = "DST_AS(17)"
    TERM_BGP_IPV4_NEXT_HOP = "BGP_IPV4_NEXT_HOP(18)"
    TERM_MUL_DST_PKTS = "MUL_DST_PKTS(19)"
    TERM_MUL_DST_BYTES = "MUL_DST_BYTES(20)"


class NetflowV9TemplateRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9TemplateRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_id = fields.TypedField("Template_ID", Integer)
    field_count = fields.TypedField("Field_Count", Integer)
    field_type = fields.TypedField("Field_Type", NetflowV9Field)
    field_length = fields.TypedField("Field_Length", HexBinary)


class NetflowV9TemplateFlowSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9TemplateFlowSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_set_id = fields.TypedField("Flow_Set_ID", HexBinary)
    length = fields.TypedField("Length", Integer)
    template_record = fields.TypedField("Template_Record", NetflowV9TemplateRecord, multiple=True)

    def __init__(self):
        super(NetflowV9TemplateFlowSet, self).__init__()
        self.flow_set_id = "00"


class NetflowV9OptionsTemplateRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9OptionsTemplateRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_id = fields.TypedField("Template_ID", Integer)
    option_scope_length = fields.TypedField("Option_Scope_Length", HexBinary)
    option_length = fields.TypedField("Option_Length", HexBinary)
    scope_field_type = fields.TypedField("Scope_Field_Type", NetflowV9ScopeField)
    scope_field_length = fields.TypedField("Scope_Field_Length", HexBinary)
    option_field_type = fields.TypedField("Option_Field_Type", NetflowV9Field)
    option_field_length = fields.TypedField("Option_Field_Length", HexBinary)


class NetflowV9OptionsTemplateFlowSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9OptionsTemplateFlowSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_set_id = fields.TypedField("Flow_Set_ID", HexBinary)
    length = fields.TypedField("Length", Integer)
    options_template_record = fields.TypedField("Options_Template_Record", NetflowV9OptionsTemplateRecord, multiple=True)
    padding = fields.TypedField("Padding", HexBinary)

    def __init__(self):
        super(NetflowV9OptionsTemplateFlowSet, self).__init__()
        self.flow_set_id = "01"


class FlowCollectionElement(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.FlowCollectionElementType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_record_field_value = fields.TypedField("Flow_Record_Field_Value", String, multiple=True)


class FlowDataRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.FlowDataRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_record_collection_element = fields.TypedField("Flow_Record_Collection_Element", FlowCollectionElement, multiple=True)


class OptionCollectionElement(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.OptionCollectionElementType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    option_record_field_value = fields.TypedField("Option_Record_Field_Value", String, multiple=True)


class OptionsDataRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.OptionsDataRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    scope_field_value = fields.TypedField("Scope_Field_Value", String)
    option_record_collection_element = fields.TypedField("Option_Record_Collection_Element", OptionCollectionElement, multiple=True)


class NetflowV9DataRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9DataRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_data_record = fields.TypedField("Flow_Data_Record", FlowDataRecord, multiple=True)
    options_data_record = fields.TypedField("Options_Data_Record", OptionsDataRecord, multiple=True)


class NetflowV9DataFlowSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9DataFlowSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_set_id_template_id = fields.TypedField("Flow_Set_ID_Template_ID", Integer)
    length = fields.TypedField("Length", Integer)
    data_record = fields.TypedField("Data_Record", NetflowV9DataRecord, multiple=True)
    padding = fields.TypedField("Padding", HexBinary)


class NetflowV9FlowSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9FlowSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_flow_set = fields.TypedField("Template_Flow_Set", NetflowV9TemplateFlowSet)
    options_template_flow_set = fields.TypedField("Options_Template_Flow_Set", NetflowV9OptionsTemplateFlowSet)
    data_flow_set = fields.TypedField("Data_Flow_Set", NetflowV9DataFlowSet)


class NetflowV9ExportPacket(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetflowV9ExportPacketType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_header = fields.TypedField("Packet_Header", NetflowV9PacketHeader)
    flow_set = fields.TypedField("Flow_Set", NetflowV9FlowSet, multiple=True)


class SiLKSensorDirection(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKDirectionType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_IN = "in"
    TERM_IN_WEB = "inweb"
    TERM_IN_NULL = "innull"
    TERM_OUT = "out"
    TERM_OUT_WEB = "outweb"
    TERM_OUT_NULL = "outnull"


class SiLKSensorClass(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKSensorClassType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_ALL = "all"


class SiLKCountryCode(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKCountryCodeType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"


class SiLKAddress(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKAddressType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_NON_ROUTABLE = "non-routable (0)"
    TERM_INTERNAL = "internal(1)"
    TERM_EXTERNAL = "routable_external(2)"


class SiLKFlowAttributes(BaseProperty):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKAddressType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    TERM_F = "F (FIN flag)"
    TERM_T = "T (Timeout)"
    TERM_C = "C (Continuation)"


class SiLKSensorInfo(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKSensorInfoType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    sensor_id = fields.TypedField("Sensor_ID", String)
    class_ = fields.TypedField("Class", SiLKSensorClass)
    type_ = fields.TypedField("Type", SiLKSensorDirection)


class SiLKRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.SiLKRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    packet_count = fields.TypedField("Packet_Count", Integer)
    byte_count = fields.TypedField("Byte_Count", Integer)
    tcp_flags = fields.TypedField("TCP_Flags", HexBinary)
    start_time = fields.TypedField("Start_Time", Integer)
    duration = fields.TypedField("Duration", Integer)
    end_time = fields.TypedField("End_Time", Integer)
    sensor_info = fields.TypedField("Sensor_Info", SiLKSensorInfo)
    icmp_type = fields.TypedField("ICMP_Type", Integer)
    icmp_code = fields.TypedField("ICMP_Code", Integer)
    router_next_hop_ip = fields.TypedField("Router_Next_Hop_IP", Address)
    initial_tcp_flags = fields.TypedField("Initial_TCP_Flags", TCPFlags)
    session_tcp_flags = fields.TypedField("Session_TCP_Flags", HexBinary)
    flow_attributes = fields.TypedField("Flow_Attributes", SiLKFlowAttributes)
    flow_application = fields.TypedField("Flow_Application", String)
    src_ip_type = fields.TypedField("Src_IP_Type", SiLKAddress)
    dest_ip_type = fields.TypedField("Dest_IP_Type", SiLKAddress)
    src_country_code = fields.TypedField("Src_Country_Code", SiLKCountryCode)
    dest_country_code = fields.TypedField("Dest_Country_Code", SiLKCountryCode)
    src_mapname = fields.TypedField("Src_MAPNAME", String)
    dest_mapname = fields.TypedField("Dest_MAPNAME", String)


class IPFIXMessageHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXMessageHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    version = fields.TypedField("Version", HexBinary)
    byte_length = fields.TypedField("Byte_Length", HexBinary)
    export_timestamp = fields.TypedField("Export_Timestamp", Integer)
    sequence_number = fields.TypedField("Sequence_Number", Integer)
    observation_domain_id = fields.TypedField("Observation_Domain_ID", Integer)

    def __init__(self):
        super(IPFIXMessageHeader, self).__init__()
        self.version = "0a"


class IPFIXSetHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXSetHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    set_id = fields.TypedField("Set_ID", Integer)
    length = fields.TypedField("Length", Integer)


class IPFIXTemplateRecordHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXTemplateRecordHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_id = fields.TypedField("Template_ID", Integer)
    field_count = fields.TypedField("Field_Count", HexBinary)


class IPFIXTemplateRecordFieldSpecifiers(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXTemplateRecordFieldSpecifiersType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    enterprise_bit = fields.TypedField("Enterprise_Bit")
    information_element_id = fields.TypedField("Information_Element_ID", String)
    field_length = fields.TypedField("Field_Length", String)
    enterprise_number = fields.TypedField("Enterprise_Number", String)


class IPFIXTemplateRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXTemplateRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_record_header = fields.TypedField("Template_Record_Header", IPFIXTemplateRecordHeader)
    field_specifier = fields.TypedField("Field_Specifier", IPFIXTemplateRecordFieldSpecifiers, multiple=True)


class IPFIXTemplateSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXTemplateSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    set_header = fields.TypedField("Set_Header", IPFIXSetHeader)
    template_record = fields.TypedField("Template_Record", IPFIXTemplateRecord, multiple=True)
    padding = fields.TypedField("Padding", HexBinary)


class IPFIXOptionsTemplateRecordHeader(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXOptionsTemplateRecordHeaderType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_id = fields.TypedField("Template_ID", Integer)
    field_count = fields.TypedField("Field_Count", HexBinary)
    scope_field_count = fields.TypedField("Scope_Field_Count", PositiveInteger)


class IPFIXOptionsTemplateRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXOptionsTemplateRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    options_template_record_header = fields.TypedField("Options_Template_Record_Header", IPFIXOptionsTemplateRecordHeader)
    field_specifier = fields.TypedField("Field_Specifier", IPFIXTemplateRecordFieldSpecifiers, multiple=True)


class IPFIXOptionsTemplateSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXOptionsTemplateSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    set_header = fields.TypedField("Set_Header", IPFIXSetHeader)
    options_template_record = fields.TypedField("Options_Template_Record", IPFIXOptionsTemplateRecord, multiple=True)
    padding = fields.TypedField("Padding", HexBinary)


class IPFIXDataRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXDataRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    field_value = fields.TypedField("Field_Value", String, multiple=True)


class IPFIXDataSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXDataSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    set_header = fields.TypedField("Set_Header", IPFIXSetHeader)
    data_record = fields.TypedField("Data_Record", IPFIXDataRecord, multiple=True)
    padding = fields.TypedField("Padding", HexBinary)


class IPFIXSet(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXSetType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    template_set = fields.TypedField("Template_Set", IPFIXTemplateSet)
    options_template_set = fields.TypedField("Options_Template_Set", IPFIXOptionsTemplateSet)
    data_set = fields.TypedField("Data_Set", IPFIXDataSet)


class IPFIXMessage(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.IPFIXMessageType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    message_header = fields.TypedField("Message_Header", IPFIXMessageHeader)
    set_ = fields.TypedField("Set", IPFIXSet, multiple=True)


class UnidirectionalRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.UnidirectionalRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    ipfix_message = fields.TypedField("IPFIX_Message", IPFIXMessage)
    netflowv9_export_packet = fields.TypedField("NetflowV9_Export_Packet", NetflowV9ExportPacket)
    netflowv5_packet = fields.TypedField("NetflowV5_Packet", NetflowV5Packet)
    silk_record = fields.TypedField("SiLK_Record", SiLKRecord)


class NetworkLayerInfo(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetworkLayerInfoType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    src_socket_address = fields.TypedField("Src_Socket_Address", SocketAddress)
    dest_socket_address = fields.TypedField("Dest_Socket_Address", SocketAddress)
    ip_protocol = fields.TypedField("IP_Protocol", String)


class NetworkFlowLabel(NetworkLayerInfo):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetworkFlowLabelType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    ingress_interface_index = fields.TypedField("Ingress_Interface_Index", Integer)
    egress_interface_index = fields.TypedField("Egress_Interface_Index", Integer)
    ip_type_of_service = fields.TypedField("IP_Type_Of_Service", HexBinary)


class YAFTCPFlow(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.YAFTCPFlowType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    tcp_sequence_number = fields.TypedField("TCP_Sequence_Number", Integer)
    initial_tcp_flags = fields.TypedField("Initial_TCP_Flags", TCPFlags)
    union_tcp_flags = fields.TypedField("Union_TCP_Flags", HexBinary)


class YAFFlow(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.YAFFlowType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow_start_milliseconds = fields.TypedField("Flow_Start_Milliseconds", Integer)
    flow_end_milliseconds = fields.TypedField("Flow_End_Milliseconds", Integer)
    octet_total_count = fields.TypedField("Octet_Total_Count", Integer)
    packet_total_count = fields.TypedField("Packet_Total_Count", Integer)
    flow_end_reason = fields.TypedField("Flow_End_Reason", HexBinary)
    silk_app_label = fields.TypedField("SiLK_App_Label", Integer)
    payload_entropy = fields.TypedField("Payload_Entropy", Integer)
    ml_app_label = fields.TypedField("ML_App_Label", HexBinary)
    tcp_flow = fields.TypedField("TCP_Flow", YAFTCPFlow)
    vlan_id_mac_addr = fields.TypedField("Vlan_ID_MAC_Addr", Address)
    passive_os_fingerprinting = fields.TypedField("Passive_OS_Fingerprinting", PlatformSpecification)
    first_packet_banner = fields.TypedField("First_Packet_Banner", HexBinary)
    second_packet_banner = fields.TypedField("Second_Packet_Banner", HexBinary)
    n_bytes_payload = fields.TypedField("N_Bytes_Payload", HexBinary)


class YAFReverseFlow(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.YAFReverseFlowType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    reverse_octet_total_count = fields.TypedField("Reverse_Octet_Total_Count", Integer)
    reverse_packet_total_count = fields.TypedField("Reverse_Packet_Total_Count", Integer)
    reverse_payload_entropy = fields.TypedField("Reverse_Payload_Entropy", Integer)
    reverse_flow_delta_milliseconds = fields.TypedField("Reverse_Flow_Delta_Milliseconds", Integer)
    tcp_reverse_flow = fields.TypedField("TCP_Reverse_Flow", YAFTCPFlow)
    reverse_vlan_id_mac_addr = fields.TypedField("Reverse_Vlan_ID_MAC_Addr", Address)
    reverse_passive_os_fingerprinting = fields.TypedField("Reverse_Passive_OS_Fingerprinting", PlatformSpecification)
    reverse_first_packet = fields.TypedField("Reverse_First_Packet", HexBinary)
    reverse_n_bytes_payload = fields.TypedField("Reverse_N_Bytes_Payload", HexBinary)


class YAFRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.YAFRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    flow = fields.TypedField("Flow", YAFFlow)
    reverse_flow = fields.TypedField("Reverse_Flow", YAFReverseFlow)


class BidirectionalRecord(entities.Entity):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.BidirectionalRecordType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"

    yaf_record = fields.TypedField("YAF_Record", YAFRecord)


class NetworkFlow(ObjectProperties):
    _binding = network_flow_binding
    _binding_class = network_flow_binding.NetworkFlowObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkFlowObject-2"
    _XSI_NS = "NetFlowObj"
    _XSI_TYPE = "NetworkFlowObjectType"

    network_flow_label = fields.TypedField("Network_Flow_Label", NetworkFlowLabel)
    unidirectional_flow_record = fields.TypedField("Unidirectional_Flow_Record", UnidirectionalRecord)
    bidirectional_flow_record = fields.TypedField("Bidirectional_Flow_Record", BidirectionalRecord)
