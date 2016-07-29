# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.network_subnet_object as network_subnet_binding
from cybox.objects.network_route_entry_object import NetworkRouteEntry
from cybox.common import ObjectProperties, String, StructuredText, Integer


class Routes(entities.EntityList):
    _binding = network_subnet_binding
    _binding_class = network_subnet_binding.RoutesType
    _namespace = "http://cybox.mitre.org/objects#NetworkSubnetObject-2"
    route = fields.TypedField("Route", NetworkRouteEntry, multiple=True)


class NetworkSubnet(ObjectProperties):
    _binding = network_subnet_binding
    _binding_class = network_subnet_binding.NetworkSubnetObjectType
    _namespace = "http://cybox.mitre.org/objects#NetworkSubnetObject-2"
    _XSI_NS = "NetworkSubnetObj"
    _XSI_TYPE = "NetworkSubnetObjectType"

    name = fields.TypedField("Name", String)
    description = fields.TypedField("Description", StructuredText)
    number_of_ip_addresses = fields.TypedField("Number_Of_IP_Addresses", Integer)
    routes = fields.TypedField("Routes", Routes)
