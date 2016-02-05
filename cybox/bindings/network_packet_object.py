# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object
from . import port_object


class LinkLayerType(GeneratedsSuper):
    """A link layer protocol is a hardware interface protocol, such as
    Ethernet, or a logical link routing protocol, such as ARP."""

    subclass = None
    superclass = None
    def __init__(self, Physical_Interface=None, Logical_Protocols=None):
        self.Physical_Interface = Physical_Interface
        self.Logical_Protocols = Logical_Protocols
    def factory(*args_, **kwargs_):
        if LinkLayerType.subclass:
            return LinkLayerType.subclass(*args_, **kwargs_)
        else:
            return LinkLayerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Physical_Interface(self): return self.Physical_Interface
    def set_Physical_Interface(self, Physical_Interface): self.Physical_Interface = Physical_Interface
    def get_Logical_Protocols(self): return self.Logical_Protocols
    def set_Logical_Protocols(self, Logical_Protocols): self.Logical_Protocols = Logical_Protocols
    def hasContent_(self):
        if (
            self.Physical_Interface is not None or
            self.Logical_Protocols is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='LinkLayerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LinkLayerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='LinkLayerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='LinkLayerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Physical_Interface is not None:
            self.Physical_Interface.export(lwrite, level, 'PacketObj:', name_='Physical_Interface', pretty_print=pretty_print)
        if self.Logical_Protocols is not None:
            self.Logical_Protocols.export(lwrite, level, 'PacketObj:', name_='Logical_Protocols', pretty_print=pretty_print)
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
        if nodeName_ == 'Physical_Interface':
            obj_ = PhysicalInterfaceType.factory()
            obj_.build(child_)
            self.set_Physical_Interface(obj_)
        elif nodeName_ == 'Logical_Protocols':
            obj_ = LogicalProtocolType.factory()
            obj_.build(child_)
            self.set_Logical_Protocols(obj_)
# end class LinkLayerType

class PhysicalInterfaceType(GeneratedsSuper):
    """Multiple interface types exist - only most common (Ethernet)
    included now. Others will be added later as needed."""

    subclass = None
    superclass = None
    def __init__(self, Ethernet=None):
        self.Ethernet = Ethernet
    def factory(*args_, **kwargs_):
        if PhysicalInterfaceType.subclass:
            return PhysicalInterfaceType.subclass(*args_, **kwargs_)
        else:
            return PhysicalInterfaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Ethernet(self): return self.Ethernet
    def set_Ethernet(self, Ethernet): self.Ethernet = Ethernet
    def hasContent_(self):
        if (
            self.Ethernet is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='PhysicalInterfaceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PhysicalInterfaceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='PhysicalInterfaceType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='PhysicalInterfaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Ethernet is not None:
            self.Ethernet.export(lwrite, level, 'PacketObj:', name_='Ethernet', pretty_print=pretty_print)
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
        if nodeName_ == 'Ethernet':
            obj_ = EthernetInterfaceType.factory()
            obj_.build(child_)
            self.set_Ethernet(obj_)
# end class PhysicalInterfaceType

class LogicalProtocolType(GeneratedsSuper):
    """Logical Protocols characterizes the logical protocol of a link layer
    connection. One example of a logical protocol is ARP."""

    subclass = None
    superclass = None
    def __init__(self, ARP_RARP=None, NDP=None):
        self.ARP_RARP = ARP_RARP
        self.NDP = NDP
    def factory(*args_, **kwargs_):
        if LogicalProtocolType.subclass:
            return LogicalProtocolType.subclass(*args_, **kwargs_)
        else:
            return LogicalProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ARP_RARP(self): return self.ARP_RARP
    def set_ARP_RARP(self, ARP_RARP): self.ARP_RARP = ARP_RARP
    def get_NDP(self): return self.NDP
    def set_NDP(self, NDP): self.NDP = NDP
    def hasContent_(self):
        if (
            self.ARP_RARP is not None or
            self.NDP is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='LogicalProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LogicalProtocolType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='LogicalProtocolType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='LogicalProtocolType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ARP_RARP is not None:
            self.ARP_RARP.export(lwrite, level, 'PacketObj:', name_='ARP_RARP', pretty_print=pretty_print)
        if self.NDP is not None:
            self.NDP.export(lwrite, level, 'PacketObj:', name_='NDP', pretty_print=pretty_print)
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
        if nodeName_ == 'ARP_RARP':
            obj_ = ARPType.factory()
            obj_.build(child_)
            self.set_ARP_RARP(obj_)
        elif nodeName_ == 'NDP':
            obj_ = NDPType.factory()
            obj_.build(child_)
            self.set_NDP(obj_)
# end class LogicalProtocolType

class EthernetInterfaceType(GeneratedsSuper):
    """Ethernet sends network packets from the sending host to one or more
    receiving hosts. (REF: IEEE 802.3;
    http://wiki.wireshark.org/Ethernet)"""

    subclass = None
    superclass = None
    def __init__(self, Ethernet_Header=None):
        self.Ethernet_Header = Ethernet_Header
    def factory(*args_, **kwargs_):
        if EthernetInterfaceType.subclass:
            return EthernetInterfaceType.subclass(*args_, **kwargs_)
        else:
            return EthernetInterfaceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Ethernet_Header(self): return self.Ethernet_Header
    def set_Ethernet_Header(self, Ethernet_Header): self.Ethernet_Header = Ethernet_Header
    def hasContent_(self):
        if (
            self.Ethernet_Header is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='EthernetInterfaceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EthernetInterfaceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='EthernetInterfaceType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='EthernetInterfaceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Ethernet_Header is not None:
            self.Ethernet_Header.export(lwrite, level, 'PacketObj:', name_='Ethernet_Header', pretty_print=pretty_print)
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
        if nodeName_ == 'Ethernet_Header':
            obj_ = EthernetHeaderType.factory()
            obj_.build(child_)
            self.set_Ethernet_Header(obj_)
# end class EthernetInterfaceType

class EthernetHeaderType(GeneratedsSuper):
    """Ethernet header characterizes and ethernet header and includes
    information such as source MAC address, destination MAC address,
    and more."""

    subclass = None
    superclass = None
    def __init__(self, Destination_MAC_Addr=None, Source_MAC_Addr=None, Type_Or_Length=None, Checksum=None):
        self.Destination_MAC_Addr = Destination_MAC_Addr
        self.Source_MAC_Addr = Source_MAC_Addr
        self.Type_Or_Length = Type_Or_Length
        self.Checksum = Checksum
    def factory(*args_, **kwargs_):
        if EthernetHeaderType.subclass:
            return EthernetHeaderType.subclass(*args_, **kwargs_)
        else:
            return EthernetHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Destination_MAC_Addr(self): return self.Destination_MAC_Addr
    def set_Destination_MAC_Addr(self, Destination_MAC_Addr): self.Destination_MAC_Addr = Destination_MAC_Addr
    def get_Source_MAC_Addr(self): return self.Source_MAC_Addr
    def set_Source_MAC_Addr(self, Source_MAC_Addr): self.Source_MAC_Addr = Source_MAC_Addr
    def get_Type_Or_Length(self): return self.Type_Or_Length
    def set_Type_Or_Length(self, Type_Or_Length): self.Type_Or_Length = Type_Or_Length
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Destination_MAC_Addr is not None or
            self.Source_MAC_Addr is not None or
            self.Type_Or_Length is not None or
            self.Checksum is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='EthernetHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EthernetHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='EthernetHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='EthernetHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Destination_MAC_Addr is not None:
            self.Destination_MAC_Addr.export(lwrite, level, 'PacketObj:', name_='Destination_MAC_Addr', pretty_print=pretty_print)
        if self.Source_MAC_Addr is not None:
            self.Source_MAC_Addr.export(lwrite, level, 'PacketObj:', name_='Source_MAC_Addr', pretty_print=pretty_print)
        if self.Type_Or_Length is not None:
            self.Type_Or_Length.export(lwrite, level, 'PacketObj:', name_='Type_Or_Length', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
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
        if nodeName_ == 'Destination_MAC_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Destination_MAC_Addr(obj_)
        elif nodeName_ == 'Source_MAC_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Source_MAC_Addr(obj_)
        elif nodeName_ == 'Type_Or_Length':
            obj_ = TypeLengthType.factory()
            obj_.build(child_)
            self.set_Type_Or_Length(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
# end class EthernetHeaderType

class TypeLengthType(GeneratedsSuper):
    """0-1500 then it is a length field. Otherwise, it defines the protocol
    type of the Internet layer."""

    subclass = None
    superclass = None
    def __init__(self, Length=None, Internet_Layer_Type=None):
        self.Length = Length
        self.Internet_Layer_Type = Internet_Layer_Type
    def factory(*args_, **kwargs_):
        if TypeLengthType.subclass:
            return TypeLengthType.subclass(*args_, **kwargs_)
        else:
            return TypeLengthType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Internet_Layer_Type(self): return self.Internet_Layer_Type
    def set_Internet_Layer_Type(self, Internet_Layer_Type): self.Internet_Layer_Type = Internet_Layer_Type
    def validate_IANAEtherType(self, value):
        # Validate type IANAEtherType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Length is not None or
            self.Internet_Layer_Type is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='TypeLengthType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TypeLengthType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='TypeLengthType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='TypeLengthType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.Internet_Layer_Type is not None:
            self.Internet_Layer_Type.export(lwrite, level, 'PacketObj:', name_='Internet_Layer_Type', pretty_print=pretty_print)
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
        if nodeName_ == 'Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Internet_Layer_Type':
            obj_ = IANAEtherType.factory()
            obj_.build(child_)
            self.set_Internet_Layer_Type(obj_)
# end class TypeLengthType

class ARPType(GeneratedsSuper):
    """The Address Resolution Protocol is a request and reply protocol that
    runs encapsulated by the line protocol. It is communicated
    within the boundaries of a single network, never routed across
    internetwork nodes. This property places ARP into the Link
    Layer. It is encapsulated. REF: http://www.comptechdoc.org/indep
    endent/networking/guide/netarp.html"""

    subclass = None
    superclass = None
    def __init__(self, Hardware_Addr_Type=None, Proto_Addr_Type=None, Hardware_Addr_Size=None, Proto_Addr_Size=None, Op_Type=None, Sender_Hardware_Addr=None, Sender_Protocol_Addr=None, Recip_Hardware_Addr=None, Recip_Protocol_Addr=None):
        self.Hardware_Addr_Type = Hardware_Addr_Type
        self.Proto_Addr_Type = Proto_Addr_Type
        self.Hardware_Addr_Size = Hardware_Addr_Size
        self.Proto_Addr_Size = Proto_Addr_Size
        self.Op_Type = Op_Type
        self.Sender_Hardware_Addr = Sender_Hardware_Addr
        self.Sender_Protocol_Addr = Sender_Protocol_Addr
        self.Recip_Hardware_Addr = Recip_Hardware_Addr
        self.Recip_Protocol_Addr = Recip_Protocol_Addr
    def factory(*args_, **kwargs_):
        if ARPType.subclass:
            return ARPType.subclass(*args_, **kwargs_)
        else:
            return ARPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hardware_Addr_Type(self): return self.Hardware_Addr_Type
    def set_Hardware_Addr_Type(self, Hardware_Addr_Type): self.Hardware_Addr_Type = Hardware_Addr_Type
    def validate_IANAHardwareType(self, value):
        # Validate type IANAHardwareType, a restriction on None.
        pass
    def get_Proto_Addr_Type(self): return self.Proto_Addr_Type
    def set_Proto_Addr_Type(self, Proto_Addr_Type): self.Proto_Addr_Type = Proto_Addr_Type
    def validate_IANAEtherType(self, value):
        # Validate type IANAEtherType, a restriction on None.
        pass
    def get_Hardware_Addr_Size(self): return self.Hardware_Addr_Size
    def set_Hardware_Addr_Size(self, Hardware_Addr_Size): self.Hardware_Addr_Size = Hardware_Addr_Size
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Proto_Addr_Size(self): return self.Proto_Addr_Size
    def set_Proto_Addr_Size(self, Proto_Addr_Size): self.Proto_Addr_Size = Proto_Addr_Size
    def get_Op_Type(self): return self.Op_Type
    def set_Op_Type(self, Op_Type): self.Op_Type = Op_Type
    def validate_ARPOpType(self, value):
        # Validate type ARPOpType, a restriction on None.
        pass
    def get_Sender_Hardware_Addr(self): return self.Sender_Hardware_Addr
    def set_Sender_Hardware_Addr(self, Sender_Hardware_Addr): self.Sender_Hardware_Addr = Sender_Hardware_Addr
    def get_Sender_Protocol_Addr(self): return self.Sender_Protocol_Addr
    def set_Sender_Protocol_Addr(self, Sender_Protocol_Addr): self.Sender_Protocol_Addr = Sender_Protocol_Addr
    def get_Recip_Hardware_Addr(self): return self.Recip_Hardware_Addr
    def set_Recip_Hardware_Addr(self, Recip_Hardware_Addr): self.Recip_Hardware_Addr = Recip_Hardware_Addr
    def get_Recip_Protocol_Addr(self): return self.Recip_Protocol_Addr
    def set_Recip_Protocol_Addr(self, Recip_Protocol_Addr): self.Recip_Protocol_Addr = Recip_Protocol_Addr
    def hasContent_(self):
        if (
            self.Hardware_Addr_Type is not None or
            self.Proto_Addr_Type is not None or
            self.Hardware_Addr_Size is not None or
            self.Proto_Addr_Size is not None or
            self.Op_Type is not None or
            self.Sender_Hardware_Addr is not None or
            self.Sender_Protocol_Addr is not None or
            self.Recip_Hardware_Addr is not None or
            self.Recip_Protocol_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ARPType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ARPType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ARPType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hardware_Addr_Type is not None:
            self.Hardware_Addr_Type.export(lwrite, level, 'PacketObj:', name_='Hardware_Addr_Type', pretty_print=pretty_print)
        if self.Proto_Addr_Type is not None:
            self.Proto_Addr_Type.export(lwrite, level, 'PacketObj:', name_='Proto_Addr_Type', pretty_print=pretty_print)
        if self.Hardware_Addr_Size is not None:
            self.Hardware_Addr_Size.export(lwrite, level, 'PacketObj:', name_='Hardware_Addr_Size', pretty_print=pretty_print)
        if self.Proto_Addr_Size is not None:
            self.Proto_Addr_Size.export(lwrite, level, 'PacketObj:', name_='Proto_Addr_Size', pretty_print=pretty_print)
        if self.Op_Type is not None:
            self.Op_Type.export(lwrite, level, 'PacketObj:', name_='Op_Type', pretty_print=pretty_print)
        if self.Sender_Hardware_Addr is not None:
            self.Sender_Hardware_Addr.export(lwrite, level, 'PacketObj:', name_='Sender_Hardware_Addr', pretty_print=pretty_print)
        if self.Sender_Protocol_Addr is not None:
            self.Sender_Protocol_Addr.export(lwrite, level, 'PacketObj:', name_='Sender_Protocol_Addr', pretty_print=pretty_print)
        if self.Recip_Hardware_Addr is not None:
            self.Recip_Hardware_Addr.export(lwrite, level, 'PacketObj:', name_='Recip_Hardware_Addr', pretty_print=pretty_print)
        if self.Recip_Protocol_Addr is not None:
            self.Recip_Protocol_Addr.export(lwrite, level, 'PacketObj:', name_='Recip_Protocol_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'Hardware_Addr_Type':
            obj_ = IANAHardwareType.factory()
            obj_.build(child_)
            self.set_Hardware_Addr_Type(obj_)
        elif nodeName_ == 'Proto_Addr_Type':
            obj_ = IANAEtherType.factory()
            obj_.build(child_)
            self.set_Proto_Addr_Type(obj_)
        elif nodeName_ == 'Hardware_Addr_Size':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hardware_Addr_Size(obj_)
        elif nodeName_ == 'Proto_Addr_Size':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Proto_Addr_Size(obj_)
        elif nodeName_ == 'Op_Type':
            obj_ = ARPOpType.factory()
            obj_.build(child_)
            self.set_Op_Type(obj_)
        elif nodeName_ == 'Sender_Hardware_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Sender_Hardware_Addr(obj_)
        elif nodeName_ == 'Sender_Protocol_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Sender_Protocol_Addr(obj_)
        elif nodeName_ == 'Recip_Hardware_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Recip_Hardware_Addr(obj_)
        elif nodeName_ == 'Recip_Protocol_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Recip_Protocol_Addr(obj_)
# end class ARPType

class NDPType(GeneratedsSuper):
    """NDP Type characterizes NDP (Neighbor Discover Protocol) IPv6
    packets. NDP defines five ICMPv6 packet types. RFC 2461:
    http://tools.ietf.org/html/rfc4861"""

    subclass = None
    superclass = None
    def __init__(self, ICMPv6_Header=None, Router_Solicitation=None, Router_Advertisement=None, Neighbor_Solicitation=None, Neighbor_Advertisement=None, Redirect=None):
        self.ICMPv6_Header = ICMPv6_Header
        self.Router_Solicitation = Router_Solicitation
        self.Router_Advertisement = Router_Advertisement
        self.Neighbor_Solicitation = Neighbor_Solicitation
        self.Neighbor_Advertisement = Neighbor_Advertisement
        self.Redirect = Redirect
    def factory(*args_, **kwargs_):
        if NDPType.subclass:
            return NDPType.subclass(*args_, **kwargs_)
        else:
            return NDPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ICMPv6_Header(self): return self.ICMPv6_Header
    def set_ICMPv6_Header(self, ICMPv6_Header): self.ICMPv6_Header = ICMPv6_Header
    def get_Router_Solicitation(self): return self.Router_Solicitation
    def set_Router_Solicitation(self, Router_Solicitation): self.Router_Solicitation = Router_Solicitation
    def get_Router_Advertisement(self): return self.Router_Advertisement
    def set_Router_Advertisement(self, Router_Advertisement): self.Router_Advertisement = Router_Advertisement
    def get_Neighbor_Solicitation(self): return self.Neighbor_Solicitation
    def set_Neighbor_Solicitation(self, Neighbor_Solicitation): self.Neighbor_Solicitation = Neighbor_Solicitation
    def get_Neighbor_Advertisement(self): return self.Neighbor_Advertisement
    def set_Neighbor_Advertisement(self, Neighbor_Advertisement): self.Neighbor_Advertisement = Neighbor_Advertisement
    def get_Redirect(self): return self.Redirect
    def set_Redirect(self, Redirect): self.Redirect = Redirect
    def hasContent_(self):
        if (
            self.ICMPv6_Header is not None or
            self.Router_Solicitation is not None or
            self.Router_Advertisement is not None or
            self.Neighbor_Solicitation is not None or
            self.Neighbor_Advertisement is not None or
            self.Redirect is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NDPType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NDPType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NDPType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NDPType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ICMPv6_Header is not None:
            self.ICMPv6_Header.export(lwrite, level, 'PacketObj:', name_='ICMPv6_Header', pretty_print=pretty_print)
        if self.Router_Solicitation is not None:
            self.Router_Solicitation.export(lwrite, level, 'PacketObj:', name_='Router_Solicitation', pretty_print=pretty_print)
        if self.Router_Advertisement is not None:
            self.Router_Advertisement.export(lwrite, level, 'PacketObj:', name_='Router_Advertisement', pretty_print=pretty_print)
        if self.Neighbor_Solicitation is not None:
            self.Neighbor_Solicitation.export(lwrite, level, 'PacketObj:', name_='Neighbor_Solicitation', pretty_print=pretty_print)
        if self.Neighbor_Advertisement is not None:
            self.Neighbor_Advertisement.export(lwrite, level, 'PacketObj:', name_='Neighbor_Advertisement', pretty_print=pretty_print)
        if self.Redirect is not None:
            self.Redirect.export(lwrite, level, 'PacketObj:', name_='Redirect', pretty_print=pretty_print)
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
        if nodeName_ == 'ICMPv6_Header':
            obj_ = ICMPv6HeaderType.factory()
            obj_.build(child_)
            self.set_ICMPv6_Header(obj_)
        elif nodeName_ == 'Router_Solicitation':
            obj_ = RouterSolicitationType.factory()
            obj_.build(child_)
            self.set_Router_Solicitation(obj_)
        elif nodeName_ == 'Router_Advertisement':
            obj_ = RouterAdvertisementType.factory()
            obj_.build(child_)
            self.set_Router_Advertisement(obj_)
        elif nodeName_ == 'Neighbor_Solicitation':
            obj_ = NeighborSolicitationType.factory()
            obj_.build(child_)
            self.set_Neighbor_Solicitation(obj_)
        elif nodeName_ == 'Neighbor_Advertisement':
            obj_ = NeighborAdvertisementType.factory()
            obj_.build(child_)
            self.set_Neighbor_Advertisement(obj_)
        elif nodeName_ == 'Redirect':
            obj_ = RedirectType.factory()
            obj_.build(child_)
            self.set_Redirect(obj_)
# end class NDPType

class RouterSolicitationType(GeneratedsSuper):
    """Hosts send Router Solicitations in order to prompt routers to
    generate Router Advertisements quickly.(type=133; code=0)"""

    subclass = None
    superclass = None
    def __init__(self, Options=None):
        if Options is None:
            self.Options = []
        else:
            self.Options = Options
    def factory(*args_, **kwargs_):
        if RouterSolicitationType.subclass:
            return RouterSolicitationType.subclass(*args_, **kwargs_)
        else:
            return RouterSolicitationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def add_Options(self, value): self.Options.append(value)
    def insert_Options(self, index, value): self.Options[index] = value
    def hasContent_(self):
        if (
            self.Options
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RouterSolicitationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RouterSolicitationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RouterSolicitationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RouterSolicitationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Options_ in self.Options:
            Options_.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
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
        if nodeName_ == 'Options':
            obj_ = RouterSolicitationOptionsType.factory()
            obj_.build(child_)
            self.Options.append(obj_)
# end class RouterSolicitationType

class RouterSolicitationOptionsType(GeneratedsSuper):
    """Neighbor Discovery messages include zero or more options, some of
    which may appear multiple times in the same message."""

    subclass = None
    superclass = None
    def __init__(self, Src_Link_Addr=None):
        self.Src_Link_Addr = Src_Link_Addr
    def factory(*args_, **kwargs_):
        if RouterSolicitationOptionsType.subclass:
            return RouterSolicitationOptionsType.subclass(*args_, **kwargs_)
        else:
            return RouterSolicitationOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Src_Link_Addr(self): return self.Src_Link_Addr
    def set_Src_Link_Addr(self, Src_Link_Addr): self.Src_Link_Addr = Src_Link_Addr
    def hasContent_(self):
        if (
            self.Src_Link_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RouterSolicitationOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RouterSolicitationOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RouterSolicitationOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RouterSolicitationOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Src_Link_Addr is not None:
            self.Src_Link_Addr.export(lwrite, level, 'PacketObj:', name_='Src_Link_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'Src_Link_Addr':
            obj_ = NDPLinkAddrType.factory()
            obj_.build(child_)
            self.set_Src_Link_Addr(obj_)
# end class RouterSolicitationOptionsType

class RouterAdvertisementType(GeneratedsSuper):
    """Routers send out Router Advertisement messages periodically, or in
    response to Router Solicitations. (type=134; code=0)1-bit
    "Managed address configuration" flag. When set, it indicates
    that addresses are available via Dynamic Host Configuration
    Protocol. If the M flag is set, the O flag is redundant and can
    be ignored because DHCPv6 will return all available
    configuration information.1-bit "Other configuration" flag. When
    set, it indicates that other configuration information is
    available via DHCPv6. Examples of such information are DNS-
    related information or information on other servers within the
    network."""

    subclass = None
    superclass = None
    def __init__(self, other_config_flag=None, managed_address_config_flag=None, Cur_Hop_Limit=None, Router_Lifetime=None, Reachable_Time=None, Retrans_Timer=None, Options=None):
        self.other_config_flag = _cast(bool, other_config_flag)
        self.managed_address_config_flag = _cast(bool, managed_address_config_flag)
        self.Cur_Hop_Limit = Cur_Hop_Limit
        self.Router_Lifetime = Router_Lifetime
        self.Reachable_Time = Reachable_Time
        self.Retrans_Timer = Retrans_Timer
        self.Options = Options
    def factory(*args_, **kwargs_):
        if RouterAdvertisementType.subclass:
            return RouterAdvertisementType.subclass(*args_, **kwargs_)
        else:
            return RouterAdvertisementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Cur_Hop_Limit(self): return self.Cur_Hop_Limit
    def set_Cur_Hop_Limit(self, Cur_Hop_Limit): self.Cur_Hop_Limit = Cur_Hop_Limit
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Router_Lifetime(self): return self.Router_Lifetime
    def set_Router_Lifetime(self, Router_Lifetime): self.Router_Lifetime = Router_Lifetime
    def get_Reachable_Time(self): return self.Reachable_Time
    def set_Reachable_Time(self, Reachable_Time): self.Reachable_Time = Reachable_Time
    def get_Retrans_Timer(self): return self.Retrans_Timer
    def set_Retrans_Timer(self, Retrans_Timer): self.Retrans_Timer = Retrans_Timer
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def get_other_config_flag(self): return self.other_config_flag
    def set_other_config_flag(self, other_config_flag): self.other_config_flag = other_config_flag
    def get_managed_address_config_flag(self): return self.managed_address_config_flag
    def set_managed_address_config_flag(self, managed_address_config_flag): self.managed_address_config_flag = managed_address_config_flag
    def hasContent_(self):
        if (
            self.Cur_Hop_Limit is not None or
            self.Router_Lifetime is not None or
            self.Reachable_Time is not None or
            self.Retrans_Timer is not None or
            self.Options is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RouterAdvertisementType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RouterAdvertisementType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RouterAdvertisementType'):
        if self.other_config_flag is not None:

            lwrite(' other_config_flag="%s"' % self.gds_format_boolean(self.other_config_flag, input_name='other_config_flag'))
        if self.managed_address_config_flag is not None:

            lwrite(' managed_address_config_flag="%s"' % self.gds_format_boolean(self.managed_address_config_flag, input_name='managed_address_config_flag'))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RouterAdvertisementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Cur_Hop_Limit is not None:
            self.Cur_Hop_Limit.export(lwrite, level, 'PacketObj:', name_='Cur_Hop_Limit', pretty_print=pretty_print)
        if self.Router_Lifetime is not None:
            self.Router_Lifetime.export(lwrite, level, 'PacketObj:', name_='Router_Lifetime', pretty_print=pretty_print)
        if self.Reachable_Time is not None:
            self.Reachable_Time.export(lwrite, level, 'PacketObj:', name_='Reachable_Time', pretty_print=pretty_print)
        if self.Retrans_Timer is not None:
            self.Retrans_Timer.export(lwrite, level, 'PacketObj:', name_='Retrans_Timer', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('other_config_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.other_config_flag = True
            elif value in ('false', '0'):
                self.other_config_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('managed_address_config_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.managed_address_config_flag = True
            elif value in ('false', '0'):
                self.managed_address_config_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Cur_Hop_Limit':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Cur_Hop_Limit(obj_)
        elif nodeName_ == 'Router_Lifetime':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Router_Lifetime(obj_)
        elif nodeName_ == 'Reachable_Time':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reachable_Time(obj_)
        elif nodeName_ == 'Retrans_Timer':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Retrans_Timer(obj_)
        elif nodeName_ == 'Options':
            obj_ = RouterAdvertisementOptionsType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
# end class RouterAdvertisementType

class RouterAdvertisementOptionsType(GeneratedsSuper):
    """Router Advertisement messages include zero or more options, some of
    which may appear multiple times in the same message."""

    subclass = None
    superclass = None
    def __init__(self, Src_Link_Addr=None, MTU=None, Prefix_Info=None):
        self.Src_Link_Addr = Src_Link_Addr
        self.MTU = MTU
        self.Prefix_Info = Prefix_Info
    def factory(*args_, **kwargs_):
        if RouterAdvertisementOptionsType.subclass:
            return RouterAdvertisementOptionsType.subclass(*args_, **kwargs_)
        else:
            return RouterAdvertisementOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Src_Link_Addr(self): return self.Src_Link_Addr
    def set_Src_Link_Addr(self, Src_Link_Addr): self.Src_Link_Addr = Src_Link_Addr
    def get_MTU(self): return self.MTU
    def set_MTU(self, MTU): self.MTU = MTU
    def get_Prefix_Info(self): return self.Prefix_Info
    def set_Prefix_Info(self, Prefix_Info): self.Prefix_Info = Prefix_Info
    def hasContent_(self):
        if (
            self.Src_Link_Addr is not None or
            self.MTU is not None or
            self.Prefix_Info is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RouterAdvertisementOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RouterAdvertisementOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RouterAdvertisementOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RouterAdvertisementOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Src_Link_Addr is not None:
            self.Src_Link_Addr.export(lwrite, level, 'PacketObj:', name_='Src_Link_Addr', pretty_print=pretty_print)
        if self.MTU is not None:
            self.MTU.export(lwrite, level, 'PacketObj:', name_='MTU', pretty_print=pretty_print)
        if self.Prefix_Info is not None:
            self.Prefix_Info.export(lwrite, level, 'PacketObj:', name_='Prefix_Info', pretty_print=pretty_print)
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
        if nodeName_ == 'Src_Link_Addr':
            obj_ = NDPLinkAddrType.factory()
            obj_.build(child_)
            self.set_Src_Link_Addr(obj_)
        elif nodeName_ == 'MTU':
            obj_ = NDPMTUType.factory()
            obj_.build(child_)
            self.set_MTU(obj_)
        elif nodeName_ == 'Prefix_Info':
            obj_ = NDPPrefixInfoType.factory()
            obj_.build(child_)
            self.set_Prefix_Info(obj_)
# end class RouterAdvertisementOptionsType

class NeighborSolicitationType(GeneratedsSuper):
    """Nodes send Neighbor Solicitations to request the link-layer address
    of a target node while also providing their own link-layer
    address to the target. Neighbor Solicitations are multicast when
    the node needs to resolve an address and unicast when the node
    seeks to verify the reachability of a neighbor. (type=135;
    code=0)"""

    subclass = None
    superclass = None
    def __init__(self, Target_IPv6_Addr=None, Options=None):
        self.Target_IPv6_Addr = Target_IPv6_Addr
        self.Options = Options
    def factory(*args_, **kwargs_):
        if NeighborSolicitationType.subclass:
            return NeighborSolicitationType.subclass(*args_, **kwargs_)
        else:
            return NeighborSolicitationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Target_IPv6_Addr(self): return self.Target_IPv6_Addr
    def set_Target_IPv6_Addr(self, Target_IPv6_Addr): self.Target_IPv6_Addr = Target_IPv6_Addr
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def hasContent_(self):
        if (
            self.Target_IPv6_Addr is not None or
            self.Options is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NeighborSolicitationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NeighborSolicitationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NeighborSolicitationType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NeighborSolicitationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Target_IPv6_Addr is not None:
            self.Target_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Target_IPv6_Addr', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
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
        if nodeName_ == 'Target_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Target_IPv6_Addr(obj_)
        elif nodeName_ == 'Options':
            obj_ = NeighborSolicitationOptionsType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
# end class NeighborSolicitationType

class NeighborSolicitationOptionsType(GeneratedsSuper):
    """Neighbor Solicitation messages include zero or more options, some of
    which may appear multiple times in the same message."""

    subclass = None
    superclass = None
    def __init__(self, Src_Link_Addr=None):
        self.Src_Link_Addr = Src_Link_Addr
    def factory(*args_, **kwargs_):
        if NeighborSolicitationOptionsType.subclass:
            return NeighborSolicitationOptionsType.subclass(*args_, **kwargs_)
        else:
            return NeighborSolicitationOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Src_Link_Addr(self): return self.Src_Link_Addr
    def set_Src_Link_Addr(self, Src_Link_Addr): self.Src_Link_Addr = Src_Link_Addr
    def hasContent_(self):
        if (
            self.Src_Link_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NeighborSolicitationOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NeighborSolicitationOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NeighborSolicitationOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NeighborSolicitationOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Src_Link_Addr is not None:
            self.Src_Link_Addr.export(lwrite, level, 'PacketObj:', name_='Src_Link_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'Src_Link_Addr':
            obj_ = NDPLinkAddrType.factory()
            obj_.build(child_)
            self.set_Src_Link_Addr(obj_)
# end class NeighborSolicitationOptionsType

class NeighborAdvertisementType(GeneratedsSuper):
    """A node sends Neighbor Advertisements in response to Neighbor
    Solicitations and sends unsolicited Neighbor Advertisements in
    order to (unreliably) propagate new information quickly.
    (type=136; code=0)Router flag. When set, the R-bit indicates
    that the sender is a router. The R-bit is used by Neighbor
    Unreachability Detection to detect a router that changes to a
    host.Solicited flag. When set, the S-bit indicates that the
    advertisement was sent in response to a Neighbor Solicitation
    from the Destination address. The S-bit is used as a
    reachability confirmation for Neighbor Unreachability
    Detection.Override flag. When set, the O-bit indicates that the
    advertisement should override an existing cache entry and update
    the cached link-layer address."""

    subclass = None
    superclass = None
    def __init__(self, override_flag=None, router_flag=None, solicited_flag=None, Target_IPv6_Addr=None, Options=None):
        self.override_flag = _cast(bool, override_flag)
        self.router_flag = _cast(bool, router_flag)
        self.solicited_flag = _cast(bool, solicited_flag)
        self.Target_IPv6_Addr = Target_IPv6_Addr
        self.Options = Options
    def factory(*args_, **kwargs_):
        if NeighborAdvertisementType.subclass:
            return NeighborAdvertisementType.subclass(*args_, **kwargs_)
        else:
            return NeighborAdvertisementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Target_IPv6_Addr(self): return self.Target_IPv6_Addr
    def set_Target_IPv6_Addr(self, Target_IPv6_Addr): self.Target_IPv6_Addr = Target_IPv6_Addr
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def get_override_flag(self): return self.override_flag
    def set_override_flag(self, override_flag): self.override_flag = override_flag
    def get_router_flag(self): return self.router_flag
    def set_router_flag(self, router_flag): self.router_flag = router_flag
    def get_solicited_flag(self): return self.solicited_flag
    def set_solicited_flag(self, solicited_flag): self.solicited_flag = solicited_flag
    def hasContent_(self):
        if (
            self.Target_IPv6_Addr is not None or
            self.Options is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NeighborAdvertisementType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NeighborAdvertisementType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NeighborAdvertisementType'):
        if self.override_flag is not None:

            lwrite(' override_flag="%s"' % self.gds_format_boolean(self.override_flag, input_name='override_flag'))
        if self.router_flag is not None:

            lwrite(' router_flag="%s"' % self.gds_format_boolean(self.router_flag, input_name='router_flag'))
        if self.solicited_flag is not None:

            lwrite(' solicited_flag="%s"' % self.gds_format_boolean(self.solicited_flag, input_name='solicited_flag'))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NeighborAdvertisementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Target_IPv6_Addr is not None:
            self.Target_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Target_IPv6_Addr', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('override_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.override_flag = True
            elif value in ('false', '0'):
                self.override_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('router_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.router_flag = True
            elif value in ('false', '0'):
                self.router_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('solicited_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.solicited_flag = True
            elif value in ('false', '0'):
                self.solicited_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Target_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Target_IPv6_Addr(obj_)
        elif nodeName_ == 'Options':
            obj_ = NeighborOptionsType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
# end class NeighborAdvertisementType

class NeighborOptionsType(GeneratedsSuper):
    """Neighbor Advertisement messages include zero or more options, some
    of which may appear multiple times in the same message."""

    subclass = None
    superclass = None
    def __init__(self, Target_Link_Addr=None):
        self.Target_Link_Addr = Target_Link_Addr
    def factory(*args_, **kwargs_):
        if NeighborOptionsType.subclass:
            return NeighborOptionsType.subclass(*args_, **kwargs_)
        else:
            return NeighborOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Target_Link_Addr(self): return self.Target_Link_Addr
    def set_Target_Link_Addr(self, Target_Link_Addr): self.Target_Link_Addr = Target_Link_Addr
    def hasContent_(self):
        if (
            self.Target_Link_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NeighborOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NeighborOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NeighborOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NeighborOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Target_Link_Addr is not None:
            self.Target_Link_Addr.export(lwrite, level, 'PacketObj:', name_='Target_Link_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'Target_Link_Addr':
            obj_ = NDPLinkAddrType.factory()
            obj_.build(child_)
            self.set_Target_Link_Addr(obj_)
# end class NeighborOptionsType

class RedirectType(GeneratedsSuper):
    """Routers send Redirect packets to inform a host of a better first-hop
    node on the path to a destination. Hosts can be redirected to a
    better first-hop router but can also be informed by a redirect
    that the destination is in fact a neighbor. The latter is
    accomplished by setting the ICMP Target Address equal to the
    ICMP Destination Address. (type=137; code=0)"""

    subclass = None
    superclass = None
    def __init__(self, Target_IPv6_Addr=None, Dest_IPv6_Addr=None, Options=None):
        self.Target_IPv6_Addr = Target_IPv6_Addr
        self.Dest_IPv6_Addr = Dest_IPv6_Addr
        self.Options = Options
    def factory(*args_, **kwargs_):
        if RedirectType.subclass:
            return RedirectType.subclass(*args_, **kwargs_)
        else:
            return RedirectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Target_IPv6_Addr(self): return self.Target_IPv6_Addr
    def set_Target_IPv6_Addr(self, Target_IPv6_Addr): self.Target_IPv6_Addr = Target_IPv6_Addr
    def get_Dest_IPv6_Addr(self): return self.Dest_IPv6_Addr
    def set_Dest_IPv6_Addr(self, Dest_IPv6_Addr): self.Dest_IPv6_Addr = Dest_IPv6_Addr
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def hasContent_(self):
        if (
            self.Target_IPv6_Addr is not None or
            self.Dest_IPv6_Addr is not None or
            self.Options is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RedirectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RedirectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RedirectType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RedirectType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Target_IPv6_Addr is not None:
            self.Target_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Target_IPv6_Addr', pretty_print=pretty_print)
        if self.Dest_IPv6_Addr is not None:
            self.Dest_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Dest_IPv6_Addr', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
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
        if nodeName_ == 'Target_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Target_IPv6_Addr(obj_)
        elif nodeName_ == 'Dest_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Dest_IPv6_Addr(obj_)
        elif nodeName_ == 'Options':
            obj_ = RedirectOptionsType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
# end class RedirectType

class RedirectOptionsType(GeneratedsSuper):
    """Redirect messages include zero or more options, some of which may
    appear multiple times in the same message."""

    subclass = None
    superclass = None
    def __init__(self, Target_Link_Addr=None, Redirected_Header=None):
        self.Target_Link_Addr = Target_Link_Addr
        self.Redirected_Header = Redirected_Header
    def factory(*args_, **kwargs_):
        if RedirectOptionsType.subclass:
            return RedirectOptionsType.subclass(*args_, **kwargs_)
        else:
            return RedirectOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Target_Link_Addr(self): return self.Target_Link_Addr
    def set_Target_Link_Addr(self, Target_Link_Addr): self.Target_Link_Addr = Target_Link_Addr
    def get_Redirected_Header(self): return self.Redirected_Header
    def set_Redirected_Header(self, Redirected_Header): self.Redirected_Header = Redirected_Header
    def hasContent_(self):
        if (
            self.Target_Link_Addr is not None or
            self.Redirected_Header is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RedirectOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RedirectOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RedirectOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RedirectOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Target_Link_Addr is not None:
            self.Target_Link_Addr.export(lwrite, level, 'PacketObj:', name_='Target_Link_Addr', pretty_print=pretty_print)
        if self.Redirected_Header is not None:
            self.Redirected_Header.export(lwrite, level, 'PacketObj:', name_='Redirected_Header', pretty_print=pretty_print)
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
        if nodeName_ == 'Target_Link_Addr':
            obj_ = NDPLinkAddrType.factory()
            obj_.build(child_)
            self.set_Target_Link_Addr(obj_)
        elif nodeName_ == 'Redirected_Header':
            obj_ = NDPRedirectedHeaderType.factory()
            obj_.build(child_)
            self.set_Redirected_Header(obj_)
# end class RedirectOptionsType

class NDPLinkAddrType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Length=None, Link_Layer_MAC_Addr=None):
        self.Length = Length
        self.Link_Layer_MAC_Addr = Link_Layer_MAC_Addr
    def factory(*args_, **kwargs_):
        if NDPLinkAddrType.subclass:
            return NDPLinkAddrType.subclass(*args_, **kwargs_)
        else:
            return NDPLinkAddrType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Link_Layer_MAC_Addr(self): return self.Link_Layer_MAC_Addr
    def set_Link_Layer_MAC_Addr(self, Link_Layer_MAC_Addr): self.Link_Layer_MAC_Addr = Link_Layer_MAC_Addr
    def hasContent_(self):
        if (
            self.Length is not None or
            self.Link_Layer_MAC_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NDPLinkAddrType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NDPLinkAddrType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NDPLinkAddrType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NDPLinkAddrType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.Link_Layer_MAC_Addr is not None:
            self.Link_Layer_MAC_Addr.export(lwrite, level, 'PacketObj:', name_='Link_Layer_MAC_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Link_Layer_MAC_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Link_Layer_MAC_Addr(obj_)
# end class NDPLinkAddrType

class NDPPrefixInfoType(GeneratedsSuper):
    """Prefix Info characterizes Prefix Information for Router
    Advertisement Options. It provides hosts with on-link prefixes
    and prefixes for Address Autoconfiguration. (type=3). RFC
    4861.1-bit on-link flag. When set, indicates that this prefix
    can be used for on-link determintation. When not set the
    advertisement makes no statement about on-link or off-link
    properties of the prefix.1-bit autonomous address-configuration
    flag. When set indicates that this prefix can be usd for
    stateless address configuration."""

    subclass = None
    superclass = None
    def __init__(self, addr_config_flag=None, link_flag=None, Length=None, Prefix_Length=None, Valid_Lifetime=None, Preferred_Lifetime=None, Prefix=None):
        self.addr_config_flag = _cast(bool, addr_config_flag)
        self.link_flag = _cast(bool, link_flag)
        self.Length = Length
        self.Prefix_Length = Prefix_Length
        self.Valid_Lifetime = Valid_Lifetime
        self.Preferred_Lifetime = Preferred_Lifetime
        self.Prefix = Prefix
    def factory(*args_, **kwargs_):
        if NDPPrefixInfoType.subclass:
            return NDPPrefixInfoType.subclass(*args_, **kwargs_)
        else:
            return NDPPrefixInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Prefix_Length(self): return self.Prefix_Length
    def set_Prefix_Length(self, Prefix_Length): self.Prefix_Length = Prefix_Length
    def get_Valid_Lifetime(self): return self.Valid_Lifetime
    def set_Valid_Lifetime(self, Valid_Lifetime): self.Valid_Lifetime = Valid_Lifetime
    def get_Preferred_Lifetime(self): return self.Preferred_Lifetime
    def set_Preferred_Lifetime(self, Preferred_Lifetime): self.Preferred_Lifetime = Preferred_Lifetime
    def get_Prefix(self): return self.Prefix
    def set_Prefix(self, Prefix): self.Prefix = Prefix
    def get_addr_config_flag(self): return self.addr_config_flag
    def set_addr_config_flag(self, addr_config_flag): self.addr_config_flag = addr_config_flag
    def get_link_flag(self): return self.link_flag
    def set_link_flag(self, link_flag): self.link_flag = link_flag
    def hasContent_(self):
        if (
            self.Length is not None or
            self.Prefix_Length is not None or
            self.Valid_Lifetime is not None or
            self.Preferred_Lifetime is not None or
            self.Prefix is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NDPPrefixInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NDPPrefixInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NDPPrefixInfoType'):
        if self.addr_config_flag is not None:

            lwrite(' addr_config_flag="%s"' % self.gds_format_boolean(self.addr_config_flag, input_name='addr_config_flag'))
        if self.link_flag is not None:

            lwrite(' link_flag="%s"' % self.gds_format_boolean(self.link_flag, input_name='link_flag'))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NDPPrefixInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.Prefix_Length is not None:
            self.Prefix_Length.export(lwrite, level, 'PacketObj:', name_='Prefix_Length', pretty_print=pretty_print)
        if self.Valid_Lifetime is not None:
            self.Valid_Lifetime.export(lwrite, level, 'PacketObj:', name_='Valid_Lifetime', pretty_print=pretty_print)
        if self.Preferred_Lifetime is not None:
            self.Preferred_Lifetime.export(lwrite, level, 'PacketObj:', name_='Preferred_Lifetime', pretty_print=pretty_print)
        if self.Prefix is not None:
            self.Prefix.export(lwrite, level, 'PacketObj:', name_='Prefix', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('addr_config_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.addr_config_flag = True
            elif value in ('false', '0'):
                self.addr_config_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('link_flag', node)
        if value is not None:

            if value in ('true', '1'):
                self.link_flag = True
            elif value in ('false', '0'):
                self.link_flag = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Prefix_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Prefix_Length(obj_)
        elif nodeName_ == 'Valid_Lifetime':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Valid_Lifetime(obj_)
        elif nodeName_ == 'Preferred_Lifetime':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Preferred_Lifetime(obj_)
        elif nodeName_ == 'Prefix':
            obj_ = PrefixType.factory()
            obj_.build(child_)
            self.set_Prefix(obj_)
# end class NDPPrefixInfoType

class NDPRedirectedHeaderType(GeneratedsSuper):
    """The redirected header option is used in redirect messages and
    contains all or part of the packet that is being redirected.
    (type=4)"""

    subclass = None
    superclass = None
    def __init__(self, Length=None, IPHeader_And_Data=None):
        self.Length = Length
        self.IPHeader_And_Data = IPHeader_And_Data
    def factory(*args_, **kwargs_):
        if NDPRedirectedHeaderType.subclass:
            return NDPRedirectedHeaderType.subclass(*args_, **kwargs_)
        else:
            return NDPRedirectedHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_IPHeader_And_Data(self): return self.IPHeader_And_Data
    def set_IPHeader_And_Data(self, IPHeader_And_Data): self.IPHeader_And_Data = IPHeader_And_Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Length is not None or
            self.IPHeader_And_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NDPRedirectedHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NDPRedirectedHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NDPRedirectedHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NDPRedirectedHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.IPHeader_And_Data is not None:
            self.IPHeader_And_Data.export(lwrite, level, 'PacketObj:', name_='IPHeader_And_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'IPHeader_And_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IPHeader_And_Data(obj_)
# end class NDPRedirectedHeaderType

class NDPMTUType(GeneratedsSuper):
    """The MTU option is used in Router Advertisement messages to ensure
    that all nodes on a link use the same MTU value in those cases
    where the link MTU is not well known. (type=5)."""

    subclass = None
    superclass = None
    def __init__(self, Length=None, MTU=None):
        self.Length = Length
        self.MTU = MTU
    def factory(*args_, **kwargs_):
        if NDPMTUType.subclass:
            return NDPMTUType.subclass(*args_, **kwargs_)
        else:
            return NDPMTUType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_MTU(self): return self.MTU
    def set_MTU(self, MTU): self.MTU = MTU
    def hasContent_(self):
        if (
            self.Length is not None or
            self.MTU is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NDPMTUType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NDPMTUType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NDPMTUType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NDPMTUType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.MTU is not None:
            self.MTU.export(lwrite, level, 'PacketObj:', name_='MTU', pretty_print=pretty_print)
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
        if nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'MTU':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_MTU(obj_)
# end class NDPMTUType

class InternetLayerType(GeneratedsSuper):
    """The Internet layer is the group of methods, protocols, and
    specifications that are used to transport packets from the
    origiating host across network boundaries. Not all protocols are
    currently defined, just those most commonly used: IPv4, ICMPv4,
    IPv6, ICMPv6. Other protocols will be added as needed.
    (http://en.wikipedia.org/wiki/Internet_layer)"""

    subclass = None
    superclass = None
    def __init__(self, IPv4=None, ICMPv4=None, IPv6=None, ICMPv6=None):
        self.IPv4 = IPv4
        self.ICMPv4 = ICMPv4
        self.IPv6 = IPv6
        self.ICMPv6 = ICMPv6
    def factory(*args_, **kwargs_):
        if InternetLayerType.subclass:
            return InternetLayerType.subclass(*args_, **kwargs_)
        else:
            return InternetLayerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IPv4(self): return self.IPv4
    def set_IPv4(self, IPv4): self.IPv4 = IPv4
    def get_ICMPv4(self): return self.ICMPv4
    def set_ICMPv4(self, ICMPv4): self.ICMPv4 = ICMPv4
    def get_IPv6(self): return self.IPv6
    def set_IPv6(self, IPv6): self.IPv6 = IPv6
    def get_ICMPv6(self): return self.ICMPv6
    def set_ICMPv6(self, ICMPv6): self.ICMPv6 = ICMPv6
    def hasContent_(self):
        if (
            self.IPv4 is not None or
            self.ICMPv4 is not None or
            self.IPv6 is not None or
            self.ICMPv6 is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='InternetLayerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='InternetLayerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='InternetLayerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='InternetLayerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IPv4 is not None:
            self.IPv4.export(lwrite, level, 'PacketObj:', name_='IPv4', pretty_print=pretty_print)
        if self.ICMPv4 is not None:
            self.ICMPv4.export(lwrite, level, 'PacketObj:', name_='ICMPv4', pretty_print=pretty_print)
        if self.IPv6 is not None:
            self.IPv6.export(lwrite, level, 'PacketObj:', name_='IPv6', pretty_print=pretty_print)
        if self.ICMPv6 is not None:
            self.ICMPv6.export(lwrite, level, 'PacketObj:', name_='ICMPv6', pretty_print=pretty_print)
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
        if nodeName_ == 'IPv4':
            obj_ = IPv4PacketType.factory()
            obj_.build(child_)
            self.set_IPv4(obj_)
        elif nodeName_ == 'ICMPv4':
            obj_ = ICMPv4PacketType.factory()
            obj_.build(child_)
            self.set_ICMPv4(obj_)
        elif nodeName_ == 'IPv6':
            obj_ = IPv6PacketType.factory()
            obj_.build(child_)
            self.set_IPv6(obj_)
        elif nodeName_ == 'ICMPv6':
            obj_ = ICMPv6PacketType.factory()
            obj_.build(child_)
            self.set_ICMPv6(obj_)
# end class InternetLayerType

class IPv4PacketType(GeneratedsSuper):
    """Internet Protocol version 4 (IPv4) is a connectionless protocol for
    use on packet-switched link layer networks (e.g., Ethernet).
    REF: RFC 791; http://en.wikipedia.org/wiki/IPv4."""

    subclass = None
    superclass = None
    def __init__(self, IPv4_Header=None, Data=None):
        self.IPv4_Header = IPv4_Header
        self.Data = Data
    def factory(*args_, **kwargs_):
        if IPv4PacketType.subclass:
            return IPv4PacketType.subclass(*args_, **kwargs_)
        else:
            return IPv4PacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IPv4_Header(self): return self.IPv4_Header
    def set_IPv4_Header(self, IPv4_Header): self.IPv4_Header = IPv4_Header
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.IPv4_Header is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4PacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4PacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4PacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4PacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IPv4_Header is not None:
            self.IPv4_Header.export(lwrite, level, 'PacketObj:', name_='IPv4_Header', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'IPv4_Header':
            obj_ = IPv4HeaderType.factory()
            obj_.build(child_)
            self.set_IPv4_Header(obj_)
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class IPv4PacketType

class IPv4HeaderType(GeneratedsSuper):
    """The IPv4 header provides addressing, and internet modules use fields
    in the header to fragment and reassemble internet datagrams when
    necessary for transmission through small packet networks. REF:
    RFC 791."""

    subclass = None
    superclass = None
    def __init__(self, IP_Version=None, Header_Length=None, DSCP=None, ECN=None, Total_Length=None, Identification=None, Flags=None, Fragment_Offset=None, TTL=None, Protocol=None, Checksum=None, Src_IPv4_Addr=None, Dest_IPv4_Addr=None, Option=None):
        self.IP_Version = IP_Version
        self.Header_Length = Header_Length
        self.DSCP = DSCP
        self.ECN = ECN
        self.Total_Length = Total_Length
        self.Identification = Identification
        self.Flags = Flags
        self.Fragment_Offset = Fragment_Offset
        self.TTL = TTL
        self.Protocol = Protocol
        self.Checksum = Checksum
        self.Src_IPv4_Addr = Src_IPv4_Addr
        self.Dest_IPv4_Addr = Dest_IPv4_Addr
        if Option is None:
            self.Option = []
        else:
            self.Option = Option
    def factory(*args_, **kwargs_):
        if IPv4HeaderType.subclass:
            return IPv4HeaderType.subclass(*args_, **kwargs_)
        else:
            return IPv4HeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Version(self): return self.IP_Version
    def set_IP_Version(self, IP_Version): self.IP_Version = IP_Version
    def validate_IPVersionType(self, value):
        # Validate type IPVersionType, a restriction on None.
        pass
    def get_Header_Length(self): return self.Header_Length
    def set_Header_Length(self, Header_Length): self.Header_Length = Header_Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_DSCP(self): return self.DSCP
    def set_DSCP(self, DSCP): self.DSCP = DSCP
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_ECN(self): return self.ECN
    def set_ECN(self, ECN): self.ECN = ECN
    def get_Total_Length(self): return self.Total_Length
    def set_Total_Length(self, Total_Length): self.Total_Length = Total_Length
    def get_Identification(self): return self.Identification
    def set_Identification(self, Identification): self.Identification = Identification
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Flags(self): return self.Flags
    def set_Flags(self, Flags): self.Flags = Flags
    def get_Fragment_Offset(self): return self.Fragment_Offset
    def set_Fragment_Offset(self, Fragment_Offset): self.Fragment_Offset = Fragment_Offset
    def get_TTL(self): return self.TTL
    def set_TTL(self, TTL): self.TTL = TTL
    def get_Protocol(self): return self.Protocol
    def set_Protocol(self, Protocol): self.Protocol = Protocol
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def get_Src_IPv4_Addr(self): return self.Src_IPv4_Addr
    def set_Src_IPv4_Addr(self, Src_IPv4_Addr): self.Src_IPv4_Addr = Src_IPv4_Addr
    def get_Dest_IPv4_Addr(self): return self.Dest_IPv4_Addr
    def set_Dest_IPv4_Addr(self, Dest_IPv4_Addr): self.Dest_IPv4_Addr = Dest_IPv4_Addr
    def get_Option(self): return self.Option
    def set_Option(self, Option): self.Option = Option
    def add_Option(self, value): self.Option.append(value)
    def insert_Option(self, index, value): self.Option[index] = value
    def hasContent_(self):
        if (
            self.IP_Version is not None or
            self.Header_Length is not None or
            self.DSCP is not None or
            self.ECN is not None or
            self.Total_Length is not None or
            self.Identification is not None or
            self.Flags is not None or
            self.Fragment_Offset is not None or
            self.TTL is not None or
            self.Protocol is not None or
            self.Checksum is not None or
            self.Src_IPv4_Addr is not None or
            self.Dest_IPv4_Addr is not None or
            self.Option
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4HeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4HeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4HeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4HeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_Version is not None:
            self.IP_Version.export(lwrite, level, 'PacketObj:', name_='IP_Version', pretty_print=pretty_print)
        if self.Header_Length is not None:
            self.Header_Length.export(lwrite, level, 'PacketObj:', name_='Header_Length', pretty_print=pretty_print)
        if self.DSCP is not None:
            self.DSCP.export(lwrite, level, 'PacketObj:', name_='DSCP', pretty_print=pretty_print)
        if self.ECN is not None:
            self.ECN.export(lwrite, level, 'PacketObj:', name_='ECN', pretty_print=pretty_print)
        if self.Total_Length is not None:
            self.Total_Length.export(lwrite, level, 'PacketObj:', name_='Total_Length', pretty_print=pretty_print)
        if self.Identification is not None:
            self.Identification.export(lwrite, level, 'PacketObj:', name_='Identification', pretty_print=pretty_print)
        if self.Flags is not None:
            self.Flags.export(lwrite, level, 'PacketObj:', name_='Flags', pretty_print=pretty_print)
        if self.Fragment_Offset is not None:
            self.Fragment_Offset.export(lwrite, level, 'PacketObj:', name_='Fragment_Offset', pretty_print=pretty_print)
        if self.TTL is not None:
            self.TTL.export(lwrite, level, 'PacketObj:', name_='TTL', pretty_print=pretty_print)
        if self.Protocol is not None:
            self.Protocol.export(lwrite, level, 'PacketObj:', name_='Protocol', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
        if self.Src_IPv4_Addr is not None:
            self.Src_IPv4_Addr.export(lwrite, level, 'PacketObj:', name_='Src_IPv4_Addr', pretty_print=pretty_print)
        if self.Dest_IPv4_Addr is not None:
            self.Dest_IPv4_Addr.export(lwrite, level, 'PacketObj:', name_='Dest_IPv4_Addr', pretty_print=pretty_print)
        for Option_ in self.Option:
            Option_.export(lwrite, level, 'PacketObj:', name_='Option', pretty_print=pretty_print)
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
        if nodeName_ == 'IP_Version':
            obj_ = IPVersionType.factory()
            obj_.build(child_)
            self.set_IP_Version(obj_)
        elif nodeName_ == 'Header_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Header_Length(obj_)
        elif nodeName_ == 'DSCP':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_DSCP(obj_)
        elif nodeName_ == 'ECN':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ECN(obj_)
        elif nodeName_ == 'Total_Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Total_Length(obj_)
        elif nodeName_ == 'Identification':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Identification(obj_)
        elif nodeName_ == 'Flags':
            obj_ = IPv4FlagsType.factory()
            obj_.build(child_)
            self.set_Flags(obj_)
        elif nodeName_ == 'Fragment_Offset':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Fragment_Offset(obj_)
        elif nodeName_ == 'TTL':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TTL(obj_)
        elif nodeName_ == 'Protocol':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Protocol(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
        elif nodeName_ == 'Src_IPv4_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Src_IPv4_Addr(obj_)
        elif nodeName_ == 'Dest_IPv4_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Dest_IPv4_Addr(obj_)
        elif nodeName_ == 'Option':
            obj_ = IPv4OptionType.factory()
            obj_.build(child_)
            self.Option.append(obj_)
# end class IPv4HeaderType

class IPv4FlagsType(GeneratedsSuper):
    """These flag types are used to control or identify fragments in an IP
    packet. It is a three-bit field, each of the three bits are
    defined by a field with a string value that indicates the
    meaning of whether or not the bit is set."""

    subclass = None
    superclass = None
    def __init__(self, Reserved=None, Do_Not_Fragment=None, More_Fragments=None):
        self.Reserved = Reserved
        self.Do_Not_Fragment = Do_Not_Fragment
        self.More_Fragments = More_Fragments
    def factory(*args_, **kwargs_):
        if IPv4FlagsType.subclass:
            return IPv4FlagsType.subclass(*args_, **kwargs_)
        else:
            return IPv4FlagsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Reserved(self): return self.Reserved
    def set_Reserved(self, Reserved): self.Reserved = Reserved
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Do_Not_Fragment(self): return self.Do_Not_Fragment
    def set_Do_Not_Fragment(self, Do_Not_Fragment): self.Do_Not_Fragment = Do_Not_Fragment
    def validate_DoNotFragmentType(self, value):
        # Validate type DoNotFragmentType, a restriction on None.
        pass
    def get_More_Fragments(self): return self.More_Fragments
    def set_More_Fragments(self, More_Fragments): self.More_Fragments = More_Fragments
    def validate_MoreFragmentsType(self, value):
        # Validate type MoreFragmentsType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Reserved is not None or
            self.Do_Not_Fragment is not None or
            self.More_Fragments is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4FlagsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4FlagsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4FlagsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4FlagsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Reserved is not None:
            self.Reserved.export(lwrite, level, 'PacketObj:', name_='Reserved', pretty_print=pretty_print)
        if self.Do_Not_Fragment is not None:
            self.Do_Not_Fragment.export(lwrite, level, 'PacketObj:', name_='Do_Not_Fragment', pretty_print=pretty_print)
        if self.More_Fragments is not None:
            self.More_Fragments.export(lwrite, level, 'PacketObj:', name_='More_Fragments', pretty_print=pretty_print)
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
        if nodeName_ == 'Reserved':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reserved(obj_)
        elif nodeName_ == 'Do_Not_Fragment':
            obj_ = DoNotFragmentType.factory()
            obj_.build(child_)
            self.set_Do_Not_Fragment(obj_)
        elif nodeName_ == 'More_Fragments':
            obj_ = MoreFragmentsType.factory()
            obj_.build(child_)
            self.set_More_Fragments(obj_)
# end class IPv4FlagsType

class IPv4OptionType(GeneratedsSuper):
    """The IPv4 option field is variable in length with zero or more
    options."""

    subclass = None
    superclass = None
    def __init__(self, Copy_Flag=None, Class=None, Option=None):
        self.Copy_Flag = Copy_Flag
        self.Class = Class
        self.Option = Option
    def factory(*args_, **kwargs_):
        if IPv4OptionType.subclass:
            return IPv4OptionType.subclass(*args_, **kwargs_)
        else:
            return IPv4OptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Copy_Flag(self): return self.Copy_Flag
    def set_Copy_Flag(self, Copy_Flag): self.Copy_Flag = Copy_Flag
    def validate_IPv4CopyFlagType(self, value):
        # Validate type IPv4CopyFlagType, a restriction on None.
        pass
    def get_Class(self): return self.Class
    def set_Class(self, Class): self.Class = Class
    def validate_IPv4ClassType(self, value):
        # Validate type IPv4ClassType, a restriction on None.
        pass
    def get_Option(self): return self.Option
    def set_Option(self, Option): self.Option = Option
    def validate_IPv4OptionsType(self, value):
        # Validate type IPv4OptionsType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Copy_Flag is not None or
            self.Class is not None or
            self.Option is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4OptionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4OptionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4OptionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4OptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Copy_Flag is not None:
            self.Copy_Flag.export(lwrite, level, 'PacketObj:', name_='Copy_Flag', pretty_print=pretty_print)
        if self.Class is not None:
            self.Class.export(lwrite, level, 'PacketObj:', name_='Class', pretty_print=pretty_print)
        if self.Option is not None:
            self.Option.export(lwrite, level, 'PacketObj:', name_='Option', pretty_print=pretty_print)
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
        if nodeName_ == 'Copy_Flag':
            obj_ = IPv4CopyFlagType.factory()
            obj_.build(child_)
            self.set_Copy_Flag(obj_)
        elif nodeName_ == 'Class':
            obj_ = IPv4ClassType.factory()
            obj_.build(child_)
            self.set_Class(obj_)
        elif nodeName_ == 'Option':
            obj_ = IPv4OptionsType.factory()
            obj_.build(child_)
            self.set_Option(obj_)
# end class IPv4OptionType

class IPv6PacketType(GeneratedsSuper):
    """Internet Protocol version 6 (IPv6) is intended to succeed IPv4, and
    like IPv4 it is a connectionless protocol for use on packet-
    switched link layer networks. RFC 3513, RFC 2460,
    http://en.wikipedia.org/wiki/IPv6."""

    subclass = None
    superclass = None
    def __init__(self, IPv6_Header=None, Data=None, Ext_Headers=None):
        self.IPv6_Header = IPv6_Header
        self.Data = Data
        if Ext_Headers is None:
            self.Ext_Headers = []
        else:
            self.Ext_Headers = Ext_Headers
    def factory(*args_, **kwargs_):
        if IPv6PacketType.subclass:
            return IPv6PacketType.subclass(*args_, **kwargs_)
        else:
            return IPv6PacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IPv6_Header(self): return self.IPv6_Header
    def set_IPv6_Header(self, IPv6_Header): self.IPv6_Header = IPv6_Header
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def get_Ext_Headers(self): return self.Ext_Headers
    def set_Ext_Headers(self, Ext_Headers): self.Ext_Headers = Ext_Headers
    def add_Ext_Headers(self, value): self.Ext_Headers.append(value)
    def insert_Ext_Headers(self, index, value): self.Ext_Headers[index] = value
    def hasContent_(self):
        if (
            self.IPv6_Header is not None or
            self.Data is not None or
            self.Ext_Headers
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6PacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6PacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6PacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6PacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IPv6_Header is not None:
            self.IPv6_Header.export(lwrite, level, 'PacketObj:', name_='IPv6_Header', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
        for Ext_Headers_ in self.Ext_Headers:
            Ext_Headers_.export(lwrite, level, 'PacketObj:', name_='Ext_Headers', pretty_print=pretty_print)
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
        if nodeName_ == 'IPv6_Header':
            obj_ = IPv6HeaderType.factory()
            obj_.build(child_)
            self.set_IPv6_Header(obj_)
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
        elif nodeName_ == 'Ext_Headers':
            obj_ = IPv6ExtHeaderType.factory()
            obj_.build(child_)
            self.Ext_Headers.append(obj_)
# end class IPv6PacketType

class IPv6HeaderType(GeneratedsSuper):
    """The IPv6 header is a simplification of the IPv4 header."""

    subclass = None
    superclass = None
    def __init__(self, IP_Version=None, Traffic_Class=None, Flow_Label=None, Payload_Length=None, Next_Header=None, TTL=None, Src_IPv6_Addr=None, Dest_IPv6_Addr=None):
        self.IP_Version = IP_Version
        self.Traffic_Class = Traffic_Class
        self.Flow_Label = Flow_Label
        self.Payload_Length = Payload_Length
        self.Next_Header = Next_Header
        self.TTL = TTL
        self.Src_IPv6_Addr = Src_IPv6_Addr
        self.Dest_IPv6_Addr = Dest_IPv6_Addr
    def factory(*args_, **kwargs_):
        if IPv6HeaderType.subclass:
            return IPv6HeaderType.subclass(*args_, **kwargs_)
        else:
            return IPv6HeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Version(self): return self.IP_Version
    def set_IP_Version(self, IP_Version): self.IP_Version = IP_Version
    def validate_IPVersionTypeEnum(self, value):
        # Validate type IPVersionTypeEnum, a restriction on xs:string.
        pass
    def get_Traffic_Class(self): return self.Traffic_Class
    def set_Traffic_Class(self, Traffic_Class): self.Traffic_Class = Traffic_Class
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Flow_Label(self): return self.Flow_Label
    def set_Flow_Label(self, Flow_Label): self.Flow_Label = Flow_Label
    def get_Payload_Length(self): return self.Payload_Length
    def set_Payload_Length(self, Payload_Length): self.Payload_Length = Payload_Length
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_TTL(self): return self.TTL
    def set_TTL(self, TTL): self.TTL = TTL
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Src_IPv6_Addr(self): return self.Src_IPv6_Addr
    def set_Src_IPv6_Addr(self, Src_IPv6_Addr): self.Src_IPv6_Addr = Src_IPv6_Addr
    def get_Dest_IPv6_Addr(self): return self.Dest_IPv6_Addr
    def set_Dest_IPv6_Addr(self, Dest_IPv6_Addr): self.Dest_IPv6_Addr = Dest_IPv6_Addr
    def hasContent_(self):
        if (
            self.IP_Version is not None or
            self.Traffic_Class is not None or
            self.Flow_Label is not None or
            self.Payload_Length is not None or
            self.Next_Header is not None or
            self.TTL is not None or
            self.Src_IPv6_Addr is not None or
            self.Dest_IPv6_Addr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6HeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6HeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6HeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6HeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_Version is not None:
            self.IP_Version.export(lwrite, level, 'PacketObj:', name_='IP_Version', pretty_print=pretty_print)
        if self.Traffic_Class is not None:
            self.Traffic_Class.export(lwrite, level, 'PacketObj:', name_='Traffic_Class', pretty_print=pretty_print)
        if self.Flow_Label is not None:
            self.Flow_Label.export(lwrite, level, 'PacketObj:', name_='Flow_Label', pretty_print=pretty_print)
        if self.Payload_Length is not None:
            self.Payload_Length.export(lwrite, level, 'PacketObj:', name_='Payload_Length', pretty_print=pretty_print)
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.TTL is not None:
            self.TTL.export(lwrite, level, 'PacketObj:', name_='TTL', pretty_print=pretty_print)
        if self.Src_IPv6_Addr is not None:
            self.Src_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Src_IPv6_Addr', pretty_print=pretty_print)
        if self.Dest_IPv6_Addr is not None:
            self.Dest_IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='Dest_IPv6_Addr', pretty_print=pretty_print)
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
        if nodeName_ == 'IP_Version':
            obj_ = IPVersionType.factory()
            obj_.build(child_)
            self.set_IP_Version(obj_)
        elif nodeName_ == 'Traffic_Class':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Traffic_Class(obj_)
        elif nodeName_ == 'Flow_Label':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Label(obj_)
        elif nodeName_ == 'Payload_Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Payload_Length(obj_)
        elif nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'TTL':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TTL(obj_)
        elif nodeName_ == 'Src_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Src_IPv6_Addr(obj_)
        elif nodeName_ == 'Dest_IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Dest_IPv6_Addr(obj_)
# end class IPv6HeaderType

class IPv6ExtHeaderType(GeneratedsSuper):
    """In IPv6, optional internet-layer information is encoded in separate
    headers that may be placed between the IPv6 header and the
    upper-layer header in a packet. An IPv6 packet may carry zero,
    one, or more extension headers, each identified by the Next
    Header field of the preceding header.
    http://tools.ietf.org/html/rfc2460"""

    subclass = None
    superclass = None
    def __init__(self, Hop_by_Hop_Options=None, Routing=None, Fragment=None, Destination_Options=None, Authentication_Header=None, Encapsulating_Security_Payload=None):
        self.Hop_by_Hop_Options = Hop_by_Hop_Options
        self.Routing = Routing
        self.Fragment = Fragment
        if Destination_Options is None:
            self.Destination_Options = []
        else:
            self.Destination_Options = Destination_Options
        self.Authentication_Header = Authentication_Header
        self.Encapsulating_Security_Payload = Encapsulating_Security_Payload
    def factory(*args_, **kwargs_):
        if IPv6ExtHeaderType.subclass:
            return IPv6ExtHeaderType.subclass(*args_, **kwargs_)
        else:
            return IPv6ExtHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hop_by_Hop_Options(self): return self.Hop_by_Hop_Options
    def set_Hop_by_Hop_Options(self, Hop_by_Hop_Options): self.Hop_by_Hop_Options = Hop_by_Hop_Options
    def get_Routing(self): return self.Routing
    def set_Routing(self, Routing): self.Routing = Routing
    def get_Fragment(self): return self.Fragment
    def set_Fragment(self, Fragment): self.Fragment = Fragment
    def get_Destination_Options(self): return self.Destination_Options
    def set_Destination_Options(self, Destination_Options): self.Destination_Options = Destination_Options
    def add_Destination_Options(self, value): self.Destination_Options.append(value)
    def insert_Destination_Options(self, index, value): self.Destination_Options[index] = value
    def get_Authentication_Header(self): return self.Authentication_Header
    def set_Authentication_Header(self, Authentication_Header): self.Authentication_Header = Authentication_Header
    def get_Encapsulating_Security_Payload(self): return self.Encapsulating_Security_Payload
    def set_Encapsulating_Security_Payload(self, Encapsulating_Security_Payload): self.Encapsulating_Security_Payload = Encapsulating_Security_Payload
    def hasContent_(self):
        if (
            self.Hop_by_Hop_Options is not None or
            self.Routing is not None or
            self.Fragment is not None or
            self.Destination_Options or
            self.Authentication_Header is not None or
            self.Encapsulating_Security_Payload is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6ExtHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6ExtHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6ExtHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6ExtHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hop_by_Hop_Options is not None:
            self.Hop_by_Hop_Options.export(lwrite, level, 'PacketObj:', name_='Hop_by_Hop_Options', pretty_print=pretty_print)
        if self.Routing is not None:
            self.Routing.export(lwrite, level, 'PacketObj:', name_='Routing', pretty_print=pretty_print)
        if self.Fragment is not None:
            self.Fragment.export(lwrite, level, 'PacketObj:', name_='Fragment', pretty_print=pretty_print)
        for Destination_Options_ in self.Destination_Options:
            Destination_Options_.export(lwrite, level, 'PacketObj:', name_='Destination_Options', pretty_print=pretty_print)
        if self.Authentication_Header is not None:
            self.Authentication_Header.export(lwrite, level, 'PacketObj:', name_='Authentication_Header', pretty_print=pretty_print)
        if self.Encapsulating_Security_Payload is not None:
            self.Encapsulating_Security_Payload.export(lwrite, level, 'PacketObj:', name_='Encapsulating_Security_Payload', pretty_print=pretty_print)
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
        if nodeName_ == 'Hop_by_Hop_Options':
            obj_ = HopByHopOptionsType.factory()
            obj_.build(child_)
            self.set_Hop_by_Hop_Options(obj_)
        elif nodeName_ == 'Routing':
            obj_ = RoutingType.factory()
            obj_.build(child_)
            self.set_Routing(obj_)
        elif nodeName_ == 'Fragment':
            obj_ = FragmentType.factory()
            obj_.build(child_)
            self.set_Fragment(obj_)
        elif nodeName_ == 'Destination_Options':
            obj_ = DestinationOptionsType.factory()
            obj_.build(child_)
            self.Destination_Options.append(obj_)
        elif nodeName_ == 'Authentication_Header':
            obj_ = AuthenticationHeaderType.factory()
            obj_.build(child_)
            self.set_Authentication_Header(obj_)
        elif nodeName_ == 'Encapsulating_Security_Payload':
            obj_ = EncapsulatingSecurityPayloadType.factory()
            obj_.build(child_)
            self.set_Encapsulating_Security_Payload(obj_)
# end class IPv6ExtHeaderType

class IPv6OptionType(GeneratedsSuper):
    """Specifies the meaning of each bit of the 8-bit IPv6OptionType type."""

    subclass = None
    superclass = None
    def __init__(self, Do_Not_Recogn_Action=None, Packet_Change=None, Option_Byte=None):
        self.Do_Not_Recogn_Action = Do_Not_Recogn_Action
        self.Packet_Change = Packet_Change
        self.Option_Byte = Option_Byte
    def factory(*args_, **kwargs_):
        if IPv6OptionType.subclass:
            return IPv6OptionType.subclass(*args_, **kwargs_)
        else:
            return IPv6OptionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Do_Not_Recogn_Action(self): return self.Do_Not_Recogn_Action
    def set_Do_Not_Recogn_Action(self, Do_Not_Recogn_Action): self.Do_Not_Recogn_Action = Do_Not_Recogn_Action
    def validate_IPv6DoNotRecogActionType(self, value):
        # Validate type IPv6DoNotRecogActionType, a restriction on None.
        pass
    def get_Packet_Change(self): return self.Packet_Change
    def set_Packet_Change(self, Packet_Change): self.Packet_Change = Packet_Change
    def validate_IPv6PacketChangeType(self, value):
        # Validate type IPv6PacketChangeType, a restriction on None.
        pass
    def get_Option_Byte(self): return self.Option_Byte
    def set_Option_Byte(self, Option_Byte): self.Option_Byte = Option_Byte
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Do_Not_Recogn_Action is not None or
            self.Packet_Change is not None or
            self.Option_Byte is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6OptionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6OptionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6OptionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6OptionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Do_Not_Recogn_Action is not None:
            self.Do_Not_Recogn_Action.export(lwrite, level, 'PacketObj:', name_='Do_Not_Recogn_Action', pretty_print=pretty_print)
        if self.Packet_Change is not None:
            self.Packet_Change.export(lwrite, level, 'PacketObj:', name_='Packet_Change', pretty_print=pretty_print)
        if self.Option_Byte is not None:
            self.Option_Byte.export(lwrite, level, 'PacketObj:', name_='Option_Byte', pretty_print=pretty_print)
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
        if nodeName_ == 'Do_Not_Recogn_Action':
            obj_ = IPv6DoNotRecogActionType.factory()
            obj_.build(child_)
            self.set_Do_Not_Recogn_Action(obj_)
        elif nodeName_ == 'Packet_Change':
            obj_ = IPv6PacketChangeType.factory()
            obj_.build(child_)
            self.set_Packet_Change(obj_)
        elif nodeName_ == 'Option_Byte':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Byte(obj_)
# end class IPv6OptionType

class TransportLayerType(GeneratedsSuper):
    """only UDP and TCP defined to begin. Other protocols will be defined
    as necessary."""

    subclass = None
    superclass = None
    def __init__(self, TCP=None, UDP=None):
        self.TCP = TCP
        self.UDP = UDP
    def factory(*args_, **kwargs_):
        if TransportLayerType.subclass:
            return TransportLayerType.subclass(*args_, **kwargs_)
        else:
            return TransportLayerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TCP(self): return self.TCP
    def set_TCP(self, TCP): self.TCP = TCP
    def get_UDP(self): return self.UDP
    def set_UDP(self, UDP): self.UDP = UDP
    def hasContent_(self):
        if (
            self.TCP is not None or
            self.UDP is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='TransportLayerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TransportLayerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='TransportLayerType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='TransportLayerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TCP is not None:
            self.TCP.export(lwrite, level, 'PacketObj:', name_='TCP', pretty_print=pretty_print)
        if self.UDP is not None:
            self.UDP.export(lwrite, level, 'PacketObj:', name_='UDP', pretty_print=pretty_print)
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
        if nodeName_ == 'TCP':
            obj_ = TCPType.factory()
            obj_.build(child_)
            self.set_TCP(obj_)
        elif nodeName_ == 'UDP':
            obj_ = UDPType.factory()
            obj_.build(child_)
            self.set_UDP(obj_)
# end class TransportLayerType

class TCPType(GeneratedsSuper):
    """TCP provides reliable, ordered delivery of a stream of bytes from a
    prograom on one computer to another program on another computer.
    http://en.wikipedia.org/wiki/Transmission_Control_Protocol"""

    subclass = None
    superclass = None
    def __init__(self, TCP_Header=None, Options=None, Data=None):
        self.TCP_Header = TCP_Header
        self.Options = Options
        self.Data = Data
    def factory(*args_, **kwargs_):
        if TCPType.subclass:
            return TCPType.subclass(*args_, **kwargs_)
        else:
            return TCPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TCP_Header(self): return self.TCP_Header
    def set_TCP_Header(self, TCP_Header): self.TCP_Header = TCP_Header
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.TCP_Header is not None or
            self.Options is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='TCPType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TCPType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='TCPType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='TCPType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TCP_Header is not None:
            self.TCP_Header.export(lwrite, level, 'PacketObj:', name_='TCP_Header', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'PacketObj:', name_='Options', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'TCP_Header':
            obj_ = TCPHeaderType.factory()
            obj_.build(child_)
            self.set_TCP_Header(obj_)
        elif nodeName_ == 'Options':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
        elif nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class TCPType

class UDPType(GeneratedsSuper):
    """UDP uses a simple transmission model without implicit handshaking
    dialogues for providing reliability, ordering, or data
    integrity. Thus, UDP provides an unreliable service and
    datagrams may arrive out of order, appear duplicated, or go
    missing without notice.
    http://en.wikipedia.org/wiki/User_Datagram_Protocol"""

    subclass = None
    superclass = None
    def __init__(self, UDP_Header=None, Data=None):
        self.UDP_Header = UDP_Header
        self.Data = Data
    def factory(*args_, **kwargs_):
        if UDPType.subclass:
            return UDPType.subclass(*args_, **kwargs_)
        else:
            return UDPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_UDP_Header(self): return self.UDP_Header
    def set_UDP_Header(self, UDP_Header): self.UDP_Header = UDP_Header
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def hasContent_(self):
        if (
            self.UDP_Header is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='UDPType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UDPType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='UDPType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='UDPType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.UDP_Header is not None:
            self.UDP_Header.export(lwrite, level, 'PacketObj:', name_='UDP_Header', pretty_print=pretty_print)
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'UDP_Header':
            obj_ = UDPHeaderType.factory()
            obj_.build(child_)
            self.set_UDP_Header(obj_)
        elif nodeName_ == 'Data':
            obj_ = cybox_common.DataSegmentType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class UDPType

class TCPHeaderType(GeneratedsSuper):
    """The TCP header contains 10 mandatory fields and an optional
    extension field.
    http://en.wikipedia.org/wiki/Transmission_Control_Protocol"""

    subclass = None
    superclass = None
    def __init__(self, Src_Port=None, Dest_Port=None, Seq_Num=None, ACK_Num=None, Data_Offset=None, Reserved=None, TCP_Flags=None, Window=None, Checksum=None, Urg_Ptr=None):
        self.Src_Port = Src_Port
        self.Dest_Port = Dest_Port
        self.Seq_Num = Seq_Num
        self.ACK_Num = ACK_Num
        self.Data_Offset = Data_Offset
        self.Reserved = Reserved
        self.TCP_Flags = TCP_Flags
        self.Window = Window
        self.Checksum = Checksum
        self.Urg_Ptr = Urg_Ptr
    def factory(*args_, **kwargs_):
        if TCPHeaderType.subclass:
            return TCPHeaderType.subclass(*args_, **kwargs_)
        else:
            return TCPHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Src_Port(self): return self.Src_Port
    def set_Src_Port(self, Src_Port): self.Src_Port = Src_Port
    def get_Dest_Port(self): return self.Dest_Port
    def set_Dest_Port(self, Dest_Port): self.Dest_Port = Dest_Port
    def get_Seq_Num(self): return self.Seq_Num
    def set_Seq_Num(self, Seq_Num): self.Seq_Num = Seq_Num
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_ACK_Num(self): return self.ACK_Num
    def set_ACK_Num(self, ACK_Num): self.ACK_Num = ACK_Num
    def get_Data_Offset(self): return self.Data_Offset
    def set_Data_Offset(self, Data_Offset): self.Data_Offset = Data_Offset
    def get_Reserved(self): return self.Reserved
    def set_Reserved(self, Reserved): self.Reserved = Reserved
    def get_TCP_Flags(self): return self.TCP_Flags
    def set_TCP_Flags(self, TCP_Flags): self.TCP_Flags = TCP_Flags
    def get_Window(self): return self.Window
    def set_Window(self, Window): self.Window = Window
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def get_Urg_Ptr(self): return self.Urg_Ptr
    def set_Urg_Ptr(self, Urg_Ptr): self.Urg_Ptr = Urg_Ptr
    def hasContent_(self):
        if (
            self.Src_Port is not None or
            self.Dest_Port is not None or
            self.Seq_Num is not None or
            self.ACK_Num is not None or
            self.Data_Offset is not None or
            self.Reserved is not None or
            self.TCP_Flags is not None or
            self.Window is not None or
            self.Checksum is not None or
            self.Urg_Ptr is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='TCPHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TCPHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='TCPHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='TCPHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Src_Port is not None:
            self.Src_Port.export(lwrite, level, 'PacketObj:', name_='Src_Port', pretty_print=pretty_print)
        if self.Dest_Port is not None:
            self.Dest_Port.export(lwrite, level, 'PacketObj:', name_='Dest_Port', pretty_print=pretty_print)
        if self.Seq_Num is not None:
            self.Seq_Num.export(lwrite, level, 'PacketObj:', name_='Seq_Num', pretty_print=pretty_print)
        if self.ACK_Num is not None:
            self.ACK_Num.export(lwrite, level, 'PacketObj:', name_='ACK_Num', pretty_print=pretty_print)
        if self.Data_Offset is not None:
            self.Data_Offset.export(lwrite, level, 'PacketObj:', name_='Data_Offset', pretty_print=pretty_print)
        if self.Reserved is not None:
            self.Reserved.export(lwrite, level, 'PacketObj:', name_='Reserved', pretty_print=pretty_print)
        if self.TCP_Flags is not None:
            self.TCP_Flags.export(lwrite, level, 'PacketObj:', name_='TCP_Flags', pretty_print=pretty_print)
        if self.Window is not None:
            self.Window.export(lwrite, level, 'PacketObj:', name_='Window', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
        if self.Urg_Ptr is not None:
            self.Urg_Ptr.export(lwrite, level, 'PacketObj:', name_='Urg_Ptr', pretty_print=pretty_print)
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
        if nodeName_ == 'Src_Port':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_Src_Port(obj_)
        elif nodeName_ == 'Dest_Port':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_Dest_Port(obj_)
        elif nodeName_ == 'Seq_Num':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Seq_Num(obj_)
        elif nodeName_ == 'ACK_Num':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ACK_Num(obj_)
        elif nodeName_ == 'Data_Offset':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data_Offset(obj_)
        elif nodeName_ == 'Reserved':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reserved(obj_)
        elif nodeName_ == 'TCP_Flags':
            obj_ = TCPFlagsType.factory()
            obj_.build(child_)
            self.set_TCP_Flags(obj_)
        elif nodeName_ == 'Window':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Window(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
        elif nodeName_ == 'Urg_Ptr':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Urg_Ptr(obj_)
# end class TCPHeaderType

class TCPFlagsType(GeneratedsSuper):
    """Defines the 9 different flags in the TCP header.ECN-nonce
    concealment protection.Congestion Window Reduced (CWR) flag is
    set by the sending host to indicate that it received a TCP
    segment with the ECE flag set and had responded in congestion
    control mechanism. http://en.wikipedia.org/wiki
    /Transmission_Control_ProtocolECN-Echo indicates: if the SYN
    flag is set, that the TCP peer is ECN capable; if the SYN flag
    is clear, that a packet with Congestion Experienced flag in IP
    header set is received during normal transmission. http://en.wik
    ipedia.org/wiki/Transmission_Control_ProtocolIndicates that the
    Urgent point field is significant.indicates that the
    Acknowledgment field is significant. All packets after the
    initial SYN packet sent by the client should have this flag set.
    http://en.wikipedia.org/wiki/Transmission_Control_ProtocolPush
    functions. asks to push the buffered dtata to the receiving
    application.
    http://en.wikipedia.org/wiki/Transmission_Control_ProtocolReset
    the connection.Synchronize sequence numbers. Only the first
    packet sent from each end should have this flag set.
    http://en.wikipedia.org/wiki/Transmission_Control_ProtocolIf
    this flag is set, it means there is no more data from sender."""

    subclass = None
    superclass = None
    def __init__(self, ece=None, urg=None, ack=None, cwr=None, psh=None, syn=None, rst=None, ns=None, fin=None):
        self.ece = _cast(bool, ece)
        self.urg = _cast(bool, urg)
        self.ack = _cast(bool, ack)
        self.cwr = _cast(bool, cwr)
        self.psh = _cast(bool, psh)
        self.syn = _cast(bool, syn)
        self.rst = _cast(bool, rst)
        self.ns = _cast(bool, ns)
        self.fin = _cast(bool, fin)
        pass
    def factory(*args_, **kwargs_):
        if TCPFlagsType.subclass:
            return TCPFlagsType.subclass(*args_, **kwargs_)
        else:
            return TCPFlagsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ece(self): return self.ece
    def set_ece(self, ece): self.ece = ece
    def get_urg(self): return self.urg
    def set_urg(self, urg): self.urg = urg
    def get_ack(self): return self.ack
    def set_ack(self, ack): self.ack = ack
    def get_cwr(self): return self.cwr
    def set_cwr(self, cwr): self.cwr = cwr
    def get_psh(self): return self.psh
    def set_psh(self, psh): self.psh = psh
    def get_syn(self): return self.syn
    def set_syn(self, syn): self.syn = syn
    def get_rst(self): return self.rst
    def set_rst(self, rst): self.rst = rst
    def get_ns(self): return self.ns
    def set_ns(self, ns): self.ns = ns
    def get_fin(self): return self.fin
    def set_fin(self, fin): self.fin = fin
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='TCPFlagsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TCPFlagsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='TCPFlagsType'):
        if self.ece is not None:

            lwrite(' ece="%s"' % self.gds_format_boolean(self.ece, input_name='ece'))
        if self.urg is not None:

            lwrite(' urg="%s"' % self.gds_format_boolean(self.urg, input_name='urg'))
        if self.ack is not None:

            lwrite(' ack="%s"' % self.gds_format_boolean(self.ack, input_name='ack'))
        if self.cwr is not None:

            lwrite(' cwr="%s"' % self.gds_format_boolean(self.cwr, input_name='cwr'))
        if self.psh is not None:

            lwrite(' psh="%s"' % self.gds_format_boolean(self.psh, input_name='psh'))
        if self.syn is not None:

            lwrite(' syn="%s"' % self.gds_format_boolean(self.syn, input_name='syn'))
        if self.rst is not None:

            lwrite(' rst="%s"' % self.gds_format_boolean(self.rst, input_name='rst'))
        if self.ns is not None:

            lwrite(' ns="%s"' % self.gds_format_boolean(self.ns, input_name='ns'))
        if self.fin is not None:

            lwrite(' fin="%s"' % self.gds_format_boolean(self.fin, input_name='fin'))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='TCPFlagsType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ece', node)
        if value is not None:

            if value in ('true', '1'):
                self.ece = True
            elif value in ('false', '0'):
                self.ece = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('urg', node)
        if value is not None:

            if value in ('true', '1'):
                self.urg = True
            elif value in ('false', '0'):
                self.urg = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ack', node)
        if value is not None:

            if value in ('true', '1'):
                self.ack = True
            elif value in ('false', '0'):
                self.ack = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('cwr', node)
        if value is not None:

            if value in ('true', '1'):
                self.cwr = True
            elif value in ('false', '0'):
                self.cwr = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('psh', node)
        if value is not None:

            if value in ('true', '1'):
                self.psh = True
            elif value in ('false', '0'):
                self.psh = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('syn', node)
        if value is not None:

            if value in ('true', '1'):
                self.syn = True
            elif value in ('false', '0'):
                self.syn = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('rst', node)
        if value is not None:

            if value in ('true', '1'):
                self.rst = True
            elif value in ('false', '0'):
                self.rst = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('ns', node)
        if value is not None:

            if value in ('true', '1'):
                self.ns = True
            elif value in ('false', '0'):
                self.ns = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fin', node)
        if value is not None:

            if value in ('true', '1'):
                self.fin = True
            elif value in ('false', '0'):
                self.fin = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TCPFlagsType

class UDPHeaderType(GeneratedsSuper):
    """The UDP header type defines the four fields in the UDP header."""

    subclass = None
    superclass = None
    def __init__(self, SrcPort=None, DestPort=None, Length=None, Checksum=None):
        self.SrcPort = SrcPort
        self.DestPort = DestPort
        self.Length = Length
        self.Checksum = Checksum
    def factory(*args_, **kwargs_):
        if UDPHeaderType.subclass:
            return UDPHeaderType.subclass(*args_, **kwargs_)
        else:
            return UDPHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_SrcPort(self): return self.SrcPort
    def set_SrcPort(self, SrcPort): self.SrcPort = SrcPort
    def get_DestPort(self): return self.DestPort
    def set_DestPort(self, DestPort): self.DestPort = DestPort
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.SrcPort is not None or
            self.DestPort is not None or
            self.Length is not None or
            self.Checksum is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='UDPHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UDPHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='UDPHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='UDPHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.SrcPort is not None:
            self.SrcPort.export(lwrite, level, 'PacketObj:', name_='SrcPort', pretty_print=pretty_print)
        if self.DestPort is not None:
            self.DestPort.export(lwrite, level, 'PacketObj:', name_='DestPort', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'PacketObj:', name_='Length', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
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
        if nodeName_ == 'SrcPort':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_SrcPort(obj_)
        elif nodeName_ == 'DestPort':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_DestPort(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
# end class UDPHeaderType

class ICMPv4PacketType(GeneratedsSuper):
    """ICMP is used to send error messages (e.g., a datagram cannot reach
    its destination), informational messages ( e.g., timestamp
    information), or a traceroute message. REF:
    http://www.networksorcery.com/enp/protocol/icmp.htm"""

    subclass = None
    superclass = None
    def __init__(self, ICMPv4_Header=None, Error_Msg=None, Info_Msg=None, Traceroute=None):
        self.ICMPv4_Header = ICMPv4_Header
        self.Error_Msg = Error_Msg
        self.Info_Msg = Info_Msg
        self.Traceroute = Traceroute
    def factory(*args_, **kwargs_):
        if ICMPv4PacketType.subclass:
            return ICMPv4PacketType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4PacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ICMPv4_Header(self): return self.ICMPv4_Header
    def set_ICMPv4_Header(self, ICMPv4_Header): self.ICMPv4_Header = ICMPv4_Header
    def get_Error_Msg(self): return self.Error_Msg
    def set_Error_Msg(self, Error_Msg): self.Error_Msg = Error_Msg
    def get_Info_Msg(self): return self.Info_Msg
    def set_Info_Msg(self, Info_Msg): self.Info_Msg = Info_Msg
    def get_Traceroute(self): return self.Traceroute
    def set_Traceroute(self, Traceroute): self.Traceroute = Traceroute
    def hasContent_(self):
        if (
            self.ICMPv4_Header is not None or
            self.Error_Msg is not None or
            self.Info_Msg is not None or
            self.Traceroute is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4PacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4PacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4PacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4PacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ICMPv4_Header is not None:
            self.ICMPv4_Header.export(lwrite, level, 'PacketObj:', name_='ICMPv4_Header', pretty_print=pretty_print)
        if self.Error_Msg is not None:
            self.Error_Msg.export(lwrite, level, 'PacketObj:', name_='Error_Msg', pretty_print=pretty_print)
        if self.Info_Msg is not None:
            self.Info_Msg.export(lwrite, level, 'PacketObj:', name_='Info_Msg', pretty_print=pretty_print)
        if self.Traceroute is not None:
            self.Traceroute.export(lwrite, level, 'PacketObj:', name_='Traceroute', pretty_print=pretty_print)
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
        if nodeName_ == 'ICMPv4_Header':
            obj_ = ICMPv4HeaderType.factory()
            obj_.build(child_)
            self.set_ICMPv4_Header(obj_)
        elif nodeName_ == 'Error_Msg':
            obj_ = ICMPv4ErrorMessageType.factory()
            obj_.build(child_)
            self.set_Error_Msg(obj_)
        elif nodeName_ == 'Info_Msg':
            obj_ = ICMPv4InfoMessageType.factory()
            obj_.build(child_)
            self.set_Info_Msg(obj_)
        elif nodeName_ == 'Traceroute':
            obj_ = ICMPv4TracerouteType.factory()
            obj_.build(child_)
            self.set_Traceroute(obj_)
# end class ICMPv4PacketType

class ICMPv4HeaderType(GeneratedsSuper):
    """Actual ICMP header bytes are defined, corresponding to the ICMP
    type, ICMP code, and to the checksum."""

    subclass = None
    superclass = None
    def __init__(self, Type=None, Code=None, Checksum=None):
        self.Type = Type
        self.Code = Code
        self.Checksum = Checksum
    def factory(*args_, **kwargs_):
        if ICMPv4HeaderType.subclass:
            return ICMPv4HeaderType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4HeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Code(self): return self.Code
    def set_Code(self, Code): self.Code = Code
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Code is not None or
            self.Checksum is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4HeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4HeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4HeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4HeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'PacketObj:', name_='Type', pretty_print=pretty_print)
        if self.Code is not None:
            self.Code.export(lwrite, level, 'PacketObj:', name_='Code', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
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
        if nodeName_ == 'Type':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Code':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Code(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
# end class ICMPv4HeaderType

class ICMPv4ErrorMessageType(GeneratedsSuper):
    """ICMP error messages include destination unreachable messages, source
    quench messages, redirect messages, and time exceeded messages."""

    subclass = None
    superclass = None
    def __init__(self, Destination_Unreachable=None, Source_Quench=None, Redirect_Message=None, Time_Exceeded=None, Error_Msg_Content=None):
        self.Destination_Unreachable = Destination_Unreachable
        self.Source_Quench = Source_Quench
        self.Redirect_Message = Redirect_Message
        self.Time_Exceeded = Time_Exceeded
        self.Error_Msg_Content = Error_Msg_Content
    def factory(*args_, **kwargs_):
        if ICMPv4ErrorMessageType.subclass:
            return ICMPv4ErrorMessageType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4ErrorMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Destination_Unreachable(self): return self.Destination_Unreachable
    def set_Destination_Unreachable(self, Destination_Unreachable): self.Destination_Unreachable = Destination_Unreachable
    def get_Source_Quench(self): return self.Source_Quench
    def set_Source_Quench(self, Source_Quench): self.Source_Quench = Source_Quench
    def get_Redirect_Message(self): return self.Redirect_Message
    def set_Redirect_Message(self, Redirect_Message): self.Redirect_Message = Redirect_Message
    def get_Time_Exceeded(self): return self.Time_Exceeded
    def set_Time_Exceeded(self, Time_Exceeded): self.Time_Exceeded = Time_Exceeded
    def get_Error_Msg_Content(self): return self.Error_Msg_Content
    def set_Error_Msg_Content(self, Error_Msg_Content): self.Error_Msg_Content = Error_Msg_Content
    def hasContent_(self):
        if (
            self.Destination_Unreachable is not None or
            self.Source_Quench is not None or
            self.Redirect_Message is not None or
            self.Time_Exceeded is not None or
            self.Error_Msg_Content is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4ErrorMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4ErrorMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4ErrorMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4ErrorMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Destination_Unreachable is not None:
            self.Destination_Unreachable.export(lwrite, level, 'PacketObj:', name_='Destination_Unreachable', pretty_print=pretty_print)
        if self.Source_Quench is not None:
            self.Source_Quench.export(lwrite, level, 'PacketObj:', name_='Source_Quench', pretty_print=pretty_print)
        if self.Redirect_Message is not None:
            self.Redirect_Message.export(lwrite, level, 'PacketObj:', name_='Redirect_Message', pretty_print=pretty_print)
        if self.Time_Exceeded is not None:
            self.Time_Exceeded.export(lwrite, level, 'PacketObj:', name_='Time_Exceeded', pretty_print=pretty_print)
        if self.Error_Msg_Content is not None:
            self.Error_Msg_Content.export(lwrite, level, 'PacketObj:', name_='Error_Msg_Content', pretty_print=pretty_print)
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
        if nodeName_ == 'Destination_Unreachable':
            obj_ = ICMPv4DestinationUnreachableType.factory()
            obj_.build(child_)
            self.set_Destination_Unreachable(obj_)
        elif nodeName_ == 'Source_Quench':
            obj_ = ICMPv4SourceQuenchType.factory()
            obj_.build(child_)
            self.set_Source_Quench(obj_)
        elif nodeName_ == 'Redirect_Message':
            obj_ = ICMPv4RedirectMessageType.factory()
            obj_.build(child_)
            self.set_Redirect_Message(obj_)
        elif nodeName_ == 'Time_Exceeded':
            obj_ = ICMPv4TimeExceededType.factory()
            obj_.build(child_)
            self.set_Time_Exceeded(obj_)
        elif nodeName_ == 'Error_Msg_Content':
            obj_ = ICMPv4ErrorMessageContentType.factory()
            obj_.build(child_)
            self.set_Error_Msg_Content(obj_)
# end class ICMPv4ErrorMessageType

class ICMPv4ErrorMessageContentType(GeneratedsSuper):
    """Elements associated with ICMPv4 error messages (as opposed to ICMP
    informational messages or ICMP traceroute message)."""

    subclass = None
    superclass = None
    def __init__(self, IP_Header=None, First_Eight_Bytes=None):
        self.IP_Header = IP_Header
        self.First_Eight_Bytes = First_Eight_Bytes
    def factory(*args_, **kwargs_):
        if ICMPv4ErrorMessageContentType.subclass:
            return ICMPv4ErrorMessageContentType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4ErrorMessageContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_Header(self): return self.IP_Header
    def set_IP_Header(self, IP_Header): self.IP_Header = IP_Header
    def get_First_Eight_Bytes(self): return self.First_Eight_Bytes
    def set_First_Eight_Bytes(self, First_Eight_Bytes): self.First_Eight_Bytes = First_Eight_Bytes
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.IP_Header is not None or
            self.First_Eight_Bytes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4ErrorMessageContentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4ErrorMessageContentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4ErrorMessageContentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4ErrorMessageContentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_Header is not None:
            self.IP_Header.export(lwrite, level, 'PacketObj:', name_='IP_Header', pretty_print=pretty_print)
        if self.First_Eight_Bytes is not None:
            self.First_Eight_Bytes.export(lwrite, level, 'PacketObj:', name_='First_Eight_Bytes', pretty_print=pretty_print)
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
        if nodeName_ == 'IP_Header':
            obj_ = IPv4HeaderType.factory()
            obj_.build(child_)
            self.set_IP_Header(obj_)
        elif nodeName_ == 'First_Eight_Bytes':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_First_Eight_Bytes(obj_)
# end class ICMPv4ErrorMessageContentType

class ICMPv4InfoMessageType(GeneratedsSuper):
    """ICMP informational messages include echo request/reply, timestamp
    request/reply, and address mask request/reply."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Reply=None, Echo_Request=None, Timestamp_Request=None, Timestamp_Reply=None, Address_Mask_Request=None, Address_Mask_Reply=None, Info_Msg_Content=None):
        self.Echo_Reply = Echo_Reply
        self.Echo_Request = Echo_Request
        self.Timestamp_Request = Timestamp_Request
        self.Timestamp_Reply = Timestamp_Reply
        self.Address_Mask_Request = Address_Mask_Request
        self.Address_Mask_Reply = Address_Mask_Reply
        self.Info_Msg_Content = Info_Msg_Content
    def factory(*args_, **kwargs_):
        if ICMPv4InfoMessageType.subclass:
            return ICMPv4InfoMessageType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4InfoMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Reply(self): return self.Echo_Reply
    def set_Echo_Reply(self, Echo_Reply): self.Echo_Reply = Echo_Reply
    def get_Echo_Request(self): return self.Echo_Request
    def set_Echo_Request(self, Echo_Request): self.Echo_Request = Echo_Request
    def get_Timestamp_Request(self): return self.Timestamp_Request
    def set_Timestamp_Request(self, Timestamp_Request): self.Timestamp_Request = Timestamp_Request
    def get_Timestamp_Reply(self): return self.Timestamp_Reply
    def set_Timestamp_Reply(self, Timestamp_Reply): self.Timestamp_Reply = Timestamp_Reply
    def get_Address_Mask_Request(self): return self.Address_Mask_Request
    def set_Address_Mask_Request(self, Address_Mask_Request): self.Address_Mask_Request = Address_Mask_Request
    def get_Address_Mask_Reply(self): return self.Address_Mask_Reply
    def set_Address_Mask_Reply(self, Address_Mask_Reply): self.Address_Mask_Reply = Address_Mask_Reply
    def get_Info_Msg_Content(self): return self.Info_Msg_Content
    def set_Info_Msg_Content(self, Info_Msg_Content): self.Info_Msg_Content = Info_Msg_Content
    def hasContent_(self):
        if (
            self.Echo_Reply is not None or
            self.Echo_Request is not None or
            self.Timestamp_Request is not None or
            self.Timestamp_Reply is not None or
            self.Address_Mask_Request is not None or
            self.Address_Mask_Reply is not None or
            self.Info_Msg_Content is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4InfoMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4InfoMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4InfoMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4InfoMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Reply is not None:
            self.Echo_Reply.export(lwrite, level, 'PacketObj:', name_='Echo_Reply', pretty_print=pretty_print)
        if self.Echo_Request is not None:
            self.Echo_Request.export(lwrite, level, 'PacketObj:', name_='Echo_Request', pretty_print=pretty_print)
        if self.Timestamp_Request is not None:
            self.Timestamp_Request.export(lwrite, level, 'PacketObj:', name_='Timestamp_Request', pretty_print=pretty_print)
        if self.Timestamp_Reply is not None:
            self.Timestamp_Reply.export(lwrite, level, 'PacketObj:', name_='Timestamp_Reply', pretty_print=pretty_print)
        if self.Address_Mask_Request is not None:
            self.Address_Mask_Request.export(lwrite, level, 'PacketObj:', name_='Address_Mask_Request', pretty_print=pretty_print)
        if self.Address_Mask_Reply is not None:
            self.Address_Mask_Reply.export(lwrite, level, 'PacketObj:', name_='Address_Mask_Reply', pretty_print=pretty_print)
        if self.Info_Msg_Content is not None:
            self.Info_Msg_Content.export(lwrite, level, 'PacketObj:', name_='Info_Msg_Content', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Reply':
            obj_ = ICMPv4EchoReplyType.factory()
            obj_.build(child_)
            self.set_Echo_Reply(obj_)
        elif nodeName_ == 'Echo_Request':
            obj_ = ICMPv4EchoRequestType.factory()
            obj_.build(child_)
            self.set_Echo_Request(obj_)
        elif nodeName_ == 'Timestamp_Request':
            obj_ = ICMPv4TimestampRequestType.factory()
            obj_.build(child_)
            self.set_Timestamp_Request(obj_)
        elif nodeName_ == 'Timestamp_Reply':
            obj_ = ICMPv4TimestampReplyType.factory()
            obj_.build(child_)
            self.set_Timestamp_Reply(obj_)
        elif nodeName_ == 'Address_Mask_Request':
            obj_ = ICMPv4AddressMaskRequestType.factory()
            obj_.build(child_)
            self.set_Address_Mask_Request(obj_)
        elif nodeName_ == 'Address_Mask_Reply':
            obj_ = ICMPv4AddressMaskReplyType.factory()
            obj_.build(child_)
            self.set_Address_Mask_Reply(obj_)
        elif nodeName_ == 'Info_Msg_Content':
            obj_ = ICMPv4InfoMessageContentType.factory()
            obj_.build(child_)
            self.set_Info_Msg_Content(obj_)
# end class ICMPv4InfoMessageType

class ICMPv4InfoMessageContentType(GeneratedsSuper):
    """Elements associated with ICMPv4 informational messages (as opposed
    to ICMP error messages or ICMP traceroute message)."""

    subclass = None
    superclass = None
    def __init__(self, Identifier=None, Sequence_Number=None):
        self.Identifier = Identifier
        self.Sequence_Number = Sequence_Number
    def factory(*args_, **kwargs_):
        if ICMPv4InfoMessageContentType.subclass:
            return ICMPv4InfoMessageContentType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4InfoMessageContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Identifier(self): return self.Identifier
    def set_Identifier(self, Identifier): self.Identifier = Identifier
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def hasContent_(self):
        if (
            self.Identifier is not None or
            self.Sequence_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4InfoMessageContentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4InfoMessageContentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4InfoMessageContentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4InfoMessageContentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Identifier is not None:
            self.Identifier.export(lwrite, level, 'PacketObj:', name_='Identifier', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'PacketObj:', name_='Sequence_Number', pretty_print=pretty_print)
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
        if nodeName_ == 'Identifier':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Identifier(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
# end class ICMPv4InfoMessageContentType

class ICMPv4TracerouteType(GeneratedsSuper):
    """Elements associated with ICMPv4 traceroute message (as opposed to
    ICMP error messages or ICMP informational messages); corresponds
    to ICMP type =30.
    (http://www.networksorcery.com/enp/protocol/icmp/msg30.htm)"""

    subclass = None
    superclass = None
    def __init__(self, Outbound_Packet_Forward_Success=None, Outbound_Packet_no_Route=None, Identifier=None, Outbound_Hop_Count=None, Return_Hop_Count=None, Output_Link_Speed=None, Output_Link_MTU=None):
        self.Outbound_Packet_Forward_Success = Outbound_Packet_Forward_Success
        self.Outbound_Packet_no_Route = Outbound_Packet_no_Route
        self.Identifier = Identifier
        self.Outbound_Hop_Count = Outbound_Hop_Count
        self.Return_Hop_Count = Return_Hop_Count
        self.Output_Link_Speed = Output_Link_Speed
        self.Output_Link_MTU = Output_Link_MTU
    def factory(*args_, **kwargs_):
        if ICMPv4TracerouteType.subclass:
            return ICMPv4TracerouteType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4TracerouteType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Outbound_Packet_Forward_Success(self): return self.Outbound_Packet_Forward_Success
    def set_Outbound_Packet_Forward_Success(self, Outbound_Packet_Forward_Success): self.Outbound_Packet_Forward_Success = Outbound_Packet_Forward_Success
    def get_Outbound_Packet_no_Route(self): return self.Outbound_Packet_no_Route
    def set_Outbound_Packet_no_Route(self, Outbound_Packet_no_Route): self.Outbound_Packet_no_Route = Outbound_Packet_no_Route
    def get_Identifier(self): return self.Identifier
    def set_Identifier(self, Identifier): self.Identifier = Identifier
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Outbound_Hop_Count(self): return self.Outbound_Hop_Count
    def set_Outbound_Hop_Count(self, Outbound_Hop_Count): self.Outbound_Hop_Count = Outbound_Hop_Count
    def get_Return_Hop_Count(self): return self.Return_Hop_Count
    def set_Return_Hop_Count(self, Return_Hop_Count): self.Return_Hop_Count = Return_Hop_Count
    def get_Output_Link_Speed(self): return self.Output_Link_Speed
    def set_Output_Link_Speed(self, Output_Link_Speed): self.Output_Link_Speed = Output_Link_Speed
    def get_Output_Link_MTU(self): return self.Output_Link_MTU
    def set_Output_Link_MTU(self, Output_Link_MTU): self.Output_Link_MTU = Output_Link_MTU
    def hasContent_(self):
        if (
            self.Outbound_Packet_Forward_Success is not None or
            self.Outbound_Packet_no_Route is not None or
            self.Identifier is not None or
            self.Outbound_Hop_Count is not None or
            self.Return_Hop_Count is not None or
            self.Output_Link_Speed is not None or
            self.Output_Link_MTU is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TracerouteType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4TracerouteType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4TracerouteType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TracerouteType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Outbound_Packet_Forward_Success is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sOutbound_Packet_Forward_Success>%s</%sOutbound_Packet_Forward_Success>%s' % ('PacketObj:', self.gds_format_boolean(self.Outbound_Packet_Forward_Success, input_name='Outbound_Packet_Forward_Success'), 'PacketObj:', eol_))
        if self.Outbound_Packet_no_Route is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sOutbound_Packet_no_Route>%s</%sOutbound_Packet_no_Route>%s' % ('PacketObj:', self.gds_format_boolean(self.Outbound_Packet_no_Route, input_name='Outbound_Packet_no_Route'), 'PacketObj:', eol_))
        if self.Identifier is not None:
            self.Identifier.export(lwrite, level, 'PacketObj:', name_='Identifier', pretty_print=pretty_print)
        if self.Outbound_Hop_Count is not None:
            self.Outbound_Hop_Count.export(lwrite, level, 'PacketObj:', name_='Outbound_Hop_Count', pretty_print=pretty_print)
        if self.Return_Hop_Count is not None:
            self.Return_Hop_Count.export(lwrite, level, 'PacketObj:', name_='Return_Hop_Count', pretty_print=pretty_print)
        if self.Output_Link_Speed is not None:
            self.Output_Link_Speed.export(lwrite, level, 'PacketObj:', name_='Output_Link_Speed', pretty_print=pretty_print)
        if self.Output_Link_MTU is not None:
            self.Output_Link_MTU.export(lwrite, level, 'PacketObj:', name_='Output_Link_MTU', pretty_print=pretty_print)
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
        if nodeName_ == 'Outbound_Packet_Forward_Success':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Outbound_Packet_Forward_Success')
            self.Outbound_Packet_Forward_Success = ival_
        elif nodeName_ == 'Outbound_Packet_no_Route':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Outbound_Packet_no_Route')
            self.Outbound_Packet_no_Route = ival_
        elif nodeName_ == 'Identifier':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Identifier(obj_)
        elif nodeName_ == 'Outbound_Hop_Count':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Outbound_Hop_Count(obj_)
        elif nodeName_ == 'Return_Hop_Count':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Return_Hop_Count(obj_)
        elif nodeName_ == 'Output_Link_Speed':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Output_Link_Speed(obj_)
        elif nodeName_ == 'Output_Link_MTU':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Output_Link_MTU(obj_)
# end class ICMPv4TracerouteType

class ICMPv6PacketType(GeneratedsSuper):
    """ICMP is used to send error messages (e.g., a datagram cannot reach
    its destination), informational messages ( e.g., ping). Only the
    message types defined in RFC 4443 (ICMP v6) are included;
    additional message types will be defined as needed. REF:
    http://tools.ietf.org/html/rfc4443 and
    http://www.networksorcery.com/enp/protocol/icmpv6.htm and
    http://en.wikipedia.org/wiki/ICMPv6."""

    subclass = None
    superclass = None
    def __init__(self, ICMPv6_Header=None, Error_Msg=None, Info_Msg=None):
        self.ICMPv6_Header = ICMPv6_Header
        self.Error_Msg = Error_Msg
        self.Info_Msg = Info_Msg
    def factory(*args_, **kwargs_):
        if ICMPv6PacketType.subclass:
            return ICMPv6PacketType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6PacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ICMPv6_Header(self): return self.ICMPv6_Header
    def set_ICMPv6_Header(self, ICMPv6_Header): self.ICMPv6_Header = ICMPv6_Header
    def get_Error_Msg(self): return self.Error_Msg
    def set_Error_Msg(self, Error_Msg): self.Error_Msg = Error_Msg
    def get_Info_Msg(self): return self.Info_Msg
    def set_Info_Msg(self, Info_Msg): self.Info_Msg = Info_Msg
    def hasContent_(self):
        if (
            self.ICMPv6_Header is not None or
            self.Error_Msg is not None or
            self.Info_Msg is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6PacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6PacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6PacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6PacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ICMPv6_Header is not None:
            self.ICMPv6_Header.export(lwrite, level, 'PacketObj:', name_='ICMPv6_Header', pretty_print=pretty_print)
        if self.Error_Msg is not None:
            self.Error_Msg.export(lwrite, level, 'PacketObj:', name_='Error_Msg', pretty_print=pretty_print)
        if self.Info_Msg is not None:
            self.Info_Msg.export(lwrite, level, 'PacketObj:', name_='Info_Msg', pretty_print=pretty_print)
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
        if nodeName_ == 'ICMPv6_Header':
            obj_ = ICMPv6HeaderType.factory()
            obj_.build(child_)
            self.set_ICMPv6_Header(obj_)
        elif nodeName_ == 'Error_Msg':
            obj_ = ICMPv6ErrorMessageType.factory()
            obj_.build(child_)
            self.set_Error_Msg(obj_)
        elif nodeName_ == 'Info_Msg':
            obj_ = ICMPv6InfoMessageType.factory()
            obj_.build(child_)
            self.set_Info_Msg(obj_)
# end class ICMPv6PacketType

class ICMPv6HeaderType(GeneratedsSuper):
    """Actual ICMP header bytes are defined, corresponding to the ICMP
    type, ICMP code, and to the checksum. Translation of each type
    and code byte are defined in text by using boolean values
    associated with corresponding elements in the informational and
    error message type elements."""

    subclass = None
    superclass = None
    def __init__(self, Type=None, Code=None, Checksum=None):
        self.Type = Type
        self.Code = Code
        self.Checksum = Checksum
    def factory(*args_, **kwargs_):
        if ICMPv6HeaderType.subclass:
            return ICMPv6HeaderType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6HeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Code(self): return self.Code
    def set_Code(self, Code): self.Code = Code
    def get_Checksum(self): return self.Checksum
    def set_Checksum(self, Checksum): self.Checksum = Checksum
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Code is not None or
            self.Checksum is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6HeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6HeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6HeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6HeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'PacketObj:', name_='Type', pretty_print=pretty_print)
        if self.Code is not None:
            self.Code.export(lwrite, level, 'PacketObj:', name_='Code', pretty_print=pretty_print)
        if self.Checksum is not None:
            self.Checksum.export(lwrite, level, 'PacketObj:', name_='Checksum', pretty_print=pretty_print)
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
        if nodeName_ == 'Type':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Code':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Code(obj_)
        elif nodeName_ == 'Checksum':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Checksum(obj_)
# end class ICMPv6HeaderType

class ICMPv6ErrorMessageType(GeneratedsSuper):
    """ICMP v6 error messages include destination unreachable messages,
    packet too big messages, and time exceeded messages, and
    parameter problem messages, as defined in RFC 2463. Type values
    of ICMP v6 error messages range from 1 to 127."""

    subclass = None
    superclass = None
    def __init__(self, Destination_Unreachable=None, Packet_Too_Big=None, Time_Exceeded=None, Parameter_Problem=None, Invoking_Packet=None):
        self.Destination_Unreachable = Destination_Unreachable
        self.Packet_Too_Big = Packet_Too_Big
        self.Time_Exceeded = Time_Exceeded
        self.Parameter_Problem = Parameter_Problem
        self.Invoking_Packet = Invoking_Packet
    def factory(*args_, **kwargs_):
        if ICMPv6ErrorMessageType.subclass:
            return ICMPv6ErrorMessageType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6ErrorMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Destination_Unreachable(self): return self.Destination_Unreachable
    def set_Destination_Unreachable(self, Destination_Unreachable): self.Destination_Unreachable = Destination_Unreachable
    def get_Packet_Too_Big(self): return self.Packet_Too_Big
    def set_Packet_Too_Big(self, Packet_Too_Big): self.Packet_Too_Big = Packet_Too_Big
    def get_Time_Exceeded(self): return self.Time_Exceeded
    def set_Time_Exceeded(self, Time_Exceeded): self.Time_Exceeded = Time_Exceeded
    def get_Parameter_Problem(self): return self.Parameter_Problem
    def set_Parameter_Problem(self, Parameter_Problem): self.Parameter_Problem = Parameter_Problem
    def get_Invoking_Packet(self): return self.Invoking_Packet
    def set_Invoking_Packet(self, Invoking_Packet): self.Invoking_Packet = Invoking_Packet
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Destination_Unreachable is not None or
            self.Packet_Too_Big is not None or
            self.Time_Exceeded is not None or
            self.Parameter_Problem is not None or
            self.Invoking_Packet is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6ErrorMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6ErrorMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6ErrorMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6ErrorMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Destination_Unreachable is not None:
            self.Destination_Unreachable.export(lwrite, level, 'PacketObj:', name_='Destination_Unreachable', pretty_print=pretty_print)
        if self.Packet_Too_Big is not None:
            self.Packet_Too_Big.export(lwrite, level, 'PacketObj:', name_='Packet_Too_Big', pretty_print=pretty_print)
        if self.Time_Exceeded is not None:
            self.Time_Exceeded.export(lwrite, level, 'PacketObj:', name_='Time_Exceeded', pretty_print=pretty_print)
        if self.Parameter_Problem is not None:
            self.Parameter_Problem.export(lwrite, level, 'PacketObj:', name_='Parameter_Problem', pretty_print=pretty_print)
        if self.Invoking_Packet is not None:
            self.Invoking_Packet.export(lwrite, level, 'PacketObj:', name_='Invoking_Packet', pretty_print=pretty_print)
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
        if nodeName_ == 'Destination_Unreachable':
            obj_ = ICMPv6DestinationUnreachableType.factory()
            obj_.build(child_)
            self.set_Destination_Unreachable(obj_)
        elif nodeName_ == 'Packet_Too_Big':
            obj_ = ICMPv6PacketTooBigType.factory()
            obj_.build(child_)
            self.set_Packet_Too_Big(obj_)
        elif nodeName_ == 'Time_Exceeded':
            obj_ = ICMPv6TimeExceededType.factory()
            obj_.build(child_)
            self.set_Time_Exceeded(obj_)
        elif nodeName_ == 'Parameter_Problem':
            obj_ = ICMPv6ParameterProblemType.factory()
            obj_.build(child_)
            self.set_Parameter_Problem(obj_)
        elif nodeName_ == 'Invoking_Packet':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Invoking_Packet(obj_)
# end class ICMPv6ErrorMessageType

class ICMPv6InfoMessageType(GeneratedsSuper):
    """ICMP v6 informational messages include echo request/reply; other
    informational message types will be added in the future as they
    are more commonly used (only echo request/reply are defined in
    RFC 4443)."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Request=None, Echo_Reply=None, Info_Msg_Content=None):
        self.Echo_Request = Echo_Request
        self.Echo_Reply = Echo_Reply
        self.Info_Msg_Content = Info_Msg_Content
    def factory(*args_, **kwargs_):
        if ICMPv6InfoMessageType.subclass:
            return ICMPv6InfoMessageType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6InfoMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Request(self): return self.Echo_Request
    def set_Echo_Request(self, Echo_Request): self.Echo_Request = Echo_Request
    def get_Echo_Reply(self): return self.Echo_Reply
    def set_Echo_Reply(self, Echo_Reply): self.Echo_Reply = Echo_Reply
    def get_Info_Msg_Content(self): return self.Info_Msg_Content
    def set_Info_Msg_Content(self, Info_Msg_Content): self.Info_Msg_Content = Info_Msg_Content
    def hasContent_(self):
        if (
            self.Echo_Request is not None or
            self.Echo_Reply is not None or
            self.Info_Msg_Content is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6InfoMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6InfoMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6InfoMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6InfoMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Request is not None:
            self.Echo_Request.export(lwrite, level, 'PacketObj:', name_='Echo_Request', pretty_print=pretty_print)
        if self.Echo_Reply is not None:
            self.Echo_Reply.export(lwrite, level, 'PacketObj:', name_='Echo_Reply', pretty_print=pretty_print)
        if self.Info_Msg_Content is not None:
            self.Info_Msg_Content.export(lwrite, level, 'PacketObj:', name_='Info_Msg_Content', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Request':
            obj_ = ICMPv4EchoRequestType.factory()
            obj_.build(child_)
            self.set_Echo_Request(obj_)
        elif nodeName_ == 'Echo_Reply':
            obj_ = ICMPv4EchoReplyType.factory()
            obj_.build(child_)
            self.set_Echo_Reply(obj_)
        elif nodeName_ == 'Info_Msg_Content':
            obj_ = ICMPv4InfoMessageContentType.factory()
            obj_.build(child_)
            self.set_Info_Msg_Content(obj_)
# end class ICMPv6InfoMessageType

class ICMPv6InfoMessageContentType(GeneratedsSuper):
    """Elements associated with ICMPv6 informational messages (as opposed
    to ICMP v6 error messages)."""

    subclass = None
    superclass = None
    def __init__(self, Identifier=None, Sequence_Number=None):
        self.Identifier = Identifier
        self.Sequence_Number = Sequence_Number
    def factory(*args_, **kwargs_):
        if ICMPv6InfoMessageContentType.subclass:
            return ICMPv6InfoMessageContentType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6InfoMessageContentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Identifier(self): return self.Identifier
    def set_Identifier(self, Identifier): self.Identifier = Identifier
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def hasContent_(self):
        if (
            self.Identifier is not None or
            self.Sequence_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6InfoMessageContentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6InfoMessageContentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6InfoMessageContentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6InfoMessageContentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Identifier is not None:
            self.Identifier.export(lwrite, level, 'PacketObj:', name_='Identifier', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'PacketObj:', name_='Sequence_Number', pretty_print=pretty_print)
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
        if nodeName_ == 'Identifier':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Identifier(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
# end class ICMPv6InfoMessageContentType

class ICMPv4EchoReplyType(GeneratedsSuper):
    """Echo reply v4 informational message (used to ping); ICMP type=0."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Reply=None, Data=None):
        self.Echo_Reply = Echo_Reply
        self.Data = Data
    def factory(*args_, **kwargs_):
        if ICMPv4EchoReplyType.subclass:
            return ICMPv4EchoReplyType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4EchoReplyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Reply(self): return self.Echo_Reply
    def set_Echo_Reply(self, Echo_Reply): self.Echo_Reply = Echo_Reply
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Echo_Reply is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4EchoReplyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4EchoReplyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4EchoReplyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4EchoReplyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Reply is not None:
            lwrite('<%sEcho_Reply>%s</%sEcho_Reply>%s' % ('PacketObj:', self.gds_format_boolean(self.Echo_Reply, input_name='Echo_Reply'), 'PacketObj:', eol_))
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Reply':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Echo_Reply')
            self.Echo_Reply = ival_
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class ICMPv4EchoReplyType

class ICMPv4DestinationUnreachableType(GeneratedsSuper):
    """Destination Unreachable error message; ICMP type=3."""

    subclass = None
    superclass = None
    def __init__(self, Destination_Network_Unreachable=None, Destination_Host_Unreachable=None, Destination_Protocol_Unreachable=None, Destination_Port_Unreachable=None, Fragmentation_Required=None, Source_Route_Failed=None, Destination_Network_Unknown=None, Destination_Host_Unknown=None, Source_Host_Isolated=None, Network_Administratively_Prohibited=None, Host_Administratively_Prohibited=None, Network_Unreachable_For_TOS=None, Host_Unreachable_For_TOS=None, Communication_Administratively_Prohibited=None, Host_Precedence_Violation=None, Precedence_Cutoff_In_Effect=None):
        self.Destination_Network_Unreachable = Destination_Network_Unreachable
        self.Destination_Host_Unreachable = Destination_Host_Unreachable
        self.Destination_Protocol_Unreachable = Destination_Protocol_Unreachable
        self.Destination_Port_Unreachable = Destination_Port_Unreachable
        self.Fragmentation_Required = Fragmentation_Required
        self.Source_Route_Failed = Source_Route_Failed
        self.Destination_Network_Unknown = Destination_Network_Unknown
        self.Destination_Host_Unknown = Destination_Host_Unknown
        self.Source_Host_Isolated = Source_Host_Isolated
        self.Network_Administratively_Prohibited = Network_Administratively_Prohibited
        self.Host_Administratively_Prohibited = Host_Administratively_Prohibited
        self.Network_Unreachable_For_TOS = Network_Unreachable_For_TOS
        self.Host_Unreachable_For_TOS = Host_Unreachable_For_TOS
        self.Communication_Administratively_Prohibited = Communication_Administratively_Prohibited
        self.Host_Precedence_Violation = Host_Precedence_Violation
        self.Precedence_Cutoff_In_Effect = Precedence_Cutoff_In_Effect
    def factory(*args_, **kwargs_):
        if ICMPv4DestinationUnreachableType.subclass:
            return ICMPv4DestinationUnreachableType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4DestinationUnreachableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Destination_Network_Unreachable(self): return self.Destination_Network_Unreachable
    def set_Destination_Network_Unreachable(self, Destination_Network_Unreachable): self.Destination_Network_Unreachable = Destination_Network_Unreachable
    def get_Destination_Host_Unreachable(self): return self.Destination_Host_Unreachable
    def set_Destination_Host_Unreachable(self, Destination_Host_Unreachable): self.Destination_Host_Unreachable = Destination_Host_Unreachable
    def get_Destination_Protocol_Unreachable(self): return self.Destination_Protocol_Unreachable
    def set_Destination_Protocol_Unreachable(self, Destination_Protocol_Unreachable): self.Destination_Protocol_Unreachable = Destination_Protocol_Unreachable
    def get_Destination_Port_Unreachable(self): return self.Destination_Port_Unreachable
    def set_Destination_Port_Unreachable(self, Destination_Port_Unreachable): self.Destination_Port_Unreachable = Destination_Port_Unreachable
    def get_Fragmentation_Required(self): return self.Fragmentation_Required
    def set_Fragmentation_Required(self, Fragmentation_Required): self.Fragmentation_Required = Fragmentation_Required
    def get_Source_Route_Failed(self): return self.Source_Route_Failed
    def set_Source_Route_Failed(self, Source_Route_Failed): self.Source_Route_Failed = Source_Route_Failed
    def get_Destination_Network_Unknown(self): return self.Destination_Network_Unknown
    def set_Destination_Network_Unknown(self, Destination_Network_Unknown): self.Destination_Network_Unknown = Destination_Network_Unknown
    def get_Destination_Host_Unknown(self): return self.Destination_Host_Unknown
    def set_Destination_Host_Unknown(self, Destination_Host_Unknown): self.Destination_Host_Unknown = Destination_Host_Unknown
    def get_Source_Host_Isolated(self): return self.Source_Host_Isolated
    def set_Source_Host_Isolated(self, Source_Host_Isolated): self.Source_Host_Isolated = Source_Host_Isolated
    def get_Network_Administratively_Prohibited(self): return self.Network_Administratively_Prohibited
    def set_Network_Administratively_Prohibited(self, Network_Administratively_Prohibited): self.Network_Administratively_Prohibited = Network_Administratively_Prohibited
    def get_Host_Administratively_Prohibited(self): return self.Host_Administratively_Prohibited
    def set_Host_Administratively_Prohibited(self, Host_Administratively_Prohibited): self.Host_Administratively_Prohibited = Host_Administratively_Prohibited
    def get_Network_Unreachable_For_TOS(self): return self.Network_Unreachable_For_TOS
    def set_Network_Unreachable_For_TOS(self, Network_Unreachable_For_TOS): self.Network_Unreachable_For_TOS = Network_Unreachable_For_TOS
    def get_Host_Unreachable_For_TOS(self): return self.Host_Unreachable_For_TOS
    def set_Host_Unreachable_For_TOS(self, Host_Unreachable_For_TOS): self.Host_Unreachable_For_TOS = Host_Unreachable_For_TOS
    def get_Communication_Administratively_Prohibited(self): return self.Communication_Administratively_Prohibited
    def set_Communication_Administratively_Prohibited(self, Communication_Administratively_Prohibited): self.Communication_Administratively_Prohibited = Communication_Administratively_Prohibited
    def get_Host_Precedence_Violation(self): return self.Host_Precedence_Violation
    def set_Host_Precedence_Violation(self, Host_Precedence_Violation): self.Host_Precedence_Violation = Host_Precedence_Violation
    def get_Precedence_Cutoff_In_Effect(self): return self.Precedence_Cutoff_In_Effect
    def set_Precedence_Cutoff_In_Effect(self, Precedence_Cutoff_In_Effect): self.Precedence_Cutoff_In_Effect = Precedence_Cutoff_In_Effect
    def hasContent_(self):
        if (
            self.Destination_Network_Unreachable is not None or
            self.Destination_Host_Unreachable is not None or
            self.Destination_Protocol_Unreachable is not None or
            self.Destination_Port_Unreachable is not None or
            self.Fragmentation_Required is not None or
            self.Source_Route_Failed is not None or
            self.Destination_Network_Unknown is not None or
            self.Destination_Host_Unknown is not None or
            self.Source_Host_Isolated is not None or
            self.Network_Administratively_Prohibited is not None or
            self.Host_Administratively_Prohibited is not None or
            self.Network_Unreachable_For_TOS is not None or
            self.Host_Unreachable_For_TOS is not None or
            self.Communication_Administratively_Prohibited is not None or
            self.Host_Precedence_Violation is not None or
            self.Precedence_Cutoff_In_Effect is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4DestinationUnreachableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4DestinationUnreachableType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4DestinationUnreachableType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4DestinationUnreachableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Destination_Network_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Network_Unreachable>%s</%sDestination_Network_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Network_Unreachable, input_name='Destination_Network_Unreachable'), 'PacketObj:', eol_))
        if self.Destination_Host_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Host_Unreachable>%s</%sDestination_Host_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Host_Unreachable, input_name='Destination_Host_Unreachable'), 'PacketObj:', eol_))
        if self.Destination_Protocol_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Protocol_Unreachable>%s</%sDestination_Protocol_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Protocol_Unreachable, input_name='Destination_Protocol_Unreachable'), 'PacketObj:', eol_))
        if self.Destination_Port_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Port_Unreachable>%s</%sDestination_Port_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Port_Unreachable, input_name='Destination_Port_Unreachable'), 'PacketObj:', eol_))
        if self.Fragmentation_Required is not None:
            self.Fragmentation_Required.export(lwrite, level, 'PacketObj:', name_='Fragmentation_Required', pretty_print=pretty_print)
        if self.Source_Route_Failed is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSource_Route_Failed>%s</%sSource_Route_Failed>%s' % ('PacketObj:', self.gds_format_boolean(self.Source_Route_Failed, input_name='Source_Route_Failed'), 'PacketObj:', eol_))
        if self.Destination_Network_Unknown is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Network_Unknown>%s</%sDestination_Network_Unknown>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Network_Unknown, input_name='Destination_Network_Unknown'), 'PacketObj:', eol_))
        if self.Destination_Host_Unknown is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_Host_Unknown>%s</%sDestination_Host_Unknown>%s' % ('PacketObj:', self.gds_format_boolean(self.Destination_Host_Unknown, input_name='Destination_Host_Unknown'), 'PacketObj:', eol_))
        if self.Source_Host_Isolated is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSource_Host_Isolated>%s</%sSource_Host_Isolated>%s' % ('PacketObj:', self.gds_format_boolean(self.Source_Host_Isolated, input_name='Source_Host_Isolated'), 'PacketObj:', eol_))
        if self.Network_Administratively_Prohibited is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sNetwork_Administratively_Prohibited>%s</%sNetwork_Administratively_Prohibited>%s' % ('PacketObj:', self.gds_format_boolean(self.Network_Administratively_Prohibited, input_name='Network_Administratively_Prohibited'), 'PacketObj:', eol_))
        if self.Host_Administratively_Prohibited is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sHost_Administratively_Prohibited>%s</%sHost_Administratively_Prohibited>%s' % ('PacketObj:', self.gds_format_boolean(self.Host_Administratively_Prohibited, input_name='Host_Administratively_Prohibited'), 'PacketObj:', eol_))
        if self.Network_Unreachable_For_TOS is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sNetwork_Unreachable_For_TOS>%s</%sNetwork_Unreachable_For_TOS>%s' % ('PacketObj:', self.gds_format_boolean(self.Network_Unreachable_For_TOS, input_name='Network_Unreachable_For_TOS'), 'PacketObj:', eol_))
        if self.Host_Unreachable_For_TOS is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sHost_Unreachable_For_TOS>%s</%sHost_Unreachable_For_TOS>%s' % ('PacketObj:', self.gds_format_boolean(self.Host_Unreachable_For_TOS, input_name='Host_Unreachable_For_TOS'), 'PacketObj:', eol_))
        if self.Communication_Administratively_Prohibited is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sCommunication_Administratively_Prohibited>%s</%sCommunication_Administratively_Prohibited>%s' % ('PacketObj:', self.gds_format_boolean(self.Communication_Administratively_Prohibited, input_name='Communication_Administratively_Prohibited'), 'PacketObj:', eol_))
        if self.Host_Precedence_Violation is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sHost_Precedence_Violation>%s</%sHost_Precedence_Violation>%s' % ('PacketObj:', self.gds_format_boolean(self.Host_Precedence_Violation, input_name='Host_Precedence_Violation'), 'PacketObj:', eol_))
        if self.Precedence_Cutoff_In_Effect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sPrecedence_Cutoff_In_Effect>%s</%sPrecedence_Cutoff_In_Effect>%s' % ('PacketObj:', self.gds_format_boolean(self.Precedence_Cutoff_In_Effect, input_name='Precedence_Cutoff_In_Effect'), 'PacketObj:', eol_))
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
        if nodeName_ == 'Destination_Network_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Network_Unreachable')
            self.Destination_Network_Unreachable = ival_
        elif nodeName_ == 'Destination_Host_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Host_Unreachable')
            self.Destination_Host_Unreachable = ival_
        elif nodeName_ == 'Destination_Protocol_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Protocol_Unreachable')
            self.Destination_Protocol_Unreachable = ival_
        elif nodeName_ == 'Destination_Port_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Port_Unreachable')
            self.Destination_Port_Unreachable = ival_
        elif nodeName_ == 'Fragmentation_Required':
            obj_ = FragmentationRequiredType.factory()
            obj_.build(child_)
            self.set_Fragmentation_Required(obj_)
        elif nodeName_ == 'Source_Route_Failed':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Source_Route_Failed')
            self.Source_Route_Failed = ival_
        elif nodeName_ == 'Destination_Network_Unknown':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Network_Unknown')
            self.Destination_Network_Unknown = ival_
        elif nodeName_ == 'Destination_Host_Unknown':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Destination_Host_Unknown')
            self.Destination_Host_Unknown = ival_
        elif nodeName_ == 'Source_Host_Isolated':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Source_Host_Isolated')
            self.Source_Host_Isolated = ival_
        elif nodeName_ == 'Network_Administratively_Prohibited':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Network_Administratively_Prohibited')
            self.Network_Administratively_Prohibited = ival_
        elif nodeName_ == 'Host_Administratively_Prohibited':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Host_Administratively_Prohibited')
            self.Host_Administratively_Prohibited = ival_
        elif nodeName_ == 'Network_Unreachable_For_TOS':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Network_Unreachable_For_TOS')
            self.Network_Unreachable_For_TOS = ival_
        elif nodeName_ == 'Host_Unreachable_For_TOS':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Host_Unreachable_For_TOS')
            self.Host_Unreachable_For_TOS = ival_
        elif nodeName_ == 'Communication_Administratively_Prohibited':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Communication_Administratively_Prohibited')
            self.Communication_Administratively_Prohibited = ival_
        elif nodeName_ == 'Host_Precedence_Violation':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Host_Precedence_Violation')
            self.Host_Precedence_Violation = ival_
        elif nodeName_ == 'Precedence_Cutoff_In_Effect':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Precedence_Cutoff_In_Effect')
            self.Precedence_Cutoff_In_Effect = ival_
# end class ICMPv4DestinationUnreachableType

class FragmentationRequiredType(GeneratedsSuper):
    """This further specifies an ICMP destination unreachable (type=3)
    message of code=4 (fragmentation required) message by providing
    a Next-Hop MTU field."""

    subclass = None
    superclass = None
    def __init__(self, Fragmentation_Required=None, Next_Hop_MTU=None):
        self.Fragmentation_Required = Fragmentation_Required
        self.Next_Hop_MTU = Next_Hop_MTU
    def factory(*args_, **kwargs_):
        if FragmentationRequiredType.subclass:
            return FragmentationRequiredType.subclass(*args_, **kwargs_)
        else:
            return FragmentationRequiredType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Fragmentation_Required(self): return self.Fragmentation_Required
    def set_Fragmentation_Required(self, Fragmentation_Required): self.Fragmentation_Required = Fragmentation_Required
    def get_Next_Hop_MTU(self): return self.Next_Hop_MTU
    def set_Next_Hop_MTU(self, Next_Hop_MTU): self.Next_Hop_MTU = Next_Hop_MTU
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Fragmentation_Required is not None or
            self.Next_Hop_MTU is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='FragmentationRequiredType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FragmentationRequiredType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='FragmentationRequiredType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='FragmentationRequiredType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Fragmentation_Required is not None:
            lwrite('<%sFragmentation_Required>%s</%sFragmentation_Required>%s' % ('PacketObj:', self.gds_format_boolean(self.Fragmentation_Required, input_name='Fragmentation_Required'), 'PacketObj:', eol_))
        if self.Next_Hop_MTU is not None:
            self.Next_Hop_MTU.export(lwrite, level, 'PacketObj:', name_='Next_Hop_MTU', pretty_print=pretty_print)
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
        if nodeName_ == 'Fragmentation_Required':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Fragmentation_Required')
            self.Fragmentation_Required = ival_
        elif nodeName_ == 'Next_Hop_MTU':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Next_Hop_MTU(obj_)
# end class FragmentationRequiredType

class ICMPv4SourceQuenchType(GeneratedsSuper):
    """Source Quench (congestion control) error message; ICMP type=4."""

    subclass = None
    superclass = None
    def __init__(self, Source_Quench=None):
        self.Source_Quench = Source_Quench
    def factory(*args_, **kwargs_):
        if ICMPv4SourceQuenchType.subclass:
            return ICMPv4SourceQuenchType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4SourceQuenchType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Source_Quench(self): return self.Source_Quench
    def set_Source_Quench(self, Source_Quench): self.Source_Quench = Source_Quench
    def hasContent_(self):
        if (
            self.Source_Quench is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4SourceQuenchType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4SourceQuenchType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4SourceQuenchType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4SourceQuenchType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Source_Quench is not None:
            lwrite('<%sSource_Quench>%s</%sSource_Quench>%s' % ('PacketObj:', self.gds_format_boolean(self.Source_Quench, input_name='Source_Quench'), 'PacketObj:', eol_))
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
        if nodeName_ == 'Source_Quench':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Source_Quench')
            self.Source_Quench = ival_
# end class ICMPv4SourceQuenchType

class ICMPv4RedirectMessageType(GeneratedsSuper):
    """Redirect Message error message; ICMP type=5."""

    subclass = None
    superclass = None
    def __init__(self, Network_Redirect=None, Host_Redirect=None, ToS_Network_Redirect=None, ToS_Host_Redirect=None, IP_Address=None):
        self.Network_Redirect = Network_Redirect
        self.Host_Redirect = Host_Redirect
        self.ToS_Network_Redirect = ToS_Network_Redirect
        self.ToS_Host_Redirect = ToS_Host_Redirect
        self.IP_Address = IP_Address
    def factory(*args_, **kwargs_):
        if ICMPv4RedirectMessageType.subclass:
            return ICMPv4RedirectMessageType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4RedirectMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Redirect(self): return self.Network_Redirect
    def set_Network_Redirect(self, Network_Redirect): self.Network_Redirect = Network_Redirect
    def get_Host_Redirect(self): return self.Host_Redirect
    def set_Host_Redirect(self, Host_Redirect): self.Host_Redirect = Host_Redirect
    def get_ToS_Network_Redirect(self): return self.ToS_Network_Redirect
    def set_ToS_Network_Redirect(self, ToS_Network_Redirect): self.ToS_Network_Redirect = ToS_Network_Redirect
    def get_ToS_Host_Redirect(self): return self.ToS_Host_Redirect
    def set_ToS_Host_Redirect(self, ToS_Host_Redirect): self.ToS_Host_Redirect = ToS_Host_Redirect
    def get_IP_Address(self): return self.IP_Address
    def set_IP_Address(self, IP_Address): self.IP_Address = IP_Address
    def hasContent_(self):
        if (
            self.Network_Redirect is not None or
            self.Host_Redirect is not None or
            self.ToS_Network_Redirect is not None or
            self.ToS_Host_Redirect is not None or
            self.IP_Address is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4RedirectMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4RedirectMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4RedirectMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4RedirectMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Network_Redirect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sNetwork_Redirect>%s</%sNetwork_Redirect>%s' % ('PacketObj:', self.gds_format_boolean(self.Network_Redirect, input_name='Network_Redirect'), 'PacketObj:', eol_))
        if self.Host_Redirect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sHost_Redirect>%s</%sHost_Redirect>%s' % ('PacketObj:', self.gds_format_boolean(self.Host_Redirect, input_name='Host_Redirect'), 'PacketObj:', eol_))
        if self.ToS_Network_Redirect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sToS_Network_Redirect>%s</%sToS_Network_Redirect>%s' % ('PacketObj:', self.gds_format_boolean(self.ToS_Network_Redirect, input_name='ToS_Network_Redirect'), 'PacketObj:', eol_))
        if self.ToS_Host_Redirect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sToS_Host_Redirect>%s</%sToS_Host_Redirect>%s' % ('PacketObj:', self.gds_format_boolean(self.ToS_Host_Redirect, input_name='ToS_Host_Redirect'), 'PacketObj:', eol_))
        if self.IP_Address is not None:
            self.IP_Address.export(lwrite, level, 'PacketObj:', name_='IP_Address', pretty_print=pretty_print)
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
        if nodeName_ == 'Network_Redirect':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Network_Redirect')
            self.Network_Redirect = ival_
        elif nodeName_ == 'Host_Redirect':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Host_Redirect')
            self.Host_Redirect = ival_
        elif nodeName_ == 'ToS_Network_Redirect':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'ToS_Network_Redirect')
            self.ToS_Network_Redirect = ival_
        elif nodeName_ == 'ToS_Host_Redirect':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'ToS_Host_Redirect')
            self.ToS_Host_Redirect = ival_
        elif nodeName_ == 'IP_Address':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Address(obj_)
# end class ICMPv4RedirectMessageType

class ICMPv4EchoRequestType(GeneratedsSuper):
    """Echo Request informational message (used to ping); ICMP type=8."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Request=None, Data=None):
        self.Echo_Request = Echo_Request
        self.Data = Data
    def factory(*args_, **kwargs_):
        if ICMPv4EchoRequestType.subclass:
            return ICMPv4EchoRequestType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4EchoRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Request(self): return self.Echo_Request
    def set_Echo_Request(self, Echo_Request): self.Echo_Request = Echo_Request
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Echo_Request is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4EchoRequestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4EchoRequestType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4EchoRequestType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4EchoRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Request is not None:
            lwrite('<%sEcho_Request>%s</%sEcho_Request>%s' % ('PacketObj:', self.gds_format_boolean(self.Echo_Request, input_name='Echo_Request'), 'PacketObj:', eol_))
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Request':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Echo_Request')
            self.Echo_Request = ival_
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class ICMPv4EchoRequestType

class ICMPv4TimeExceededType(GeneratedsSuper):
    """Time Exceeded error message; ICMP type=11."""

    subclass = None
    superclass = None
    def __init__(self, TTL_Exceeded_In_Transit=None, Frag_Reassembly_Time_Exceeded=None):
        self.TTL_Exceeded_In_Transit = TTL_Exceeded_In_Transit
        self.Frag_Reassembly_Time_Exceeded = Frag_Reassembly_Time_Exceeded
    def factory(*args_, **kwargs_):
        if ICMPv4TimeExceededType.subclass:
            return ICMPv4TimeExceededType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4TimeExceededType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TTL_Exceeded_In_Transit(self): return self.TTL_Exceeded_In_Transit
    def set_TTL_Exceeded_In_Transit(self, TTL_Exceeded_In_Transit): self.TTL_Exceeded_In_Transit = TTL_Exceeded_In_Transit
    def get_Frag_Reassembly_Time_Exceeded(self): return self.Frag_Reassembly_Time_Exceeded
    def set_Frag_Reassembly_Time_Exceeded(self, Frag_Reassembly_Time_Exceeded): self.Frag_Reassembly_Time_Exceeded = Frag_Reassembly_Time_Exceeded
    def hasContent_(self):
        if (
            self.TTL_Exceeded_In_Transit is not None or
            self.Frag_Reassembly_Time_Exceeded is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimeExceededType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4TimeExceededType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4TimeExceededType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimeExceededType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TTL_Exceeded_In_Transit is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sTTL_Exceeded_In_Transit>%s</%sTTL_Exceeded_In_Transit>%s' % ('PacketObj:', self.gds_format_boolean(self.TTL_Exceeded_In_Transit, input_name='TTL_Exceeded_In_Transit'), 'PacketObj:', eol_))
        if self.Frag_Reassembly_Time_Exceeded is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sFrag_Reassembly_Time_Exceeded>%s</%sFrag_Reassembly_Time_Exceeded>%s' % ('PacketObj:', self.gds_format_boolean(self.Frag_Reassembly_Time_Exceeded, input_name='Frag_Reassembly_Time_Exceeded'), 'PacketObj:', eol_))
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
        if nodeName_ == 'TTL_Exceeded_In_Transit':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'TTL_Exceeded_In_Transit')
            self.TTL_Exceeded_In_Transit = ival_
        elif nodeName_ == 'Frag_Reassembly_Time_Exceeded':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Frag_Reassembly_Time_Exceeded')
            self.Frag_Reassembly_Time_Exceeded = ival_
# end class ICMPv4TimeExceededType

class ICMPv4TimestampRequestType(GeneratedsSuper):
    """Time Stamp Request informational message; ICMP type=13."""

    subclass = None
    superclass = None
    def __init__(self, Timestamp=None, Originate_Timestamp=None):
        self.Timestamp = Timestamp
        self.Originate_Timestamp = Originate_Timestamp
    def factory(*args_, **kwargs_):
        if ICMPv4TimestampRequestType.subclass:
            return ICMPv4TimestampRequestType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4TimestampRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Timestamp(self): return self.Timestamp
    def set_Timestamp(self, Timestamp): self.Timestamp = Timestamp
    def get_Originate_Timestamp(self): return self.Originate_Timestamp
    def set_Originate_Timestamp(self, Originate_Timestamp): self.Originate_Timestamp = Originate_Timestamp
    def hasContent_(self):
        if (
            self.Timestamp is not None or
            self.Originate_Timestamp is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimestampRequestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4TimestampRequestType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4TimestampRequestType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimestampRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Timestamp is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sTimestamp>%s</%sTimestamp>%s' % ('PacketObj:', self.gds_format_boolean(self.Timestamp, input_name='Timestamp'), 'PacketObj:', eol_))
        if self.Originate_Timestamp is not None:
            self.Originate_Timestamp.export(lwrite, level, 'PacketObj:', name_='Originate_Timestamp', pretty_print=pretty_print)
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
        if nodeName_ == 'Timestamp':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Timestamp')
            self.Timestamp = ival_
        elif nodeName_ == 'Originate_Timestamp':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Originate_Timestamp(obj_)
# end class ICMPv4TimestampRequestType

class ICMPv4TimestampReplyType(GeneratedsSuper):
    """Time Stamp Reply informational message; ICMP type=14."""

    subclass = None
    superclass = None
    def __init__(self, Timestamp_Reply=None, Originate_Timestamp=None, Receive_Timestamp=None, Transmit_Timestamp=None):
        self.Timestamp_Reply = Timestamp_Reply
        self.Originate_Timestamp = Originate_Timestamp
        self.Receive_Timestamp = Receive_Timestamp
        self.Transmit_Timestamp = Transmit_Timestamp
    def factory(*args_, **kwargs_):
        if ICMPv4TimestampReplyType.subclass:
            return ICMPv4TimestampReplyType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4TimestampReplyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Timestamp_Reply(self): return self.Timestamp_Reply
    def set_Timestamp_Reply(self, Timestamp_Reply): self.Timestamp_Reply = Timestamp_Reply
    def get_Originate_Timestamp(self): return self.Originate_Timestamp
    def set_Originate_Timestamp(self, Originate_Timestamp): self.Originate_Timestamp = Originate_Timestamp
    def get_Receive_Timestamp(self): return self.Receive_Timestamp
    def set_Receive_Timestamp(self, Receive_Timestamp): self.Receive_Timestamp = Receive_Timestamp
    def get_Transmit_Timestamp(self): return self.Transmit_Timestamp
    def set_Transmit_Timestamp(self, Transmit_Timestamp): self.Transmit_Timestamp = Transmit_Timestamp
    def hasContent_(self):
        if (
            self.Timestamp_Reply is not None or
            self.Originate_Timestamp is not None or
            self.Receive_Timestamp is not None or
            self.Transmit_Timestamp is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimestampReplyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4TimestampReplyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4TimestampReplyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4TimestampReplyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Timestamp_Reply is not None:
            lwrite('<%sTimestamp_Reply>%s</%sTimestamp_Reply>%s' % ('PacketObj:', self.gds_format_boolean(self.Timestamp_Reply, input_name='Timestamp_Reply'), 'PacketObj:', eol_))
        if self.Originate_Timestamp is not None:
            self.Originate_Timestamp.export(lwrite, level, 'PacketObj:', name_='Originate_Timestamp', pretty_print=pretty_print)
        if self.Receive_Timestamp is not None:
            self.Receive_Timestamp.export(lwrite, level, 'PacketObj:', name_='Receive_Timestamp', pretty_print=pretty_print)
        if self.Transmit_Timestamp is not None:
            self.Transmit_Timestamp.export(lwrite, level, 'PacketObj:', name_='Transmit_Timestamp', pretty_print=pretty_print)
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
        if nodeName_ == 'Timestamp_Reply':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Timestamp_Reply')
            self.Timestamp_Reply = ival_
        elif nodeName_ == 'Originate_Timestamp':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Originate_Timestamp(obj_)
        elif nodeName_ == 'Receive_Timestamp':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Receive_Timestamp(obj_)
        elif nodeName_ == 'Transmit_Timestamp':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Transmit_Timestamp(obj_)
# end class ICMPv4TimestampReplyType

class ICMPv4AddressMaskRequestType(GeneratedsSuper):
    """Address Mask Request informational message; ICMP type=17."""

    subclass = None
    superclass = None
    def __init__(self, Address_Mask_Request=None, Address_Mask=None):
        self.Address_Mask_Request = Address_Mask_Request
        self.Address_Mask = Address_Mask
    def factory(*args_, **kwargs_):
        if ICMPv4AddressMaskRequestType.subclass:
            return ICMPv4AddressMaskRequestType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4AddressMaskRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Address_Mask_Request(self): return self.Address_Mask_Request
    def set_Address_Mask_Request(self, Address_Mask_Request): self.Address_Mask_Request = Address_Mask_Request
    def get_Address_Mask(self): return self.Address_Mask
    def set_Address_Mask(self, Address_Mask): self.Address_Mask = Address_Mask
    def hasContent_(self):
        if (
            self.Address_Mask_Request is not None or
            self.Address_Mask is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4AddressMaskRequestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4AddressMaskRequestType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4AddressMaskRequestType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4AddressMaskRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address_Mask_Request is not None:
            lwrite('<%sAddress_Mask_Request>%s</%sAddress_Mask_Request>%s' % ('PacketObj:', self.gds_format_boolean(self.Address_Mask_Request, input_name='Address_Mask_Request'), 'PacketObj:', eol_))
        if self.Address_Mask is not None:
            self.Address_Mask.export(lwrite, level, 'PacketObj:', name_='Address_Mask', pretty_print=pretty_print)
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
        if nodeName_ == 'Address_Mask_Request':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Address_Mask_Request')
            self.Address_Mask_Request = ival_
        elif nodeName_ == 'Address_Mask':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Address_Mask(obj_)
# end class ICMPv4AddressMaskRequestType

class ICMPv4AddressMaskReplyType(GeneratedsSuper):
    """Address Mask informational message; ICMP type=18."""

    subclass = None
    superclass = None
    def __init__(self, Address_Mask_Reply=None, Address_Mask=None):
        self.Address_Mask_Reply = Address_Mask_Reply
        self.Address_Mask = Address_Mask
    def factory(*args_, **kwargs_):
        if ICMPv4AddressMaskReplyType.subclass:
            return ICMPv4AddressMaskReplyType.subclass(*args_, **kwargs_)
        else:
            return ICMPv4AddressMaskReplyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Address_Mask_Reply(self): return self.Address_Mask_Reply
    def set_Address_Mask_Reply(self, Address_Mask_Reply): self.Address_Mask_Reply = Address_Mask_Reply
    def get_Address_Mask(self): return self.Address_Mask
    def set_Address_Mask(self, Address_Mask): self.Address_Mask = Address_Mask
    def hasContent_(self):
        if (
            self.Address_Mask_Reply is not None or
            self.Address_Mask is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4AddressMaskReplyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv4AddressMaskReplyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv4AddressMaskReplyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv4AddressMaskReplyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address_Mask_Reply is not None:
            lwrite('<%sAddress_Mask_Reply>%s</%sAddress_Mask_Reply>%s' % ('PacketObj:', self.gds_format_boolean(self.Address_Mask_Reply, input_name='Address_Mask_Reply'), 'PacketObj:', eol_))
        if self.Address_Mask is not None:
            self.Address_Mask.export(lwrite, level, 'PacketObj:', name_='Address_Mask', pretty_print=pretty_print)
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
        if nodeName_ == 'Address_Mask_Reply':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Address_Mask_Reply')
            self.Address_Mask_Reply = ival_
        elif nodeName_ == 'Address_Mask':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Address_Mask(obj_)
# end class ICMPv4AddressMaskReplyType

class ICMPv6DestinationUnreachableType(GeneratedsSuper):
    """Destination unreachable error message; ICMP v6 type=1."""

    subclass = None
    superclass = None
    def __init__(self, No_Route=None, Comm_Prohibited=None, Beyond_Scope=None, Address_Unreachable=None, Port_Unreachable=None, Src_Addr_Failed_Policy=None, Reject_Route=None):
        self.No_Route = No_Route
        self.Comm_Prohibited = Comm_Prohibited
        self.Beyond_Scope = Beyond_Scope
        self.Address_Unreachable = Address_Unreachable
        self.Port_Unreachable = Port_Unreachable
        self.Src_Addr_Failed_Policy = Src_Addr_Failed_Policy
        self.Reject_Route = Reject_Route
    def factory(*args_, **kwargs_):
        if ICMPv6DestinationUnreachableType.subclass:
            return ICMPv6DestinationUnreachableType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6DestinationUnreachableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_No_Route(self): return self.No_Route
    def set_No_Route(self, No_Route): self.No_Route = No_Route
    def get_Comm_Prohibited(self): return self.Comm_Prohibited
    def set_Comm_Prohibited(self, Comm_Prohibited): self.Comm_Prohibited = Comm_Prohibited
    def get_Beyond_Scope(self): return self.Beyond_Scope
    def set_Beyond_Scope(self, Beyond_Scope): self.Beyond_Scope = Beyond_Scope
    def get_Address_Unreachable(self): return self.Address_Unreachable
    def set_Address_Unreachable(self, Address_Unreachable): self.Address_Unreachable = Address_Unreachable
    def get_Port_Unreachable(self): return self.Port_Unreachable
    def set_Port_Unreachable(self, Port_Unreachable): self.Port_Unreachable = Port_Unreachable
    def get_Src_Addr_Failed_Policy(self): return self.Src_Addr_Failed_Policy
    def set_Src_Addr_Failed_Policy(self, Src_Addr_Failed_Policy): self.Src_Addr_Failed_Policy = Src_Addr_Failed_Policy
    def get_Reject_Route(self): return self.Reject_Route
    def set_Reject_Route(self, Reject_Route): self.Reject_Route = Reject_Route
    def hasContent_(self):
        if (
            self.No_Route is not None or
            self.Comm_Prohibited is not None or
            self.Beyond_Scope is not None or
            self.Address_Unreachable is not None or
            self.Port_Unreachable is not None or
            self.Src_Addr_Failed_Policy is not None or
            self.Reject_Route is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6DestinationUnreachableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6DestinationUnreachableType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6DestinationUnreachableType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6DestinationUnreachableType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.No_Route is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sNo_Route>%s</%sNo_Route>%s' % ('PacketObj:', self.gds_format_boolean(self.No_Route, input_name='No_Route'), 'PacketObj:', eol_))
        if self.Comm_Prohibited is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sComm_Prohibited>%s</%sComm_Prohibited>%s' % ('PacketObj:', self.gds_format_boolean(self.Comm_Prohibited, input_name='Comm_Prohibited'), 'PacketObj:', eol_))
        if self.Beyond_Scope is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sBeyond_Scope>%s</%sBeyond_Scope>%s' % ('PacketObj:', self.gds_format_boolean(self.Beyond_Scope, input_name='Beyond_Scope'), 'PacketObj:', eol_))
        if self.Address_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sAddress_Unreachable>%s</%sAddress_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Address_Unreachable, input_name='Address_Unreachable'), 'PacketObj:', eol_))
        if self.Port_Unreachable is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sPort_Unreachable>%s</%sPort_Unreachable>%s' % ('PacketObj:', self.gds_format_boolean(self.Port_Unreachable, input_name='Port_Unreachable'), 'PacketObj:', eol_))
        if self.Src_Addr_Failed_Policy is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSrc_Addr_Failed_Policy>%s</%sSrc_Addr_Failed_Policy>%s' % ('PacketObj:', self.gds_format_boolean(self.Src_Addr_Failed_Policy, input_name='Src_Addr_Failed_Policy'), 'PacketObj:', eol_))
        if self.Reject_Route is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sReject_Route>%s</%sReject_Route>%s' % ('PacketObj:', self.gds_format_boolean(self.Reject_Route, input_name='Reject_Route'), 'PacketObj:', eol_))
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
        if nodeName_ == 'No_Route':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'No_Route')
            self.No_Route = ival_
        elif nodeName_ == 'Comm_Prohibited':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Comm_Prohibited')
            self.Comm_Prohibited = ival_
        elif nodeName_ == 'Beyond_Scope':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Beyond_Scope')
            self.Beyond_Scope = ival_
        elif nodeName_ == 'Address_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Address_Unreachable')
            self.Address_Unreachable = ival_
        elif nodeName_ == 'Port_Unreachable':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Port_Unreachable')
            self.Port_Unreachable = ival_
        elif nodeName_ == 'Src_Addr_Failed_Policy':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Src_Addr_Failed_Policy')
            self.Src_Addr_Failed_Policy = ival_
        elif nodeName_ == 'Reject_Route':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Reject_Route')
            self.Reject_Route = ival_
# end class ICMPv6DestinationUnreachableType

class ICMPv6PacketTooBigType(GeneratedsSuper):
    """Packet too big error message; ICMP v6 type=2."""

    subclass = None
    superclass = None
    def __init__(self, Packet_Too_Big=None, MTU=None):
        self.Packet_Too_Big = Packet_Too_Big
        self.MTU = MTU
    def factory(*args_, **kwargs_):
        if ICMPv6PacketTooBigType.subclass:
            return ICMPv6PacketTooBigType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6PacketTooBigType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Packet_Too_Big(self): return self.Packet_Too_Big
    def set_Packet_Too_Big(self, Packet_Too_Big): self.Packet_Too_Big = Packet_Too_Big
    def get_MTU(self): return self.MTU
    def set_MTU(self, MTU): self.MTU = MTU
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Packet_Too_Big is not None or
            self.MTU is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6PacketTooBigType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6PacketTooBigType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6PacketTooBigType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6PacketTooBigType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Packet_Too_Big is not None:
            lwrite('<%sPacket_Too_Big>%s</%sPacket_Too_Big>%s' % ('PacketObj:', self.gds_format_boolean(self.Packet_Too_Big, input_name='Packet_Too_Big'), 'PacketObj:', eol_))
        if self.MTU is not None:
            self.MTU.export(lwrite, level, 'PacketObj:', name_='MTU', pretty_print=pretty_print)
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
        if nodeName_ == 'Packet_Too_Big':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Packet_Too_Big')
            self.Packet_Too_Big = ival_
        elif nodeName_ == 'MTU':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_MTU(obj_)
# end class ICMPv6PacketTooBigType

class ICMPv6TimeExceededType(GeneratedsSuper):
    """Time exceeded error message; ICMP v6 type=3."""

    subclass = None
    superclass = None
    def __init__(self, Hop_Limit_Exceeded=None, Fragment_Reassem_Time_Exceeded=None):
        self.Hop_Limit_Exceeded = Hop_Limit_Exceeded
        self.Fragment_Reassem_Time_Exceeded = Fragment_Reassem_Time_Exceeded
    def factory(*args_, **kwargs_):
        if ICMPv6TimeExceededType.subclass:
            return ICMPv6TimeExceededType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6TimeExceededType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hop_Limit_Exceeded(self): return self.Hop_Limit_Exceeded
    def set_Hop_Limit_Exceeded(self, Hop_Limit_Exceeded): self.Hop_Limit_Exceeded = Hop_Limit_Exceeded
    def get_Fragment_Reassem_Time_Exceeded(self): return self.Fragment_Reassem_Time_Exceeded
    def set_Fragment_Reassem_Time_Exceeded(self, Fragment_Reassem_Time_Exceeded): self.Fragment_Reassem_Time_Exceeded = Fragment_Reassem_Time_Exceeded
    def hasContent_(self):
        if (
            self.Hop_Limit_Exceeded is not None or
            self.Fragment_Reassem_Time_Exceeded is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6TimeExceededType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6TimeExceededType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6TimeExceededType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6TimeExceededType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hop_Limit_Exceeded is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sHop_Limit_Exceeded>%s</%sHop_Limit_Exceeded>%s' % ('PacketObj:', self.gds_format_boolean(self.Hop_Limit_Exceeded, input_name='Hop_Limit_Exceeded'), 'PacketObj:', eol_))
        if self.Fragment_Reassem_Time_Exceeded is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sFragment_Reassem_Time_Exceeded>%s</%sFragment_Reassem_Time_Exceeded>%s' % ('PacketObj:', self.gds_format_boolean(self.Fragment_Reassem_Time_Exceeded, input_name='Fragment_Reassem_Time_Exceeded'), 'PacketObj:', eol_))
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
        if nodeName_ == 'Hop_Limit_Exceeded':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Hop_Limit_Exceeded')
            self.Hop_Limit_Exceeded = ival_
        elif nodeName_ == 'Fragment_Reassem_Time_Exceeded':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Fragment_Reassem_Time_Exceeded')
            self.Fragment_Reassem_Time_Exceeded = ival_
# end class ICMPv6TimeExceededType

class ICMPv6ParameterProblemType(GeneratedsSuper):
    """Parameter problem error message; ICMP v6 type=4."""

    subclass = None
    superclass = None
    def __init__(self, Erroneous_Header_Field=None, Unrecognized_Next_Header_Type=None, Unrecognized_IPv6_Option=None, Pointer=None):
        self.Erroneous_Header_Field = Erroneous_Header_Field
        self.Unrecognized_Next_Header_Type = Unrecognized_Next_Header_Type
        self.Unrecognized_IPv6_Option = Unrecognized_IPv6_Option
        self.Pointer = Pointer
    def factory(*args_, **kwargs_):
        if ICMPv6ParameterProblemType.subclass:
            return ICMPv6ParameterProblemType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6ParameterProblemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Erroneous_Header_Field(self): return self.Erroneous_Header_Field
    def set_Erroneous_Header_Field(self, Erroneous_Header_Field): self.Erroneous_Header_Field = Erroneous_Header_Field
    def get_Unrecognized_Next_Header_Type(self): return self.Unrecognized_Next_Header_Type
    def set_Unrecognized_Next_Header_Type(self, Unrecognized_Next_Header_Type): self.Unrecognized_Next_Header_Type = Unrecognized_Next_Header_Type
    def get_Unrecognized_IPv6_Option(self): return self.Unrecognized_IPv6_Option
    def set_Unrecognized_IPv6_Option(self, Unrecognized_IPv6_Option): self.Unrecognized_IPv6_Option = Unrecognized_IPv6_Option
    def get_Pointer(self): return self.Pointer
    def set_Pointer(self, Pointer): self.Pointer = Pointer
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Erroneous_Header_Field is not None or
            self.Unrecognized_Next_Header_Type is not None or
            self.Unrecognized_IPv6_Option is not None or
            self.Pointer is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6ParameterProblemType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6ParameterProblemType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6ParameterProblemType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6ParameterProblemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Erroneous_Header_Field is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sErroneous_Header_Field>%s</%sErroneous_Header_Field>%s' % ('PacketObj:', self.gds_format_boolean(self.Erroneous_Header_Field, input_name='Erroneous_Header_Field'), 'PacketObj:', eol_))
        if self.Unrecognized_Next_Header_Type is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sUnrecognized_Next_Header_Type>%s</%sUnrecognized_Next_Header_Type>%s' % ('PacketObj:', self.gds_format_boolean(self.Unrecognized_Next_Header_Type, input_name='Unrecognized_Next_Header_Type'), 'PacketObj:', eol_))
        if self.Unrecognized_IPv6_Option is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sUnrecognized_IPv6_Option>%s</%sUnrecognized_IPv6_Option>%s' % ('PacketObj:', self.gds_format_boolean(self.Unrecognized_IPv6_Option, input_name='Unrecognized_IPv6_Option'), 'PacketObj:', eol_))
        if self.Pointer is not None:
            self.Pointer.export(lwrite, level, 'PacketObj:', name_='Pointer', pretty_print=pretty_print)
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
        if nodeName_ == 'Erroneous_Header_Field':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Erroneous_Header_Field')
            self.Erroneous_Header_Field = ival_
        elif nodeName_ == 'Unrecognized_Next_Header_Type':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Unrecognized_Next_Header_Type')
            self.Unrecognized_Next_Header_Type = ival_
        elif nodeName_ == 'Unrecognized_IPv6_Option':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Unrecognized_IPv6_Option')
            self.Unrecognized_IPv6_Option = ival_
        elif nodeName_ == 'Pointer':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pointer(obj_)
# end class ICMPv6ParameterProblemType

class ICMPv6EchoRequestType(GeneratedsSuper):
    """Echo request informational ICMP v6 message; type=128."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Request=None, Data=None):
        self.Echo_Request = Echo_Request
        self.Data = Data
    def factory(*args_, **kwargs_):
        if ICMPv6EchoRequestType.subclass:
            return ICMPv6EchoRequestType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6EchoRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Request(self): return self.Echo_Request
    def set_Echo_Request(self, Echo_Request): self.Echo_Request = Echo_Request
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Echo_Request is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6EchoRequestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6EchoRequestType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6EchoRequestType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6EchoRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Request is not None:
            lwrite('<%sEcho_Request>%s</%sEcho_Request>%s' % ('PacketObj:', self.gds_format_boolean(self.Echo_Request, input_name='Echo_Request'), 'PacketObj:', eol_))
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Request':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Echo_Request')
            self.Echo_Request = ival_
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class ICMPv6EchoRequestType

class ICMPv6EchoReplyType(GeneratedsSuper):
    """Echo reply informational ICMP v6 message; type=129."""

    subclass = None
    superclass = None
    def __init__(self, Echo_Reply=None, Data=None):
        self.Echo_Reply = Echo_Reply
        self.Data = Data
    def factory(*args_, **kwargs_):
        if ICMPv6EchoReplyType.subclass:
            return ICMPv6EchoReplyType.subclass(*args_, **kwargs_)
        else:
            return ICMPv6EchoReplyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Echo_Reply(self): return self.Echo_Reply
    def set_Echo_Reply(self, Echo_Reply): self.Echo_Reply = Echo_Reply
    def get_Data(self): return self.Data
    def set_Data(self, Data): self.Data = Data
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Echo_Reply is not None or
            self.Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6EchoReplyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ICMPv6EchoReplyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ICMPv6EchoReplyType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ICMPv6EchoReplyType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Echo_Reply is not None:
            lwrite('<%sEcho_Reply>%s</%sEcho_Reply>%s' % ('PacketObj:', self.gds_format_boolean(self.Echo_Reply, input_name='Echo_Reply'), 'PacketObj:', eol_))
        if self.Data is not None:
            self.Data.export(lwrite, level, 'PacketObj:', name_='Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Echo_Reply':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Echo_Reply')
            self.Echo_Reply = ival_
        elif nodeName_ == 'Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Data(obj_)
# end class ICMPv6EchoReplyType

class PrefixType(GeneratedsSuper):
    """Provides an IP address or a prefix of an IP address for NDP for
    IPv6."""

    subclass = None
    superclass = None
    def __init__(self, IPv6_Addr=None, IP_Addr_Prefix=None):
        self.IPv6_Addr = IPv6_Addr
        self.IP_Addr_Prefix = IP_Addr_Prefix
    def factory(*args_, **kwargs_):
        if PrefixType.subclass:
            return PrefixType.subclass(*args_, **kwargs_)
        else:
            return PrefixType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IPv6_Addr(self): return self.IPv6_Addr
    def set_IPv6_Addr(self, IPv6_Addr): self.IPv6_Addr = IPv6_Addr
    def get_IP_Addr_Prefix(self): return self.IP_Addr_Prefix
    def set_IP_Addr_Prefix(self, IP_Addr_Prefix): self.IP_Addr_Prefix = IP_Addr_Prefix
    def hasContent_(self):
        if (
            self.IPv6_Addr is not None or
            self.IP_Addr_Prefix is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='PrefixType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PrefixType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='PrefixType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='PrefixType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IPv6_Addr is not None:
            self.IPv6_Addr.export(lwrite, level, 'PacketObj:', name_='IPv6_Addr', pretty_print=pretty_print)
        if self.IP_Addr_Prefix is not None:
            self.IP_Addr_Prefix.export(lwrite, level, 'PacketObj:', name_='IP_Addr_Prefix', pretty_print=pretty_print)
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
        if nodeName_ == 'IPv6_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IPv6_Addr(obj_)
        elif nodeName_ == 'IP_Addr_Prefix':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_IP_Addr_Prefix(obj_)
# end class PrefixType

class HopByHopOptionsType(GeneratedsSuper):
    """Defines fields for the IPv6 Hop-by-Hop Options header which is used
    to carry optional information that must be examined by every
    node along a packet's delivery path."""

    subclass = None
    superclass = None
    def __init__(self, Next_Header=None, Header_Ext_Len=None, Option_Data=None):
        self.Next_Header = Next_Header
        self.Header_Ext_Len = Header_Ext_Len
        if Option_Data is None:
            self.Option_Data = []
        else:
            self.Option_Data = Option_Data
    def factory(*args_, **kwargs_):
        if HopByHopOptionsType.subclass:
            return HopByHopOptionsType.subclass(*args_, **kwargs_)
        else:
            return HopByHopOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Header_Ext_Len(self): return self.Header_Ext_Len
    def set_Header_Ext_Len(self, Header_Ext_Len): self.Header_Ext_Len = Header_Ext_Len
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Option_Data(self): return self.Option_Data
    def set_Option_Data(self, Option_Data): self.Option_Data = Option_Data
    def add_Option_Data(self, value): self.Option_Data.append(value)
    def insert_Option_Data(self, index, value): self.Option_Data[index] = value
    def hasContent_(self):
        if (
            self.Next_Header is not None or
            self.Header_Ext_Len is not None or
            self.Option_Data
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='HopByHopOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HopByHopOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='HopByHopOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='HopByHopOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Header_Ext_Len is not None:
            self.Header_Ext_Len.export(lwrite, level, 'PacketObj:', name_='Header_Ext_Len', pretty_print=pretty_print)
        for Option_Data_ in self.Option_Data:
            Option_Data_.export(lwrite, level, 'PacketObj:', name_='Option_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Header_Ext_Len':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Header_Ext_Len(obj_)
        elif nodeName_ == 'Option_Data':
            obj_ = OptionDataType.factory()
            obj_.build(child_)
            self.Option_Data.append(obj_)
# end class HopByHopOptionsType

class OptionDataType(GeneratedsSuper):
    """Defines the variable-length fields associated with IPv6 extension
    headers (the Hop-by-Hop Options header and the Destination
    Options header). Contains one or more type-length-value
    (TLV)-encoded options."""

    subclass = None
    superclass = None
    def __init__(self, Option_Type=None, Option_Data_Len=None, Pad1=None, PadN=None):
        self.Option_Type = Option_Type
        self.Option_Data_Len = Option_Data_Len
        self.Pad1 = Pad1
        self.PadN = PadN
    def factory(*args_, **kwargs_):
        if OptionDataType.subclass:
            return OptionDataType.subclass(*args_, **kwargs_)
        else:
            return OptionDataType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Option_Type(self): return self.Option_Type
    def set_Option_Type(self, Option_Type): self.Option_Type = Option_Type
    def get_Option_Data_Len(self): return self.Option_Data_Len
    def set_Option_Data_Len(self, Option_Data_Len): self.Option_Data_Len = Option_Data_Len
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Pad1(self): return self.Pad1
    def set_Pad1(self, Pad1): self.Pad1 = Pad1
    def get_PadN(self): return self.PadN
    def set_PadN(self, PadN): self.PadN = PadN
    def hasContent_(self):
        if (
            self.Option_Type is not None or
            self.Option_Data_Len is not None or
            self.Pad1 is not None or
            self.PadN is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='OptionDataType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OptionDataType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='OptionDataType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='OptionDataType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Option_Type is not None:
            self.Option_Type.export(lwrite, level, 'PacketObj:', name_='Option_Type', pretty_print=pretty_print)
        if self.Option_Data_Len is not None:
            self.Option_Data_Len.export(lwrite, level, 'PacketObj:', name_='Option_Data_Len', pretty_print=pretty_print)
        if self.Pad1 is not None:
            self.Pad1.export(lwrite, level, 'PacketObj:', name_='Pad1', pretty_print=pretty_print)
        if self.PadN is not None:
            self.PadN.export(lwrite, level, 'PacketObj:', name_='PadN', pretty_print=pretty_print)
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
        if nodeName_ == 'Option_Type':
            obj_ = IPv6OptionType.factory()
            obj_.build(child_)
            self.set_Option_Type(obj_)
        elif nodeName_ == 'Option_Data_Len':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Data_Len(obj_)
        elif nodeName_ == 'Pad1':
            obj_ = Pad1Type.factory()
            obj_.build(child_)
            self.set_Pad1(obj_)
        elif nodeName_ == 'PadN':
            obj_ = PadNType.factory()
            obj_.build(child_)
            self.set_PadN(obj_)
# end class OptionDataType

class RoutingType(GeneratedsSuper):
    """Specifies the fields of the Routing header, which is used by an IPv6
    source to list one or more intermediate nodes to be "visited" on
    the way to a packet's destination.
    http://tools.ietf.org/html/rfc2460"""

    subclass = None
    superclass = None
    def __init__(self, Next_Header=None, Header_Ext_Len=None, Routing_Type=None, Segments_Left=None, Type_Specific_Data=None):
        self.Next_Header = Next_Header
        self.Header_Ext_Len = Header_Ext_Len
        self.Routing_Type = Routing_Type
        self.Segments_Left = Segments_Left
        self.Type_Specific_Data = Type_Specific_Data
    def factory(*args_, **kwargs_):
        if RoutingType.subclass:
            return RoutingType.subclass(*args_, **kwargs_)
        else:
            return RoutingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Header_Ext_Len(self): return self.Header_Ext_Len
    def set_Header_Ext_Len(self, Header_Ext_Len): self.Header_Ext_Len = Header_Ext_Len
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Routing_Type(self): return self.Routing_Type
    def set_Routing_Type(self, Routing_Type): self.Routing_Type = Routing_Type
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Segments_Left(self): return self.Segments_Left
    def set_Segments_Left(self, Segments_Left): self.Segments_Left = Segments_Left
    def get_Type_Specific_Data(self): return self.Type_Specific_Data
    def set_Type_Specific_Data(self, Type_Specific_Data): self.Type_Specific_Data = Type_Specific_Data
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Next_Header is not None or
            self.Header_Ext_Len is not None or
            self.Routing_Type is not None or
            self.Segments_Left is not None or
            self.Type_Specific_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='RoutingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RoutingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='RoutingType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='RoutingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Header_Ext_Len is not None:
            self.Header_Ext_Len.export(lwrite, level, 'PacketObj:', name_='Header_Ext_Len', pretty_print=pretty_print)
        if self.Routing_Type is not None:
            self.Routing_Type.export(lwrite, level, 'PacketObj:', name_='Routing_Type', pretty_print=pretty_print)
        if self.Segments_Left is not None:
            self.Segments_Left.export(lwrite, level, 'PacketObj:', name_='Segments_Left', pretty_print=pretty_print)
        if self.Type_Specific_Data is not None:
            self.Type_Specific_Data.export(lwrite, level, 'PacketObj:', name_='Type_Specific_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Header_Ext_Len':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Header_Ext_Len(obj_)
        elif nodeName_ == 'Routing_Type':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Routing_Type(obj_)
        elif nodeName_ == 'Segments_Left':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Segments_Left(obj_)
        elif nodeName_ == 'Type_Specific_Data':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Type_Specific_Data(obj_)
# end class RoutingType

class FragmentType(GeneratedsSuper):
    """Specifies the fields of the Fragment header, which is used by an
    IPv6 source to send a packet larger than would fit in the path
    MTU. http://tools.ietf.org/html/rfc2460"""

    subclass = None
    superclass = None
    def __init__(self, Fragment_Header=None, Fragment=None):
        self.Fragment_Header = Fragment_Header
        self.Fragment = Fragment
    def factory(*args_, **kwargs_):
        if FragmentType.subclass:
            return FragmentType.subclass(*args_, **kwargs_)
        else:
            return FragmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Fragment_Header(self): return self.Fragment_Header
    def set_Fragment_Header(self, Fragment_Header): self.Fragment_Header = Fragment_Header
    def get_Fragment(self): return self.Fragment
    def set_Fragment(self, Fragment): self.Fragment = Fragment
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Fragment_Header is not None or
            self.Fragment is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='FragmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FragmentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='FragmentType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='FragmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Fragment_Header is not None:
            self.Fragment_Header.export(lwrite, level, 'PacketObj:', name_='Fragment_Header', pretty_print=pretty_print)
        if self.Fragment is not None:
            self.Fragment.export(lwrite, level, 'PacketObj:', name_='Fragment', pretty_print=pretty_print)
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
        if nodeName_ == 'Fragment_Header':
            obj_ = FragmentHeaderType.factory()
            obj_.build(child_)
            self.set_Fragment_Header(obj_)
        elif nodeName_ == 'Fragment':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Fragment(obj_)
# end class FragmentType

class DestinationOptionsType(GeneratedsSuper):
    """Defines fields for the IPv6 Destination Options header which is used
    to carry optional information that needs to be examined only by
    a packet's destination node(s)."""

    subclass = None
    superclass = None
    def __init__(self, Next_Header=None, Header_Ext_Len=None, Option_Data=None):
        self.Next_Header = Next_Header
        self.Header_Ext_Len = Header_Ext_Len
        if Option_Data is None:
            self.Option_Data = []
        else:
            self.Option_Data = Option_Data
    def factory(*args_, **kwargs_):
        if DestinationOptionsType.subclass:
            return DestinationOptionsType.subclass(*args_, **kwargs_)
        else:
            return DestinationOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Header_Ext_Len(self): return self.Header_Ext_Len
    def set_Header_Ext_Len(self, Header_Ext_Len): self.Header_Ext_Len = Header_Ext_Len
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Option_Data(self): return self.Option_Data
    def set_Option_Data(self, Option_Data): self.Option_Data = Option_Data
    def add_Option_Data(self, value): self.Option_Data.append(value)
    def insert_Option_Data(self, index, value): self.Option_Data[index] = value
    def hasContent_(self):
        if (
            self.Next_Header is not None or
            self.Header_Ext_Len is not None or
            self.Option_Data
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='DestinationOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DestinationOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='DestinationOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='DestinationOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Header_Ext_Len is not None:
            self.Header_Ext_Len.export(lwrite, level, 'PacketObj:', name_='Header_Ext_Len', pretty_print=pretty_print)
        for Option_Data_ in self.Option_Data:
            Option_Data_.export(lwrite, level, 'PacketObj:', name_='Option_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Header_Ext_Len':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Header_Ext_Len(obj_)
        elif nodeName_ == 'Option_Data':
            obj_ = OptionDataType.factory()
            obj_.build(child_)
            self.Option_Data.append(obj_)
# end class DestinationOptionsType

class AuthenticationHeaderType(GeneratedsSuper):
    """The IP Authentication Header is used to provide connectionless
    integrity and data origin authentication for IP datagrams and to
    provide protection against replays.
    http://www.ietf.org/rfc/rfc2402.txt"""

    subclass = None
    superclass = None
    def __init__(self, Next_Header=None, Header_Ext_Len=None, Security_Parameters_Index=None, Sequence_Number=None, Authentication_Data=None):
        self.Next_Header = Next_Header
        self.Header_Ext_Len = Header_Ext_Len
        self.Security_Parameters_Index = Security_Parameters_Index
        self.Sequence_Number = Sequence_Number
        self.Authentication_Data = Authentication_Data
    def factory(*args_, **kwargs_):
        if AuthenticationHeaderType.subclass:
            return AuthenticationHeaderType.subclass(*args_, **kwargs_)
        else:
            return AuthenticationHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Header_Ext_Len(self): return self.Header_Ext_Len
    def set_Header_Ext_Len(self, Header_Ext_Len): self.Header_Ext_Len = Header_Ext_Len
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Security_Parameters_Index(self): return self.Security_Parameters_Index
    def set_Security_Parameters_Index(self, Security_Parameters_Index): self.Security_Parameters_Index = Security_Parameters_Index
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def get_Authentication_Data(self): return self.Authentication_Data
    def set_Authentication_Data(self, Authentication_Data): self.Authentication_Data = Authentication_Data
    def hasContent_(self):
        if (
            self.Next_Header is not None or
            self.Header_Ext_Len is not None or
            self.Security_Parameters_Index is not None or
            self.Sequence_Number is not None or
            self.Authentication_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='AuthenticationHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AuthenticationHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='AuthenticationHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='AuthenticationHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Header_Ext_Len is not None:
            self.Header_Ext_Len.export(lwrite, level, 'PacketObj:', name_='Header_Ext_Len', pretty_print=pretty_print)
        if self.Security_Parameters_Index is not None:
            self.Security_Parameters_Index.export(lwrite, level, 'PacketObj:', name_='Security_Parameters_Index', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'PacketObj:', name_='Sequence_Number', pretty_print=pretty_print)
        if self.Authentication_Data is not None:
            self.Authentication_Data.export(lwrite, level, 'PacketObj:', name_='Authentication_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Header_Ext_Len':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Header_Ext_Len(obj_)
        elif nodeName_ == 'Security_Parameters_Index':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_Parameters_Index(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
        elif nodeName_ == 'Authentication_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Authentication_Data(obj_)
# end class AuthenticationHeaderType

class EncapsulatingSecurityPayloadType(GeneratedsSuper):
    """ESP is used to provide confidentiality, data origin authentication,
    connectionless integrity, an anti-replay service (a form of
    partial sequence integrity), and limited traffic flow
    confidentiality. http://www.ietf.org/rfc/rfc2406.txt"""

    subclass = None
    superclass = None
    def __init__(self, Security_Parameters_Index=None, Sequence_Number=None, Payload_Data=None, Padding=None, Padding_Len=None, Next_Header=None, Authentication_Data=None):
        self.Security_Parameters_Index = Security_Parameters_Index
        self.Sequence_Number = Sequence_Number
        self.Payload_Data = Payload_Data
        self.Padding = Padding
        self.Padding_Len = Padding_Len
        self.Next_Header = Next_Header
        self.Authentication_Data = Authentication_Data
    def factory(*args_, **kwargs_):
        if EncapsulatingSecurityPayloadType.subclass:
            return EncapsulatingSecurityPayloadType.subclass(*args_, **kwargs_)
        else:
            return EncapsulatingSecurityPayloadType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Security_Parameters_Index(self): return self.Security_Parameters_Index
    def set_Security_Parameters_Index(self, Security_Parameters_Index): self.Security_Parameters_Index = Security_Parameters_Index
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def get_Payload_Data(self): return self.Payload_Data
    def set_Payload_Data(self, Payload_Data): self.Payload_Data = Payload_Data
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def get_Padding_Len(self): return self.Padding_Len
    def set_Padding_Len(self, Padding_Len): self.Padding_Len = Padding_Len
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_Authentication_Data(self): return self.Authentication_Data
    def set_Authentication_Data(self, Authentication_Data): self.Authentication_Data = Authentication_Data
    def hasContent_(self):
        if (
            self.Security_Parameters_Index is not None or
            self.Sequence_Number is not None or
            self.Payload_Data is not None or
            self.Padding is not None or
            self.Padding_Len is not None or
            self.Next_Header is not None or
            self.Authentication_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='EncapsulatingSecurityPayloadType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EncapsulatingSecurityPayloadType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='EncapsulatingSecurityPayloadType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='EncapsulatingSecurityPayloadType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Security_Parameters_Index is not None:
            self.Security_Parameters_Index.export(lwrite, level, 'PacketObj:', name_='Security_Parameters_Index', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'PacketObj:', name_='Sequence_Number', pretty_print=pretty_print)
        if self.Payload_Data is not None:
            self.Payload_Data.export(lwrite, level, 'PacketObj:', name_='Payload_Data', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'PacketObj:', name_='Padding', pretty_print=pretty_print)
        if self.Padding_Len is not None:
            self.Padding_Len.export(lwrite, level, 'PacketObj:', name_='Padding_Len', pretty_print=pretty_print)
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Authentication_Data is not None:
            self.Authentication_Data.export(lwrite, level, 'PacketObj:', name_='Authentication_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Security_Parameters_Index':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_Parameters_Index(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
        elif nodeName_ == 'Payload_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Payload_Data(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
        elif nodeName_ == 'Padding_Len':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding_Len(obj_)
        elif nodeName_ == 'Next_Header':
            obj_ = IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Authentication_Data':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Authentication_Data(obj_)
# end class EncapsulatingSecurityPayloadType

class Pad1Type(GeneratedsSuper):
    """The Pad1 type specifies how one octet of padding is inserted into
    the Options area of a header. The Pad1 option type does not have
    length and value fields."""

    subclass = None
    superclass = None
    def __init__(self, Octet=None):
        self.Octet = Octet
    def factory(*args_, **kwargs_):
        if Pad1Type.subclass:
            return Pad1Type.subclass(*args_, **kwargs_)
        else:
            return Pad1Type(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Octet(self): return self.Octet
    def set_Octet(self, Octet): self.Octet = Octet
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Octet is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='Pad1Type', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Pad1Type')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='Pad1Type'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='Pad1Type', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Octet is not None:
            self.Octet.export(lwrite, level, 'PacketObj:', name_='Octet', pretty_print=pretty_print)
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
        if nodeName_ == 'Octet':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Octet(obj_)
# end class Pad1Type

class PadNType(GeneratedsSuper):
    """The PadN type specifies how two or more octets of padding are
    inserted into the Options area of a header."""

    subclass = None
    superclass = None
    def __init__(self, Octet=None, Option_Data_Length=None, Option_Data=None):
        self.Octet = Octet
        self.Option_Data_Length = Option_Data_Length
        self.Option_Data = Option_Data
    def factory(*args_, **kwargs_):
        if PadNType.subclass:
            return PadNType.subclass(*args_, **kwargs_)
        else:
            return PadNType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Octet(self): return self.Octet
    def set_Octet(self, Octet): self.Octet = Octet
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Option_Data_Length(self): return self.Option_Data_Length
    def set_Option_Data_Length(self, Option_Data_Length): self.Option_Data_Length = Option_Data_Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Option_Data(self): return self.Option_Data
    def set_Option_Data(self, Option_Data): self.Option_Data = Option_Data
    def hasContent_(self):
        if (
            self.Octet is not None or
            self.Option_Data_Length is not None or
            self.Option_Data is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='PadNType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PadNType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='PadNType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='PadNType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Octet is not None:
            self.Octet.export(lwrite, level, 'PacketObj:', name_='Octet', pretty_print=pretty_print)
        if self.Option_Data_Length is not None:
            self.Option_Data_Length.export(lwrite, level, 'PacketObj:', name_='Option_Data_Length', pretty_print=pretty_print)
        if self.Option_Data is not None:
            self.Option_Data.export(lwrite, level, 'PacketObj:', name_='Option_Data', pretty_print=pretty_print)
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
        if nodeName_ == 'Octet':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Octet(obj_)
        elif nodeName_ == 'Option_Data_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Data_Length(obj_)
        elif nodeName_ == 'Option_Data':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Data(obj_)
# end class PadNType

class FragmentHeaderType(GeneratedsSuper):
    """Each fragment has a header containing next header information, the
    offset of the fragment, an M flag specifying whether or not it
    is the last fragment, and an identification value."""

    subclass = None
    superclass = None
    def __init__(self, Next_Header=None, Fragment_Offset=None, M_Flag=None, Identification=None):
        self.Next_Header = Next_Header
        self.Fragment_Offset = Fragment_Offset
        self.M_Flag = M_Flag
        self.Identification = Identification
    def factory(*args_, **kwargs_):
        if FragmentHeaderType.subclass:
            return FragmentHeaderType.subclass(*args_, **kwargs_)
        else:
            return FragmentHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Next_Header(self): return self.Next_Header
    def set_Next_Header(self, Next_Header): self.Next_Header = Next_Header
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Fragment_Offset(self): return self.Fragment_Offset
    def set_Fragment_Offset(self, Fragment_Offset): self.Fragment_Offset = Fragment_Offset
    def get_M_Flag(self): return self.M_Flag
    def set_M_Flag(self, M_Flag): self.M_Flag = M_Flag
    def validate_MFlagType(self, value):
        # Validate type MFlagType, a restriction on None.
        pass
    def get_Identification(self): return self.Identification
    def set_Identification(self, Identification): self.Identification = Identification
    def hasContent_(self):
        if (
            self.Next_Header is not None or
            self.Fragment_Offset is not None or
            self.M_Flag is not None or
            self.Identification is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='FragmentHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FragmentHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='FragmentHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='FragmentHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Next_Header is not None:
            self.Next_Header.export(lwrite, level, 'PacketObj:', name_='Next_Header', pretty_print=pretty_print)
        if self.Fragment_Offset is not None:
            self.Fragment_Offset.export(lwrite, level, 'PacketObj:', name_='Fragment_Offset', pretty_print=pretty_print)
        if self.M_Flag is not None:
            self.M_Flag.export(lwrite, level, 'PacketObj:', name_='M_Flag', pretty_print=pretty_print)
        if self.Identification is not None:
            self.Identification.export(lwrite, level, 'PacketObj:', name_='Identification', pretty_print=pretty_print)
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
        if nodeName_ == 'Next_Header':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Next_Header(obj_)
        elif nodeName_ == 'Fragment_Offset':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Fragment_Offset(obj_)
        elif nodeName_ == 'M_Flag':
            obj_ = MFlagType.factory()
            obj_.build(child_)
            self.set_M_Flag(obj_)
        elif nodeName_ == 'Identification':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Identification(obj_)
# end class FragmentHeaderType

class MFlagType(cybox_common.BaseObjectPropertyType):
    """MFlagType specifies whether there are more fragments, via a union of
    the MFlagTypeEnum type and the atomic xs:string type. Its base
    type is the cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(MFlagType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if MFlagType.subclass:
            return MFlagType.subclass(*args_, **kwargs_)
        else:
            return MFlagType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(MFlagType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='MFlagType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MFlagType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='MFlagType'):
        super(MFlagType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MFlagType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='MFlagType', fromsubclass_=False, pretty_print=True):
        super(MFlagType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(MFlagType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MFlagType

class IANAPortNumberRegistryType(cybox_common.BaseObjectPropertyType):
    """IANAPortNumberRegistryType specifies port numbers, via a union of
    the IANAPortNumberRegistryTypeEnum type and the atomic xs:string
    type. Its base type is the cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IANAPortNumberRegistryType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IANAPortNumberRegistryType.subclass:
            return IANAPortNumberRegistryType.subclass(*args_, **kwargs_)
        else:
            return IANAPortNumberRegistryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IANAPortNumberRegistryType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IANAPortNumberRegistryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAPortNumberRegistryType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IANAPortNumberRegistryType'):
        super(IANAPortNumberRegistryType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAPortNumberRegistryType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IANAPortNumberRegistryType', fromsubclass_=False, pretty_print=True):
        super(IANAPortNumberRegistryType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IANAPortNumberRegistryType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IANAPortNumberRegistryType

class IANAAssignedIPNumbersType(cybox_common.BaseObjectPropertyType):
    """IANAAssignedIPNumbersType specifies Internet Protocol numbers, via a
    union of the IANAAssignedIPNumbersTypeEnum type and the atomic
    xs:string type. Its base type is the cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(IANAAssignedIPNumbersType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IANAAssignedIPNumbersType.subclass:
            return IANAAssignedIPNumbersType.subclass(*args_, **kwargs_)
        else:
            return IANAAssignedIPNumbersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IANAAssignedIPNumbersType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IANAAssignedIPNumbersType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAAssignedIPNumbersType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IANAAssignedIPNumbersType'):
        super(IANAAssignedIPNumbersType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAAssignedIPNumbersType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IANAAssignedIPNumbersType', fromsubclass_=False, pretty_print=True):
        super(IANAAssignedIPNumbersType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IANAAssignedIPNumbersType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IANAAssignedIPNumbersType

class IANAEtherType(cybox_common.BaseObjectPropertyType):
    """EtherObjectType specifies "type" field of Ethernets, via a union of
    the IANAEtherTypeEnum type and the atomic xs:string type. Its
    base type is the cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IANAEtherType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IANAEtherType.subclass:
            return IANAEtherType.subclass(*args_, **kwargs_)
        else:
            return IANAEtherType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IANAEtherType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IANAEtherType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAEtherType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IANAEtherType'):
        super(IANAEtherType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAEtherType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IANAEtherType', fromsubclass_=False, pretty_print=True):
        super(IANAEtherType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IANAEtherType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IANAEtherType

class IANAHardwareType(cybox_common.BaseObjectPropertyType):
    """IANAHardwareType specifies the type of hardware, via a union of the
    IANAHardwareTypeEnum type and the atomic xs:string type. Its
    base type is the cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IANAHardwareType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IANAHardwareType.subclass:
            return IANAHardwareType.subclass(*args_, **kwargs_)
        else:
            return IANAHardwareType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IANAHardwareType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IANAHardwareType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAHardwareType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IANAHardwareType'):
        super(IANAHardwareType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IANAHardwareType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IANAHardwareType', fromsubclass_=False, pretty_print=True):
        super(IANAHardwareType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IANAHardwareType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IANAHardwareType

class IPVersionType(cybox_common.BaseObjectPropertyType):
    """IPVersionType specifies IP versions, via a union of the
    IPVersionTypeEnum type and the atomic xs:string type. See
    http://www.iana.org/assignments/version-numbers/version-
    numbers.xml for a complete list. Its base type is the
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPVersionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPVersionType.subclass:
            return IPVersionType.subclass(*args_, **kwargs_)
        else:
            return IPVersionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPVersionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPVersionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPVersionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPVersionType'):
        super(IPVersionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPVersionType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPVersionType', fromsubclass_=False, pretty_print=True):
        super(IPVersionType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPVersionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPVersionType

class IPv6PacketChangeType(cybox_common.BaseObjectPropertyType):
    """IPV6PacketChangeType specifies whether a packet has changed, via a
    union of the IPv6PacketChangeTypeEnum type and the atomic
    xs:string type. Its base type is the cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPv6PacketChangeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPv6PacketChangeType.subclass:
            return IPv6PacketChangeType.subclass(*args_, **kwargs_)
        else:
            return IPv6PacketChangeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPv6PacketChangeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6PacketChangeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6PacketChangeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6PacketChangeType'):
        super(IPv6PacketChangeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6PacketChangeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6PacketChangeType', fromsubclass_=False, pretty_print=True):
        super(IPv6PacketChangeType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPv6PacketChangeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPv6PacketChangeType

class IPv6DoNotRecogActionType(cybox_common.BaseObjectPropertyType):
    """IPv6DoNotRecogActionType specifies possible actions when option is
    not recognized, via a union of the IPv6DoNotRecogActionTypeEnum
    type and the atomic xs:string type. Its base type is the
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPv6DoNotRecogActionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPv6DoNotRecogActionType.subclass:
            return IPv6DoNotRecogActionType.subclass(*args_, **kwargs_)
        else:
            return IPv6DoNotRecogActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPv6DoNotRecogActionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv6DoNotRecogActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6DoNotRecogActionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv6DoNotRecogActionType'):
        super(IPv6DoNotRecogActionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv6DoNotRecogActionType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv6DoNotRecogActionType', fromsubclass_=False, pretty_print=True):
        super(IPv6DoNotRecogActionType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPv6DoNotRecogActionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPv6DoNotRecogActionType

class IPv4OptionsType(cybox_common.BaseObjectPropertyType):
    """IPv4OptionsType specifies IPv4 options, via a union of the
    IPv4OptionsTypeEnum type and the atomic xs:string type. Its base
    type is the cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPv4OptionsType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPv4OptionsType.subclass:
            return IPv4OptionsType.subclass(*args_, **kwargs_)
        else:
            return IPv4OptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPv4OptionsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4OptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4OptionsType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4OptionsType'):
        super(IPv4OptionsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4OptionsType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4OptionsType', fromsubclass_=False, pretty_print=True):
        super(IPv4OptionsType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPv4OptionsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPv4OptionsType

class IPv4ClassType(cybox_common.BaseObjectPropertyType):
    """IPv4ClassType specifies IPv4 class type, via a union of the
    IPv4ClassTypeEnum type and the atomic xs:string type. Its base
    type is the cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPv4ClassType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPv4ClassType.subclass:
            return IPv4ClassType.subclass(*args_, **kwargs_)
        else:
            return IPv4ClassType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPv4ClassType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4ClassType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4ClassType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4ClassType'):
        super(IPv4ClassType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4ClassType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4ClassType', fromsubclass_=False, pretty_print=True):
        super(IPv4ClassType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPv4ClassType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPv4ClassType

class IPv4CopyFlagType(cybox_common.BaseObjectPropertyType):
    """IPv4CopyFlagType specifies value of IPv4 copy flag, via a union of
    the IPv4CopyFlagTypeEnum type and the atomic xs:string type. Its
    base type is the cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(IPv4CopyFlagType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if IPv4CopyFlagType.subclass:
            return IPv4CopyFlagType.subclass(*args_, **kwargs_)
        else:
            return IPv4CopyFlagType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(IPv4CopyFlagType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='IPv4CopyFlagType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4CopyFlagType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='IPv4CopyFlagType'):
        super(IPv4CopyFlagType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='IPv4CopyFlagType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='IPv4CopyFlagType', fromsubclass_=False, pretty_print=True):
        super(IPv4CopyFlagType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(IPv4CopyFlagType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IPv4CopyFlagType

class MoreFragmentsType(cybox_common.BaseObjectPropertyType):
    """MoreFragmentsType specifies whether there are more fragments, via a
    union of the MoreFragmentsTypeEnum type and the atomic xs:string
    type. Its base type is the cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(MoreFragmentsType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if MoreFragmentsType.subclass:
            return MoreFragmentsType.subclass(*args_, **kwargs_)
        else:
            return MoreFragmentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(MoreFragmentsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='MoreFragmentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MoreFragmentsType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='MoreFragmentsType'):
        super(MoreFragmentsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MoreFragmentsType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='MoreFragmentsType', fromsubclass_=False, pretty_print=True):
        super(MoreFragmentsType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(MoreFragmentsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MoreFragmentsType

class DoNotFragmentType(cybox_common.BaseObjectPropertyType):
    """DoNotFragmentType specifies fragmenting options, via a union of the
    DoNotFragmentTypeEnum type and the atomic xs:string type. Its
    base type is the cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        # PROP: This is a BaseObjectPropertyType subclass
        super(DoNotFragmentType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DoNotFragmentType.subclass:
            return DoNotFragmentType.subclass(*args_, **kwargs_)
        else:
            return DoNotFragmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DoNotFragmentType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='DoNotFragmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DoNotFragmentType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='DoNotFragmentType'):
        super(DoNotFragmentType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DoNotFragmentType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='DoNotFragmentType', fromsubclass_=False, pretty_print=True):
        super(DoNotFragmentType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(DoNotFragmentType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DoNotFragmentType

class ARPOpType(cybox_common.BaseObjectPropertyType):
    """ARPOpType specifies types of ARP operations, via a union of the
    ARPOpTypeEnum type and the atomic xs:string type. Its base type
    is the cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ARPOpType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ARPOpType.subclass:
            return ARPOpType.subclass(*args_, **kwargs_)
        else:
            return ARPOpType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ARPOpType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='ARPOpType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPOpType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='ARPOpType'):
        super(ARPOpType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ARPOpType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='ARPOpType', fromsubclass_=False, pretty_print=True):
        super(ARPOpType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
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
        super(ARPOpType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ARPOpType

class NetworkPacketObjectType(cybox_common.ObjectPropertiesType):
    """The NetworkPacketObjectType's definition of a network packet is
    based on the TCP/IP model/Internet protocol suite. In the TCP/IP
    stack, "packet" is generally defined as IP header plus payload,
    but we also include the LinkLayer from the OSI model, which
    defines the physical network interfaces and routing protocols.
    Protocol fields are provided but requirements are not
    enforced/captured; all fields are optional."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Link_Layer=None, Internet_Layer=None, Transport_Layer=None):
        super(NetworkPacketObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Link_Layer = Link_Layer
        self.Internet_Layer = Internet_Layer
        self.Transport_Layer = Transport_Layer
    def factory(*args_, **kwargs_):
        if NetworkPacketObjectType.subclass:
            return NetworkPacketObjectType.subclass(*args_, **kwargs_)
        else:
            return NetworkPacketObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Link_Layer(self): return self.Link_Layer
    def set_Link_Layer(self, Link_Layer): self.Link_Layer = Link_Layer
    def get_Internet_Layer(self): return self.Internet_Layer
    def set_Internet_Layer(self, Internet_Layer): self.Internet_Layer = Internet_Layer
    def get_Transport_Layer(self): return self.Transport_Layer
    def set_Transport_Layer(self, Transport_Layer): self.Transport_Layer = Transport_Layer
    def hasContent_(self):
        if (
            self.Link_Layer is not None or
            self.Internet_Layer is not None or
            self.Transport_Layer is not None or
            super(NetworkPacketObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='PacketObj:', name_='NetworkPacketObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkPacketObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='PacketObj:', name_='NetworkPacketObjectType'):
        super(NetworkPacketObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkPacketObjectType')
    def exportChildren(self, lwrite, level, namespace_='PacketObj:', name_='NetworkPacketObjectType', fromsubclass_=False, pretty_print=True):
        super(NetworkPacketObjectType, self).exportChildren(lwrite, level, 'PacketObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Link_Layer is not None:
            self.Link_Layer.export(lwrite, level, 'PacketObj:', name_='Link_Layer', pretty_print=pretty_print)
        if self.Internet_Layer is not None:
            self.Internet_Layer.export(lwrite, level, 'PacketObj:', name_='Internet_Layer', pretty_print=pretty_print)
        if self.Transport_Layer is not None:
            self.Transport_Layer.export(lwrite, level, 'PacketObj:', name_='Transport_Layer', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(NetworkPacketObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Link_Layer':
            obj_ = LinkLayerType.factory()
            obj_.build(child_)
            self.set_Link_Layer(obj_)
        elif nodeName_ == 'Internet_Layer':
            obj_ = InternetLayerType.factory()
            obj_.build(child_)
            self.set_Internet_Layer(obj_)
        elif nodeName_ == 'Transport_Layer':
            obj_ = TransportLayerType.factory()
            obj_.build(child_)
            self.set_Transport_Layer(obj_)
        super(NetworkPacketObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkPacketObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Invoking_Packet': cybox_common.HexBinaryObjectPropertyType,
    'Errors': cybox_common.ErrorsType,
    'Recip_Hardware_Addr': address_object.AddressObjectType,
    'IP_Addr_Prefix': address_object.AddressObjectType,
    'Destination_MAC_Addr': address_object.AddressObjectType,
    'Cur_Hop_Limit': cybox_common.IntegerObjectPropertyType,
    'Option_Data': cybox_common.IntegerObjectPropertyType,
    'Preferred_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Src_IPv6_Addr': address_object.AddressObjectType,
    'Src_IPv4_Addr': address_object.AddressObjectType,
    'Metadata': cybox_common.MetadataType,
    'Src_Port': port_object.PortObjectType,
    'Address': address_object.AddressObjectType,
    'Dest_IPv4_Addr': address_object.AddressObjectType,
    'Transmit_Timestamp': cybox_common.UnsignedIntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'String': cybox_common.ExtractedStringType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Security_Parameters_Index': cybox_common.HexBinaryObjectPropertyType,
    'IPHeader_And_Data': cybox_common.HexBinaryObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Target_IPv6_Addr': address_object.AddressObjectType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Checksum': cybox_common.HexBinaryObjectPropertyType,
    'Address_Mask': address_object.AddressObjectType,
    'DSCP': cybox_common.HexBinaryObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Code': cybox_common.HexBinaryObjectPropertyType,
    'Next_Header': cybox_common.HexBinaryObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Header_Length': cybox_common.IntegerObjectPropertyType,
    'Seq_Num': cybox_common.HexBinaryObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Padding_Len': cybox_common.HexBinaryObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Fragment_Offset': cybox_common.HexBinaryObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Segments': cybox_common.HashSegmentsType,
    'Layer4_Protocol': port_object.Layer4ProtocolType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Octet': cybox_common.HexBinaryObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Link_Layer_MAC_Addr': address_object.AddressObjectType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Tool': cybox_common.ToolInformationType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Reachable_Time': cybox_common.IntegerObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.PositiveIntegerObjectPropertyType,
    'Proto_Addr_Size': cybox_common.HexBinaryObjectPropertyType,
    'IP_Address': address_object.AddressObjectType,
    'Sequence_Number': cybox_common.HexBinaryObjectPropertyType,
    'Option_Data_Length': cybox_common.IntegerObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Urg_Ptr': cybox_common.HexBinaryObjectPropertyType,
    'Option_Data_Len': cybox_common.HexBinaryObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Router_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Option_Byte': cybox_common.HexBinaryObjectPropertyType,
    'Data_Offset': cybox_common.HexBinaryObjectPropertyType,
    'Hash': cybox_common.HashType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Options': cybox_common.HexBinaryObjectPropertyType,
    'Output_Link_MTU': cybox_common.HexBinaryObjectPropertyType,
    'IPv6_Addr': address_object.AddressObjectType,
    'Dest_IPv6_Addr': address_object.AddressObjectType,
    'Payload_Length': cybox_common.HexBinaryObjectPropertyType,
    'Output_Link_Speed': cybox_common.HexBinaryObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Flow_Label': cybox_common.HexBinaryObjectPropertyType,
    'Total_Length': cybox_common.HexBinaryObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Pointer': cybox_common.HexBinaryObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Port': port_object.PortObjectType,
    'Contributor': cybox_common.ContributorType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Identification': cybox_common.HexBinaryObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'ECN': cybox_common.HexBinaryObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'SrcPort': port_object.PortObjectType,
    'Strings': cybox_common.ExtractedStringsType,
    'Padding': cybox_common.HexBinaryObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Prefix_Length': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Data': cybox_common.HexBinaryObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'ACK_Num': cybox_common.HexBinaryObjectPropertyType,
    'First_Eight_Bytes': cybox_common.HexBinaryObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Hardware_Addr_Size': cybox_common.HexBinaryObjectPropertyType,
    'Source_MAC_Addr': address_object.AddressObjectType,
    'Next_Hop_MTU': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Outbound_Hop_Count': cybox_common.HexBinaryObjectPropertyType,
    'Traffic_Class': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Build_Information': cybox_common.BuildInformationType,
    'References': cybox_common.ToolReferencesType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Retrans_Timer': cybox_common.IntegerObjectPropertyType,
    'Window': cybox_common.HexBinaryObjectPropertyType,
    'Sender_Protocol_Addr': address_object.AddressObjectType,
    'Segments_Left': cybox_common.IntegerObjectPropertyType,
    'DestPort': port_object.PortObjectType,
    'Dest_Port': port_object.PortObjectType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Sender_Hardware_Addr': address_object.AddressObjectType,
    'Routing_Type': cybox_common.HexBinaryObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Error': cybox_common.ErrorType,
    'Originate_Timestamp': cybox_common.UnsignedIntegerObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Valid_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Receive_Timestamp': cybox_common.UnsignedIntegerObjectPropertyType,
    'MTU': cybox_common.HexBinaryObjectPropertyType,
    'Header_Ext_Len': cybox_common.HexBinaryObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Type_Specific_Data': cybox_common.StringObjectPropertyType,
    'Recip_Protocol_Addr': address_object.AddressObjectType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Return_Hop_Count': cybox_common.HexBinaryObjectPropertyType,
    'Reserved': cybox_common.HexBinaryObjectPropertyType,
    'Payload_Data': cybox_common.HexBinaryObjectPropertyType,
    'Dependency': cybox_common.DependencyType,
    'Tools': cybox_common.ToolsInformationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Fragment': cybox_common.HexBinaryObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Authentication_Data': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
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
        rootTag = 'Network_Packet'
        rootClass = NetworkPacketObjectType
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
        rootTag = 'Network_Packet'
        rootClass = NetworkPacketObjectType
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
        rootTag = 'Network_Packet'
        rootClass = NetworkPacketObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Packet",
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
    "NetworkPacketObjectType",
    "LinkLayerType",
    "PhysicalInterfaceType",
    "LogicalProtocolType",
    "EthernetInterfaceType",
    "EthernetHeaderType",
    "TypeLengthType",
    "ARPType",
    "ARPOpType",
    "NDPType",
    "RouterSolicitationType",
    "RouterSolicitationOptionsType",
    "RouterAdvertisementType",
    "RouterAdvertisementOptionsType",
    "NeighborSolicitationType",
    "NeighborSolicitationOptionsType",
    "NeighborAdvertisementType",
    "NeighborOptionsType",
    "RedirectType",
    "RedirectOptionsType",
    "NDPLinkAddrType",
    "NDPPrefixInfoType",
    "NDPRedirectedHeaderType",
    "NDPMTUType",
    "InternetLayerType",
    "IPv4PacketType",
    "IPv4HeaderType",
    "IPv4FlagsType",
    "DoNotFragmentType",
    "MoreFragmentsType",
    "IPv4OptionType",
    "IPv4CopyFlagType",
    "IPv4ClassType",
    "IPv4OptionsType",
    "IPv6PacketType",
    "IPv6HeaderType",
    "IPv6ExtHeaderType",
    "IPv6DoNotRecogActionType",
    "IPv6PacketChangeType",
    "IPv6OptionType",
    "IPVersionType",
    "TransportLayerType",
    "TCPType",
    "UDPType",
    "TCPHeaderType",
    "TCPFlagsType",
    "UDPHeaderType",
    "IANAHardwareType",
    "IANAEtherType",
    "IANAAssignedIPNumbersType",
    "IANAPortNumberRegistryType",
    "ICMPv4PacketType",
    "ICMPv4HeaderType",
    "ICMPv4ErrorMessageType",
    "ICMPv4ErrorMessageContentType",
    "ICMPv4InfoMessageType",
    "ICMPv4InfoMessageContentType",
    "ICMPv4TracerouteType",
    "ICMPv6PacketType",
    "ICMPv6HeaderType",
    "ICMPv6ErrorMessageType",
    "ICMPv6InfoMessageType",
    "ICMPv6InfoMessageContentType",
    "ICMPv4EchoReplyType",
    "ICMPv4DestinationUnreachableType",
    "FragmentationRequiredType",
    "ICMPv4SourceQuenchType",
    "ICMPv4RedirectMessageType",
    "ICMPv4EchoRequestType",
    "ICMPv4TimeExceededType",
    "ICMPv4TimestampRequestType",
    "ICMPv4TimestampReplyType",
    "ICMPv4AddressMaskRequestType",
    "ICMPv4AddressMaskReplyType",
    "ICMPv6DestinationUnreachableType",
    "ICMPv6PacketTooBigType",
    "ICMPv6TimeExceededType",
    "ICMPv6ParameterProblemType",
    "ICMPv6EchoRequestType",
    "ICMPv6EchoReplyType",
    "PrefixType",
    "HopByHopOptionsType",
    "OptionDataType",
    "RoutingType",
    "FragmentType",
    "DestinationOptionsType",
    "AuthenticationHeaderType",
    "EncapsulatingSecurityPayloadType",
    "Pad1Type",
    "PadNType",
    "FragmentHeaderType",
    "MFlagType"
    ]
