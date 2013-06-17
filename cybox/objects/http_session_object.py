# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.http_session_object as http_session_binding
from cybox.objects.uri_object import URI
from cybox.objects.address_object import Address
from cybox.objects.port_object import Port
from cybox.common import ObjectProperties, String, DateTime, PositiveInteger, Integer

class HTTPSession(ObjectProperties):
    _XSI_NS = "HTTPSessionObj"
    _XSI_TYPE = "HTTPSessionObjectType"

    def __init__(self):
        super(HTTPSession, self).__init__()
        self.http_request_responses = []

    def to_obj(self):
        http_session_obj = http_session_binding.HTTPSessionObjectType()
        super(HTTPSession, self).to_obj(http_session_obj)
        if len(self.http_request_responses) > 0 :
            for request_response in self.http_request_responses:
                http_session_obj.add_HTTP_Request_Response(request_response.to_obj())
        return http_session_obj

    def to_dict(self):
        http_session_dict = {}
        super(HTTPSession, self).to_dict(http_session_dict)

        if len(self.http_request_responses) > 0 :
            request_response_list = []
            for request_response in self.http_request_responses:
                request_response_list.append(request_response.to_dict())
            http_session_dict['http_request_responses'] = request_response_list
        return http_session_dict

    @staticmethod
    def from_dict(http_session_dict):
        if not http_session_dict:
            return None
        http_session_ = HTTPSession()
        http_session_.http_request_responses = [HTTPRequestResponse.from_dict(x) for x in http_session_dict.get('http_request_responses', [])]
        return http_session_

    @staticmethod
    def from_obj(http_session_obj):
        if not http_session_obj:
            return None
        http_session_ = HTTPSession()
        http_session_.http_request_responses = [HTTPRequestResponse.from_obj(x) for x in http_session_obj.get_HTTP_Request_Response()]
        return http_session_

class HTTPRequestResponse(cybox.Entity):
    def __init__(self):
        super(HTTPRequestResponse, self).__init__()
        self.http_client_request = None
        self.http_server_response = None

    def to_obj(self):
        http_request_response_obj = http_session_binding.HTTPRequestResponseType()
        if self.http_client_request is not None: http_request_response_obj.set_HTTP_Client_Request(self.http_client_request.to_obj())
        if self.http_server_response is not None: http_request_response_obj.set_HTTP_Server_Response(self.http_server_response.to_obj())
        return http_request_response_obj

    def to_dict(self):
        http_request_response_dict = {}
        if self.http_client_request is not None: http_request_response_dict['http_client_request'] = self.http_client_request.to_dict()
        if self.http_server_response is not None: http_request_response_dict['http_server_response'] = self.http_server_response.to_dict()
        return http_request_response_dict

    @staticmethod
    def from_dict(http_request_response_dict):
        if not http_request_response_dict:
            return None
        http_request_response_ = HTTPRequestResponse()
        http_request_response_.http_client_request = HTTPClientRequest.from_dict(http_request_response_dict.get('http_request_response'))
        http_request_response_.http_server_response = HTTPServerResponse.from_dict(http_request_response_dict.get('http_server_response'))
        return http_request_response_

    @staticmethod
    def from_obj(http_request_response_obj):
        if not http_request_response_obj:
            return None
        http_request_response_ = HTTPRequestResponse()
        http_request_response_.http_client_request = HTTPClientRequest.from_obj(http_request_response_obj.get_HTTP_Client_Request())
        http_request_response_.http_server_response = HTTPServerResponse.from_obj(http_request_response_obj.get_HTTP_Server_Response())
        return http_request_response_

class HTTPClientRequest(cybox.Entity):
    def __init__(self):
        super(HTTPClientRequest, self).__init__()
        self.http_request_line = None
        self.http_request_header = None
        self.http_message_body = None

    def to_obj(self):
        http_client_request_obj = http_session_binding.HTTPClientRequestType()
        if self.http_request_line is not None: http_client_request_obj.set_HTTP_Request_Line(self.http_request_line.to_obj())
        if self.http_request_header is not None: http_client_request_obj.set_HTTP_Request_Header(self.http_request_header.to_obj())
        if self.http_message_body is not None: http_client_request_obj.set_HTTP_Message_Body(self.http_message_body.to_obj())
        return http_client_request_obj

    def to_dict(self):
        http_client_request_dict = {}
        if self.http_request_line is not None: http_client_request_dict['http_request_line'] = self.http_request_line.to_dict()
        if self.http_request_header is not None: http_client_request_dict['http_request_header'] = self.http_request_header.to_dict()
        if self.http_message_body is not None: http_client_request_dict['http_message_body'] = self.http_message_body.to_dict()
        return http_client_request_dict

    @staticmethod
    def from_dict(http_client_request_dict):
        if not http_client_request_dict:
            return None
        http_client_request_ = HTTPClientRequest()
        http_client_request_.http_request_line = HTTPRequestLine.from_dict(http_client_request_dict.get('http_request_line'))
        http_client_request_.http_request_header = HTTPRequestHeader.from_dict(http_client_request_dict.get('http_request_header'))
        http_client_request_.http_message_body = HTTPMessage.from_dict(http_client_request_dict.get('http_message_body'))
        return http_client_request_

    @staticmethod
    def from_obj(http_client_request_obj):
        if not http_client_request_obj:
            return None
        http_client_request_ = HTTPClientRequest()
        http_client_request_.http_request_line = HTTPRequestLine.from_obj(http_client_request_obj.get_HTTP_Request_Line())
        http_client_request_.http_request_header = HTTPRequestHeader.from_obj(http_client_request_obj.get_HTTP_Request_Header())
        http_client_request_.http_message_body = HTTPMessage.from_obj(http_client_request_obj.get_HTTP_Message_Body())
        return http_client_request_

class HTTPRequestLine(cybox.Entity):
    def __init__(self):
        super(HTTPRequestLine, self).__init__()
        self.http_method = None
        self.value = None
        self.version = None

    def to_obj(self):
        http_request_line_obj = http_session_binding.HTTPRequestLineType()
        if self.http_method is not None : http_request_line_obj.set_HTTP_Method(self.http_method.to_obj())
        if self.value is not None : http_request_line_obj.set_Value(self.value.to_obj())
        if self.version is not None : http_request_line_obj.set_Version(self.version.to_obj())
        return http_request_line_obj

    def to_dict(self):
        http_request_line_dict = {}
        if self.http_method is not None : http_request_line_dict['http_method'] = self.http_method.to_dict()
        if self.value is not None : http_request_line_dict['value'] = self.value.to_dict()
        if self.version is not None : http_request_line_dict['version'] = self.version.to_dict()
        return http_request_line_dict

    @staticmethod
    def from_dict(http_request_line_dict):
        if not http_request_line_dict:
            return None
        http_request_line_ = HTTPRequestLine()
        http_request_line_.http_method = String.from_dict(http_request_line_dict.get('http_method'))
        http_request_line_.value = String.from_dict(http_request_line_dict.get('value'))
        http_request_line_.version = String.from_dict(http_request_line_dict.get('version'))
        return http_request_line_

    @staticmethod
    def from_obj(http_request_line_obj):
        if not http_request_line_obj:
            return None
        http_request_line_ = HTTPRequestLine()
        http_request_line_.http_method = String.from_obj(http_request_line_obj.get_HTTP_Method())
        http_request_line_.value = String.from_obj(http_request_line_obj.get_Value())
        http_request_line_.version = String.from_obj(http_request_line_obj.get_Version())
        return http_request_line_

