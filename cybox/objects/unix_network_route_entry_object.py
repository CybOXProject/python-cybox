# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.unix_network_route_entry_object as unix_network_route_entry_binding
from cybox.common import String, UnsignedInteger, UnsignedLong
from cybox.objects.network_route_entry_object import NetworkRouteEntry


class UnixNetworkRouteEntry(NetworkRouteEntry):
    _binding = unix_network_route_entry_binding
    _binding_class = unix_network_route_entry_binding.UnixNetworkRouteEntryObjectType
    _namespace = "http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2"
    _XSI_NS = "UnixNetworkRouteEntryObj"
    _XSI_TYPE = "UnixNetworkRouteEntryObjectType"

    flags = fields.TypedField("Flags", String)
    mss = fields.TypedField("MSS", UnsignedInteger)
    ref = fields.TypedField("Ref", UnsignedLong)
    use = fields.TypedField("Use", UnsignedLong)
    window = fields.TypedField("Window", UnsignedInteger)
