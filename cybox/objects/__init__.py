# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


class UnknownObjectType(Exception):
    pass


def get_class_for_object_type(object_type):
    return _OBJ_META.get_class_for_object_type(object_type)


class _ObjectType(object):

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


class _ObjectMetadata(object):
    """Metadata about CybOX objects."""

    def __init__(self, object_list):
        self._obj_dict = {}

        for obj in object_list:
            o = _ObjectType(*obj)
            self.add_object(o)

    def add_object(self, object_type):
        # TODO: are there other ways we want to look up this data?
        self._obj_dict[object_type.name] = object_type

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
# A list of (object_name, api_class, binding, namespace, dependencies) tuples
# This is loaded by the ObjectMetadata class and should not be accessed
# directly.
OBJ_LIST = [
    ('AccountObjectType', 'cybox.objects.account_object.Account', 'account_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/account-2', []),
    ('AddressObjectType', 'cybox.objects.address_object.Address', 'address_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/address-2', []),
    ('APIObjectType', 'cybox.objects.api_object.API', 'api_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/api-2', []),
    ('ArchiveFileObjectType', 'cybox.objects.archive_file_object.ArchiveFile', 'archive_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/archive-file-1', ['FileObjectType']),
    ('ArtifactObjectType', 'cybox.objects.artifact_object.Artifact', 'artifact_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/artifact-2', []),
    ('ARPCacheObjectType', 'cybox.objects.arp_cache_object.ARPCache', 'arp_cache_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/arp-cache-1', []),
    ('ASObjectType', 'cybox.objects.as_object.AS', 'as_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/as-1', []),
    ('CodeObjectType', 'cybox.objects.code_object.Code', 'code_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/code-2', []),
    ('CustomObjectType', 'cybox.objects.custom_object.Custom', 'custom_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/custom-1', []),
    ('DeviceObjectType', 'cybox.objects.device_object.Device', 'device_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/device-2', []),
    ('DiskObjectType', 'cybox.objects.disk_object.Disk', 'disk_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/disk-2', ['DiskPartitionObjectType']),
    ('DiskPartitionObjectType', 'cybox.objects.disk_partition_object.DiskPartition', 'disk_partition_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/disk-partition-2', []),
    ('DNSCacheObjectType', 'cybox.objects.dns_cache_object.DNSCache', 'dns_cache_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/dns-cache-2', ['DNSRecordObjectType', 'AddressObjectType', 'URIObjectType']),
    ('DNSQueryObjectType', 'cybox.objects.dns_query_object.DNSQuery', 'dns_query_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/dns-query-2', ['DNSRecordObjectType', 'URIObjectType', 'AddressObjectType']),
    ('DNSRecordObjectType', 'cybox.objects.dns_record_object.DNSRecord', 'dns_record_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/dns-record-2', ['URIObjectType', 'AddressObjectType']),
    ('DomainNameObjectType', 'cybox.objects.domain_name_object.DomainName', 'domain_name_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/domain-name-1', []),
    ('EmailMessageObjectType', 'cybox.objects.email_message_object.EmailMessage', 'email_message_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/email-message-2', ['FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('FileObjectType', 'cybox.objects.file_object.File', 'file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/file-2', []),
    ('GUIDialogboxObjectType', 'cybox.objects.gui_dialogbox_object.GUIDialogbox', 'gui_dialogbox_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/gui-dialogbox-2', ['GUIObjectType']),
    ('GUIObjectType', 'cybox.objects.gui_object.GUI', 'gui_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/gui-2', []),
    ('GUIWindowObjectType', 'cybox.objects.gui_window_object.GUIWindow', 'gui_window_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/gui-window-2', ['GUIObjectType']),
    ('HostnameObjectType', 'cybox.objects.hostname_object.Hostname', 'hostname_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/hostname-1', []),
    ('HTTPSessionObjectType', 'cybox.objects.http_session_object.HTTPSession', 'http_session_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/http-session-2', ['AddressObjectType', 'PortObjectType', 'URIObjectType']),
    ('ImageFileObjectType', 'cybox.objects.image_file_object.ImageFile', 'image_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/image-file-1', ['FileObjectType']),
    ('LibraryObjectType', 'cybox.objects.library_object.Library', 'library_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/library-2', []),
    ('LinkObjectType', 'cybox.objects.link_object.Link', 'link_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/link-1', ['URIObjectType']),
    ('LinuxPackageObjectType', 'cybox.objects.linux_package_object.LinuxPackage', 'linux_package_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/linux-package-2', []),
    ('MemoryObjectType', 'cybox.objects.memory_object.Memory', 'memory_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/memory-2', []),
    ('MutexObjectType', 'cybox.objects.mutex_object.Mutex', 'mutex_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/mutex-2', []),
    ('NetRouteObjectType', 'cybox.objects.network_route_object.NetRoute', 'network_route_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-route-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('NetworkConnectionObjectType', 'cybox.objects.network_connection_object.NetworkConnection', 'network_connection_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-connection-2', ['SocketAddressObjectType', 'HTTPSessionObjectType', 'DNSQueryObjectType', 'DNSRecordObjectType', 'URIObjectType']),
    ('NetworkFlowObjectType', None, 'network_flow_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-flow-2', ['NetworkPacketType', 'AddressObjectType', 'SocketAddressObjectType']),
    ('NetworkPacketObjectType', 'cybox.objects.network_packet_object.NetworkPacket', 'network_packet_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-packet-2', ['AddressObjectType', 'PortObjectType']),
    ('NetworkRouteEntryObjectType', 'cybox.objects.network_route_entry_object.NetworkRouteEntry', 'network_route_entry_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-route-entry-2', ['AddressObjectType']),
    ('NetworkSocketObjectType', 'cybox.objects.network_socket_object.NetworkSocket', 'network_socket_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-socket-2', ['SocketAddressObjectType']),
    ('NetworkSubnetObjectType', 'cybox.objects.network_subnet_object.NetworkSubnet', 'network_subnet_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/network-subnet-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('PDFFileObjectType', 'cybox.objects.pdf_file_object.PDFFile', 'pdf_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/pdf-file-1', ['FileObjectType']),
    ('PipeObjectType', 'cybox.objects.pipe_object.Pipe', 'pipe_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/pipe-2', []),
    ('PortObjectType', 'cybox.objects.port_object.Port', 'port_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/port-2', []),
    ('ProcessObjectType', 'cybox.objects.process_object.Process', 'process_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/process-2', ['NetworkConnectionObjectType', 'PortObjectType']),
    ('ProductObjectType', 'cybox.objects.product_object.Product', 'product_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/product-2', []),
    ('SemaphoreObjectType', 'cybox.objects.semaphore_object.Semaphore', 'semaphore_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/semaphore-2', []),
    ('SMSMessageObjectType', 'cybox.objects.sms_message_object.SMSMessage', 'sms_message_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/sms-message-1', []),
    ('SocketAddressObjectType', 'cybox.objects.socket_address_object.SocketAddress', 'socket_address_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/socket-address-1', ['AddressObjectType', 'PortObjectType']),
    ('SystemObjectType', 'cybox.objects.system_object.System', 'system_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/system-2', ['AddressObjectType']),
    ('UnixFileObjectType', None, 'unix_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-file-2', ['FileObjectType']),
    ('UnixNetworkRouteEntryObjectType', None, 'unix_network_route_entry_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-network-route-entry-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('UnixPipeObjectType', None, 'unix_pipe_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-pipe-2', ['PipeObjectType']),
    ('UnixProcessObjectType', None, 'unix_process_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-process-2', ['ProcessObjectType', 'AddressObjectType', 'PortObjectType']),
    ('UnixUserAccountObjectType', None, 'unix_user_account_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-user-account-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('UnixVolumeObjectType', None, 'unix_volume_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/unix-volume-2', ['VolumeObjectType']),
    ('URIObjectType', 'cybox.objects.uri_object.URI', 'uri_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/uri-2', []),
    ('URLHistoryObjectType', None, 'url_history_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/url-history-1', ['URIObjectType','HostnameObjectType']),
    ('UserAccountObjectType', 'cybox.objects.user_account_object.UserAccount', 'user_account_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/user-account-2', ['AccountObjectType']),
    ('VolumeObjectType', 'cybox.objects.volume_object.Volume', 'volume_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/volume-2', []),
    ('WhoisObjectType', 'cybox.objects.whois_object.WhoisEntry', 'whois_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/whois-2', ['URIObjectType', 'AddressObjectType']),
    ('WindowsComputerAccountObjectType', 'cybox.objects.win_computer_account_object.WinComputerAccount', 'win_computer_account_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-computer-account-2', ['AccountObjectType', 'PortObjectType']),
    ('WindowsCriticalSectionObjectType', 'cybox.objects.win_critical_section_object.WinCriticalSection', 'win_critical_section_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-critical-section-2', []),
    ('WindowsDriverObjectType', 'cybox.objects.win_driver_object.WinDriver', 'win_driver_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-driver-3', []),
    ('WindowsEventLogObjectType', 'cybox.objects.win_event_log_object.WinEventLog', 'win_event_log_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-event-log-2', []),
    ('WindowsEventObjectType', 'cybox.objects.win_event_object.WinEvent', 'win_event_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-event-2', ['WindowsHandleObjectType']),
    ('WindowsExecutableFileObjectType', 'cybox.objects.win_executable_file_object.WinExecutableFile', 'win_executable_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-executable-file-2', ['WindowsFileObjectType', 'FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsFileObjectType', 'cybox.objects.win_file_object.WinFile', 'win_file_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-file-2', ['FileObjectType', 'WinComputerAccountObjectType', 'AccountObjectType', 'PortObjectType']),
    ('WindowsFilemappingObjectType', 'cybox.objects.win_filemapping_object.WinFilemapping', 'win_filemapping_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-filemapping-1', ['WindowsHandleObjectType']),
    ('WindowsHandleObjectType', 'cybox.objects.win_handle_object.WinHandle', 'win_handle_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-handle-2', []),
    ('WindowsHookObjectType', 'cybox.objects.win_hook_object.WinHook', 'windows_hook_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-hook-1', ['WindowsHandleObjectType','LibraryObjectType']),
    ('WindowsKernelHookObjectType', 'cybox.objects.win_kernel_hook_object.WinKernelHook', 'win_kernel_hook_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-kernel-hook-2', []),
    ('WindowsKernelObjectType', 'cybox.objects.win_kernel_object.WinKernel', 'win_kernel_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-kernel-2', []),
    ('WindowsMailslotObjectType', 'cybox.objects.win_mailslot_object.WinMailslot', 'win_mailslot_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-mailslot-2', ['WindowsHandleObjectType']),
    ('WindowsMemoryPageRegionObjectType', 'cybox.objects.win_memory_page_region_object.WinMemoryPageRegion', 'win_memory_page_region_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-memory-page-region-2', ['MemoryObjectType']),
    ('WindowsMutexObjectType', 'cybox.objects.win_mutex_object.WinMutex', 'win_mutex_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-mutex-2', ['WindowsHandleObjectType', 'MutexObjectType']),
    ('WindowsNetworkRouteEntryObjectType', 'cybox.objects.win_network_route_entry_object.WinNetworkRouteEntry', 'win_network_route_entry_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-network-route-entry-2', ['NetworkRouteEntryObjectType', 'AddressObjectType']),
    ('WindowsNetworkShareObjectType', 'cybox.objects.win_network_share_object.WinNetworkShare', 'win_network_share_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-network-share-2', []),
    ('WindowsPipeObjectType', 'cybox.objects.win_pipe_object.WinPipe', 'win_pipe_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-pipe-2', ['PipeObjectType']),
    ('WindowsPrefetchObjectType', 'cybox.objects.win_prefetch_object.WinPrefetch', 'win_prefetch_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-prefetch-2', ['WindowsVolumeObjectType', 'VolumeObjectType', 'DeviceObjectType']),
    ('WindowsProcessObjectType', 'cybox.objects.win_process_object.WinProcess', 'win_process_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-process-2', ['ProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsRegistryKeyObjectType', 'cybox.objects.win_registry_key_object.WinRegistryKey', 'win_registry_key_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-registry-key-2', ['WindowsHandleObjectType']),
    ('WindowsSemaphoreObjectType', 'cybox.objects.win_semaphore_object.WinSemaphore', 'win_semaphore_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-semaphore-2', ['WindowsHandleObjectType', 'SemaphoreObjectType']),
    ('WindowsServiceObjectType', 'cybox.objects.win_service_object.WinService', 'win_service_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-service-2', ['WindowsProcessObjectType', 'WindowsHandleObjectType', 'MemoryObjectType', 'AddressObjectType', 'PortObjectType']),
    ('WindowsSystemObjectType', 'cybox.objects.win_system_object.WinSystem', 'win_system_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-system-2', ['WindowsHandleObjectType', 'SystemObjectType', 'AddressObjectType']),
    ('WindowsSystemRestoreObjectType', 'cybox.objects.win_system_restore_object.WinSystemRestore', 'win_system_restore_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-system-restore-2', []),
    ('WindowsTaskObjectType', 'cybox.objects.win_task_object.WinTask', 'win_task_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-task-2', ['EmailMessageObjectType', 'FileObjectType', 'AddressObjectType', 'URIObjectType']),
    ('WindowsThreadObjectType', 'cybox.objects.win_thread_object.WinThread', 'win_thread_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-thread-2', ['WindowsHandleObjectType']),
    ('WindowsUserAccountObjectType', 'cybox.objects.win_user_object.WinUser', 'win_user_account_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-user-account-2', ['UserAccountObjectType', 'AccountObjectType']),
    ('WindowsVolumeObjectType', 'cybox.objects.win_volume_object.WinVolume', 'win_volume_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-volume-2', ['VolumeObjectType']),
    ('WindowsWaitableTimerObjectType', 'cybox.objects.win_waitable_timer_object.WinWaitableTimer', 'win_waitable_timer_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/win-waitable-timer-2', ['WindowsHandleObjectType']),
    ('X509CertificateObjectType', 'cybox.objects.x509_certificate_object.X509Certificate', 'x509_certificate_object', 'http://docs.oasis-open.org/cti/ns/cybox/objects/x509-certificate-2', []),
]


_OBJ_META = _ObjectMetadata(OBJ_LIST)
