# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import address_object
from . import port_object
from . import uri_object


class HTTPRequestResponseType(GeneratedsSuper):
    """The HTTPRequestResponseType captures a single HTTP request/response
    pair.The ordinal_position attribute specifies the ordinal
    positioning of the HTTP request/response pair in the context of
    the HTTP session. This may be useful in certain cases for
    preserving observed HTTP request/response ordering."""
    subclass = None
    superclass = None
    def __init__(self, ordinal_position=None, HTTP_Client_Request=None, HTTP_Provisional_Server_Response=None, HTTP_Server_Response=None):
        self.ordinal_position = _cast(int, ordinal_position)
        self.HTTP_Client_Request = HTTP_Client_Request
        self.HTTP_Provisional_Server_Response = HTTP_Provisional_Server_Response
        self.HTTP_Server_Response = HTTP_Server_Response
    def factory(*args_, **kwargs_):
        if HTTPRequestResponseType.subclass:
            return HTTPRequestResponseType.subclass(*args_, **kwargs_)
        else:
            return HTTPRequestResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Client_Request(self): return self.HTTP_Client_Request
    def set_HTTP_Client_Request(self, HTTP_Client_Request): self.HTTP_Client_Request = HTTP_Client_Request
    def get_HTTP_Provisional_Server_Response(self): return self.HTTP_Provisional_Server_Response
    def set_HTTP_Provisional_Server_Response(self, HTTP_Provisional_Server_Response): self.HTTP_Provisional_Server_Response = HTTP_Provisional_Server_Response
    def get_HTTP_Server_Response(self): return self.HTTP_Server_Response
    def set_HTTP_Server_Response(self, HTTP_Server_Response): self.HTTP_Server_Response = HTTP_Server_Response
    def get_ordinal_position(self): return self.ordinal_position
    def set_ordinal_position(self, ordinal_position): self.ordinal_position = ordinal_position
    def hasContent_(self):
        if (
            self.HTTP_Client_Request is not None or
            self.HTTP_Provisional_Server_Response is not None or
            self.HTTP_Server_Response is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestResponseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPRequestResponseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPRequestResponseType'):
        if self.ordinal_position is not None:

            lwrite(' ordinal_position="%s"' % self.gds_format_integer(self.ordinal_position, input_name='ordinal_position'))
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HTTP_Client_Request is not None:
            self.HTTP_Client_Request.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Client_Request', pretty_print=pretty_print)
        if self.HTTP_Provisional_Server_Response is not None:
            self.HTTP_Provisional_Server_Response.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Provisional_Server_Response', pretty_print=pretty_print)
        if self.HTTP_Server_Response is not None:
            self.HTTP_Server_Response.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Server_Response', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ordinal_position', node)
        if value is not None:

            try:
                self.ordinal_position = int(value)
            except ValueError as exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
            if self.ordinal_position < 0:
                raise_parse_error(node, 'Invalid NonNegativeInteger')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'HTTP_Client_Request':
            obj_ = HTTPClientRequestType.factory()
            obj_.build(child_)
            self.set_HTTP_Client_Request(obj_)
        elif nodeName_ == 'HTTP_Provisional_Server_Response':
            obj_ = HTTPServerResponseType.factory()
            obj_.build(child_)
            self.set_HTTP_Provisional_Server_Response(obj_)
        elif nodeName_ == 'HTTP_Server_Response':
            obj_ = HTTPServerResponseType.factory()
            obj_.build(child_)
            self.set_HTTP_Server_Response(obj_)

