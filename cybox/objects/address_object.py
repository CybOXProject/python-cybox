import cybox.bindings.address_object_1_2 as address_binding

from cybox.common.attributes import String, Integer
from cybox.common.defined_object import DefinedObject

class Address(DefinedObject):
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
    CAT_EXT = "ext-value"

    CATS = (CAT_IPV4, CAT_EMAIL, None) # only allow these for now

    def __init__(self):
        self.address_value = None
        self.category = None
        self.is_destination = None
        self.is_source = None
        self.ext_category = None
        self.vlan_name = None
        self.vlan_num = None

    # Properties
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value not in Address.CATS:
            raise ValueError("Unknown Category: %s" % value)
        self._category = value

    # Import/Export
    def to_obj(self):
        addr_object = address_binding.AddressObjectType()
        addr_object.set_anyAttributes_(
                {'xsi:type': 'AddressObj:AddressObjectType'})

        if self.address_value is not None:
            addr_object.set_Address_Value(self.address_value.to_obj())
        if self.category is not None:
            addr_object.set_category(self.category)
        if self.is_destination is not None:
            addr_object.set_is_destination(self.is_destination)
        if self.is_source is not None:
            addr_object.set_is_source(self.is_source)
        if self.ext_category is not None:
            addr_object.set_Ext_Category(self.ext_category.to_obj())
        if self.vlan_name is not None:
            addr_object.set_VLAN_Name(self.vlan_name.to_obj())
        if self.vlan_num is not None:
            addr_object.set_VLAN_Num(self.vlan_num.to_obj())

        return addr_object

    def to_dict(self):
        result = {}

        if self.address_value is not None:
            result['address_value'] = self.address_value.to_dict()
        if self.category is not None:
            result['category'] = self.category
        if self.is_destination is not None:
            result['is_destination'] = self.is_destination
        if self.is_source is not None:
            result['is_source'] = self.is_source
        if self.ext_category is not None:
            result['ext_category'] = self.ext_category.to_dict()
        if self.vlan_name is not None:
            result['vlan_name'] = self.vlan_name.to_dict()
        if self.vlan_num is not None:
            result['vlan_num'] = self.vlan_num.to_dict()

        return result

    @staticmethod
    def from_obj(addr_object):
        if not addr_object:
            return None

        addr = Address()

        addr.address_value = String.from_obj(addr_object.get_Address_Value())
        addr.category = addr_object.get_category()
        addr.is_destination = addr_object.get_is_destination()
        addr.is_source = addr_object.get_is_source()
        addr.ext_category = String.from_obj(addr_object.get_Ext_Category())
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

        if 'category' in addr_dict:
            addr.category = addr_dict['category']
        if 'is_destination' in addr_dict:
            addr.is_destination = addr_dict['is_destination']
        if 'is_source' in addr_dict:
            addr.is_source = addr_dict['is_source']
        if 'address_value' in addr_dict:
            addr.address_value = String.from_dict(addr_dict['address_value'])
        if 'ext_category' in addr_dict:
            addr.ext_category = String.from_dict(addr_dict['ext_category'])
        if 'vlan_name' in addr_dict:
            addr.vlan_name = String.from_dict(addr_dict['vlan_name'])
        if 'vlan_number' in addr_dict:
            addr.vlan_number = Integer.from_dict(addr_dict['vlan_number'])

        return addr
