# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import itertools

import cybox
import cybox.utils.idgen

__all__ = ['Namespace', 'NamespaceParser', 'META', 'UnknownObjectType']


class UnknownObjectType(Exception):
    pass


class Namespace(object):
    """An XML namespace used to define CybOX objects.

    Encapsulates the full namespace (URL), the most commonly-used prefix for
    the namespace, and (if applicable), the location of the corresponding
    schema.
    """

    def __init__(self, name, prefix, schema_location=''):
        """Create a new namespace.

        Arguments:
        - name: the full namespace (a URI)
        - prefix: a shortened prefix for the URL (used in the xmlns)
        - schema_location: a URL to locate the schema for this namespace

        schema_location is optional and defaults to an empty string.
        """
        self.name = name
        self.prefix = prefix
        self.schema_location = schema_location

    def __repr__(self):
        return "Namespace('%s', '%s', '%s')" % (self.name,
                                                self.prefix,
                                                self.schema_location)


class ObjectType(object):

    def __init__(self, name, api_class, binding, namespace, dependencies):
        """Create a new namespace.

        Arguments (all strings)
        - name: the name of the Object
        - api_class: The fully qualified name of the class that implements
          the Object
        - binding: the name of the binding containing the Object
        - namespace: the namespace where the Object is defined
        - dependencies: a list of strings, where each string is another
          ObjectType
        """
        self.name = name
        self.api_class = api_class
        self.binding = binding
        self.namespace = namespace
        self.dependencies = dependencies


class Metadata(object):
    """Metadata about CybOX objects and namespaces."""

    def __init__(self, namespace_list, object_list):
        self._ns_dict = {}
        self._prefix_dict = {}
        self._obj_dict = {}

        for ns in namespace_list:
            n = Namespace(*ns)
            self.add_namespace(n)

        for obj in object_list:
            o = ObjectType(*obj)
            self.add_object(o)

    def add_namespace(self, namespace):
        self._ns_dict[namespace.name] = namespace
        self._prefix_dict[namespace.prefix] = namespace

    def add_object(self, object_type):
        # TODO: are there other ways we want to look up this data?
        self._obj_dict[object_type.name] = object_type

    def lookup_namespace(self, namespace):
        return self._ns_dict.get(namespace)

    def lookup_prefix(self, prefix):
        return self._prefix_dict.get(prefix)

    def lookup_object(self, object_name):
        return self._obj_dict.get(object_name)

    def get_class_for_object_type(self, object_type):
        """Gets the class where a given XML Type can be parsed.

        Each ObjectType instance should define a member api_class, which
        consists of a fully-qualified name of a class (including the module it
        is defined in).

        Arguments:
        - object_type: a string

        Raises:
        - UnknownObjectType, if object_type has not been defined in obj_list.
        - ImportError, if the specified module is not available.
        - AttributeError, if the module does not contain the given class.
        """
        otype = self.lookup_object(object_type)
        if not otype:
            err = "%s is not a known ObjectType" % object_type
            raise UnknownObjectType(err)

        full_class_name = otype.api_class
        if not full_class_name:
            err = "%s does not have a specified API class" % object_type
            raise UnknownObjectType(err)

        module = ".".join(full_class_name.split('.')[:-1])
        class_name = full_class_name.split('.')[-1]

        # May raise ImportError
        mod = __import__(module, fromlist=[class_name])

        # May raise AttributeError
        return getattr(mod, class_name)

