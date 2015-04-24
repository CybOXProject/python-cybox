API Coverage
============

The *python-cybox* APIs currently provide ⚠ partial coverage of all CybOX-defined constructs. Development is ongoing toward the goal of providing ✓ full CybOX language support in the APIs. Until such time that full coverage is provided, an overview of which constructs are available in these APIs will be maintained below.


CybOX Features
--------------

=============================   ==========================  ==========================================
CybOX Construct                  API Coverage                Documentation
=============================   ==========================  ==========================================
Composite Observable            ✓ Full                      :class:`cybox.core.observable.ObservableComposition`
Event                           ⚠ Partial                   :class:`cybox.core.event.Event`
Object                          ⚠ Partial                   :class:`cybox.core.object.Object`
Observables                     ⚠ Partial                   :class:`cybox.core.observable.Observables`
Observable                      ⚠ Partial                   :class:`cybox.core.observable.Observable`
Relationships                   ⚠ Partial
=============================   ==========================  ==========================================

CybOX Objects
-------------

==================================  =====================   ==========================================================================================
CybOX Construct                     API Coverage            Documentation
==================================  =====================   ==========================================================================================
Account Object                      ✓ Full                  :class:`cybox.objects.account_object.Account`
Address Object                      ✓ Full                  :class:`cybox.objects.address_object.Address`
API Object                          ✓ Full                  :class:`cybox.objects.api_object.API`
Archive File Object                 ✓ Full                  :class:`cybox.objects.archive_file_object.ArchiveFile`
ARP Cache Object                    ✓ Full                  :class:`cybox.objects.arp_cache_object.ARPCache`
Artifact Object                     ✓ Full                  :class:`cybox.objects.artifact_object.Artifact`
AS Object                           ✓ Full                  :class:`cybox.objects.as_object.AutonomousSystem`
Code Object                         ✓ Full                  :class:`cybox.objects.code_object.Code`
Custom Object                       × None
Device Object                       ✓ Full                  :class:`cybox.objects.device_object.Device`
Disk Object                         ✓ Full                  :class:`cybox.objects.disk_object.Disk`
Disk Partition Object               ✓ Full                  :class:`cybox.objects.disk_partition_object.DiskPartition`
DNS Cache Object                    ✓ Full                  :class:`cybox.objects.dns_cache_object.DNSCache`
DNS Query Object                    ✓ Full                  :class:`cybox.objects.dns_query_object.DNSQuery`
DNS Record Object                   ✓ Full                  :class:`cybox.objects.dns_record_object.DNSRecord`
Domain Name Object                  ✓ Full                  :class:`cybox.objects.domain_name_object.DomainName`
Email Message Object                ✓ Full                  :class:`cybox.objects.email_message_object.EmailMessage`
File Object                         ✓ Full                  :class:`cybox.objects.file_object.File`
GUI Dialogbox Object                ✓ Full                  :class:`cybox.objects.gui_dialogbox_object.GUIDialogbox`
GUI Object                          ✓ Full                  :class:`cybox.objects.gui_object.GUI`
GUI Window Object                   ✓ Full                  :class:`cybox.objects.gui_window_object.GUIWindow`
HTTP Session Object                 ✓ Full                  :class:`cybox.objects.http_session_object.HTTPSession`
Hostname Object                     ✓ Full                  :class:`cybox.objects.hostname_object.Hostname`
Image File Object                   ✓ Full                  :class:`cybox.objects.image_file_object.ImageFile`
Library Object                      ✓ Full                  :class:`cybox.objects.library_object.Library`
Link Object                         ✓ Full                  :class:`cybox.objects.link_object.Link`
Linux Package Object                ✓ Full                  :class:`cybox.objects.linux_package_object.LinuxPackage`
Memory Object                       ✓ Full                  :class:`cybox.objects.memory_object.Memory`
Mutex Object                        ✓ Full                  :class:`cybox.objects.mutex_object.Mutex`
Network Connection Object           ✓ Full                  :class:`cybox.objects.network_connection_object.NetworkConnection`
Network Flow Object                 × None
Network Packet Object               ✓ Full                  :class:`cybox.objects.network_packet_object.NetworkPacket`
Network Route Entry Object          ✓ Full                  :class:`cybox.objects.network_route_entry_object.NetworkRouteEntry`
Network Route Object                ✓ Full                  :class:`cybox.objects.network_route_object.NetRoute`
Network Socket Object               ✓ Full                  :class:`cybox.objects.network_socket_object.NetworkSocket`
Network Subnet Object               ✓ Full                  :class:`cybox.objects.network_subnet_object.NetworkSubnet`
PDF File Object                     ⚠ Partial               :class:`cybox.objects.pdf_file_object.PDFFile`
Pipe Object                         ✓ Full                  :class:`cybox.objects.pipe_object.Pipe`
Port Object                         ✓ Full                  :class:`cybox.objects.port_object.Port`
Process Object                      ✓ Full                  :class:`cybox.objects.process_object.Process`
Product Object                      ✓ Full                  :class:`cybox.objects.product_object.Product`
Semaphore Object                    ✓ Full                  :class:`cybox.objects.semaphore_object.Semaphore`
SMS Message Object                  ✓ Full                  :class:`cybox.objects.sms_message_object.SMSMessage`
Socket Address Object               ✓ Full                  :class:`cybox.objects.socket_address_object.SocketAddress`
System Object                       ⚠ Partial               :class:`cybox.objects.system_object.System`
URI Object                          ✓ Full                  :class:`cybox.objects.uri_object.URI`
URL History Object                  × None
Unix File Object                    × None
Unix Network Route Entry Object     × None
Unix Pipe Object                    × None
Unix Process Object                 × None
Unix User Account Object            × None
Unix Volume Object                  × None
User Account Object                 ✓ Full                  :class:`cybox.objects.user_account_object.UserAccount`
User Session Object                 × None
Volume Object                       ✓ Full                  :class:`cybox.objects.volume_object.Volume`
Whois Object                        ✓ Full                  :class:`cybox.objects.whois_object.WhoisEntry`
Win Computer Account Object         ✓ Full                  :class:`cybox.objects.win_computer_account_object.WinComputerAccount`
Win Critical Section Object         ✓ Full                  :class:`cybox.objects.win_critical_section_object.WinCriticalSection`
Win Driver Object                   ✓ Full                  :class:`cybox.objects.win_driver_object.WinDriver`
Win Event Log Object                ✓ Full                  :class:`cybox.objects.win_event_log_object.WinEventLog`
Win Event Object                    ✓ Full                  :class:`cybox.objects.win_event_object.WinEvent`
Win Executable File Object          ✓ Full                  :class:`cybox.objects.win_executable_file_object.WinExecutableFile`
Win File Object                     ✓ Full                  :class:`cybox.objects.win_file_object.WinFile`
Win Filemapping Object              ✓ Full                  :class:`cybox.objects.win_filemapping_object.WinFilemapping`
Win Handle Object                   ✓ Full                  :class:`cybox.objects.win_handle_object.WinHandle`
Win Hook Object                     ✓ Full                  :class:`cybox.objects.win_hook_object.WinHook`
Win Kernel Hook Object              ✓ Full                  :class:`cybox.objects.win_kernel_hook_object.WinKernelHook`
Win Kernel Object                   ✓ Full                  :class:`cybox.objects.win_kernel_object.WinKernel`
Win Mailslot Object                 ✓ Full                  :class:`cybox.objects.win_mailslot_object.WinMailslot`
Win Memory Page Region Object       ✓ Full                  :class:`cybox.objects.win_memory_page_region_object.WinMemoryPageRegion`
Win Mutex Object                    ✓ Full                  :class:`cybox.objects.win_mutex_object.WinMutex`
Win Network Route Entry Object      ✓ Full                  :class:`cybox.objects.win_network_route_entry_object.WinNetworkRouteEntry`
Win Network Share Object            ✓ Full                  :class:`cybox.objects.win_network_share_object.WinNetworkShare`
Win Pipe Object                     ✓ Full                  :class:`cybox.objects.win_pipe_object.WinPipe`
Win Prefetch Object                 ✓ Full                  :class:`cybox.objects.win_prefetch_object.WinPrefetch`
Win Process Object                  ✓ Full                  :class:`cybox.objects.win_process_object.WinProcess`
Win Registry Key Object             ✓ Full                  :class:`cybox.objects.win_registry_key_object.WinRegistryKey`
Win Semaphore Object                ✓ Full                  :class:`cybox.objects.win_semaphore_object.WinSemaphore`
Win Service Object                  ✓ Full                  :class:`cybox.objects.win_service_object.WinService`
Win System Object                   ✓ Full                  :class:`cybox.objects.win_system_object.WinSystem`
Win System Restore Object           ✓ Full                  :class:`cybox.objects.win_system_restore_object.WinSystemRestore`
Win Task Object                     ✓ Full                  :class:`cybox.objects.win_task_object.WinTask`
Win Thread Object                   ✓ Full                  :class:`cybox.objects.win_thread_object.WinThread`
Win User Account Object             ✓ Full                  :class:`cybox.objects.win_user_object.WinUser`
Win Volume Object                   ✓ Full                  :class:`cybox.objects.win_volume_object.WinVolume`
Win Waitable Timer Object           ✓ Full                  :class:`cybox.objects.win_waitable_timer_object.WinWaitableTimer`
X509 Certificate Object             ✓ Full                  :class:`cybox.objects.x509_certificate_object.X509Certificate`
==================================  =====================   ==========================================================================================

