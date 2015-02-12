# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_route_entry_object as network_route_entry_binding
from cybox.common import ObjectProperties, String, UnsignedLong, Duration
from cybox.objects.address_object import Address


class NetworkRouteEntry(ObjectProperties):
    _binding = network_route_entry_binding
    _binding_class = network_route_entry_binding.NetworkRouteEntryObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteEntryObject-2"
    _XSI_NS = "NetworkRouteEntryObj"
    _XSI_TYPE = "NetworkRouteEntryObjectType"

    is_ipv6 = cybox.TypedField("is_ipv6")
    is_autoconfigure_address = cybox.TypedField("is_autoconfigure_address")
    is_immortal = cybox.TypedField("is_immortal")
    is_loopback = cybox.TypedField("is_loopback")
    is_publish = cybox.TypedField("is_publish")
    
    destination_address = cybox.TypedField("Destination_Address", Address)
    origin = cybox.TypedField("Origin", Address)
    netmask = cybox.TypedField("Netmask", Address)
    gateway_address = cybox.TypedField("Gateway_Address", Address)
    metric = cybox.TypedField("Metric", UnsignedLong)
    
    type_ = cybox.TypedField("Type", String)
    protocol = cybox.TypedField("Protocol", String)
    interface = cybox.TypedField("Interface", String)
    preferred_lifetime = cybox.TypedField("Preferred_Lifetime", Duration)
    valid_lifetime = cybox.TypedField("Valid_Lifetime", Duration)
    route_age = cybox.TypedField("Route_Age", Duration)
    