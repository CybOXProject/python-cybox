"""Common utility methods"""

from cybox.utils.idgen import *

import itertools

# Maps an ObjectType name to a tuple (module, class_name) where the class
# can be found
OBJECTS = {
            "AddressObjectType": 'cybox.objects.address_object.Address',
            "ArtifactType": 'cybox.objects.artifact.Artifact',
            "URIObjectType": 'cybox.objects.uri_object.URI',
            "EmailMessageObjectType": 'cybox.objects.email_message_object.EmailMessage',
            "FileObjectType": 'cybox.objects.file_object.File',
            "WindowsEventObjectType" : 'cybox.objects.win_event_object.Win_Event',
            # These are just for testing. Please don't attempt to use!
            "!!ObjectTestCase": 'cybox.utils.IDGenerator',
            "!!MissingModule": 'some.nonexistent.module',
            "!!BadClassName": 'cybox.utils.NonexistentClass',
          }

class UnknownObjectTypeError(Exception):
    pass

def get_class_for_object_type(object_type):
    """Gets the class where a given XML Type can be parsed

    Raises an UnknownObjectType if object_type has not been defined in the
        dictionary above.
    Raises an ImportError if the specified module is not available.
    Raises an AttributeError if the specified module does not contain the
         correct class.
    """
    full_class_name = OBJECTS.get(object_type)
    if not full_class_name:
        raise UnknownObjectTypeError("%s is not a known object type" %
                                        object_type)

    module = ".".join(full_class_name.split('.')[:-1])
    class_name = full_class_name.split('.')[-1]

    # May raise ImportError
    mod = __import__(module, fromlist=[class_name])

    # May raise AttributeError
    return getattr(mod, class_name)


def test_value(value):
    """
    Test if an input string value is not None and has a length grater than 0 or
    if a dictionary contains a "value" key whose value is not None and has
    a length greater than 0.

    We explicitly want to return True even if the value is False or 0, since
    some parts of the standards are boolean or allow a 0 value, and we want to
    distinguish the case where the "value" key is omitted entirely.
    """
    if isinstance(value, dict):
        v = value.get('value', None)
    elif isinstance(value, str):
        v = value
    elif isinstance(value, unicode):
        v = value
    elif isinstance(value, int):
        v = value
    elif isinstance(value, float):
        v = value
    else:
        v = None
    return (v is not None) and (len(str(v)) > 0)


