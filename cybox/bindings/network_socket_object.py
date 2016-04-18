# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import socket_address_object


class SocketOptionsType(GeneratedsSuper):
    """The SocketOptionsType specifies any particular options used by the
    socket. If an options is supported only by specific address
    families or socket types, that's indicated in parentheses."""

    subclass = None
    superclass = None
    def __init__(self, IP_MULTICAST_IF=None, IP_MULTICAST_IF2=None, IP_MULTICAST_LOOP=None, IP_TOS=None, SO_BROADCAST=None, SO_CONDITIONAL_ACCEPT=None, SO_KEEPALIVE=None, SO_DONTROUTE=None, SO_LINGER=None, SO_DONTLINGER=None, SO_OOBINLINE=None, SO_RCVBUF=None, SO_GROUP_PRIORITY=None, SO_REUSEADDR=None, SO_DEBUG=None, SO_RCVTIMEO=None, SO_SNDBUF=None, SO_SNDTIMEO=None, SO_UPDATE_ACCEPT_CONTEXT=None, SO_TIMEOUT=None, TCP_NODELAY=None):
        self.IP_MULTICAST_IF = IP_MULTICAST_IF
        self.IP_MULTICAST_IF2 = IP_MULTICAST_IF2
        self.IP_MULTICAST_LOOP = IP_MULTICAST_LOOP
        self.IP_TOS = IP_TOS
        self.SO_BROADCAST = SO_BROADCAST
        self.SO_CONDITIONAL_ACCEPT = SO_CONDITIONAL_ACCEPT
        self.SO_KEEPALIVE = SO_KEEPALIVE
        self.SO_DONTROUTE = SO_DONTROUTE
        self.SO_LINGER = SO_LINGER
        self.SO_DONTLINGER = SO_DONTLINGER
        self.SO_OOBINLINE = SO_OOBINLINE
        self.SO_RCVBUF = SO_RCVBUF
        self.SO_GROUP_PRIORITY = SO_GROUP_PRIORITY
        self.SO_REUSEADDR = SO_REUSEADDR
        self.SO_DEBUG = SO_DEBUG
        self.SO_RCVTIMEO = SO_RCVTIMEO
        self.SO_SNDBUF = SO_SNDBUF
        self.SO_SNDTIMEO = SO_SNDTIMEO
        self.SO_UPDATE_ACCEPT_CONTEXT = SO_UPDATE_ACCEPT_CONTEXT
        self.SO_TIMEOUT = SO_TIMEOUT
        self.TCP_NODELAY = TCP_NODELAY
    def factory(*args_, **kwargs_):
        if SocketOptionsType.subclass:
            return SocketOptionsType.subclass(*args_, **kwargs_)
        else:
            return SocketOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_IP_MULTICAST_IF(self): return self.IP_MULTICAST_IF
    def set_IP_MULTICAST_IF(self, IP_MULTICAST_IF): self.IP_MULTICAST_IF = IP_MULTICAST_IF
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_IP_MULTICAST_IF2(self): return self.IP_MULTICAST_IF2
    def set_IP_MULTICAST_IF2(self, IP_MULTICAST_IF2): self.IP_MULTICAST_IF2 = IP_MULTICAST_IF2
    def get_IP_MULTICAST_LOOP(self): return self.IP_MULTICAST_LOOP
    def set_IP_MULTICAST_LOOP(self, IP_MULTICAST_LOOP): self.IP_MULTICAST_LOOP = IP_MULTICAST_LOOP
    def get_IP_TOS(self): return self.IP_TOS
    def set_IP_TOS(self, IP_TOS): self.IP_TOS = IP_TOS
    def get_SO_BROADCAST(self): return self.SO_BROADCAST
    def set_SO_BROADCAST(self, SO_BROADCAST): self.SO_BROADCAST = SO_BROADCAST
    def get_SO_CONDITIONAL_ACCEPT(self): return self.SO_CONDITIONAL_ACCEPT
    def set_SO_CONDITIONAL_ACCEPT(self, SO_CONDITIONAL_ACCEPT): self.SO_CONDITIONAL_ACCEPT = SO_CONDITIONAL_ACCEPT
    def get_SO_KEEPALIVE(self): return self.SO_KEEPALIVE
    def set_SO_KEEPALIVE(self, SO_KEEPALIVE): self.SO_KEEPALIVE = SO_KEEPALIVE
    def get_SO_DONTROUTE(self): return self.SO_DONTROUTE
    def set_SO_DONTROUTE(self, SO_DONTROUTE): self.SO_DONTROUTE = SO_DONTROUTE
    def get_SO_LINGER(self): return self.SO_LINGER
    def set_SO_LINGER(self, SO_LINGER): self.SO_LINGER = SO_LINGER
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_SO_DONTLINGER(self): return self.SO_DONTLINGER
    def set_SO_DONTLINGER(self, SO_DONTLINGER): self.SO_DONTLINGER = SO_DONTLINGER
    def get_SO_OOBINLINE(self): return self.SO_OOBINLINE
    def set_SO_OOBINLINE(self, SO_OOBINLINE): self.SO_OOBINLINE = SO_OOBINLINE
    def get_SO_RCVBUF(self): return self.SO_RCVBUF
    def set_SO_RCVBUF(self, SO_RCVBUF): self.SO_RCVBUF = SO_RCVBUF
    def get_SO_GROUP_PRIORITY(self): return self.SO_GROUP_PRIORITY
    def set_SO_GROUP_PRIORITY(self, SO_GROUP_PRIORITY): self.SO_GROUP_PRIORITY = SO_GROUP_PRIORITY
    def get_SO_REUSEADDR(self): return self.SO_REUSEADDR
    def set_SO_REUSEADDR(self, SO_REUSEADDR): self.SO_REUSEADDR = SO_REUSEADDR
    def get_SO_DEBUG(self): return self.SO_DEBUG
    def set_SO_DEBUG(self, SO_DEBUG): self.SO_DEBUG = SO_DEBUG
    def get_SO_RCVTIMEO(self): return self.SO_RCVTIMEO
    def set_SO_RCVTIMEO(self, SO_RCVTIMEO): self.SO_RCVTIMEO = SO_RCVTIMEO
    def get_SO_SNDBUF(self): return self.SO_SNDBUF
    def set_SO_SNDBUF(self, SO_SNDBUF): self.SO_SNDBUF = SO_SNDBUF
    def get_SO_SNDTIMEO(self): return self.SO_SNDTIMEO
    def set_SO_SNDTIMEO(self, SO_SNDTIMEO): self.SO_SNDTIMEO = SO_SNDTIMEO
    def get_SO_UPDATE_ACCEPT_CONTEXT(self): return self.SO_UPDATE_ACCEPT_CONTEXT
    def set_SO_UPDATE_ACCEPT_CONTEXT(self, SO_UPDATE_ACCEPT_CONTEXT): self.SO_UPDATE_ACCEPT_CONTEXT = SO_UPDATE_ACCEPT_CONTEXT
    def get_SO_TIMEOUT(self): return self.SO_TIMEOUT
    def set_SO_TIMEOUT(self, SO_TIMEOUT): self.SO_TIMEOUT = SO_TIMEOUT
    def get_TCP_NODELAY(self): return self.TCP_NODELAY
    def set_TCP_NODELAY(self, TCP_NODELAY): self.TCP_NODELAY = TCP_NODELAY
    def hasContent_(self):
        if (
            self.IP_MULTICAST_IF is not None or
            self.IP_MULTICAST_IF2 is not None or
            self.IP_MULTICAST_LOOP is not None or
            self.IP_TOS is not None or
            self.SO_BROADCAST is not None or
            self.SO_CONDITIONAL_ACCEPT is not None or
            self.SO_KEEPALIVE is not None or
            self.SO_DONTROUTE is not None or
            self.SO_LINGER is not None or
            self.SO_DONTLINGER is not None or
            self.SO_OOBINLINE is not None or
            self.SO_RCVBUF is not None or
            self.SO_GROUP_PRIORITY is not None or
            self.SO_REUSEADDR is not None or
            self.SO_DEBUG is not None or
            self.SO_RCVTIMEO is not None or
            self.SO_SNDBUF is not None or
            self.SO_SNDTIMEO is not None or
            self.SO_UPDATE_ACCEPT_CONTEXT is not None or
            self.SO_TIMEOUT is not None or
            self.TCP_NODELAY is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='SocketOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SocketOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='SocketOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='SocketOptionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.IP_MULTICAST_IF is not None:
            self.IP_MULTICAST_IF.export(lwrite, level, 'NetworkSocketObj:', name_='IP_MULTICAST_IF', pretty_print=pretty_print)
        if self.IP_MULTICAST_IF2 is not None:
            self.IP_MULTICAST_IF2.export(lwrite, level, 'NetworkSocketObj:', name_='IP_MULTICAST_IF2', pretty_print=pretty_print)
        if self.IP_MULTICAST_LOOP is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sIP_MULTICAST_LOOP>%s</%sIP_MULTICAST_LOOP>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.IP_MULTICAST_LOOP, input_name='IP_MULTICAST_LOOP'), 'NetworkSocketObj:', eol_))
        if self.IP_TOS is not None:
            self.IP_TOS.export(lwrite, level, 'NetworkSocketObj:', name_='IP_TOS', pretty_print=pretty_print)
        if self.SO_BROADCAST is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_BROADCAST>%s</%sSO_BROADCAST>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_BROADCAST, input_name='SO_BROADCAST'), 'NetworkSocketObj:', eol_))
        if self.SO_CONDITIONAL_ACCEPT is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_CONDITIONAL_ACCEPT>%s</%sSO_CONDITIONAL_ACCEPT>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_CONDITIONAL_ACCEPT, input_name='SO_CONDITIONAL_ACCEPT'), 'NetworkSocketObj:', eol_))
        if self.SO_KEEPALIVE is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_KEEPALIVE>%s</%sSO_KEEPALIVE>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_KEEPALIVE, input_name='SO_KEEPALIVE'), 'NetworkSocketObj:', eol_))
        if self.SO_DONTROUTE is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_DONTROUTE>%s</%sSO_DONTROUTE>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_DONTROUTE, input_name='SO_DONTROUTE'), 'NetworkSocketObj:', eol_))
        if self.SO_LINGER is not None:
            self.SO_LINGER.export(lwrite, level, 'NetworkSocketObj:', name_='SO_LINGER', pretty_print=pretty_print)
        if self.SO_DONTLINGER is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_DONTLINGER>%s</%sSO_DONTLINGER>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_DONTLINGER, input_name='SO_DONTLINGER'), 'NetworkSocketObj:', eol_))
        if self.SO_OOBINLINE is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_OOBINLINE>%s</%sSO_OOBINLINE>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_OOBINLINE, input_name='SO_OOBINLINE'), 'NetworkSocketObj:', eol_))
        if self.SO_RCVBUF is not None:
            self.SO_RCVBUF.export(lwrite, level, 'NetworkSocketObj:', name_='SO_RCVBUF', pretty_print=pretty_print)
        if self.SO_GROUP_PRIORITY is not None:
            self.SO_GROUP_PRIORITY.export(lwrite, level, 'NetworkSocketObj:', name_='SO_GROUP_PRIORITY', pretty_print=pretty_print)
        if self.SO_REUSEADDR is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_REUSEADDR>%s</%sSO_REUSEADDR>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_REUSEADDR, input_name='SO_REUSEADDR'), 'NetworkSocketObj:', eol_))
        if self.SO_DEBUG is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSO_DEBUG>%s</%sSO_DEBUG>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.SO_DEBUG, input_name='SO_DEBUG'), 'NetworkSocketObj:', eol_))
        if self.SO_RCVTIMEO is not None:
            self.SO_RCVTIMEO.export(lwrite, level, 'NetworkSocketObj:', name_='SO_RCVTIMEO', pretty_print=pretty_print)
        if self.SO_SNDBUF is not None:
            self.SO_SNDBUF.export(lwrite, level, 'NetworkSocketObj:', name_='SO_SNDBUF', pretty_print=pretty_print)
        if self.SO_SNDTIMEO is not None:
            self.SO_SNDTIMEO.export(lwrite, level, 'NetworkSocketObj:', name_='SO_SNDTIMEO', pretty_print=pretty_print)
        if self.SO_UPDATE_ACCEPT_CONTEXT is not None:
            self.SO_UPDATE_ACCEPT_CONTEXT.export(lwrite, level, 'NetworkSocketObj:', name_='SO_UPDATE_ACCEPT_CONTEXT', pretty_print=pretty_print)
        if self.SO_TIMEOUT is not None:
            self.SO_TIMEOUT.export(lwrite, level, 'NetworkSocketObj:', name_='SO_TIMEOUT', pretty_print=pretty_print)
        if self.TCP_NODELAY is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sTCP_NODELAY>%s</%sTCP_NODELAY>%s' % ('NetworkSocketObj:', self.gds_format_boolean(self.TCP_NODELAY, input_name='TCP_NODELAY'), 'NetworkSocketObj:', eol_))
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
        if nodeName_ == 'IP_MULTICAST_IF':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IP_MULTICAST_IF(obj_)
        elif nodeName_ == 'IP_MULTICAST_IF2':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IP_MULTICAST_IF2(obj_)
        elif nodeName_ == 'IP_MULTICAST_LOOP':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'IP_MULTICAST_LOOP')
            self.IP_MULTICAST_LOOP = ival_
        elif nodeName_ == 'IP_TOS':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IP_TOS(obj_)
        elif nodeName_ == 'SO_BROADCAST':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_BROADCAST')
            self.SO_BROADCAST = ival_
        elif nodeName_ == 'SO_CONDITIONAL_ACCEPT':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_CONDITIONAL_ACCEPT')
            self.SO_CONDITIONAL_ACCEPT = ival_
        elif nodeName_ == 'SO_KEEPALIVE':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_KEEPALIVE')
            self.SO_KEEPALIVE = ival_
        elif nodeName_ == 'SO_DONTROUTE':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_DONTROUTE')
            self.SO_DONTROUTE = ival_
        elif nodeName_ == 'SO_LINGER':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_LINGER(obj_)
        elif nodeName_ == 'SO_DONTLINGER':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_DONTLINGER')
            self.SO_DONTLINGER = ival_
        elif nodeName_ == 'SO_OOBINLINE':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_OOBINLINE')
            self.SO_OOBINLINE = ival_
        elif nodeName_ == 'SO_RCVBUF':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_RCVBUF(obj_)
        elif nodeName_ == 'SO_GROUP_PRIORITY':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_GROUP_PRIORITY(obj_)
        elif nodeName_ == 'SO_REUSEADDR':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_REUSEADDR')
            self.SO_REUSEADDR = ival_
        elif nodeName_ == 'SO_DEBUG':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'SO_DEBUG')
            self.SO_DEBUG = ival_
        elif nodeName_ == 'SO_RCVTIMEO':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_RCVTIMEO(obj_)
        elif nodeName_ == 'SO_SNDBUF':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_SNDBUF(obj_)
        elif nodeName_ == 'SO_SNDTIMEO':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_SNDTIMEO(obj_)
        elif nodeName_ == 'SO_UPDATE_ACCEPT_CONTEXT':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_UPDATE_ACCEPT_CONTEXT(obj_)
        elif nodeName_ == 'SO_TIMEOUT':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_SO_TIMEOUT(obj_)
        elif nodeName_ == 'TCP_NODELAY':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'TCP_NODELAY')
            self.TCP_NODELAY = ival_