class HTTPClientRequestType(GeneratedsSuper):
    """The HTTPClientRequestType field captures the details of an HTTP
    client request."""

    subclass = None
    superclass = None
    def __init__(self, HTTP_Request_Line=None, HTTP_Request_Header=None, HTTP_Message_Body=None):
        self.HTTP_Request_Line = HTTP_Request_Line
        self.HTTP_Request_Header = HTTP_Request_Header
        self.HTTP_Message_Body = HTTP_Message_Body
    def factory(*args_, **kwargs_):
        if HTTPClientRequestType.subclass:
            return HTTPClientRequestType.subclass(*args_, **kwargs_)
        else:
            return HTTPClientRequestType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Request_Line(self): return self.HTTP_Request_Line
    def set_HTTP_Request_Line(self, HTTP_Request_Line): self.HTTP_Request_Line = HTTP_Request_Line
    def get_HTTP_Request_Header(self): return self.HTTP_Request_Header
    def set_HTTP_Request_Header(self, HTTP_Request_Header): self.HTTP_Request_Header = HTTP_Request_Header
    def get_HTTP_Message_Body(self): return self.HTTP_Message_Body
    def set_HTTP_Message_Body(self, HTTP_Message_Body): self.HTTP_Message_Body = HTTP_Message_Body
    def hasContent_(self):
        if (
            self.HTTP_Request_Line is not None or
            self.HTTP_Request_Header is not None or
            self.HTTP_Message_Body is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPClientRequestType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPClientRequestType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPClientRequestType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPClientRequestType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HTTP_Request_Line is not None:
            self.HTTP_Request_Line.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Request_Line', pretty_print=pretty_print)
        if self.HTTP_Request_Header is not None:
            self.HTTP_Request_Header.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Request_Header', pretty_print=pretty_print)
        if self.HTTP_Message_Body is not None:
            self.HTTP_Message_Body.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Message_Body', pretty_print=pretty_print)
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
        if nodeName_ == 'HTTP_Request_Line':
            obj_ = HTTPRequestLineType.factory()
            obj_.build(child_)
            self.set_HTTP_Request_Line(obj_)
        elif nodeName_ == 'HTTP_Request_Header':
            obj_ = HTTPRequestHeaderType.factory()
            obj_.build(child_)
            self.set_HTTP_Request_Header(obj_)
        elif nodeName_ == 'HTTP_Message_Body':
            obj_ = HTTPMessageType.factory()
            obj_.build(child_)
            self.set_HTTP_Message_Body(obj_)
# end class HTTPClientRequestType

class HTTPServerResponseType(GeneratedsSuper):
    """The HTTPServerResponseType captures the details of an HTTP server
    response."""

    subclass = None
    superclass = None
    def __init__(self, HTTP_Status_Line=None, HTTP_Response_Header=None, HTTP_Message_Body=None):
        self.HTTP_Status_Line = HTTP_Status_Line
        self.HTTP_Response_Header = HTTP_Response_Header
        self.HTTP_Message_Body = HTTP_Message_Body
    def factory(*args_, **kwargs_):
        if HTTPServerResponseType.subclass:
            return HTTPServerResponseType.subclass(*args_, **kwargs_)
        else:
            return HTTPServerResponseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Status_Line(self): return self.HTTP_Status_Line
    def set_HTTP_Status_Line(self, HTTP_Status_Line): self.HTTP_Status_Line = HTTP_Status_Line
    def get_HTTP_Response_Header(self): return self.HTTP_Response_Header
    def set_HTTP_Response_Header(self, HTTP_Response_Header): self.HTTP_Response_Header = HTTP_Response_Header
    def get_HTTP_Message_Body(self): return self.HTTP_Message_Body
    def set_HTTP_Message_Body(self, HTTP_Message_Body): self.HTTP_Message_Body = HTTP_Message_Body
    def hasContent_(self):
        if (
            self.HTTP_Status_Line is not None or
            self.HTTP_Response_Header is not None or
            self.HTTP_Message_Body is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPServerResponseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPServerResponseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPServerResponseType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPServerResponseType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HTTP_Status_Line is not None:
            self.HTTP_Status_Line.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Status_Line', pretty_print=pretty_print)
        if self.HTTP_Response_Header is not None:
            self.HTTP_Response_Header.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Response_Header', pretty_print=pretty_print)
        if self.HTTP_Message_Body is not None:
            self.HTTP_Message_Body.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Message_Body', pretty_print=pretty_print)
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
        if nodeName_ == 'HTTP_Status_Line':
            obj_ = HTTPStatusLineType.factory()
            obj_.build(child_)
            self.set_HTTP_Status_Line(obj_)
        elif nodeName_ == 'HTTP_Response_Header':
            obj_ = HTTPResponseHeaderType.factory()
            obj_.build(child_)
            self.set_HTTP_Response_Header(obj_)
        elif nodeName_ == 'HTTP_Message_Body':
            obj_ = HTTPMessageType.factory()
            obj_.build(child_)
            self.set_HTTP_Message_Body(obj_)
# end class HTTPServerResponseType

class HTTPRequestLineType(GeneratedsSuper):
    """The HTTPRequestLineType captures a single HTTP request line."""

    subclass = None
    superclass = None
    def __init__(self, HTTP_Method=None, Value=None, Version=None):
        self.HTTP_Method = HTTP_Method
        self.Value = Value
        self.Version = Version
    def factory(*args_, **kwargs_):
        if HTTPRequestLineType.subclass:
            return HTTPRequestLineType.subclass(*args_, **kwargs_)
        else:
            return HTTPRequestLineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Method(self): return self.HTTP_Method
    def set_HTTP_Method(self, HTTP_Method): self.HTTP_Method = HTTP_Method
    def validate_HTTPMethodType(self, value):
        # Validate type HTTPMethodType, a restriction on None.
        pass
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def hasContent_(self):
        if (
            self.HTTP_Method is not None or
            self.Value is not None or
            self.Version is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestLineType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPRequestLineType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPRequestLineType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestLineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.HTTP_Method is not None:
            # Temporary fix for forcing datatype output
            #self.HTTP_Method.datatype = 'string'
            self.HTTP_Method.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Method', pretty_print=pretty_print)
        if self.Value is not None:
            self.Value.export(lwrite, level, 'HTTPSessionObj:', name_='Value', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(lwrite, level, 'HTTPSessionObj:', name_='Version', pretty_print=pretty_print)
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
        if nodeName_ == 'HTTP_Method':
            obj_ = HTTPMethodType.factory()
            obj_.build(child_)
            self.set_HTTP_Method(obj_)
        elif nodeName_ == 'Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Value(obj_)
        elif nodeName_ == 'Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
# end class HTTPRequestLineType

class HTTPRequestHeaderType(GeneratedsSuper):
    """The HTTPRequestHeaderType captures the raw or parsed header of an
    HTTP request."""

    subclass = None
    superclass = None
    def __init__(self, Raw_Header=None, Parsed_Header=None):
        self.Raw_Header = Raw_Header
        self.Parsed_Header = Parsed_Header
    def factory(*args_, **kwargs_):
        if HTTPRequestHeaderType.subclass:
            return HTTPRequestHeaderType.subclass(*args_, **kwargs_)
        else:
            return HTTPRequestHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Raw_Header(self): return self.Raw_Header
    def set_Raw_Header(self, Raw_Header): self.Raw_Header = Raw_Header
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Parsed_Header(self): return self.Parsed_Header
    def set_Parsed_Header(self, Parsed_Header): self.Parsed_Header = Parsed_Header
    def hasContent_(self):
        if (
            self.Raw_Header is not None or
            self.Parsed_Header is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPRequestHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Raw_Header is not None:
            if self.Raw_Header.get_valueOf_() is not None:
                value = self.Raw_Header.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Header.set_valueOf_(value)
            self.Raw_Header.export(lwrite, level, 'HTTPSessionObj:', name_='Raw_Header', pretty_print=pretty_print)
        if self.Parsed_Header is not None:
            self.Parsed_Header.export(lwrite, level, 'HTTPSessionObj:', name_='Parsed_Header', pretty_print=pretty_print)
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
        if nodeName_ == 'Raw_Header':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Header(obj_)
        elif nodeName_ == 'Parsed_Header':
            obj_ = HTTPRequestHeaderFieldsType.factory()
            obj_.build(child_)
            self.set_Parsed_Header(obj_)
# end class HTTPRequestHeaderType

class HTTPRequestHeaderFieldsType(GeneratedsSuper):
    """The HTTPRequestHeaderFieldsType captures parsed HTTP request header
    fields."""

    subclass = None
    superclass = None
    def __init__(self, Accept=None, Accept_Charset=None, Accept_Language=None, Accept_Datetime=None, Accept_Encoding=None, Authorization=None, Cache_Control=None, Connection=None, Cookie=None, Content_Length=None, Content_MD5=None, Content_Type=None, Date=None, Expect=None, From=None, Host=None, If_Match=None, If_Modified_Since=None, If_None_Match=None, If_Range=None, If_Unmodified_Since=None, Max_Forwards=None, Pragma=None, Proxy_Authorization=None, Range=None, Referer=None, TE=None, User_Agent=None, Via=None, Warning=None, DNT=None, X_Requested_With=None, X_Forwarded_For=None, X_Forwarded_Proto=None, X_ATT_DeviceId=None, X_Wap_Profile=None):
        self.Accept = Accept
        self.Accept_Charset = Accept_Charset
        self.Accept_Language = Accept_Language
        self.Accept_Datetime = Accept_Datetime
        self.Accept_Encoding = Accept_Encoding
        self.Authorization = Authorization
        self.Cache_Control = Cache_Control
        self.Connection = Connection
        self.Cookie = Cookie
        self.Content_Length = Content_Length
        self.Content_MD5 = Content_MD5
        self.Content_Type = Content_Type
        self.Date = Date
        self.Expect = Expect
        self.From = From
        self.Host = Host
        self.If_Match = If_Match
        self.If_Modified_Since = If_Modified_Since
        self.If_None_Match = If_None_Match
        self.If_Range = If_Range
        self.If_Unmodified_Since = If_Unmodified_Since
        self.Max_Forwards = Max_Forwards
        self.Pragma = Pragma
        self.Proxy_Authorization = Proxy_Authorization
        self.Range = Range
        self.Referer = Referer
        self.TE = TE
        self.User_Agent = User_Agent
        self.Via = Via
        self.Warning = Warning
        self.DNT = DNT
        self.X_Requested_With = X_Requested_With
        self.X_Forwarded_For = X_Forwarded_For
        self.X_Forwarded_Proto = X_Forwarded_Proto
        self.X_ATT_DeviceId = X_ATT_DeviceId
        self.X_Wap_Profile = X_Wap_Profile
    def factory(*args_, **kwargs_):
        if HTTPRequestHeaderFieldsType.subclass:
            return HTTPRequestHeaderFieldsType.subclass(*args_, **kwargs_)
        else:
            return HTTPRequestHeaderFieldsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Accept(self): return self.Accept
    def set_Accept(self, Accept): self.Accept = Accept
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Accept_Charset(self): return self.Accept_Charset
    def set_Accept_Charset(self, Accept_Charset): self.Accept_Charset = Accept_Charset
    def get_Accept_Language(self): return self.Accept_Language
    def set_Accept_Language(self, Accept_Language): self.Accept_Language = Accept_Language
    def get_Accept_Datetime(self): return self.Accept_Datetime
    def set_Accept_Datetime(self, Accept_Datetime): self.Accept_Datetime = Accept_Datetime
    def get_Accept_Encoding(self): return self.Accept_Encoding
    def set_Accept_Encoding(self, Accept_Encoding): self.Accept_Encoding = Accept_Encoding
    def get_Authorization(self): return self.Authorization
    def set_Authorization(self, Authorization): self.Authorization = Authorization
    def get_Cache_Control(self): return self.Cache_Control
    def set_Cache_Control(self, Cache_Control): self.Cache_Control = Cache_Control
    def get_Connection(self): return self.Connection
    def set_Connection(self, Connection): self.Connection = Connection
    def get_Cookie(self): return self.Cookie
    def set_Cookie(self, Cookie): self.Cookie = Cookie
    def get_Content_Length(self): return self.Content_Length
    def set_Content_Length(self, Content_Length): self.Content_Length = Content_Length
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Content_MD5(self): return self.Content_MD5
    def set_Content_MD5(self, Content_MD5): self.Content_MD5 = Content_MD5
    def get_Content_Type(self): return self.Content_Type
    def set_Content_Type(self, Content_Type): self.Content_Type = Content_Type
    def get_Date(self): return self.Date
    def set_Date(self, Date): self.Date = Date
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Expect(self): return self.Expect
    def set_Expect(self, Expect): self.Expect = Expect
    def get_From(self): return self.From
    def set_From(self, From): self.From = From
    def get_Host(self): return self.Host
    def set_Host(self, Host): self.Host = Host
    def get_If_Match(self): return self.If_Match
    def set_If_Match(self, If_Match): self.If_Match = If_Match
    def get_If_Modified_Since(self): return self.If_Modified_Since
    def set_If_Modified_Since(self, If_Modified_Since): self.If_Modified_Since = If_Modified_Since
    def get_If_None_Match(self): return self.If_None_Match
    def set_If_None_Match(self, If_None_Match): self.If_None_Match = If_None_Match
    def get_If_Range(self): return self.If_Range
    def set_If_Range(self, If_Range): self.If_Range = If_Range
    def get_If_Unmodified_Since(self): return self.If_Unmodified_Since
    def set_If_Unmodified_Since(self, If_Unmodified_Since): self.If_Unmodified_Since = If_Unmodified_Since
    def get_Max_Forwards(self): return self.Max_Forwards
    def set_Max_Forwards(self, Max_Forwards): self.Max_Forwards = Max_Forwards
    def get_Pragma(self): return self.Pragma
    def set_Pragma(self, Pragma): self.Pragma = Pragma
    def get_Proxy_Authorization(self): return self.Proxy_Authorization
    def set_Proxy_Authorization(self, Proxy_Authorization): self.Proxy_Authorization = Proxy_Authorization
    def get_Range(self): return self.Range
    def set_Range(self, Range): self.Range = Range
    def get_Referer(self): return self.Referer
    def set_Referer(self, Referer): self.Referer = Referer
    def get_TE(self): return self.TE
    def set_TE(self, TE): self.TE = TE
    def get_User_Agent(self): return self.User_Agent
    def set_User_Agent(self, User_Agent): self.User_Agent = User_Agent
    def get_Via(self): return self.Via
    def set_Via(self, Via): self.Via = Via
    def get_Warning(self): return self.Warning
    def set_Warning(self, Warning): self.Warning = Warning
    def get_DNT(self): return self.DNT
    def set_DNT(self, DNT): self.DNT = DNT
    def get_X_Requested_With(self): return self.X_Requested_With
    def set_X_Requested_With(self, X_Requested_With): self.X_Requested_With = X_Requested_With
    def get_X_Forwarded_For(self): return self.X_Forwarded_For
    def set_X_Forwarded_For(self, X_Forwarded_For): self.X_Forwarded_For = X_Forwarded_For
    def get_X_Forwarded_Proto(self): return self.X_Forwarded_Proto
    def set_X_Forwarded_Proto(self, X_Forwarded_Proto): self.X_Forwarded_Proto = X_Forwarded_Proto
    def get_X_ATT_DeviceId(self): return self.X_ATT_DeviceId
    def set_X_ATT_DeviceId(self, X_ATT_DeviceId): self.X_ATT_DeviceId = X_ATT_DeviceId
    def get_X_Wap_Profile(self): return self.X_Wap_Profile
    def set_X_Wap_Profile(self, X_Wap_Profile): self.X_Wap_Profile = X_Wap_Profile
    def hasContent_(self):
        if (
            self.Accept is not None or
            self.Accept_Charset is not None or
            self.Accept_Language is not None or
            self.Accept_Datetime is not None or
            self.Accept_Encoding is not None or
            self.Authorization is not None or
            self.Cache_Control is not None or
            self.Connection is not None or
            self.Cookie is not None or
            self.Content_Length is not None or
            self.Content_MD5 is not None or
            self.Content_Type is not None or
            self.Date is not None or
            self.Expect is not None or
            self.From is not None or
            self.Host is not None or
            self.If_Match is not None or
            self.If_Modified_Since is not None or
            self.If_None_Match is not None or
            self.If_Range is not None or
            self.If_Unmodified_Since is not None or
            self.Max_Forwards is not None or
            self.Pragma is not None or
            self.Proxy_Authorization is not None or
            self.Range is not None or
            self.Referer is not None or
            self.TE is not None or
            self.User_Agent is not None or
            self.Via is not None or
            self.Warning is not None or
            self.DNT is not None or
            self.X_Requested_With is not None or
            self.X_Forwarded_For is not None or
            self.X_Forwarded_Proto is not None or
            self.X_ATT_DeviceId is not None or
            self.X_Wap_Profile is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderFieldsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPRequestHeaderFieldsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderFieldsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPRequestHeaderFieldsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Accept is not None:
            self.Accept.export(lwrite, level, 'HTTPSessionObj:', name_='Accept', pretty_print=pretty_print)
        if self.Accept_Charset is not None:
            self.Accept_Charset.export(lwrite, level, 'HTTPSessionObj:', name_='Accept_Charset', pretty_print=pretty_print)
        if self.Accept_Language is not None:
            self.Accept_Language.export(lwrite, level, 'HTTPSessionObj:', name_='Accept_Language', pretty_print=pretty_print)
        if self.Accept_Datetime is not None:
            self.Accept_Datetime.export(lwrite, level, 'HTTPSessionObj:', name_='Accept_Datetime', pretty_print=pretty_print)
        if self.Accept_Encoding is not None:
            self.Accept_Encoding.export(lwrite, level, 'HTTPSessionObj:', name_='Accept_Encoding', pretty_print=pretty_print)
        if self.Authorization is not None:
            self.Authorization.export(lwrite, level, 'HTTPSessionObj:', name_='Authorization', pretty_print=pretty_print)
        if self.Cache_Control is not None:
            self.Cache_Control.export(lwrite, level, 'HTTPSessionObj:', name_='Cache_Control', pretty_print=pretty_print)
        if self.Connection is not None:
            self.Connection.export(lwrite, level, 'HTTPSessionObj:', name_='Connection', pretty_print=pretty_print)
        if self.Cookie is not None:
            self.Cookie.export(lwrite, level, 'HTTPSessionObj:', name_='Cookie', pretty_print=pretty_print)
        if self.Content_Length is not None:
            self.Content_Length.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Length', pretty_print=pretty_print)
        if self.Content_MD5 is not None:
            self.Content_MD5.export(lwrite, level, 'HTTPSessionObj:', name_='Content_MD5', pretty_print=pretty_print)
        if self.Content_Type is not None:
            self.Content_Type.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Type', pretty_print=pretty_print)
        if self.Date is not None:
            self.Date.export(lwrite, level, 'HTTPSessionObj:', name_='Date', pretty_print=pretty_print)
        if self.Expect is not None:
            self.Expect.export(lwrite, level, 'HTTPSessionObj:', name_='Expect', pretty_print=pretty_print)
        if self.From is not None:
            self.From.export(lwrite, level, 'HTTPSessionObj:', name_='From', pretty_print=pretty_print)
        if self.Host is not None:
            self.Host.export(lwrite, level, 'HTTPSessionObj:', name_='Host', pretty_print=pretty_print)
        if self.If_Match is not None:
            self.If_Match.export(lwrite, level, 'HTTPSessionObj:', name_='If_Match', pretty_print=pretty_print)
        if self.If_Modified_Since is not None:
            self.If_Modified_Since.export(lwrite, level, 'HTTPSessionObj:', name_='If_Modified_Since', pretty_print=pretty_print)
        if self.If_None_Match is not None:
            self.If_None_Match.export(lwrite, level, 'HTTPSessionObj:', name_='If_None_Match', pretty_print=pretty_print)
        if self.If_Range is not None:
            self.If_Range.export(lwrite, level, 'HTTPSessionObj:', name_='If_Range', pretty_print=pretty_print)
        if self.If_Unmodified_Since is not None:
            self.If_Unmodified_Since.export(lwrite, level, 'HTTPSessionObj:', name_='If_Unmodified_Since', pretty_print=pretty_print)
        if self.Max_Forwards is not None:
            self.Max_Forwards.export(lwrite, level, 'HTTPSessionObj:', name_='Max_Forwards', pretty_print=pretty_print)
        if self.Pragma is not None:
            self.Pragma.export(lwrite, level, 'HTTPSessionObj:', name_='Pragma', pretty_print=pretty_print)
        if self.Proxy_Authorization is not None:
            self.Proxy_Authorization.export(lwrite, level, 'HTTPSessionObj:', name_='Proxy_Authorization', pretty_print=pretty_print)
        if self.Range is not None:
            self.Range.export(lwrite, level, 'HTTPSessionObj:', name_='Range', pretty_print=pretty_print)
        if self.Referer is not None:
            self.Referer.export(lwrite, level, 'HTTPSessionObj:', name_='Referer', pretty_print=pretty_print)
        if self.TE is not None:
            self.TE.export(lwrite, level, 'HTTPSessionObj:', name_='TE', pretty_print=pretty_print)
        if self.User_Agent is not None:
            self.User_Agent.export(lwrite, level, 'HTTPSessionObj:', name_='User_Agent', pretty_print=pretty_print)
        if self.Via is not None:
            self.Via.export(lwrite, level, 'HTTPSessionObj:', name_='Via', pretty_print=pretty_print)
        if self.Warning is not None:
            self.Warning.export(lwrite, level, 'HTTPSessionObj:', name_='Warning', pretty_print=pretty_print)
        if self.DNT is not None:
            self.DNT.export(lwrite, level, 'HTTPSessionObj:', name_='DNT', pretty_print=pretty_print)
        if self.X_Requested_With is not None:
            self.X_Requested_With.export(lwrite, level, 'HTTPSessionObj:', name_='X_Requested_With', pretty_print=pretty_print)
        if self.X_Forwarded_For is not None:
            self.X_Forwarded_For.export(lwrite, level, 'HTTPSessionObj:', name_='X_Forwarded_For', pretty_print=pretty_print)
        if self.X_Forwarded_Proto is not None:
            self.X_Forwarded_Proto.export(lwrite, level, 'HTTPSessionObj:', name_='X_Forwarded_Proto', pretty_print=pretty_print)
        if self.X_ATT_DeviceId is not None:
            self.X_ATT_DeviceId.export(lwrite, level, 'HTTPSessionObj:', name_='X_ATT_DeviceId', pretty_print=pretty_print)
        if self.X_Wap_Profile is not None:
            self.X_Wap_Profile.export(lwrite, level, 'HTTPSessionObj:', name_='X_Wap_Profile', pretty_print=pretty_print)
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
        if nodeName_ == 'Accept':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept(obj_)
        elif nodeName_ == 'Accept_Charset':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept_Charset(obj_)
        elif nodeName_ == 'Accept_Language':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept_Language(obj_)
        elif nodeName_ == 'Accept_Datetime':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept_Datetime(obj_)
        elif nodeName_ == 'Accept_Encoding':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept_Encoding(obj_)
        elif nodeName_ == 'Authorization':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Authorization(obj_)
        elif nodeName_ == 'Cache_Control':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Cache_Control(obj_)
        elif nodeName_ == 'Connection':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Connection(obj_)
        elif nodeName_ == 'Cookie':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Cookie(obj_)
        elif nodeName_ == 'Content_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Length(obj_)
        elif nodeName_ == 'Content_MD5':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_MD5(obj_)
        elif nodeName_ == 'Content_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Type(obj_)
        elif nodeName_ == 'Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Date(obj_)
        elif nodeName_ == 'Expect':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Expect(obj_)
        elif nodeName_ == 'From':
            obj_ = address_object.AddressObjectType.factory()
            obj_.build(child_)
            self.set_From(obj_)
        elif nodeName_ == 'Host':
            obj_ = HostFieldType.factory()
            obj_.build(child_)
            self.set_Host(obj_)
        elif nodeName_ == 'If_Match':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_If_Match(obj_)
        elif nodeName_ == 'If_Modified_Since':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_If_Modified_Since(obj_)
        elif nodeName_ == 'If_None_Match':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_If_None_Match(obj_)
        elif nodeName_ == 'If_Range':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_If_Range(obj_)
        elif nodeName_ == 'If_Unmodified_Since':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_If_Unmodified_Since(obj_)
        elif nodeName_ == 'Max_Forwards':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Max_Forwards(obj_)
        elif nodeName_ == 'Pragma':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pragma(obj_)
        elif nodeName_ == 'Proxy_Authorization':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Proxy_Authorization(obj_)
        elif nodeName_ == 'Range':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Range(obj_)
        elif nodeName_ == 'Referer':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Referer(obj_)
        elif nodeName_ == 'TE':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_TE(obj_)
        elif nodeName_ == 'User_Agent':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Agent(obj_)
        elif nodeName_ == 'Via':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Via(obj_)
        elif nodeName_ == 'Warning':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Warning(obj_)
        elif nodeName_ == 'DNT':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_DNT(obj_)
        elif nodeName_ == 'X_Requested_With':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Requested_With(obj_)
        elif nodeName_ == 'X_Forwarded_For':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Forwarded_For(obj_)
        elif nodeName_ == 'X_Forwarded_Proto':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Forwarded_Proto(obj_)
        elif nodeName_ == 'X_ATT_DeviceId':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_ATT_DeviceId(obj_)
        elif nodeName_ == 'X_Wap_Profile':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_X_Wap_Profile(obj_)
# end class HTTPRequestHeaderFieldsType

class HTTPResponseHeaderType(GeneratedsSuper):
    """The HTTPResponseHeaderType captures the raw or parsed header of an
    HTTP response."""

    subclass = None
    superclass = None
    def __init__(self, Raw_Header=None, Parsed_Header=None):
        self.Raw_Header = Raw_Header
        self.Parsed_Header = Parsed_Header
    def factory(*args_, **kwargs_):
        if HTTPResponseHeaderType.subclass:
            return HTTPResponseHeaderType.subclass(*args_, **kwargs_)
        else:
            return HTTPResponseHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Raw_Header(self): return self.Raw_Header
    def set_Raw_Header(self, Raw_Header): self.Raw_Header = Raw_Header
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Parsed_Header(self): return self.Parsed_Header
    def set_Parsed_Header(self, Parsed_Header): self.Parsed_Header = Parsed_Header
    def hasContent_(self):
        if (
            self.Raw_Header is not None or
            self.Parsed_Header is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPResponseHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Raw_Header is not None:
            if self.Raw_Header.get_valueOf_() is not None:
                value = self.Raw_Header.get_valueOf_()
                if not value.startswith('<![CDATA['):
                    value = '<![CDATA[' + value + ']]>'
                    self.Raw_Header.set_valueOf_(value)
            self.Raw_Header.export(lwrite, level, 'HTTPSessionObj:', name_='Raw_Header', pretty_print=pretty_print)
        if self.Parsed_Header is not None:
            self.Parsed_Header.export(lwrite, level, 'HTTPSessionObj:', name_='Parsed_Header', pretty_print=pretty_print)
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
        if nodeName_ == 'Raw_Header':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Raw_Header(obj_)
        elif nodeName_ == 'Parsed_Header':
            obj_ = HTTPResponseHeaderFieldsType.factory()
            obj_.build(child_)
            self.set_Parsed_Header(obj_)
# end class HTTPResponseHeaderType

class HTTPResponseHeaderFieldsType(GeneratedsSuper):
    """The HTTPRequestHeaderFieldsType captures parsed HTTP request header
    fields."""

    subclass = None
    superclass = None
    def __init__(self, Access_Control_Allow_Origin=None, Accept_Ranges=None, Age=None, Cache_Control=None, Connection=None, Content_Encoding=None, Content_Language=None, Content_Length=None, Content_Location=None, Content_MD5=None, Content_Disposition=None, Content_Range=None, Content_Type=None, Date=None, ETag=None, Expires=None, Last_Modified=None, Link=None, Location=None, P3P=None, Pragma=None, Proxy_Authenticate=None, Refresh=None, Retry_After=None, Server=None, Set_Cookie=None, Strict_Transport_Security=None, Trailer=None, Transfer_Encoding=None, Vary=None, Via=None, Warning=None, WWW_Authenticate=None, X_Frame_Options=None, X_XSS_Protection=None, X_Content_Type_Options=None, X_Powered_By=None, X_UA_Compatible=None):
        self.Access_Control_Allow_Origin = Access_Control_Allow_Origin
        self.Accept_Ranges = Accept_Ranges
        self.Age = Age
        self.Cache_Control = Cache_Control
        self.Connection = Connection
        self.Content_Encoding = Content_Encoding
        self.Content_Language = Content_Language
        self.Content_Length = Content_Length
        self.Content_Location = Content_Location
        self.Content_MD5 = Content_MD5
        self.Content_Disposition = Content_Disposition
        self.Content_Range = Content_Range
        self.Content_Type = Content_Type
        self.Date = Date
        self.ETag = ETag
        self.Expires = Expires
        self.Last_Modified = Last_Modified
        self.Link = Link
        self.Location = Location
        self.P3P = P3P
        self.Pragma = Pragma
        self.Proxy_Authenticate = Proxy_Authenticate
        self.Refresh = Refresh
        self.Retry_After = Retry_After
        self.Server = Server
        self.Set_Cookie = Set_Cookie
        self.Strict_Transport_Security = Strict_Transport_Security
        self.Trailer = Trailer
        self.Transfer_Encoding = Transfer_Encoding
        self.Vary = Vary
        self.Via = Via
        self.Warning = Warning
        self.WWW_Authenticate = WWW_Authenticate
        self.X_Frame_Options = X_Frame_Options
        self.X_XSS_Protection = X_XSS_Protection
        self.X_Content_Type_Options = X_Content_Type_Options
        self.X_Powered_By = X_Powered_By
        self.X_UA_Compatible = X_UA_Compatible
    def factory(*args_, **kwargs_):
        if HTTPResponseHeaderFieldsType.subclass:
            return HTTPResponseHeaderFieldsType.subclass(*args_, **kwargs_)
        else:
            return HTTPResponseHeaderFieldsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Access_Control_Allow_Origin(self): return self.Access_Control_Allow_Origin
    def set_Access_Control_Allow_Origin(self, Access_Control_Allow_Origin): self.Access_Control_Allow_Origin = Access_Control_Allow_Origin
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Accept_Ranges(self): return self.Accept_Ranges
    def set_Accept_Ranges(self, Accept_Ranges): self.Accept_Ranges = Accept_Ranges
    def get_Age(self): return self.Age
    def set_Age(self, Age): self.Age = Age
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_Cache_Control(self): return self.Cache_Control
    def set_Cache_Control(self, Cache_Control): self.Cache_Control = Cache_Control
    def get_Connection(self): return self.Connection
    def set_Connection(self, Connection): self.Connection = Connection
    def get_Content_Encoding(self): return self.Content_Encoding
    def set_Content_Encoding(self, Content_Encoding): self.Content_Encoding = Content_Encoding
    def get_Content_Language(self): return self.Content_Language
    def set_Content_Language(self, Content_Language): self.Content_Language = Content_Language
    def get_Content_Length(self): return self.Content_Length
    def set_Content_Length(self, Content_Length): self.Content_Length = Content_Length
    def get_Content_Location(self): return self.Content_Location
    def set_Content_Location(self, Content_Location): self.Content_Location = Content_Location
    def get_Content_MD5(self): return self.Content_MD5
    def set_Content_MD5(self, Content_MD5): self.Content_MD5 = Content_MD5
    def get_Content_Disposition(self): return self.Content_Disposition
    def set_Content_Disposition(self, Content_Disposition): self.Content_Disposition = Content_Disposition
    def get_Content_Range(self): return self.Content_Range
    def set_Content_Range(self, Content_Range): self.Content_Range = Content_Range
    def get_Content_Type(self): return self.Content_Type
    def set_Content_Type(self, Content_Type): self.Content_Type = Content_Type
    def get_Date(self): return self.Date
    def set_Date(self, Date): self.Date = Date
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_ETag(self): return self.ETag
    def set_ETag(self, ETag): self.ETag = ETag
    def get_Expires(self): return self.Expires
    def set_Expires(self, Expires): self.Expires = Expires
    def get_Last_Modified(self): return self.Last_Modified
    def set_Last_Modified(self, Last_Modified): self.Last_Modified = Last_Modified
    def get_Link(self): return self.Link
    def set_Link(self, Link): self.Link = Link
    def get_Location(self): return self.Location
    def set_Location(self, Location): self.Location = Location
    def get_P3P(self): return self.P3P
    def set_P3P(self, P3P): self.P3P = P3P
    def get_Pragma(self): return self.Pragma
    def set_Pragma(self, Pragma): self.Pragma = Pragma
    def get_Proxy_Authenticate(self): return self.Proxy_Authenticate
    def set_Proxy_Authenticate(self, Proxy_Authenticate): self.Proxy_Authenticate = Proxy_Authenticate
    def get_Refresh(self): return self.Refresh
    def set_Refresh(self, Refresh): self.Refresh = Refresh
    def get_Retry_After(self): return self.Retry_After
    def set_Retry_After(self, Retry_After): self.Retry_After = Retry_After
    def get_Server(self): return self.Server
    def set_Server(self, Server): self.Server = Server
    def get_Set_Cookie(self): return self.Set_Cookie
    def set_Set_Cookie(self, Set_Cookie): self.Set_Cookie = Set_Cookie
    def get_Strict_Transport_Security(self): return self.Strict_Transport_Security
    def set_Strict_Transport_Security(self, Strict_Transport_Security): self.Strict_Transport_Security = Strict_Transport_Security
    def get_Trailer(self): return self.Trailer
    def set_Trailer(self, Trailer): self.Trailer = Trailer
    def get_Transfer_Encoding(self): return self.Transfer_Encoding
    def set_Transfer_Encoding(self, Transfer_Encoding): self.Transfer_Encoding = Transfer_Encoding
    def get_Vary(self): return self.Vary
    def set_Vary(self, Vary): self.Vary = Vary
    def get_Via(self): return self.Via
    def set_Via(self, Via): self.Via = Via
    def get_Warning(self): return self.Warning
    def set_Warning(self, Warning): self.Warning = Warning
    def get_WWW_Authenticate(self): return self.WWW_Authenticate
    def set_WWW_Authenticate(self, WWW_Authenticate): self.WWW_Authenticate = WWW_Authenticate
    def get_X_Frame_Options(self): return self.X_Frame_Options
    def set_X_Frame_Options(self, X_Frame_Options): self.X_Frame_Options = X_Frame_Options
    def get_X_XSS_Protection(self): return self.X_XSS_Protection
    def set_X_XSS_Protection(self, X_XSS_Protection): self.X_XSS_Protection = X_XSS_Protection
    def get_X_Content_Type_Options(self): return self.X_Content_Type_Options
    def set_X_Content_Type_Options(self, X_Content_Type_Options): self.X_Content_Type_Options = X_Content_Type_Options
    def get_X_Powered_By(self): return self.X_Powered_By
    def set_X_Powered_By(self, X_Powered_By): self.X_Powered_By = X_Powered_By
    def get_X_UA_Compatible(self): return self.X_UA_Compatible
    def set_X_UA_Compatible(self, X_UA_Compatible): self.X_UA_Compatible = X_UA_Compatible
    def hasContent_(self):
        if (
            self.Access_Control_Allow_Origin is not None or
            self.Accept_Ranges is not None or
            self.Age is not None or
            self.Cache_Control is not None or
            self.Connection is not None or
            self.Content_Encoding is not None or
            self.Content_Language is not None or
            self.Content_Length is not None or
            self.Content_Location is not None or
            self.Content_MD5 is not None or
            self.Content_Disposition is not None or
            self.Content_Range is not None or
            self.Content_Type is not None or
            self.Date is not None or
            self.ETag is not None or
            self.Expires is not None or
            self.Last_Modified is not None or
            self.Link is not None or
            self.Location is not None or
            self.P3P is not None or
            self.Pragma is not None or
            self.Proxy_Authenticate is not None or
            self.Refresh is not None or
            self.Retry_After is not None or
            self.Server is not None or
            self.Set_Cookie is not None or
            self.Strict_Transport_Security is not None or
            self.Trailer is not None or
            self.Transfer_Encoding is not None or
            self.Vary is not None or
            self.Via is not None or
            self.Warning is not None or
            self.WWW_Authenticate is not None or
            self.X_Frame_Options is not None or
            self.X_XSS_Protection is not None or
            self.X_Content_Type_Options is not None or
            self.X_Powered_By is not None or
            self.X_UA_Compatible is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderFieldsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPResponseHeaderFieldsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderFieldsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPResponseHeaderFieldsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Access_Control_Allow_Origin is not None:
            self.Access_Control_Allow_Origin.export(lwrite, level, 'HTTPSessionObj:', name_='Access_Control_Allow_Origin', pretty_print=pretty_print)
        if self.Accept_Ranges is not None:
            self.Accept_Ranges.export(lwrite, level, 'HTTPSessionObj:', name_='Accept_Ranges', pretty_print=pretty_print)
        if self.Age is not None:
            self.Age.export(lwrite, level, 'HTTPSessionObj:', name_='Age', pretty_print=pretty_print)
        if self.Cache_Control is not None:
            self.Cache_Control.export(lwrite, level, 'HTTPSessionObj:', name_='Cache_Control', pretty_print=pretty_print)
        if self.Connection is not None:
            self.Connection.export(lwrite, level, 'HTTPSessionObj:', name_='Connection', pretty_print=pretty_print)
        if self.Content_Encoding is not None:
            self.Content_Encoding.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Encoding', pretty_print=pretty_print)
        if self.Content_Language is not None:
            self.Content_Language.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Language', pretty_print=pretty_print)
        if self.Content_Length is not None:
            self.Content_Length.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Length', pretty_print=pretty_print)
        if self.Content_Location is not None:
            self.Content_Location.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Location', pretty_print=pretty_print)
        if self.Content_MD5 is not None:
            self.Content_MD5.export(lwrite, level, 'HTTPSessionObj:', name_='Content_MD5', pretty_print=pretty_print)
        if self.Content_Disposition is not None:
            self.Content_Disposition.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Disposition', pretty_print=pretty_print)
        if self.Content_Range is not None:
            self.Content_Range.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Range', pretty_print=pretty_print)
        if self.Content_Type is not None:
            self.Content_Type.export(lwrite, level, 'HTTPSessionObj:', name_='Content_Type', pretty_print=pretty_print)
        if self.Date is not None:
            self.Date.export(lwrite, level, 'HTTPSessionObj:', name_='Date', pretty_print=pretty_print)
        if self.ETag is not None:
            self.ETag.export(lwrite, level, 'HTTPSessionObj:', name_='ETag', pretty_print=pretty_print)
        if self.Expires is not None:
            self.Expires.export(lwrite, level, 'HTTPSessionObj:', name_='Expires', pretty_print=pretty_print)
        if self.Last_Modified is not None:
            self.Last_Modified.export(lwrite, level, 'HTTPSessionObj:', name_='Last_Modified', pretty_print=pretty_print)
        if self.Link is not None:
            self.Link.export(lwrite, level, 'HTTPSessionObj:', name_='Link', pretty_print=pretty_print)
        if self.Location is not None:
            self.Location.export(lwrite, level, 'HTTPSessionObj:', name_='Location', pretty_print=pretty_print)
        if self.P3P is not None:
            self.P3P.export(lwrite, level, 'HTTPSessionObj:', name_='P3P', pretty_print=pretty_print)
        if self.Pragma is not None:
            self.Pragma.export(lwrite, level, 'HTTPSessionObj:', name_='Pragma', pretty_print=pretty_print)
        if self.Proxy_Authenticate is not None:
            self.Proxy_Authenticate.export(lwrite, level, 'HTTPSessionObj:', name_='Proxy_Authenticate', pretty_print=pretty_print)
        if self.Refresh is not None:
            self.Refresh.export(lwrite, level, 'HTTPSessionObj:', name_='Refresh', pretty_print=pretty_print)
        if self.Retry_After is not None:
            self.Retry_After.export(lwrite, level, 'HTTPSessionObj:', name_='Retry_After', pretty_print=pretty_print)
        if self.Server is not None:
            self.Server.export(lwrite, level, 'HTTPSessionObj:', name_='Server', pretty_print=pretty_print)
        if self.Set_Cookie is not None:
            self.Set_Cookie.export(lwrite, level, 'HTTPSessionObj:', name_='Set_Cookie', pretty_print=pretty_print)
        if self.Strict_Transport_Security is not None:
            self.Strict_Transport_Security.export(lwrite, level, 'HTTPSessionObj:', name_='Strict_Transport_Security', pretty_print=pretty_print)
        if self.Trailer is not None:
            self.Trailer.export(lwrite, level, 'HTTPSessionObj:', name_='Trailer', pretty_print=pretty_print)
        if self.Transfer_Encoding is not None:
            self.Transfer_Encoding.export(lwrite, level, 'HTTPSessionObj:', name_='Transfer_Encoding', pretty_print=pretty_print)
        if self.Vary is not None:
            self.Vary.export(lwrite, level, 'HTTPSessionObj:', name_='Vary', pretty_print=pretty_print)
        if self.Via is not None:
            self.Via.export(lwrite, level, 'HTTPSessionObj:', name_='Via', pretty_print=pretty_print)
        if self.Warning is not None:
            self.Warning.export(lwrite, level, 'HTTPSessionObj:', name_='Warning', pretty_print=pretty_print)
        if self.WWW_Authenticate is not None:
            self.WWW_Authenticate.export(lwrite, level, 'HTTPSessionObj:', name_='WWW_Authenticate', pretty_print=pretty_print)
        if self.X_Frame_Options is not None:
            self.X_Frame_Options.export(lwrite, level, 'HTTPSessionObj:', name_='X_Frame_Options', pretty_print=pretty_print)
        if self.X_XSS_Protection is not None:
            self.X_XSS_Protection.export(lwrite, level, 'HTTPSessionObj:', name_='X_XSS_Protection', pretty_print=pretty_print)
        if self.X_Content_Type_Options is not None:
            self.X_Content_Type_Options.export(lwrite, level, 'HTTPSessionObj:', name_='X_Content_Type_Options', pretty_print=pretty_print)
        if self.X_Powered_By is not None:
            self.X_Powered_By.export(lwrite, level, 'HTTPSessionObj:', name_='X_Powered_By', pretty_print=pretty_print)
        if self.X_UA_Compatible is not None:
            self.X_UA_Compatible.export(lwrite, level, 'HTTPSessionObj:', name_='X_UA_Compatible', pretty_print=pretty_print)
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
        if nodeName_ == 'Access_Control_Allow_Origin':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Access_Control_Allow_Origin(obj_)
        elif nodeName_ == 'Accept_Ranges':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Accept_Ranges(obj_)
        elif nodeName_ == 'Age':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Age(obj_)
        elif nodeName_ == 'Cache_Control':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Cache_Control(obj_)
        elif nodeName_ == 'Connection':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Connection(obj_)
        elif nodeName_ == 'Content_Encoding':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Encoding(obj_)
        elif nodeName_ == 'Content_Language':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Language(obj_)
        elif nodeName_ == 'Content_Length':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Length(obj_)
        elif nodeName_ == 'Content_Location':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Location(obj_)
        elif nodeName_ == 'Content_MD5':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_MD5(obj_)
        elif nodeName_ == 'Content_Disposition':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Disposition(obj_)
        elif nodeName_ == 'Content_Range':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Range(obj_)
        elif nodeName_ == 'Content_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Content_Type(obj_)
        elif nodeName_ == 'Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Date(obj_)
        elif nodeName_ == 'ETag':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_ETag(obj_)
        elif nodeName_ == 'Expires':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Expires(obj_)
        elif nodeName_ == 'Last_Modified':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Modified(obj_)
        elif nodeName_ == 'Link':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Link(obj_)
        elif nodeName_ == 'Location':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Location(obj_)
        elif nodeName_ == 'P3P':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_P3P(obj_)
        elif nodeName_ == 'Pragma':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pragma(obj_)
        elif nodeName_ == 'Proxy_Authenticate':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Proxy_Authenticate(obj_)
        elif nodeName_ == 'Refresh':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Refresh(obj_)
        elif nodeName_ == 'Retry_After':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Retry_After(obj_)
        elif nodeName_ == 'Server':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Server(obj_)
        elif nodeName_ == 'Set_Cookie':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Set_Cookie(obj_)
        elif nodeName_ == 'Strict_Transport_Security':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Strict_Transport_Security(obj_)
        elif nodeName_ == 'Trailer':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trailer(obj_)
        elif nodeName_ == 'Transfer_Encoding':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Transfer_Encoding(obj_)
        elif nodeName_ == 'Vary':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Vary(obj_)
        elif nodeName_ == 'Via':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Via(obj_)
        elif nodeName_ == 'Warning':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Warning(obj_)
        elif nodeName_ == 'WWW_Authenticate':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_WWW_Authenticate(obj_)
        elif nodeName_ == 'X_Frame_Options':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Frame_Options(obj_)
        elif nodeName_ == 'X_XSS_Protection':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_XSS_Protection(obj_)
        elif nodeName_ == 'X_Content_Type_Options':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Content_Type_Options(obj_)
        elif nodeName_ == 'X_Powered_By':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_Powered_By(obj_)
        elif nodeName_ == 'X_UA_Compatible':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_X_UA_Compatible(obj_)
# end class HTTPResponseHeaderFieldsType

class HTTPMessageType(GeneratedsSuper):
    """The HTTPMessageType captures a single HTTP message body and its
    length."""

    subclass = None
    superclass = None
    def __init__(self, Length=None, Message_Body=None):
        self.Length = Length
        self.Message_Body = Message_Body
    def factory(*args_, **kwargs_):
        if HTTPMessageType.subclass:
            return HTTPMessageType.subclass(*args_, **kwargs_)
        else:
            return HTTPMessageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Length(self): return self.Length
    def set_Length(self, Length): self.Length = Length
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Message_Body(self): return self.Message_Body
    def set_Message_Body(self, Message_Body): self.Message_Body = Message_Body
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Length is not None or
            self.Message_Body is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPMessageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPMessageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPMessageType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPMessageType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Length is not None:
            self.Length.export(lwrite, level, 'HTTPSessionObj:', name_='Length', pretty_print=pretty_print)
        if self.Message_Body is not None:
            self.Message_Body.export(lwrite, level, 'HTTPSessionObj:', name_='Message_Body', pretty_print=pretty_print)
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
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Length(obj_)
        elif nodeName_ == 'Message_Body':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Message_Body(obj_)
# end class HTTPMessageType

class HTTPStatusLineType(GeneratedsSuper):
    """The HTTPStatusLineType captures a single HTTP response status line."""

    subclass = None
    superclass = None
    def __init__(self, Version=None, Status_Code=None, Reason_Phrase=None):
        self.Version = Version
        self.Status_Code = Status_Code
        self.Reason_Phrase = Reason_Phrase
    def factory(*args_, **kwargs_):
        if HTTPStatusLineType.subclass:
            return HTTPStatusLineType.subclass(*args_, **kwargs_)
        else:
            return HTTPStatusLineType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Status_Code(self): return self.Status_Code
    def set_Status_Code(self, Status_Code): self.Status_Code = Status_Code
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Reason_Phrase(self): return self.Reason_Phrase
    def set_Reason_Phrase(self, Reason_Phrase): self.Reason_Phrase = Reason_Phrase
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Status_Code is not None or
            self.Reason_Phrase is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPStatusLineType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPStatusLineType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPStatusLineType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPStatusLineType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            self.Version.export(lwrite, level, 'HTTPSessionObj:', name_='Version', pretty_print=pretty_print)
        if self.Status_Code is not None:
            self.Status_Code.export(lwrite, level, 'HTTPSessionObj:', name_='Status_Code', pretty_print=pretty_print)
        if self.Reason_Phrase is not None:
            self.Reason_Phrase.export(lwrite, level, 'HTTPSessionObj:', name_='Reason_Phrase', pretty_print=pretty_print)
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
        if nodeName_ == 'Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        elif nodeName_ == 'Status_Code':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Status_Code(obj_)
        elif nodeName_ == 'Reason_Phrase':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Reason_Phrase(obj_)
# end class HTTPStatusLineType

class HostFieldType(GeneratedsSuper):
    """The HostFieldType captures the details of the HTTP request Host
    header field."""

    subclass = None
    superclass = None
    def __init__(self, Domain_Name=None, Port=None):
        self.Domain_Name = Domain_Name
        self.Port = Port
    def factory(*args_, **kwargs_):
        if HostFieldType.subclass:
            return HostFieldType.subclass(*args_, **kwargs_)
        else:
            return HostFieldType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Domain_Name(self): return self.Domain_Name
    def set_Domain_Name(self, Domain_Name): self.Domain_Name = Domain_Name
    def get_Port(self): return self.Port
    def set_Port(self, Port): self.Port = Port
    def hasContent_(self):
        if (
            self.Domain_Name is not None or
            self.Port is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HostFieldType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HostFieldType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HostFieldType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HostFieldType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Domain_Name is not None:
            self.Domain_Name.export(lwrite, level, 'HTTPSessionObj:', name_='Domain_Name', pretty_print=pretty_print)
        if self.Port is not None:
            self.Port.export(lwrite, level, 'HTTPSessionObj:', name_='Port', pretty_print=pretty_print)
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
        if nodeName_ == 'Domain_Name':
            obj_ = uri_object.URIObjectType.factory()
            obj_.build(child_)
            self.set_Domain_Name(obj_)
        elif nodeName_ == 'Port':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.set_Port(obj_)
# end class HostFieldType

class HTTPMethodType(cybox_common.BaseObjectPropertyType):
    """HTTPMethodType specifies HTTP method types, via a union of the
    HTTPMethodEnum type and the atomic xs:string type. Its base type
    is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(HTTPMethodType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if HTTPMethodType.subclass:
            return HTTPMethodType.subclass(*args_, **kwargs_)
        else:
            return HTTPMethodType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(HTTPMethodType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPMethodType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPMethodType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPMethodType'):
        super(HTTPMethodType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPMethodType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPMethodType', fromsubclass_=False, pretty_print=True):
        super(HTTPMethodType, self).exportChildren(lwrite, level, 'HTTPSessionObj:', name_, True, pretty_print=pretty_print)
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
        super(HTTPMethodType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class HTTPMethodType

class HTTPSessionObjectType(cybox_common.ObjectPropertiesType):
    """The HTTPSessionObjectType is intended to capture the details of an
    HTTP session."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, HTTP_Request_Response=None):
        super(HTTPSessionObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        if HTTP_Request_Response is None:
            self.HTTP_Request_Response = []
        else:
            self.HTTP_Request_Response = HTTP_Request_Response
    def factory(*args_, **kwargs_):
        if HTTPSessionObjectType.subclass:
            return HTTPSessionObjectType.subclass(*args_, **kwargs_)
        else:
            return HTTPSessionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_HTTP_Request_Response(self): return self.HTTP_Request_Response
    def set_HTTP_Request_Response(self, HTTP_Request_Response): self.HTTP_Request_Response = HTTP_Request_Response
    def add_HTTP_Request_Response(self, value): self.HTTP_Request_Response.append(value)
    def insert_HTTP_Request_Response(self, index, value): self.HTTP_Request_Response[index] = value
    def hasContent_(self):
        if (
            self.HTTP_Request_Response or
            super(HTTPSessionObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPSessionObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPSessionObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='HTTPSessionObj:', name_='HTTPSessionObjectType'):
        super(HTTPSessionObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='HTTPSessionObjectType')
    def exportChildren(self, lwrite, level, namespace_='HTTPSessionObj:', name_='HTTPSessionObjectType', fromsubclass_=False, pretty_print=True):
        super(HTTPSessionObjectType, self).exportChildren(lwrite, level, 'HTTPSessionObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for HTTP_Request_Response_ in self.HTTP_Request_Response:
            HTTP_Request_Response_.export(lwrite, level, 'HTTPSessionObj:', name_='HTTP_Request_Response', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(HTTPSessionObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'HTTP_Request_Response':
            obj_ = HTTPRequestResponseType.factory()
            obj_.build(child_)
            self.HTTP_Request_Response.append(obj_)
        super(HTTPSessionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class HTTPSessionObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'URI': uri_object.URIObjectType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Warning': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'Layer4_Protocol': port_object.Layer4ProtocolType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'From': address_object.AddressObjectType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Location': uri_object.URIObjectType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Link': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Server': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Via': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Contributors': cybox_common.PersonnelType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Expect': cybox_common.StringObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'X_Forwarded_For': cybox_common.StringObjectPropertyType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'Domain_Name': uri_object.URIObjectType,
    'Dependencies': cybox_common.DependenciesType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Referer': uri_object.URIObjectType,
    'Hashes': cybox_common.HashListType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'DNT': cybox_common.StringObjectPropertyType,
    'Connection': cybox_common.StringObjectPropertyType,
    'X_Requested_With': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'P3P': cybox_common.StringObjectPropertyType,
    'If_Unmodified_Since': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'ETag': cybox_common.StringObjectPropertyType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'Vary': uri_object.URIObjectType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'X_Wap_Profile': uri_object.URIObjectType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Address': address_object.AddressObjectType,
    'TE': cybox_common.StringObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Dependency': cybox_common.DependencyType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'String': cybox_common.ExtractedStringType,
    'Tools': cybox_common.ToolsInformationType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'If_Match': cybox_common.StringObjectPropertyType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Port': port_object.PortObjectType,
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
        rootTag = 'HTTP_Session'
        rootClass = HTTPSessionObjectType
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
        rootTag = 'HTTP_Session'
        rootClass = HTTPSessionObjectType
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
        rootTag = 'HTTP_Session'
        rootClass = HTTPSessionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="HTTP_Session",
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
    "HTTPSessionObjectType",
    "HTTPRequestResponseType",
    "HTTPClientRequestType",
    "HTTPServerResponseType",
    "HTTPRequestLineType",
    "HTTPRequestHeaderType",
    "HTTPRequestHeaderFieldsType",
    "HTTPResponseHeaderType",
    "HTTPResponseHeaderFieldsType",
    "HTTPMessageType",
    "HTTPStatusLineType",
    "HostFieldType",
    "HTTPMethodType"
    ]