class HTTPRequestHeader(cybox.Entity):
    def __init__(self):
        super(HTTPRequestHeader, self).__init__()
        self.raw_header = None
        self.parsed_header = None

    def to_obj(self):
        http_request_header_obj = http_session_binding.HTTPRequestHeaderType()
        if self.raw_header is not None : http_request_header_obj.set_Raw_Header(self.raw_header.to_obj())
        if self.parsed_header is not None : http_request_header_obj.set_Parsed_Header(self.parsed_header.to_obj())
        return http_request_header_obj

    def to_dict(self):
        http_request_header_dict = {}
        if self.raw_header is not None : http_request_header_dict['raw_header'] = self.raw_header.to_dict()
        if self.parsed_header is not None : http_request_header_dict['parsed_header'] = self.parsed_header.to_dict()
        return http_request_header_dict

    @staticmethod
    def from_dict(http_request_header_dict):
        if not http_request_header_dict:
            return None
        http_request_header_ = HTTPRequestHeader()
        http_request_header_.raw_header = String.from_dict(http_request_header_dict.get('raw_header'))
        http_request_header_.parsed_header = HTTPRequestHeaderFields.from_dict(http_request_header_dict.get('parsed_header'))
        return http_request_header_

    @staticmethod
    def from_obj(http_request_header_obj):
        if not http_request_header_obj:
            return None
        http_request_header_ = HTTPRequestHeader()
        http_request_header_.raw_header = String.from_obj(http_request_header_obj.get_Raw_Header())
        http_request_header_.parsed_header = HTTPRequestHeaderFields.from_obj(http_request_header_obj.get_Parsed_Header())
        return http_request_header_

class HTTPMessage(cybox.Entity):
    def __init__(self):
        super(HTTPMessage, self).__init__()
        self.length = None
        self.message_body = None

    def to_obj(self):
        http_message_obj = http_session_binding.HTTPMessageType()
        if self.length is not None : http_message_obj.set_Length(self.length.to_obj())
        if self.message_body is not None : http_message_obj.set_Message_Body(self.message_body.to_obj())
        return http_message_obj

    def to_dict(self):
        http_message_dict = {}
        if self.length is not None : http_message_dict['length'] = self.length.to_dict()
        if self.message_body is not None : http_message_dict['message_body'] = self.message_body.to_dict()
        return http_message_dict

    @staticmethod
    def from_dict(http_message_dict):
        if not http_message_dict:
            return None
        http_message_ = HTTPMessage()
        http_message_.length = PositiveInteger.from_dict(http_message_dict.get('length'))
        http_message_.message_body = String.from_dict(http_message_dict.get('message_body'))
        return http_message_

    @staticmethod
    def from_obj(http_message_obj):
        if not http_message_obj:
            return None
        http_message_ = HTTPMessage()
        http_message_.length = PositiveInteger.from_obj(http_message_obj.get_Length())
        http_message_.message_body = String.from_obj(http_message_obj.get_Message_Body())
        return http_message_

