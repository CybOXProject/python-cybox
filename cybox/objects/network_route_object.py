# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.network_route_object as network_route_binding
from cybox.common import Duration, ObjectProperties, StructuredText
from cybox.objects.network_route_entry_object import NetworkRouteEntry


class NetworkRouteEntries(entities.EntityList):
    _binding = network_route_binding
    _binding_class = network_route_binding.NetworkRouteEntriesType
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteObject-2"
    network_route_entry = fields.TypedField("Network_Route_Entry", NetworkRouteEntry, multiple=True)


class NetRoute(ObjectProperties):
    _binding = network_route_binding
    _binding_class = network_route_binding.NetRouteObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkRouteObject-2"
    _XSI_NS = "NetworkRouteObj"
    _XSI_TYPE = "NetRouteObjectType"

    is_ipv6 = fields.TypedField("is_ipv6")
    is_autoconfigure_address = fields.TypedField("is_autoconfigure_address")
    is_immortal = fields.TypedField("is_immortal")
    is_loopback = fields.TypedField("is_loopback")
    is_publish = fields.TypedField("is_publish")

    description = fields.TypedField("Description", StructuredText)
    preferred_lifetime = fields.TypedField("Preferred_Lifetime", Duration)
    valid_lifetime = fields.TypedField("Valid_Lifetime", Duration)
    route_age = fields.TypedField("Route_Age", Duration)

    network_route_entries = fields.TypedField("Network_Route_Entries", NetworkRouteEntries)
