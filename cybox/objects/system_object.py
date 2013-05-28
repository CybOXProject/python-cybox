# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.system_object as system_binding
from cybox.common.environment_variable_list import EnvironmentVariableList
from cybox.objects.address_object import Address
from cybox.common import ObjectProperties, String, UnsignedInteger, UnsignedLong, Date, Time, Duration

class System(ObjectProperties):
    _XSI_NS = "SystemObj"
    _XSI_TYPE = "SystemObjectType"

    def __init__(self):
        super(System, self).__init__()
        self.available_physical_memory = None
        self.bios_info = None
        self.date = None
        self.hostname = None
        self.local_time = None
        self.network_interface_list = None
        self.os = None
        self.processor = None
        self.processor_architecture = None
        self.system_time = None
        self.timezone_dst = None
        self.timezone_standard = None
        self.total_physical_memory = None
        self.uptime = None
        self.username = None

    def to_obj(self, object_type = None):
        if not object_type:
            system_obj = system_binding.SystemObjectType()
        else:
            system_obj = object_type
        super(System, self).to_obj(system_obj)
        if self.available_physical_memory is not None : system_obj.set_Available_Physical_Memory(self.available_physical_memory.to_obj())
        if self.bios_info is not None : system_obj.set_BIOS_Info(self.bios_info.to_obj())
        if self.date is not None : system_obj.set_Date(self.date.to_obj())
        if self.hostname is not None : system_obj.set_Hostname(self.hostname.to_obj())
        if self.local_time is not None : system_obj.set_Local_Time(self.local_time.to_obj())
        if self.network_interface_list is not None : system_obj.set_Network_Interface_List(self.network_interface_list.to_obj())
        if self.os is not None : system_obj.set_OS(self.os.to_obj())
        if self.processor is not None : system_obj.set_Processor(self.processor.to_obj())
        if self.processor_architecture is not None : system_obj.set_Processor_Architecture(self.processor_architecture.to_obj())
        if self.system_time is not None : system_obj.set_System_Time(self.system_time.to_obj())
        if self.timezone_dst is not None : system_obj.set_Timezone_DST(self.timezone_dst.to_obj())
        if self.timezone_standard is not None : system_obj.set_Timezone_Standard(self.timezone_standard.to_obj())
        if self.total_physical_memory is not None : system_obj.set_Total_Physical_Memory(self.total_physical_memory.to_obj())
        if self.uptime is not None : system_obj.set_Uptime(self.uptime.to_obj())
        if self.username is not None : system_obj.set_Username(self.username.to_obj())
        return system_obj

    def to_dict(self):
        system_dict = {}
        if self.available_physical_memory is not None : system_dict['available_physical_memory'] = self.available_physical_memory.to_dict()
        if self.bios_info is not None : system_dict['bios_info'] = self.bios_info.to_dict()
        if self.date is not None : system_dict['date'] = self.date.to_dict()
        if self.hostname is not None : system_dict['hostname'] = self.hostname.to_dict()
        if self.local_time is not None : system_dict['local_time'] = self.local_time.to_dict()
        if self.network_interface_list is not None : system_dict['network_interface_list'] = self.network_interface_list.to_dict()
        if self.os is not None : system_dict['os'] = self.os.to_dict()
        if self.processor is not None : system_dict['processor'] = self.processor.to_dict()
        if self.processor_architecture is not None : system_dict['processor_architecture'] = self.processor_architecture.to_dict()
        if self.system_time is not None : system_dict['system_time'] = self.system_time.to_dict()
        if self.timezone_dst is not None : system_dict['timezone_dst'] = self.timezone_dst.to_dict()
        if self.timezone_standard is not None : system_dict['timezone_standard'] = self.timezone_standard.to_dict()
        if self.total_physical_memory is not None : system_dict['total_physical_memory'] = self.total_physical_memory.to_dict()
        if self.uptime is not None : system_dict['uptime'] = self.uptime.to_dict()
        if self.username is not None : system_dict['username'] = self.username.to_dict()
        return system_dict

    @staticmethod
    def from_dict(system_dict, system_class = None):
        if not system_dict:
            return None
        if not system_class:
            system_ = System()
        else:
            system_ = system_class
        system_.available_physical_memory = UnsignedLong.from_dict(system_dict.get('available_physical_memory'))
        system_.bios_info = BIOSInfo.from_dict(system_dict.get('bios_info'))
        system_.date = Date.from_dict(system_dict.get('date'))
        system_.hostname = String.from_dict(system_dict.get('hostname'))
        system_.local_time = Time.from_dict(system_dict.get('local_time'))
        system_.network_interface_list = NetworkInterfaceList.from_list(system_dict.get('network_interface_list'))
        system_.os = OS.from_dict(system_dict.get('os'))
        system_.processor = String.from_dict(system_dict.get('processor'))
        system_.processor_architecture = String.from_dict(system_dict.get('processor_architecture'))
        system_.system_time = Time.from_dict(system_dict.get('system_time'))
        system_.timezone_dst = String.from_dict(system_dict.get('timezone_dst'))
        system_.timezone_standard = String.from_dict(system_dict.get('timezone_standard'))
        system_.total_physical_memory = UnsignedLong.from_dict(system_dict.get('total_physical_memory'))
        system_.uptime = Duration.from_dict(system_dict.get('uptime'))
        system_.username = String.from_dict(system_dict.get('username'))
        return system_

    @staticmethod
    def from_obj(system_obj, system_class = None):
        if not system_obj:
            return None
        if not system_class:
            system_ = System()
        else:
            system_ = system_class
        system_.available_physical_memory = UnsignedLong.from_obj(system_obj.get_Available_Physical_Memory())
        system_.bios_info = BIOSInfo.from_obj(system_obj.get_BIOS_Info())
        system_.date = Date.from_obj(system_obj.get_Date())
        system_.hostname = String.from_obj(system_obj.get_Hostname())
        system_.local_time = Time.from_obj(system_obj.get_Local_Time())
        system_.network_interface_list = NetworkInterfaceList.from_obj(system_obj.get_Network_Interface_List())
        system_.os = OS.from_obj(system_obj.get_OS())
        system_.processor = String.from_obj(system_obj.get_Processor())
        system_.processor_architecture = String.from_obj(system_obj.get_Processor_Architecture())
        system_.system_time = Time.from_obj(system_obj.get_System_Time())
        system_.timezone_dst = String.from_obj(system_obj.get_Timezone_DST())
        system_.timezone_standard = String.from_obj(system_obj.get_Timezone_Standard())
        system_.total_physical_memory = UnsignedLong.from_obj(system_obj.get_Total_Physical_Memory())
        system_.uptime = Duration.from_obj(system_obj.get_Uptime())
        system_.username = String.from_obj(system_obj.get_Username())
        return system_