# A list of (namespace, prefix, schemalocation) tuples
# This is loaded by the Metadata class and should not be accessed directly.
NS_LIST = [
    ('http://www.w3.org/2001/XMLSchema-instance', 'xsi', ''),
    ('http://cybox.mitre.org/cybox-2', 'cybox', 'http://cybox.mitre.org/XMLSchema/core/2.0.1/cybox_core.xsd'),
    ('http://cybox.mitre.org/common-2', 'cyboxCommon', 'http://cybox.mitre.org/XMLSchema/common/2.0.1/cybox_common.xsd'),
    ('http://cybox.mitre.org/default_vocabularies-2', 'cyboxVocabs', 'http://cybox.mitre.org/XMLSchema/default_vocabularies/2.0.1/cybox_default_vocabularies.xsd'),
    ('http://cybox.mitre.org/objects#AccountObject-2', 'AccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Account/2.0.1/Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#AddressObject-2', 'AddressObj', 'http://cybox.mitre.org/XMLSchema/objects/Address/2.0.1/Address_Object.xsd'),
    ('http://cybox.mitre.org/objects#APIObject-2', 'APIObj', 'http://cybox.mitre.org/XMLSchema/objects/API/2.0.1/API_Object.xsd'),
    ('http://cybox.mitre.org/objects#ArtifactObject-2', 'ArtifactObj', 'http://cybox.mitre.org/XMLSchema/objects/Artifact/2.0.1/Artifact_Object.xsd'),
    ('http://cybox.mitre.org/objects#CodeObject-2', 'CodeObj', 'http://cybox.mitre.org/XMLSchema/objects/Code/2.0.1/Code_Object.xsd'),
    ('http://cybox.mitre.org/objects#CustomObject-1', 'CustomObj', 'http://cybox.mitre.org/XMLSchema/objects/Custom/1.0.1/Custom_Object.xsd'),
    ('http://cybox.mitre.org/objects#DeviceObject-2', 'DeviceObj', 'http://cybox.mitre.org/XMLSchema/objects/Device/2.0.1/Device_Object.xsd'),
    ('http://cybox.mitre.org/objects#DiskObject-2', 'DiskObj', 'http://cybox.mitre.org/XMLSchema/objects/Disk/2.0.1/Disk_Object.xsd'),
    ('http://cybox.mitre.org/objects#DiskPartitionObject-2', 'DiskPartitionObj', 'http://cybox.mitre.org/XMLSchema/objects/Disk_Partition/2.0.1/Disk_Partition_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSCacheObject-2', 'DNSCacheObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Cache/2.0.1/DNS_Cache_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSQueryObject-2', 'DNSQueryObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Query/2.0.1/DNS_Query_Object.xsd'),
    ('http://cybox.mitre.org/objects#DNSRecordObject-2', 'DNSRecordObj', 'http://cybox.mitre.org/XMLSchema/objects/DNS_Record/2.0.1/DNS_Record_Object.xsd'),
    ('http://cybox.mitre.org/objects#EmailMessageObject-2', 'EmailMessageObj', 'http://cybox.mitre.org/XMLSchema/objects/Email_Message/2.0.1/Email_Message_Object.xsd'),
    ('http://cybox.mitre.org/objects#FileObject-2', 'FileObj', 'http://cybox.mitre.org/XMLSchema/objects/File/2.0.1/File_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIDialogboxObject-2', 'GUIDialogboxObj', 'http://cybox.mitre.org/XMLSchema/objects/GUI_Dialogbox/2.0.1/GUI_Dialogbox_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIObject-2', 'GUIObj', 'http://cybox.mitre.org/XMLSchema/objects/GUI/2.0.1/GUI_Object.xsd'),
    ('http://cybox.mitre.org/objects#GUIWindowObject-2', 'GUIWindowObj', 'http://cybox.mitre.org/XMLSchema/objects/GUI_Window/2.0.1/GUI_Window_Object.xsd'),
    ('http://cybox.mitre.org/objects#HTTPSessionObject-2', 'HTTPSessionObj', 'http://cybox.mitre.org/XMLSchema/objects/HTTP_Session/2.0.1/HTTP_Session_Object.xsd'),
    ('http://cybox.mitre.org/objects#LibraryObject-2', 'LibraryObj', 'http://cybox.mitre.org/XMLSchema/objects/Library/2.0.1/Library_Object.xsd'),
    ('http://cybox.mitre.org/objects#LinkObject-1', 'LinkObj', 'http://cybox.mitre.org/XMLSchema/objects/Link/1.0.1/Link_Object.xsd'),
    ('http://cybox.mitre.org/objects#LinuxPackageObject-2', 'LinuxPackageObj', 'http://cybox.mitre.org/XMLSchema/objects/Linux_Package/2.0.1/Linux_Package_Object.xsd'),
    ('http://cybox.mitre.org/objects#MemoryObject-2', 'MemoryObj', 'http://cybox.mitre.org/XMLSchema/objects/Memory/2.0.1/Memory_Object.xsd'),
    ('http://cybox.mitre.org/objects#MutexObject-2', 'MutexObj', 'http://cybox.mitre.org/XMLSchema/objects/Mutex/2.0.1/Mutex_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkConnectionObject-2', 'NetworkConnectionObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Connection/2.0.1/Network_Connection_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkFlowObject-2', 'NetFlowObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Flow/2.0.1/Network_Flow_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkRouteEntryObject-2', 'NetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Route_Entry/2.0.1/Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkRouteObject-2', 'NetworkRouteObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Route/2.0.1/Network_Route_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkSocketObject-2', 'NetworkSocketObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Socket/2.0.1/Network_Socket_Object.xsd'),
    ('http://cybox.mitre.org/objects#NetworkSubnetObject-2', 'NetworkSubnetObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Subnet/2.0.1/Network_Subnet_Object.xsd'),
    ('http://cybox.mitre.org/objects#PacketObject-2', 'PacketObj', 'http://cybox.mitre.org/XMLSchema/objects/Network_Packet/2.0.1/Network_Packet_Object.xsd'),
    ('http://cybox.mitre.org/objects#PDFFileObject-1', 'PDFFileObj', 'http://cybox.mitre.org/XMLSchema/objects/PDF_File/1.0.1/PDF_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#PipeObject-2', 'PipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Pipe/2.0.1/Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#PortObject-2', 'PortObj', 'http://cybox.mitre.org/XMLSchema/objects/Port/2.0.1/Port_Object.xsd'),
    ('http://cybox.mitre.org/objects#ProcessObject-2', 'ProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Process/2.0.1/Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#SemaphoreObject-2', 'SemaphoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Semaphore/2.0.1/Semaphore_Object.xsd'),
    ('http://cybox.mitre.org/objects#SocketAddressObject-1', 'SocketAddressObj', 'http://cybox.mitre.org/XMLSchema/objects/Socket_Address/2.0.1/Socket_Address_Object.xsd'),
    ('http://cybox.mitre.org/objects#SystemObject-2', 'SystemObj', 'http://cybox.mitre.org/XMLSchema/objects/System/2.0.1/System_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixFileObject-2', 'UnixFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_File/2.0.1/Unix_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2', 'UnixNetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Network_Route_Entry/2.0.1/Unix_Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixPipeObject', 'UnixPipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Pipe/2.0.1/Unix_Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixProcessObject-2', 'UnixProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Process/2.0.1/Unix_Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixUserAccountObject-2', 'UnixUserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_User_Account/2.0.1/Unix_User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#UnixVolumeObject-2', 'UnixVolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Unix_Volume/2.0.1/Unix_Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#URIObject-2', 'URIObj', 'http://cybox.mitre.org/XMLSchema/objects/URI/2.0.1/URI_Object.xsd'),
    ('http://cybox.mitre.org/objects#UserAccountObject-2', 'UserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/User_Account/2.0.1/User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#VolumeObject-2', 'VolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Volume/2.0.1/Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#WhoisObject-2', 'WhoisObj', 'http://cybox.mitre.org/XMLSchema/objects/Whois/2.0.1/Whois_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinComputerAccountObject-2', 'WinComputerAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Computer_Account/2.0.1/Win_Computer_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinCriticalSectionObject-2', 'WinCriticalSectionObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Critical_Section/2.0.1/Win_Critical_Section_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinDriverObject-2', 'WinDriverObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Driver/2.0.1/Win_Driver_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinEventLogObject-2', 'WinEventLogObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Event_Log/2.0.1/Win_Event_Log_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinEventObject-2', 'WinEventObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Event/2.0.1/Win_Event_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinExecutableFileObject-2', 'WinExecutableFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Executable_File/2.0.1/Win_Executable_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinFileObject-2', 'WinFileObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_File/2.0.1/Win_File_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinHandleObject-2', 'WinHandleObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Handle/2.0.1/Win_Handle_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinKernelHookObject-2', 'WinKernelHookObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel_Hook/2.0.1/Win_Kernel_Hook_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinKernelObject-2', 'WinKernelObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Kernel/2.0.1/Win_Kernel_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMailslotObject-2', 'WinMailslotObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Mailslot/2.0.1/Win_Mailslot_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2', 'WinMemoryPageRegionObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Memory_Page_Region/2.0.1/Win_Memory_Page_Region_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinMutexObject-2', 'WinMutexObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Mutex/2.0.1/Win_Mutex_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2', 'WinNetworkRouteEntryObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Route_Entry/2.0.1/Win_Network_Route_Entry_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinNetworkShareObject-2', 'WinNetworkShareObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Network_Share/2.0.1/Win_Network_Share_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinPipeObject-2', 'WinPipeObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Pipe/2.0.1/Win_Pipe_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinPrefetchObject-2', 'WinPrefetchObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Prefetch/2.0.1/Win_Prefetch_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinProcessObject-2', 'WinProcessObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Process/2.0.1/Win_Process_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinRegistryKeyObject-2', 'WinRegistryKeyObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Registry_Key/2.0.1/Win_Registry_Key_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSemaphoreObject-2', 'WinSemaphoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Semaphore/2.0.1/Win_Semaphore_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinServiceObject-2', 'WinServiceObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Service/2.0.1/Win_Service_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSystemObject-2', 'WinSystemObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_System/2.0.1/Win_System_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinSystemRestoreObject-2', 'WinSystemRestoreObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_System_Restore/2.0.1/Win_System_Restore_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinTaskObject-2', 'WinTaskObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Task/2.0.1/Win_Task_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinThreadObject-2', 'WinThreadObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Thread/2.0.1/Win_Thread_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinUserAccountObject-2', 'WinUserAccountObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_User_Account/2.0.1/Win_User_Account_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinVolumeObject-2', 'WinVolumeObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Volume/2.0.1/Win_Volume_Object.xsd'),
    ('http://cybox.mitre.org/objects#WinWaitableTimerObject-2', 'WinWaitableTimerObj', 'http://cybox.mitre.org/XMLSchema/objects/Win_Waitable_Timer/2.0.1/Win_Waitable_Timer_Object.xsd'),
    ('http://cybox.mitre.org/objects#X509CertificateObject-2', 'X509CertificateObj', 'http://cybox.mitre.org/XMLSchema/objects/X509_Certificate/2.0.1/X509_Certificate_Object.xsd'),
]


