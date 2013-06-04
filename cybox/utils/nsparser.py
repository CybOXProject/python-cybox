# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import itertools


class Namespace(object):
    """An XML namespace used to define CybOX objects.

    Encapsulates the full namespace (URL), the most commonly-used prefix for
    the namespace, and (if applicable), the location of the corresponding
    schema.
    """

    def __init__(self, name, prefix, schema_location):
        """Create a new namespace.

        Arguments:
        - name: the full namespace (a URI)
        - prefix: a shortened prefix for the URL (used in the xmlns)
        - schema_location: a URL to locate the schema for this namespace
        """
        self.name = name
        self.prefix = prefix
        self.schema_location = schema_location

    def __repr__(self):
        return "Namespace('%s', '%s', '%s')" % (self.name,
                                                self.prefix,
                                                self.schema_location)


class ObjectType(object):

    def __init__(self, name, api_class, namespace):
        self.name = name
        self.api_class = api_class
        self.namespace = namespace


class Metadata(object):
    """Metadata about CybOX objects and namespaces."""

    def __init__(self):
        self._ns_dict = {}
        self._prefix_dict = {}

        for ns in NS_LIST:
            n = Namespace(*ns)
            self._ns_dict[n.name] = n
            self._prefix_dict[n.prefix] = n

    def lookup_namespace(self, namespace):
        return self._ns_dict[namespace]

    def lookup_prefix(self, prefix):
        return self._prefix_dict[prefix]


