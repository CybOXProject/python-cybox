# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object


class BIOSInfoType(GeneratedsSuper):
    """The BIOSInfoType type specifies information about a system's BIOS."""

    subclass = None
    superclass = None
    def __init__(self, BIOS_Date=None, BIOS_Version=None, BIOS_Manufacturer=None, BIOS_Release_Date=None, BIOS_Serial_Number=None):
        self.BIOS_Date = BIOS_Date
        self.BIOS_Version = BIOS_Version
        self.BIOS_Manufacturer = BIOS_Manufacturer
        self.BIOS_Release_Date = BIOS_Release_Date
        self.BIOS_Serial_Number = BIOS_Serial_Number
    def factory(*args_, **kwargs_):
        if BIOSInfoType.subclass:
            return BIOSInfoType.subclass(*args_, **kwargs_)
        else:
            return BIOSInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_BIOS_Date(self): return self.BIOS_Date
    def set_BIOS_Date(self, BIOS_Date): self.BIOS_Date = BIOS_Date
    def validate_DateObjectPropertyType(self, value):
        # Validate type cybox_common.DateObjectPropertyType, a restriction on None.
        pass
    def get_BIOS_Version(self): return self.BIOS_Version
    def set_BIOS_Version(self, BIOS_Version): self.BIOS_Version = BIOS_Version
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_BIOS_Manufacturer(self): return self.BIOS_Manufacturer
    def set_BIOS_Manufacturer(self, BIOS_Manufacturer): self.BIOS_Manufacturer = BIOS_Manufacturer
    def get_BIOS_Release_Date(self): return self.BIOS_Release_Date
    def set_BIOS_Release_Date(self, BIOS_Release_Date): self.BIOS_Release_Date = BIOS_Release_Date
    def get_BIOS_Serial_Number(self): return self.BIOS_Serial_Number
    def set_BIOS_Serial_Number(self, BIOS_Serial_Number): self.BIOS_Serial_Number = BIOS_Serial_Number
    def hasContent_(self):
        if (
            self.BIOS_Date is not None or
            self.BIOS_Version is not None or
            self.BIOS_Manufacturer is not None or
            self.BIOS_Release_Date is not None or
            self.BIOS_Serial_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='BIOSInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BIOSInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='BIOSInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='BIOSInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.BIOS_Date is not None:
            self.BIOS_Date.export(lwrite, level, 'SystemObj:', name_='BIOS_Date', pretty_print=pretty_print)
        if self.BIOS_Version is not None:
            self.BIOS_Version.export(lwrite, level, 'SystemObj:', name_='BIOS_Version', pretty_print=pretty_print)
        if self.BIOS_Manufacturer is not None:
            self.BIOS_Manufacturer.export(lwrite, level, 'SystemObj:', name_='BIOS_Manufacturer', pretty_print=pretty_print)
        if self.BIOS_Release_Date is not None:
            self.BIOS_Release_Date.export(lwrite, level, 'SystemObj:', name_='BIOS_Release_Date', pretty_print=pretty_print)
        if self.BIOS_Serial_Number is not None:
            self.BIOS_Serial_Number.export(lwrite, level, 'SystemObj:', name_='BIOS_Serial_Number', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'BIOS_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_BIOS_Date(obj_)
        elif nodeName_ == 'BIOS_Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_BIOS_Version(obj_)
        elif nodeName_ == 'BIOS_Manufacturer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_BIOS_Manufacturer(obj_)
        elif nodeName_ == 'BIOS_Release_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_BIOS_Release_Date(obj_)
        elif nodeName_ == 'BIOS_Serial_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_BIOS_Serial_Number(obj_)
# end class BIOSInfoType

class NetworkInterfaceListType(GeneratedsSuper):
    """The NetworkInterfaceListType type specifies information about the
    network interfaces present on the system."""

    subclass = None
    superclass = None
    def __init__(self, Network_Interface=None):
        if Network_Interface is None:
            self.Network_Interface = []
        else:
            self.Network_Interface = Network_Interface
    def factory(*args_, **kwargs_):
        if NetworkInterfaceListType.subclass:
            return NetworkInterfaceListType.subclass(*args_, **kwargs_)
        else:
            return NetworkInterfaceListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Interface(self): return self.Network_Interface
    def set_Network_Interface(self, Network_Interface): self.Network_Interface = Network_Interface
    def add_Network_Interface(self, value): self.Network_Interface.append(value)
    def insert_Network_Interface(self, index, value): self.Network_Interface[index] = value
    def hasContent_(self):
        if (
            self.Network_Interface
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='NetworkInterfaceListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkInterfaceListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='NetworkInterfaceListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='NetworkInterfaceListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Network_Interface_ in self.Network_Interface:
            Network_Interface_.export(lwrite, level, 'SystemObj:', name_='Network_Interface', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Network_Interface':
            obj_ = NetworkInterfaceType.factory()
            obj_.build(child_)
            self.Network_Interface.append(obj_)
# end class NetworkInterfaceListType

class IPGatewayListType(GeneratedsSuper):
    """The IPGatewayListType type specifies the IP Addresses of the
    gateways used by the system."""

    subclass = None
    superclass = None
    def __init__(self, IP_Gateway_Address=None):
        if IP_Gateway_Address is None:
            self.IP_Gateway_Address = []
        else:
            self.IP_Gateway_Address = IP_Gateway_Address
    def factory(*args_, **kwargs_):
        if IPGatewayListType.subclass:
            return IPGatewayListType.subclass(*args_, **kwargs_)
        else:
            return IPGatewayListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Gateway_Address(self): return self.IP_Gateway_Address
    def set_IP_Gateway_Address(self, IP_Gateway_Address): self.IP_Gateway_Address = IP_Gateway_Address
    def add_IP_Gateway_Address(self, value): self.IP_Gateway_Address.append(value)
    def insert_IP_Gateway_Address(self, index, value): self.IP_Gateway_Address[index] = value
    def hasContent_(self):
        if (
            self.IP_Gateway_Address
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='IPGatewayListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPGatewayListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='IPGatewayListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='IPGatewayListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for IP_Gateway_Address_ in self.IP_Gateway_Address:
            IP_Gateway_Address_.export(lwrite, level, 'SystemObj:', name_='IP_Gateway_Address', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IP_Gateway_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.IP_Gateway_Address.append(obj_)
# end class IPGatewayListType

class NetworkInterfaceType(GeneratedsSuper):
    """The NetworkInterfaceType type specifies information about a network
    interface, such as its MAC address."""

    subclass = None
    superclass = None
    def __init__(self, Adapter=None, Description=None, DHCP_Lease_Expires=None, DHCP_Lease_Obtained=None, DHCP_Server_List=None, IP_Gateway_List=None, IP_List=None, MAC=None):
        self.Adapter = Adapter
        self.Description = Description
        self.DHCP_Lease_Expires = DHCP_Lease_Expires
        self.DHCP_Lease_Obtained = DHCP_Lease_Obtained
        self.DHCP_Server_List = DHCP_Server_List
        self.IP_Gateway_List = IP_Gateway_List
        self.IP_List = IP_List
        self.MAC = MAC
    def factory(*args_, **kwargs_):
        if NetworkInterfaceType.subclass:
            return NetworkInterfaceType.subclass(*args_, **kwargs_)
        else:
            return NetworkInterfaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Adapter(self): return self.Adapter
    def set_Adapter(self, Adapter): self.Adapter = Adapter
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_DHCP_Lease_Expires(self): return self.DHCP_Lease_Expires
    def set_DHCP_Lease_Expires(self, DHCP_Lease_Expires): self.DHCP_Lease_Expires = DHCP_Lease_Expires
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_DHCP_Lease_Obtained(self): return self.DHCP_Lease_Obtained
    def set_DHCP_Lease_Obtained(self, DHCP_Lease_Obtained): self.DHCP_Lease_Obtained = DHCP_Lease_Obtained
    def get_DHCP_Server_List(self): return self.DHCP_Server_List
    def set_DHCP_Server_List(self, DHCP_Server_List): self.DHCP_Server_List = DHCP_Server_List
    def get_IP_Gateway_List(self): return self.IP_Gateway_List
    def set_IP_Gateway_List(self, IP_Gateway_List): self.IP_Gateway_List = IP_Gateway_List
    def get_IP_List(self): return self.IP_List
    def set_IP_List(self, IP_List): self.IP_List = IP_List
    def get_MAC(self): return self.MAC
    def set_MAC(self, MAC): self.MAC = MAC
    def hasContent_(self):
        if (
            self.Adapter is not None or
            self.Description is not None or
            self.DHCP_Lease_Expires is not None or
            self.DHCP_Lease_Obtained is not None or
            self.DHCP_Server_List is not None or
            self.IP_Gateway_List is not None or
            self.IP_List is not None or
            self.MAC is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='NetworkInterfaceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkInterfaceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='NetworkInterfaceType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='NetworkInterfaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Adapter is not None:
            self.Adapter.export(lwrite, level, 'SystemObj:', name_='Adapter', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, 'SystemObj:', name_='Description', pretty_print=pretty_print)
        if self.DHCP_Lease_Expires is not None:
            self.DHCP_Lease_Expires.export(lwrite, level, 'SystemObj:', name_='DHCP_Lease_Expires', pretty_print=pretty_print)
        if self.DHCP_Lease_Obtained is not None:
            self.DHCP_Lease_Obtained.export(lwrite, level, 'SystemObj:', name_='DHCP_Lease_Obtained', pretty_print=pretty_print)
        if self.DHCP_Server_List is not None:
            self.DHCP_Server_List.export(lwrite, level, 'SystemObj:', name_='DHCP_Server_List', pretty_print=pretty_print)
        if self.IP_Gateway_List is not None:
            self.IP_Gateway_List.export(lwrite, level, 'SystemObj:', name_='IP_Gateway_List', pretty_print=pretty_print)
        if self.IP_List is not None:
            self.IP_List.export(lwrite, level, 'SystemObj:', name_='IP_List', pretty_print=pretty_print)
        if self.MAC is not None:
            self.MAC.export(lwrite, level, 'SystemObj:', name_='MAC', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Adapter':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Adapter(obj_)
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'DHCP_Lease_Expires':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_DHCP_Lease_Expires(obj_)
        elif nodeName_ == 'DHCP_Lease_Obtained':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_DHCP_Lease_Obtained(obj_)
        elif nodeName_ == 'DHCP_Server_List':
            obj_ = DHCPServerListType.factory()
            obj_.build(child_)
            self.set_DHCP_Server_List(obj_)
        elif nodeName_ == 'IP_Gateway_List':
            obj_ = IPGatewayListType.factory()
            obj_.build(child_)
            self.set_IP_Gateway_List(obj_)
        elif nodeName_ == 'IP_List':
            obj_ = IPInfoListType.factory()
            obj_.build(child_)
            self.set_IP_List(obj_)
        elif nodeName_ == 'MAC':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_MAC(obj_)
# end class NetworkInterfaceType

class IPInfoListType(GeneratedsSuper):
    """The IPInfoListType type specifies a list of IP address/subnet mask
    pairs associated with a network interface."""

    subclass = None
    superclass = None
    def __init__(self, IP_Info=None):
        if IP_Info is None:
            self.IP_Info = []
        else:
            self.IP_Info = IP_Info
    def factory(*args_, **kwargs_):
        if IPInfoListType.subclass:
            return IPInfoListType.subclass(*args_, **kwargs_)
        else:
            return IPInfoListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Info(self): return self.IP_Info
    def set_IP_Info(self, IP_Info): self.IP_Info = IP_Info
    def add_IP_Info(self, value): self.IP_Info.append(value)
    def insert_IP_Info(self, index, value): self.IP_Info[index] = value
    def hasContent_(self):
        if (
            self.IP_Info
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='IPInfoListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPInfoListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='IPInfoListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='IPInfoListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for IP_Info_ in self.IP_Info:
            IP_Info_.export(lwrite, level, 'SystemObj:', name_='IP_Info', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IP_Info':
            obj_ = IPInfoType.factory()
            obj_.build(child_)
            self.IP_Info.append(obj_)
# end class IPInfoListType

class IPInfoType(GeneratedsSuper):
    """The IP_Info type specifies information about the IP address and its
    associated subnet mask used by a network interface."""

    subclass = None
    superclass = None
    def __init__(self, IP_Address=None, Subnet_Mask=None):
        self.IP_Address = IP_Address
        self.Subnet_Mask = Subnet_Mask
    def factory(*args_, **kwargs_):
        if IPInfoType.subclass:
            return IPInfoType.subclass(*args_, **kwargs_)
        else:
            return IPInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def get_Subnet_Mask(self): return self.Subnet_Mask
    def set_Subnet_Mask(self, Subnet_Mask): self.Subnet_Mask = Subnet_Mask
    def hasContent_(self):
        if (
            self.IP_Address is not None or
            self.Subnet_Mask is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='IPInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='IPInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='IPInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_Address is not None:
            self.IP_Address.export(lwrite, level, 'SystemObj:', name_='IP_Address', pretty_print=pretty_print)
        if self.Subnet_Mask is not None:
            self.Subnet_Mask.export(lwrite, level, 'SystemObj:', name_='Subnet_Mask', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IP_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
        elif nodeName_ == 'Subnet_Mask':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Subnet_Mask(obj_)
# end class IPInfoType

class DHCPServerListType(GeneratedsSuper):
    """The DHCPServerListType type specifies a list of DHCP Servers, via
    their IP addresses."""

    subclass = None
    superclass = None
    def __init__(self, DHCP_Server_Address=None):
        if DHCP_Server_Address is None:
            self.DHCP_Server_Address = []
        else:
            self.DHCP_Server_Address = DHCP_Server_Address
    def factory(*args_, **kwargs_):
        if DHCPServerListType.subclass:
            return DHCPServerListType.subclass(*args_, **kwargs_)
        else:
            return DHCPServerListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_DHCP_Server_Address(self): return self.DHCP_Server_Address
    def set_DHCP_Server_Address(self, DHCP_Server_Address): self.DHCP_Server_Address = DHCP_Server_Address
    def add_DHCP_Server_Address(self, value): self.DHCP_Server_Address.append(value)
    def insert_DHCP_Server_Address(self, index, value): self.DHCP_Server_Address[index] = value
    def hasContent_(self):
        if (
            self.DHCP_Server_Address
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='DHCPServerListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DHCPServerListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='DHCPServerListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='DHCPServerListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for DHCP_Server_Address_ in self.DHCP_Server_Address:
            DHCP_Server_Address_.export(lwrite, level, 'SystemObj:', name_='DHCP_Server_Address', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'DHCP_Server_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.DHCP_Server_Address.append(obj_)
# end class DHCPServerListType

class BitnessType(cybox_common.BaseObjectPropertyType):
    """BitnessType specifies CPU architecture bitness, via a union of the
    BitnessEnum type and the atomic xs:string type. Its base type is
    the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(BitnessType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if BitnessType.subclass:
            return BitnessType.subclass(*args_, **kwargs_)
        else:
            return BitnessType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(BitnessType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='BitnessType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BitnessType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='BitnessType'):
        super(BitnessType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='BitnessType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='BitnessType', fromsubclass_=False, pretty_print=True):
        super(BitnessType, self).exportChildren(lwrite, level, 'SystemObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(BitnessType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BitnessType

class ProcessorArchType(cybox_common.BaseObjectPropertyType):
    """ProcessorArchType specifies CPU architecture types, via a union of
    the ProcessorArchEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ProcessorArchType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ProcessorArchType.subclass:
            return ProcessorArchType.subclass(*args_, **kwargs_)
        else:
            return ProcessorArchType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ProcessorArchType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='ProcessorArchType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessorArchType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='ProcessorArchType'):
        super(ProcessorArchType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessorArchType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='ProcessorArchType', fromsubclass_=False, pretty_print=True):
        super(ProcessorArchType, self).exportChildren(lwrite, level, 'SystemObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(ProcessorArchType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ProcessorArchType

class OSType(cybox_common.PlatformSpecificationType):
    """The OSType type specifies information about an operating system. It
    imports and extends the cybox_common.PlatformSpecificationType from the CybOX
    Common Types."""

    subclass = None
    superclass = cybox_common.PlatformSpecificationType
    def __init__(self, Description=None, Identifier=None, Bitness=None, Build_Number=None, Environment_Variable_List=None, Install_Date=None, Patch_Level=None, Platform=None):
        super(OSType, self).__init__(Description, Identifier, )
        self.Bitness = Bitness
        self.Build_Number = Build_Number
        self.Environment_Variable_List = Environment_Variable_List
        self.Install_Date = Install_Date
        self.Patch_Level = Patch_Level
        self.Platform = Platform
    def factory(*args_, **kwargs_):
        if OSType.subclass:
            return OSType.subclass(*args_, **kwargs_)
        else:
            return OSType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Bitness(self): return self.Bitness
    def set_Bitness(self, Bitness): self.Bitness = Bitness
    def validate_BitnessType(self, value):
        # Validate type BitnessType, a restriction on None.
        pass
    def get_Build_Number(self): return self.Build_Number
    def set_Build_Number(self, Build_Number): self.Build_Number = Build_Number
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Environment_Variable_List(self): return self.Environment_Variable_List
    def set_Environment_Variable_List(self, Environment_Variable_List): self.Environment_Variable_List = Environment_Variable_List
    def get_Install_Date(self): return self.Install_Date
    def set_Install_Date(self, Install_Date): self.Install_Date = Install_Date
    def validate_DateObjectPropertyType(self, value):
        # Validate type cybox_common.DateObjectPropertyType, a restriction on None.
        pass
    def get_Patch_Level(self): return self.Patch_Level
    def set_Patch_Level(self, Patch_Level): self.Patch_Level = Patch_Level
    def get_Platform(self): return self.Platform
    def set_Platform(self, Platform): self.Platform = Platform
    def hasContent_(self):
        if (
            self.Bitness is not None or
            self.Build_Number is not None or
            self.Environment_Variable_List is not None or
            self.Install_Date is not None or
            self.Patch_Level is not None or
            self.Platform is not None or
            super(OSType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='OSType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OSType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='OSType'):
        super(OSType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='OSType')
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='OSType', fromsubclass_=False, pretty_print=True):
        super(OSType, self).exportChildren(lwrite, level, 'SystemObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Bitness is not None:
            self.Bitness.export(lwrite, level, 'SystemObj:', name_='Bitness', pretty_print=pretty_print)
        if self.Build_Number is not None:
            self.Build_Number.export(lwrite, level, 'SystemObj:', name_='Build_Number', pretty_print=pretty_print)
        if self.Environment_Variable_List is not None:
            self.Environment_Variable_List.export(lwrite, level, 'SystemObj:', name_='Environment_Variable_List', pretty_print=pretty_print)
        if self.Install_Date is not None:
            self.Install_Date.export(lwrite, level, 'SystemObj:', name_='Install_Date', pretty_print=pretty_print)
        if self.Patch_Level is not None:
            self.Patch_Level.export(lwrite, level, 'SystemObj:', name_='Patch_Level', pretty_print=pretty_print)
        if self.Platform is not None:
            self.Platform.export(lwrite, level, 'SystemObj:', name_='Platform', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(OSType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Bitness':
            obj_ = BitnessType.factory()
            obj_.build(child_)
            self.set_Bitness(obj_)
        elif nodeName_ == 'Build_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Build_Number(obj_)
        elif nodeName_ == 'Environment_Variable_List':
            obj_ = cybox_common.EnvironmentVariableListType.factory()
            obj_.build(child_)
            self.set_Environment_Variable_List(obj_)
        elif nodeName_ == 'Install_Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Install_Date(obj_)
        elif nodeName_ == 'Patch_Level':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Patch_Level(obj_)
        elif nodeName_ == 'Platform':
            obj_ = cybox_common.PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Platform(obj_)
        super(OSType, self).buildChildren(child_, node, nodeName_, True)
# end class OSType

class SystemObjectType(cybox_common.ObjectPropertiesType):
    """The SystemObjectType type is intended to characterize computer
    systems (as a combination of both software and hardware)."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Available_Physical_Memory=None, BIOS_Info=None, Date=None, Hostname=None, Local_Time=None, Network_Interface_List=None, OS=None, Processor=None, Processor_Architecture=None, System_Time=None, Timezone_DST=None, Timezone_Standard=None, Total_Physical_Memory=None, Uptime=None, Username=None):
        super(SystemObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Available_Physical_Memory = Available_Physical_Memory
        self.BIOS_Info = BIOS_Info
        self.Date = Date
        self.Hostname = Hostname
        self.Local_Time = Local_Time
        self.Network_Interface_List = Network_Interface_List
        self.OS = OS
        self.Processor = Processor
        self.Processor_Architecture = Processor_Architecture
        self.System_Time = System_Time
        self.Timezone_DST = Timezone_DST
        self.Timezone_Standard = Timezone_Standard
        self.Total_Physical_Memory = Total_Physical_Memory
        self.Uptime = Uptime
        self.Username = Username
    def factory(*args_, **kwargs_):
        if SystemObjectType.subclass:
            return SystemObjectType.subclass(*args_, **kwargs_)
        else:
            return SystemObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Available_Physical_Memory(self): return self.Available_Physical_Memory
    def set_Available_Physical_Memory(self, Available_Physical_Memory): self.Available_Physical_Memory = Available_Physical_Memory
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_BIOS_Info(self): return self.BIOS_Info
    def set_BIOS_Info(self, BIOS_Info): self.BIOS_Info = BIOS_Info
    def get_Date(self): return self.Date
    def set_Date(self, Date): self.Date = Date
    def validate_DateObjectPropertyType(self, value):
        # Validate type cybox_common.DateObjectPropertyType, a restriction on None.
        pass
    def get_Hostname(self): return self.Hostname
    def set_Hostname(self, Hostname): self.Hostname = Hostname
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Local_Time(self): return self.Local_Time
    def set_Local_Time(self, Local_Time): self.Local_Time = Local_Time
    def validate_TimeObjectPropertyType(self, value):
        # Validate type cybox_common.TimeObjectPropertyType, a restriction on None.
        pass
    def get_Network_Interface_List(self): return self.Network_Interface_List
    def set_Network_Interface_List(self, Network_Interface_List): self.Network_Interface_List = Network_Interface_List
    def get_OS(self): return self.OS
    def set_OS(self, OS): self.OS = OS
    def get_Processor(self): return self.Processor
    def set_Processor(self, Processor): self.Processor = Processor
    def get_Processor_Architecture(self): return self.Processor_Architecture
    def set_Processor_Architecture(self, Processor_Architecture): self.Processor_Architecture = Processor_Architecture
    def validate_ProcessorArchType(self, value):
        # Validate type ProcessorArchType, a restriction on None.
        pass
    def get_System_Time(self): return self.System_Time
    def set_System_Time(self, System_Time): self.System_Time = System_Time
    def get_Timezone_DST(self): return self.Timezone_DST
    def set_Timezone_DST(self, Timezone_DST): self.Timezone_DST = Timezone_DST
    def get_Timezone_Standard(self): return self.Timezone_Standard
    def set_Timezone_Standard(self, Timezone_Standard): self.Timezone_Standard = Timezone_Standard
    def get_Total_Physical_Memory(self): return self.Total_Physical_Memory
    def set_Total_Physical_Memory(self, Total_Physical_Memory): self.Total_Physical_Memory = Total_Physical_Memory
    def get_Uptime(self): return self.Uptime
    def set_Uptime(self, Uptime): self.Uptime = Uptime
    def validate_DurationObjectPropertyType(self, value):
        # Validate type cybox_common.DurationObjectPropertyType, a restriction on None.
        pass
    def get_Username(self): return self.Username
    def set_Username(self, Username): self.Username = Username
    def hasContent_(self):
        if (
            self.Available_Physical_Memory is not None or
            self.BIOS_Info is not None or
            self.Date is not None or
            self.Hostname is not None or
            self.Local_Time is not None or
            self.Network_Interface_List is not None or
            self.OS is not None or
            self.Processor is not None or
            self.Processor_Architecture is not None or
            self.System_Time is not None or
            self.Timezone_DST is not None or
            self.Timezone_Standard is not None or
            self.Total_Physical_Memory is not None or
            self.Uptime is not None or
            self.Username is not None or
            super(SystemObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='SystemObj:', name_='SystemObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SystemObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='SystemObj:', name_='SystemObjectType'):
        super(SystemObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SystemObjectType')
    def exportChildren(self, lwrite, level, namespace_='SystemObj:', name_='SystemObjectType', fromsubclass_=False, pretty_print=True):
        super(SystemObjectType, self).exportChildren(lwrite, level, 'SystemObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Available_Physical_Memory is not None:
            self.Available_Physical_Memory.export(lwrite, level, 'SystemObj:', name_='Available_Physical_Memory', pretty_print=pretty_print)
        if self.BIOS_Info is not None:
            self.BIOS_Info.export(lwrite, level, 'SystemObj:', name_='BIOS_Info', pretty_print=pretty_print)
        if self.Date is not None:
            self.Date.export(lwrite, level, 'SystemObj:', name_='Date', pretty_print=pretty_print)
        if self.Hostname is not None:
            self.Hostname.export(lwrite, level, 'SystemObj:', name_='Hostname', pretty_print=pretty_print)
        if self.Local_Time is not None:
            self.Local_Time.export(lwrite, level, 'SystemObj:', name_='Local_Time', pretty_print=pretty_print)
        if self.Network_Interface_List is not None:
            self.Network_Interface_List.export(lwrite, level, 'SystemObj:', name_='Network_Interface_List', pretty_print=pretty_print)
        if self.OS is not None:
            self.OS.export(lwrite, level, 'SystemObj:', name_='OS', pretty_print=pretty_print)
        if self.Processor is not None:
            self.Processor.export(lwrite, level, 'SystemObj:', name_='Processor', pretty_print=pretty_print)
        if self.Processor_Architecture is not None:
            self.Processor_Architecture.export(lwrite, level, 'SystemObj:', name_='Processor_Architecture', pretty_print=pretty_print)
        if self.System_Time is not None:
            self.System_Time.export(lwrite, level, 'SystemObj:', name_='System_Time', pretty_print=pretty_print)
        if self.Timezone_DST is not None:
            self.Timezone_DST.export(lwrite, level, 'SystemObj:', name_='Timezone_DST', pretty_print=pretty_print)
        if self.Timezone_Standard is not None:
            self.Timezone_Standard.export(lwrite, level, 'SystemObj:', name_='Timezone_Standard', pretty_print=pretty_print)
        if self.Total_Physical_Memory is not None:
            self.Total_Physical_Memory.export(lwrite, level, 'SystemObj:', name_='Total_Physical_Memory', pretty_print=pretty_print)
        if self.Uptime is not None:
            self.Uptime.export(lwrite, level, 'SystemObj:', name_='Uptime', pretty_print=pretty_print)
        if self.Username is not None:
            self.Username.export(lwrite, level, 'SystemObj:', name_='Username', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(SystemObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Available_Physical_Memory':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Available_Physical_Memory(obj_)
        elif nodeName_ == 'BIOS_Info':
            obj_ = BIOSInfoType.factory()
            obj_.build(child_)
            self.set_BIOS_Info(obj_)
        elif nodeName_ == 'Date':
            obj_ = cybox_common.DateObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Date(obj_)
        elif nodeName_ == 'Hostname':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hostname(obj_)
        elif nodeName_ == 'Local_Time':
            obj_ = cybox_common.TimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Local_Time(obj_)
        elif nodeName_ == 'Network_Interface_List':
            obj_ = NetworkInterfaceListType.factory()
            obj_.build(child_)
            self.set_Network_Interface_List(obj_)
        elif nodeName_ == 'OS':
            obj_ = OSType.factory()
            obj_.build(child_)
            self.set_OS(obj_)
        elif nodeName_ == 'Processor':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Processor(obj_)
        elif nodeName_ == 'Processor_Architecture':
            obj_ = ProcessorArchType.factory()
            obj_.build(child_)
            self.set_Processor_Architecture(obj_)
        elif nodeName_ == 'System_Time':
            obj_ = cybox_common.TimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_System_Time(obj_)
        elif nodeName_ == 'Timezone_DST':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Timezone_DST(obj_)
        elif nodeName_ == 'Timezone_Standard':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Timezone_Standard(obj_)
        elif nodeName_ == 'Total_Physical_Memory':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Total_Physical_Memory(obj_)
        elif nodeName_ == 'Uptime':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Uptime(obj_)
        elif nodeName_ == 'Username':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Username(obj_)
        super(SystemObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class SystemObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'DHCP_Lease_Expires': cybox_common.DateTimeObjectPropertyType,
    'Time': cybox_common.TimeType,
    'DHCP_Server_Address': address_object.AddressObjectType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'IP_Gateway_Address': address_object.AddressObjectType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'MAC': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'IP_Address': address_object.AddressObjectType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Subnet_Mask': address_object.AddressObjectType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'BIOS_Manufacturer': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Available_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Uptime': cybox_common.DurationObjectPropertyType,
    'Hostname': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'BIOS_Version': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'System_Time': cybox_common.TimeObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Build_Number': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Patch_Level': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Install_Date': cybox_common.DateObjectPropertyType,
    'Total_Physical_Memory': cybox_common.UnsignedLongObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'DHCP_Lease_Obtained': cybox_common.DateTimeObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Timezone_DST': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'BIOS_Date': cybox_common.DateObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Timezone_Standard': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'BIOS_Serial_Number': cybox_common.StringObjectPropertyType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Local_Time': cybox_common.TimeObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Adapter': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Processor': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'BIOS_Release_Date': cybox_common.DateObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Tool': cybox_common.ToolInformationType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'System'
        rootClass = SystemObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'System'
        rootClass = SystemObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'System'
        rootClass = SystemObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="System",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "SystemObjectType",
    "BIOSInfoType",
    "NetworkInterfaceListType",
    "IPGatewayListType",
    "NetworkInterfaceType",
    "IPInfoListType",
    "IPInfoType",
    "DHCPServerListType",
    "OSType",
    "ProcessorArchType",
    "BitnessType"
    ]