# end class SocketOptionsType

class ProtocolType(cybox_common.BaseObjectPropertyType):
    """ProtocolType specifies protocol types, via a union of the
    ProtocolTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(ProtocolType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ProtocolType.subclass:
            return ProtocolType.subclass(*args_, **kwargs_)
        else:
            return ProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(ProtocolType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='ProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProtocolType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='ProtocolType'):
        super(ProtocolType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ProtocolType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='ProtocolType', fromsubclass_=False, pretty_print=True):
        super(ProtocolType, self).exportChildren(lwrite, level, 'NetworkSocketObj:', name_, True, pretty_print=pretty_print)
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
        super(ProtocolType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ProtocolType

class SocketType(cybox_common.BaseObjectPropertyType):
    """SocketType specifies socket types, via a union of the SocketTypeEnum
    type and the atomic xs:string type. Its base type is the CybOX
    Core cybox_common.BaseObjectPropertyType, for permitting complex (i.e.
    regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(SocketType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if SocketType.subclass:
            return SocketType.subclass(*args_, **kwargs_)
        else:
            return SocketType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(SocketType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='SocketType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SocketType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='SocketType'):
        super(SocketType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SocketType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='SocketType', fromsubclass_=False, pretty_print=True):
        super(SocketType, self).exportChildren(lwrite, level, 'NetworkSocketObj:', name_, True, pretty_print=pretty_print)
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
        super(SocketType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class SocketType

class DomainFamilyType(cybox_common.BaseObjectPropertyType):
    """DomainFamilyType specifies domain family types, via a union of the
    DomainTypeEnum type and the atomic xs:string type. Its base type
    is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(DomainFamilyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DomainFamilyType.subclass:
            return DomainFamilyType.subclass(*args_, **kwargs_)
        else:
            return DomainFamilyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DomainFamilyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='DomainFamilyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DomainFamilyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='DomainFamilyType'):
        super(DomainFamilyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DomainFamilyType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='DomainFamilyType', fromsubclass_=False, pretty_print=True):
        super(DomainFamilyType, self).exportChildren(lwrite, level, 'NetworkSocketObj:', name_, True, pretty_print=pretty_print)
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
        super(DomainFamilyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DomainFamilyType

class AddressFamilyType(cybox_common.BaseObjectPropertyType):
    """AddressFamilyType specifies address family types, via a union of the
    AddressFamilyTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(AddressFamilyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if AddressFamilyType.subclass:
            return AddressFamilyType.subclass(*args_, **kwargs_)
        else:
            return AddressFamilyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(AddressFamilyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='AddressFamilyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AddressFamilyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='AddressFamilyType'):
        super(AddressFamilyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AddressFamilyType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='AddressFamilyType', fromsubclass_=False, pretty_print=True):
        super(AddressFamilyType, self).exportChildren(lwrite, level, 'NetworkSocketObj:', name_, True, pretty_print=pretty_print)
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
        super(AddressFamilyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AddressFamilyType

class NetworkSocketObjectType(cybox_common.ObjectPropertiesType):
    """The NetworkSocketObjectType is intended to characterize network
    sockets.The is_blocking field specifies whether or not the
    socket is in blocking mode. The is_listening field specifies
    whether or not the socket is in listening mode."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_blocking=None, is_listening=None, Address_Family=None, Domain=None, Local_Address=None, Options=None, Protocol=None, Remote_Address=None, Type=None, Socket_Descriptor=None):
        super(NetworkSocketObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_blocking = _cast(bool, is_blocking)
        self.is_listening = _cast(bool, is_listening)
        self.Address_Family = Address_Family
        self.Domain = Domain
        self.Local_Address = Local_Address
        self.Options = Options
        self.Protocol = Protocol
        self.Remote_Address = Remote_Address
        self.Type = Type
        self.Socket_Descriptor = Socket_Descriptor
    def factory(*args_, **kwargs_):
        if NetworkSocketObjectType.subclass:
            return NetworkSocketObjectType.subclass(*args_, **kwargs_)
        else:
            return NetworkSocketObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Address_Family(self): return self.Address_Family
    def set_Address_Family(self, Address_Family): self.Address_Family = Address_Family
    def validate_AddressFamilyType(self, value):
        # Validate type AddressFamilyType, a restriction on None.
        pass
    def get_Domain(self): return self.Domain
    def set_Domain(self, Domain): self.Domain = Domain
    def validate_DomainFamilyType(self, value):
        # Validate type DomainFamilyType, a restriction on None.
        pass
    def get_Local_Address(self): return self.Local_Address
    def set_Local_Address(self, Local_Address): self.Local_Address = Local_Address
    def get_Options(self): return self.Options
    def set_Options(self, Options): self.Options = Options
    def get_Protocol(self): return self.Protocol
    def set_Protocol(self, Protocol): self.Protocol = Protocol
    def validate_ProtocolType(self, value):
        # Validate type ProtocolType, a restriction on None.
        pass
    def get_Remote_Address(self): return self.Remote_Address
    def set_Remote_Address(self, Remote_Address): self.Remote_Address = Remote_Address
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Socket_Descriptor(self): return self.Socket_Descriptor
    def set_Socket_Descriptor(self, Socket_Descriptor): self.Socket_Descriptor = Socket_Descriptor
    def validate_SocketType(self, value):
        # Validate type SocketType, a restriction on None.
        pass
    def get_is_blocking(self): return self.is_blocking
    def set_is_blocking(self, is_blocking): self.is_blocking = is_blocking
    def get_is_listening(self): return self.is_listening
    def set_is_listening(self, is_listening): self.is_listening = is_listening
    def hasContent_(self):
        if (
            self.Address_Family is not None or
            self.Domain is not None or
            self.Local_Address is not None or
            self.Options is not None or
            self.Protocol is not None or
            self.Remote_Address is not None or
            self.Type is not None or
            self.Socket_Descriptor is not None or
            super(NetworkSocketObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkSocketObj:', name_='NetworkSocketObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkSocketObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkSocketObj:', name_='NetworkSocketObjectType'):
        super(NetworkSocketObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkSocketObjectType')
        if self.is_blocking is not None:

            lwrite(' is_blocking="%s"' % self.gds_format_boolean(self.is_blocking, input_name='is_blocking'))
        if self.is_listening is not None:

            lwrite(' is_listening="%s"' % self.gds_format_boolean(self.is_listening, input_name='is_listening'))
    def exportChildren(self, lwrite, level, namespace_='NetworkSocketObj:', name_='NetworkSocketObjectType', fromsubclass_=False, pretty_print=True):
        super(NetworkSocketObjectType, self).exportChildren(lwrite, level, 'NetworkSocketObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address_Family is not None:
            self.Address_Family.export(lwrite, level, 'NetworkSocketObj:', name_='Address_Family', pretty_print=pretty_print)
        if self.Domain is not None:
            self.Domain.export(lwrite, level, 'NetworkSocketObj:', name_='Domain', pretty_print=pretty_print)
        if self.Local_Address is not None:
            self.Local_Address.export(lwrite, level, 'NetworkSocketObj:', name_='Local_Address', pretty_print=pretty_print)
        if self.Options is not None:
            self.Options.export(lwrite, level, 'NetworkSocketObj:', name_='Options', pretty_print=pretty_print)
        if self.Protocol is not None:
            self.Protocol.export(lwrite, level, 'NetworkSocketObj:', name_='Protocol', pretty_print=pretty_print)
        if self.Remote_Address is not None:
            self.Remote_Address.export(lwrite, level, 'NetworkSocketObj:', name_='Remote_Address', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'NetworkSocketObj:', name_='Type', pretty_print=pretty_print)
        if self.Socket_Descriptor is not None:
            self.Socket_Descriptor.export(lwrite, level, 'NetworkSocketObj:', name_='Socket_Descriptor', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_blocking', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_blocking = True
            elif value in ('false', '0'):
                self.is_blocking = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_listening', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_listening = True
            elif value in ('false', '0'):
                self.is_listening = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(NetworkSocketObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Address_Family':
            obj_ = AddressFamilyType.factory()
            obj_.build(child_)
            self.set_Address_Family(obj_)
        elif nodeName_ == 'Domain':
            obj_ = DomainFamilyType.factory()
            obj_.build(child_)
            self.set_Domain(obj_)
        elif nodeName_ == 'Local_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Local_Address(obj_)
        elif nodeName_ == 'Options':
            obj_ = SocketOptionsType.factory()
            obj_.build(child_)
            self.set_Options(obj_)
        elif nodeName_ == 'Protocol':
            obj_ = ProtocolType.factory()
            obj_.build(child_)
            self.set_Protocol(obj_)
        elif nodeName_ == 'Remote_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Remote_Address(obj_)
        elif nodeName_ == 'Type':
            obj_ = SocketType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Socket_Descriptor':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Socket_Descriptor(obj_)
        super(NetworkSocketObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkSocketObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'SO_GROUP_PRIORITY': cybox_common.UnsignedIntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'SO_RCVTIMEO': cybox_common.UnsignedIntegerObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'SO_RCVBUF': cybox_common.UnsignedIntegerObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'SO_UPDATE_ACCEPT_CONTEXT': cybox_common.UnsignedIntegerObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Remote_Address': socket_address_object.SocketAddressObjectType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'SO_LINGER': cybox_common.UnsignedIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'SO_TIMEOUT': cybox_common.UnsignedIntegerObjectPropertyType,
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
    'SO_SNDBUF': cybox_common.UnsignedIntegerObjectPropertyType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'IP_TOS': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
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
    'SO_SNDTIMEO': cybox_common.UnsignedIntegerObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'IP_MULTICAST_IF2': cybox_common.StringObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Time': cybox_common.TimeType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Socket_Address': socket_address_object.SocketAddressObjectType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'IP_MULTICAST_IF': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Local_Address': socket_address_object.SocketAddressObjectType,
    'Tools': cybox_common.ToolsInformationType,
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
        rootTag = 'Network_Socket'
        rootClass = NetworkSocketObjectType
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
        rootTag = 'Network_Socket'
        rootClass = NetworkSocketObjectType
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
        rootTag = 'Network_Socket'
        rootClass = NetworkSocketObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Socket",
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
    "NetworkSocketObjectType",
    "SocketOptionsType",
    "AddressFamilyType",
    "DomainFamilyType",
    "SocketType",
    "ProtocolType"
    ]
