# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.arp_cache_object as arp_binding
from cybox.objects.address_object import Address
from cybox.objects.system_object import NetworkInterface
from cybox.common import ObjectProperties, String, HexBinary, StructuredText, PlatformSpecification

class ARPCacheEntry(cybox.Entity):
    _binding = arp_binding
    _binding_class = arp_binding.ARPCacheEntryType
    _namespace = "http://cybox.mitre.org/objects#ARPCacheObject-1"
    
    ip_address = cybox.TypedField("IP_Address", Address)
    physical_address = cybox.TypedField("Physical_Address", String)
    type_ = cybox.TypedField("Type", String)
    network_interface = cybox.TypedField("Network_Interface", NetworkInterface)

class ARPCache(ObjectProperties):
    _binding = arp_binding
    _binding_class = arp_binding.ARPCacheObjectType
    _namespace = "http://cybox.mitre.org/objects#ARPCacheObject-1"
    _XSI_NS = "ARPCacheObj"
    _XSI_TYPE = "ARPCacheObjectType"

    arp_cache_entry = cybox.TypedField("ARP_Cache_Entry", ARPCacheEntry, multiple=True)
