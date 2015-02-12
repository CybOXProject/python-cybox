# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.network_subnet_object as network_subnet_binding
from cybox.objects.network_route_entry_object import NetworkRouteEntry
from cybox.common import ObjectProperties, String, StructuredText, Integer

class Routes(cybox.EntityList):
    _binding = network_subnet_binding
    _binding_class = network_subnet_binding.RoutesType
    _binding_var = "Route"
    _contained_type = NetworkRouteEntry
    _namespace = "http://cybox.mitre.org/objects#NetworkSubnetObject-2"

class NetworkSubnet(ObjectProperties):
    _binding = network_subnet_binding
    _binding_class = network_subnet_binding.NetworkSubnetObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkSubnetObject-2"
    _XSI_NS = "NetworkSubnetObj"
    _XSI_TYPE = "NetworkSubnetObjectType"

    name = cybox.TypedField("Name", String)
    description = cybox.TypedField("Description", StructuredText)
    number_of_ip_addresses = cybox.TypedField("Number_Of_IP_Addresses", Integer)
    routes = cybox.TypedField("Routes", Routes)


