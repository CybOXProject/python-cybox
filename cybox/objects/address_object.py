# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields
from mixbox.vendor import six

import cybox.bindings.address_object as address_binding
from cybox.common import ObjectProperties, String, Integer


@six.python_2_unicode_compatible
class Address(ObjectProperties):
    _binding = address_binding
    _binding_class = _binding.AddressObjectType
    _namespace = 'http://cybox.mitre.org/objects#AddressObject-2'
    _value_field = 'address_value'
    _XSI_NS = 'AddressObj'
    _XSI_TYPE = 'AddressObjectType'

    CAT_ASN = "asn"
    CAT_ATM = "atm"
    CAT_CIDR = "cidr"
    CAT_EMAIL = "e-mail"
    CAT_MAC = "mac"
    CAT_IPV4 = "ipv4-addr"
    CAT_IPV4_NET = "ipv4-net"
    CAT_IPV4_NETMASK = "ipv4-netmask"
    CAT_IPV6 = "ipv6-addr"
    CAT_IPV6_NET = "ipv6-net"
    CAT_IPV6_NETMASK = "ipv6-netmask"

    address_value = fields.TypedField("Address_Value", String)
    category = fields.TypedField("category")
    is_destination = fields.TypedField("is_destination")
    is_source = fields.TypedField("is_source")
    is_spoofed = fields.TypedField("is_spoofed")
    vlan_name = fields.TypedField("VLAN_Name", String)
    vlan_num = fields.TypedField("VLAN_Num", Integer)

    def __init__(self, address_value=None, category=None):
        super(Address, self).__init__()
        self.address_value = address_value
        self.category = category

    def __str__(self):
        return six.text_type(self.address_value)

    # Shortcuts
    @property
    def condition(self):
        return self.address_value.condition

    @condition.setter
    def condition(self, value):
        self.address_value.condition = value


class EmailAddress(Address):
    """Convenience class for creating email addresses.

    Note that this is not an actual CybOX type."""

    def __init__(self, addr_string=None):
        super(EmailAddress, self).__init__(addr_string, Address.CAT_EMAIL)

    @classmethod
    def istypeof(cls, obj):
        return isinstance(obj, Address) and obj.category == Address.CAT_EMAIL