# A list of (object_name, api_class, binding, namespace, dependencies) tuples
# This is loaded by the Metadata class and should not be accessed directly.
OBJ_LIST = [
    ('AccountObjectType', 'cybox.objects.account_object.Account', 'account_object', 'http://cybox.mitre.org/objects#AccountObject-2', []),
    ('AddressObjectType', 'cybox.objects.address_object.Address', 'address_object', 'http://cybox.mitre.org/objects#AddressObject-2', []),
    ('APIObjectType', 'cybox.objects.api_object.API', 'api_object', 'http://cybox.mitre.org/objects#APIObject-2', []),
    ('ArtifactObjectType', 'cybox.objects.artifact_object.Artifact', 'artifact_object', 'http://cybox.mitre.org/objects#ArtifactObject-2', []),
    ('CodeObjectType', None, 'code_object', 'http://cybox.mitre.org/objects#CodeObject-2', []),
    ('CustomObjectType', None, 'custom_object', 'http://cybox.mitre.org/objects#CustomObject-1', []),
    ('DeviceObjectType', None, 'device_object', 'http://cybox.mitre.org/objects#DeviceObject-2', []),
    ('DiskObjectType', 'cybox.objects.disk_object.Disk', 'disk_object', 'http://cybox.mitre.org/objects#DiskObject-2', ['DiskPartitionObjectType']),
    ('DiskPartitionObjectType', 'cybox.objects.disk_partition_object.DiskPartition', 'disk_partition_object', 'http://cybox.mitre.org/objects#DiskPartitionObject-2', []),
    ('DNSCacheEntryType', None, 'dns_cache_object', 'http://cybox.mitre.org/objects#DNSCacheObject-2', ['DNSRecordObjectType', 'AddressObjectType', 'URIObjectType']),
    ('DNSQueryObjectType', 'cybox.objects.dns_query_object.DNSQuery', 'dns_query_object', 'http://cybox.mitre.org/objects#DNSQueryObject-2', ['DNSRecordObjectType', 'URIObjectType', 'AddressObjectType']),
    ('DNSRecordObjectType', 'cybox.objects.dns_record_object.DNSRecord', 'dns_record_object', 'http://cybox.mitre.org/objects#DNSRecordObject-2', ['URIObjectType', 'AddressObjectType']),
    ('EmailMessageObjectType', 'cybox.objects.email_message_object.EmailMessage', 'email_message_object', 'http://cybox.mitre.org/objects#EmailMessageObject-2', ['FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('FileObjectType', 'cybox.objects.file_object.File', 'file_object', 'http://cybox.mitre.org/objects#FileObject-2', []),
    ('GUIDialogboxObjectType', 'cybox.objects.gui_dialogbox_object.GUIDialogbox', 'gui_dialogbox_object', 'http://cybox.mitre.org/objects#GUIDialogboxObject-2', ['GUIObjectType']),
    ('GUIObjectType', 'cybox.objects.gui_object.GUI', 'gui_object', 'http://cybox.mitre.org/objects#GUIObject-2', []),
    ('GUIWindowObjectType', 'cybox.objects.gui_window_object.GUIWindow', 'gui_window_object', 'http://cybox.mitre.org/objects#GUIWindowObject-2', ['GUIObjectType']),
    ('HTTPSessionObjectType', 'cybox.objects.http_session_object.HTTPSession', 'http_session_object', 'http://cybox.mitre.org/objects#HTTPSessionObject-2', ['AddressObjectType', 'PortObjectType', 'URIObjectType']),
    ('LibraryObjectType', 'cybox.objects.library_object.Library', 'library_object', 'http://cybox.mitre.org/objects#LibraryObject-2', []),
    ('LinkObjectType', None, 'link_object', 'http://cybox.mitre.org/objects#LinkObject-1', ['URIObjectType']),
    ('LinuxPackageObjectType', None, 'linux_package_object', 'http://cybox.mitre.org/objects#LinuxPackageObject-2', []),
    ('MemoryObjectType', 'cybox.objects.memory_object.Memory', 'memory_object', 'http://cybox.mitre.org/objects#MemoryObject-2', []),
    ('MutexObjectType', 'cybox.objects.mutex_object.Mutex', 'mutex_object', 'http://cybox.mitre.org/objects#MutexObject-2', []),
    ('NetRouteObjectType', None, 'network_route_object', 'http://cybox.mitre.org/objects#NetworkRouteObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('NetworkConnectionObjectType', 'cybox.objects.network_connection_object.NetworkConnection', 'network_connection_object', 'http://cybox.mitre.org/objects#NetworkConnectionObject-2', ['SocketAddressObjectType', 'HTTPSessionObjectType', 'DNSQueryObjectType', 'DNSRecordObjectType', 'URIObjectType']),
    ('NetworkFlowObjectType', None, 'network_flow_object', 'http://cybox.mitre.org/objects#NetworkFlowObject-2', ['NetworkPacketType', 'AddressObjectType', 'SocketAddressObjectType']),
    ('NetworkPacketObjectType', 'cybox.objects.network_packet_object.NetworkPacket', 'network_packet_object', 'http://cybox.mitre.org/objects#PacketObject-2', ['AddressObjectType', 'PortObjectType']),
    ('NetworkRouteEntryObjectType', None, 'network_route_entry_object', 'http://cybox.mitre.org/objects#NetworkRouteEntryObject-2', ['AddressObjectType']),
    ('NetworkSocketObjectType', 'cybox.objects.network_socket_object.NetworkSocket', 'network_socket_object', 'http://cybox.mitre.org/objects#NetworkSocketObject-2', ['SocketAddressObjectType']),
    ('NetworkSubnetObjectType', None, 'network_subnet_object', 'http://cybox.mitre.org/objects#NetworkSubnetObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('PDFFileObjectType', None, 'pdf_file_object', 'http://cybox.mitre.org/objects#PDFFileObject-1', []),
    ('PipeObjectType', 'cybox.objects.pipe_object.Pipe', 'pipe_object', 'http://cybox.mitre.org/objects#PipeObject-2', []),
    ('PortObjectType', 'cybox.objects.port_object.Port', 'port_object', 'http://cybox.mitre.org/objects#PortObject-2', []),
    ('ProcessObjectType', 'cybox.objects.process_object.Process', 'process_object', 'http://cybox.mitre.org/objects#ProcessObject-2', ['NetworkConnectionObjectType', 'PortObjectType']),
    ('SemaphoreObjectType', None, 'semaphore_object', 'http://cybox.mitre.org/objects#SemaphoreObject-2', []),
    ('SocketAddressObjectType', 'cybox.objects.socket_address_object.SocketAddress', 'socket_address_object', 'http://cybox.mitre.org/objects#SocketAddressObject-1', ['AddressObjectType', 'PortObjectType']),
    ('SystemObjectType', 'cybox.objects.system_object.System', 'system_object', 'http://cybox.mitre.org/objects#SystemObject-2', ['AddressObjectType']),
    ('UnixFileObjectType', None, 'unix_file_object', 'http://cybox.mitre.org/objects#UnixFileObject-2', ['FileObjectType']),
    ('UnixNetworkRouteEntryObjectType', None, 'unix_network_route_entry_object', 'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('UnixPipeObjectType', None, 'unix_pipe_object', 'http://cybox.mitre.org/objects#UnixPipeObject', ['PipeObjectType']),
    ('UnixProcessObjectType', None, 'unix_process_object', 'http://cybox.mitre.org/objects#UnixProcessObject-2', ['ProcessObjectType', 'AddressObjectType', 'PortObjectType']),
    ('UnixUserAccountObjectType', None, 'unix_user_account_object', 'http://cybox.mitre.org/objects#UnixUserAccountObject-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('UnixVolumeObjectType', None, 'unix_volume_object', 'http://cybox.mitre.org/objects#UnixVolumeObject-2', ['VolumeObjectType']),
    ('URIObjectType', 'cybox.objects.uri_object.URI', 'uri_object', 'http://cybox.mitre.org/objects#URIObject-2', []),
    ('UserAccountObjectType', 'cybox.objects.user_account_object.UserAccount', 'user_account_object', 'http://cybox.mitre.org/objects#UserAccountObject-2', ['AccountObjectType']),
    ('VolumeObjectType', 'cybox.objects.volume_object.Volume', 'volume_object', 'http://cybox.mitre.org/objects#VolumeObject-2', []),
    ('WhoisObjectType', 'cybox.objects.whois_object.WhoisEntry', 'whois_object', 'http://cybox.mitre.org/objects#WhoisObject-2', ['URIObjectType', 'AddressObjectType']),
    ('WinComputerAccountObjectType', None, 'win_computer_account_object', 'http://cybox.mitre.org/objects#WinComputerAccountObject-2', ['AccountObjectType', 'PortObjectType']),
    ('WinCriticalSectionObjectType', None, 'win_critical_section_object', 'http://cybox.mitre.org/objects#WinCriticalSectionObject-2', []),
    ('WindowsDriverObjectType', 'cybox.objects.win_driver_object.WinDriver', 'win_driver_object', 'http://cybox.mitre.org/objects#WinDriverObject-2', []),
    ('WindowsEventLogObjectType', 'cybox.objects.win_event_log_object.WinEventLog', 'win_event_log_object', 'http://cybox.mitre.org/objects#WinEventLogObject-2', []),
    ('WindowsEventObjectType', 'cybox.objects.win_event_object.WinEvent', 'win_event_object', 'http://cybox.mitre.org/objects#WinEventObject-2', ['WindowsHandleObjectType']),
    ('WindowsExecutableFileObjectType', 'cybox.objects.win_executable_file_object.WinExecutableFile', 'win_executable_file_object', 'http://cybox.mitre.org/objects#WinExecutableFileObject-2', ['WindowsFileObjectType', 'FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsFileObjectType', 'cybox.objects.win_file_object.WinFile', 'win_file_object', 'http://cybox.mitre.org/objects#WinFileObject-2', ['FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsHandleObjectType', 'cybox.objects.win_handle_object.WinHandle', 'win_handle_object', 'http://cybox.mitre.org/objects#WinHandleObject-2', []),
    ('WindowsKernelHookObjectType', 'cybox.objects.win_kernel_hook_object.WinKernelHook', 'win_kernel_hook_object', 'http://cybox.mitre.org/objects#WinKernelHookObject-2', []),
    ('WindowsKernelObjectType', None, 'win_kernel_object', 'http://cybox.mitre.org/objects#WinKernelObject-2', []),
    ('WindowsMailslotObjectType', 'cybox.objects.win_mailslot_object.WinMailslot', 'win_mailslot_object', 'http://cybox.mitre.org/objects#WinMailslotObject-2', ['WindowsHandleObjectType']),
    ('WindowsMemoryPageRegionObjectType', None, 'win_memory_page_region_object', 'http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2', ['MemoryObjectType']),
    ('WindowsMutexObjectType', 'cybox.objects.win_mutex_object.WinMutex', 'win_mutex_object', 'http://cybox.mitre.org/objects#WinMutexObject-2', ['WindowsHandleObjectType', 'MutexObjectType']),
    ('WindowsNetworkRouteEntryObjectType', None, 'win_network_route_entry_object', 'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('WindowsNetworkShareObjectType', 'cybox.objects.win_network_share_object.WinNetworkShare', 'win_network_share_object', 'http://cybox.mitre.org/objects#WinNetworkShareObject-2', []),
    ('WindowsPipeObjectType', 'cybox.objects.win_pipe_object.WinPipe', 'win_pipe_object', 'http://cybox.mitre.org/objects#WinPipeObject-2', ['PipeObjectType']),
    ('WindowsPrefetchObjectType', None, 'win_prefetch_object', 'http://cybox.mitre.org/objects#WinPrefetchObject-2', ['WindowsVolumeObjectType', 'VolumeObjectType', 'DeviceObjectType']),
    ('WindowsProcessObjectType', 'cybox.objects.win_process_object.WinProcess', 'win_process_object', 'http://cybox.mitre.org/objects#WinProcessObject-2', ['ProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsRegistryKeyObjectType', 'cybox.objects.win_registry_key_object.WinRegistryKey', 'win_registry_key_object', 'http://cybox.mitre.org/objects#WinRegistryKeyObject-2', ['WindowsHandleObjectType']),
    ('WindowsSemaphoreObjectType', None, 'win_semaphore_object', 'http://cybox.mitre.org/objects#WinSemaphoreObject-2', ['WindowsHandleObjectType', 'SemaphoreObjectType']),
    ('WindowsServiceObjectType', 'cybox.objects.win_service_object.WinService', 'win_service_object', 'http://cybox.mitre.org/objects#WinServiceObject-2', ['WindowsProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsSystemObjectType', 'cybox.objects.win_system_object.WinSystem', 'win_system_object', 'http://cybox.mitre.org/objects#WinSystemObject-2', ['WindowsHandleObjectType', 'SystemObjectType', 'AddressObjectType']),
    ('WindowsSystemRestoreObjectType', None, 'win_system_restore_object', 'http://cybox.mitre.org/objects#WinSystemRestoreObject-2', []),
    ('WindowsTaskObjectType', 'cybox.objects.win_task_object.WinTask', 'win_task_object', 'http://cybox.mitre.org/objects#WinTaskObject-2', ['EmailMessageObjectType', 'FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('WindowsThreadObjectType', 'cybox.objects.win_thread_object.WinThread', 'win_thread_object', 'http://cybox.mitre.org/objects#WinThreadObject-2', ['WindowsHandleObjectType']),
    ('WindowsUserAccountObjectType', 'cybox.objects.win_user_object.WinUser', 'win_user_account_object', 'http://cybox.mitre.org/objects#WinUserAccountObject-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('WindowsVolumeObjectType', 'cybox.objects.win_volume_object.WinVolume', 'win_volume_object', 'http://cybox.mitre.org/objects#WinVolumeObject-2', ['VolumeObjectType']),
    ('WindowsWaitableTimerObjectType', None, 'win_waitable_timer_object', 'http://cybox.mitre.org/objects#WinWaitableTimerObject-2', ['WindowsHandleObjectType']),
    ('X509CertificateObjectType', 'cybox.objects.x509_certificate_object.X509Certificate', 'x509_certificate_object', 'http://cybox.mitre.org/objects#X509CertificateObject-2', []),
]


META = Metadata(NS_LIST, OBJ_LIST)


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

        if object.get_Related_Objects() is not None:
            related_objects = object.get_Related_Objects()

            for rel_obj in related_objects.get_Related_Object():
                self.get_namespace_from_object(rel_obj)

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
        obj_type = xsi_type.split(':')[1]

        o = META.lookup_object(obj_type)
        if o:
            self.add_object_namespace(o)

    def add_object_namespace(self, object_type):
        if object_type.name not in self.object_types:
            #Add the object type
            self.object_types.append(object_type.name)

            #Add any dependencies
            for dependency in object_type.dependencies:
                self.add_object_dependency(dependency)

    def add_object_dependency(self, object_dependency):
        if object_dependency not in self.object_types and object_dependency not in self.object_type_dependencies:
            self.object_type_dependencies.append(object_dependency)
            o = META.lookup_object(object_dependency)
            #Add recursive dependencies as needed
            for dependency in o.dependencies:
                self.add_object_dependency(dependency)

    def build_namespaces_schemalocations_str(self):
        '''Build the namespace/schemalocation declaration string'''

        output_string = '\n '
        schemalocs = []
        #Add the XSI and CybOX Core/Common namespaces and schemalocation
        output_string += 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" \n '
        output_string += 'xmlns:cybox="http://cybox.mitre.org/cybox-2" \n '
        output_string += 'xmlns:cyboxCommon="http://cybox.mitre.org/common-2" \n '
        output_string += 'xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2" \n '

        idns = cybox.utils.idgen._get_generator().namespace
        output_string += 'xmlns:%s="%s" \n ' % (idns.prefix, idns.name)

        schemalocs.append('http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.0.1/cybox_core.xsd')
        schemalocs.append(' http://cybox.mitre.org/default_vocabularies-2 http://cybox.mitre.org/XMLSchema/default_vocabularies/2.0.1/cybox_default_vocabularies.xsd')

        for object_type in self.object_types:
            namespace = META.lookup_object(object_type).namespace
            ns = META.lookup_namespace(namespace)

            output_string += ('xmlns:' + ns.prefix + '=' + '"' + namespace + '"' + ' \n ')
            schemalocs.append(' ' + namespace + ' ' + ns.schema_location)

        for object_type_dependency in self.object_type_dependencies:
            if object_type_dependency not in self.object_types:
                namespace = META.lookup_object(object_type_dependency).namespace
                ns = META.lookup_namespace(namespace)
                output_string += ('xmlns:' + ns.prefix + '=' + '"' + namespace + '"' + ' \n ')

        output_string += 'xsi:schemaLocation="'

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
            'http://cybox.mitre.org/cybox-2': ['cybox', 'http://cybox.mitre.org/XMLSchema/core/2.0.1/cybox_core.xsd'],
            'http://cybox.mitre.org/common-2': ['cyboxCommon', 'http://cybox.mitre.org/XMLSchema/common/2.0.1/cybox_common.xsd']
        }

        for object_type in itertools.chain(self.object_types, self.object_type_dependencies):
            namespace = META.lookup_object(object_type).namespace
            ns = META.lookup_namespace(namespace)

            namespace_dict[namespace] = [ns.prefix, ns.schema_location]

        return namespace_dict
