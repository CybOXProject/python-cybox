import common_methods
import cybox.bindings.address_object_1_2 as address_binding
from cybox.bindings.cybox_common_types_1_0 import StringObjectAttributeType as String
from cybox.bindings.cybox_common_types_1_0 import IntegerObjectAttributeType as Integer

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

    CATS = (CAT_IPV4, CAT_EMAIL) # only allow these for now

    def __init__(self):
        # Initialize members so things don't break.
        self.is_destination = False
        self.is_source = False
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

    @property
    def is_destination(self):
        return self._is_destination

    @is_destination.setter
    def is_destination(self, value):
        self._is_destination = value

    @property
    def is_source(self):
        return self._is_source

    @is_source.setter
    def is_source(self, value):
        self._is_source = value

    @property
    def address_value(self):
        return self._address_value

    @address_value.setter
    def address_value(self, value):
        self._address_value = value

    @property
    def ext_category(self):
        return self._ext_category

    @ext_category.setter
    def ext_category(self, value):
        self._ext_category = value

    @property
    def vlan_name(self):
        return self._vlan_name

    @vlan_name.setter
    def vlan_name(self, value):
        self._vlan_name = value

    @property
    def vlan_number(self):
        return self._vlan_number

    @vlan_number.setter
    def vlan_number(self, value):
        self._vlan_number = value

    # Import/Export
    def to_obj(self):
        addr_object = address_binding.AddressObjectType()
        addr_object.set_anyAttributes_(
                {'xsi:type': 'AddressObj:AddressObjectType'})

        # Required fields
        addr_object.set_category(self.category)
        addr_object.set_is_destination(self.is_destination)
        addr_object.set_is_source(self.is_source)
        addr_object.set_Address_Value(String(valueOf_=self.address_value))

        # Optional fields
        if self.ext_category is not None:
            addr_object.set_Ext_Category(String(valueOf_=self.ext_category))
        if self.vlan_name is not None:
            addr_object.set_VLAN_Name(String(valueOf_=self.vlan_name))
        if self.vlan_num is not None:
            addr_object.set_VLAN_Num(Integer(valueOf_=self.vlan_num))

        return addr_object

    def to_dict(self):
        result = {}

        # Required fields
        result['category'] = self.category
        result['is_destination'] = self.is_destination
        result['is_source'] = self.is_source
        result['address_value'] = self.address_value

        # Optional fields
        if self.ext_category is not None:
            result['ext_category'] = self.ext_category
        if self.vlan_name is not None:
            result['vlan_name'] = self.vlan_name
        if self.vlan_num is not None:
            result['vlan_num'] = self.vlan_num

        return result

    @staticmethod
    def from_obj(addr_object):
        addr = Address()
        addr.category = addr_object.get_category()
        addr.is_destination = addr_object.get_is_destination()
        addr.is_source = addr_object.get_is_source()
        addr.address_value = addr_object.get_Address_Value().get_valueOf_()

        # Optional fields
        ext = addr_object.get_Ext_Category()
        if ext:
            addr.ext_category = ext.get_valueOf_()
        vname = addr_object.get_VLAN_Name()
        if vname:
            addr.vlan_name = vname.get_valueOf_()
        vnum = addr_object.get_VLAN_Num()
        if vnum:
            addr.vlan_num = vnum.get_valueOf_()
        return addr

    @staticmethod
    def from_dict(addr_dict):
        address = Address()

        if 'category' in addr_dict:
            address.category = addr_dict['category']
        if 'is_destination' in addr_dict:
            address.is_destination = addr_dict['is_destination']
        if 'is_source' in addr_dict:
            address.is_source = addr_dict['is_source']
        if 'address_value' in addr_dict:
            address.address_value = addr_dict['address_value']
        if 'ext_category' in addr_dict:
            address.ext_category = addr_dict['ext_category']
        if 'vlan_name' in addr_dict:
            address.vlan_name = addr_dict['vlan_name']
        if 'vlan_number' in addr_dict:
            address.vlan_number = addr_dict['vlan_number']

        return address

    # Conversion
    @classmethod
    def object_from_dict(cls, address_attributes):
        """Create the Address Object object representation from an input dictionary"""
        return cls.from_dict(address_attributes).to_obj()

    @classmethod
    def dict_from_object(cls, defined_object):
        """Parse and return a dictionary for an Address Object object"""
        return cls.from_obj(defined_object).to_dict()