class HTTPRequestHeaderFields(cybox.Entity):
    def __init__(self):
        super(HTTPRequestHeaderFields, self).__init__()
        self.accept = None
        self.accept_charset = None
        self.accept_language = None
        self.accept_datetime = None
        self.accept_encoding = None
        self.authorization = None
        self.cache_control = None
        self.connection = None
        self.cookie = None
        self.content_length = None
        self.content_md5 = None
        self.content_type = None
        self.date = None
        self.expect = None
        self.from_ = None
        self.host = None
        self.if_match = None
        self.if_modified_since = None
        self.if_none_match = None
        self.if_range = None
        self.if_unmodified_since = None
        self.max_forwards = None
        self.pragma = None
        self.proxy_authorization = None
        self.range = None
        self.referer = None
        self.te = None
        self.user_agent = None
        self.via = None
        self.warning = None
        self.dnt = None
        self.x_requested_with = None
        self.x_requested_for = None
        self.x_att_deviceid = None
        self.x_wap_profile = None

    def to_obj(self):
        http_request_header_fields_obj = http_session_binding.HTTPRequestHeaderFieldsType()

        if self.accept is not None : http_request_header_fields_obj.set_Accept(self.accept.to_obj())
        if self.accept_charset is not None : http_request_header_fields_obj.set_Accept_Charset(self.accept_charset.to_obj())
        if self.accept_language is not None : http_request_header_fields_obj.set_Accept_Language(self.accept_language.to_obj())
        if self.accept_datetime is not None : http_request_header_fields_obj.set_Accept_Datetime(self.accept_datetime.to_obj())
        if self.accept_encoding is not None : http_request_header_fields_obj.set_Accept_Encoding(self.accept_encoding.to_obj())
        if self.authorization is not None : http_request_header_fields_obj.set_Authorization(self.authorization.to_obj())
        if self.cache_control is not None : http_request_header_fields_obj.set_Cache_Control(self.cache_control.to_obj())
        if self.connection is not None : http_request_header_fields_obj.set_Connection(self.connection.to_obj())
        if self.cookie is not None : http_request_header_fields_obj.set_Cookie(self.cookie.to_obj())
        if self.content_length is not None : http_request_header_fields_obj.set_Content_Length(self.content_length.to_obj())
        if self.content_md5 is not None : http_request_header_fields_obj.set_Content_MD5(self.content_md5.to_obj())
        if self.content_type is not None : http_request_header_fields_obj.set_Content_Type(self.content_type.to_obj())
        if self.date is not None : http_request_header_fields_obj.set_Date(self.date.to_obj())
        if self.expect is not None : http_request_header_fields_obj.set_Expect(self.expect.to_obj())
        if self.from_ is not None : http_request_header_fields_obj.set_From(self.from_.to_obj())
        if self.host is not None : http_request_header_fields_obj.set_Host(self.host.to_obj())
        if self.if_match is not None : http_request_header_fields_obj.set_If_Match(self.if_match.to_obj())
        if self.if_modified_since is not None : http_request_header_fields_obj.set_If_Modified_Since(self.if_modified_since.to_obj())
        if self.if_none_match is not None : http_request_header_fields_obj.set_If_None_Match(self.if_none_match.to_obj())
        if self.if_range is not None : http_request_header_fields_obj.set_If_Range(self.if_range.to_obj())
        if self.if_unmodified_since is not None : http_request_header_fields_obj.set_If_Unmodified_Since(self.if_unmodified_since.to_obj())
        if self.max_forwards is not None : http_request_header_fields_obj.set_Max_Forwards(self.max_forwards.to_obj())
        if self.pragma is not None : http_request_header_fields_obj.set_Pragma(self.pragma.to_obj())
        if self.proxy_authorization is not None : http_request_header_fields_obj.set_Proxy_Authorization(self.proxy_authorization.to_obj())
        if self.range is not None : http_request_header_fields_obj.set_Range(self.range.to_obj())
        if self.referer is not None : http_request_header_fields_obj.set_Referer(self.referer.to_obj())
        if self.te is not None : http_request_header_fields_obj.set_TE(self.te.to_obj())
        if self.user_agent is not None : http_request_header_fields_obj.set_User_Agent(self.user_agent.to_obj())
        if self.via is not None : http_request_header_fields_obj.set_Via(self.via.to_obj())
        if self.warning is not None : http_request_header_fields_obj.set_Warning(self.warning.to_obj())
        if self.dnt is not None : http_request_header_fields_obj.set_DNT(self.dnt.to_obj())
        if self.x_requested_with is not None : http_request_header_fields_obj.set_X_Requested_With(self.x_requested_with.to_obj())
        if self.x_requested_for is not None : http_request_header_fields_obj.set_X_Requested_For(self.x_requested_for.to_obj())
        if self.x_att_deviceid is not None : http_request_header_fields_obj.set_X_ATT_DeviceId(self.x_att_deviceid.to_obj())
        if self.x_wap_profile is not None : http_request_header_fields_obj.set_X_Wap_Profile(self.x_wap_profile.to_obj())

        return http_request_header_fields_obj

    def to_dict(self):
        http_request_header_fields_dict = {}

        if self.accept is not None : http_request_header_fields_dict['accept'] = self.accept.to_dict()
        if self.accept_charset is not None : http_request_header_fields_dict['accept_charset'] = self.accept_charset.to_dict()
        if self.accept_language is not None : http_request_header_fields_dict['accept_language'] = self.accept_language.to_dict()
        if self.accept_datetime is not None : http_request_header_fields_dict['accept_datetime'] = self.accept_datetime.to_dict()
        if self.accept_encoding is not None : http_request_header_fields_dict['accept_encoding'] = self.accept_encoding.to_dict()
        if self.authorization is not None : http_request_header_fields_dict['authorization'] = self.authorization.to_dict()
        if self.cache_control is not None : http_request_header_fields_dict['cache_control'] = self.cache_control.to_dict()
        if self.connection is not None : http_request_header_fields_dict['connection'] = self.connection.to_dict()
        if self.cookie is not None : http_request_header_fields_dict['cookie'] = self.cookie.to_dict()
        if self.content_length is not None : http_request_header_fields_dict['content_length'] = self.content_length.to_dict()
        if self.content_md5 is not None : http_request_header_fields_dict['content_md5'] = self.content_md5.to_dict()
        if self.content_type is not None : http_request_header_fields_dict['content_type'] = self.content_type.to_dict()
        if self.date is not None : http_request_header_fields_dict['date'] = self.date.to_dict()
        if self.expect is not None : http_request_header_fields_dict['expect'] = self.expect.to_dict()
        if self.from_ is not None : http_request_header_fields_dict['from'] = self.from_.to_dict()
        if self.host is not None : http_request_header_fields_dict['host'] = self.host.to_dict()
        if self.if_match is not None : http_request_header_fields_dict['if_match'] = self.if_match.to_dict()
        if self.if_modified_since is not None : http_request_header_fields_dict['if_modified_since'] = self.if_modified_since.to_dict()
        if self.if_none_match is not None : http_request_header_fields_dict['if_none_match'] = self.if_none_match.to_dict()
        if self.if_range is not None : http_request_header_fields_dict['if_range'] = self.if_range.to_dict()
        if self.if_unmodified_since is not None : http_request_header_fields_dict['if_unmodified_since'] = self.if_unmodified_since.to_dict()
        if self.max_forwards is not None : http_request_header_fields_dict['max_forwards'] = self.max_forwards.to_dict()
        if self.pragma is not None : http_request_header_fields_dict['pragma'] = self.pragma.to_dict()
        if self.proxy_authorization is not None : http_request_header_fields_dict['proxy_authorization'] = self.proxy_authorization.to_dict()
        if self.range is not None : http_request_header_fields_dict['range'] = self.range.to_dict()
        if self.referer is not None : http_request_header_fields_dict['referer'] = self.referer.to_dict()
        if self.te is not None : http_request_header_fields_dict['te'] = self.te.to_dict()
        if self.user_agent is not None : http_request_header_fields_dict['user_agent'] = self.user_agent.to_dict()
        if self.via is not None : http_request_header_fields_dict['via'] = self.via.to_dict()
        if self.warning is not None : http_request_header_fields_dict['warning'] = self.warning.to_dict()
        if self.dnt is not None : http_request_header_fields_dict['dnt'] = self.dnt.to_dict()
        if self.x_requested_with is not None : http_request_header_fields_dict['x_requested_with'] = self.x_requested_with.to_dict()
        if self.x_requested_for is not None : http_request_header_fields_dict['x_requested_for'] = self.x_requested_for.to_dict()
        if self.x_att_deviceid is not None : http_request_header_fields_dict['x_att_deviceid'] = self.x_att_deviceid.to_dict()
        if self.x_wap_profile is not None : http_request_header_fields_dict['x_wap_profile'] = self.x_wap_profile.to_dict()

        return http_request_header_fields_dict

    @staticmethod
    def from_dict(http_request_header_fields_dict):
        if not http_request_header_fields_dict:
            return None
        http_request_header_fields_ = HTTPRequestHeaderFields()
        http_request_header_fields_.accept = String.from_dict(http_request_header_fields_dict.get('accept'))
        http_request_header_fields_.accept_charset = String.from_dict(http_request_header_fields_dict.get('accept_charset'))
        http_request_header_fields_.accept_language = String.from_dict(http_request_header_fields_dict.get('accept_language'))
        http_request_header_fields_.accept_datetime = String.from_dict(http_request_header_fields_dict.get('accept_datetime'))
        http_request_header_fields_.accept_encoding = String.from_dict(http_request_header_fields_dict.get('accept_encoding'))
        http_request_header_fields_.authorization = String.from_dict(http_request_header_fields_dict.get('authorization'))
        http_request_header_fields_.cache_control = String.from_dict(http_request_header_fields_dict.get('cache_control'))
        http_request_header_fields_.connection = String.from_dict(http_request_header_fields_dict.get('connection'))
        http_request_header_fields_.cookie = String.from_dict(http_request_header_fields_dict.get('cookie'))
        http_request_header_fields_.content_length = Integer.from_dict(http_request_header_fields_dict.get('content_length'))
        http_request_header_fields_.content_md5 = String.from_dict(http_request_header_fields_dict.get('content_md5'))
        http_request_header_fields_.content_type = String.from_dict(http_request_header_fields_dict.get('content_type'))
        http_request_header_fields_.date = DateTime.from_dict(http_request_header_fields_dict.get('date'))
        http_request_header_fields_.expect = String.from_dict(http_request_header_fields_dict.get('expect'))
        http_request_header_fields_.from_ = Address.from_dict(http_request_header_fields_dict.get('from'))
        http_request_header_fields_.host = HostField.from_dict(http_request_header_fields_dict.get('host'))
        http_request_header_fields_.if_match = String.from_dict(http_request_header_fields_dict.get('if_match'))
        http_request_header_fields_.if_modified_since = DateTime.from_dict(http_request_header_fields_dict.get('if_modified_since'))
        http_request_header_fields_.if_none_match = String.from_dict(http_request_header_fields_dict.get('if_none_match'))
        http_request_header_fields_.if_range = String.from_dict(http_request_header_fields_dict.get('if_range'))
        http_request_header_fields_.if_unmodified_since = DateTime.from_dict(http_request_header_fields_dict.get('if_unmodified_since'))
        http_request_header_fields_.max_forwards = Integer.from_dict(http_request_header_fields_dict.get('max_forwards'))
        http_request_header_fields_.pragma = String.from_dict(http_request_header_fields_dict.get('pragma'))
        http_request_header_fields_.proxy_authorization = String.from_dict(http_request_header_fields_dict.get('proxy_authorization'))
        http_request_header_fields_.range = String.from_dict(http_request_header_fields_dict.get('range'))
        http_request_header_fields_.referer = URI.from_dict(http_request_header_fields_dict.get('referer'))
        http_request_header_fields_.te = String.from_dict(http_request_header_fields_dict.get('te'))
        http_request_header_fields_.user_agent = String.from_dict(http_request_header_fields_dict.get('user_agent'))
        http_request_header_fields_.via = String.from_dict(http_request_header_fields_dict.get('via'))
        http_request_header_fields_.warning = String.from_dict(http_request_header_fields_dict.get('warning'))
        http_request_header_fields_.dnt = URI.from_dict(http_request_header_fields_dict.get('dnt'))
        http_request_header_fields_.x_requested_with = String.from_dict(http_request_header_fields_dict.get('x_requested_with'))
        http_request_header_fields_.x_requested_for = String.from_dict(http_request_header_fields_dict.get('x_requested_for'))
        http_request_header_fields_.x_att_deviceid = String.from_dict(http_request_header_fields_dict.get('x_att_deviceid'))
        http_request_header_fields_.x_wap_profile = String.from_dict(http_request_header_fields_dict.get('x_wap_profile'))
        return http_request_header_fields_

    @staticmethod
    def from_obj(http_request_header_fields_obj):
        if not http_request_header_fields_obj:
            return None
        http_request_header_fields_ = HTTPRequestHeaderFields()
        http_request_header_fields_.accept = String.from_obj(http_request_header_fields_obj.get_Accept())
        http_request_header_fields_.accept_charset = String.from_obj(http_request_header_fields_obj.get_Accept_Charset())
        http_request_header_fields_.accept_language = String.from_obj(http_request_header_fields_obj.get_Accept_Language())
        http_request_header_fields_.accept_datetime = String.from_obj(http_request_header_fields_obj.get_Accept_Datetime())
        http_request_header_fields_.accept_encoding = String.from_obj(http_request_header_fields_obj.get_Accept_Encoding())
        http_request_header_fields_.authorization = String.from_obj(http_request_header_fields_obj.get_Authorization())
        http_request_header_fields_.cache_control = String.from_obj(http_request_header_fields_obj.get_Cache_Control())
        http_request_header_fields_.connection = String.from_obj(http_request_header_fields_obj.get_Connection())
        http_request_header_fields_.cookie = String.from_obj(http_request_header_fields_obj.get_Cookie())
        http_request_header_fields_.content_length = Integer.from_obj(http_request_header_fields_obj.get_Content_Length())
        http_request_header_fields_.content_md5 = String.from_obj(http_request_header_fields_obj.get_Content_MD5())
        http_request_header_fields_.content_type = String.from_obj(http_request_header_fields_obj.get_Content_Type())
        http_request_header_fields_.date = DateTime.from_obj(http_request_header_fields_obj.get_Date())
        http_request_header_fields_.expect = String.from_obj(http_request_header_fields_obj.get_Expect())
        http_request_header_fields_.from_ = Address.from_obj(http_request_header_fields_obj.get_From())
        http_request_header_fields_.host = HostField.from_obj(http_request_header_fields_obj.get_Host())
        http_request_header_fields_.if_match = String.from_obj(http_request_header_fields_obj.get_If_Match())
        http_request_header_fields_.if_modified_since = DateTime.from_obj(http_request_header_fields_obj.get_If_Modified_Since())
        http_request_header_fields_.if_none_match = String.from_obj(http_request_header_fields_obj.get_If_None_Match())
        http_request_header_fields_.if_range = String.from_obj(http_request_header_fields_obj.get_If_Range())
        http_request_header_fields_.if_unmodified_since = DateTime.from_obj(http_request_header_fields_obj.get_If_Unmodified_Since())
        http_request_header_fields_.max_forwards = Integer.from_obj(http_request_header_fields_obj.get_Max_Forwards())
        http_request_header_fields_.pragma = String.from_obj(http_request_header_fields_obj.get_Pragma())
        http_request_header_fields_.proxy_authorization = String.from_obj(http_request_header_fields_obj.get_Proxy_Authorization())
        http_request_header_fields_.range = String.from_obj(http_request_header_fields_obj.get_Range())
        http_request_header_fields_.referer = URI.from_obj(http_request_header_fields_obj.get_Referer())
        http_request_header_fields_.te = String.from_obj(http_request_header_fields_obj.get_TE())
        http_request_header_fields_.user_agent = String.from_obj(http_request_header_fields_obj.get_User_Agent())
        http_request_header_fields_.via = String.from_obj(http_request_header_fields_obj.get_Via())
        http_request_header_fields_.warning = String.from_obj(http_request_header_fields_obj.get_Warning())
        http_request_header_fields_.dnt = URI.from_obj(http_request_header_fields_obj.get_DNT())
        http_request_header_fields_.x_requested_with = String.from_obj(http_request_header_fields_obj.get_X_Requested_With())
        http_request_header_fields_.x_requested_for = String.from_obj(http_request_header_fields_obj.get_X_Requested_For())
        http_request_header_fields_.x_att_deviceid = String.from_obj(http_request_header_fields_obj.get_X_ATT_DeviceId())
        http_request_header_fields_.x_wap_profile = String.from_obj(http_request_header_fields_obj.get_X_Wap_Profile())
        return http_request_header_fields_

