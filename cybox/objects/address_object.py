# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.address_object as address_binding

from cybox.common import ObjectProperties, String, Integer


class Address(ObjectProperties):
    _binding = address_binding
    _namespace = 'http://cybox.mitre.org/objects#AddressObject-2'
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

    def __init__(self, address_value=None, category=None):
        super(Address, self).__init__()
        self.address_value = address_value
        self.category = category
        self.is_destination = None
        self.is_source = None
        self.vlan_name = None
        self.vlan_num = None

    def __str__(self):
        return str(self.address_value)

    @property
    def address_value(self):
        return self._address_value

    @address_value.setter
    def address_value(self, value):
        if value is not None and not isinstance(value, String):
            value = String(value)
        self._address_value = value

    # Shortcuts
    @property
    def condition(self):
        return self.address_value.condition

    @condition.setter
    def condition(self, value):
        self.address_value.condition = value

    def to_obj(self):
        addr_object = address_binding.AddressObjectType()
        super(Address, self).to_obj(addr_object)

        if self.address_value is not None:
            addr_object.set_Address_Value(self.address_value.to_obj())
        if self.category is not None:
            addr_object.set_category(self.category)
        if self.is_destination is not None:
            addr_object.set_is_destination(self.is_destination)
        if self.is_source is not None:
            addr_object.set_is_source(self.is_source)
        if self.vlan_name is not None:
            addr_object.set_VLAN_Name(self.vlan_name.to_obj())
        if self.vlan_num is not None:
            addr_object.set_VLAN_Num(self.vlan_num.to_obj())

        return addr_object

    def to_dict(self):
        address_dict = {}
        super(Address, self).to_dict(address_dict)

        if self.address_value is not None:
            address_dict['address_value'] = self.address_value.to_dict()
        if self.category is not None:
            address_dict['category'] = self.category
        if self.is_destination is not None:
            address_dict['is_destination'] = self.is_destination
        if self.is_source is not None:
            address_dict['is_source'] = self.is_source
        if self.vlan_name is not None:
            address_dict['vlan_name'] = self.vlan_name.to_dict()
        if self.vlan_num is not None:
            address_dict['vlan_num'] = self.vlan_num.to_dict()

        return address_dict

    @staticmethod
    def from_obj(addr_object):
        if not addr_object:
            return None

        addr = Address()
        ObjectProperties.from_obj(addr_object, addr)

        addr.address_value = String.from_obj(addr_object.get_Address_Value())
        addr.category = addr_object.get_category()
        addr.is_destination = addr_object.get_is_destination()
        addr.is_source = addr_object.get_is_source()
        addr.vlan_name = String.from_obj(addr_object.get_VLAN_Name())
        addr.vlan_num = Integer.from_obj(addr_object.get_VLAN_Num())

        return addr

    @staticmethod
    def from_dict(addr_dict, category=None):
        if not addr_dict:
            return None

        addr = Address()

        # Shortcut if only a string is passed as a parameter
        if not isinstance(addr_dict, dict):
            addr.address_value = String.from_dict(addr_dict)
            addr.category = category
            return addr

        ObjectProperties.from_dict(addr_dict, addr)

        addr.category = addr_dict.get('category')
        addr.is_destination = addr_dict.get('is_destination')
        addr.is_source = addr_dict.get('is_source')
        addr.address_value = String.from_dict(addr_dict.get('address_value'))
        addr.vlan_name = String.from_dict(addr_dict.get('vlan_name'))
        addr.vlan_number = Integer.from_dict(addr_dict.get('vlan_number'))

        return addr


class EmailAddress(Address):
    """Convenience class for creating email addresses.

    Note that this is not an actual CybOX type."""

    def __init__(self, addr_string):
        super(EmailAddress, self).__init__(addr_string, Address.CAT_EMAIL)
