# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.network_route_entry_object as network_route_entry_binding
from cybox.common import ObjectProperties, String, UnsignedLong, Duration
from cybox.objects.address_object import Address


class NetworkRouteEntry(ObjectProperties):
    _binding = network_route_entry_binding
    _binding_class = network_route_entry_binding.NetworkRouteEntryObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteEntryObject-2"
    _XSI_NS = "NetworkRouteEntryObj"
    _XSI_TYPE = "NetworkRouteEntryObjectType"

    is_ipv6 = fields.TypedField("is_ipv6")
    is_autoconfigure_address = fields.TypedField("is_autoconfigure_address")
    is_immortal = fields.TypedField("is_immortal")
    is_loopback = fields.TypedField("is_loopback")
    is_publish = fields.TypedField("is_publish")

    destination_address = fields.TypedField("Destination_Address", Address)
    origin = fields.TypedField("Origin", Address)
    netmask = fields.TypedField("Netmask", Address)
    gateway_address = fields.TypedField("Gateway_Address", Address)
    metric = fields.TypedField("Metric", UnsignedLong)

    type_ = fields.TypedField("Type", String)
    protocol = fields.TypedField("Protocol", String)
    interface = fields.TypedField("Interface", String)
    preferred_lifetime = fields.TypedField("Preferred_Lifetime", Duration)
    valid_lifetime = fields.TypedField("Valid_Lifetime", Duration)
    route_age = fields.TypedField("Route_Age", Duration)