class HostField(cybox.Entity):
    def __init__(self):
        super(HostField, self).__init__()
        self.domain_name = None
        self.port = None

    def to_obj(self):
        host_field_obj = http_session_binding.HostFieldType()
        if self.domain_name is not None : host_field_obj.set_Domain_Name(self.domain_name.to_obj())
        if self.port is not None : host_field_obj.set_Port(self.port.to_obj())
        return host_field_obj

    def to_dict(self):
        host_field_dict = {}
        if self.domain_name is not None : host_field_dict['domain_name'] = self.domain_name.to_dict()
        if self.port is not None : host_field_dict['port'] = self.port.to_dict()
        return host_field_dict

    @staticmethod
    def from_dict(host_field_dict):
        if not host_field_dict:
            return None
        host_field_ = HostField()
        host_field_.domain_name = URI.from_dict(host_field_dict.get('domain_name'))
        host_field_.port = Port.from_dict(host_field_dict.get('port'))
        return host_field_

    @staticmethod
    def from_obj(host_field_obj):
        if not host_field_obj:
            return None
        host_field_ = HostField()
        host_field_.domain_name = URI.from_obj(host_field_obj.get_Domain_Name())
        host_field_.port = Port.from_obj(host_field_obj.get_Port())
        return host_field_

class HTTPServerResponse(cybox.Entity):
    def __init__(self):
       super(HTTPClientRequest, self).__init__()
       self.http_status_line = None
       self.http_response_header = None
       self.http_message_body = None

    def to_obj(self):
        http_server_response_obj = http_session_binding.HTTPServerResponseType()
        if self.http_status_line is not None: http_server_response_obj.set_HTTP_Status_Line(self.http_status_line.to_obj())
        if self.http_response_header is not None: http_server_response_obj.set_HTTP_Response_Header(self.http_response_header.to_obj())
        if self.http_message_body is not None: http_server_response_obj.set_HTTP_Message_Body(self.http_message_body.to_obj())
        return http_server_response_obj

    def to_dict(self):
        http_server_response_dict = {}
        if self.http_status_line is not None: http_server_response_dict['http_status_line'] = self.http_status_line.to_dict()
        if self.http_response_header is not None: http_server_response_dict['http_response_header'] = self.http_response_header.to_dict()
        if self.http_message_body is not None: http_server_response_dict['http_message_body'] = self.http_message_body.to_dict()
        return http_server_response_dict

    @staticmethod
    def from_dict(http_server_response_dict):
        if not http_server_response_dict:
            return None
        http_server_response_ = HTTPServerResponse()
        http_server_response_.http_status_line = HTTPStatusLine.from_dict(http_server_response_dict.get('http_status_line'))
        http_server_response_.http_response_header = HTTPResponseHeader.from_dict(http_server_response_dict.get('http_response_header'))
        http_server_response_.http_message_body = HTTPMessage.from_dict(http_server_response_dict.get('http_message_body'))
        return http_server_response_

    @staticmethod
    def from_obj(http_server_response_obj):
        if not http_server_response_obj:
            return None
        http_server_response_ = HTTPServerResponse()
        http_server_response_.http_status_line = HTTPStatusLine.from_obj(http_server_response_obj.get_HTTP_Status_Line())
        http_server_response_.http_request_header = HTTPResponseHeader.from_obj(http_server_response_obj.get_HTTP_Response_Header())
        http_server_response_.http_message_body = HTTPMessage.from_obj(http_server_response_obj.get_HTTP_Message_Body())
        return http_server_response_