class NamespaceParser(object):
    '''Functions for finding out the namespaces used within Observables'''
    OBJECTS_PATH = '' #Objects path - set to point to the CybOX Objects Bindings folder
    
    #Dictionary for storing Defined Objects, their main types, namespaces, and schemalocations
    DEFINED_OBJECTS_DICT = {'AccountObjectType' : {'binding_name' : 'account_object_1_2', 'namespace_prefix' : 'AccountObj', 'namespace' : 'http://cybox.mitre.org/objects#AccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Account/Account_Object_1.2.xsd'},
                   'AddressObjectType' : {'binding_name' : 'address_object_1_2', 'namespace_prefix' : 'AddressObj', 'namespace' : 'http://cybox.mitre.org/objects#AddressObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Address/Address_Object_1.2.xsd'},
                   'APIObjectType' : {'binding_name' : 'api_object_1_1', 'namespace_prefix' : 'APIObj', 'namespace' : 'http://cybox.mitre.org/objects#APIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/API/API_Object_1.1.xsd'},
                   'ArtifactType' : {'binding_name' : 'artifact_object_1_0', 'namespace_prefix' : 'ArtifactObj', 'namespace' : 'http://cybox.mitre.org/objects#ArtifactObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Artifact/Artifact_Object_1.0.xsd'},
                   'CodeObjectType' : {'binding_name' : 'code_object_1_1', 'namespace_prefix' : 'CodeObj', 'namespace' : 'http://cybox.mitre.org/objects#CodeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Code/Code_Object_1.1.xsd'},
                   'DeviceObjectType' : {'binding_name' : 'device_object_1_1', 'namespace_prefix' : 'DeviceObj', 'namespace' : 'http://cybox.mitre.org/objects#DeviceObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Device/Device_Object_1.1.xsd'},
                   'DiskObjectType' : {'binding_name' : 'disk_object_1_3', 'namespace_prefix' : 'DiskObj', 'namespace' : 'http://cybox.mitre.org/objects#DiskObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Disk/Disk_Object_1.3.xsd', 'dependencies' : 'DiskPartitionObjectType'},
                   'DiskPartitionObjectType' : {'binding_name' : 'disk_partition_object_1_3', 'namespace_prefix' : 'DiskPartitionObj', 'namespace' : 'http://cybox.mitre.org/objects#DiskPartitionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Disk_Partition/Disk_Partition_Object_1.3.xsd'},
                   'DNSCacheEntryType' : {'binding_name' : 'dns_cache_object_1_3', 'namespace_prefix' : 'DNSCacheObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSCacheObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Cache/DNS_Cache_Object_1.3.xsd', 'dependencies' : 'DNSRecordObjectType,AddressObjectType,URIObjectType'},
                   'DNSQueryObjectType' : {'binding_name' : 'dns_query_object_1_0', 'namespace_prefix' : 'DNSQueryObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSQueryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Query/DNS_Query_Object_1.0.xsd', 'dependencies' : 'DNSRecordObjectType,URIObjectType,AddressObjectType'},
                   'DNSRecordObjectType' : {'binding_name' : 'dns_record_object_1_1', 'namespace_prefix' : 'DNSRecordObj', 'namespace' : 'http://cybox.mitre.org/objects#DNSRecordObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/DNS_Record/DNS_Record_Object_1.1.xsd', 'dependencies' : 'URIObjectType,AddressObjectType'},
                   'EmailMessageObjectType' : {'binding_name' : 'email_message_object_1_2', 'namespace_prefix' : 'EmailMessageObj', 'namespace' : 'http://cybox.mitre.org/objects#EmailMessageObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Email_Message/Email_Message_Object_1.2.xsd', 'dependencies' : 'FileObjectType,AddressObjectType,URIObjectType'},
                   'FileObjectType' : {'binding_name' : 'file_object_1_3', 'namespace_prefix' : 'FileObj', 'namespace' : 'http://cybox.mitre.org/objects#FileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/File/File_Object_1.3.xsd'},
                   'GUIDialogboxObjectType' : {'binding_name' : 'gui_dialogbox_object_1_2', 'namespace_prefix' : 'GUIDialogboxObj', 'namespace' : 'http://cybox.mitre.org/objects#GUIDialogboxObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI_Dialogbox/GUI_Dialogbox_Object_1.2.xsd', 'dependencies' : 'GUIObjectType'},
                   'GUIObjectType' : {'binding_name' : 'gui_object_1_2', 'namespace_prefix' : 'GUIObj', 'namespace' : 'http://cybox.mitre.org/objects#GUIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI/GUI_Object_1.2.xsd'},
                   'GUIWindowObjectType' : {'binding_name' : 'gui_window_object_1_2', 'namespace_prefix' : 'GUIWindowOb', 'namespace' : 'http://cybox.mitre.org/objects#GUIWindowObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/GUI_Window/GUI_Window_Object_1.2.xsd', 'dependencies' : 'GUIObjectType'},
                   'HTTPSessionObjectType' : {'binding_name' : 'http_session_object_1_0', 'namespace_prefix' : 'HTTPSessionObj', 'namespace' : 'http://cybox.mitre.org/objects#HTTPSessionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/HTTP_Session/HTTP_Session_Object_1.0.xsd', 'dependencies' : 'AddressObjectType,PortObjectType,URIObjectType'},
                   'LibraryObjectType' : {'binding_name' : 'library_object_1_3', 'namespace_prefix' : 'LibraryObj', 'namespace' : 'http://cybox.mitre.org/objects#LibraryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Library/Library_Object_1.3.xsd'},
                   'LinuxPackageObjectType' : {'binding_name' : 'linux_package_object_1_3', 'namespace_prefix' : 'LinuxPackageObj', 'namespace' : 'http://cybox.mitre.org/objects#LinuxPackageObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Linux_Package/Linux_Package_Object_1.3.xsd'},
                   'MemoryObjectType' : {'binding_name' : 'memory_object_1_2', 'namespace_prefix' : 'MemoryObj', 'namespace' : 'http://cybox.mitre.org/objects#MemoryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Memory/Memory_Object_1.2.xsd'},
                   'MutexObjectType' : {'binding_name' : 'mutex_object_1_3', 'namespace_prefix' : 'MutexObj', 'namespace' : 'http://cybox.mitre.org/objects#MutexObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Mutex/Mutex_Object_1.3.xsd'},
                   'NetworkConnectionType' : {'binding_name' : 'network_connection_object_1_0', 'namespace_prefix' : 'NetworkConnectionObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkConnectionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Connection/Network_Connection_Object_1.0.xsd', 'dependencies' : 'AddressObjectType,PortObjectType,HTTPSessionObjectType,DNSQueryObjectType,DNSRecordObjectType,URIObjectType'},
                   'NetworkFlowObjectType' : {'binding_name' : 'network_flow_object_1_1', 'namespace_prefix' : 'NetFlowObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkFlowObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Flow/Network_Flow_Object_1.1.xsd', 'dependencies' : 'NetworkPacketType,AddressObjectType,PortObjectType'},
                   'NetworkPacketType' : {'binding_name' : 'network_packet_object_1_1', 'namespace_prefix' : 'PacketObj', 'namespace' : 'http://cybox.mitre.org/objects#PacketObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Packet/Network_Packet_Object_1.1.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'NetworkRouteEntryObjectType' : {'binding_name' : 'network_route_entry_object_1_1', 'namespace_prefix' : 'NetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Route_Entry/Network_Route_Entry_Object_1.1.xsd', 'dependencies' : 'AddressObjectType'},
                   'NetRouteObjectType' : {'binding_name' : 'network_route_object_1_2', 'namespace_prefix' : 'NetworkRouteObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkRouteObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Route/Network_Route_Object_1.2.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'NetworkSubnetObjectType' : {'binding_name' : 'network_subnet_object_1_1', 'namespace_prefix' : 'NetworkSubnetObj', 'namespace' : 'http://cybox.mitre.org/objects#NetworkSubnetObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Network_Subnet/Network_Subnet_Object_1.1.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'PipeObjectType' : {'binding_name' : 'pipe_object_1_3', 'namespace_prefix' : 'PipeObj', 'namespace' : 'http://cybox.mitre.org/objects#PipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Pipe/Pipe_Object_1.3.xsd'},
                   'PortObjectType' : {'binding_name' : 'port_object_1_3', 'namespace_prefix' : 'PortObj', 'namespace' : 'http://cybox.mitre.org/objects#PortObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Port/Port_Object_1.3.xsd'},
                   'ProcessObjectType' : {'binding_name' : 'process_object_1_3', 'namespace_prefix' : 'ProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#ProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Process/Process_Object_1.3.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'SemaphoreObjectType' : {'binding_name' : 'semaphore_object_1_3', 'namespace_prefix' : 'SemaphoreObj', 'namespace' : 'http://cybox.mitre.org/objects#SemaphoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Semaphore/Semaphore_Object_1.3.xsd'},
                   'SocketObjectType' : {'binding_name' : 'socket_object_1_4', 'namespace_prefix' : 'SocketObj', 'namespace' : 'http://cybox.mitre.org/objects#SocketObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Socket/Socket_Object_1.4.xsd', 'dependencies' : 'AddressObjectType,PortObjectType'},
                   'SystemObjectType' : {'binding_name' : 'system_object_1_3', 'namespace_prefix' : 'SystemObj', 'namespace' : 'http://cybox.mitre.org/objects#SystemObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/System/System_Object_1.3.xsd', 'dependencies' : 'AddressObjectType'},
                   'UnixFileObjectType' : {'binding_name' : 'unix_file_object_1_3', 'namespace_prefix' : 'UnixFileObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_File/Unix_File_Object_1.3.xsd', 'dependencies' : 'FileObjectType'},
                   'UnixNetworkRouteEntryObjectType' : {'binding_name' : 'unix_network_route_entry_object_1_1', 'namespace_prefix' : 'UnixNetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Network_Route_Entry/Unix_Network_Route_Entry_Object_1.1.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'UnixPipeObjectType' : {'binding_name' : 'unix_pipe_object_1_2', 'namespace_prefix' : 'UnixPipeObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixPipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Pipe/Unix_Pipe_Object_1.2.xsd', 'dependencies' : 'PipeObjectType'},
                   'UnixProcessObjectType' : {'binding_name' : 'unix_process_object_1_3', 'namespace_prefix' : 'UnixProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Process/Unix_Process_Object_1.3.xsd', 'dependencies' : 'ProcessObjectType,AddressObjectType,PortObjectType'},
                   'UnixUserAccountObjectType' : {'binding_name' : 'unix_user_account_object_1_2', 'namespace_prefix' : 'UnixUserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixUserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_User_Account/Unix_User_Account_Object_1.2.xsd', 'dependencies' : 'UserAccountObjectType,AccountObjectType'},
                   'UnixVolumeObjectType' : {'binding_name' : 'unix_volume_object_1_2', 'namespace_prefix' : 'UnixVolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#UnixVolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Unix_Volume/Unix_Volume_Object_1.2.xsd', 'dependencies' : 'VolumeObjectType'},
                   'URIObjectType' : {'binding_name' : 'uri_object_1_2', 'namespace_prefix' : 'URIObj', 'namespace' : 'http://cybox.mitre.org/objects#URIObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/URI/URI_Object_1.2.xsd'},
                   'UserAccountObjectType' : {'binding_name' : 'user_account_object_1_2', 'namespace_prefix' : 'UserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#UserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/User_Account/User_Account_Object_1.2.xsd', 'dependencies' : 'AccountObjectType'},
                   'VolumeObjectType' : {'binding_name' : 'volume_object_1_3', 'namespace_prefix' : 'VolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#VolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Volume/Volume_Object_1.3.xsd'},
                   'WhoisObjectType' : {'binding_name' : 'whois_object_1_0', 'namespace_prefix' : 'WhoisObj', 'namespace' : 'http://cybox.mitre.org/objects#WhoisObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Whois/Whois_Object_1.0.xsd', 'dependencies' : 'URIObjectType,AddressObjectType'},
                   'WinComputerAccountObjectType' : {'binding_name' : 'win_computer_account_object_1_3', 'namespace_prefix' : 'WinComputerAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#WinComputerAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Computer_Account/Win_Computer_Account_Object_1.3.xsd', 'dependencies' : 'AccountObjectType,PortObjectType'},
                   'WinCriticalSectionObjectType' : {'binding_name' : 'win_critical_section_object_1_2', 'namespace_prefix' : 'WinCriticalSectionObj', 'namespace' : 'http://cybox.mitre.org/objects#WinCriticalSectionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Critical_Section/Win_Critical_Section_Object_1.2.xsd'},
                   'WindowsDriverObjectType' : {'binding_name' : 'win_driver_object_1_2', 'namespace_prefix' : 'WinDriverObj', 'namespace' : 'http://cybox.mitre.org/objects#WinDriverObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Driver/Win_Driver_Object_1.2.xsd'},
                   'WindowsEventLogObjectType' : {'binding_name' : 'win_event_log_object_1_2', 'namespace_prefix' : 'WinEventLogObj', 'namespace' : 'http://cybox.mitre.org/objects#WinEventLogObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Event_Log/Win_Event_Log_Object_1.2.xsd'},
                   'WindowsEventObjectType' : {'binding_name' : 'win_event_object_1_3', 'namespace_prefix' : 'WinEventObj', 'namespace' : 'http://cybox.mitre.org/objects#WinEventObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Event/Win_Event_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsExecutableFileObjectType' : {'binding_name' : 'win_executable_file_object_1_3', 'namespace_prefix' : 'WinExecutableFileObj', 'namespace' : 'http://cybox.mitre.org/objects#WinExecutableFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Executable_File/Win_Executable_File_Object_1.3.xsd', 'dependencies' : 'WindowsFileObjectType,FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'},
                   'WindowsFileObjectType' : {'binding_name' : 'win_file_object_1_3', 'namespace_prefix' : 'WinFileObj', 'namespace' : 'http://cybox.mitre.org/objects#WinFileObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_File/Win_File_Object_1.3.xsd', 'dependencies' : 'FileObjectType,WinComputerAccountObjectType,AccountObjectType,PortObjectType'},
                   'WindowsHandleObjectType' : {'binding_name' : 'win_handle_object_1_3', 'namespace_prefix' : 'WinHandleObj', 'namespace' : 'http://cybox.mitre.org/objects#WinHandleObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Handle/Win_Handle_Object_1.3.xsd'},
                   'WindowsKernelHookObjectType' : {'binding_name' : 'win_kernel_hook_object_1_3', 'namespace_prefix' : 'WinKernelHookObj', 'namespace' : 'http://cybox.mitre.org/objects#WinKernelHookObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel_Hook/Win_Kernel_Hook_Object_1.3.xsd'},
                   'WindowsKernelObjectType' : {'binding_name' : 'win_kernel_object_1_2', 'namespace_prefix' : 'WinKernelObj', 'namespace' : 'http://cybox.mitre.org/objects#WinKernelObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel/Win_Kernel_Object_1.2.xsd'},
                   'WindowsMailslotObjectType' : {'binding_name' : 'win_mailslot_object_1_2', 'namespace_prefix' : 'WinMailslotObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMailslotObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Mailslot/Win_Mailslot_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsMemoryPageRegionObjectType' : {'binding_name' : 'win_memory_page_region_object_1_0', 'namespace_prefix' : 'WinMemoryPageRegionObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Memory_Page_Region/Win_Memory_Page_Region_Object_1.0.xsd', 'dependencies' : 'MemoryObjectType'},
                   'WindowsMutexObjectType' : {'binding_name' : 'win_mutex_object_1_2', 'namespace_prefix' : 'WinMutexObj', 'namespace' : 'http://cybox.mitre.org/objects#WinMutexObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Mutex/Win_Mutex_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,MutexObjectType'},
                   'WindowsNetworkRouteEntryObjectType' : {'binding_name' : 'win_network_route_entry_object_1_3', 'namespace_prefix' : 'WinNetworkRouteEntryObj', 'namespace' : 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Route_Entry/Win_Network_Route_Entry_Object_1.3.xsd', 'dependencies' : 'NetworkRouteEntryObjectType,AddressObjectType'},
                   'WindowsNetworkShareObjectType' : {'binding_name' : 'win_network_share_object_1_3', 'namespace_prefix' : 'WinNetworkShareObj', 'namespace' : 'http://cybox.mitre.org/objects#WinNetworkShareObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Share/Win_Network_Share_Object_1.3.xsd'},
                   'WindowsPipeObjectType' : {'binding_name' : 'win_pipe_object_1_2', 'namespace_prefix' : 'WinPipeObj', 'namespace' : 'http://cybox.mitre.org/objects#WinPipeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Pipe/Win_Pipe_Object_1.2.xsd', 'dependencies' : 'PipeObjectType'},
                   'WindowsPrefetchObjectType' : {'binding_name' : 'win_prefetch_object_1_2', 'namespace_prefix' : 'WinPrefetchObj', 'namespace' : 'http://cybox.mitre.org/objects#WinPrefetchObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Prefetch/Win_Prefetch_Object_1.2.xsd', 'dependencies' : 'WindowsVolumeObjectType,VolumeObjectType,DeviceObjectType'},
                   'WindowsProcessObjectType' : {'binding_name' : 'win_process_object_1_3', 'namespace_prefix' : 'WinProcessObj', 'namespace' : 'http://cybox.mitre.org/objects#WinProcessObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Process/Win_Process_Object_1.3.xsd', 'dependencies' : 'ProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'},
                   'WindowsRegistryKeyObjectType' : {'binding_name' : 'win_registry_key_object_1_3', 'namespace_prefix' : 'WinRegistryKeyObj', 'namespace' : 'http://cybox.mitre.org/objects#WinRegistryKeyObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Registry_Key/Win_Registry_Key_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsSemaphoreObjectType' : {'binding_name' : 'win_semaphore_object_1_2', 'namespace_prefix' : 'WinSemaphoreObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSemaphoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Semaphore/Win_Semaphore_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,SemaphoreObjectType'},
                   'WindowsServiceObjectType' : {'binding_name' : 'win_service_object_1_3', 'namespace_prefix' : 'WinServiceObj', 'namespace' : 'http://cybox.mitre.org/objects#WinServiceObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Service/Win_Service_Object_1.3.xsd', 'dependencies' : 'WindowsProcessObjectType,WindowsHandleObjectType,MemoryObjectType,AddressObjectType,PortObjectType'},
                   'WindowsSystemObjectType' : {'binding_name' : 'win_system_object_1_2', 'namespace_prefix' : 'WinSystemObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSystemObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_System/Win_System_Object_1.2.xsd', 'dependencies' : 'WindowsHandleObjectType,SystemObjectType,AddressObjectType'},
                   'WindowsSystemRestoreObjectType' : {'binding_name' : 'win_system_restore_object_1_2', 'namespace_prefix' : 'WinSystemRestoreObj', 'namespace' : 'http://cybox.mitre.org/objects#WinSystemRestoreObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_System_Restore/Win_System_Restore_Object_1.2.xsd'},
                   'WindowsTaskObjectType' : {'binding_name' : 'win_task_object_1_3', 'namespace_prefix' : 'WinTaskObj', 'namespace' : 'http://cybox.mitre.org/objects#WinTaskObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Task/Win_Task_Object_1.3.xsd', 'dependencies' : 'EmailMessageObjectType,FileObjectType,AddressObjectType,URIObjectType'},
                   'WindowsThreadObjectType' : {'binding_name' : 'win_thread_object_1_3', 'namespace_prefix' : 'WinThreadObj', 'namespace' : 'http://cybox.mitre.org/objects#WinThreadObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Thread/Win_Thread_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'WindowsUserAccountObjectType' : {'binding_name' : 'win_user_account_object_1_3', 'namespace_prefix' : 'WinUserAccountObj', 'namespace' : 'http://cybox.mitre.org/objects#WinUserAccountObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_User_Account/Win_User_Account_Object_1.3.xsd', 'dependencies' : 'UserAccountObjectType,AccountObjectType'},
                   'WindowsVolumeObjectType' : {'binding_name' : 'win_volume_object_1_3', 'namespace_prefix' : 'WinVolumeObj', 'namespace' : 'http://cybox.mitre.org/objects#WinVolumeObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Volume/Win_Volume_Object_1.3.xsd', 'dependencies' : 'VolumeObjectType'},
                   'WindowsWaitableTimerObjectType' : {'binding_name' : 'win_waitable_timer_object_1_3', 'namespace_prefix' : 'WinWaitableTimerObj', 'namespace' : 'http://cybox.mitre.org/objects#WinWaitableTimerObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/Win_Waitable_Timer/Win_Waitable_Timer_Object_1.3.xsd', 'dependencies' : 'WindowsHandleObjectType'},
                   'X509CertificateObjectType' : {'binding_name' : 'x509_certificate_object_1_2', 'namespace_prefix' : 'X509CertificateObj', 'namespace' : 'http://cybox.mitre.org/objects#X509CertificateObject', 'schemalocation' : 'http://cybox.mitre.org/XMLSchema/objects/X509_Certificate/X509_Certificate_Object_1.2.xsd'} }
    
    def __init__(self, observable_list):
        self.observable_list = observable_list if observable_list else []
        self.object_types = []
        self.object_type_dependencies = []
        
        self.get_object_namespaces() # parse the observables, build our lists
    
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
        if observable.get_Stateful_Measure() is not None:
            object = observable.get_Stateful_Measure().get_Object()
            self.get_namespace_from_object(object)
        
        elif observable.get_Event() is not None:
            self.process_event_namespace(observable.get_Event())
        
        elif observable.get_Observable_Composition() is not None:
            for embedded_observable in observable.get_Observable_Composition().get_Observable():
                self.process_observable_namespace(embedded_observable)
    
    def get_namespace_from_object(self, object):
        if object.get_Defined_Object() is not None:
            defined_object = object.get_Defined_Object()
            
            if ('get_anyAttributes_' in dir(defined_object)) and (defined_object.get_anyAttributes_() is not None):
                any_attributes = defined_object.get_anyAttributes_()
                self.get_defined_object_namespace(any_attributes)
                
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
                
    def get_defined_object_namespace(self, any_attributes):
        for key, value in any_attributes.items():
            if (key == '{http://www.w3.org/2001/XMLSchema-instance}type' or key == 'xsi:type') and value.split(':')[1] in self.DEFINED_OBJECTS_DICT:
                self.add_object_namespace(value.split(':')[1])
    
    def add_object_namespace(self, object_type):
        if object_type not in self.object_types:
            #Add the object type
            self.object_types.append(object_type)
            
            #Add any dependencies
            if self.DEFINED_OBJECTS_DICT.get(object_type).get('dependencies') is not None:
                dependencies = self.DEFINED_OBJECTS_DICT.get(object_type).get('dependencies').split(',')
                
                for dependency in dependencies:
                    if dependency not in self.object_types:
                        self.object_type_dependencies.append(dependency)
   
    def build_namespaces_schemalocations_str(self):
        '''Build the namespace/schemalocation declaration string'''
        
        output_string = '\n '
        schemalocs = []
        #Add the XSI and CybOX Core/Common namespaces and schemalocation
        output_string += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n '
        output_string += 'xmlns:cybox="http://cybox.mitre.org/cybox_v1" \n '
        output_string += 'xmlns:Common="http://cybox.mitre.org/Common_v1" \n '
        schemalocs.append('http://cybox.mitre.org/cybox_v1 http://cybox.mitre.org/XMLSchema/cybox_core_v1.0.xsd')
        
        for object_type in self.object_types:
            namespace_prefix = self.DEFINED_OBJECTS_DICT.get(object_type).get('namespace_prefix')
            namespace = self.DEFINED_OBJECTS_DICT.get(object_type).get('namespace')
            output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')
        
        for object_type_dependency in self.object_type_dependencies:
            if object_type_dependency not in self.object_types:
                namespace_prefix = self.DEFINED_OBJECTS_DICT.get(object_type_dependency).get('namespace_prefix')
                namespace = self.DEFINED_OBJECTS_DICT.get(object_type_dependency).get('namespace')
                output_string += ('xmlns:' + namespace_prefix + '=' + '"' + namespace + '"' + ' \n ')
        
        output_string += 'xsi:schemaLocation="'
        
        for object_type in self.object_types:
            namespace = self.DEFINED_OBJECTS_DICT.get(object_type).get('namespace')
            schemalocation = self.DEFINED_OBJECTS_DICT.get(object_type).get('schemalocation')
            schemalocs.append(' ' + namespace + ' ' + schemalocation)
        
        for schemalocation_string in schemalocs:
            if schemalocs.index(schemalocation_string) == (len(schemalocs) - 1):
                output_string += (schemalocation_string + '"')
            else:
                output_string += (schemalocation_string + '\n')
        
        return output_string
    
    def get_namespace_dict(self):
        '''returns a dictionary of namespace->(prefix, schemalocation)'''
        
        namespace_dict = {'http://www.w3.org/2001/XMLSchema-instance' : ['xsi', ''],
                          'http://cybox.mitre.org/cybox_v1' : ['cybox', 'http://cybox.mitre.org/XMLSchema/cybox_core_v1.0.xsd'],
                          'http://cybox.mitre.org/Common_v1' : ['Common', 'http://cybox.mitre.org/XMLSchema/cybox_common_types_v1.0.xsd'] }
        
        for object_type in itertools.chain(self.object_types, self.object_type_dependencies):
            namespace           = self.DEFINED_OBJECTS_DICT.get(object_type).get('namespace')
            namespace_prefix    = self.DEFINED_OBJECTS_DICT.get(object_type_dependency).get('namespace_prefix')
            schemalocation      = self.DEFINED_OBJECTS_DICT.get(object_type).get('schemalocation')
            
            namespace_dict[namespace] = [namespace_prefix, schemalocation]
        
        return namespace_dict

