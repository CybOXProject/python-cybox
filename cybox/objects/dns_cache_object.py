# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.dns_cache_object as dns_cache_binding
from cybox.common import ObjectProperties, PositiveInteger
from cybox.objects.dns_record_object import DNSRecord


class DNSCacheEntry(entities.Entity):
    _namespace = "http://cybox.mitre.org/objects#DNSCacheObject-2"
    _binding = dns_cache_binding
    _binding_class = dns_cache_binding.DNSCacheEntryType

    dns_entry = fields.TypedField("DNS_Entry", DNSRecord)
    ttl = fields.TypedField("TTL", PositiveInteger)


class DNSCache(ObjectProperties):
    _binding = dns_cache_binding
    _binding_class = dns_cache_binding.DNSCacheObjectType
    _namespace = "http://cybox.mitre.org/objects#DNSCacheObject-2"
    _XSI_NS = "DNSCacheObj"
    _XSI_TYPE = "DNSCacheObjectType"

    dns_cache_entry = fields.TypedField("DNS_Cache_Entry", DNSCacheEntry,
                                       multiple=True)