class HTTPStatusLine(cybox.Entity):
    def __init__(self):
        super(HTTPStatusLine, self).__init__()
        self.version = None
        self.status_code = None
        self.reason_phrase = None

    def to_obj(self):
        http_status_line_obj = http_session_binding.HTTPStatusLineType()
        if self.version is not None : http_status_line_obj.set_Version(self.version.to_obj())
        if self.status_code is not None : http_status_line_obj.set_Status_Code(self.status_code.to_obj())
        if self.reason_phrase is not None : http_status_line_obj.set_Reason_Phrase(self.reason_phrase.to_obj())
        return http_status_line_obj

    def to_dict(self):
        http_status_line_dict = {}
        if self.version is not None : http_status_line_dict['version'] = self.version.to_dict()
        if self.status_code is not None : http_status_line_dict['status_code'] = self.status_code.to_dict()
        if self.reason_phrase is not None : http_status_line_dict['reason_phrase'] = self.reason_phrase.to_dict()
        return http_status_line_dict

    @staticmethod
    def from_dict(http_status_line_dict):
        if not http_status_line_dict:
            return None
        http_status_line_ = HTTPStatusLine()
        http_status_line_.version = String.from_dict(http_status_line_dict.get('version'))
        http_status_line_.status_code = PositiveInteger.from_dict(http_status_line_dict.get('status_code'))
        http_status_line_.reason_phrase = String.from_dict(http_status_line_dict.get('reason_phrase'))
        return http_status_line_

    @staticmethod
    def from_obj(http_status_line_obj):
        if not http_status_line_obj:
            return None
        http_status_line_ = HTTPStatusLine()
        http_status_line_.version = String.from_obj(http_status_line_obj.get_Version())
        http_status_line_.status_code = PositiveInteger.from_obj(http_status_line_obj.get_Status_Code())
        http_status_line_.reason_phrase = String.from_obj(http_status_line_obj.get_Reason_Phrase())
        return http_status_line_

