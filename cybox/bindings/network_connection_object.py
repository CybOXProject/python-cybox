# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import dns_query_object
from . import http_session_object
from . import socket_address_object


class Layer7ConnectionsType(GeneratedsSuper):
    """The Layer7ConnectionsType specifies the different types of
    application (layer 7 in the OSI model) connections that may be
    initiated as part of the network connection."""

    subclass = None
    superclass = None
    def __init__(self, HTTP_Session=None, DNS_Query=None):
        self.HTTP_Session = HTTP_Session
        if DNS_Query is None:
            self.DNS_Query = []
        else:
            self.DNS_Query = DNS_Query
    def factory(*args_, **kwargs_):
        if Layer7ConnectionsType.subclass:
            return Layer7ConnectionsType.subclass(*args_, **kwargs_)
        else:
            return Layer7ConnectionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Session(self): return self.HTTP_Session
    def set_HTTP_Session(self, HTTP_Session): self.HTTP_Session = HTTP_Session
    def get_DNS_Query(self): return self.DNS_Query
    def set_DNS_Query(self, DNS_Query): self.DNS_Query = DNS_Query
    def add_DNS_Query(self, value): self.DNS_Query.append(value)
    def insert_DNS_Query(self, index, value): self.DNS_Query[index] = value
    def hasContent_(self):
        if (
            self.HTTP_Session is not None or
            self.DNS_Query
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer7ConnectionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer7ConnectionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkConnectionObj:', name_='Layer7ConnectionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer7ConnectionsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HTTP_Session is not None:
            self.HTTP_Session.export(lwrite, level, 'NetworkConnectionObj:', name_='HTTP_Session', pretty_print=pretty_print)
        for DNS_Query_ in self.DNS_Query:
            DNS_Query_.export(lwrite, level, 'NetworkConnectionObj:', name_='DNS_Query', pretty_print=pretty_print)
    def build(self, node):
        self.__sourecenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'HTTP_Session':
            obj_ = http_session_object.HTTPSessionObjectType.factory()
            obj_.build(child_)
            self.set_HTTP_Session(obj_)
        elif nodeName_ == 'DNS_Query':
            obj_ = dns_query_object.DNSQueryObjectType.factory()
            obj_.build(child_)
            self.DNS_Query.append(obj_)
# end class Layer7ConnectionsType

class Layer7ProtocolType(cybox_common.BaseObjectPropertyType):
    """Layer7ProtocolType specifies Layer 7 protocol types, via a union of
    the Layer7ProtocolEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(Layer7ProtocolType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Layer7ProtocolType.subclass:
            return Layer7ProtocolType.subclass(*args_, **kwargs_)
        else:
            return Layer7ProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(Layer7ProtocolType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer7ProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer7ProtocolType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkConnectionObj:', name_='Layer7ProtocolType'):
        super(Layer7ProtocolType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer7ProtocolType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer7ProtocolType', fromsubclass_=False, pretty_print=True):
        super(Layer7ProtocolType, self).exportChildren(lwrite, level, 'NetworkConnectionObj:', name_, True, pretty_print=pretty_print)
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
        super(Layer7ProtocolType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class Layer7ProtocolType

class Layer3ProtocolType(cybox_common.BaseObjectPropertyType):
    """Layer3ProtocolType specifies Layer 3 protocol types, via a union of
    the Layer3ProtocolEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(Layer3ProtocolType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if Layer3ProtocolType.subclass:
            return Layer3ProtocolType.subclass(*args_, **kwargs_)
        else:
            return Layer3ProtocolType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(Layer3ProtocolType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer3ProtocolType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer3ProtocolType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkConnectionObj:', name_='Layer3ProtocolType'):
        super(Layer3ProtocolType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Layer3ProtocolType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='Layer3ProtocolType', fromsubclass_=False, pretty_print=True):
        super(Layer3ProtocolType, self).exportChildren(lwrite, level, 'NetworkConnectionObj:', name_, True, pretty_print=pretty_print)
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
        super(Layer3ProtocolType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class Layer3ProtocolType

class NetworkConnectionObjectType(cybox_common.ObjectPropertiesType):
    """The NetworkConnectionObjectType is intended as a way of
    characterizing local or remote (i.e. Internet) network
    connections.The tls_used field specifies whether or not
    Transport Layer Security (TLS) is used in the network
    connection."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, tls_used=None, Creation_Time=None, Layer3_Protocol=None, Layer4_Protocol=None, Layer7_Protocol=None, Source_Socket_Address=None, Source_TCP_State=None, Destination_Socket_Address=None, Destination_TCP_State=None, Layer7_Connections=None):
        super(NetworkConnectionObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.tls_used = _cast(bool, tls_used)
        self.Creation_Time = Creation_Time
        self.Layer3_Protocol = Layer3_Protocol
        self.Layer4_Protocol = Layer4_Protocol
        self.Layer7_Protocol = Layer7_Protocol
        self.Source_Socket_Address = Source_Socket_Address
        self.Source_TCP_State = Source_TCP_State
        self.Destination_Socket_Address = Destination_Socket_Address
        self.Destination_TCP_State = Destination_TCP_State
        self.Layer7_Connections = Layer7_Connections
    def factory(*args_, **kwargs_):
        if NetworkConnectionObjectType.subclass:
            return NetworkConnectionObjectType.subclass(*args_, **kwargs_)
        else:
            return NetworkConnectionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Creation_Time(self): return self.Creation_Time
    def set_Creation_Time(self, Creation_Time): self.Creation_Time = Creation_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Layer3_Protocol(self): return self.Layer3_Protocol
    def set_Layer3_Protocol(self, Layer3_Protocol): self.Layer3_Protocol = Layer3_Protocol
    def validate_Layer3ProtocolType(self, value):
        # Validate type Layer3ProtocolType, a restriction on None.
        pass
    def get_Layer4_Protocol(self): return self.Layer4_Protocol
    def set_Layer4_Protocol(self, Layer4_Protocol): self.Layer4_Protocol = Layer4_Protocol
    def validate_Layer4ProtocolType(self, value):
        # Validate type Layer4ProtocolType, a restriction on None.
        pass
    def get_Layer7_Protocol(self): return self.Layer7_Protocol
    def set_Layer7_Protocol(self, Layer7_Protocol): self.Layer7_Protocol = Layer7_Protocol
    def validate_Layer7ProtocolType(self, value):
        # Validate type Layer7ProtocolType, a restriction on None.
        pass
    def get_Source_Socket_Address(self): return self.Source_Socket_Address
    def set_Source_Socket_Address(self, Source_Socket_Address): self.Source_Socket_Address = Source_Socket_Address
    def get_Source_TCP_State(self): return self.Source_TCP_State
    def set_Source_TCP_State(self, Source_TCP_State): self.Source_TCP_State = Source_TCP_State
    def validate_TCPStateEnum(self, value):
        # Validate type TCPStateEnum, a restriction on xs:string.
        pass
    def get_Destination_Socket_Address(self): return self.Destination_Socket_Address
    def set_Destination_Socket_Address(self, Destination_Socket_Address): self.Destination_Socket_Address = Destination_Socket_Address
    def get_Destination_TCP_State(self): return self.Destination_TCP_State
    def set_Destination_TCP_State(self, Destination_TCP_State): self.Destination_TCP_State = Destination_TCP_State
    def get_Layer7_Connections(self): return self.Layer7_Connections
    def set_Layer7_Connections(self, Layer7_Connections): self.Layer7_Connections = Layer7_Connections
    def get_tls_used(self): return self.tls_used
    def set_tls_used(self, tls_used): self.tls_used = tls_used
    def hasContent_(self):
        if (
            self.Creation_Time is not None or
            self.Layer3_Protocol is not None or
            self.Layer4_Protocol is not None or
            self.Layer7_Protocol is not None or
            self.Source_Socket_Address is not None or
            self.Source_TCP_State is not None or
            self.Destination_Socket_Address is not None or
            self.Destination_TCP_State is not None or
            self.Layer7_Connections is not None or
            super(NetworkConnectionObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='NetworkConnectionObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkConnectionObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='NetworkConnectionObj:', name_='NetworkConnectionObjectType'):
        super(NetworkConnectionObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkConnectionObjectType')
        if self.tls_used is not None:

            lwrite(' tls_used="%s"' % self.gds_format_boolean(self.tls_used, input_name='tls_used'))
    def exportChildren(self, lwrite, level, namespace_='NetworkConnectionObj:', name_='NetworkConnectionObjectType', fromsubclass_=False, pretty_print=True):
        super(NetworkConnectionObjectType, self).exportChildren(lwrite, level, 'NetworkConnectionObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Creation_Time is not None:
            self.Creation_Time.export(lwrite, level, 'NetworkConnectionObj:', name_='Creation_Time', pretty_print=pretty_print)
        if self.Layer3_Protocol is not None:
            self.Layer3_Protocol.export(lwrite, level, 'NetworkConnectionObj:', name_='Layer3_Protocol', pretty_print=pretty_print)
        if self.Layer4_Protocol is not None:
            self.Layer4_Protocol.export(lwrite, level, 'NetworkConnectionObj:', name_='Layer4_Protocol', pretty_print=pretty_print)
        if self.Layer7_Protocol is not None:
            self.Layer7_Protocol.export(lwrite, level, 'NetworkConnectionObj:', name_='Layer7_Protocol', pretty_print=pretty_print)
        if self.Source_Socket_Address is not None:
            self.Source_Socket_Address.export(lwrite, level, 'NetworkConnectionObj:', name_='Source_Socket_Address', pretty_print=pretty_print)
        if self.Source_TCP_State is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sSource_TCP_State>%s</%sSource_TCP_State>%s' % ('NetworkConnectionObj:', self.gds_format_string(quote_xml(self.Source_TCP_State), input_name='Source_TCP_State'), 'NetworkConnectionObj:', eol_))
        if self.Destination_Socket_Address is not None:
            self.Destination_Socket_Address.export(lwrite, level, 'NetworkConnectionObj:', name_='Destination_Socket_Address', pretty_print=pretty_print)
        if self.Destination_TCP_State is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sDestination_TCP_State>%s</%sDestination_TCP_State>%s' % ('NetworkConnectionObj:', self.gds_format_string(quote_xml(self.Destination_TCP_State), input_name='Destination_TCP_State'), 'NetworkConnectionObj:', eol_))
        if self.Layer7_Connections is not None:
            self.Layer7_Connections.export(lwrite, level, 'NetworkConnectionObj:', name_='Layer7_Connections', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('tls_used', node)
        if value is not None:

            if value in ('true', '1'):
                self.tls_used = True
            elif value in ('false', '0'):
                self.tls_used = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(NetworkConnectionObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Creation_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Time(obj_)
        elif nodeName_ == 'Layer3_Protocol':
            obj_ = Layer3ProtocolType.factory()
            obj_.build(child_)
            self.set_Layer3_Protocol(obj_)
        elif nodeName_ == 'Layer4_Protocol':
            obj_ = cybox_common.Layer4ProtocolType.factory()
            obj_.build(child_)
            self.set_Layer4_Protocol(obj_)
        elif nodeName_ == 'Layer7_Protocol':
            obj_ = Layer7ProtocolType.factory()
            obj_.build(child_)
            self.set_Layer7_Protocol(obj_)
        elif nodeName_ == 'Source_Socket_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Source_Socket_Address(obj_)
        elif nodeName_ == 'Source_TCP_State':
            Source_TCP_State_ = child_.text
            Source_TCP_State_ = self.gds_validate_string(Source_TCP_State_, node, 'Source_TCP_State')
            self.Source_TCP_State = Source_TCP_State_
        elif nodeName_ == 'Destination_Socket_Address':
            obj_ = socket_address_object.SocketAddressObjectType.factory()
            obj_.build(child_)
            self.set_Destination_Socket_Address(obj_)
        elif nodeName_ == 'Destination_TCP_State':
            Destination_TCP_State_ = child_.text
            Destination_TCP_State_ = self.gds_validate_string(Destination_TCP_State_, node, 'Destination_TCP_State')
            self.Destination_TCP_State = Destination_TCP_State_
        elif nodeName_ == 'Layer7_Connections':
            obj_ = Layer7ConnectionsType.factory()
            obj_.build(child_)
            self.set_Layer7_Connections(obj_)
        super(NetworkConnectionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class NetworkConnectionObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Parsed_Header': http_session_object.HTTPResponseHeaderFieldsType,
    'Answer_Resource_Records': dns_query_object.DNSResourceRecordsType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'Host': http_session_object.HostFieldType,
    'Authority_Resource_Records': dns_query_object.DNSResourceRecordsType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.PositiveIntegerObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'HTTP_Server_Response': http_session_object.HTTPServerResponseType,
    'TE': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Warning': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Question': dns_query_object.DNSQuestionType,
    'System': cybox_common.ObjectPropertiesType,
    'HTTP_Request_Line': http_session_object.HTTPRequestLineType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'DNS_Query': dns_query_object.DNSQueryObjectType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Additional_Records': dns_query_object.DNSResourceRecordsType,
    'Link': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Server': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Via': cybox_common.StringObjectPropertyType,
    'X_Requested_For': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Expect': cybox_common.StringObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Destination_Socket_Address': socket_address_object.SocketAddressObjectType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'HTTP_Client_Request': http_session_object.HTTPClientRequestType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'HTTP_Session': http_session_object.HTTPSessionObjectType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Connection': cybox_common.StringObjectPropertyType,
    'X_Requested_With': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'P3P': cybox_common.StringObjectPropertyType,
    'If_Unmodified_Since': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'HTTP_Response_Header': http_session_object.HTTPResponseHeaderType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'Source_Socket_Address': socket_address_object.SocketAddressObjectType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'QType': dns_query_object.DNSRecordType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Socket_Address': socket_address_object.SocketAddressObjectType,
    'HTTP_Method': http_session_object.HTTPMethodType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'HTTP_Status_Line': http_session_object.HTTPStatusLineType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'HTTP_Message_Body': http_session_object.HTTPMessageType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'HTTP_Request_Response': http_session_object.HTTPRequestResponseType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'HTTP_Request_Header': http_session_object.HTTPRequestHeaderType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'ETag': cybox_common.StringObjectPropertyType,
    'Date_Ran': cybox_common.DateTimeObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'If_Match': cybox_common.StringObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
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
        rootTag = 'Network_Connection'
        rootClass = NetworkConnectionObjectType
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
        rootTag = 'Network_Connection'
        rootClass = NetworkConnectionObjectType
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
        rootTag = 'Network_Connection'
        rootClass = NetworkConnectionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Network_Connection",
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
    "NetworkConnectionObjectType",
    "Layer7ConnectionsType",
    "Layer3ProtocolType",
    "Layer4ProtocolType",
    "Layer7ProtocolType"
    ]