class NetworkInterface(cybox.Entity):
    def __init__(self):
        super(NetworkInterface, self).__init__()
        self.adapter = None
        self.description = None
        self.dhcp_lease_expires = None
        self.dhcp_lease_obtained = None
        self.dhcp_server_list = None
        self.ip_gateway_list = None
        self.ip_list = None
        self.mac = None

    def to_obj(self):
        network_interface_obj = system_binding.NetworkInterfaceType()
        if self.adapter is not None : network_interface_obj.set_Adapter(self.adapter.to_obj())
        if self.description is not None : network_interface_obj.set_Description(self.description.to_obj())
        if self.dhcp_lease_expires is not None : network_interface_obj.set_DHCP_Lease_Expires(self.dhcp_lease_expires.to_obj())
        if self.dhcp_lease_obtained is not None : network_interface_obj.set_DHCP_Lease_Obtained(self.dhcp_lease_obtained.to_obj())
        if self.dhcp_server_list is not None : network_interface_obj.set_DHCP_Server_List(self.dhcp_server_list.to_obj())
        if self.ip_gateway_list is not None : network_interface_obj.set_IP_Gateway_List(self.ip_gateway_list.to_obj())
        if self.ip_list is not None : network_interface_obj.set_IP_List(self.ip_list.to_obj())
        if self.mac is not None : network_interface_obj.set_MAC(self.mac.to_obj())
        return network_interface_obj

    def to_dict(self):
        network_interface_dict = {}
        if self.adapter is not None : network_interface_dict['adapter'] = self.adapter.to_dict()
        if self.description is not None : network_interface_dict['description'] = self.description.to_dict()
        if self.dhcp_lease_expires is not None : network_interface_dict['dhcp_lease_expires'] = self.dhcp_lease_expires.to_dict()
        if self.dhcp_lease_obtained is not None : network_interface_dict['dhcp_lease_obtained'] = self.dhcp_lease_obtained.to_dict()
        if self.dhcp_server_list is not None : network_interface_dict['dhcp_server_list'] = self.dhcp_server_list.to_list()
        if self.ip_gateway_list is not None : network_interface_dict['ip_gateway_list'] = self.ip_gateway_list.to_list()
        if self.ip_list is not None : network_interface_dict['ip_list'] = self.ip_list.to_list()
        if self.mac is not None : network_interface_dict['mac'] = self.mac.to_dict()
        return network_interface_dict

    @staticmethod
    def from_dict(network_interface_dict):
        if not network_interface_dict:
            return None
        network_interface_ = NetworkInterface()
        network_interface_.adapter = String.from_dict(network_interface_dict.get('adapter'))
        network_interface_.description = String.from_dict(network_interface_dict.get('description'))
        network_interface_.dhcp_lease_expires = DateTime.from_dict(network_interface_dict.get('dhcp_lease_expires'))
        network_interface_.dhcp_lease_obtained = DateTime.from_dict(network_interface_dict.get('dhcp_lease_obtained'))
        network_interface_.dhcp_server_list = DHCPServerList.from_list(network_interface_dict.get('dhcp_server_list'))
        network_interface_.ip_gateway_list = IPGatewayList.from_list(network_interface_dict.get('ip_gateway_list'))
        network_interface_.ip_list = IPInfoList.from_list(network_interface_dict.get('ip_list'))
        network_interface_.mac = String.from_dict(network_interface_dict.get('mac'))
        return network_interface_

    @staticmethod
    def from_obj(network_interface_obj):
        if not network_interface_obj:
            return None
        network_interface_ = NetworkInterface()
        network_interface_.adapter = String.from_obj(network_interface_obj.get_Adapter())
        network_interface_.description = String.from_obj(network_interface_obj.get_Description())
        network_interface_.dhcp_lease_expires = DateTime.from_obj(network_interface_obj.get_DHCP_Lease_Expires())
        network_interface_.dhcp_lease_obtained = DateTime.from_obj(network_interface_obj.get_DHCP_Lease_Obtained())
        network_interface_.dhcp_server_list = DHCPServerList.from_obj(network_interface_obj.get_DHCP_Server_List())
        network_interface_.ip_gateway_list = IPGatewayList.from_obj(network_interface_obj.get_IP_Gateway_List())
        network_interface_.ip_list = IPInfoList.from_obj(network_interface_obj.get_IP_List())
        network_interface_.mac = String.from_obj(network_interface_obj.get_MAC())
        return network_interface_