CybOX Vocabularies
------------------

=========================================   ========================================    ===========================================================
CybOX Construct                              API Coverage                                Documentation
=========================================   ========================================    ===========================================================
ActionArgumentNameVocab-1.0                 ✓ Full                                      :class:`cybox.common.vocabs.ActionArgumentName`
ActionNameVocab-1.0                         × None *(replaced by version 1.1)*
ActionNameVocab-1.1                         ✓ Full                                      :class:`cybox.common.vocabs.ActionName`
ActionObjectAssociationTypeVocab-1.0        ✓ Full                                      :class:`cybox.common.vocabs.AssociationType`
ActionRelationshipTypeVocab-1.0             × None
ActionTypeVocab-1.0                         ✓ Full                                      :class:`cybox.common.vocabs.ActionType`
CharacterEncodingVocab-1.0                  ✓ Full                                      :class:`cybox.common.vocabs.CharacterEncoding`
EventTypeVocab-1.0                          × None *(replaced by version 1.0.1)*
EventTypeVocab-1.0.1                        ✓ Full                                      :class:`cybox.common.vocabs.EventType`
HashNameVocab-1.0                           ✓ Full                                      :class:`cybox.common.vocabs.HashName`
InformationSourceTypeVocab-1.0              ✓ Full                                      :class:`cybox.common.vocabs.InformationSourceType`
ObjectRelationshipVocab-1.0                 × None *(replaced by version 1.1)*
ObjectRelationshipVocab-1.1                 ✓ Full                                      :class:`cybox.common.vocabs.ObjectRelationship`
ObjectStateVocab-1.0                        × None
ToolTypeVocab-1.0                           × None *(replaced by version 1.1)*
ToolTypeVocab-1.1                           ✓ Full                                      :class:`cybox.common.vocabs.ToolType`
=========================================   ========================================    ===========================================================