class HTTPResponseHeader(cybox.Entity):
    def __init__(self):
        super(HTTPResponseHeader, self).__init__()
        self.raw_header = None
        self.parsed_header = None

    def to_obj(self):
        http_response_header_obj = http_session_binding.HTTPResponseHeaderType()
        if self.raw_header is not None : http_response_header_obj.set_Raw_Header(self.raw_header.to_obj())
        if self.parsed_header is not None : http_response_header_obj.set_Parsed_Header(self.parsed_header.to_obj())
        return http_response_header_obj

    def to_dict(self):
        http_response_header_dict = {}
        if self.raw_header is not None : http_response_header_dict['raw_header'] = self.raw_header.to_dict()
        if self.parsed_header is not None : http_response_header_dict['parsed_header'] = self.parsed_header.to_dict()
        return http_response_header_dict

    @staticmethod
    def from_dict(http_response_header_dict):
        if not http_response_header_dict:
            return None
        http_response_header_ = HTTPResponseHeader()
        http_response_header_.raw_header = String.from_dict(http_response_header_dict.get('raw_header'))
        http_response_header_.parsed_header = HTTPResponseHeaderFields.from_dict(http_response_header_dict.get('parsed_header'))
        return http_response_header_

    @staticmethod
    def from_obj(http_response_header_obj):
        if not http_response_header_obj:
            return None
        http_response_header_ = HTTPResponseHeader()
        http_response_header_.raw_header = String.from_obj(http_response_header_obj.get_Raw_Header())
        http_response_header_.parsed_header = HTTPResponseHeaderFields.from_obj(http_response_header_obj.get_Parsed_Header())
        return http_response_header_