# A list of (namespace, prefix, schemalocation) tuples
# This is loaded by the Metadata class and should not be accessed directly.
NS_LIST = [
    ('http://www.w3.org/2001/XMLSchema-instance', 'xsi', ''),
    ('http://cybox.mitre.org/cybox-2', 'cybox', 'http,//cybox.mitre.org/XMLSchema/core/2.0/cybox_core.xsd'),
    ('http://cybox.mitre.org/common-2', 'cyboxCommon', 'http,//cybox.mitre.org/XMLSchema/common/2.0/cybox_common.xsd'),
    ('http://cybox.mitre.org/default_vocabularies-2', 'cyboxVocabs', 'http,//cybox.mitre.org/XMLSchema/default_vocabularies/2.0.0/cybox_default_vocabularies.xsd'),
    ('http://cybox.mitre.org/objects#AccountObject-2', 'AccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Account/2.0/Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#AddressObject-2', 'AddressObj', 'http://cybox.mitre.org/XMLSchema/objects/Address/2.0/Address_Object.xsd'),
    ('http://cybox.mitre.org/objects#APIObject-2', 'APIObj', 'http://cybox.mitre.org/XMLSchema/objects/API/2.0/API_Object.xsd'),
    ('http://cybox.mitre.org/objects#ArtifactObject-2', 'ArtifactObj', 'http://cybox.mitre.org/XMLSchema/objects/Artifact/2.0/Artifact_Object.xsd'),
    ('http://cybox.mitre.org/objects#CodeObject-2', 'CodeObj', 'http://cybox.mitre.org/XMLSchema/objects/Code/2.0/Code_Object.xsd'),
    ('http://cybox.mitre.org/objects#CustomObject-1', 'CustomObj', 'http://cybox.mitre.org/XMLSchema/objects/Custom/1.0/Custom_Object.xsd'),
    ('http://cybox.mitre.org/objects#DeviceObject-2', 'DeviceObj', 'http://cybox.mitre.org/XMLSchema/objects/Device/2.0/Device_Object.xsd'),
    ('http://cybox.mitre.org/objects#DiskObject-2', 'DiskObj', 'http://cybox.mitre.org/XMLSchema/objects/Disk/2.0/Disk_Object.xsd'),
    ('http://cybox.mitre.org/objects#DiskPartitionObject-2', 'DiskPartitionObj', 'http://cybox.mitre.org/XMLSchema/objects/Disk_Partition/2.0/Disk_Partition_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSCacheObject-2', 'DNSCacheObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Cache/2.0/DNS_Cache_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSQueryObject-2', 'DNSQueryObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Query/2.0/DNS_Query_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSRecordObject-2', 'DNSRecordObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Record/2.0/DNS_Record_Object.xsd'),
    ('http://cybox.mitre.org/objects#EmailMessageObject-2', 'EmailMessageObj', 'http://cybox.mitre.org/XMLSchema/objects/Email_Message/2.0/Email_Message_Object.xsd'),
    ('http://cybox.mitre.org/objects#FileObject-2', 'FileObj', 'http://cybox.mitre.org/XMLSchema/objects/File/2.0/File_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIDialogboxObject-2', 'GUIDialogboxObj', 'http://cybox.mitre.org/XMLSchema/objects/GUI_Dialogbox/2.0/GUI_Dialogbox_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIObject-2', 'GUIObj', 'http://cybox.mitre.org/XMLSchema/objects/GUI/2.0/GUI_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIWindowObject-2', 'GUIWindowOb', 'http://cybox.mitre.org/XMLSchema/objects/GUI_Window/2.0/GUI_Window_Object.xsd'),
    ('http://cybox.mitre.org/objects#HTTPSessionObject-2', 'HTTPSessionObj', 'http://cybox.mitre.org/XMLSchema/objects/HTTP_Session/2.0/HTTP_Session_Object.xsd'),
    ('http://cybox.mitre.org/objects#LibraryObject-2', 'LibraryObj', 'http://cybox.mitre.org/XMLSchema/objects/Library/2.0/Library_Object.xsd'),
    ('http://cybox.mitre.org/objects#LinkObject-1', 'LinkObj', 'http://cybox.mitre.org/XMLSchema/objects/Link/1.0/Link_Object.xsd'),
    ('http://cybox.mitre.org/objects#LinuxPackageObject-2', 'LinuxPackageObj', 'http://cybox.mitre.org/XMLSchema/objects/Linux_Package/2.0/Linux_Package_Object.xsd'),
    ('http://cybox.mitre.org/objects#MemoryObject-2', 'MemoryObj', 'http://cybox.mitre.org/XMLSchema/objects/Memory/2.0/Memory_Object.xsd'),
    ('http://cybox.mitre.org/objects#MutexObject-2', 'MutexObj', 'http://cybox.mitre.org/XMLSchema/objects/Mutex/2.0/Mutex_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkConnectionObject-2', 'NetworkConnectionObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Connection/2.0/Network_Connection_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkFlowObject-2', 'NetFlowObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Flow/2.0/Network_Flow_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkRouteEntryObject-2', 'NetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Route_Entry/2.0/Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkRouteObject-2', 'NetworkRouteObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Route/2.0/Network_Route_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkSocketObject-2', 'NetworkSocketObj', 'http://cybox.mitre.org/XMLSchema/objects/Socket/2.0/Socket_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkSubnetObject-2', 'NetworkSubnetObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Subnet/2.0/Network_Subnet_Object.xsd'),
    ('http://cybox.mitre.org/objects#PacketObject-2', 'PacketObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Packet/2.0/Network_Packet_Object.xsd'),
    ('http://cybox.mitre.org/objects#PDFFileObject-1', 'PDFFileObj', 'http://cybox.mitre.org/XMLSchema/objects/PDF_File/1.0/PDF_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#PipeObject-2', 'PipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Pipe/2.0/Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#PortObject-2', 'PortObj', 'http://cybox.mitre.org/XMLSchema/objects/Port/2.0/Port_Object.xsd'),
    ('http://cybox.mitre.org/objects#ProcessObject-2', 'ProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Process/2.0/Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#SemaphoreObject-2', 'SemaphoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Semaphore/2.0/Semaphore_Object.xsd'),
    ('http://cybox.mitre.org/objects#SocketAddressObject-1', 'SocketAddressObj', 'http://cybox.mitre.org/XMLSchema/objects/Socket_Address/1.0/Socket_Address_Object.xsd'),
    ('http://cybox.mitre.org/objects#SystemObject-2', 'SystemObj', 'http://cybox.mitre.org/XMLSchema/objects/System/2.0/System_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixFileObject-2', 'UnixFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_File/2.0/Unix_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2', 'UnixNetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Network_Route_Entry/2.0/Unix_Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixPipeObject', 'UnixPipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Pipe/2.0/Unix_Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixProcessObject-2', 'UnixProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Process/2.0/Unix_Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixUserAccountObject-2', 'UnixUserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_User_Account/2.0/Unix_User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixVolumeObject-2', 'UnixVolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Volume/2.0/Unix_Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#URIObject-2', 'URIObj', 'http://cybox.mitre.org/XMLSchema/objects/URI/2.0/URI_Object.xsd'),
    ('http://cybox.mitre.org/objects#UserAccountObject-2', 'UserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/User_Account/2.0/User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#VolumeObject-2', 'VolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Volume/2.0/Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#WhoisObject-2', 'WhoisObj', 'http://cybox.mitre.org/XMLSchema/objects/Whois/2.0/Whois_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinComputerAccountObject-2', 'WinComputerAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Computer_Account/2.0/Win_Computer_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinCriticalSectionObject-2', 'WinCriticalSectionObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Critical_Section/2.0/Win_Critical_Section_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinDriverObject-2', 'WinDriverObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Driver/2.0/Win_Driver_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinEventLogObject-2', 'WinEventLogObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Event_Log/2.0/Win_Event_Log_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinEventObject-2', 'WinEventObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Event/2.0/Win_Event_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinExecutableFileObject-2', 'WinExecutableFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Executable_File/2.0/Win_Executable_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinFileObject-2', 'WinFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_File/2.0/Win_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinHandleObject-2', 'WinHandleObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Handle/2.0/Win_Handle_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinKernelHookObject-2', 'WinKernelHookObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel_Hook/2.0/Win_Kernel_Hook_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinKernelObject-2', 'WinKernelObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel/2.0/Win_Kernel_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMailslotObject-2', 'WinMailslotObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Mailslot/2.0/Win_Mailslot_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2', 'WinMemoryPageRegionObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Memory_Page_Region/2.0/Win_Memory_Page_Region_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMutexObject-2', 'WinMutexObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Mutex/2.0/Win_Mutex_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2', 'WinNetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Route_Entry/2.0/Win_Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinNetworkShareObject-2', 'WinNetworkShareObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Share/2.0/Win_Network_Share_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinPipeObject-2', 'WinPipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Pipe/2.0/Win_Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinPrefetchObject-2', 'WinPrefetchObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Prefetch/2.0/Win_Prefetch_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinProcessObject-2', 'WinProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Process/2.0/Win_Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinRegistryKeyObject-2', 'WinRegistryKeyObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Registry_Key/2.0/Win_Registry_Key_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSemaphoreObject-2', 'WinSemaphoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Semaphore/2.0/Win_Semaphore_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinServiceObject-2', 'WinServiceObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Service/2.0/Win_Service_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSystemObject-2', 'WinSystemObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_System/2.0/Win_System_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSystemRestoreObject-2', 'WinSystemRestoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_System_Restore/2.0/Win_System_Restore_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinTaskObject-2', 'WinTaskObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Task/2.0/Win_Task_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinThreadObject-2', 'WinThreadObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Thread/2.0/Win_Thread_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinUserAccountObject-2', 'WinUserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_User_Account/2.0/Win_User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinVolumeObject-2', 'WinVolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Volume/2.0/Win_Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinWaitableTimerObject-2', 'WinWaitableTimerObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Waitable_Timer/2.0/Win_Waitable_Timer_Object.xsd'),
    ('http://cybox.mitre.org/objects#X509CertificateObject-2', 'X509CertificateObj', 'http://cybox.mitre.org/XMLSchema/objects/X509_Certificate/2.0/X509_Certificate_Object.xsd'),
]

