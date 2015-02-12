# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_route_object as network_route_binding
from cybox.common import ObjectProperties, String, UnsignedLong, StructuredText, Duration
from cybox.objects.network_route_entry_object import NetworkRouteEntry

class NetworkRouteEntries(cybox.EntityList):
    _binding = network_route_binding
    _binding_class = network_route_binding.NetworkRouteEntriesType
    _binding_var = "Network_Route_Entry"
    _contained_type = NetworkRouteEntry
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteObject-2"
    
class NetRoute(ObjectProperties):
    _binding = network_route_binding
    _binding_class = network_route_binding.NetRouteObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteObject-2"
    _XSI_NS = "NetworkRouteObj"
    _XSI_TYPE = "NetRouteObjectType"

    is_ipv6 = cybox.TypedField("is_ipv6")
    is_autoconfigure_address = cybox.TypedField("is_autoconfigure_address")
    is_immortal = cybox.TypedField("is_immortal")
    is_loopback = cybox.TypedField("is_loopback")
    is_publish = cybox.TypedField("is_publish")
    
    description = cybox.TypedField("Description", StructuredText)
    preferred_lifetime = cybox.TypedField("Preferred_Lifetime", Duration)
    valid_lifetime = cybox.TypedField("Valid_Lifetime", Duration)
    route_age = cybox.TypedField("Route_Age", Duration)

    network_route_entries = cybox.TypedField("Network_Route_Entries", NetworkRouteEntries)
    