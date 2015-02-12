# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.system_object as system_binding
from cybox.common import PlatformSpecification, ObjectProperties, String, UnsignedInteger, UnsignedLong, Date, DateTime, Duration, EnvironmentVariableList
from cybox.common.properties import Time
from cybox.objects.address_object import Address
from cybox import TypedField

class DHCPServerList(cybox.EntityList):
    _binding_class = system_binding.DHCPServerListType
    _binding_var = "DHCP_Server_Address"
    _contained_type = Address
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class IPGatewayList(cybox.EntityList):
    _binding_class = system_binding.IPGatewayListType
    _binding_var = "IP_Gateway_Address"
    _contained_type = Address
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    
    
class IPInfo(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.IPInfoType


    def __init__(self):
        super(IPInfo, self).__init__()
        ip_address = TypedField("IP_Address", Address)
        subnet_mask = TypedField("Subnet_Mask", Address)

class IPInfoList(cybox.EntityList):
    _binding_class = system_binding.IPInfoListType
    _binding_var = "IP_Info_List"
    _contained_type = IPInfo
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"


class OS(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.OSType
    
    bitness = TypedField("Bitness", String)
    build_number = TypedField("Build_Number", String)
    environment_variable_list = TypedField("Environment_Variable_List", EnvironmentVariableList)
    install_date = TypedField("Install_Date", Date)
    patch_level = TypedField("Patch_Level", String)
    platform = TypedField("Platform", PlatformSpecification)

    def __init__(self):
        super(OS, self).__init__()

class BIOSInfo(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.BIOSInfoType

    bios_date = cybox.TypedField("BIOS_Date", Date)
    bios_version = cybox.TypedField("BIOS_Version", String)
    bios_manufacturer = cybox.TypedField("BIOS_Manufacturer", String)
    bios_release_date = cybox.TypedField("BIOS_Release_Date", Date)
    bios_serial_number = cybox.TypedField("BIOS_Serial_Number", String)

    def __init__(self):
        super(BIOSInfo, self).__init__()

class NetworkInterface(cybox.Entity):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _binding = system_binding
    _binding_class = system_binding.NetworkInterfaceType
    
    adapter = TypedField("Adapter", String)
    description = TypedField("Description", String)
    dhcp_lease_expires = TypedField("DHCP_Lease_Expires", DateTime)
    dhcp_lease_obtained = TypedField("DHCP_Lease_Obtained", DateTime)
    dhcp_server_list = TypedField("DHCP_Server_List", DHCPServerList)
    ip_gateway_list = TypedField("IP_Gateway_List", IPGatewayList)
    ip_list = TypedField("IP_List", IPInfoList)
    mac = TypedField("MAC", String)
    

    def __init__(self):
        super(NetworkInterface, self).__init__()

class NetworkInterfaceList(cybox.EntityList):
    _binding_class = system_binding.NetworkInterfaceListType
    _binding_var = "Network_Interface"
    _contained_type = NetworkInterface
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    
class System(ObjectProperties):
    _namespace = "http://cybox.mitre.org/objects#SystemObject-2"
    _XSI_NS = "SystemObj"
    _XSI_TYPE = "SystemObjectType"
    _binding = system_binding
    _binding_class = system_binding.SystemObjectType
    
    available_physical_memory = cybox.TypedField("Available_Physical_Memory", UnsignedLong)
    bios_info = cybox.TypedField("BIOS_Info", BIOSInfo)
    date = cybox.TypedField("Date", Date)
    hostname = cybox.TypedField("Hostname", String)
    local_time = cybox.TypedField("Local_Time", Time)
    network_interface_list = cybox.TypedField("Network_Interface_List", NetworkInterfaceList)
    os = cybox.TypedField("OS", OS)
    processor = cybox.TypedField("Processor", String)
    # TODO
    # processor_architecture = cybox.TypedField("Processor_Architecture", ProcessorArch)
    system_time = cybox.TypedField("System_Time", Time)
    timezone_dst = cybox.TypedField("Timezone_DST", String)
    timezone_standard = cybox.TypedField("Timezone_Standard", String)
    total_physical_memory = cybox.TypedField("Total_Physical_Memory", UnsignedLong)
    uptime = cybox.TypedField("Uptime", Duration)
    username = cybox.TypedField("Username", String)
    
    def __init__(self):
        super(System, self).__init__()