class HTTPResponseHeaderFields(cybox.Entity):
    def __init__(self):
        super(HTTPResponseHeaderFields, self).__init__()
        self.access_control_allow_origin = None
        self.accept_ranges = None
        self.age = None
        self.cache_control = None
        self.connection = None
        self.content_encoding = None
        self.content_language = None
        self.content_length = None
        self.content_location = None
        self.content_md5 = None
        self.content_disposition = None
        self.content_range = None
        self.content_type = None
        self.date = None
        self.etag = None
        self.expires = None
        self.last_modified = None
        self.link = None
        self.location = None
        self.p3p = None
        self.pragma = None
        self.proxy_authenticate = None
        self.refresh = None
        self.retry_after = None
        self.server = None
        self.set_cookie = None
        self.strict_transport_security = None
        self.trailer = None
        self.transfer_encoding = None
        self.vary = None
        self.via = None
        self.warning = None
        self.www_authenticate = None
        self.x_frame_options = None
        self.x_xss_protection = None
        self.x_content_type_options = None
        self.x_forwarded_proto = None
        self.x_powered_by = None
        self.x_ua_compatible = None

    def to_obj(self):
        http_response_header_fields_obj = http_session_binding.HTTPResponseHeaderFieldsType()

        if self.access_control_allow_origin is not None : http_response_header_fields_obj.set_Access_Control_Allow_Origin(self.access_control_allow_origin.to_obj())
        if self.accept_ranges is not None : http_response_header_fields_obj.set_Accept_Ranges(self.accept_ranges.to_obj())
        if self.age is not None : http_response_header_fields_obj.set_Age(self.age.to_obj())
        if self.cache_control is not None : http_response_header_fields_obj.set_Cache_Control(self.cache_control.to_obj())
        if self.connection is not None : http_response_header_fields_obj.set_Connection(self.connection.to_obj())
        if self.content_encoding is not None : http_response_header_fields_obj.set_Content_Encoding(self.content_encoding.to_obj())
        if self.content_language is not None : http_response_header_fields_obj.set_Content_Language(self.content_language.to_obj())
        if self.content_length is not None : http_response_header_fields_obj.set_Content_Length(self.content_length.to_obj())
        if self.content_location is not None : http_response_header_fields_obj.set_Content_Location(self.content_location.to_obj())
        if self.content_md5 is not None : http_response_header_fields_obj.set_Content_MD5(self.content_md5.to_obj())
        if self.content_disposition is not None : http_response_header_fields_obj.set_Content_Disposition(self.content_disposition.to_obj())
        if self.content_range is not None : http_response_header_fields_obj.set_Content_Range(self.content_range.to_obj())
        if self.content_type is not None : http_response_header_fields_obj.set_Content_Type(self.content_type.to_obj())
        if self.date is not None : http_response_header_fields_obj.set_Date(self.date.to_obj())
        if self.etag is not None : http_response_header_fields_obj.set_Etag(self.etag.to_obj())
        if self.expires is not None : http_response_header_fields_obj.set_Expires(self.expires.to_obj())
        if self.last_modified is not None : http_response_header_fields_obj.set_Last_Modified(self.last_modified.to_obj())
        if self.link is not None : http_response_header_fields_obj.set_Link(self.link.to_obj())
        if self.location is not None : http_response_header_fields_obj.set_Link(self.location.to_obj())
        if self.p3p is not None : http_response_header_fields_obj.set_P3P(self.p3p.to_obj())
        if self.pragma is not None : http_response_header_fields_obj.set_Pragma(self.pragma.to_obj())
        if self.proxy_authenticate is not None : http_response_header_fields_obj.set_Proxy_Authenticate(self.proxy_authenticate.to_obj())
        if self.refresh is not None : http_response_header_fields_obj.set_Refresh(self.refresh.to_obj())
        if self.retry_after is not None : http_response_header_fields_obj.set_Retry_After(self.retry_after.to_obj())
        if self.server is not None : http_response_header_fields_obj.set_Server(self.server.to_obj())
        if self.set_cookie is not None : http_response_header_fields_obj.set_Set_Cookie(self.set_cookie.to_obj())
        if self.strict_transport_security is not None : http_response_header_fields_obj.set_Strict_Transport_Security(self.strict_transport_security.to_obj())
        if self.trailer is not None : http_response_header_fields_obj.set_Trailer(self.trailer.to_obj())
        if self.transfer_encoding is not None : http_response_header_fields_obj.set_Transfer_Encoding(self.transfer_encoding.to_obj())
        if self.vary is not None : http_response_header_fields_obj.set_Vary(self.vary.to_obj())
        if self.via is not None : http_response_header_fields_obj.set_Via(self.via.to_obj())
        if self.warning is not None : http_response_header_fields_obj.set_Warning(self.warning.to_obj())
        if self.www_authenticate is not None : http_response_header_fields_obj.set_WWW_Authenticate(self.www_authenticate.to_obj())
        if self.x_frame_options is not None : http_response_header_fields_obj.set_X_Frame_Options(self.x_frame_options.to_obj())
        if self.x_xss_protection is not None : http_response_header_fields_obj.set_X_XSS_Protection(self.x_xss_protection.to_obj())
        if self.x_content_type_options is not None : http_response_header_fields_obj.set_Content_Type_Options(self.x_content_type_options.to_obj())
        if self.x_forwarded_proto is not None : http_response_header_fields_obj.set_X_Forwarded_Proto(self.x_forwarded_proto.to_obj())
        if self.x_powered_by is not None : http_response_header_fields_obj.set_X_Powered_By(self.x_powered_by.to_obj())
        if self.x_ua_compatible is not None : http_response_header_fields_obj.set_X_UA_Compatible(self.x_ua_compatible.to_obj())

        return http_response_header_fields_obj

    def to_dict(self):
        http_response_header_fields_dict = {}

        if self.access_control_allow_origin is not None : http_response_header_fields_dict['access_control_allow_origin'] = self.access_control_allow_origin.to_dict()
        if self.accept_ranges is not None : http_response_header_fields_dict['accept_ranges'] = self.accept_ranges.to_dict()
        if self.age is not None : http_response_header_fields_dict['age'] = self.age.to_dict()
        if self.cache_control is not None : http_response_header_fields_dict['cache_control'] = self.cache_control.to_dict()
        if self.connection is not None : http_response_header_fields_dict['connection'] = self.connection.to_dict()
        if self.content_encoding is not None : http_response_header_fields_dict['content_encoding'] = self.content_encoding.to_dict()
        if self.content_language is not None : http_response_header_fields_dict['content_language'] = self.content_language.to_dict()
        if self.content_length is not None : http_response_header_fields_dict['content_length'] = self.content_length.to_dict()
        if self.content_location is not None : http_response_header_fields_dict['content_location'] = self.content_location.to_dict()
        if self.content_md5 is not None : http_response_header_fields_dict['content_md5'] = self.content_md5.to_dict()
        if self.content_disposition is not None : http_response_header_fields_dict['content_disposition'] = self.content_disposition.to_dict()
        if self.content_range is not None : http_response_header_fields_dict['content_range'] = self.content_range.to_dict()
        if self.content_type is not None : http_response_header_fields_dict['content_type'] = self.content_type.to_dict()
        if self.date is not None : http_response_header_fields_dict['date'] = self.date.to_dict()
        if self.etag is not None : http_response_header_fields_dict['etag'] = self.etag.to_dict()
        if self.expires is not None : http_response_header_fields_dict['expires'] = self.expires.to_dict()
        if self.last_modified is not None : http_response_header_fields_dict['last_modified'] = self.last_modified.to_dict()
        if self.link is not None : http_response_header_fields_dict['link'] = self.link.to_dict()
        if self.location is not None : http_response_header_fields_dict['location'] = self.location.to_dict()
        if self.p3p is not None : http_response_header_fields_dict['p3p'] = self.p3p.to_dict()
        if self.pragma is not None : http_response_header_fields_dict['pragma'] = self.pragma.to_dict()
        if self.proxy_authenticate is not None : http_response_header_fields_dict['proxy_authenticate'] = self.proxy_authenticate.to_dict()
        if self.refresh is not None : http_response_header_fields_dict['refresh'] = self.refresh.to_dict()
        if self.retry_after is not None : http_response_header_fields_dict['retry_after'] = self.retry_after.to_dict()
        if self.server is not None : http_response_header_fields_dict['server'] = self.server.to_dict()
        if self.set_cookie is not None : http_response_header_fields_dict['set_cookie'] = self.set_cookie.to_dict()
        if self.strict_transport_security is not None : http_response_header_fields_dict['strict_transport_security'] = self.strict_transport_security.to_dict()
        if self.trailer is not None : http_response_header_fields_dict['trailer'] = self.trailer.to_dict()
        if self.transfer_encoding is not None : http_response_header_fields_dict['transfer_encoding'] = self.transfer_encoding.to_dict()
        if self.vary is not None : http_response_header_fields_dict['vary'] = self.vary.to_dict()
        if self.via is not None : http_response_header_fields_dict['via'] = self.via.to_dict()
        if self.warning is not None : http_response_header_fields_dict['warning'] = self.warning.to_dict()
        if self.www_authenticate is not None : http_response_header_fields_dict['www_authenticate'] = self.www_authenticate.to_dict()
        if self.x_frame_options is not None : http_response_header_fields_dict['x_frame_options'] = self.x_frame_options.to_dict()
        if self.x_xss_protection is not None : http_response_header_fields_dict['x_xss_protection'] = self.x_xss_protection.to_dict()
        if self.x_content_type_options is not None : http_response_header_fields_dict['x_content_type_options'] = self.x_content_type_options.to_dict()
        if self.x_forwarded_proto is not None : http_response_header_fields_dict['x_forwarded_proto'] = self.x_forwarded_proto.to_dict()
        if self.x_powered_by is not None : http_response_header_fields_dict['x_powered_by'] = self.x_powered_by.to_dict()
        if self.x_ua_compatible is not None : http_response_header_fields_dict['x_ua_compatible'] = self.x_ua_compatible.to_dict()

        return http_response_header_fields_dict

    @staticmethod
    def from_dict(http_response_header_fields_dict):
        if not http_response_header_fields_dict:
            return None
        http_response_header_fields_ = HTTPResponseHeaderFields()
        http_response_header_fields_.access_control_allow_origin = String.from_dict(http_response_header_fields_dict.get('access_control_allow_origin'))
        http_response_header_fields_.accept_ranges = String.from_dict(http_response_header_fields_dict.get('accept_ranges'))
        http_response_header_fields_.age = Integer.from_dict(http_response_header_fields_dict.get('age'))
        http_response_header_fields_.cache_control = String.from_dict(http_response_header_fields_dict.get('cache_control'))
        http_response_header_fields_.connection = String.from_dict(http_response_header_fields_dict.get('connection'))
        http_response_header_fields_.content_encoding = String.from_dict(http_response_header_fields_dict.get('content_encoding'))
        http_response_header_fields_.content_language = String.from_dict(http_response_header_fields_dict.get('content_language'))
        http_response_header_fields_.content_length = Integer.from_dict(http_response_header_fields_dict.get('content_length'))
        http_response_header_fields_.content_location = String.from_dict(http_response_header_fields_dict.get('content_location'))
        http_response_header_fields_.content_md5 = String.from_dict(http_response_header_fields_dict.get('content_md5'))
        http_response_header_fields_.content_disposition = String.from_dict(http_response_header_fields_dict.get('content_disposition'))
        http_response_header_fields_.content_range = String.from_dict(http_response_header_fields_dict.get('content_range'))
        http_response_header_fields_.content_type = String.from_dict(http_response_header_fields_dict.get('content_type'))
        http_response_header_fields_.date = DateTime.from_dict(http_response_header_fields_dict.get('date'))
        http_response_header_fields_.etag = String.from_dict(http_response_header_fields_dict.get('etag'))
        http_response_header_fields_.expires = DateTime.from_dict(http_response_header_fields_dict.get('expires'))
        http_response_header_fields_.last_modified = DateTime.from_dict(http_response_header_fields_dict.get('last_modified'))
        http_response_header_fields_.link = String.from_dict(http_response_header_fields_dict.get('link'))
        http_response_header_fields_.location = URI.from_dict(http_response_header_fields_dict.get('location'))
        http_response_header_fields_.p3p = String.from_dict(http_response_header_fields_dict.get('p3p'))
        http_response_header_fields_.pragma = String.from_dict(http_response_header_fields_dict.get('pragma'))
        http_response_header_fields_.proxy_authenticate = String.from_dict(http_response_header_fields_dict.get('proxy_authenticate'))
        http_response_header_fields_.refresh = Integer.from_dict(http_response_header_fields_dict.get('refresh'))
        http_response_header_fields_.retry_after = Integer.from_dict(http_response_header_fields_dict.get('retry_after'))
        http_response_header_fields_.server = String.from_dict(http_response_header_fields_dict.get('server'))
        http_response_header_fields_.set_cookie = String.from_dict(http_response_header_fields_dict.get('set_cookie'))
        http_response_header_fields_.strict_transport_security = String.from_dict(http_response_header_fields_dict.get('strict_transport_security'))
        http_response_header_fields_.trailer = String.from_dict(http_response_header_fields_dict.get('trailer'))
        http_response_header_fields_.transfer_encoding = String.from_dict(http_response_header_fields_dict.get('transfer_encoding'))
        http_response_header_fields_.vary = URI.from_dict(http_response_header_fields_dict.get('vary'))
        http_response_header_fields_.via = String.from_dict(http_response_header_fields_dict.get('via'))
        http_response_header_fields_.warning = String.from_dict(http_response_header_fields_dict.get('warning'))
        http_response_header_fields_.www_authenticate = String.from_dict(http_response_header_fields_dict.get('www_authenticate'))
        http_response_header_fields_.x_frame_options = String.from_dict(http_response_header_fields_dict.get('x_frame_options'))
        http_response_header_fields_.x_xss_protection = String.from_dict(http_response_header_fields_dict.get('x_xss_protection'))
        http_response_header_fields_.x_content_type_options = String.from_dict(http_response_header_fields_dict.get('x_content_type_options'))
        http_response_header_fields_.x_forwarded_proto = String.from_dict(http_response_header_fields_dict.get('x_forwarded_proto'))
        http_response_header_fields_.x_powered_by = String.from_dict(http_response_header_fields_dict.get('x_powered_by'))
        http_response_header_fields_.x_ua_compatible = String.from_dict(http_response_header_fields_dict.get('x_ua_compatible'))
        return http_response_header_fields_

    @staticmethod
    def from_obj(http_response_header_fields_obj):
        if not http_response_header_fields_obj:
            return None
        http_response_header_fields_ = HTTPResponseHeaderFields()
        http_response_header_fields_.access_control_allow_origin = String.from_obj(http_response_header_fields_obj.get_Access_Control_Allow_Origin())
        http_response_header_fields_.accept_ranges = String.from_obj(http_response_header_fields_obj.get_Accept_Ranges())
        http_response_header_fields_.age = Integer.from_obj(http_response_header_fields_obj.get_Age())
        http_response_header_fields_.cache_control = String.from_obj(http_response_header_fields_obj.get_Cache_Control())
        http_response_header_fields_.connection = String.from_obj(http_response_header_fields_obj.get_Connection())
        http_response_header_fields_.content_encoding = String.from_obj(http_response_header_fields_obj.get_Content_Encoding())
        http_response_header_fields_.content_language = String.from_obj(http_response_header_fields_obj.get_Content_Language())
        http_response_header_fields_.content_length = Integer.from_obj(http_response_header_fields_obj.get_Content_Length())
        http_response_header_fields_.content_location = String.from_obj(http_response_header_fields_obj.get_Content_Location())
        http_response_header_fields_.content_md5 = String.from_obj(http_response_header_fields_obj.get_Content_MD5())
        http_response_header_fields_.content_disposition = String.from_obj(http_response_header_fields_obj.get_Content_Disposition())
        http_response_header_fields_.content_range = String.from_obj(http_response_header_fields_obj.get_Content_Range())
        http_response_header_fields_.content_type = String.from_obj(http_response_header_fields_obj.get_Content_Type())
        http_response_header_fields_.date = DateTime.from_obj(http_response_header_fields_obj.get_Date())
        http_response_header_fields_.etag = String.from_obj(http_response_header_fields_obj.get_ETag())
        http_response_header_fields_.expires = DateTime.from_obj(http_response_header_fields_obj.get_Expires())
        http_response_header_fields_.last_modified = DateTime.from_obj(http_response_header_fields_obj.get_Last_Modified())
        http_response_header_fields_.link = String.from_obj(http_response_header_fields_obj.get_Link())
        http_response_header_fields_.location = URI.from_obj(http_response_header_fields_obj.get_Location())
        http_response_header_fields_.p3p = String.from_obj(http_response_header_fields_obj.get_P3P())
        http_response_header_fields_.pragma = String.from_obj(http_response_header_fields_obj.get_Pragma())
        http_response_header_fields_.proxy_authenticate = String.from_obj(http_response_header_fields_obj.get_Proxy_Authenticate())
        http_response_header_fields_.refresh = Integer.from_obj(http_response_header_fields_obj.get_Refresh())
        http_response_header_fields_.retry_after = Integer.from_obj(http_response_header_fields_obj.get_Retry_After())
        http_response_header_fields_.server = String.from_obj(http_response_header_fields_obj.get_Server())
        http_response_header_fields_.set_cookie = String.from_obj(http_response_header_fields_obj.get_Set_Cookie())
        http_response_header_fields_.strict_transport_security = String.from_obj(http_response_header_fields_obj.get_Strict_Transport_Security())
        http_response_header_fields_.trailer = String.from_obj(http_response_header_fields_obj.get_Trailer())
        http_response_header_fields_.transfer_encoding = String.from_obj(http_response_header_fields_obj.get_Transfer_Encoding())
        http_response_header_fields_.vary = URI.from_obj(http_response_header_fields_obj.get_Vary())
        http_response_header_fields_.via = String.from_obj(http_response_header_fields_obj.get_Via())
        http_response_header_fields_.warning = String.from_obj(http_response_header_fields_obj.get_Warning())
        http_response_header_fields_.www_authenticate = String.from_obj(http_response_header_fields_obj.get_WWW_Authenticate())
        http_response_header_fields_.x_frame_options = String.from_obj(http_response_header_fields_obj.get_X_Frame_Option())
        http_response_header_fields_.x_xss_protection = String.from_obj(http_response_header_fields_obj.get_X_XSS_Protection())
        http_response_header_fields_.x_content_type_options = String.from_obj(http_response_header_fields_obj.get_X_Content_Type_Options())
        http_response_header_fields_.x_forwarded_proto = String.from_obj(http_response_header_fields_obj.get_X_Forwarded_Proto())
        http_response_header_fields_.x_powered_by = String.from_obj(http_response_header_fields_obj.get_X_Powered_By())
        http_response_header_fields_.x_ua_compatible = String.from_obj(http_response_header_fields_obj.get_X_UA_Compatible())
        return http_response_header_fields_
