# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from cybox.bindings import *
from . import cybox_common
from . import address_object
from . import network_packet_object
from . import socket_address_object


class NetworkLayerInfoType(GeneratedsSuper):
    """Network layer information (relative to the OSI network model) which
    is typically captured in all types of network flow records."""

    subclass = None
    superclass = None
    def __init__(self, Src_Socket_Address=None, Dest_Socket_Address=None, IP_Protocol=None, extensiontype_=None):
        self.Src_Socket_Address = Src_Socket_Address
        self.Dest_Socket_Address = Dest_Socket_Address
        self.IP_Protocol = IP_Protocol
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if NetworkLayerInfoType.subclass:
            return NetworkLayerInfoType.subclass(*args_, **kwargs_)
        else:
            return NetworkLayerInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Src_Socket_Address(self): return self.Src_Socket_Address
    def set_Src_Socket_Address(self, Src_Socket_Address): self.Src_Socket_Address = Src_Socket_Address
    def get_Dest_Socket_Address(self): return self.Dest_Socket_Address
    def set_Dest_Socket_Address(self, Dest_Socket_Address): self.Dest_Socket_Address = Dest_Socket_Address
    def get_IP_Protocol(self): return self.IP_Protocol
    def set_IP_Protocol(self, IP_Protocol): self.IP_Protocol = IP_Protocol
    def validate_IANAAssignedIPNumbersType(self, value):
        # Validate type network_packet_object.IANAAssignedIPNumbersType, a restriction on None.
        pass
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.Src_Socket_Address is not None or
            self.Dest_Socket_Address is not None or
            self.IP_Protocol is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkLayerInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkLayerInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetworkLayerInfoType'):
        if self.extensiontype_ is not None:

            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkLayerInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Src_Socket_Address is not None:
            self.Src_Socket_Address.export(lwrite, level, 'NetFlowObj:', name_='Src_Socket_Address', pretty_print=pretty_print)
        if self.Dest_Socket_Address is not None:
            self.Dest_Socket_Address.export(lwrite, level, 'NetFlowObj:', name_='Dest_Socket_Address', pretty_print=pretty_print)
        if self.IP_Protocol is not None:
            self.IP_Protocol.export(lwrite, level, 'NetFlowObj:', name_='IP_Protocol', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None:

            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Src_Socket_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Src_Socket_Address(obj_)
        elif nodeName_ == 'Dest_Socket_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Dest_Socket_Address(obj_)
        elif nodeName_ == 'IP_Protocol':
            obj_ = network_packet_object.IANAAssignedIPNumbersType.factory()
            obj_.build(child_)
            self.set_IP_Protocol(obj_)
# end class NetworkLayerInfoType

class NetworkFlowLabelType(NetworkLayerInfoType):
    """The NetworkFlowLabelType contains elements that are common to all
    flow record formats. It builds off of network layer information
    (a 5-tuple that commonly defines a flow) and includes ingress
    and egress interface indexes and IP protocol information (not
    present if all flow record formats). Egress information is
    usually not thought of as part of the extended 7-tuple, but we
    include it for organizational purposes. Because these fields are
    defined here, they are excluded from the fields associated
    directly with each different flow record format type."""

    subclass = None
    superclass = NetworkLayerInfoType
    def __init__(self, Src_Socket_Address=None, Dest_Socket_Address=None, IP_Protocol=None, Ingress_Interface_Index=None, Egress_Interface_Index=None, IP_Type_Of_Service=None):
        super(NetworkFlowLabelType, self).__init__(Src_Socket_Address, Dest_Socket_Address, IP_Protocol, )
        self.Ingress_Interface_Index = Ingress_Interface_Index
        self.Egress_Interface_Index = Egress_Interface_Index
        self.IP_Type_Of_Service = IP_Type_Of_Service
    def factory(*args_, **kwargs_):
        if NetworkFlowLabelType.subclass:
            return NetworkFlowLabelType.subclass(*args_, **kwargs_)
        else:
            return NetworkFlowLabelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Ingress_Interface_Index(self): return self.Ingress_Interface_Index
    def set_Ingress_Interface_Index(self, Ingress_Interface_Index): self.Ingress_Interface_Index = Ingress_Interface_Index
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Egress_Interface_Index(self): return self.Egress_Interface_Index
    def set_Egress_Interface_Index(self, Egress_Interface_Index): self.Egress_Interface_Index = Egress_Interface_Index
    def get_IP_Type_Of_Service(self): return self.IP_Type_Of_Service
    def set_IP_Type_Of_Service(self, IP_Type_Of_Service): self.IP_Type_Of_Service = IP_Type_Of_Service
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Ingress_Interface_Index is not None or
            self.Egress_Interface_Index is not None or
            self.IP_Type_Of_Service is not None or
            super(NetworkFlowLabelType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkFlowLabelType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkFlowLabelType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetworkFlowLabelType'):
        super(NetworkFlowLabelType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkFlowLabelType')
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkFlowLabelType', fromsubclass_=False, pretty_print=True):
        super(NetworkFlowLabelType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Ingress_Interface_Index is not None:
            self.Ingress_Interface_Index.export(lwrite, level, 'NetFlowObj:', name_='Ingress_Interface_Index', pretty_print=pretty_print)
        if self.Egress_Interface_Index is not None:
            self.Egress_Interface_Index.export(lwrite, level, 'NetFlowObj:', name_='Egress_Interface_Index', pretty_print=pretty_print)
        if self.IP_Type_Of_Service is not None:
            self.IP_Type_Of_Service.export(lwrite, level, 'NetFlowObj:', name_='IP_Type_Of_Service', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(NetworkFlowLabelType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Ingress_Interface_Index':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Ingress_Interface_Index(obj_)
        elif nodeName_ == 'Egress_Interface_Index':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Egress_Interface_Index(obj_)
        elif nodeName_ == 'IP_Type_Of_Service':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IP_Type_Of_Service(obj_)
        super(NetworkFlowLabelType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkFlowLabelType

class UnidirectionalRecordType(GeneratedsSuper):
    """Netflow record formats that capture traffic in one direction."""

    subclass = None
    superclass = None
    def __init__(self, IPFIX_Message=None, NetflowV9_Export_Packet=None, NetflowV5_Packet=None, SiLK_Record=None):
        self.IPFIX_Message = IPFIX_Message
        self.NetflowV9_Export_Packet = NetflowV9_Export_Packet
        self.NetflowV5_Packet = NetflowV5_Packet
        self.SiLK_Record = SiLK_Record
    def factory(*args_, **kwargs_):
        if UnidirectionalRecordType.subclass:
            return UnidirectionalRecordType.subclass(*args_, **kwargs_)
        else:
            return UnidirectionalRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IPFIX_Message(self): return self.IPFIX_Message
    def set_IPFIX_Message(self, IPFIX_Message): self.IPFIX_Message = IPFIX_Message
    def get_NetflowV9_Export_Packet(self): return self.NetflowV9_Export_Packet
    def set_NetflowV9_Export_Packet(self, NetflowV9_Export_Packet): self.NetflowV9_Export_Packet = NetflowV9_Export_Packet
    def get_NetflowV5_Packet(self): return self.NetflowV5_Packet
    def set_NetflowV5_Packet(self, NetflowV5_Packet): self.NetflowV5_Packet = NetflowV5_Packet
    def get_SiLK_Record(self): return self.SiLK_Record
    def set_SiLK_Record(self, SiLK_Record): self.SiLK_Record = SiLK_Record
    def hasContent_(self):
        if (
            self.IPFIX_Message is not None or
            self.NetflowV9_Export_Packet is not None or
            self.NetflowV5_Packet is not None or
            self.SiLK_Record is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='UnidirectionalRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnidirectionalRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='UnidirectionalRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='UnidirectionalRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IPFIX_Message is not None:
            self.IPFIX_Message.export(lwrite, level, 'NetFlowObj:', name_='IPFIX_Message', pretty_print=pretty_print)
        if self.NetflowV9_Export_Packet is not None:
            self.NetflowV9_Export_Packet.export(lwrite, level, 'NetFlowObj:', name_='NetflowV9_Export_Packet', pretty_print=pretty_print)
        if self.NetflowV5_Packet is not None:
            self.NetflowV5_Packet.export(lwrite, level, 'NetFlowObj:', name_='NetflowV5_Packet', pretty_print=pretty_print)
        if self.SiLK_Record is not None:
            self.SiLK_Record.export(lwrite, level, 'NetFlowObj:', name_='SiLK_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'IPFIX_Message':
            obj_ = IPFIXMessageType.factory()
            obj_.build(child_)
            self.set_IPFIX_Message(obj_)
        elif nodeName_ == 'NetflowV9_Export_Packet':
            obj_ = NetflowV9ExportPacketType.factory()
            obj_.build(child_)
            self.set_NetflowV9_Export_Packet(obj_)
        elif nodeName_ == 'NetflowV5_Packet':
            obj_ = NetflowV5PacketType.factory()
            obj_.build(child_)
            self.set_NetflowV5_Packet(obj_)
        elif nodeName_ == 'SiLK_Record':
            obj_ = SiLKRecordType.factory()
            obj_.build(child_)
            self.set_SiLK_Record(obj_)
# end class UnidirectionalRecordType

class BidirectionalRecordType(GeneratedsSuper):
    """Network record formats that capture traffic in both directions.
    Later, we plan to add Argus as a network flow format type. Argus
    supports bidirectional flows, and as such, is usually used as an
    alternative to NetFlow v5 analysis via SiLK
    (http://www.qosient.com/argus/)."""

    subclass = None
    superclass = None
    def __init__(self, YAF_Record=None):
        self.YAF_Record = YAF_Record
    def factory(*args_, **kwargs_):
        if BidirectionalRecordType.subclass:
            return BidirectionalRecordType.subclass(*args_, **kwargs_)
        else:
            return BidirectionalRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_YAF_Record(self): return self.YAF_Record
    def set_YAF_Record(self, YAF_Record): self.YAF_Record = YAF_Record
    def hasContent_(self):
        if (
            self.YAF_Record is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='BidirectionalRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BidirectionalRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='BidirectionalRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='BidirectionalRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.YAF_Record is not None:
            self.YAF_Record.export(lwrite, level, 'NetFlowObj:', name_='YAF_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'YAF_Record':
            obj_ = YAFRecordType.factory()
            obj_.build(child_)
            self.set_YAF_Record(obj_)
# end class BidirectionalRecordType

class IPFIXMessageType(GeneratedsSuper):
    """The IPFIX protocol provides IP flow information.
    http://tools.ietf.org/html/rfc5101"""

    subclass = None
    superclass = None
    def __init__(self, Message_Header=None, Set=None):
        self.Message_Header = Message_Header
        if Set is None:
            self.Set = []
        else:
            self.Set = Set
    def factory(*args_, **kwargs_):
        if IPFIXMessageType.subclass:
            return IPFIXMessageType.subclass(*args_, **kwargs_)
        else:
            return IPFIXMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Message_Header(self): return self.Message_Header
    def set_Message_Header(self, Message_Header): self.Message_Header = Message_Header
    def get_Set(self): return self.Set
    def set_Set(self, Set): self.Set = Set
    def add_Set(self, value): self.Set.append(value)
    def insert_Set(self, index, value): self.Set[index] = value
    def hasContent_(self):
        if (
            self.Message_Header is not None or
            self.Set
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Message_Header is not None:
            self.Message_Header.export(lwrite, level, 'NetFlowObj:', name_='Message_Header', pretty_print=pretty_print)
        for Set_ in self.Set:
            Set_.export(lwrite, level, 'NetFlowObj:', name_='Set', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Message_Header':
            obj_ = IPFIXMessageHeaderType.factory()
            obj_.build(child_)
            self.set_Message_Header(obj_)
        elif nodeName_ == 'Set':
            obj_ = IPFIXSetType.factory()
            obj_.build(child_)
            self.Set.append(obj_)
# end class IPFIXMessageType

class IPFIXMessageHeaderType(GeneratedsSuper):
    """This type represents the message header for the IPFIX format. For
    more information about each of the fields, please refer to RFC
    5101 (http://tools.ietf.org/html/rfc5101) under the heading,
    "Message Header Field Descriptions." Note that common elements
    are included in the Network_Flow_Label."""

    subclass = None
    superclass = None
    def __init__(self, Version=None, Byte_Length=None, Export_Timestamp=None, Sequence_Number=None, Observation_Domain_ID=None):
        self.Version = Version
        self.Byte_Length = Byte_Length
        self.Export_Timestamp = Export_Timestamp
        self.Sequence_Number = Sequence_Number
        self.Observation_Domain_ID = Observation_Domain_ID
    def factory(*args_, **kwargs_):
        if IPFIXMessageHeaderType.subclass:
            return IPFIXMessageHeaderType.subclass(*args_, **kwargs_)
        else:
            return IPFIXMessageHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Byte_Length(self): return self.Byte_Length
    def set_Byte_Length(self, Byte_Length): self.Byte_Length = Byte_Length
    def get_Export_Timestamp(self): return self.Export_Timestamp
    def set_Export_Timestamp(self, Export_Timestamp): self.Export_Timestamp = Export_Timestamp
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def get_Observation_Domain_ID(self): return self.Observation_Domain_ID
    def set_Observation_Domain_ID(self, Observation_Domain_ID): self.Observation_Domain_ID = Observation_Domain_ID
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Byte_Length is not None or
            self.Export_Timestamp is not None or
            self.Sequence_Number is not None or
            self.Observation_Domain_ID is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXMessageHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXMessageHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXMessageHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXMessageHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            self.Version.export(lwrite, level, 'NetFlowObj:', name_='Version', pretty_print=pretty_print)
        if self.Byte_Length is not None:
            self.Byte_Length.export(lwrite, level, 'NetFlowObj:', name_='Byte_Length', pretty_print=pretty_print)
        if self.Export_Timestamp is not None:
            self.Export_Timestamp.export(lwrite, level, 'NetFlowObj:', name_='Export_Timestamp', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'NetFlowObj:', name_='Sequence_Number', pretty_print=pretty_print)
        if self.Observation_Domain_ID is not None:
            self.Observation_Domain_ID.export(lwrite, level, 'NetFlowObj:', name_='Observation_Domain_ID', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Byte_Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Byte_Length(obj_)
        elif nodeName_ == 'Export_Timestamp':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Export_Timestamp(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
        elif nodeName_ == 'Observation_Domain_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Observation_Domain_ID(obj_)
# end class IPFIXMessageHeaderType

class IPFIXSetType(GeneratedsSuper):
    """Represents the possible sets of records that can be represented in
    an IPFIX message. See RFC 5101 and look for the terms "Template
    Set", "Options Template Set", and "Data Set", for more
    information."""

    subclass = None
    superclass = None
    def __init__(self, Template_Set=None, Options_Template_Set=None, Data_Set=None):
        self.Template_Set = Template_Set
        self.Options_Template_Set = Options_Template_Set
        self.Data_Set = Data_Set
    def factory(*args_, **kwargs_):
        if IPFIXSetType.subclass:
            return IPFIXSetType.subclass(*args_, **kwargs_)
        else:
            return IPFIXSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_Set(self): return self.Template_Set
    def set_Template_Set(self, Template_Set): self.Template_Set = Template_Set
    def get_Options_Template_Set(self): return self.Options_Template_Set
    def set_Options_Template_Set(self, Options_Template_Set): self.Options_Template_Set = Options_Template_Set
    def get_Data_Set(self): return self.Data_Set
    def set_Data_Set(self, Data_Set): self.Data_Set = Data_Set
    def hasContent_(self):
        if (
            self.Template_Set is not None or
            self.Options_Template_Set is not None or
            self.Data_Set is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_Set is not None:
            self.Template_Set.export(lwrite, level, 'NetFlowObj:', name_='Template_Set', pretty_print=pretty_print)
        if self.Options_Template_Set is not None:
            self.Options_Template_Set.export(lwrite, level, 'NetFlowObj:', name_='Options_Template_Set', pretty_print=pretty_print)
        if self.Data_Set is not None:
            self.Data_Set.export(lwrite, level, 'NetFlowObj:', name_='Data_Set', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_Set':
            obj_ = IPFIXTemplateSetType.factory()
            obj_.build(child_)
            self.set_Template_Set(obj_)
        elif nodeName_ == 'Options_Template_Set':
            obj_ = IPFIXOptionsTemplateSetType.factory()
            obj_.build(child_)
            self.set_Options_Template_Set(obj_)
        elif nodeName_ == 'Data_Set':
            obj_ = IPFIXDataSetType.factory()
            obj_.build(child_)
            self.set_Data_Set(obj_)
# end class IPFIXSetType

class IPFIXTemplateSetType(GeneratedsSuper):
    """Specifies the regions of a Template Set, of which there are three:
    the Set Header, the collection of Template Records, and the
    optional padding at the end of the Template Set. See RFC 5101
    under Set Format, which is section 3.3.1, for more information."""

    subclass = None
    superclass = None
    def __init__(self, Set_Header=None, Template_Record=None, Padding=None):
        self.Set_Header = Set_Header
        if Template_Record is None:
            self.Template_Record = []
        else:
            self.Template_Record = Template_Record
        self.Padding = Padding
    def factory(*args_, **kwargs_):
        if IPFIXTemplateSetType.subclass:
            return IPFIXTemplateSetType.subclass(*args_, **kwargs_)
        else:
            return IPFIXTemplateSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Set_Header(self): return self.Set_Header
    def set_Set_Header(self, Set_Header): self.Set_Header = Set_Header
    def get_Template_Record(self): return self.Template_Record
    def set_Template_Record(self, Template_Record): self.Template_Record = Template_Record
    def add_Template_Record(self, value): self.Template_Record.append(value)
    def insert_Template_Record(self, index, value): self.Template_Record[index] = value
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Set_Header is not None or
            self.Template_Record or
            self.Padding is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXTemplateSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXTemplateSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Set_Header is not None:
            self.Set_Header.export(lwrite, level, 'NetFlowObj:', name_='Set_Header', pretty_print=pretty_print)
        for Template_Record_ in self.Template_Record:
            Template_Record_.export(lwrite, level, 'NetFlowObj:', name_='Template_Record', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'NetFlowObj:', name_='Padding', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Set_Header':
            obj_ = IPFIXSetHeaderType.factory()
            obj_.build(child_)
            self.set_Set_Header(obj_)
        elif nodeName_ == 'Template_Record':
            obj_ = IPFIXTemplateRecordType.factory()
            obj_.build(child_)
            self.Template_Record.append(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
# end class IPFIXTemplateSetType

class IPFIXOptionsTemplateSetType(GeneratedsSuper):
    """Specifies the regions of an Options Template Set, of which there are
    three: the Set Header, the collection of Options Template
    Records, and the optional padding at the end of the Options
    Template Set. See RFC 5101 under Set Format, which is section
    3.3.1, for more information."""

    subclass = None
    superclass = None
    def __init__(self, Set_Header=None, Options_Template_Record=None, Padding=None):
        self.Set_Header = Set_Header
        if Options_Template_Record is None:
            self.Options_Template_Record = []
        else:
            self.Options_Template_Record = Options_Template_Record
        self.Padding = Padding
    def factory(*args_, **kwargs_):
        if IPFIXOptionsTemplateSetType.subclass:
            return IPFIXOptionsTemplateSetType.subclass(*args_, **kwargs_)
        else:
            return IPFIXOptionsTemplateSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Set_Header(self): return self.Set_Header
    def set_Set_Header(self, Set_Header): self.Set_Header = Set_Header
    def get_Options_Template_Record(self): return self.Options_Template_Record
    def set_Options_Template_Record(self, Options_Template_Record): self.Options_Template_Record = Options_Template_Record
    def add_Options_Template_Record(self, value): self.Options_Template_Record.append(value)
    def insert_Options_Template_Record(self, index, value): self.Options_Template_Record[index] = value
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Set_Header is not None or
            self.Options_Template_Record or
            self.Padding is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXOptionsTemplateSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Set_Header is not None:
            self.Set_Header.export(lwrite, level, 'NetFlowObj:', name_='Set_Header', pretty_print=pretty_print)
        for Options_Template_Record_ in self.Options_Template_Record:
            Options_Template_Record_.export(lwrite, level, 'NetFlowObj:', name_='Options_Template_Record', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'NetFlowObj:', name_='Padding', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Set_Header':
            obj_ = IPFIXSetHeaderType.factory()
            obj_.build(child_)
            self.set_Set_Header(obj_)
        elif nodeName_ == 'Options_Template_Record':
            obj_ = IPFIXOptionsTemplateRecordType.factory()
            obj_.build(child_)
            self.Options_Template_Record.append(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
# end class IPFIXOptionsTemplateSetType

class IPFIXDataSetType(GeneratedsSuper):
    """Specifies the regions of a Data Set, of which there are three: the
    Set Header, the collection of Data Records, and the optional
    padding at the end of the Data Set. See RFC 5101 under Set
    Format, which is section 3.3.1, for more information."""

    subclass = None
    superclass = None
    def __init__(self, Set_Header=None, Data_Record=None, Padding=None):
        self.Set_Header = Set_Header
        if Data_Record is None:
            self.Data_Record = []
        else:
            self.Data_Record = Data_Record
        self.Padding = Padding
    def factory(*args_, **kwargs_):
        if IPFIXDataSetType.subclass:
            return IPFIXDataSetType.subclass(*args_, **kwargs_)
        else:
            return IPFIXDataSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Set_Header(self): return self.Set_Header
    def set_Set_Header(self, Set_Header): self.Set_Header = Set_Header
    def get_Data_Record(self): return self.Data_Record
    def set_Data_Record(self, Data_Record): self.Data_Record = Data_Record
    def add_Data_Record(self, value): self.Data_Record.append(value)
    def insert_Data_Record(self, index, value): self.Data_Record[index] = value
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Set_Header is not None or
            self.Data_Record or
            self.Padding is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXDataSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXDataSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXDataSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXDataSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Set_Header is not None:
            self.Set_Header.export(lwrite, level, 'NetFlowObj:', name_='Set_Header', pretty_print=pretty_print)
        for Data_Record_ in self.Data_Record:
            Data_Record_.export(lwrite, level, 'NetFlowObj:', name_='Data_Record', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'NetFlowObj:', name_='Padding', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Set_Header':
            obj_ = IPFIXSetHeaderType.factory()
            obj_.build(child_)
            self.set_Set_Header(obj_)
        elif nodeName_ == 'Data_Record':
            obj_ = IPFIXDataRecordType.factory()
            obj_.build(child_)
            self.Data_Record.append(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
# end class IPFIXDataSetType

class IPFIXSetHeaderType(GeneratedsSuper):
    """Defines the elements of the IPFIX set header."""

    subclass = None
    superclass = None
    def __init__(self, Set_ID=None, Length=None):
        self.Set_ID = Set_ID
        self.Length = Length
    def factory(*args_, **kwargs_):
        if IPFIXSetHeaderType.subclass:
            return IPFIXSetHeaderType.subclass(*args_, **kwargs_)
        else:
            return IPFIXSetHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Set_ID(self): return self.Set_ID
    def set_Set_ID(self, Set_ID): self.Set_ID = Set_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def hasContent_(self):
        if (
            self.Set_ID is not None or
            self.Length is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXSetHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXSetHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXSetHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXSetHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Set_ID is not None:
            self.Set_ID.export(lwrite, level, 'NetFlowObj:', name_='Set_ID', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'NetFlowObj:', name_='Length', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Set_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Set_ID(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
# end class IPFIXSetHeaderType

class IPFIXTemplateRecordType(GeneratedsSuper):
    """Specifies the regions of a Template Record, of which there are two:
    the Template Record Header, and the Field Specifiers. See RFC
    5101 under Template Record Format, section 3.4.1, for more
    information."""

    subclass = None
    superclass = None
    def __init__(self, Template_Record_Header=None, Field_Specifier=None):
        self.Template_Record_Header = Template_Record_Header
        if Field_Specifier is None:
            self.Field_Specifier = []
        else:
            self.Field_Specifier = Field_Specifier
    def factory(*args_, **kwargs_):
        if IPFIXTemplateRecordType.subclass:
            return IPFIXTemplateRecordType.subclass(*args_, **kwargs_)
        else:
            return IPFIXTemplateRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_Record_Header(self): return self.Template_Record_Header
    def set_Template_Record_Header(self, Template_Record_Header): self.Template_Record_Header = Template_Record_Header
    def get_Field_Specifier(self): return self.Field_Specifier
    def set_Field_Specifier(self, Field_Specifier): self.Field_Specifier = Field_Specifier
    def add_Field_Specifier(self, value): self.Field_Specifier.append(value)
    def insert_Field_Specifier(self, index, value): self.Field_Specifier[index] = value
    def hasContent_(self):
        if (
            self.Template_Record_Header is not None or
            self.Field_Specifier
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXTemplateRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_Record_Header is not None:
            self.Template_Record_Header.export(lwrite, level, 'NetFlowObj:', name_='Template_Record_Header', pretty_print=pretty_print)
        for Field_Specifier_ in self.Field_Specifier:
            Field_Specifier_.export(lwrite, level, 'NetFlowObj:', name_='Field_Specifier', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_Record_Header':
            obj_ = IPFIXTemplateRecordHeaderType.factory()
            obj_.build(child_)
            self.set_Template_Record_Header(obj_)
        elif nodeName_ == 'Field_Specifier':
            obj_ = IPFIXTemplateRecordFieldSpecifiersType.factory()
            obj_.build(child_)
            self.Field_Specifier.append(obj_)
# end class IPFIXTemplateRecordType

class IPFIXTemplateRecordHeaderType(GeneratedsSuper):
    """Specifies the fields in a Template Record Header, Template_ID and
    Field_Count, as explained in RFC 5101, section 3.4.1."""

    subclass = None
    superclass = None
    def __init__(self, Template_ID=None, Field_Count=None):
        self.Template_ID = Template_ID
        self.Field_Count = Field_Count
    def factory(*args_, **kwargs_):
        if IPFIXTemplateRecordHeaderType.subclass:
            return IPFIXTemplateRecordHeaderType.subclass(*args_, **kwargs_)
        else:
            return IPFIXTemplateRecordHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_ID(self): return self.Template_ID
    def set_Template_ID(self, Template_ID): self.Template_ID = Template_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Field_Count(self): return self.Field_Count
    def set_Field_Count(self, Field_Count): self.Field_Count = Field_Count
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Template_ID is not None or
            self.Field_Count is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXTemplateRecordHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_ID is not None:
            self.Template_ID.export(lwrite, level, 'NetFlowObj:', name_='Template_ID', pretty_print=pretty_print)
        if self.Field_Count is not None:
            self.Field_Count.export(lwrite, level, 'NetFlowObj:', name_='Field_Count', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Template_ID(obj_)
        elif nodeName_ == 'Field_Count':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Field_Count(obj_)
# end class IPFIXTemplateRecordHeaderType

class IPFIXTemplateRecordFieldSpecifiersType(GeneratedsSuper):
    """Specifies the fields in a Template Record Field Specifier, as
    explained in RFC 5101, section 3.2."""

    subclass = None
    superclass = None
    def __init__(self, Enterprise_Bit=None, Information_Element_ID=None, Field_Length=None, Enterprise_Number=None):
        self.Enterprise_Bit = Enterprise_Bit
        self.Information_Element_ID = Information_Element_ID
        self.Field_Length = Field_Length
        self.Enterprise_Number = Enterprise_Number
    def factory(*args_, **kwargs_):
        if IPFIXTemplateRecordFieldSpecifiersType.subclass:
            return IPFIXTemplateRecordFieldSpecifiersType.subclass(*args_, **kwargs_)
        else:
            return IPFIXTemplateRecordFieldSpecifiersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Enterprise_Bit(self): return self.Enterprise_Bit
    def set_Enterprise_Bit(self, Enterprise_Bit): self.Enterprise_Bit = Enterprise_Bit
    def get_Information_Element_ID(self): return self.Information_Element_ID
    def set_Information_Element_ID(self, Information_Element_ID): self.Information_Element_ID = Information_Element_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Field_Length(self): return self.Field_Length
    def set_Field_Length(self, Field_Length): self.Field_Length = Field_Length
    def get_Enterprise_Number(self): return self.Enterprise_Number
    def set_Enterprise_Number(self, Enterprise_Number): self.Enterprise_Number = Enterprise_Number
    def hasContent_(self):
        if (
            self.Enterprise_Bit is not None or
            self.Information_Element_ID is not None or
            self.Field_Length is not None or
            self.Enterprise_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordFieldSpecifiersType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXTemplateRecordFieldSpecifiersType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordFieldSpecifiersType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXTemplateRecordFieldSpecifiersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Enterprise_Bit is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sEnterprise_Bit>%s</%sEnterprise_Bit>%s' % ('NetFlowObj:', self.gds_format_boolean(self.Enterprise_Bit, input_name='Enterprise_Bit'), 'NetFlowObj:', eol_))
        if self.Information_Element_ID is not None:
            self.Information_Element_ID.export(lwrite, level, 'NetFlowObj:', name_='Information_Element_ID', pretty_print=pretty_print)
        if self.Field_Length is not None:
            self.Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Field_Length', pretty_print=pretty_print)
        if self.Enterprise_Number is not None:
            self.Enterprise_Number.export(lwrite, level, 'NetFlowObj:', name_='Enterprise_Number', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Enterprise_Bit':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Enterprise_Bit')
            self.Enterprise_Bit = ival_
        elif nodeName_ == 'Information_Element_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Information_Element_ID(obj_)
        elif nodeName_ == 'Field_Length':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Field_Length(obj_)
        elif nodeName_ == 'Enterprise_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Enterprise_Number(obj_)
# end class IPFIXTemplateRecordFieldSpecifiersType

class IPFIXOptionsTemplateRecordType(GeneratedsSuper):
    """Specifies the regions of an Options Template Record, of which there
    are two: the Options Template Record Header, and the Field
    Specifiers. See RFC 5101 under Options Template Record Format,
    section 3.4.2.2, for more information."""

    subclass = None
    superclass = None
    def __init__(self, Options_Template_Record_Header=None, Field_Specifier=None):
        self.Options_Template_Record_Header = Options_Template_Record_Header
        if Field_Specifier is None:
            self.Field_Specifier = []
        else:
            self.Field_Specifier = Field_Specifier
    def factory(*args_, **kwargs_):
        if IPFIXOptionsTemplateRecordType.subclass:
            return IPFIXOptionsTemplateRecordType.subclass(*args_, **kwargs_)
        else:
            return IPFIXOptionsTemplateRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Options_Template_Record_Header(self): return self.Options_Template_Record_Header
    def set_Options_Template_Record_Header(self, Options_Template_Record_Header): self.Options_Template_Record_Header = Options_Template_Record_Header
    def get_Field_Specifier(self): return self.Field_Specifier
    def set_Field_Specifier(self, Field_Specifier): self.Field_Specifier = Field_Specifier
    def add_Field_Specifier(self, value): self.Field_Specifier.append(value)
    def insert_Field_Specifier(self, index, value): self.Field_Specifier[index] = value
    def hasContent_(self):
        if (
            self.Options_Template_Record_Header is not None or
            self.Field_Specifier
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXOptionsTemplateRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Options_Template_Record_Header is not None:
            self.Options_Template_Record_Header.export(lwrite, level, 'NetFlowObj:', name_='Options_Template_Record_Header', pretty_print=pretty_print)
        for Field_Specifier_ in self.Field_Specifier:
            Field_Specifier_.export(lwrite, level, 'NetFlowObj:', name_='Field_Specifier', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Options_Template_Record_Header':
            obj_ = IPFIXOptionsTemplateRecordHeaderType.factory()
            obj_.build(child_)
            self.set_Options_Template_Record_Header(obj_)
        elif nodeName_ == 'Field_Specifier':
            obj_ = IPFIXTemplateRecordFieldSpecifiersType.factory()
            obj_.build(child_)
            self.Field_Specifier.append(obj_)
# end class IPFIXOptionsTemplateRecordType

class IPFIXOptionsTemplateRecordHeaderType(GeneratedsSuper):
    """Defines the ehader of an options template record."""

    subclass = None
    superclass = None
    def __init__(self, Template_ID=None, Field_Count=None, Scope_Field_Count=None):
        self.Template_ID = Template_ID
        self.Field_Count = Field_Count
        self.Scope_Field_Count = Scope_Field_Count
    def factory(*args_, **kwargs_):
        if IPFIXOptionsTemplateRecordHeaderType.subclass:
            return IPFIXOptionsTemplateRecordHeaderType.subclass(*args_, **kwargs_)
        else:
            return IPFIXOptionsTemplateRecordHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_ID(self): return self.Template_ID
    def set_Template_ID(self, Template_ID): self.Template_ID = Template_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Field_Count(self): return self.Field_Count
    def set_Field_Count(self, Field_Count): self.Field_Count = Field_Count
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Scope_Field_Count(self): return self.Scope_Field_Count
    def set_Scope_Field_Count(self, Scope_Field_Count): self.Scope_Field_Count = Scope_Field_Count
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Template_ID is not None or
            self.Field_Count is not None or
            self.Scope_Field_Count is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXOptionsTemplateRecordHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_ID is not None:
            self.Template_ID.export(lwrite, level, 'NetFlowObj:', name_='Template_ID', pretty_print=pretty_print)
        if self.Field_Count is not None:
            self.Field_Count.export(lwrite, level, 'NetFlowObj:', name_='Field_Count', pretty_print=pretty_print)
        if self.Scope_Field_Count is not None:
            self.Scope_Field_Count.export(lwrite, level, 'NetFlowObj:', name_='Scope_Field_Count', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Template_ID(obj_)
        elif nodeName_ == 'Field_Count':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Field_Count(obj_)
        elif nodeName_ == 'Scope_Field_Count':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Field_Count(obj_)
# end class IPFIXOptionsTemplateRecordHeaderType

class IPFIXOptionsTemplateRecordFieldSpecifiersType(GeneratedsSuper):
    """Specifies the fields in an Options Template Record Field Specifier,
    as explained in RFC 5101, sections 3.2 and 3.4.2.2. It consists
    of two sequences: Scope Fields and Option Fields, appended
    together."""

    subclass = None
    superclass = None
    def __init__(self, Scope_Enterprise_Bit=None, Scope_Information_Element_ID=None, Scope_Field_Length=None, Scope_Enterprise_Number=None, Option_Enterprise_Bit=None, Option_Information_Element_ID=None, Option_Field_Length=None, Option_Enterprise_Number=None):
        self.Scope_Enterprise_Bit = Scope_Enterprise_Bit
        self.Scope_Information_Element_ID = Scope_Information_Element_ID
        self.Scope_Field_Length = Scope_Field_Length
        self.Scope_Enterprise_Number = Scope_Enterprise_Number
        self.Option_Enterprise_Bit = Option_Enterprise_Bit
        self.Option_Information_Element_ID = Option_Information_Element_ID
        self.Option_Field_Length = Option_Field_Length
        self.Option_Enterprise_Number = Option_Enterprise_Number
    def factory(*args_, **kwargs_):
        if IPFIXOptionsTemplateRecordFieldSpecifiersType.subclass:
            return IPFIXOptionsTemplateRecordFieldSpecifiersType.subclass(*args_, **kwargs_)
        else:
            return IPFIXOptionsTemplateRecordFieldSpecifiersType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Scope_Enterprise_Bit(self): return self.Scope_Enterprise_Bit
    def set_Scope_Enterprise_Bit(self, Scope_Enterprise_Bit): self.Scope_Enterprise_Bit = Scope_Enterprise_Bit
    def get_Scope_Information_Element_ID(self): return self.Scope_Information_Element_ID
    def set_Scope_Information_Element_ID(self, Scope_Information_Element_ID): self.Scope_Information_Element_ID = Scope_Information_Element_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Scope_Field_Length(self): return self.Scope_Field_Length
    def set_Scope_Field_Length(self, Scope_Field_Length): self.Scope_Field_Length = Scope_Field_Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Scope_Enterprise_Number(self): return self.Scope_Enterprise_Number
    def set_Scope_Enterprise_Number(self, Scope_Enterprise_Number): self.Scope_Enterprise_Number = Scope_Enterprise_Number
    def get_Option_Enterprise_Bit(self): return self.Option_Enterprise_Bit
    def set_Option_Enterprise_Bit(self, Option_Enterprise_Bit): self.Option_Enterprise_Bit = Option_Enterprise_Bit
    def get_Option_Information_Element_ID(self): return self.Option_Information_Element_ID
    def set_Option_Information_Element_ID(self, Option_Information_Element_ID): self.Option_Information_Element_ID = Option_Information_Element_ID
    def get_Option_Field_Length(self): return self.Option_Field_Length
    def set_Option_Field_Length(self, Option_Field_Length): self.Option_Field_Length = Option_Field_Length
    def get_Option_Enterprise_Number(self): return self.Option_Enterprise_Number
    def set_Option_Enterprise_Number(self, Option_Enterprise_Number): self.Option_Enterprise_Number = Option_Enterprise_Number
    def hasContent_(self):
        if (
            self.Scope_Enterprise_Bit is not None or
            self.Scope_Information_Element_ID is not None or
            self.Scope_Field_Length is not None or
            self.Scope_Enterprise_Number is not None or
            self.Option_Enterprise_Bit is not None or
            self.Option_Information_Element_ID is not None or
            self.Option_Field_Length is not None or
            self.Option_Enterprise_Number is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordFieldSpecifiersType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXOptionsTemplateRecordFieldSpecifiersType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordFieldSpecifiersType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXOptionsTemplateRecordFieldSpecifiersType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Scope_Enterprise_Bit is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sScope_Enterprise_Bit>%s</%sScope_Enterprise_Bit>%s' % ('NetFlowObj:', self.gds_format_boolean(self.Scope_Enterprise_Bit, input_name='Scope_Enterprise_Bit'), 'NetFlowObj:', eol_))
        if self.Scope_Information_Element_ID is not None:
            self.Scope_Information_Element_ID.export(lwrite, level, 'NetFlowObj:', name_='Scope_Information_Element_ID', pretty_print=pretty_print)
        if self.Scope_Field_Length is not None:
            self.Scope_Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Scope_Field_Length', pretty_print=pretty_print)
        if self.Scope_Enterprise_Number is not None:
            self.Scope_Enterprise_Number.export(lwrite, level, 'NetFlowObj:', name_='Scope_Enterprise_Number', pretty_print=pretty_print)
        if self.Option_Enterprise_Bit is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sOption_Enterprise_Bit>%s</%sOption_Enterprise_Bit>%s' % ('NetFlowObj:', self.gds_format_boolean(self.Option_Enterprise_Bit, input_name='Option_Enterprise_Bit'), 'NetFlowObj:', eol_))
        if self.Option_Information_Element_ID is not None:
            self.Option_Information_Element_ID.export(lwrite, level, 'NetFlowObj:', name_='Option_Information_Element_ID', pretty_print=pretty_print)
        if self.Option_Field_Length is not None:
            self.Option_Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Option_Field_Length', pretty_print=pretty_print)
        if self.Option_Enterprise_Number is not None:
            self.Option_Enterprise_Number.export(lwrite, level, 'NetFlowObj:', name_='Option_Enterprise_Number', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Scope_Enterprise_Bit':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Scope_Enterprise_Bit')
            self.Scope_Enterprise_Bit = ival_
        elif nodeName_ == 'Scope_Information_Element_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Information_Element_ID(obj_)
        elif nodeName_ == 'Scope_Field_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Field_Length(obj_)
        elif nodeName_ == 'Scope_Enterprise_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Enterprise_Number(obj_)
        elif nodeName_ == 'Option_Enterprise_Bit':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Option_Enterprise_Bit')
            self.Option_Enterprise_Bit = ival_
        elif nodeName_ == 'Option_Information_Element_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Information_Element_ID(obj_)
        elif nodeName_ == 'Option_Field_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Field_Length(obj_)
        elif nodeName_ == 'Option_Enterprise_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Enterprise_Number(obj_)
# end class IPFIXOptionsTemplateRecordFieldSpecifiersType

class IPFIXDataRecordType(GeneratedsSuper):
    """Data records are sent in data sets. A data record consists of only
    one more more Field values."""

    subclass = None
    superclass = None
    def __init__(self, Field_Value=None):
        if Field_Value is None:
            self.Field_Value = []
        else:
            self.Field_Value = Field_Value
    def factory(*args_, **kwargs_):
        if IPFIXDataRecordType.subclass:
            return IPFIXDataRecordType.subclass(*args_, **kwargs_)
        else:
            return IPFIXDataRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Field_Value(self): return self.Field_Value
    def set_Field_Value(self, Field_Value): self.Field_Value = Field_Value
    def add_Field_Value(self, value): self.Field_Value.append(value)
    def insert_Field_Value(self, index, value): self.Field_Value[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Field_Value
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXDataRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IPFIXDataRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='IPFIXDataRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='IPFIXDataRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Field_Value_ in self.Field_Value:
            Field_Value_.export(lwrite, level, 'NetFlowObj:', name_='Field_Value', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Field_Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Field_Value.append(obj_)
# end class IPFIXDataRecordType

class NetflowV9ExportPacketType(GeneratedsSuper):
    """Netflow v9 was developed by Cisco and provides acess to IP flow
    information. http://www.ietf.org/rfc/rfc3954.txt"""

    subclass = None
    superclass = None
    def __init__(self, Packet_Header=None, Flow_Set=None):
        self.Packet_Header = Packet_Header
        if Flow_Set is None:
            self.Flow_Set = []
        else:
            self.Flow_Set = Flow_Set
    def factory(*args_, **kwargs_):
        if NetflowV9ExportPacketType.subclass:
            return NetflowV9ExportPacketType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9ExportPacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Packet_Header(self): return self.Packet_Header
    def set_Packet_Header(self, Packet_Header): self.Packet_Header = Packet_Header
    def get_Flow_Set(self): return self.Flow_Set
    def set_Flow_Set(self, Flow_Set): self.Flow_Set = Flow_Set
    def add_Flow_Set(self, value): self.Flow_Set.append(value)
    def insert_Flow_Set(self, index, value): self.Flow_Set[index] = value
    def hasContent_(self):
        if (
            self.Packet_Header is not None or
            self.Flow_Set
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9ExportPacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9ExportPacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9ExportPacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9ExportPacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Packet_Header is not None:
            self.Packet_Header.export(lwrite, level, 'NetFlowObj:', name_='Packet_Header', pretty_print=pretty_print)
        for Flow_Set_ in self.Flow_Set:
            Flow_Set_.export(lwrite, level, 'NetFlowObj:', name_='Flow_Set', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Packet_Header':
            obj_ = NetflowV9PacketHeaderType.factory()
            obj_.build(child_)
            self.set_Packet_Header(obj_)
        elif nodeName_ == 'Flow_Set':
            obj_ = NetflowV9FlowSetType.factory()
            obj_.build(child_)
            self.Flow_Set.append(obj_)
# end class NetflowV9ExportPacketType

class NetflowV9PacketHeaderType(GeneratedsSuper):
    """Header fields defined for Netflow v9. Note that common elements are
    included in the Network_Flow_Label.
    http://www.ietf.org/rfc/rfc3954.txt"""

    subclass = None
    superclass = None
    def __init__(self, Version=None, Record_Count=None, Sys_Up_Time=None, Unix_Secs=None, Sequence_Number=None, Source_ID=None):
        self.Version = Version
        self.Record_Count = Record_Count
        self.Sys_Up_Time = Sys_Up_Time
        self.Unix_Secs = Unix_Secs
        self.Sequence_Number = Sequence_Number
        self.Source_ID = Source_ID
    def factory(*args_, **kwargs_):
        if NetflowV9PacketHeaderType.subclass:
            return NetflowV9PacketHeaderType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9PacketHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Record_Count(self): return self.Record_Count
    def set_Record_Count(self, Record_Count): self.Record_Count = Record_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Sys_Up_Time(self): return self.Sys_Up_Time
    def set_Sys_Up_Time(self, Sys_Up_Time): self.Sys_Up_Time = Sys_Up_Time
    def get_Unix_Secs(self): return self.Unix_Secs
    def set_Unix_Secs(self, Unix_Secs): self.Unix_Secs = Unix_Secs
    def get_Sequence_Number(self): return self.Sequence_Number
    def set_Sequence_Number(self, Sequence_Number): self.Sequence_Number = Sequence_Number
    def get_Source_ID(self): return self.Source_ID
    def set_Source_ID(self, Source_ID): self.Source_ID = Source_ID
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Record_Count is not None or
            self.Sys_Up_Time is not None or
            self.Unix_Secs is not None or
            self.Sequence_Number is not None or
            self.Source_ID is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9PacketHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9PacketHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9PacketHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9PacketHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            self.Version.export(lwrite, level, 'NetFlowObj:', name_='Version', pretty_print=pretty_print)
        if self.Record_Count is not None:
            self.Record_Count.export(lwrite, level, 'NetFlowObj:', name_='Record_Count', pretty_print=pretty_print)
        if self.Sys_Up_Time is not None:
            self.Sys_Up_Time.export(lwrite, level, 'NetFlowObj:', name_='Sys_Up_Time', pretty_print=pretty_print)
        if self.Unix_Secs is not None:
            self.Unix_Secs.export(lwrite, level, 'NetFlowObj:', name_='Unix_Secs', pretty_print=pretty_print)
        if self.Sequence_Number is not None:
            self.Sequence_Number.export(lwrite, level, 'NetFlowObj:', name_='Sequence_Number', pretty_print=pretty_print)
        if self.Source_ID is not None:
            self.Source_ID.export(lwrite, level, 'NetFlowObj:', name_='Source_ID', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Record_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Record_Count(obj_)
        elif nodeName_ == 'Sys_Up_Time':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sys_Up_Time(obj_)
        elif nodeName_ == 'Unix_Secs':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Unix_Secs(obj_)
        elif nodeName_ == 'Sequence_Number':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sequence_Number(obj_)
        elif nodeName_ == 'Source_ID':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Source_ID(obj_)
# end class NetflowV9PacketHeaderType

class NetflowV9FlowSetType(GeneratedsSuper):
    """In an Export Packet, one or more FlowSets follow the Packet Header.
    There are three differnet types of FlowSets, as defined in RFC
    3954: a Template FlowSet, Options Template FlowSet and Data
    FlowSet."""

    subclass = None
    superclass = None
    def __init__(self, Template_Flow_Set=None, Options_Template_Flow_Set=None, Data_Flow_Set=None):
        self.Template_Flow_Set = Template_Flow_Set
        self.Options_Template_Flow_Set = Options_Template_Flow_Set
        self.Data_Flow_Set = Data_Flow_Set
    def factory(*args_, **kwargs_):
        if NetflowV9FlowSetType.subclass:
            return NetflowV9FlowSetType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9FlowSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_Flow_Set(self): return self.Template_Flow_Set
    def set_Template_Flow_Set(self, Template_Flow_Set): self.Template_Flow_Set = Template_Flow_Set
    def get_Options_Template_Flow_Set(self): return self.Options_Template_Flow_Set
    def set_Options_Template_Flow_Set(self, Options_Template_Flow_Set): self.Options_Template_Flow_Set = Options_Template_Flow_Set
    def get_Data_Flow_Set(self): return self.Data_Flow_Set
    def set_Data_Flow_Set(self, Data_Flow_Set): self.Data_Flow_Set = Data_Flow_Set
    def hasContent_(self):
        if (
            self.Template_Flow_Set is not None or
            self.Options_Template_Flow_Set is not None or
            self.Data_Flow_Set is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9FlowSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9FlowSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9FlowSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9FlowSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_Flow_Set is not None:
            self.Template_Flow_Set.export(lwrite, level, 'NetFlowObj:', name_='Template_Flow_Set', pretty_print=pretty_print)
        if self.Options_Template_Flow_Set is not None:
            self.Options_Template_Flow_Set.export(lwrite, level, 'NetFlowObj:', name_='Options_Template_Flow_Set', pretty_print=pretty_print)
        if self.Data_Flow_Set is not None:
            self.Data_Flow_Set.export(lwrite, level, 'NetFlowObj:', name_='Data_Flow_Set', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_Flow_Set':
            obj_ = NetflowV9TemplateFlowSetType.factory()
            obj_.build(child_)
            self.set_Template_Flow_Set(obj_)
        elif nodeName_ == 'Options_Template_Flow_Set':
            obj_ = NetflowV9OptionsTemplateFlowSetType.factory()
            obj_.build(child_)
            self.set_Options_Template_Flow_Set(obj_)
        elif nodeName_ == 'Data_Flow_Set':
            obj_ = NetflowV9DataFlowSetType.factory()
            obj_.build(child_)
            self.set_Data_Flow_Set(obj_)
# end class NetflowV9FlowSetType

class NetflowV9TemplateFlowSetType(GeneratedsSuper):
    """Provides the format of the Template FlowSet."""

    subclass = None
    superclass = None
    def __init__(self, Flow_Set_ID=None, Length=None, Template_Record=None):
        self.Flow_Set_ID = Flow_Set_ID
        self.Length = Length
        if Template_Record is None:
            self.Template_Record = []
        else:
            self.Template_Record = Template_Record
    def factory(*args_, **kwargs_):
        if NetflowV9TemplateFlowSetType.subclass:
            return NetflowV9TemplateFlowSetType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9TemplateFlowSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Set_ID(self): return self.Flow_Set_ID
    def set_Flow_Set_ID(self, Flow_Set_ID): self.Flow_Set_ID = Flow_Set_ID
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Template_Record(self): return self.Template_Record
    def set_Template_Record(self, Template_Record): self.Template_Record = Template_Record
    def add_Template_Record(self, value): self.Template_Record.append(value)
    def insert_Template_Record(self, index, value): self.Template_Record[index] = value
    def hasContent_(self):
        if (
            self.Flow_Set_ID is not None or
            self.Length is not None or
            self.Template_Record
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9TemplateFlowSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9TemplateFlowSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9TemplateFlowSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9TemplateFlowSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow_Set_ID is not None:
            self.Flow_Set_ID.export(lwrite, level, 'NetFlowObj:', name_='Flow_Set_ID', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'NetFlowObj:', name_='Length', pretty_print=pretty_print)
        for Template_Record_ in self.Template_Record:
            Template_Record_.export(lwrite, level, 'NetFlowObj:', name_='Template_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Set_ID':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Set_ID(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Template_Record':
            obj_ = IPFIXTemplateRecordType.factory()
            obj_.build(child_)
            self.Template_Record.append(obj_)
# end class NetflowV9TemplateFlowSetType

class NetflowV9TemplateRecordType(GeneratedsSuper):
    """Specifies the Template Record region, which includes the template
    ID, field count, field type, and field length.Number of fields
    corresponds to Count field."""

    subclass = None
    superclass = None
    def __init__(self, Template_ID=None, Field_Count=None, Field_Type=None, Field_Length=None):
        self.Template_ID = Template_ID
        self.Field_Count = Field_Count
        self.Field_Type = Field_Type
        self.Field_Length = Field_Length
    def factory(*args_, **kwargs_):
        if NetflowV9TemplateRecordType.subclass:
            return NetflowV9TemplateRecordType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9TemplateRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_ID(self): return self.Template_ID
    def set_Template_ID(self, Template_ID): self.Template_ID = Template_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Field_Count(self): return self.Field_Count
    def set_Field_Count(self, Field_Count): self.Field_Count = Field_Count
    def get_Field_Type(self): return self.Field_Type
    def set_Field_Type(self, Field_Type): self.Field_Type = Field_Type
    def validate_NetflowV9FieldType(self, value):
        # Validate type NetflowV9FieldType, a restriction on None.
        pass
    def get_Field_Length(self): return self.Field_Length
    def set_Field_Length(self, Field_Length): self.Field_Length = Field_Length
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Template_ID is not None or
            self.Field_Count is not None or
            self.Field_Type is not None or
            self.Field_Length is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9TemplateRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9TemplateRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9TemplateRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9TemplateRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_ID is not None:
            self.Template_ID.export(lwrite, level, 'NetFlowObj:', name_='Template_ID', pretty_print=pretty_print)
        if self.Field_Count is not None:
            self.Field_Count.export(lwrite, level, 'NetFlowObj:', name_='Field_Count', pretty_print=pretty_print)
        if self.Field_Type is not None:
            self.Field_Type.export(lwrite, level, 'NetFlowObj:', name_='Field_Type', pretty_print=pretty_print)
        if self.Field_Length is not None:
            self.Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Field_Length', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Template_ID(obj_)
        elif nodeName_ == 'Field_Count':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Field_Count(obj_)
        elif nodeName_ == 'Field_Type':
            obj_ = NetflowV9FieldType.factory()
            obj_.build(child_)
            self.set_Field_Type(obj_)
        elif nodeName_ == 'Field_Length':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Field_Length(obj_)
# end class NetflowV9TemplateRecordType

class NetflowV9OptionsTemplateFlowSetType(GeneratedsSuper):
    """Specifies an Options Template FlowSet, which is one or more Options
    Template Records that have been grouped together in an Export
    Packet."""

    subclass = None
    superclass = None
    def __init__(self, Flow_Set_ID=None, Length=None, Options_Template_Record=None, Padding=None):
        self.Flow_Set_ID = Flow_Set_ID
        self.Length = Length
        if Options_Template_Record is None:
            self.Options_Template_Record = []
        else:
            self.Options_Template_Record = Options_Template_Record
        self.Padding = Padding
    def factory(*args_, **kwargs_):
        if NetflowV9OptionsTemplateFlowSetType.subclass:
            return NetflowV9OptionsTemplateFlowSetType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9OptionsTemplateFlowSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Set_ID(self): return self.Flow_Set_ID
    def set_Flow_Set_ID(self, Flow_Set_ID): self.Flow_Set_ID = Flow_Set_ID
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Options_Template_Record(self): return self.Options_Template_Record
    def set_Options_Template_Record(self, Options_Template_Record): self.Options_Template_Record = Options_Template_Record
    def add_Options_Template_Record(self, value): self.Options_Template_Record.append(value)
    def insert_Options_Template_Record(self, index, value): self.Options_Template_Record[index] = value
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def hasContent_(self):
        if (
            self.Flow_Set_ID is not None or
            self.Length is not None or
            self.Options_Template_Record or
            self.Padding is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateFlowSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9OptionsTemplateFlowSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateFlowSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateFlowSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow_Set_ID is not None:
            self.Flow_Set_ID.export(lwrite, level, 'NetFlowObj:', name_='Flow_Set_ID', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'NetFlowObj:', name_='Length', pretty_print=pretty_print)
        for Options_Template_Record_ in self.Options_Template_Record:
            Options_Template_Record_.export(lwrite, level, 'NetFlowObj:', name_='Options_Template_Record', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'NetFlowObj:', name_='Padding', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Set_ID':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Set_ID(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Options_Template_Record':
            obj_ = IPFIXOptionsTemplateRecordType.factory()
            obj_.build(child_)
            self.Options_Template_Record.append(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
# end class NetflowV9OptionsTemplateFlowSetType

class NetflowV9OptionsTemplateRecordType(GeneratedsSuper):
    """Specifies the Options Template Record region, which includes the
    Option Scope Length, Option Length, and fields specifying the
    Scope field type and Scope field length."""

    subclass = None
    superclass = None
    def __init__(self, Template_ID=None, Option_Scope_Length=None, Option_Length=None, Scope_Field_Type=None, Scope_Field_Length=None, Option_Field_Type=None, Option_Field_Length=None):
        self.Template_ID = Template_ID
        self.Option_Scope_Length = Option_Scope_Length
        self.Option_Length = Option_Length
        self.Scope_Field_Type = Scope_Field_Type
        self.Scope_Field_Length = Scope_Field_Length
        self.Option_Field_Type = Option_Field_Type
        self.Option_Field_Length = Option_Field_Length
    def factory(*args_, **kwargs_):
        if NetflowV9OptionsTemplateRecordType.subclass:
            return NetflowV9OptionsTemplateRecordType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9OptionsTemplateRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Template_ID(self): return self.Template_ID
    def set_Template_ID(self, Template_ID): self.Template_ID = Template_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Option_Scope_Length(self): return self.Option_Scope_Length
    def set_Option_Scope_Length(self, Option_Scope_Length): self.Option_Scope_Length = Option_Scope_Length
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Option_Length(self): return self.Option_Length
    def set_Option_Length(self, Option_Length): self.Option_Length = Option_Length
    def get_Scope_Field_Type(self): return self.Scope_Field_Type
    def set_Scope_Field_Type(self, Scope_Field_Type): self.Scope_Field_Type = Scope_Field_Type
    def validate_NetflowV9ScopeFieldType(self, value):
        # Validate type NetflowV9ScopeFieldType, a restriction on None.
        pass
    def get_Scope_Field_Length(self): return self.Scope_Field_Length
    def set_Scope_Field_Length(self, Scope_Field_Length): self.Scope_Field_Length = Scope_Field_Length
    def get_Option_Field_Type(self): return self.Option_Field_Type
    def set_Option_Field_Type(self, Option_Field_Type): self.Option_Field_Type = Option_Field_Type
    def validate_NetflowV9FieldType(self, value):
        # Validate type NetflowV9FieldType, a restriction on None.
        pass
    def get_Option_Field_Length(self): return self.Option_Field_Length
    def set_Option_Field_Length(self, Option_Field_Length): self.Option_Field_Length = Option_Field_Length
    def hasContent_(self):
        if (
            self.Template_ID is not None or
            self.Option_Scope_Length is not None or
            self.Option_Length is not None or
            self.Scope_Field_Type is not None or
            self.Scope_Field_Length is not None or
            self.Option_Field_Type is not None or
            self.Option_Field_Length is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9OptionsTemplateRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9OptionsTemplateRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Template_ID is not None:
            self.Template_ID.export(lwrite, level, 'NetFlowObj:', name_='Template_ID', pretty_print=pretty_print)
        if self.Option_Scope_Length is not None:
            self.Option_Scope_Length.export(lwrite, level, 'NetFlowObj:', name_='Option_Scope_Length', pretty_print=pretty_print)
        if self.Option_Length is not None:
            self.Option_Length.export(lwrite, level, 'NetFlowObj:', name_='Option_Length', pretty_print=pretty_print)
        if self.Scope_Field_Type is not None:
            self.Scope_Field_Type.export(lwrite, level, 'NetFlowObj:', name_='Scope_Field_Type', pretty_print=pretty_print)
        if self.Scope_Field_Length is not None:
            self.Scope_Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Scope_Field_Length', pretty_print=pretty_print)
        if self.Option_Field_Type is not None:
            self.Option_Field_Type.export(lwrite, level, 'NetFlowObj:', name_='Option_Field_Type', pretty_print=pretty_print)
        if self.Option_Field_Length is not None:
            self.Option_Field_Length.export(lwrite, level, 'NetFlowObj:', name_='Option_Field_Length', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Template_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Template_ID(obj_)
        elif nodeName_ == 'Option_Scope_Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Scope_Length(obj_)
        elif nodeName_ == 'Option_Length':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Length(obj_)
        elif nodeName_ == 'Scope_Field_Type':
            obj_ = NetflowV9ScopeFieldType.factory()
            obj_.build(child_)
            self.set_Scope_Field_Type(obj_)
        elif nodeName_ == 'Scope_Field_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Field_Length(obj_)
        elif nodeName_ == 'Option_Field_Type':
            obj_ = NetflowV9FieldType.factory()
            obj_.build(child_)
            self.set_Option_Field_Type(obj_)
        elif nodeName_ == 'Option_Field_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Option_Field_Length(obj_)
# end class NetflowV9OptionsTemplateRecordType

class NetflowV9DataFlowSetType(GeneratedsSuper):
    """Specifies a Data FlowSet, which is one or more records, of the same
    type, that are grouped together in an Export Packet. Each record
    is either a Flow Data Record or an Options Data Record
    previously defined by a Template Record or an Options Template
    Record. http://www.ietf.org/rfc/rfc3954.txt"""

    subclass = None
    superclass = None
    def __init__(self, Flow_Set_ID_Template_ID=None, Length=None, Data_Record=None, Padding=None):
        self.Flow_Set_ID_Template_ID = Flow_Set_ID_Template_ID
        self.Length = Length
        if Data_Record is None:
            self.Data_Record = []
        else:
            self.Data_Record = Data_Record
        self.Padding = Padding
    def factory(*args_, **kwargs_):
        if NetflowV9DataFlowSetType.subclass:
            return NetflowV9DataFlowSetType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9DataFlowSetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Set_ID_Template_ID(self): return self.Flow_Set_ID_Template_ID
    def set_Flow_Set_ID_Template_ID(self, Flow_Set_ID_Template_ID): self.Flow_Set_ID_Template_ID = Flow_Set_ID_Template_ID
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def get_Data_Record(self): return self.Data_Record
    def set_Data_Record(self, Data_Record): self.Data_Record = Data_Record
    def add_Data_Record(self, value): self.Data_Record.append(value)
    def insert_Data_Record(self, index, value): self.Data_Record[index] = value
    def get_Padding(self): return self.Padding
    def set_Padding(self, Padding): self.Padding = Padding
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Flow_Set_ID_Template_ID is not None or
            self.Length is not None or
            self.Data_Record or
            self.Padding is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9DataFlowSetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9DataFlowSetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9DataFlowSetType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9DataFlowSetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow_Set_ID_Template_ID is not None:
            self.Flow_Set_ID_Template_ID.export(lwrite, level, 'NetFlowObj:', name_='Flow_Set_ID_Template_ID', pretty_print=pretty_print)
        if self.Length is not None:
            self.Length.export(lwrite, level, 'NetFlowObj:', name_='Length', pretty_print=pretty_print)
        for Data_Record_ in self.Data_Record:
            Data_Record_.export(lwrite, level, 'NetFlowObj:', name_='Data_Record', pretty_print=pretty_print)
        if self.Padding is not None:
            self.Padding.export(lwrite, level, 'NetFlowObj:', name_='Padding', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Set_ID_Template_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Set_ID_Template_ID(obj_)
        elif nodeName_ == 'Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Data_Record':
            obj_ = IPFIXDataRecordType.factory()
            obj_.build(child_)
            self.Data_Record.append(obj_)
        elif nodeName_ == 'Padding':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding(obj_)
# end class NetflowV9DataFlowSetType

class NetflowV9DataRecordType(GeneratedsSuper):
    """A Data FlowSet is one or more records, of the same type, that are
    grouped together in an Export Packet. Each record is either a
    Flow Data Record or an Options Data Record previously defined by
    a Template Record or an Options Template Record.
    http://www.ietf.org/rfc/rfc3954.txt"""

    subclass = None
    superclass = None
    def __init__(self, Flow_Data_Record=None, Options_Data_Record=None):
        if Flow_Data_Record is None:
            self.Flow_Data_Record = []
        else:
            self.Flow_Data_Record = Flow_Data_Record
        if Options_Data_Record is None:
            self.Options_Data_Record = []
        else:
            self.Options_Data_Record = Options_Data_Record
    def factory(*args_, **kwargs_):
        if NetflowV9DataRecordType.subclass:
            return NetflowV9DataRecordType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9DataRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Data_Record(self): return self.Flow_Data_Record
    def set_Flow_Data_Record(self, Flow_Data_Record): self.Flow_Data_Record = Flow_Data_Record
    def add_Flow_Data_Record(self, value): self.Flow_Data_Record.append(value)
    def insert_Flow_Data_Record(self, index, value): self.Flow_Data_Record[index] = value
    def get_Options_Data_Record(self): return self.Options_Data_Record
    def set_Options_Data_Record(self, Options_Data_Record): self.Options_Data_Record = Options_Data_Record
    def add_Options_Data_Record(self, value): self.Options_Data_Record.append(value)
    def insert_Options_Data_Record(self, index, value): self.Options_Data_Record[index] = value
    def hasContent_(self):
        if (
            self.Flow_Data_Record or
            self.Options_Data_Record
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9DataRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9DataRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9DataRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9DataRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Flow_Data_Record_ in self.Flow_Data_Record:
            Flow_Data_Record_.export(lwrite, level, 'NetFlowObj:', name_='Flow_Data_Record', pretty_print=pretty_print)
        for Options_Data_Record_ in self.Options_Data_Record:
            Options_Data_Record_.export(lwrite, level, 'NetFlowObj:', name_='Options_Data_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Data_Record':
            obj_ = FlowDataRecordType.factory()
            obj_.build(child_)
            self.Flow_Data_Record.append(obj_)
        elif nodeName_ == 'Options_Data_Record':
            obj_ = OptionsDataRecordType.factory()
            obj_.build(child_)
            self.Options_Data_Record.append(obj_)
# end class NetflowV9DataRecordType

class FlowDataRecordType(GeneratedsSuper):
    """A Flow Data Record is a data record that contains values of the Flow
    parameters corresponding to a Template Record."""

    subclass = None
    superclass = None
    def __init__(self, Flow_Record_Collection_Element=None):
        if Flow_Record_Collection_Element is None:
            self.Flow_Record_Collection_Element = []
        else:
            self.Flow_Record_Collection_Element = Flow_Record_Collection_Element
    def factory(*args_, **kwargs_):
        if FlowDataRecordType.subclass:
            return FlowDataRecordType.subclass(*args_, **kwargs_)
        else:
            return FlowDataRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Record_Collection_Element(self): return self.Flow_Record_Collection_Element
    def set_Flow_Record_Collection_Element(self, Flow_Record_Collection_Element): self.Flow_Record_Collection_Element = Flow_Record_Collection_Element
    def add_Flow_Record_Collection_Element(self, value): self.Flow_Record_Collection_Element.append(value)
    def insert_Flow_Record_Collection_Element(self, index, value): self.Flow_Record_Collection_Element[index] = value
    def hasContent_(self):
        if (
            self.Flow_Record_Collection_Element
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='FlowDataRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FlowDataRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='FlowDataRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='FlowDataRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Flow_Record_Collection_Element_ in self.Flow_Record_Collection_Element:
            Flow_Record_Collection_Element_.export(lwrite, level, 'NetFlowObj:', name_='Flow_Record_Collection_Element', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Record_Collection_Element':
            obj_ = FlowCollectionElementType.factory()
            obj_.build(child_)
            self.Flow_Record_Collection_Element.append(obj_)
# end class FlowDataRecordType

class FlowCollectionElementType(GeneratedsSuper):
    """Field values are associated with each record in the collection of a
    flow data record."""

    subclass = None
    superclass = None
    def __init__(self, Flow_Record_Field_Value=None):
        if Flow_Record_Field_Value is None:
            self.Flow_Record_Field_Value = []
        else:
            self.Flow_Record_Field_Value = Flow_Record_Field_Value
    def factory(*args_, **kwargs_):
        if FlowCollectionElementType.subclass:
            return FlowCollectionElementType.subclass(*args_, **kwargs_)
        else:
            return FlowCollectionElementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Record_Field_Value(self): return self.Flow_Record_Field_Value
    def set_Flow_Record_Field_Value(self, Flow_Record_Field_Value): self.Flow_Record_Field_Value = Flow_Record_Field_Value
    def add_Flow_Record_Field_Value(self, value): self.Flow_Record_Field_Value.append(value)
    def insert_Flow_Record_Field_Value(self, index, value): self.Flow_Record_Field_Value[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Flow_Record_Field_Value
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='FlowCollectionElementType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FlowCollectionElementType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='FlowCollectionElementType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='FlowCollectionElementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Flow_Record_Field_Value_ in self.Flow_Record_Field_Value:
            Flow_Record_Field_Value_.export(lwrite, level, 'NetFlowObj:', name_='Flow_Record_Field_Value', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Record_Field_Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Flow_Record_Field_Value.append(obj_)
# end class FlowCollectionElementType

class OptionsDataRecordType(GeneratedsSuper):
    """The data record that contains values and scope information of the
    Flow measurement parameters, corresponding to an Options
    Template Record."""

    subclass = None
    superclass = None
    def __init__(self, Scope_Field_Value=None, Option_Record_Collection_Element=None):
        self.Scope_Field_Value = Scope_Field_Value
        if Option_Record_Collection_Element is None:
            self.Option_Record_Collection_Element = []
        else:
            self.Option_Record_Collection_Element = Option_Record_Collection_Element
    def factory(*args_, **kwargs_):
        if OptionsDataRecordType.subclass:
            return OptionsDataRecordType.subclass(*args_, **kwargs_)
        else:
            return OptionsDataRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Scope_Field_Value(self): return self.Scope_Field_Value
    def set_Scope_Field_Value(self, Scope_Field_Value): self.Scope_Field_Value = Scope_Field_Value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Option_Record_Collection_Element(self): return self.Option_Record_Collection_Element
    def set_Option_Record_Collection_Element(self, Option_Record_Collection_Element): self.Option_Record_Collection_Element = Option_Record_Collection_Element
    def add_Option_Record_Collection_Element(self, value): self.Option_Record_Collection_Element.append(value)
    def insert_Option_Record_Collection_Element(self, index, value): self.Option_Record_Collection_Element[index] = value
    def hasContent_(self):
        if (
            self.Scope_Field_Value is not None or
            self.Option_Record_Collection_Element
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='OptionsDataRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OptionsDataRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='OptionsDataRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='OptionsDataRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Scope_Field_Value is not None:
            self.Scope_Field_Value.export(lwrite, level, 'NetFlowObj:', name_='Scope_Field_Value', pretty_print=pretty_print)
        for Option_Record_Collection_Element_ in self.Option_Record_Collection_Element:
            Option_Record_Collection_Element_.export(lwrite, level, 'NetFlowObj:', name_='Option_Record_Collection_Element', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Scope_Field_Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Scope_Field_Value(obj_)
        elif nodeName_ == 'Option_Record_Collection_Element':
            obj_ = OptionCollectionElementType.factory()
            obj_.build(child_)
            self.Option_Record_Collection_Element.append(obj_)
# end class OptionsDataRecordType

class OptionCollectionElementType(GeneratedsSuper):
    """Field values are associatedwith each option in the collection of an
    option data record."""

    subclass = None
    superclass = None
    def __init__(self, Option_Record_Field_Value=None):
        if Option_Record_Field_Value is None:
            self.Option_Record_Field_Value = []
        else:
            self.Option_Record_Field_Value = Option_Record_Field_Value
    def factory(*args_, **kwargs_):
        if OptionCollectionElementType.subclass:
            return OptionCollectionElementType.subclass(*args_, **kwargs_)
        else:
            return OptionCollectionElementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Option_Record_Field_Value(self): return self.Option_Record_Field_Value
    def set_Option_Record_Field_Value(self, Option_Record_Field_Value): self.Option_Record_Field_Value = Option_Record_Field_Value
    def add_Option_Record_Field_Value(self, value): self.Option_Record_Field_Value.append(value)
    def insert_Option_Record_Field_Value(self, index, value): self.Option_Record_Field_Value[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Option_Record_Field_Value
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='OptionCollectionElementType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OptionCollectionElementType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='OptionCollectionElementType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='OptionCollectionElementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Option_Record_Field_Value_ in self.Option_Record_Field_Value:
            Option_Record_Field_Value_.export(lwrite, level, 'NetFlowObj:', name_='Option_Record_Field_Value', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Option_Record_Field_Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Option_Record_Field_Value.append(obj_)
# end class OptionCollectionElementType

class NetflowV5PacketType(GeneratedsSuper):
    """Defines the contents of a Netflow v5 packet. As of 2012, Netflow v5
    is still the most commonly used network flow format. Netflow v5
    was developed by Cisco.
    http://netflow.caligare.com/netflow_v5.htm"""

    subclass = None
    superclass = None
    def __init__(self, Flow_Header=None, Flow_Record=None):
        self.Flow_Header = Flow_Header
        if Flow_Record is None:
            self.Flow_Record = []
        else:
            self.Flow_Record = Flow_Record
    def factory(*args_, **kwargs_):
        if NetflowV5PacketType.subclass:
            return NetflowV5PacketType.subclass(*args_, **kwargs_)
        else:
            return NetflowV5PacketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Header(self): return self.Flow_Header
    def set_Flow_Header(self, Flow_Header): self.Flow_Header = Flow_Header
    def get_Flow_Record(self): return self.Flow_Record
    def set_Flow_Record(self, Flow_Record): self.Flow_Record = Flow_Record
    def add_Flow_Record(self, value): self.Flow_Record.append(value)
    def insert_Flow_Record(self, index, value): self.Flow_Record[index] = value
    def hasContent_(self):
        if (
            self.Flow_Header is not None or
            self.Flow_Record
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5PacketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV5PacketType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV5PacketType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5PacketType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow_Header is not None:
            self.Flow_Header.export(lwrite, level, 'NetFlowObj:', name_='Flow_Header', pretty_print=pretty_print)
        for Flow_Record_ in self.Flow_Record:
            Flow_Record_.export(lwrite, level, 'NetFlowObj:', name_='Flow_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Header':
            obj_ = NetflowV5FlowHeaderType.factory()
            obj_.build(child_)
            self.set_Flow_Header(obj_)
        elif nodeName_ == 'Flow_Record':
            obj_ = NetflowV5FlowRecordType.factory()
            obj_.build(child_)
            self.Flow_Record.append(obj_)
# end class NetflowV5PacketType

class NetflowV5FlowHeaderType(GeneratedsSuper):
    """Defines elements of a netflow v5 header.
    http://netflow.caligare.com/netflow_v5.htm"""

    subclass = None
    superclass = None
    def __init__(self, Version=None, Count=None, Sys_Up_Time=None, Unix_Secs=None, Unix_Nsecs=None, Flow_Sequence=None, Engine_Type=None, Engine_ID=None, Sampling_Interval=None):
        if Version is None:
            self.Version = globals()['cybox_common.HexBinaryObjectPropertyType']('05')
        else:
            self.Version = Version
        self.Count = Count
        self.Sys_Up_Time = Sys_Up_Time
        self.Unix_Secs = Unix_Secs
        self.Unix_Nsecs = Unix_Nsecs
        self.Flow_Sequence = Flow_Sequence
        self.Engine_Type = Engine_Type
        self.Engine_ID = Engine_ID
        self.Sampling_Interval = Sampling_Interval
    def factory(*args_, **kwargs_):
        if NetflowV5FlowHeaderType.subclass:
            return NetflowV5FlowHeaderType.subclass(*args_, **kwargs_)
        else:
            return NetflowV5FlowHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Count(self): return self.Count
    def set_Count(self, Count): self.Count = Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Sys_Up_Time(self): return self.Sys_Up_Time
    def set_Sys_Up_Time(self, Sys_Up_Time): self.Sys_Up_Time = Sys_Up_Time
    def get_Unix_Secs(self): return self.Unix_Secs
    def set_Unix_Secs(self, Unix_Secs): self.Unix_Secs = Unix_Secs
    def get_Unix_Nsecs(self): return self.Unix_Nsecs
    def set_Unix_Nsecs(self, Unix_Nsecs): self.Unix_Nsecs = Unix_Nsecs
    def get_Flow_Sequence(self): return self.Flow_Sequence
    def set_Flow_Sequence(self, Flow_Sequence): self.Flow_Sequence = Flow_Sequence
    def get_Engine_Type(self): return self.Engine_Type
    def set_Engine_Type(self, Engine_Type): self.Engine_Type = Engine_Type
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Engine_ID(self): return self.Engine_ID
    def set_Engine_ID(self, Engine_ID): self.Engine_ID = Engine_ID
    def get_Sampling_Interval(self): return self.Sampling_Interval
    def set_Sampling_Interval(self, Sampling_Interval): self.Sampling_Interval = Sampling_Interval
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Count is not None or
            self.Sys_Up_Time is not None or
            self.Unix_Secs is not None or
            self.Unix_Nsecs is not None or
            self.Flow_Sequence is not None or
            self.Engine_Type is not None or
            self.Engine_ID is not None or
            self.Sampling_Interval is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5FlowHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV5FlowHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV5FlowHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5FlowHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            self.Version.export(lwrite, level, 'NetFlowObj:', name_='Version', pretty_print=pretty_print)
        if self.Count is not None:
            self.Count.export(lwrite, level, 'NetFlowObj:', name_='Count', pretty_print=pretty_print)
        if self.Sys_Up_Time is not None:
            self.Sys_Up_Time.export(lwrite, level, 'NetFlowObj:', name_='Sys_Up_Time', pretty_print=pretty_print)
        if self.Unix_Secs is not None:
            self.Unix_Secs.export(lwrite, level, 'NetFlowObj:', name_='Unix_Secs', pretty_print=pretty_print)
        if self.Unix_Nsecs is not None:
            self.Unix_Nsecs.export(lwrite, level, 'NetFlowObj:', name_='Unix_Nsecs', pretty_print=pretty_print)
        if self.Flow_Sequence is not None:
            self.Flow_Sequence.export(lwrite, level, 'NetFlowObj:', name_='Flow_Sequence', pretty_print=pretty_print)
        if self.Engine_Type is not None:
            self.Engine_Type.export(lwrite, level, 'NetFlowObj:', name_='Engine_Type', pretty_print=pretty_print)
        if self.Engine_ID is not None:
            self.Engine_ID.export(lwrite, level, 'NetFlowObj:', name_='Engine_ID', pretty_print=pretty_print)
        if self.Sampling_Interval is not None:
            self.Sampling_Interval.export(lwrite, level, 'NetFlowObj:', name_='Sampling_Interval', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Version':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Count(obj_)
        elif nodeName_ == 'Sys_Up_Time':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sys_Up_Time(obj_)
        elif nodeName_ == 'Unix_Secs':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Unix_Secs(obj_)
        elif nodeName_ == 'Unix_Nsecs':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Unix_Nsecs(obj_)
        elif nodeName_ == 'Flow_Sequence':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Sequence(obj_)
        elif nodeName_ == 'Engine_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Engine_Type(obj_)
        elif nodeName_ == 'Engine_ID':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Engine_ID(obj_)
        elif nodeName_ == 'Sampling_Interval':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sampling_Interval(obj_)
# end class NetflowV5FlowHeaderType

class NetflowV5FlowRecordType(GeneratedsSuper):
    """Defines elements of a Netflow v5 flow record. Recall that the seven
    elements that define the flow itself (e.g., source IP address)
    are provided in NetworkFlowLabelType. https://bto.bluecoat.com/p
    acketguide/8.6/info/netflow5-records.htm"""

    subclass = None
    superclass = None
    def __init__(self, Nexthop_IPv4_Addr=None, Packet_Count=None, Byte_Count=None, SysUpTime_Start=None, SysUpTime_End=None, Padding1=None, TCP_Flags=None, Src_Autonomous_System=None, Dest_Autonomous_System=None, Src_IP_Mask_Bit_Count=None, Dest_IP_Mask_Bit_Count=None, Padding2=None):
        self.Nexthop_IPv4_Addr = Nexthop_IPv4_Addr
        self.Packet_Count = Packet_Count
        self.Byte_Count = Byte_Count
        self.SysUpTime_Start = SysUpTime_Start
        self.SysUpTime_End = SysUpTime_End
        self.Padding1 = Padding1
        self.TCP_Flags = TCP_Flags
        self.Src_Autonomous_System = Src_Autonomous_System
        self.Dest_Autonomous_System = Dest_Autonomous_System
        self.Src_IP_Mask_Bit_Count = Src_IP_Mask_Bit_Count
        self.Dest_IP_Mask_Bit_Count = Dest_IP_Mask_Bit_Count
        self.Padding2 = Padding2
    def factory(*args_, **kwargs_):
        if NetflowV5FlowRecordType.subclass:
            return NetflowV5FlowRecordType.subclass(*args_, **kwargs_)
        else:
            return NetflowV5FlowRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Nexthop_IPv4_Addr(self): return self.Nexthop_IPv4_Addr
    def set_Nexthop_IPv4_Addr(self, Nexthop_IPv4_Addr): self.Nexthop_IPv4_Addr = Nexthop_IPv4_Addr
    def get_Packet_Count(self): return self.Packet_Count
    def set_Packet_Count(self, Packet_Count): self.Packet_Count = Packet_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Byte_Count(self): return self.Byte_Count
    def set_Byte_Count(self, Byte_Count): self.Byte_Count = Byte_Count
    def get_SysUpTime_Start(self): return self.SysUpTime_Start
    def set_SysUpTime_Start(self, SysUpTime_Start): self.SysUpTime_Start = SysUpTime_Start
    def get_SysUpTime_End(self): return self.SysUpTime_End
    def set_SysUpTime_End(self, SysUpTime_End): self.SysUpTime_End = SysUpTime_End
    def get_Padding1(self): return self.Padding1
    def set_Padding1(self, Padding1): self.Padding1 = Padding1
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_TCP_Flags(self): return self.TCP_Flags
    def set_TCP_Flags(self, TCP_Flags): self.TCP_Flags = TCP_Flags
    def get_Src_Autonomous_System(self): return self.Src_Autonomous_System
    def set_Src_Autonomous_System(self, Src_Autonomous_System): self.Src_Autonomous_System = Src_Autonomous_System
    def get_Dest_Autonomous_System(self): return self.Dest_Autonomous_System
    def set_Dest_Autonomous_System(self, Dest_Autonomous_System): self.Dest_Autonomous_System = Dest_Autonomous_System
    def get_Src_IP_Mask_Bit_Count(self): return self.Src_IP_Mask_Bit_Count
    def set_Src_IP_Mask_Bit_Count(self, Src_IP_Mask_Bit_Count): self.Src_IP_Mask_Bit_Count = Src_IP_Mask_Bit_Count
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Dest_IP_Mask_Bit_Count(self): return self.Dest_IP_Mask_Bit_Count
    def set_Dest_IP_Mask_Bit_Count(self, Dest_IP_Mask_Bit_Count): self.Dest_IP_Mask_Bit_Count = Dest_IP_Mask_Bit_Count
    def get_Padding2(self): return self.Padding2
    def set_Padding2(self, Padding2): self.Padding2 = Padding2
    def hasContent_(self):
        if (
            self.Nexthop_IPv4_Addr is not None or
            self.Packet_Count is not None or
            self.Byte_Count is not None or
            self.SysUpTime_Start is not None or
            self.SysUpTime_End is not None or
            self.Padding1 is not None or
            self.TCP_Flags is not None or
            self.Src_Autonomous_System is not None or
            self.Dest_Autonomous_System is not None or
            self.Src_IP_Mask_Bit_Count is not None or
            self.Dest_IP_Mask_Bit_Count is not None or
            self.Padding2 is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5FlowRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV5FlowRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV5FlowRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV5FlowRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Nexthop_IPv4_Addr is not None:
            self.Nexthop_IPv4_Addr.export(lwrite, level, 'NetFlowObj:', name_='Nexthop_IPv4_Addr', pretty_print=pretty_print)
        if self.Packet_Count is not None:
            self.Packet_Count.export(lwrite, level, 'NetFlowObj:', name_='Packet_Count', pretty_print=pretty_print)
        if self.Byte_Count is not None:
            self.Byte_Count.export(lwrite, level, 'NetFlowObj:', name_='Byte_Count', pretty_print=pretty_print)
        if self.SysUpTime_Start is not None:
            self.SysUpTime_Start.export(lwrite, level, 'NetFlowObj:', name_='SysUpTime_Start', pretty_print=pretty_print)
        if self.SysUpTime_End is not None:
            self.SysUpTime_End.export(lwrite, level, 'NetFlowObj:', name_='SysUpTime_End', pretty_print=pretty_print)
        if self.Padding1 is not None:
            self.Padding1.export(lwrite, level, 'NetFlowObj:', name_='Padding1', pretty_print=pretty_print)
        if self.TCP_Flags is not None:
            self.TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='TCP_Flags', pretty_print=pretty_print)
        if self.Src_Autonomous_System is not None:
            self.Src_Autonomous_System.export(lwrite, level, 'NetFlowObj:', name_='Src_Autonomous_System', pretty_print=pretty_print)
        if self.Dest_Autonomous_System is not None:
            self.Dest_Autonomous_System.export(lwrite, level, 'NetFlowObj:', name_='Dest_Autonomous_System', pretty_print=pretty_print)
        if self.Src_IP_Mask_Bit_Count is not None:
            self.Src_IP_Mask_Bit_Count.export(lwrite, level, 'NetFlowObj:', name_='Src_IP_Mask_Bit_Count', pretty_print=pretty_print)
        if self.Dest_IP_Mask_Bit_Count is not None:
            self.Dest_IP_Mask_Bit_Count.export(lwrite, level, 'NetFlowObj:', name_='Dest_IP_Mask_Bit_Count', pretty_print=pretty_print)
        if self.Padding2 is not None:
            self.Padding2.export(lwrite, level, 'NetFlowObj:', name_='Padding2', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Nexthop_IPv4_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Nexthop_IPv4_Addr(obj_)
        elif nodeName_ == 'Packet_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Packet_Count(obj_)
        elif nodeName_ == 'Byte_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Byte_Count(obj_)
        elif nodeName_ == 'SysUpTime_Start':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SysUpTime_Start(obj_)
        elif nodeName_ == 'SysUpTime_End':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SysUpTime_End(obj_)
        elif nodeName_ == 'Padding1':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding1(obj_)
        elif nodeName_ == 'TCP_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TCP_Flags(obj_)
        elif nodeName_ == 'Src_Autonomous_System':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Src_Autonomous_System(obj_)
        elif nodeName_ == 'Dest_Autonomous_System':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Dest_Autonomous_System(obj_)
        elif nodeName_ == 'Src_IP_Mask_Bit_Count':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Src_IP_Mask_Bit_Count(obj_)
        elif nodeName_ == 'Dest_IP_Mask_Bit_Count':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Dest_IP_Mask_Bit_Count(obj_)
        elif nodeName_ == 'Padding2':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Padding2(obj_)
# end class NetflowV5FlowRecordType

class SiLKRecordType(GeneratedsSuper):
    """System for Internet-Level Knowledge (CMU/SEI). The fields are taken
    from a list shown in
    http://tools.netsa.cert.org/silk/rwcut.html. Fields common to
    all network flows are defined in NetworkFlowLabelType (e.g.,
    source IP, SNMP ingress, etc.). For additional references, see
    http://tools.netsa.cert.org/silk/analysis-handbook.pdf,
    http://tools.netsa.cert.org/silk/faq.html#ipfix-fields."""

    subclass = None
    superclass = None
    def __init__(self, Packet_Count=None, Byte_Count=None, TCP_Flags=None, Start_Time=None, Duration=None, End_Time=None, Sensor_Info=None, ICMP_Type=None, ICMP_Code=None, Router_Next_Hop_IP=None, Initial_TCP_Flags=None, Session_TCP_Flags=None, Flow_Attributes=None, Flow_Application=None, Src_IP_Type=None, Dest_IP_Type=None, Src_Country_Code=None, Dest_Country_Code=None, Src_MAPNAME=None, Dest_MAPNAME=None):
        self.Packet_Count = Packet_Count
        self.Byte_Count = Byte_Count
        self.TCP_Flags = TCP_Flags
        self.Start_Time = Start_Time
        self.Duration = Duration
        self.End_Time = End_Time
        self.Sensor_Info = Sensor_Info
        self.ICMP_Type = ICMP_Type
        self.ICMP_Code = ICMP_Code
        self.Router_Next_Hop_IP = Router_Next_Hop_IP
        self.Initial_TCP_Flags = Initial_TCP_Flags
        self.Session_TCP_Flags = Session_TCP_Flags
        self.Flow_Attributes = Flow_Attributes
        self.Flow_Application = Flow_Application
        self.Src_IP_Type = Src_IP_Type
        self.Dest_IP_Type = Dest_IP_Type
        self.Src_Country_Code = Src_Country_Code
        self.Dest_Country_Code = Dest_Country_Code
        self.Src_MAPNAME = Src_MAPNAME
        self.Dest_MAPNAME = Dest_MAPNAME
    def factory(*args_, **kwargs_):
        if SiLKRecordType.subclass:
            return SiLKRecordType.subclass(*args_, **kwargs_)
        else:
            return SiLKRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Packet_Count(self): return self.Packet_Count
    def set_Packet_Count(self, Packet_Count): self.Packet_Count = Packet_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Byte_Count(self): return self.Byte_Count
    def set_Byte_Count(self, Byte_Count): self.Byte_Count = Byte_Count
    def get_TCP_Flags(self): return self.TCP_Flags
    def set_TCP_Flags(self, TCP_Flags): self.TCP_Flags = TCP_Flags
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Start_Time(self): return self.Start_Time
    def set_Start_Time(self, Start_Time): self.Start_Time = Start_Time
    def get_Duration(self): return self.Duration
    def set_Duration(self, Duration): self.Duration = Duration
    def get_End_Time(self): return self.End_Time
    def set_End_Time(self, End_Time): self.End_Time = End_Time
    def get_Sensor_Info(self): return self.Sensor_Info
    def set_Sensor_Info(self, Sensor_Info): self.Sensor_Info = Sensor_Info
    def get_ICMP_Type(self): return self.ICMP_Type
    def set_ICMP_Type(self, ICMP_Type): self.ICMP_Type = ICMP_Type
    def get_ICMP_Code(self): return self.ICMP_Code
    def set_ICMP_Code(self, ICMP_Code): self.ICMP_Code = ICMP_Code
    def get_Router_Next_Hop_IP(self): return self.Router_Next_Hop_IP
    def set_Router_Next_Hop_IP(self, Router_Next_Hop_IP): self.Router_Next_Hop_IP = Router_Next_Hop_IP
    def get_Initial_TCP_Flags(self): return self.Initial_TCP_Flags
    def set_Initial_TCP_Flags(self, Initial_TCP_Flags): self.Initial_TCP_Flags = Initial_TCP_Flags
    def get_Session_TCP_Flags(self): return self.Session_TCP_Flags
    def set_Session_TCP_Flags(self, Session_TCP_Flags): self.Session_TCP_Flags = Session_TCP_Flags
    def get_Flow_Attributes(self): return self.Flow_Attributes
    def set_Flow_Attributes(self, Flow_Attributes): self.Flow_Attributes = Flow_Attributes
    def validate_SiLKFlowAttributesType(self, value):
        # Validate type SiLKFlowAttributesType, a restriction on None.
        pass
    def get_Flow_Application(self): return self.Flow_Application
    def set_Flow_Application(self, Flow_Application): self.Flow_Application = Flow_Application
    def validate_IANAPortNumberRegistryType(self, value):
        # Validate type network_packet_object.IANAPortNumberRegistryType, a restriction on None.
        pass
    def get_Src_IP_Type(self): return self.Src_IP_Type
    def set_Src_IP_Type(self, Src_IP_Type): self.Src_IP_Type = Src_IP_Type
    def validate_SiLKAddressType(self, value):
        # Validate type SiLKAddressType, a restriction on None.
        pass
    def get_Dest_IP_Type(self): return self.Dest_IP_Type
    def set_Dest_IP_Type(self, Dest_IP_Type): self.Dest_IP_Type = Dest_IP_Type
    def get_Src_Country_Code(self): return self.Src_Country_Code
    def set_Src_Country_Code(self, Src_Country_Code): self.Src_Country_Code = Src_Country_Code
    def validate_SiLKCountryCodeType(self, value):
        # Validate type SiLKCountryCodeType, a restriction on None.
        pass
    def get_Dest_Country_Code(self): return self.Dest_Country_Code
    def set_Dest_Country_Code(self, Dest_Country_Code): self.Dest_Country_Code = Dest_Country_Code
    def get_Src_MAPNAME(self): return self.Src_MAPNAME
    def set_Src_MAPNAME(self, Src_MAPNAME): self.Src_MAPNAME = Src_MAPNAME
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Dest_MAPNAME(self): return self.Dest_MAPNAME
    def set_Dest_MAPNAME(self, Dest_MAPNAME): self.Dest_MAPNAME = Dest_MAPNAME
    def hasContent_(self):
        if (
            self.Packet_Count is not None or
            self.Byte_Count is not None or
            self.TCP_Flags is not None or
            self.Start_Time is not None or
            self.Duration is not None or
            self.End_Time is not None or
            self.Sensor_Info is not None or
            self.ICMP_Type is not None or
            self.ICMP_Code is not None or
            self.Router_Next_Hop_IP is not None or
            self.Initial_TCP_Flags is not None or
            self.Session_TCP_Flags is not None or
            self.Flow_Attributes is not None or
            self.Flow_Application is not None or
            self.Src_IP_Type is not None or
            self.Dest_IP_Type is not None or
            self.Src_Country_Code is not None or
            self.Dest_Country_Code is not None or
            self.Src_MAPNAME is not None or
            self.Dest_MAPNAME is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Packet_Count is not None:
            self.Packet_Count.export(lwrite, level, 'NetFlowObj:', name_='Packet_Count', pretty_print=pretty_print)
        if self.Byte_Count is not None:
            self.Byte_Count.export(lwrite, level, 'NetFlowObj:', name_='Byte_Count', pretty_print=pretty_print)
        if self.TCP_Flags is not None:
            self.TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='TCP_Flags', pretty_print=pretty_print)
        if self.Start_Time is not None:
            self.Start_Time.export(lwrite, level, 'NetFlowObj:', name_='Start_Time', pretty_print=pretty_print)
        if self.Duration is not None:
            self.Duration.export(lwrite, level, 'NetFlowObj:', name_='Duration', pretty_print=pretty_print)
        if self.End_Time is not None:
            self.End_Time.export(lwrite, level, 'NetFlowObj:', name_='End_Time', pretty_print=pretty_print)
        if self.Sensor_Info is not None:
            self.Sensor_Info.export(lwrite, level, 'NetFlowObj:', name_='Sensor_Info', pretty_print=pretty_print)
        if self.ICMP_Type is not None:
            self.ICMP_Type.export(lwrite, level, 'NetFlowObj:', name_='ICMP_Type', pretty_print=pretty_print)
        if self.ICMP_Code is not None:
            self.ICMP_Code.export(lwrite, level, 'NetFlowObj:', name_='ICMP_Code', pretty_print=pretty_print)
        if self.Router_Next_Hop_IP is not None:
            self.Router_Next_Hop_IP.export(lwrite, level, 'NetFlowObj:', name_='Router_Next_Hop_IP', pretty_print=pretty_print)
        if self.Initial_TCP_Flags is not None:
            self.Initial_TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='Initial_TCP_Flags', pretty_print=pretty_print)
        if self.Session_TCP_Flags is not None:
            self.Session_TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='Session_TCP_Flags', pretty_print=pretty_print)
        if self.Flow_Attributes is not None:
            self.Flow_Attributes.export(lwrite, level, 'NetFlowObj:', name_='Flow_Attributes', pretty_print=pretty_print)
        if self.Flow_Application is not None:
            self.Flow_Application.export(lwrite, level, 'NetFlowObj:', name_='Flow_Application', pretty_print=pretty_print)
        if self.Src_IP_Type is not None:
            self.Src_IP_Type.export(lwrite, level, 'NetFlowObj:', name_='Src_IP_Type', pretty_print=pretty_print)
        if self.Dest_IP_Type is not None:
            self.Dest_IP_Type.export(lwrite, level, 'NetFlowObj:', name_='Dest_IP_Type', pretty_print=pretty_print)
        if self.Src_Country_Code is not None:
            self.Src_Country_Code.export(lwrite, level, 'NetFlowObj:', name_='Src_Country_Code', pretty_print=pretty_print)
        if self.Dest_Country_Code is not None:
            self.Dest_Country_Code.export(lwrite, level, 'NetFlowObj:', name_='Dest_Country_Code', pretty_print=pretty_print)
        if self.Src_MAPNAME is not None:
            self.Src_MAPNAME.export(lwrite, level, 'NetFlowObj:', name_='Src_MAPNAME', pretty_print=pretty_print)
        if self.Dest_MAPNAME is not None:
            self.Dest_MAPNAME.export(lwrite, level, 'NetFlowObj:', name_='Dest_MAPNAME', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Packet_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Packet_Count(obj_)
        elif nodeName_ == 'Byte_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Byte_Count(obj_)
        elif nodeName_ == 'TCP_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TCP_Flags(obj_)
        elif nodeName_ == 'Start_Time':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Start_Time(obj_)
        elif nodeName_ == 'Duration':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Duration(obj_)
        elif nodeName_ == 'End_Time':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_End_Time(obj_)
        elif nodeName_ == 'Sensor_Info':
            obj_ = SiLKSensorInfoType.factory()
            obj_.build(child_)
            self.set_Sensor_Info(obj_)
        elif nodeName_ == 'ICMP_Type':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ICMP_Type(obj_)
        elif nodeName_ == 'ICMP_Code':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ICMP_Code(obj_)
        elif nodeName_ == 'Router_Next_Hop_IP':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Router_Next_Hop_IP(obj_)
        elif nodeName_ == 'Initial_TCP_Flags':
            obj_ = network_packet_object.TCPFlagsType.factory()
            obj_.build(child_)
            self.set_Initial_TCP_Flags(obj_)
        elif nodeName_ == 'Session_TCP_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Session_TCP_Flags(obj_)
        elif nodeName_ == 'Flow_Attributes':
            obj_ = SiLKFlowAttributesType.factory()
            obj_.build(child_)
            self.set_Flow_Attributes(obj_)
        elif nodeName_ == 'Flow_Application':
            obj_ = network_packet_object.IANAPortNumberRegistryType.factory()
            obj_.build(child_)
            self.set_Flow_Application(obj_)
        elif nodeName_ == 'Src_IP_Type':
            obj_ = SiLKAddressType.factory()
            obj_.build(child_)
            self.set_Src_IP_Type(obj_)
        elif nodeName_ == 'Dest_IP_Type':
            obj_ = SiLKAddressType.factory()
            obj_.build(child_)
            self.set_Dest_IP_Type(obj_)
        elif nodeName_ == 'Src_Country_Code':
            obj_ = SiLKCountryCodeType.factory()
            obj_.build(child_)
            self.set_Src_Country_Code(obj_)
        elif nodeName_ == 'Dest_Country_Code':
            obj_ = SiLKCountryCodeType.factory()
            obj_.build(child_)
            self.set_Dest_Country_Code(obj_)
        elif nodeName_ == 'Src_MAPNAME':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Src_MAPNAME(obj_)
        elif nodeName_ == 'Dest_MAPNAME':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Dest_MAPNAME(obj_)
# end class SiLKRecordType

class SiLKSensorInfoType(GeneratedsSuper):
    """Defines elements associated with a SiLK sensor."""

    subclass = None
    superclass = None
    def __init__(self, Sensor_ID=None, Class=None, Type=None):
        self.Sensor_ID = Sensor_ID
        self.Class = Class
        self.Type = Type
    def factory(*args_, **kwargs_):
        if SiLKSensorInfoType.subclass:
            return SiLKSensorInfoType.subclass(*args_, **kwargs_)
        else:
            return SiLKSensorInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Sensor_ID(self): return self.Sensor_ID
    def set_Sensor_ID(self, Sensor_ID): self.Sensor_ID = Sensor_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Class(self): return self.Class
    def set_Class(self, Class): self.Class = Class
    def validate_SiLKSensorClassType(self, value):
        # Validate type SiLKSensorClassType, a restriction on None.
        pass
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_SiLKDirectionType(self, value):
        # Validate type SiLKDirectionType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Sensor_ID is not None or
            self.Class is not None or
            self.Type is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKSensorInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKSensorInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKSensorInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKSensorInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Sensor_ID is not None:
            self.Sensor_ID.export(lwrite, level, 'NetFlowObj:', name_='Sensor_ID', pretty_print=pretty_print)
        if self.Class is not None:
            self.Class.export(lwrite, level, 'NetFlowObj:', name_='Class', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'NetFlowObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Sensor_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sensor_ID(obj_)
        elif nodeName_ == 'Class':
            obj_ = SiLKSensorClassType.factory()
            obj_.build(child_)
            self.set_Class(obj_)
        elif nodeName_ == 'Type':
            obj_ = SiLKDirectionType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
# end class SiLKSensorInfoType

class YAFRecordType(GeneratedsSuper):
    """YAF (Yet Another Flowmeter) is bidirectional network flow meter. It
    processes packet data from pcap(3) dumpfiles as generated by
    tcpdump(1) or via live capture from an interface using pcap(3)
    into bidirectional flows, then exports those flows to IPFIX.
    (REF:
    http://www.usenix.org/event/lisa10/tech/full_papers/Inacio.pdf)"""

    subclass = None
    superclass = None
    def __init__(self, Flow=None, Reverse_Flow=None):
        self.Flow = Flow
        self.Reverse_Flow = Reverse_Flow
    def factory(*args_, **kwargs_):
        if YAFRecordType.subclass:
            return YAFRecordType.subclass(*args_, **kwargs_)
        else:
            return YAFRecordType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow(self): return self.Flow
    def set_Flow(self, Flow): self.Flow = Flow
    def get_Reverse_Flow(self): return self.Reverse_Flow
    def set_Reverse_Flow(self, Reverse_Flow): self.Reverse_Flow = Reverse_Flow
    def hasContent_(self):
        if (
            self.Flow is not None or
            self.Reverse_Flow is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFRecordType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='YAFRecordType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='YAFRecordType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFRecordType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow is not None:
            self.Flow.export(lwrite, level, 'NetFlowObj:', name_='Flow', pretty_print=pretty_print)
        if self.Reverse_Flow is not None:
            self.Reverse_Flow.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Flow', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow':
            obj_ = YAFFlowType.factory()
            obj_.build(child_)
            self.set_Flow(obj_)
        elif nodeName_ == 'Reverse_Flow':
            obj_ = YAFReverseFlowType.factory()
            obj_.build(child_)
            self.set_Reverse_Flow(obj_)
# end class YAFRecordType

class YAFFlowType(GeneratedsSuper):
    """These elements of a YAF record correspond to the flow generally or
    to the forward portion of the flow. Elements common to all
    network flow objects are defined in the NetworkFlowLabelType
    (src ip address, ingress/egress interface)."""

    subclass = None
    superclass = None
    def __init__(self, Flow_Start_Milliseconds=None, Flow_End_Milliseconds=None, Octet_Total_Count=None, Packet_Total_Count=None, Flow_End_Reason=None, SiLK_App_Label=None, Payload_Entropy=None, ML_App_Label=None, TCP_Flow=None, Vlan_ID_MAC_Addr=None, Passive_OS_Fingerprinting=None, First_Packet_Banner=None, Second_Packet_Banner=None, N_Bytes_Payload=None):
        self.Flow_Start_Milliseconds = Flow_Start_Milliseconds
        self.Flow_End_Milliseconds = Flow_End_Milliseconds
        self.Octet_Total_Count = Octet_Total_Count
        self.Packet_Total_Count = Packet_Total_Count
        self.Flow_End_Reason = Flow_End_Reason
        self.SiLK_App_Label = SiLK_App_Label
        self.Payload_Entropy = Payload_Entropy
        self.ML_App_Label = ML_App_Label
        self.TCP_Flow = TCP_Flow
        self.Vlan_ID_MAC_Addr = Vlan_ID_MAC_Addr
        self.Passive_OS_Fingerprinting = Passive_OS_Fingerprinting
        self.First_Packet_Banner = First_Packet_Banner
        self.Second_Packet_Banner = Second_Packet_Banner
        self.N_Bytes_Payload = N_Bytes_Payload
    def factory(*args_, **kwargs_):
        if YAFFlowType.subclass:
            return YAFFlowType.subclass(*args_, **kwargs_)
        else:
            return YAFFlowType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Flow_Start_Milliseconds(self): return self.Flow_Start_Milliseconds
    def set_Flow_Start_Milliseconds(self, Flow_Start_Milliseconds): self.Flow_Start_Milliseconds = Flow_Start_Milliseconds
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Flow_End_Milliseconds(self): return self.Flow_End_Milliseconds
    def set_Flow_End_Milliseconds(self, Flow_End_Milliseconds): self.Flow_End_Milliseconds = Flow_End_Milliseconds
    def get_Octet_Total_Count(self): return self.Octet_Total_Count
    def set_Octet_Total_Count(self, Octet_Total_Count): self.Octet_Total_Count = Octet_Total_Count
    def get_Packet_Total_Count(self): return self.Packet_Total_Count
    def set_Packet_Total_Count(self, Packet_Total_Count): self.Packet_Total_Count = Packet_Total_Count
    def get_Flow_End_Reason(self): return self.Flow_End_Reason
    def set_Flow_End_Reason(self, Flow_End_Reason): self.Flow_End_Reason = Flow_End_Reason
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_SiLK_App_Label(self): return self.SiLK_App_Label
    def set_SiLK_App_Label(self, SiLK_App_Label): self.SiLK_App_Label = SiLK_App_Label
    def get_Payload_Entropy(self): return self.Payload_Entropy
    def set_Payload_Entropy(self, Payload_Entropy): self.Payload_Entropy = Payload_Entropy
    def get_ML_App_Label(self): return self.ML_App_Label
    def set_ML_App_Label(self, ML_App_Label): self.ML_App_Label = ML_App_Label
    def get_TCP_Flow(self): return self.TCP_Flow
    def set_TCP_Flow(self, TCP_Flow): self.TCP_Flow = TCP_Flow
    def get_Vlan_ID_MAC_Addr(self): return self.Vlan_ID_MAC_Addr
    def set_Vlan_ID_MAC_Addr(self, Vlan_ID_MAC_Addr): self.Vlan_ID_MAC_Addr = Vlan_ID_MAC_Addr
    def get_Passive_OS_Fingerprinting(self): return self.Passive_OS_Fingerprinting
    def set_Passive_OS_Fingerprinting(self, Passive_OS_Fingerprinting): self.Passive_OS_Fingerprinting = Passive_OS_Fingerprinting
    def get_First_Packet_Banner(self): return self.First_Packet_Banner
    def set_First_Packet_Banner(self, First_Packet_Banner): self.First_Packet_Banner = First_Packet_Banner
    def get_Second_Packet_Banner(self): return self.Second_Packet_Banner
    def set_Second_Packet_Banner(self, Second_Packet_Banner): self.Second_Packet_Banner = Second_Packet_Banner
    def get_N_Bytes_Payload(self): return self.N_Bytes_Payload
    def set_N_Bytes_Payload(self, N_Bytes_Payload): self.N_Bytes_Payload = N_Bytes_Payload
    def hasContent_(self):
        if (
            self.Flow_Start_Milliseconds is not None or
            self.Flow_End_Milliseconds is not None or
            self.Octet_Total_Count is not None or
            self.Packet_Total_Count is not None or
            self.Flow_End_Reason is not None or
            self.SiLK_App_Label is not None or
            self.Payload_Entropy is not None or
            self.ML_App_Label is not None or
            self.TCP_Flow is not None or
            self.Vlan_ID_MAC_Addr is not None or
            self.Passive_OS_Fingerprinting is not None or
            self.First_Packet_Banner is not None or
            self.Second_Packet_Banner is not None or
            self.N_Bytes_Payload is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFFlowType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='YAFFlowType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='YAFFlowType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFFlowType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Flow_Start_Milliseconds is not None:
            self.Flow_Start_Milliseconds.export(lwrite, level, 'NetFlowObj:', name_='Flow_Start_Milliseconds', pretty_print=pretty_print)
        if self.Flow_End_Milliseconds is not None:
            self.Flow_End_Milliseconds.export(lwrite, level, 'NetFlowObj:', name_='Flow_End_Milliseconds', pretty_print=pretty_print)
        if self.Octet_Total_Count is not None:
            self.Octet_Total_Count.export(lwrite, level, 'NetFlowObj:', name_='Octet_Total_Count', pretty_print=pretty_print)
        if self.Packet_Total_Count is not None:
            self.Packet_Total_Count.export(lwrite, level, 'NetFlowObj:', name_='Packet_Total_Count', pretty_print=pretty_print)
        if self.Flow_End_Reason is not None:
            self.Flow_End_Reason.export(lwrite, level, 'NetFlowObj:', name_='Flow_End_Reason', pretty_print=pretty_print)
        if self.SiLK_App_Label is not None:
            self.SiLK_App_Label.export(lwrite, level, 'NetFlowObj:', name_='SiLK_App_Label', pretty_print=pretty_print)
        if self.Payload_Entropy is not None:
            self.Payload_Entropy.export(lwrite, level, 'NetFlowObj:', name_='Payload_Entropy', pretty_print=pretty_print)
        if self.ML_App_Label is not None:
            self.ML_App_Label.export(lwrite, level, 'NetFlowObj:', name_='ML_App_Label', pretty_print=pretty_print)
        if self.TCP_Flow is not None:
            self.TCP_Flow.export(lwrite, level, 'NetFlowObj:', name_='TCP_Flow', pretty_print=pretty_print)
        if self.Vlan_ID_MAC_Addr is not None:
            self.Vlan_ID_MAC_Addr.export(lwrite, level, 'NetFlowObj:', name_='Vlan_ID_MAC_Addr', pretty_print=pretty_print)
        if self.Passive_OS_Fingerprinting is not None:
            self.Passive_OS_Fingerprinting.export(lwrite, level, 'NetFlowObj:', name_='Passive_OS_Fingerprinting', pretty_print=pretty_print)
        if self.First_Packet_Banner is not None:
            self.First_Packet_Banner.export(lwrite, level, 'NetFlowObj:', name_='First_Packet_Banner', pretty_print=pretty_print)
        if self.Second_Packet_Banner is not None:
            self.Second_Packet_Banner.export(lwrite, level, 'NetFlowObj:', name_='Second_Packet_Banner', pretty_print=pretty_print)
        if self.N_Bytes_Payload is not None:
            self.N_Bytes_Payload.export(lwrite, level, 'NetFlowObj:', name_='N_Bytes_Payload', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Flow_Start_Milliseconds':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_Start_Milliseconds(obj_)
        elif nodeName_ == 'Flow_End_Milliseconds':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_End_Milliseconds(obj_)
        elif nodeName_ == 'Octet_Total_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Octet_Total_Count(obj_)
        elif nodeName_ == 'Packet_Total_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Packet_Total_Count(obj_)
        elif nodeName_ == 'Flow_End_Reason':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Flow_End_Reason(obj_)
        elif nodeName_ == 'SiLK_App_Label':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SiLK_App_Label(obj_)
        elif nodeName_ == 'Payload_Entropy':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Payload_Entropy(obj_)
        elif nodeName_ == 'ML_App_Label':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ML_App_Label(obj_)
        elif nodeName_ == 'TCP_Flow':
            obj_ = YAFTCPFlowType.factory()
            obj_.build(child_)
            self.set_TCP_Flow(obj_)
        elif nodeName_ == 'Vlan_ID_MAC_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Vlan_ID_MAC_Addr(obj_)
        elif nodeName_ == 'Passive_OS_Fingerprinting':
            obj_ = cybox_common.PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Passive_OS_Fingerprinting(obj_)
        elif nodeName_ == 'First_Packet_Banner':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_First_Packet_Banner(obj_)
        elif nodeName_ == 'Second_Packet_Banner':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Second_Packet_Banner(obj_)
        elif nodeName_ == 'N_Bytes_Payload':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_N_Bytes_Payload(obj_)
# end class YAFFlowType

class YAFReverseFlowType(GeneratedsSuper):
    """These elements correspond to the reverse flow captured by in YAF
    record."""

    subclass = None
    superclass = None
    def __init__(self, Reverse_Octet_Total_Count=None, Reverse_Packet_Total_Count=None, Reverse_Payload_Entropy=None, Reverse_Flow_Delta_Milliseconds=None, TCP_Reverse_Flow=None, Reverse_Vlan_ID_MAC_Addr=None, Reverse_Passive_OS_Fingerprinting=None, Reverse_First_Packet=None, Reverse_N_Bytes_Payload=None):
        self.Reverse_Octet_Total_Count = Reverse_Octet_Total_Count
        self.Reverse_Packet_Total_Count = Reverse_Packet_Total_Count
        self.Reverse_Payload_Entropy = Reverse_Payload_Entropy
        self.Reverse_Flow_Delta_Milliseconds = Reverse_Flow_Delta_Milliseconds
        self.TCP_Reverse_Flow = TCP_Reverse_Flow
        self.Reverse_Vlan_ID_MAC_Addr = Reverse_Vlan_ID_MAC_Addr
        self.Reverse_Passive_OS_Fingerprinting = Reverse_Passive_OS_Fingerprinting
        self.Reverse_First_Packet = Reverse_First_Packet
        self.Reverse_N_Bytes_Payload = Reverse_N_Bytes_Payload
    def factory(*args_, **kwargs_):
        if YAFReverseFlowType.subclass:
            return YAFReverseFlowType.subclass(*args_, **kwargs_)
        else:
            return YAFReverseFlowType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Reverse_Octet_Total_Count(self): return self.Reverse_Octet_Total_Count
    def set_Reverse_Octet_Total_Count(self, Reverse_Octet_Total_Count): self.Reverse_Octet_Total_Count = Reverse_Octet_Total_Count
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Reverse_Packet_Total_Count(self): return self.Reverse_Packet_Total_Count
    def set_Reverse_Packet_Total_Count(self, Reverse_Packet_Total_Count): self.Reverse_Packet_Total_Count = Reverse_Packet_Total_Count
    def get_Reverse_Payload_Entropy(self): return self.Reverse_Payload_Entropy
    def set_Reverse_Payload_Entropy(self, Reverse_Payload_Entropy): self.Reverse_Payload_Entropy = Reverse_Payload_Entropy
    def get_Reverse_Flow_Delta_Milliseconds(self): return self.Reverse_Flow_Delta_Milliseconds
    def set_Reverse_Flow_Delta_Milliseconds(self, Reverse_Flow_Delta_Milliseconds): self.Reverse_Flow_Delta_Milliseconds = Reverse_Flow_Delta_Milliseconds
    def get_TCP_Reverse_Flow(self): return self.TCP_Reverse_Flow
    def set_TCP_Reverse_Flow(self, TCP_Reverse_Flow): self.TCP_Reverse_Flow = TCP_Reverse_Flow
    def get_Reverse_Vlan_ID_MAC_Addr(self): return self.Reverse_Vlan_ID_MAC_Addr
    def set_Reverse_Vlan_ID_MAC_Addr(self, Reverse_Vlan_ID_MAC_Addr): self.Reverse_Vlan_ID_MAC_Addr = Reverse_Vlan_ID_MAC_Addr
    def get_Reverse_Passive_OS_Fingerprinting(self): return self.Reverse_Passive_OS_Fingerprinting
    def set_Reverse_Passive_OS_Fingerprinting(self, Reverse_Passive_OS_Fingerprinting): self.Reverse_Passive_OS_Fingerprinting = Reverse_Passive_OS_Fingerprinting
    def get_Reverse_First_Packet(self): return self.Reverse_First_Packet
    def set_Reverse_First_Packet(self, Reverse_First_Packet): self.Reverse_First_Packet = Reverse_First_Packet
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Reverse_N_Bytes_Payload(self): return self.Reverse_N_Bytes_Payload
    def set_Reverse_N_Bytes_Payload(self, Reverse_N_Bytes_Payload): self.Reverse_N_Bytes_Payload = Reverse_N_Bytes_Payload
    def hasContent_(self):
        if (
            self.Reverse_Octet_Total_Count is not None or
            self.Reverse_Packet_Total_Count is not None or
            self.Reverse_Payload_Entropy is not None or
            self.Reverse_Flow_Delta_Milliseconds is not None or
            self.TCP_Reverse_Flow is not None or
            self.Reverse_Vlan_ID_MAC_Addr is not None or
            self.Reverse_Passive_OS_Fingerprinting is not None or
            self.Reverse_First_Packet is not None or
            self.Reverse_N_Bytes_Payload is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFReverseFlowType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='YAFReverseFlowType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='YAFReverseFlowType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFReverseFlowType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Reverse_Octet_Total_Count is not None:
            self.Reverse_Octet_Total_Count.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Octet_Total_Count', pretty_print=pretty_print)
        if self.Reverse_Packet_Total_Count is not None:
            self.Reverse_Packet_Total_Count.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Packet_Total_Count', pretty_print=pretty_print)
        if self.Reverse_Payload_Entropy is not None:
            self.Reverse_Payload_Entropy.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Payload_Entropy', pretty_print=pretty_print)
        if self.Reverse_Flow_Delta_Milliseconds is not None:
            self.Reverse_Flow_Delta_Milliseconds.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Flow_Delta_Milliseconds', pretty_print=pretty_print)
        if self.TCP_Reverse_Flow is not None:
            self.TCP_Reverse_Flow.export(lwrite, level, 'NetFlowObj:', name_='TCP_Reverse_Flow', pretty_print=pretty_print)
        if self.Reverse_Vlan_ID_MAC_Addr is not None:
            self.Reverse_Vlan_ID_MAC_Addr.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Vlan_ID_MAC_Addr', pretty_print=pretty_print)
        if self.Reverse_Passive_OS_Fingerprinting is not None:
            self.Reverse_Passive_OS_Fingerprinting.export(lwrite, level, 'NetFlowObj:', name_='Reverse_Passive_OS_Fingerprinting', pretty_print=pretty_print)
        if self.Reverse_First_Packet is not None:
            self.Reverse_First_Packet.export(lwrite, level, 'NetFlowObj:', name_='Reverse_First_Packet', pretty_print=pretty_print)
        if self.Reverse_N_Bytes_Payload is not None:
            self.Reverse_N_Bytes_Payload.export(lwrite, level, 'NetFlowObj:', name_='Reverse_N_Bytes_Payload', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Reverse_Octet_Total_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_Octet_Total_Count(obj_)
        elif nodeName_ == 'Reverse_Packet_Total_Count':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_Packet_Total_Count(obj_)
        elif nodeName_ == 'Reverse_Payload_Entropy':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_Payload_Entropy(obj_)
        elif nodeName_ == 'Reverse_Flow_Delta_Milliseconds':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_Flow_Delta_Milliseconds(obj_)
        elif nodeName_ == 'TCP_Reverse_Flow':
            obj_ = YAFTCPFlowType.factory()
            obj_.build(child_)
            self.set_TCP_Reverse_Flow(obj_)
        elif nodeName_ == 'Reverse_Vlan_ID_MAC_Addr':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_Reverse_Vlan_ID_MAC_Addr(obj_)
        elif nodeName_ == 'Reverse_Passive_OS_Fingerprinting':
            obj_ = cybox_common.PlatformSpecificationType.factory()
            obj_.build(child_)
            self.set_Reverse_Passive_OS_Fingerprinting(obj_)
        elif nodeName_ == 'Reverse_First_Packet':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_First_Packet(obj_)
        elif nodeName_ == 'Reverse_N_Bytes_Payload':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reverse_N_Bytes_Payload(obj_)
# end class YAFReverseFlowType

class YAFTCPFlowType(GeneratedsSuper):
    """Contains TCP-related information of the network flow."""

    subclass = None
    superclass = None
    def __init__(self, TCP_Sequence_Number=None, Initial_TCP_Flags=None, Union_TCP_Flags=None):
        self.TCP_Sequence_Number = TCP_Sequence_Number
        self.Initial_TCP_Flags = Initial_TCP_Flags
        self.Union_TCP_Flags = Union_TCP_Flags
    def factory(*args_, **kwargs_):
        if YAFTCPFlowType.subclass:
            return YAFTCPFlowType.subclass(*args_, **kwargs_)
        else:
            return YAFTCPFlowType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TCP_Sequence_Number(self): return self.TCP_Sequence_Number
    def set_TCP_Sequence_Number(self, TCP_Sequence_Number): self.TCP_Sequence_Number = TCP_Sequence_Number
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Initial_TCP_Flags(self): return self.Initial_TCP_Flags
    def set_Initial_TCP_Flags(self, Initial_TCP_Flags): self.Initial_TCP_Flags = Initial_TCP_Flags
    def get_Union_TCP_Flags(self): return self.Union_TCP_Flags
    def set_Union_TCP_Flags(self, Union_TCP_Flags): self.Union_TCP_Flags = Union_TCP_Flags
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.TCP_Sequence_Number is not None or
            self.Initial_TCP_Flags is not None or
            self.Union_TCP_Flags is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFTCPFlowType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='YAFTCPFlowType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='YAFTCPFlowType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='YAFTCPFlowType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TCP_Sequence_Number is not None:
            self.TCP_Sequence_Number.export(lwrite, level, 'NetFlowObj:', name_='TCP_Sequence_Number', pretty_print=pretty_print)
        if self.Initial_TCP_Flags is not None:
            self.Initial_TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='Initial_TCP_Flags', pretty_print=pretty_print)
        if self.Union_TCP_Flags is not None:
            self.Union_TCP_Flags.export(lwrite, level, 'NetFlowObj:', name_='Union_TCP_Flags', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'TCP_Sequence_Number':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TCP_Sequence_Number(obj_)
        elif nodeName_ == 'Initial_TCP_Flags':
            obj_ = network_packet_object.TCPFlagsType.factory()
            obj_.build(child_)
            self.set_Initial_TCP_Flags(obj_)
        elif nodeName_ == 'Union_TCP_Flags':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Union_TCP_Flags(obj_)
# end class YAFTCPFlowType

class SiLKSensorClassType(cybox_common.BaseObjectPropertyType):
    """SiLKSensorClassType specifies the sensor class, via a union of the
    SiLKSensorClassTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SiLKSensorClassType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SiLKSensorClassType.subclass:
            return SiLKSensorClassType.subclass(*args_, **kwargs_)
        else:
            return SiLKSensorClassType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SiLKSensorClassType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKSensorClassType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKSensorClassType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKSensorClassType'):
        super(SiLKSensorClassType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKSensorClassType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKSensorClassType', fromsubclass_=False, pretty_print=True):
        super(SiLKSensorClassType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(SiLKSensorClassType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SiLKSensorClassType

class SiLKDirectionType(cybox_common.BaseObjectPropertyType):
    """SiLKType specifies direction of SiLK traffic, via a union of the
    SiLKDirectionTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SiLKDirectionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SiLKDirectionType.subclass:
            return SiLKDirectionType.subclass(*args_, **kwargs_)
        else:
            return SiLKDirectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SiLKDirectionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKDirectionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKDirectionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKDirectionType'):
        super(SiLKDirectionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKDirectionType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKDirectionType', fromsubclass_=False, pretty_print=True):
        super(SiLKDirectionType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(SiLKDirectionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SiLKDirectionType

class SiLKCountryCodeType(cybox_common.BaseObjectPropertyType):
    """SiLKCountryCodeType specifies country codes used by SiLK, via a
    union of the SiLKCountryCodeTypeEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SiLKCountryCodeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SiLKCountryCodeType.subclass:
            return SiLKCountryCodeType.subclass(*args_, **kwargs_)
        else:
            return SiLKCountryCodeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SiLKCountryCodeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKCountryCodeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKCountryCodeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKCountryCodeType'):
        super(SiLKCountryCodeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKCountryCodeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKCountryCodeType', fromsubclass_=False, pretty_print=True):
        super(SiLKCountryCodeType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(SiLKCountryCodeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SiLKCountryCodeType

class SiLKAddressType(cybox_common.BaseObjectPropertyType):
    """SiLKAddressType specifies SiLK address types, via a union of the
    SiLKAddressTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SiLKAddressType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SiLKAddressType.subclass:
            return SiLKAddressType.subclass(*args_, **kwargs_)
        else:
            return SiLKAddressType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SiLKAddressType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKAddressType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKAddressType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKAddressType'):
        super(SiLKAddressType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKAddressType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKAddressType', fromsubclass_=False, pretty_print=True):
        super(SiLKAddressType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(SiLKAddressType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SiLKAddressType

class SiLKFlowAttributesType(cybox_common.BaseObjectPropertyType):
    """SiLKFlowAttributesType specifies SiLK flow attributes, via a union
    of the SiLKFlowAttributesTypeEnum type and the atomic xs:string
    type. Its base type is the CybOX Core cybox_common.BaseObjectPropertyType,
    for permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SiLKFlowAttributesType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SiLKFlowAttributesType.subclass:
            return SiLKFlowAttributesType.subclass(*args_, **kwargs_)
        else:
            return SiLKFlowAttributesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SiLKFlowAttributesType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKFlowAttributesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKFlowAttributesType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='SiLKFlowAttributesType'):
        super(SiLKFlowAttributesType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SiLKFlowAttributesType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='SiLKFlowAttributesType', fromsubclass_=False, pretty_print=True):
        super(SiLKFlowAttributesType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(SiLKFlowAttributesType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SiLKFlowAttributesType

class NetflowV9ScopeFieldType(cybox_common.BaseObjectPropertyType):
    """NetflowV9ScopeFieldType specifies scope field types for Netflow v9,
    via a union of the NetflowV9ScopeFieldTypeEnum type and the
    atomic xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(NetflowV9ScopeFieldType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if NetflowV9ScopeFieldType.subclass:
            return NetflowV9ScopeFieldType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9ScopeFieldType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NetflowV9ScopeFieldType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9ScopeFieldType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9ScopeFieldType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9ScopeFieldType'):
        super(NetflowV9ScopeFieldType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9ScopeFieldType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9ScopeFieldType', fromsubclass_=False, pretty_print=True):
        super(NetflowV9ScopeFieldType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(NetflowV9ScopeFieldType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NetflowV9ScopeFieldType

class NetflowV9FieldType(cybox_common.BaseObjectPropertyType):
    """NetflowV9FieldType specifies possible fields types for Netflow v9,
    via a union of the NetflowV9FieldTypeEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(NetflowV9FieldType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if NetflowV9FieldType.subclass:
            return NetflowV9FieldType.subclass(*args_, **kwargs_)
        else:
            return NetflowV9FieldType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(NetflowV9FieldType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9FieldType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9FieldType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetflowV9FieldType'):
        super(NetflowV9FieldType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetflowV9FieldType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetflowV9FieldType', fromsubclass_=False, pretty_print=True):
        super(NetflowV9FieldType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
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
        super(NetflowV9FieldType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NetflowV9FieldType

class NetworkFlowObjectType(cybox_common.ObjectPropertiesType):
    """Defines the fields necessary to summarize network traffic, expressed
    as flows of multiple packets. Does not include the packet
    payload data (i.e. the actual data that was uploaded/downloaded
    to and from the Dest IP to Source IP as included in packet
    monitoring tools, such as Wireshark)."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Network_Flow_Label=None, Unidirectional_Flow_Record=None, Bidirectional_Flow_Record=None):
        super(NetworkFlowObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Network_Flow_Label = Network_Flow_Label
        self.Unidirectional_Flow_Record = Unidirectional_Flow_Record
        self.Bidirectional_Flow_Record = Bidirectional_Flow_Record
    def factory(*args_, **kwargs_):
        if NetworkFlowObjectType.subclass:
            return NetworkFlowObjectType.subclass(*args_, **kwargs_)
        else:
            return NetworkFlowObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Flow_Label(self): return self.Network_Flow_Label
    def set_Network_Flow_Label(self, Network_Flow_Label): self.Network_Flow_Label = Network_Flow_Label
    def get_Unidirectional_Flow_Record(self): return self.Unidirectional_Flow_Record
    def set_Unidirectional_Flow_Record(self, Unidirectional_Flow_Record): self.Unidirectional_Flow_Record = Unidirectional_Flow_Record
    def get_Bidirectional_Flow_Record(self): return self.Bidirectional_Flow_Record
    def set_Bidirectional_Flow_Record(self, Bidirectional_Flow_Record): self.Bidirectional_Flow_Record = Bidirectional_Flow_Record
    def hasContent_(self):
        if (
            self.Network_Flow_Label is not None or
            self.Unidirectional_Flow_Record is not None or
            self.Bidirectional_Flow_Record is not None or
            super(NetworkFlowObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkFlowObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkFlowObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetFlowObj:', name_='NetworkFlowObjectType'):
        super(NetworkFlowObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkFlowObjectType')
    def exportChildren(self, lwrite, level, namespace_='NetFlowObj:', name_='NetworkFlowObjectType', fromsubclass_=False, pretty_print=True):
        super(NetworkFlowObjectType, self).exportChildren(lwrite, level, 'NetFlowObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Network_Flow_Label is not None:
            self.Network_Flow_Label.export(lwrite, level, 'NetFlowObj:', name_='Network_Flow_Label', pretty_print=pretty_print)
        if self.Unidirectional_Flow_Record is not None:
            self.Unidirectional_Flow_Record.export(lwrite, level, 'NetFlowObj:', name_='Unidirectional_Flow_Record', pretty_print=pretty_print)
        if self.Bidirectional_Flow_Record is not None:
            self.Bidirectional_Flow_Record.export(lwrite, level, 'NetFlowObj:', name_='Bidirectional_Flow_Record', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(NetworkFlowObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Network_Flow_Label':
            obj_ = NetworkFlowLabelType.factory()
            obj_.build(child_)
            self.set_Network_Flow_Label(obj_)
        elif nodeName_ == 'Unidirectional_Flow_Record':
            obj_ = UnidirectionalRecordType.factory()
            obj_.build(child_)
            self.set_Unidirectional_Flow_Record(obj_)
        elif nodeName_ == 'Bidirectional_Flow_Record':
            obj_ = BidirectionalRecordType.factory()
            obj_.build(child_)
            self.set_Bidirectional_Flow_Record(obj_)
        super(NetworkFlowObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkFlowObjectType

GDSClassesMapping = {
    'Reverse_Flow_Delta_Milliseconds': cybox_common.IntegerObjectPropertyType,
    'Record_Count': cybox_common.IntegerObjectPropertyType,
    'Recip_Hardware_Addr': address_object.AddressObjectType,
    'Field_Length': cybox_common.HexBinaryObjectPropertyType,
    'Error_Msg': network_packet_object.ICMPv6ErrorMessageType,
    'Metadata': cybox_common.MetadataType,
    'ICMP_Code': cybox_common.IntegerObjectPropertyType,
    'Padding1': cybox_common.HexBinaryObjectPropertyType,
    'Security_Parameters_Index': cybox_common.HexBinaryObjectPropertyType,
    'Error_Msg_Content': network_packet_object.ICMPv4ErrorMessageContentType,
    'Encapsulating_Security_Payload': network_packet_object.EncapsulatingSecurityPayloadType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Time_Exceeded': network_packet_object.ICMPv6TimeExceededType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Authenication_Data': cybox_common.HexBinaryObjectPropertyType,
    'Packet_Total_Count': cybox_common.IntegerObjectPropertyType,
    'Address_Mask_Request': network_packet_object.ICMPv4AddressMaskRequestType,
    'Flow_End_Milliseconds': cybox_common.IntegerObjectPropertyType,
    'Src_IP_Mask_Bit_Count': cybox_common.StringObjectPropertyType,
    'Protocol': network_packet_object.IANAAssignedIPNumbersType,
    'Seq_Num': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Scope_Enterprise_Number': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Link_Layer_MAC_Addr': address_object.AddressObjectType,
    'Version': cybox_common.HexBinaryObjectPropertyType,
    'Echo_Reply': network_packet_object.ICMPv6EchoReplyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Flow_Set_ID': cybox_common.HexBinaryObjectPropertyType,
    'Preferred_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'TTL': cybox_common.PositiveIntegerObjectPropertyType,
    'Option_Data_Length': cybox_common.IntegerObjectPropertyType,
    'Scope_Field_Length': cybox_common.HexBinaryObjectPropertyType,
    'Sampling_Interval': cybox_common.HexBinaryObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Ethernet_Header': network_packet_object.EthernetHeaderType,
    'Source_ID': cybox_common.HexBinaryObjectPropertyType,
    'Output_Link_MTU': cybox_common.HexBinaryObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Payload_Length': cybox_common.HexBinaryObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Flow_Sequence': cybox_common.IntegerObjectPropertyType,
    'Neighbor_Solicitation': network_packet_object.NeighborSolicitationType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Dest_IPv6_Addr': address_object.AddressObjectType,
    'Unix_Nsecs': cybox_common.IntegerObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Option_Record_Field_Value': cybox_common.StringObjectPropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Prefix_Length': cybox_common.IntegerObjectPropertyType,
    'Source_Quench': network_packet_object.ICMPv4SourceQuenchType,
    'Count': cybox_common.IntegerObjectPropertyType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'First_Eight_Bytes': cybox_common.HexBinaryObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Hardware_Addr_Size': cybox_common.HexBinaryObjectPropertyType,
    'Invoking_Packet': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'SiLK_App_Label': cybox_common.IntegerObjectPropertyType,
    'Traffic_Class': cybox_common.HexBinaryObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'N_Bytes_Payload': cybox_common.HexBinaryObjectPropertyType,
    'Dest_Socket_Address': socket_address_object.SocketAddressObjectType,
    'Reverse_Octet_Total_Count': cybox_common.IntegerObjectPropertyType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Packet_Too_Big': network_packet_object.ICMPv6PacketTooBigType,
    'Socket_Address': socket_address_object.SocketAddressObjectType,
    'Hop_by_Hop_Options': network_packet_object.HopByHopOptionsType,
    'Code': cybox_common.HexBinaryObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Valid_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Destination_Unreachable': network_packet_object.ICMPv6DestinationUnreachableType,
    'UDP': network_packet_object.UDPType,
    'Reserved': cybox_common.HexBinaryObjectPropertyType,
    'Build_Utility': cybox_common.BuildUtilityType,
    'Parameter_Problem': network_packet_object.ICMPv6ParameterProblemType,
    'Routing_Type': cybox_common.HexBinaryObjectPropertyType,
    'Reverse_Vlan_ID_MAC_Addr': address_object.AddressObjectType,
    'Hash': cybox_common.HashType,
    'IP_Protocol': network_packet_object.IANAAssignedIPNumbersType,
    'Sys_Up_Time': cybox_common.IntegerObjectPropertyType,
    'Transmit_Timestamp': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Packet_Change': network_packet_object.IPv6PacketChangeType,
    'Neighbor_Advertisement': network_packet_object.NeighborAdvertisementType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'SubDatum': cybox_common.MetadataType,
    'Address': address_object.AddressObjectType,
    'IP_Version': network_packet_object.IPVersionType,
    'Type_Specific_Data': cybox_common.StringObjectPropertyType,
    'Template_ID': cybox_common.IntegerObjectPropertyType,
    'Src_Autonomous_System': cybox_common.IntegerObjectPropertyType,
    'Padding_Len': cybox_common.HexBinaryObjectPropertyType,
    'Link_Layer': network_packet_object.LinkLayerType,
    'Echo_Request': network_packet_object.ICMPv6EchoRequestType,
    'Dest_MAPNAME': cybox_common.StringObjectPropertyType,
    'Authentication_Header': network_packet_object.AuthenticationHeaderType,
    'Flow_End_Reason': cybox_common.HexBinaryObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Octet': cybox_common.HexBinaryObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Routing': network_packet_object.RoutingType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Flow_Start_Milliseconds': cybox_common.IntegerObjectPropertyType,
    'Protol_Addr_Size': cybox_common.HexBinaryObjectPropertyType,
    'Class': network_packet_object.IPv4ClassType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Egress_Interface_Index': cybox_common.IntegerObjectPropertyType,
    'Urg_Ptr': cybox_common.HexBinaryObjectPropertyType,
    'Scope_Field_Count': cybox_common.PositiveIntegerObjectPropertyType,
    'Options': cybox_common.HexBinaryObjectPropertyType,
    'Enterprise_Number': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'IPv4': network_packet_object.IPv4PacketType,
    'IPv6': network_packet_object.IPv6PacketType,
    'Nexthop_IPv4_Addr': address_object.AddressObjectType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Target_Link_Addr': network_packet_object.NDPLinkAddrType,
    'Physical_Interface': network_packet_object.PhysicalInterfaceType,
    'Padding': cybox_common.HexBinaryObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'ECN': cybox_common.HexBinaryObjectPropertyType,
    'Packet_Count': cybox_common.IntegerObjectPropertyType,
    'Vlan_ID_MAC_Addr': address_object.AddressObjectType,
    'Information_Element_ID': cybox_common.StringObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'ICMPv4_Header': network_packet_object.ICMPv4HeaderType,
    'Data': cybox_common.HexBinaryObjectPropertyType,
    'Octet_Total_Count': cybox_common.IntegerObjectPropertyType,
    'Option_Type': network_packet_object.IPv6OptionType,
    'Next_Hop_MTU': cybox_common.HexBinaryObjectPropertyType,
    'ICMPv6': network_packet_object.ICMPv6PacketType,
    'ICMPv4': network_packet_object.ICMPv4PacketType,
    'References': cybox_common.ToolReferencesType,
    'Redirect': network_packet_object.RedirectType,
    'Initial_TCP_Flags': network_packet_object.TCPFlagsType,
    'Window': cybox_common.HexBinaryObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'TCP_Sequence_Number': cybox_common.IntegerObjectPropertyType,
    'Flow_Set_ID_Template_ID': cybox_common.IntegerObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Receive_Timestamp': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Header_Ext_Len': cybox_common.HexBinaryObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Internet_Layer_Type': network_packet_object.IANAEtherType,
    'Observation_Domain_ID': cybox_common.IntegerObjectPropertyType,
    'Info_Msg_Content': network_packet_object.ICMPv6InfoMessageContentType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'End_Time': cybox_common.IntegerObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Destination_MAC_Addr': address_object.AddressObjectType,
    'Field_Count': cybox_common.IntegerObjectPropertyType,
    'Option_Data': cybox_common.IntegerObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Src_IPv6_Addr': address_object.AddressObjectType,
    'Src_IPv4_Addr': address_object.AddressObjectType,
    'Reverse_First_Packet': cybox_common.HexBinaryObjectPropertyType,
    'Router_Solicitation': network_packet_object.RouterSolicitationType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'IPHeader_And_Data': cybox_common.HexBinaryObjectPropertyType,
    'Reachable_Time': cybox_common.IntegerObjectPropertyType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Segment_Hash': cybox_common.HashValueType,
    'Logical_Protocols': network_packet_object.LogicalProtocolType,
    'Value': cybox_common.StringObjectPropertyType,
    'Session_TCP_Flags': cybox_common.HexBinaryObjectPropertyType,
    'Destination_Options': network_packet_object.DestinationOptionsType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'IP_Type_Of_Service': cybox_common.HexBinaryObjectPropertyType,
    'Hardware_Addr_Type': network_packet_object.IANAHardwareType,
    'Start_Time': cybox_common.IntegerObjectPropertyType,
    'Src_MAPNAME': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Src_Link_Addr': network_packet_object.NDPLinkAddrType,
    'Timestamp_Request': network_packet_object.ICMPv4TimestampRequestType,
    'Tool': cybox_common.ToolInformationType,
    'TCP': network_packet_object.TCPType,
    'Target_IPv6_Addr': address_object.AddressObjectType,
    'Tool_Hashes': cybox_common.HashListType,
    'Field_Value': cybox_common.StringObjectPropertyType,
    'IP_Address': address_object.AddressObjectType,
    'Sequence_Number': cybox_common.HexBinaryObjectPropertyType,
    'TCP_Flags': network_packet_object.TCPFlagsType,
    'Internet_Layer': network_packet_object.InternetLayerType,
    'Router_Lifetime': cybox_common.IntegerObjectPropertyType,
    'Data_Offset': cybox_common.HexBinaryObjectPropertyType,
    'M_Flag': network_packet_object.MFlagType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Option_Information_Element_ID': cybox_common.StringObjectPropertyType,
    'Reverse_Passive_OS_Fingerprinting': cybox_common.PlatformSpecificationType,
    'Option_Field_Length': cybox_common.HexBinaryObjectPropertyType,
    'Output_Link_Speed': cybox_common.HexBinaryObjectPropertyType,
    'Router_Next_Hop_IP': address_object.AddressObjectType,
    'Do_Not_Fragment': network_packet_object.DoNotFragmentType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Flow_Label': cybox_common.HexBinaryObjectPropertyType,
    'ICMPv6_Header': network_packet_object.ICMPv6HeaderType,
    'Set_ID': cybox_common.IntegerObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Union_TCP_Flags': cybox_common.HexBinaryObjectPropertyType,
    'Do_Not_Recogn_Action': network_packet_object.IPv6DoNotRecogActionType,
    'Hashes': cybox_common.HashListType,
    'Engine_Type': cybox_common.StringObjectPropertyType,
    'IPv6_Addr': address_object.AddressObjectType,
    'NDP': network_packet_object.NDPType,
    'Source_MAC_Addr': address_object.AddressObjectType,
    'Padding2': cybox_common.HexBinaryObjectPropertyType,
    'Byte_Run': cybox_common.ByteRunType,
    'Copy_Flag': network_packet_object.IPv4CopyFlagType,
    'Network_Packet': network_packet_object.NetworkPacketObjectType,
    'Engine_ID': cybox_common.IntegerObjectPropertyType,
    'First_Packet_Banner': cybox_common.HexBinaryObjectPropertyType,
    'Outbound_Hop_Count': cybox_common.HexBinaryObjectPropertyType,
    'Fragmentation_Required': network_packet_object.FragmentationRequiredType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'ML_App_Label': cybox_common.HexBinaryObjectPropertyType,
    'Ext_Headers': network_packet_object.IPv6ExtHeaderType,
    'IP_Addr_Prefix': address_object.AddressObjectType,
    'Src_Socket_Address': socket_address_object.SocketAddressObjectType,
    'More_Fragments': network_packet_object.MoreFragmentsType,
    'Next_Header': cybox_common.HexBinaryObjectPropertyType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'MTU': cybox_common.HexBinaryObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Return_Hop_Count': cybox_common.HexBinaryObjectPropertyType,
    'Second_Packet_Banner': cybox_common.HexBinaryObjectPropertyType,
    'Payload_Data': cybox_common.HexBinaryObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Sender_Hardware_Addr': address_object.AddressObjectType,
    'Duration': cybox_common.IntegerObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Option_Length': cybox_common.HexBinaryObjectPropertyType,
    'Reverse_Packet_Total_Count': cybox_common.IntegerObjectPropertyType,
    'UDP_Header': network_packet_object.UDPHeaderType,
    'Errors': cybox_common.ErrorsType,
    'Cur_Hop_Limit': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'TCP_Header': network_packet_object.TCPHeaderType,
    'Router_Advertisement': network_packet_object.RouterAdvertisementType,
    'Dest_IPv4_Addr': address_object.AddressObjectType,
    'Payload_Entropy': cybox_common.IntegerObjectPropertyType,
    'Flow_Application': network_packet_object.IANAPortNumberRegistryType,
    'Flow_Record_Field_Value': cybox_common.StringObjectPropertyType,
    'Checksum': cybox_common.HexBinaryObjectPropertyType,
    'SysUpTime_Start': cybox_common.IntegerObjectPropertyType,
    'DSCP': cybox_common.HexBinaryObjectPropertyType,
    'Option_Scope_Length': cybox_common.HexBinaryObjectPropertyType,
    'Header_Length': cybox_common.IntegerObjectPropertyType,
    'Ethernet': network_packet_object.EthernetInterfaceType,
    'Export_Timestamp': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Address_Mask_Reply': network_packet_object.ICMPv4AddressMaskReplyType,
    'Fragment_Offset': cybox_common.HexBinaryObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Option_Enterprise_Number': cybox_common.StringObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Op_Type': network_packet_object.ARPOpType,
    'Compilers': cybox_common.CompilersType,
    'Originate_Timestamp': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Traceroute': network_packet_object.ICMPv4TracerouteType,
    'String': cybox_common.ExtractedStringType,
    'Type_Or_Length': network_packet_object.TypeLengthType,
    'Pad1': network_packet_object.Pad1Type,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Option_Data_Len': cybox_common.HexBinaryObjectPropertyType,
    'PadN': network_packet_object.PadNType,
    'Option_Byte': cybox_common.HexBinaryObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Proto_Addr_Type': network_packet_object.IANAEtherType,
    'IPv4_Header': network_packet_object.IPv4HeaderType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Total_Length': cybox_common.HexBinaryObjectPropertyType,
    'ICMP_Type': cybox_common.IntegerObjectPropertyType,
    'Pointer': cybox_common.HexBinaryObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'IPv6_Header': network_packet_object.IPv6HeaderType,
    'Scope_Field_Value': cybox_common.StringObjectPropertyType,
    'Fragment_Header': network_packet_object.FragmentHeaderType,
    'Identification': cybox_common.HexBinaryObjectPropertyType,
    'Reverse_N_Bytes_Payload': cybox_common.HexBinaryObjectPropertyType,
    'Transport_Layer': network_packet_object.TransportLayerType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Timestamp_Reply': network_packet_object.ICMPv4TimestampReplyType,
    'Dependencies': cybox_common.DependenciesType,
    'Byte_Length': cybox_common.HexBinaryObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Passive_OS_Fingerprinting': cybox_common.PlatformSpecificationType,
    'ACK_Num': cybox_common.HexBinaryObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Info_Msg': network_packet_object.ICMPv6InfoMessageType,
    'Flags': network_packet_object.IPv4FlagsType,
    'Prefix': network_packet_object.PrefixType,
    'Redirected_Header': network_packet_object.NDPRedirectedHeaderType,
    'Scope_Information_Element_ID': cybox_common.StringObjectPropertyType,
    'Reverse_Payload_Entropy': cybox_common.IntegerObjectPropertyType,
    'Retrans_Timer': cybox_common.IntegerObjectPropertyType,
    'Sender_Protocol_Addr': address_object.AddressObjectType,
    'Segments_Left': cybox_common.IntegerObjectPropertyType,
    'Redirect_Message': network_packet_object.ICMPv4RedirectMessageType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Fragment': cybox_common.HexBinaryObjectPropertyType,
    'Address_Mask': address_object.AddressObjectType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'IP_Header': network_packet_object.IPv4HeaderType,
    'Unix_Secs': cybox_common.IntegerObjectPropertyType,
    'Recip_Protocol_Addr': address_object.AddressObjectType,
    'Option': network_packet_object.IPv4OptionsType,
    'Prefix_Info': network_packet_object.NDPPrefixInfoType,
    'Dest_IP_Mask_Bit_Count': cybox_common.StringObjectPropertyType,
    'Sensor_ID': cybox_common.StringObjectPropertyType,
    'Byte_Count': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Dest_Autonomous_System': cybox_common.IntegerObjectPropertyType,
    'Ingress_Interface_Index': cybox_common.IntegerObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'ARP_RARP': network_packet_object.ARPType,
    'SysUpTime_End': cybox_common.IntegerObjectPropertyType,
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
        rootTag = 'Network_Flow_Object'
        rootClass = NetworkFlowObjectType
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
        rootTag = 'Network_Flow_Object'
        rootClass = NetworkFlowObjectType
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
    from cybox.compat import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Network_Flow_Object'
        rootClass = NetworkFlowObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Flow_Object",
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
    "NetworkFlowObjectType",
    "NetworkLayerInfoType",
    "NetworkFlowLabelType",
    "UnidirectionalRecordType",
    "BidirectionalRecordType",
    "IPFIXMessageType",
    "IPFIXMessageHeaderType",
    "IPFIXSetType",
    "IPFIXTemplateSetType",
    "IPFIXOptionsTemplateSetType",
    "IPFIXDataSetType",
    "IPFIXSetHeaderType",
    "IPFIXTemplateRecordType",
    "IPFIXTemplateRecordHeaderType",
    "IPFIXTemplateRecordFieldSpecifiersType",
    "IPFIXOptionsTemplateRecordType",
    "IPFIXOptionsTemplateRecordHeaderType",
    "IPFIXOptionsTemplateRecordFieldSpecifiersType",
    "IPFIXDataRecordType",
    "NetflowV9ExportPacketType",
    "NetflowV9PacketHeaderType",
    "NetflowV9FlowSetType",
    "NetflowV9TemplateFlowSetType",
    "NetflowV9TemplateRecordType",
    "NetflowV9FieldType",
    "NetflowV9OptionsTemplateFlowSetType",
    "NetflowV9OptionsTemplateRecordType",
    "NetflowV9ScopeFieldType",
    "NetflowV9DataFlowSetType",
    "NetflowV9DataRecordType",
    "FlowDataRecordType",
    "FlowCollectionElementType",
    "OptionsDataRecordType",
    "OptionCollectionElementType",
    "NetflowV5PacketType",
    "NetflowV5FlowHeaderType",
    "NetflowV5FlowRecordType",
    "SiLKRecordType",
    "SiLKFlowAttributesType",
    "SiLKAddressType",
    "SiLKCountryCodeType",
    "SiLKSensorInfoType",
    "SiLKDirectionType",
    "SiLKSensorClassType",
    "YAFRecordType",
    "YAFFlowType",
    "YAFReverseFlowType",
    "YAFTCPFlowType"
    ]
