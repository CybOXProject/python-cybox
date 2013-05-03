import itertools

#Dictionary for storing Defined Objects, their main types, namespaces, and schemalocations
OBJECT_TYPES_DICT = {
    'AccountObjectType': {
        'api_class': None,
        'binding_name': 'account_object',
        'namespace_prefix': 'AccountObj',
        'namespace': 'http://cybox.mitre.org/objects#AccountObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Account/2.0/Account_Object.xsd'
    },
    'AddressObjectType': {
        'api_class': 'cybox.objects.address_object.Address',
        'binding_name': 'address_object',
        'namespace_prefix': 'AddressObj',
        'namespace': 'http://cybox.mitre.org/objects#AddressObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Address/2.0/Address_Object.xsd'
    },
    'APIObjectType': {
        'api_class': None,
        'binding_name': 'api_object',
        'namespace_prefix': 'APIObj',
        'namespace': 'http://cybox.mitre.org/objects#APIObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/API/2.0/API_Object.xsd'
    },
    'ArtifactObjectType': {
        'api_class': 'cybox.objects.artifact_object.Artifact',
        'binding_name': 'artifact_object',
        'namespace_prefix': 'ArtifactObj',
        'namespace': 'http://cybox.mitre.org/objects#ArtifactObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Artifact/2.0/Artifact_Object.xsd'
    },
    'CodeObjectType': {
        'api_class': None,
        'binding_name': 'code_object',
        'namespace_prefix': 'CodeObj',
        'namespace': 'http://cybox.mitre.org/objects#CodeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Code/2.0/Code_Object.xsd'
    },
    'CustomObjectType': {
        'api_class': None,
        'binding_name': 'custom_object',
        'namespace_prefix': 'CustomObj',
        'namespace': 'http://cybox.mitre.org/objects#CustomObject-1',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Custom/1.0/Custom_Object.xsd'
    },
    'DeviceObjectType': {
        'api_class': None,
        'binding_name': 'device_object',
        'namespace_prefix': 'DeviceObj',
        'namespace': 'http://cybox.mitre.org/objects#DeviceObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Device/2.0/Device_Object.xsd'
    },
    'DiskObjectType': {
        'api_class': None,
        'binding_name': 'disk_object',
        'namespace_prefix': 'DiskObj',
        'namespace': 'http://cybox.mitre.org/objects#DiskObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Disk/2.0/Disk_Object.xsd',
        'dependencies': 'DiskPartitionObjectType'
    },
    'DiskPartitionObjectType': {
        'api_class': None,
        'binding_name': 'disk_partition_object',
        'namespace_prefix': 'DiskPartitionObj',
        'namespace': 'http://cybox.mitre.org/objects#DiskPartitionObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Disk_Partition/2.0/Disk_Partition_Object.xsd'
    },
    'DNSCacheEntryType': {
        'api_class': None,
        'binding_name': 'dns_cache_object',
        'namespace_prefix': 'DNSCacheObj',
        'namespace': 'http://cybox.mitre.org/objects#DNSCacheObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/DNS_Cache/2.0/DNS_Cache_Object.xsd',
        'dependencies': 'DNSRecordObjectType,AddressObjectType,URIObjectType'
    },
    'DNSQueryObjectType': {
        'api_class': None,
        'binding_name': 'dns_query_object',
        'namespace_prefix': 'DNSQueryObj',
        'namespace': 'http://cybox.mitre.org/objects#DNSQueryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/DNS_Query/2.0/DNS_Query_Object.xsd',
        'dependencies': 'DNSRecordObjectType,URIObjectType,AddressObjectType'
    },
    'DNSRecordObjectType': {
        'api_class': None,
        'binding_name': 'dns_record_object',
        'namespace_prefix': 'DNSRecordObj',
        'namespace': 'http://cybox.mitre.org/objects#DNSRecordObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/DNS_Record/2.0/DNS_Record_Object.xsd',
        'dependencies': 'URIObjectType,AddressObjectType'
    },
    'EmailMessageObjectType': {
        'api_class': 'cybox.objects.email_message_object.EmailMessage',
        'binding_name': 'email_message_object',
        'namespace_prefix': 'EmailMessageObj',
        'namespace': 'http://cybox.mitre.org/objects#EmailMessageObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Email_Message/2.0/Email_Message_Object.xsd',
        'dependencies': 'FileObjectType,AddressObjectType,URIObjectType'
    },
    'FileObjectType': {
        'api_class': 'cybox.objects.file_object.File',
        'binding_name': 'file_object',
        'namespace_prefix': 'FileObj',
        'namespace': 'http://cybox.mitre.org/objects#FileObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/File/2.0/File_Object.xsd'
    },
    'GUIDialogboxObjectType': {
        'api_class': None,
        'binding_name': 'gui_dialogbox_object',
        'namespace_prefix': 'GUIDialogboxObj',
        'namespace': 'http://cybox.mitre.org/objects#GUIDialogboxObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/GUI_Dialogbox/2.0/GUI_Dialogbox_Object.xsd',
        'dependencies': 'GUIObjectType'
    },
    'GUIObjectType': {
        'api_class': None,
        'binding_name': 'gui_object',
        'namespace_prefix': 'GUIObj',
        'namespace': 'http://cybox.mitre.org/objects#GUIObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/GUI/2.0/GUI_Object.xsd'
    },
    'GUIWindowObjectType': {
        'api_class': None,
        'binding_name': 'gui_window_object',
        'namespace_prefix': 'GUIWindowOb',
        'namespace': 'http://cybox.mitre.org/objects#GUIWindowObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/GUI_Window/2.0/GUI_Window_Object.xsd',
        'dependencies': 'GUIObjectType'
    },
    'HTTPSessionObjectType': {
        'api_class': None,
        'binding_name': 'http_session_object',
        'namespace_prefix': 'HTTPSessionObj',
        'namespace': 'http://cybox.mitre.org/objects#HTTPSessionObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/HTTP_Session/2.0/HTTP_Session_Object.xsd',
        'dependencies': 'AddressObjectType,PortObjectType,URIObjectType'
    },
    'LibraryObjectType': {
        'api_class': None,
        'binding_name': 'library_object',
        'namespace_prefix': 'LibraryObj',
        'namespace': 'http://cybox.mitre.org/objects#LibraryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Library/2.0/Library_Object.xsd'
    },
    'LinkObjectType': {
        'api_class': None,
        'binding_name': 'link_object',
        'namespace_prefix': 'LinkObj',
        'namespace': 'http://cybox.mitre.org/objects#LinkObject-1',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Link/1.0/Link_Object.xsd',
        'dependencies': 'URIObjectType'
    },
    'LinuxPackageObjectType': {
        'api_class': None,
        'binding_name': 'linux_package_object',
        'namespace_prefix': 'LinuxPackageObj',
        'namespace': 'http://cybox.mitre.org/objects#LinuxPackageObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Linux_Package/2.0/Linux_Package_Object.xsd'
    },
    'MemoryObjectType': {
        'api_class': None,
        'binding_name': 'memory_object',
        'namespace_prefix': 'MemoryObj',
        'namespace': 'http://cybox.mitre.org/objects#MemoryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Memory/2.0/Memory_Object.xsd'
    },
    'MutexObjectType': {
        'api_class': None,
        'binding_name': 'mutex_object',
        'namespace_prefix': 'MutexObj',
        'namespace': 'http://cybox.mitre.org/objects#MutexObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Mutex/2.0/Mutex_Object.xsd'
    },
    'NetworkConnectionObjectType': {
        'api_class': None,
        'binding_name': 'network_connection_object',
        'namespace_prefix': 'NetworkConnectionObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkConnectionObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Connection/2.0/Network_Connection_Object.xsd',
        'dependencies': 'SocketAddressObjectType,HTTPSessionObjectType,DNSQueryObjectType,DNSRecordObjectType,URIObjectType'
    },
    'NetworkFlowObjectType': {
        'api_class': None,
        'binding_name': 'network_flow_object',
        'namespace_prefix': 'NetFlowObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkFlowObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Flow/2.0/Network_Flow_Object.xsd',
        'dependencies': 'NetworkPacketType,AddressObjectType,SocketAddressObjectType'
    },
    'NetworkPacketType': {
        'api_class': None,
        'binding_name': 'network_packet_object',
        'namespace_prefix': 'PacketObj',
        'namespace': 'http://cybox.mitre.org/objects#PacketObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Packet/2.0/Network_Packet_Object.xsd',
        'dependencies': 'AddressObjectType,PortObjectType'
    },
    'NetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'network_route_entry_object',
        'namespace_prefix': 'NetworkRouteEntryObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkRouteEntryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Route_Entry/2.0/Network_Route_Entry_Object.xsd',
        'dependencies': 'AddressObjectType'
    },
    'NetRouteObjectType': {
        'api_class': None,
        'binding_name': 'network_route_object',
        'namespace_prefix': 'NetworkRouteObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkRouteObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Route/2.0/Network_Route_Object.xsd',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'NetworkSocketObjectType': {
        'api_class': None,
        'binding_name': 'network_socket_object',
        'namespace_prefix': 'NetworkSocketObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkSocketObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Socket/2.0/Socket_Object.xsd',
        'dependencies': 'SocketAddressObjectType'
    },
    'NetworkSubnetObjectType': {
        'api_class': None,
        'binding_name': 'network_subnet_object',
        'namespace_prefix': 'NetworkSubnetObj',
        'namespace': 'http://cybox.mitre.org/objects#NetworkSubnetObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Network_Subnet/2.0/Network_Subnet_Object.xsd',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'PDFFileObjectType': {
        'api_class': None,
        'binding_name': 'pdf_file_object',
        'namespace_prefix': 'PDFFileObj',
        'namespace': 'http://cybox.mitre.org/objects#PDFFileObject-1',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/PDF_File/1.0/PDF_File_Object.xsd'
    },
    'PipeObjectType': {
        'api_class': None,
        'binding_name': 'pipe_object',
        'namespace_prefix': 'PipeObj',
        'namespace': 'http://cybox.mitre.org/objects#PipeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Pipe/2.0/Pipe_Object.xsd'
    },
    'PortObjectType': {
        'api_class': 'cybox.objects.port_object.Port',
        'binding_name': 'port_object',
        'namespace_prefix': 'PortObj',
        'namespace': 'http://cybox.mitre.org/objects#PortObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Port/2.0/Port_Object.xsd'
    },
    'ProcessObjectType': {
        'api_class': None,
        'binding_name': 'process_object',
        'namespace_prefix': 'ProcessObj',
        'namespace': 'http://cybox.mitre.org/objects#ProcessObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Process/2.0/Process_Object.xsd',
        'dependencies': 'NetworkConnectionObjectType,PortObjectType'
    },
    'SemaphoreObjectType': {
        'api_class': None,
        'binding_name': 'semaphore_object',
        'namespace_prefix': 'SemaphoreObj',
        'namespace': 'http://cybox.mitre.org/objects#SemaphoreObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Semaphore/2.0/Semaphore_Object.xsd'
    },
    'SocketAddressObjectType': {
        'api_class': None,
        'binding_name': 'socket_address_object',
        'namespace_prefix': 'SocketAddressObj',
        'namespace': 'http://cybox.mitre.org/objects#SocketAddressObject-1',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Socket_Address/1.0/Socket_Address_Object.xsd',
        'dependencies': 'AddressObjectType,PortObjectType'
    },
    'SystemObjectType': {
        'api_class': None,
        'binding_name': 'system_object',
        'namespace_prefix': 'SystemObj',
        'namespace': 'http://cybox.mitre.org/objects#SystemObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/System/2.0/System_Object.xsd',
        'dependencies': 'AddressObjectType'
    },
    'UnixFileObjectType': {
        'api_class': None,
        'binding_name': 'unix_file_object',
        'namespace_prefix': 'UnixFileObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixFileObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_File/2.0/Unix_File_Object.xsd',
        'dependencies': 'FileObjectType'
    },
    'UnixNetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'unix_network_route_entry_object',
        'namespace_prefix': 'UnixNetworkRouteEntryObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_Network_Route_Entry/2.0/Unix_Network_Route_Entry_Object.xsd',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'UnixPipeObjectType': {
        'api_class': None,
        'binding_name': 'unix_pipe_object',
        'namespace_prefix': 'UnixPipeObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixPipeObject',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_Pipe/2.0/Unix_Pipe_Object.xsd',
        'dependencies': 'PipeObjectType'
    },
    'UnixProcessObjectType': {
        'api_class': None,
        'binding_name': 'unix_process_object',
        'namespace_prefix': 'UnixProcessObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixProcessObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_Process/2.0/Unix_Process_Object.xsd',
        'dependencies': 'ProcessObjectType,AddressObjectType,PortObjectType'
    },
    'UnixUserAccountObjectType': {
        'api_class': None,
        'binding_name': 'unix_user_account_object',
        'namespace_prefix': 'UnixUserAccountObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixUserAccountObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_User_Account/2.0/Unix_User_Account_Object.xsd',
        'dependencies': 'UserAccountObjectType,AccountObjectType'
    },
    'UnixVolumeObjectType': {
        'api_class': None,
        'binding_name': 'unix_volume_object',
        'namespace_prefix': 'UnixVolumeObj',
        'namespace': 'http://cybox.mitre.org/objects#UnixVolumeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Unix_Volume/2.0/Unix_Volume_Object.xsd',
        'dependencies': 'VolumeObjectType'
    },
    'URIObjectType': {
        'api_class': 'cybox.objects.uri_object.URI',
        'binding_name': 'uri_object',
        'namespace_prefix': 'URIObj',
        'namespace': 'http://cybox.mitre.org/objects#URIObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/URI/2.0/URI_Object.xsd'
    },
    'UserAccountObjectType': {
        'api_class': None,
        'binding_name': 'user_account_object',
        'namespace_prefix': 'UserAccountObj',
        'namespace': 'http://cybox.mitre.org/objects#UserAccountObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/User_Account/2.0/User_Account_Object.xsd',
        'dependencies': 'AccountObjectType'
    },
    'VolumeObjectType': {
        'api_class': None,
        'binding_name': 'volume_object',
        'namespace_prefix': 'VolumeObj',
        'namespace': 'http://cybox.mitre.org/objects#VolumeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Volume/2.0/Volume_Object.xsd'
    },
    'WhoisObjectType': {
        'api_class': None,
        'binding_name': 'whois_object',
        'namespace_prefix': 'WhoisObj',
        'namespace': 'http://cybox.mitre.org/objects#WhoisObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Whois/2.0/Whois_Object.xsd',
        'dependencies': 'URIObjectType,AddressObjectType'
    },
    'WinComputerAccountObjectType': {
        'api_class': None,
        'binding_name': 'win_computer_account_object',
        'namespace_prefix': 'WinComputerAccountObj',
        'namespace': 'http://cybox.mitre.org/objects#WinComputerAccountObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Computer_Account/2.0/Win_Computer_Account_Object.xsd',
        'dependencies': 'AccountObjectType,PortObjectType'
    },
    'WinCriticalSectionObjectType': {
        'api_class': None,
        'binding_name': 'win_critical_section_object',
        'namespace_prefix': 'WinCriticalSectionObj',
        'namespace': 'http://cybox.mitre.org/objects#WinCriticalSectionObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Critical_Section/2.0/Win_Critical_Section_Object.xsd'
    },
    'WindowsDriverObjectType': {
        'api_class': 'cybox.objects.win_driver_object.WinDriver',
        'binding_name': 'win_driver_object',
        'namespace_prefix': 'WinDriverObj',
        'namespace': 'http://cybox.mitre.org/objects#WinDriverObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Driver/2.0/Win_Driver_Object.xsd'
    },
    'WindowsEventLogObjectType': {
        'api_class': None,
        'binding_name': 'win_event_log_object',
        'namespace_prefix': 'WinEventLogObj',
        'namespace': 'http://cybox.mitre.org/objects#WinEventLogObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Event_Log/2.0/Win_Event_Log_Object.xsd'
    },
    'WindowsEventObjectType': {
        'api_class': 'cybox.objects.win_event_object.WinEvent',
        'binding_name': 'win_event_object',
        'namespace_prefix': 'WinEventObj',
        'namespace': 'http://cybox.mitre.org/objects#WinEventObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Event/2.0/Win_Event_Object.xsd',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsExecutableFileObjectType': {
        'api_class': None,
        'binding_name': 'win_executable_file_object',
        'namespace_prefix': 'WinExecutableFileObj',
        'namespace': 'http://cybox.mitre.org/objects#WinExecutableFileObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Executable_File/2.0/Win_Executable_File_Object.xsd',
        'dependencies': 'WindowsFileObjectType,FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'
    },
    'WindowsFileObjectType': {
        'api_class': None,
        'binding_name': 'win_file_object',
        'namespace_prefix': 'WinFileObj',
        'namespace': 'http://cybox.mitre.org/objects#WinFileObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_File/2.0/Win_File_Object.xsd',
        'dependencies': 'FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'
    },
    'WindowsHandleObjectType': {
        'api_class': None,
        'binding_name': 'win_handle_object',
        'namespace_prefix': 'WinHandleObj',
        'namespace': 'http://cybox.mitre.org/objects#WinHandleObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Handle/2.0/Win_Handle_Object.xsd'
    },
    'WindowsKernelHookObjectType': {
        'api_class': 'cybox.objects.win_kernel_hook_object.WinKernelHook',
        'binding_name': 'win_kernel_hook_object',
        'namespace_prefix': 'WinKernelHookObj',
        'namespace': 'http://cybox.mitre.org/objects#WinKernelHookObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel_Hook/2.0/Win_Kernel_Hook_Object.xsd'
    },
    'WindowsKernelObjectType': {
        'api_class': None,
        'binding_name': 'win_kernel_object',
        'namespace_prefix': 'WinKernelObj',
        'namespace': 'http://cybox.mitre.org/objects#WinKernelObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel/2.0/Win_Kernel_Object.xsd'
    },
    'WindowsMailslotObjectType': {
        'api_class': None,
        'binding_name': 'win_mailslot_object',
        'namespace_prefix': 'WinMailslotObj',
        'namespace': 'http://cybox.mitre.org/objects#WinMailslotObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Mailslot/2.0/Win_Mailslot_Object.xsd',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsMemoryPageRegionObjectType': {
        'api_class': None,
        'binding_name': 'win_memory_page_region_object',
        'namespace_prefix': 'WinMemoryPageRegionObj',
        'namespace': 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Memory_Page_Region/2.0/Win_Memory_Page_Region_Object.xsd',
        'dependencies': 'MemoryObjectType'
    },
    'WindowsMutexObjectType': {
        'api_class': 'cybox.objects.win_mutex_object.WinMutex',
        'binding_name': 'win_mutex_object',
        'namespace_prefix': 'WinMutexObj',
        'namespace': 'http://cybox.mitre.org/objects#WinMutexObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Mutex/2.0/Win_Mutex_Object.xsd',
        'dependencies': 'WindowsHandleObjectType,MutexObjectType'
    },
    'WindowsNetworkRouteEntryObjectType': {
        'api_class': None,
        'binding_name': 'win_network_route_entry_object',
        'namespace_prefix': 'WinNetworkRouteEntryObj',
        'namespace': 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Route_Entry/2.0/Win_Network_Route_Entry_Object.xsd',
        'dependencies': 'NetworkRouteEntryObjectType,AddressObjectType'
    },
    'WindowsNetworkShareObjectType': {
        'api_class': None,
        'binding_name': 'win_network_share_object',
        'namespace_prefix': 'WinNetworkShareObj',
        'namespace': 'http://cybox.mitre.org/objects#WinNetworkShareObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Share/2.0/Win_Network_Share_Object.xsd'
    },
    'WindowsPipeObjectType': {
        'api_class': None,
        'binding_name': 'win_pipe_object',
        'namespace_prefix': 'WinPipeObj',
        'namespace': 'http://cybox.mitre.org/objects#WinPipeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Pipe/2.0/Win_Pipe_Object.xsd',
        'dependencies': 'PipeObjectType'
    },
    'WindowsPrefetchObjectType': {
        'api_class': None,
        'binding_name': 'win_prefetch_object',
        'namespace_prefix': 'WinPrefetchObj',
        'namespace': 'http://cybox.mitre.org/objects#WinPrefetchObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Prefetch/2.0/Win_Prefetch_Object.xsd',
        'dependencies': 'WindowsVolumeObjectType,VolumeObjectType,DeviceObjectType'
    },
    'WindowsProcessObjectType': {
        'api_class': 'cybox.objects.win_process_object.WinProcess',
        'binding_name': 'win_process_object',
        'namespace_prefix': 'WinProcessObj',
        'namespace': 'http://cybox.mitre.org/objects#WinProcessObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Process/2.0/Win_Process_Object.xsd',
        'dependencies': 'ProcessObjectType, WindowsHandleObjectType, MemoryObjectType,AddressObjectType,PortObjectType'
    },
    'WindowsRegistryKeyObjectType': {
        'api_class': 'cybox.objects.win_registry_key_object.WinRegistryKey',
        'binding_name': 'win_registry_key_object',
        'namespace_prefix': 'WinRegistryKeyObj',
        'namespace': 'http://cybox.mitre.org/objects#WinRegistryKeyObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Registry_Key/2.0/Win_Registry_Key_Object.xsd',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsSemaphoreObjectType': {
        'api_class': None,
        'binding_name': 'win_semaphore_object',
        'namespace_prefix': 'WinSemaphoreObj',
        'namespace': 'http://cybox.mitre.org/objects#WinSemaphoreObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Semaphore/2.0/Win_Semaphore_Object.xsd',
        'dependencies': 'WindowsHandleObjectType,SemaphoreObjectType'
    },
    'WindowsServiceObjectType': {
        'api_class': 'cybox.objects.win_service_object.WinService',
        'binding_name': 'win_service_object',
        'namespace_prefix': 'WinServiceObj',
        'namespace': 'http://cybox.mitre.org/objects#WinServiceObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Service/2.0/Win_Service_Object.xsd',
        'dependencies': 'WindowsProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'
    },
    'WindowsSystemObjectType': {
        'api_class': None,
        'binding_name': 'win_system_object',
        'namespace_prefix': 'WinSystemObj',
        'namespace': 'http://cybox.mitre.org/objects#WinSystemObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_System/2.0/Win_System_Object.xsd',
        'dependencies': 'WindowsHandleObjectType,SystemObjectType,AddressObjectType'
    },
    'WindowsSystemRestoreObjectType': {
        'api_class': None,
        'binding_name': 'win_system_restore_object',
        'namespace_prefix': 'WinSystemRestoreObj',
        'namespace': 'http://cybox.mitre.org/objects#WinSystemRestoreObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_System_Restore/2.0/Win_System_Restore_Object.xsd'
    },
    'WindowsTaskObjectType': {
        'api_class': None,
        'binding_name': 'win_task_object',
        'namespace_prefix': 'WinTaskObj',
        'namespace': 'http://cybox.mitre.org/objects#WinTaskObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Task/2.0/Win_Task_Object.xsd',
        'dependencies': 'EmailMessageObjectType,FileObjectType,AddressObjectType,URIObjectType'
    },
    'WindowsThreadObjectType': {
        'api_class': None,
        'binding_name': 'win_thread_object',
        'namespace_prefix': 'WinThreadObj',
        'namespace': 'http://cybox.mitre.org/objects#WinThreadObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Thread/2.0/Win_Thread_Object.xsd',
        'dependencies': 'WindowsHandleObjectType'
    },
    'WindowsUserAccountObjectType': {
        'api_class': None,
        'binding_name': 'win_user_account_object',
        'namespace_prefix': 'WinUserAccountObj',
        'namespace': 'http://cybox.mitre.org/objects#WinUserAccountObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_User_Account/2.0/Win_User_Account_Object.xsd',
        'dependencies': 'UserAccountObjectType,AccountObjectType'
    },
    'WindowsVolumeObjectType': {
        'api_class': None,
        'binding_name': 'win_volume_object',
        'namespace_prefix': 'WinVolumeObj',
        'namespace': 'http://cybox.mitre.org/objects#WinVolumeObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Volume/2.0/Win_Volume_Object.xsd',
        'dependencies': 'VolumeObjectType'
    },
    'WindowsWaitableTimerObjectType': {
        'api_class': None,
        'binding_name': 'win_waitable_timer_object',
        'namespace_prefix': 'WinWaitableTimerObj',
        'namespace': 'http://cybox.mitre.org/objects#WinWaitableTimerObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/Win_Waitable_Timer/2.0/Win_Waitable_Timer_Object.xsd',
        'dependencies': 'WindowsHandleObjectType'
    },
    'X509CertificateObjectType': {
        'api_class': None,
        'binding_name': 'x509_certificate_object',
        'namespace_prefix': 'X509CertificateObj',
        'namespace': 'http://cybox.mitre.org/objects#X509CertificateObject-2',
        'schemalocation': 'http://cybox.mitre.org/XMLSchema/objects/X509_Certificate/2.0/X509_Certificate_Object.xsd'
    },

    # These are just for testing. Please don't attempt to use!
    "!!MissingAPIClass": {},
    "!!MissingModule": {'api_class': 'some.nonexistent.module'},
    "!!BadClassName": {'api_class': 'cybox.utils.NonexistentClass'},
}


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
            namespace_prefix = OBJECT_TYPES_DICT.get(object_type).get('namespace_prefix')
            namespace = OBJECT_TYPES_DICT.get(object_type).get('namespace')
            output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')

        for object_type_dependency in self.object_type_dependencies:
            if object_type_dependency not in self.object_types:
                namespace_prefix = OBJECT_TYPES_DICT.get(object_type_dependency).get('namespace_prefix')
                namespace = OBJECT_TYPES_DICT.get(object_type_dependency).get('namespace')
                output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')

        output_string += 'xsi:schemaLocation="'

        for object_type in self.object_types:
            namespace = OBJECT_TYPES_DICT.get(object_type).get('namespace')
            schemalocation = OBJECT_TYPES_DICT.get(object_type).get('schemalocation')
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
            namespace_prefix = OBJECT_TYPES_DICT.get(object_type).get('namespace_prefix')
            schemalocation = OBJECT_TYPES_DICT.get(object_type).get('schemalocation')

            namespace_dict[namespace] = [namespace_prefix, schemalocation]

        return namespace_dict