#Dictionary for storing Defined Objects, their main types, namespaces, and schemalocations
OBJECT_TYPES_DICT = {
    'AccountObjectType': {
        'api_class': None,
        'binding_name': 'account_object',
        'namespace': 'http://cybox.mitre.org/objects#AccountObject-2',
    },
    'AddressObjectType': {
        'api_class': 'cybox.objects.address_object.Address',
        'binding_name': 'address_object',
        'namespace': 'http://cybox.mitre.org/objects#AddressObject-2',
    },
    'APIObjectType': {
        'api_class': None,
        'binding_name': 'api_object',
        'namespace': 'http://cybox.mitre.org/objects#APIObject-2',
    },
    'ArtifactObjectType': {
        'api_class': 'cybox.objects.artifact_object.Artifact',
        'binding_name': 'artifact_object',
        'namespace': 'http://cybox.mitre.org/objects#ArtifactObject-2',
    },
    'CodeObjectType': {
        'api_class': None,
        'binding_name': 'code_object',
        'namespace': 'http://cybox.mitre.org/objects#CodeObject-2',
    },
    'CustomObjectType': {
        'api_class': None,
        'binding_name': 'custom_object',
        'namespace': 'http://cybox.mitre.org/objects#CustomObject-1',
    },
    'DeviceObjectType': {
        'api_class': None,
        'binding_name': 'device_object',
        'namespace': 'http://cybox.mitre.org/objects#DeviceObject-2',
    },
    'DiskObjectType': {
        'api_class': None,
        'binding_name': 'disk_object',
        'namespace': 'http://cybox.mitre.org/objects#DiskObject-2',
        'dependencies': 'DiskPartitionObjectType'
    },
    'DiskPartitionObjectType': {
        'api_class': None,
        'binding_name': 'disk_partition_object',
        'namespace': 'http://cybox.mitre.org/objects#DiskPartitionObject-2',
    },
    'DNSCacheEntryType': {
        'api_class': None,
        'binding_name': 'dns_cache_object',
        'namespace': 'http://cybox.mitre.org/objects#DNSCacheObject-2',
        'dependencies': 'DNSRecordObjectType,AddressObjectType,URIObjectType'
    },
    'DNSQueryObjectType': {
        'api_class': 'cybox.objects.dns_query_object.DNSQuery',
        'binding_name': 'dns_query_object',
        'namespace': 'http://cybox.mitre.org/objects#DNSQueryObject-2',
        'dependencies': 'DNSRecordObjectType,URIObjectType,AddressObjectType'
    },
    'DNSRecordObjectType': {
        'api_class': 'cybox.objects.dns_record_object.DNSRecord',
        'binding_name': 'dns_record_object',
        'namespace': 'http://cybox.mitre.org/objects#DNSRecordObject-2',
        'dependencies': 'URIObjectType,AddressObjectType'
    },
    'EmailMessageObjectType': {
        'api_class': 'cybox.objects.email_message_object.EmailMessage',
        'binding_name': 'email_message_object',
        'namespace': 'http://cybox.mitre.org/objects#EmailMessageObject-2',
        'dependencies': 'FileObjectType,AddressObjectType,URIObjectType'
    },
    'FileObjectType': {
        'api_class': 'cybox.objects.file_object.File',
        'binding_name': 'file_object',
        'namespace': 'http://cybox.mitre.org/objects#FileObject-2',
    },
    'GUIDialogboxObjectType': {
        'api_class': None,
        'binding_name': 'gui_dialogbox_object',
        'namespace': 'http://cybox.mitre.org/objects#GUIDialogboxObject-2',
        'dependencies': 'GUIObjectType'
    },
    'GUIObjectType': {
        'api_class': None,
        'binding_name': 'gui_object',
        'namespace': 'http://cybox.mitre.org/objects#GUIObject-2',
    },
    'GUIWindowObjectType': {
        'api_class': None,
        'binding_name': 'gui_window_object',
        'namespace': 'http://cybox.mitre.org/objects#GUIWindowObject-2',
        'dependencies': 'GUIObjectType'
    },
    'HTTPSessionObjectType': {
        'api_class': 'cybox.objects.http_session_object.HTTPSession',
        'binding_name': 'http_session_object',
        'namespace': 'http://cybox.mitre.org/objects#HTTPSessionObject-2',
        'dependencies': 'AddressObjectType,PortObjectType,URIObjectType'
    },
    'LibraryObjectType': {
        'api_class':'cybox.objects.library_object.Library',
        'binding_name': 'library_object',
        'namespace': 'http://cybox.mitre.org/objects#LibraryObject-2',
    },
    'LinkObjectType': {
        'api_class': None,
        'binding_name': 'link_object',
        'namespace': 'http://cybox.mitre.org/objects#LinkObject-1',
        'dependencies': 'URIObjectType'
    },
    'LinuxPackageObjectType': {
        'api_class': None,
        'binding_name': 'linux_package_object',
        'namespace': 'http://cybox.mitre.org/objects#LinuxPackageObject-2',
    },
    'MemoryObjectType': {
        'api_class': 'cybox.objects.memory_object.Memory',
        'binding_name': 'memory_object',
        'namespace': 'http://cybox.mitre.org/objects#MemoryObject-2',
    },
    'MutexObjectType': {
        'api_class': 'cybox.objects.mutex_object.Mutex',
        'binding_name': 'mutex_object',
        'namespace': 'http://cybox.mitre.org/objects#MutexObject-2',
    },
    'NetworkConnectionObjectType': {
        'api_class': 'cybox.objects.network_connection_object.NetworkConnection',
        'binding_name': 'network_connection_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkConnectionObject-2',
        'dependencies': 'SocketAddressObjectType,HTTPSessionObjectType,DNSQueryObjectType,DNSRecordObjectType,URIObjectType'
    },
    'NetworkFlowObjectType': {
        'api_class': None,
        'binding_name': 'network_flow_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkFlowObject-2',
        'dependencies': 'NetworkPacketType,AddressObjectType,SocketAddressObjectType'
    },
    'NetworkPacketType': {
        'api_class': None,
        'binding_name': 'network_packet_object',
        'namespace': 'http://cybox.mitre.org/objects#PacketObject-2',
        'dependencies': 'AddressObjectType,PortObjectType'
    },
    'NetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'network_route_entry_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkRouteEntryObject-2',
        'dependencies': 'AddressObjectType'
    },
    'NetRouteObjectType': {
        'api_class': None,
        'binding_name': 'network_route_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkRouteObject-2',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'NetworkSocketObjectType': {
        'api_class': 'cybox.objects.network_socket_object.NetworkSocket',
        'binding_name': 'network_socket_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkSocketObject-2',
        'dependencies': 'SocketAddressObjectType'
    },
    'NetworkSubnetObjectType': {
        'api_class': None,
        'binding_name': 'network_subnet_object',
        'namespace': 'http://cybox.mitre.org/objects#NetworkSubnetObject-2',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'PDFFileObjectType': {
        'api_class': None,
        'binding_name': 'pdf_file_object',
        'namespace': 'http://cybox.mitre.org/objects#PDFFileObject-1',
    },
    'PipeObjectType': {
        'api_class': 'cybox.objects.pipe_object.Pipe',
        'binding_name': 'pipe_object',
        'namespace': 'http://cybox.mitre.org/objects#PipeObject-2',
    },
    'PortObjectType': {
        'api_class': 'cybox.objects.port_object.Port',
        'binding_name': 'port_object',
        'namespace': 'http://cybox.mitre.org/objects#PortObject-2',
    },
    'ProcessObjectType': {
        'api_class': 'cybox.objects.process_object.Process',
        'binding_name': 'process_object',
        'namespace': 'http://cybox.mitre.org/objects#ProcessObject-2',
        'dependencies': 'NetworkConnectionObjectType,PortObjectType'
    },
    'SemaphoreObjectType': {
        'api_class': None,
        'binding_name': 'semaphore_object',
        'namespace': 'http://cybox.mitre.org/objects#SemaphoreObject-2',
    },
    'SocketAddressObjectType': {
        'api_class': 'cybox.objects.socket_address_object.SocketAddress',
        'binding_name': 'socket_address_object',
        'namespace': 'http://cybox.mitre.org/objects#SocketAddressObject-1',
        'dependencies': 'AddressObjectType,PortObjectType'
    },
    'SystemObjectType': {
        'api_class': 'cybox.objects.system_object.System',
        'binding_name': 'system_object',
        'namespace': 'http://cybox.mitre.org/objects#SystemObject-2',
        'dependencies': 'AddressObjectType'
    },
    'UnixFileObjectType': {
        'api_class': None,
        'binding_name': 'unix_file_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixFileObject-2',
        'dependencies': 'FileObjectType'
    },
    'UnixNetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'unix_network_route_entry_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'UnixPipeObjectType': {
        'api_class': None,
        'binding_name': 'unix_pipe_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixPipeObject',
        'dependencies': 'PipeObjectType'
    },
    'UnixProcessObjectType': {
        'api_class': None,
        'binding_name': 'unix_process_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixProcessObject-2',
        'dependencies': 'ProcessObjectType,AddressObjectType,PortObjectType'
    },
    'UnixUserAccountObjectType': {
        'api_class': None,
        'binding_name': 'unix_user_account_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixUserAccountObject-2',
        'dependencies': 'UserAccountObjectType,AccountObjectType'
    },
    'UnixVolumeObjectType': {
        'api_class': None,
        'binding_name': 'unix_volume_object',
        'namespace': 'http://cybox.mitre.org/objects#UnixVolumeObject-2',
        'dependencies': 'VolumeObjectType'
    },
    'URIObjectType': {
        'api_class': 'cybox.objects.uri_object.URI',
        'binding_name': 'uri_object',
        'namespace': 'http://cybox.mitre.org/objects#URIObject-2',
    },
    'UserAccountObjectType': {
        'api_class': None,
        'binding_name': 'user_account_object',
        'namespace': 'http://cybox.mitre.org/objects#UserAccountObject-2',
        'dependencies': 'AccountObjectType'
    },
    'VolumeObjectType': {
        'api_class': None,
        'binding_name': 'volume_object',
        'namespace': 'http://cybox.mitre.org/objects#VolumeObject-2',
    },
    'WhoisObjectType': {
        'api_class': 'cybox.objects.whois_object.WhoisEntry',
        'binding_name': 'whois_object',
        'namespace': 'http://cybox.mitre.org/objects#WhoisObject-2',
        'dependencies': 'URIObjectType,AddressObjectType'
    },
    'WinComputerAccountObjectType': {
        'api_class': None,
        'binding_name': 'win_computer_account_object',
        'namespace': 'http://cybox.mitre.org/objects#WinComputerAccountObject-2',
        'dependencies': 'AccountObjectType,PortObjectType'
    },
    'WinCriticalSectionObjectType': {
        'api_class': None,
        'binding_name': 'win_critical_section_object',
        'namespace': 'http://cybox.mitre.org/objects#WinCriticalSectionObject-2',
    },
    'WindowsDriverObjectType': {
        'api_class': 'cybox.objects.win_driver_object.WinDriver',
        'binding_name': 'win_driver_object',
        'namespace': 'http://cybox.mitre.org/objects#WinDriverObject-2',
    },
    'WindowsEventLogObjectType': {
        'api_class': None,
        'binding_name': 'win_event_log_object',
        'namespace': 'http://cybox.mitre.org/objects#WinEventLogObject-2',
    },
    'WindowsEventObjectType': {
        'api_class': 'cybox.objects.win_event_object.WinEvent',
        'binding_name': 'win_event_object',
        'namespace': 'http://cybox.mitre.org/objects#WinEventObject-2',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsExecutableFileObjectType': {
        'api_class': 'cybox.objects.win_executable_file_object.WinExecutableFile',
        'binding_name': 'win_executable_file_object',
        'namespace': 'http://cybox.mitre.org/objects#WinExecutableFileObject-2',
        'dependencies': 'WindowsFileObjectType,FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'
    },
    'WindowsFileObjectType': {
        'api_class': 'cybox.objects.win_file_object.WinFile',
        'binding_name': 'win_file_object',
        'namespace': 'http://cybox.mitre.org/objects#WinFileObject-2',
        'dependencies': 'FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'
    },
    'WindowsHandleObjectType': {
        'api_class': 'cybox.objects.win_handle_object.WinHandle',
        'binding_name': 'win_handle_object',
        'namespace': 'http://cybox.mitre.org/objects#WinHandleObject-2',
    },
    'WindowsKernelHookObjectType': {
        'api_class': 'cybox.objects.win_kernel_hook_object.WinKernelHook',
        'binding_name': 'win_kernel_hook_object',
        'namespace': 'http://cybox.mitre.org/objects#WinKernelHookObject-2',
    },
    'WindowsKernelObjectType': {
        'api_class': None,
        'binding_name': 'win_kernel_object',
        'namespace': 'http://cybox.mitre.org/objects#WinKernelObject-2',
    },
    'WindowsMailslotObjectType': {
        'api_class': None,
        'binding_name': 'win_mailslot_object',
        'namespace': 'http://cybox.mitre.org/objects#WinMailslotObject-2',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsMemoryPageRegionObjectType': {
        'api_class': None,
        'binding_name': 'win_memory_page_region_object',
        'namespace': 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2',
        'dependencies': 'MemoryObjectType'
    },
    'WindowsMutexObjectType': {
        'api_class': 'cybox.objects.win_mutex_object.WinMutex',
        'binding_name': 'win_mutex_object',
        'namespace': 'http://cybox.mitre.org/objects#WinMutexObject-2',
        'dependencies': 'WindowsHandleObjectType,MutexObjectType'
    },
    'WindowsNetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'win_network_route_entry_object',
        'namespace': 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'WindowsNetworkShareObjectType': {
        'api_class': 'cybox.objects.win_network_share_object.WinNetworkShare',
        'binding_name': 'win_network_share_object',
        'namespace': 'http://cybox.mitre.org/objects#WinNetworkShareObject-2',
    },
    'WindowsPipeObjectType': {
        'api_class': 'cybox.objects.win_pipe_object.WinPipe',
        'binding_name': 'win_pipe_object',
        'namespace': 'http://cybox.mitre.org/objects#WinPipeObject-2',
        'dependencies': 'PipeObjectType'
    },
    'WindowsPrefetchObjectType': {
        'api_class': None,
        'binding_name': 'win_prefetch_object',
        'namespace': 'http://cybox.mitre.org/objects#WinPrefetchObject-2',
        'dependencies': 'WindowsVolumeObjectType,VolumeObjectType,DeviceObjectType'
    },
    'WindowsProcessObjectType': {
        'api_class': 'cybox.objects.win_process_object.WinProcess',
        'binding_name': 'win_process_object',
        'namespace': 'http://cybox.mitre.org/objects#WinProcessObject-2',
        'dependencies': 'ProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'
    },
    'WindowsRegistryKeyObjectType': {
        'api_class': 'cybox.objects.win_registry_key_object.WinRegistryKey',
        'binding_name': 'win_registry_key_object',
        'namespace': 'http://cybox.mitre.org/objects#WinRegistryKeyObject-2',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsSemaphoreObjectType': {
        'api_class': None,
        'binding_name': 'win_semaphore_object',
        'namespace': 'http://cybox.mitre.org/objects#WinSemaphoreObject-2',
        'dependencies': 'WindowsHandleObjectType,SemaphoreObjectType'
    },
    'WindowsServiceObjectType': {
        'api_class': 'cybox.objects.win_service_object.WinService',
        'binding_name': 'win_service_object',
        'namespace': 'http://cybox.mitre.org/objects#WinServiceObject-2',
        'dependencies': 'WindowsProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'
    },
    'WindowsSystemObjectType': {
        'api_class': 'cybox.objects.win_system_object.WinSystem',
        'binding_name': 'win_system_object',
        'namespace': 'http://cybox.mitre.org/objects#WinSystemObject-2',
        'dependencies': 'WindowsHandleObjectType,SystemObjectType,AddressObjectType'
    },
    'WindowsSystemRestoreObjectType': {
        'api_class': None,
        'binding_name': 'win_system_restore_object',
        'namespace': 'http://cybox.mitre.org/objects#WinSystemRestoreObject-2',
    },
    'WindowsTaskObjectType': {
        'api_class': None,
        'binding_name': 'win_task_object',
        'namespace': 'http://cybox.mitre.org/objects#WinTaskObject-2',
        'dependencies': 'EmailMessageObjectType,FileObjectType,AddressObjectType,URIObjectType'
    },
    'WindowsThreadObjectType': {
        'api_class': None,
        'binding_name': 'win_thread_object',
        'namespace': 'http://cybox.mitre.org/objects#WinThreadObject-2',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsUserAccountObjectType': {
        'api_class': None,
        'binding_name': 'win_user_account_object',
        'namespace': 'http://cybox.mitre.org/objects#WinUserAccountObject-2',
        'dependencies': 'UserAccountObjectType,AccountObjectType'
    },
    'WindowsVolumeObjectType': {
        'api_class': None,
        'binding_name': 'win_volume_object',
        'namespace': 'http://cybox.mitre.org/objects#WinVolumeObject-2',
        'dependencies': 'VolumeObjectType'
    },
    'WindowsWaitableTimerObjectType': {
        'api_class': None,
        'binding_name': 'win_waitable_timer_object',
        'namespace': 'http://cybox.mitre.org/objects#WinWaitableTimerObject-2',
        'dependencies': 'WindowsHandleObjectType'
    },
    'X509CertificateObjectType': {
        'api_class': None,
        'binding_name': 'x509_certificate_object',
        'namespace': 'http://cybox.mitre.org/objects#X509CertificateObject-2',
    },

    # These are just for testing. Please don't attempt to use!
    "!!MissingAPIClass": {},
    "!!MissingModule": {'api_class': 'some.nonexistent.module'},
    "!!BadClassName": {'api_class': 'cybox.utils.NonexistentClass'},
}


META = Metadata()


class NamespaceParser(object):
    '''Functions for finding out the namespaces used within Observables'''

    def __init__(self, observable_list):
        self.observable_list = observable_list if observable_list else []
        self.object_types = []
        self.object_type_dependencies = []

        # parse the observables, build our lists
        self.get_object_namespaces()

    #Functions for grabbing the namespaces of all objects in the current Observables instance
    def get_object_namespaces(self):
        for observable in self.observable_list:
            self.process_observable_namespace(observable)

    def process_event_namespace(self, event):
        if event.get_Actions() is not None:
            for action in event.get_Actions().get_Action():
                for associated_object in action.get_Associated_Objects().get_Associated_Object():
                    self.get_namespace_from_object(associated_object)

        if event.get_Event() is not None:
            for embedded_event in event.get_Event():
                self.process_event_namespace(embedded_event)

    def process_observable_namespace(self, observable):
        if observable.get_Object() is not None:
            self.get_namespace_from_object(observable.get_Object())

        elif observable.get_Event() is not None:
            self.process_event_namespace(observable.get_Event())

        elif observable.get_Observable_Composition() is not None:
            for embedded_observable in observable.get_Observable_Composition().get_Observable():
                self.process_observable_namespace(embedded_observable)

    def get_namespace_from_object(self, object):
        if object.get_Properties() is not None:
            object_properties = object.get_Properties()

            if object_properties.get_xsi_type() is not None:
                xsi_type = object_properties.get_xsi_type()
                self.get_defined_object_namespace(xsi_type)

        if object.get_Discovery_Method() is not None:
            discovery_method = object.get_Discovery_Method()

            if discovery_method.get_System() is not None:
                self.add_object_namespace('SystemObjectType')

            if discovery_method.get_Tools() is not None:
                for tool in discovery_method.get_Tools().get_Tool():
                    if tool.get_Execution_Environment() is not None:
                        execution_environment = tool.get_Execution_Environment()

                        if execution_environment.get_System() is not None:
                            self.add_object_namespace('SystemObjectType')

                        if execution_environment.get_User_Account_Info() is not None:
                            self.add_object_namespace('UserAccountObjectType')

            if discovery_method.get_Instance() is not None:
                self.add_object_namespace('ProcessObjectType')

    def get_defined_object_namespace(self, xsi_type):
        if xsi_type.split(':')[1] in OBJECT_TYPES_DICT:
            self.add_object_namespace(xsi_type.split(':')[1])

    def add_object_namespace(self, object_type):
        if object_type not in self.object_types:
            #Add the object type
            self.object_types.append(object_type)

            #Add any dependencies
            if OBJECT_TYPES_DICT.get(object_type).get('dependencies') is not None:
                dependencies = OBJECT_TYPES_DICT.get(object_type).get('dependencies').split(',')

                for dependency in dependencies:
                    if dependency not in self.object_types and dependency not in self.object_type_dependencies:
                        self.object_type_dependencies.append(dependency)

    def build_namespaces_schemalocations_str(self):
        '''Build the namespace/schemalocation declaration string'''

        output_string = '\n '
        schemalocs = []
        #Add the XSI and CybOX Core/Common namespaces and schemalocation
        output_string += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n '
        output_string += 'xmlns:cybox="http://cybox.mitre.org/cybox-2" \n '
        output_string += 'xmlns:cyboxCommon="http://cybox.mitre.org/common-2" \n '
        schemalocs.append('http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.0/cybox_core.xsd')

        for object_type in self.object_types:
            namespace = OBJECT_TYPES_DICT.get(object_type).get('namespace')
            namespace_prefix = META.lookup_namespace(namespace).prefix
            output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')

        for object_type_dependency in self.object_type_dependencies:
            if object_type_dependency not in self.object_types:
                namespace = OBJECT_TYPES_DICT.get(object_type_dependency).get('namespace')
                namespace_prefix = META.lookup_namespace(namespace).prefix
                output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')

        output_string += 'xsi:schemaLocation="'

        for object_type in self.object_types:
            namespace = OBJECT_TYPES_DICT.get(object_type).get('namespace')
            namespace_prefix = META.lookup_namespace(namespace).prefix
            schemalocation = META.lookup_namespace(namespace).schema_location
            schemalocs.append(' ' + namespace + ' ' + schemalocation)

        for schemalocation_string in schemalocs:
            if schemalocs.index(schemalocation_string) == (len(schemalocs) - 1):
                output_string += (schemalocation_string + '"')
            else:
                output_string += (schemalocation_string + '\n')

        return output_string

    def get_namespace_dict(self):
        '''returns a dictionary of namespace->(prefix, schemalocation)'''

        namespace_dict = {
            'http://www.w3.org/2001/XMLSchema-instance': ['xsi', ''],
            'http://cybox.mitre.org/cybox-2': ['cybox', 'http://cybox.mitre.org/XMLSchema/core/2.0/cybox_core.xsd'],
            'http://cybox.mitre.org/common-2': ['cyboxCommon', 'http://cybox.mitre.org/XMLSchema/common/2.0/cybox_common.xsd']
        }

        for object_type in itertools.chain(self.object_types, self.object_type_dependencies):
            namespace = OBJECT_TYPES_DICT.get(object_type).get('namespace')
            ns = META.lookup_namespace(namespace)

            namespace_dict[namespace] = [ns.prefix, ns.schema_location]

        return namespace_dict