class NetworkInterfaceList(cybox.EntityList):
    _contained_type = NetworkInterface
    _binding_class = system_binding.NetworkInterfaceListType

    def __init__(self):
        super(NetworkInterfaceList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Network_Interface(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Network_Interface()

class DHCPServerList(cybox.EntityList):
    _contained_type = Address
    _binding_class = system_binding.DHCPServerListType

    def __init__(self):
        super(DHCPServerList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_DHCP_Server_Address(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_DHCP_Server_Address()

class IPGatewayList(cybox.EntityList):
    _contained_type = Address
    _binding_class = system_binding.IPGatewayListType

    def __init__(self):
        super(IPGatewayList, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_IP_Gateway_Address(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_IP_Gateway_Address()

class OS(cybox.Entity):
    def __init__(self):
        super(OS, self).__init__()
        self.bitness = None
        self.build_number = None
        self.environment_variable_list = None
        self.install_date = None
        self.patch_level = None
        self.platform = None
    
    def to_obj(self):
        os_obj = system_binding.OSType()
        if self.bitness is not None : os_obj.set_Bitness(self.bitness.to_obj())
        if self.build_number is not None : os_obj.set_Build_Number(self.build_number.to_obj())
        if self.environment_variable_list is not None : os_obj.set_Environment_Variable_List(self.environment_variable_list.to_obj())
        if self.install_date is not None : os_obj.set_Install_Date(self.install_date.to_obj())
        if self.patch_level is not None : os_obj.set_Patch_Level(self.patch_level.to_obj())
        if self.platform is not None : os_obj.set_Platform(self.platform.to_obj())
        return os_obj

    def to_dict(self):
        os_dict = {}
        if self.bitness is not None : os_dict['bitness'] = self.bitness.to_dict()
        if self.build_number is not None : os_dict['build_number'] = self.build_number.to_dict()
        if self.environment_variable_list is not None : os_dict['environment_variable_list'] = self.environment_variable_list.to_dict()
        if self.install_date is not None : os_dict['install_date'] = self.install_date.to_dict()
        if self.patch_level is not None : os_dict['patch_level'] = self.patch_level.to_dict()
        if self.platform is not None : os_dict['platform'] = self.platform.to_dict()
        return os_dict

    @staticmethod
    def from_dict(os_dict):
        if not os_dict:
            return None
        os_ = OS()
        os_.bitness = String.from_dict(os_dict.get('bitness'))
        os_.build_number = String.from_dict(os_dict.get('build_number'))
        os_.environment_variable_list = EnvironmentVariableList.from_list(os_dict.get('environment_variable_list'))
        os_.install_date = Date.from_dict(os_dict.get('install_date'))
        os_.patch_level = String.from_dict(os_dict.get('patch_level'))
        os_.platform = None #TODO: add support for platform specification
        return os_

    @staticmethod
    def from_obj(os_obj):
        if not os_obj:
            return None
        os_ = OS()
        os_.bitness = String.from_obj(os_obj.get_Bitness())
        os_.build_number = String.from_obj(os_obj.get_Build_Number())
        os_.environment_variable_list = EnvironmentVariableList.from_obj(os_obj.get_Environment_Variable_List())
        os_.install_date = Date.from_obj(os_obj.get_Install_Date())
        os_.patch_level = String.from_obj(os_obj.get_Patch_Level())
        os_.platform = None #TODO: add support for platform specification
        return os_

class BIOSInfo(cybox.Entity):
    def __init__(self):
        super(BIOSInfo, self).__init__()
        self.bios_date = None
        self.bios_version = None
        self.bios_manufacturer = None
        self.bios_release_date = None
        self.bios_serial_number = None

    def to_obj(self):
        bios_info_obj = system_binding.BIOSInfoType()
        if self.bios_date is not None : bios_info_obj.set_BIOS_Date(self.bios_date.to_obj())
        if self.bios_version is not None : bios_info_obj.set_BIOS_Version(self.bios_version.to_obj())
        if self.bios_manufacturer is not None : bios_info_obj.set_BIOS_Manufacturer(self.bios_manufacturer.to_obj())
        if self.bios_release_date is not None : bios_info_obj.set_BIOS_Release_Date(self.bios_release_date.to_obj())
        if self.bios_serial_number is not None : bios_info_obj.set_BIOS_Serial_Number(self.bios_serial_number.to_obj())
        return bios_info_obj

    def to_dict(self):
        bios_info_dict = {}
        if self.bios_date is not None : bios_info_dict['bios_date'] = self.bios_date.to_dict()
        if self.bios_version is not None : bios_info_dict['bios_version'] = self.bios_version.to_dict()
        if self.bios_manufacturer is not None : bios_info_dict['bios_manufacturer'] = self.bios_manufacturer.to_dict()
        if self.bios_release_date is not None : bios_info_dict['bios_release_date'] = self.bios_release_date.to_dict()
        if self.bios_serial_number is not None : bios_info_dict['bios_serial_number'] = self.bios_serial_number.to_dict()
        return bios_info_dict

    @staticmethod
    def from_dict(bios_info_dict):
        if not bios_info_dict:
            return None
        bios_info_ = BIOSInfo()
        bios_info_.bios_date = Date.from_dict(bios_info_dict.get('bios_date'))
        bios_info_.bios_version = String.from_dict(bios_info_dict.get('bios_version'))
        bios_info_.bios_manufacturer = String.from_dict(bios_info_dict.get('bios_manufacturer'))
        bios_info_.bios_release_date = Date.from_dict(bios_info_dict.get('bios_release_date'))
        bios_info_.bios_serial_number = String.from_dict(bios_info_dict.get('bios_serial_number'))
        return bios_info_

    @staticmethod
    def from_obj(bios_info_obj):
        if not bios_info_obj:
            return None
        bios_info_ = BIOSInfo()
        bios_info_.bios_date = Date.from_obj(bios_info_obj.get_BIOS_Date())
        bios_info_.bios_version = String.from_obj(bios_info_obj.get_BIOS_Version())
        bios_info_.bios_manufacturer = String.from_obj(bios_info_obj.get_BIOS_Manufacturer())
        bios_info_.bios_release_date = Date.from_obj(bios_info_obj.get_BIOS_Release_Date())
        bios_info_.bios_serial_number = String.from_obj(bios_info_obj.get_BIOS_Serial_Number())
        return bios_info_
