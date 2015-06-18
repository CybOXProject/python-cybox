# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_network_route_entry_object as win_network_route_entry_binding
from cybox.objects.network_route_entry_object import NetworkRouteEntry
from cybox.common import String


class WinNetworkRouteEntry(NetworkRouteEntry):
    _binding = win_network_route_entry_binding
    _binding_class = win_network_route_entry_binding.WindowsNetworkRouteEntryObjectType
    _namespace = "http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2"
    _XSI_NS = "WinNetworkRouteEntryObj"
    _XSI_TYPE = "WindowsNetworkRouteEntryObjectType"

    nl_route_protocol = fields.TypedField("NL_ROUTE_PROTOCOL", String)
    nl_route_origin = fields.TypedField("NL_ROUTE_ORIGIN", String)
