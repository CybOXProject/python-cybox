# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.http_session_object as http_session_binding
from cybox.objects.uri_object import URI
from cybox.objects.address_object import EmailAddress
from cybox.objects.port_object import Port
from cybox.common import ObjectProperties, String, DateTime, PositiveInteger, Integer


class HTTPRequestLine(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestLineType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_method = fields.TypedField("HTTP_Method", String)
    value = fields.TypedField("Value", String)
    version = fields.TypedField("Version", String)


class HostField(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HostFieldType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    domain_name = fields.TypedField("Domain_Name", URI)
    port = fields.TypedField("Port", Port)


class HTTPRequestHeaderFields(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestHeaderFieldsType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    accept = fields.TypedField("Accept", String)
    accept_charset = fields.TypedField("Accept_Charset", String)
    accept_language = fields.TypedField("Accept_Language", String)
    accept_datetime = fields.TypedField("Accept_Datetime", String)
    accept_encoding = fields.TypedField("Accept_Encoding", String)
    authorization = fields.TypedField("Authorization", String)
    cache_control = fields.TypedField("Cache_Control", String)
    connection = fields.TypedField("Connection", String)
    cookie = fields.TypedField("Cookie", String)
    content_length = fields.TypedField("Content_Length", Integer)
    content_md5 = fields.TypedField("Content_MD5", String)
    content_type = fields.TypedField("Content_Type", String)
    date = fields.TypedField("Date", DateTime)
    expect = fields.TypedField("Expect", String)
    from_ = fields.TypedField("From", EmailAddress)
    host = fields.TypedField("Host", HostField)
    if_match = fields.TypedField("If_Match", String)
    if_modified_since = fields.TypedField("If_Modified_Since", DateTime)
    if_none_match = fields.TypedField("If_None_Match", String)
    if_range = fields.TypedField("If_Range", String)
    if_unmodified_since = fields.TypedField("If_Unmodified_Since", DateTime)
    max_forwards = fields.TypedField("Max_Forwards", Integer)
    pragma = fields.TypedField("Pragma", String)
    proxy_authorization = fields.TypedField("Proxy_Authorization", String)
    range_ = fields.TypedField("Range", String)
    referer = fields.TypedField("Referer", URI)
    te = fields.TypedField("TE", String)
    user_agent = fields.TypedField("User_Agent", String)
    via = fields.TypedField("Via", String)
    warning = fields.TypedField("Warning", String)
    dnt = fields.TypedField("DNT", String)
    x_requested_with = fields.TypedField("X_Requested_With", String)
    x_forwarded_for = fields.TypedField("X_Forwarded_For", String)
    x_forwarded_proto = fields.TypedField("X_Forwarded_Proto", String)
    x_att_deviceid = fields.TypedField("X_ATT_DeviceId", String)
    x_wap_profile = fields.TypedField("X_Wap_Profile", URI)


class HTTPRequestHeader(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestHeaderType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    raw_header = fields.TypedField("Raw_Header", String)
    parsed_header = fields.TypedField("Parsed_Header", HTTPRequestHeaderFields)


class HTTPMessage(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPMessageType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    length = fields.TypedField("Length", PositiveInteger)
    message_body = fields.TypedField("Message_Body", String)


class HTTPClientRequest(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPClientRequestType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_request_line = fields.TypedField("HTTP_Request_Line", HTTPRequestLine)
    http_request_header = fields.TypedField("HTTP_Request_Header",
                                           HTTPRequestHeader)
    http_message_body = fields.TypedField("HTTP_Message_Body", HTTPMessage)


class HTTPStatusLine(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPStatusLineType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    version = fields.TypedField("Version", String)
    status_code = fields.TypedField("Status_Code", PositiveInteger)
    reason_phrase = fields.TypedField("Reason_Phrase", String)


class HTTPResponseHeaderFields(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPResponseHeaderFieldsType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    access_control_allow_origin = \
            fields.TypedField("Access_Control_Allow_Origin", String)
    accept_ranges = fields.TypedField("Accept_Ranges", String)
    age = fields.TypedField("Age", Integer)
    cache_control = fields.TypedField("Cache_Control", String)
    connection = fields.TypedField("Connection", String)
    content_encoding = fields.TypedField("Content_Encoding", String)
    content_language = fields.TypedField("Content_Language", String)
    content_length = fields.TypedField("Content_Length", Integer)
    content_location = fields.TypedField("Content_Location", String)
    content_md5 = fields.TypedField("Content_MD5", String)
    content_disposition = fields.TypedField("Content_Disposition", String)
    content_range = fields.TypedField("Content_Range", String)
    content_type = fields.TypedField("Content_Type", String)
    date = fields.TypedField("Date", DateTime)
    etag = fields.TypedField("ETag", String)
    expires = fields.TypedField("Expires", DateTime)
    last_modified = fields.TypedField("Last_Modified", DateTime)
    link = fields.TypedField("Link", String)
    location = fields.TypedField("Location", URI)
    p3p = fields.TypedField("P3P", String)
    pragma = fields.TypedField("Pragma", String)
    proxy_authenticate = fields.TypedField("Proxy_Authenticate", String)
    refresh = fields.TypedField("Refresh", String)
    retry_after = fields.TypedField("Retry_After", Integer)
    server = fields.TypedField("Server", String)
    set_cookie = fields.TypedField("Set_Cookie", String)
    strict_transport_security = fields.TypedField("Strict_Transport_Security",
                                                 String)
    trailer = fields.TypedField("Trailer", String)
    transfer_encoding = fields.TypedField("Transfer_Encoding", String)
    vary = fields.TypedField("Vary", String)
    via = fields.TypedField("Via", String)
    warning = fields.TypedField("Warning", String)
    www_authenticate = fields.TypedField("WWW_Authenticate", String)
    x_frame_options = fields.TypedField("X_Frame_Options", String)
    x_xss_protection = fields.TypedField("X_XSS_Protection", String)
    x_content_type_options = fields.TypedField("X_Content_Type_Options", String)
    x_powered_by = fields.TypedField("X_Powered_By", String)
    x_ua_compatible = fields.TypedField("X_UA_Compatible", String)


class HTTPResponseHeader(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPResponseHeaderType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    raw_header = fields.TypedField("Raw_Header", String)
    parsed_header = fields.TypedField("Parsed_Header", HTTPResponseHeaderFields)


class HTTPServerResponse(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPServerResponseType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_status_line = fields.TypedField("HTTP_Status_Line", HTTPStatusLine)
    http_response_header = fields.TypedField("HTTP_Response_Header",
                                            HTTPResponseHeader)
    http_message_body = fields.TypedField("HTTP_Message_Body", HTTPMessage)


class HTTPRequestResponse(entities.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestResponseType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    ordinal_position = fields.TypedField("ordinal_position")
    http_client_request = fields.TypedField("HTTP_Client_Request", HTTPClientRequest)
    http_provisional_server_response = fields.TypedField("HTTP_Provisional_Server_Response", HTTPServerResponse)
    http_server_response = fields.TypedField("HTTP_Server_Response", HTTPServerResponse)


class HTTPSession(ObjectProperties):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPSessionObjectType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"
    _XSI_NS = "HTTPSessionObj"
    _XSI_TYPE = "HTTPSessionObjectType"

    http_request_response = fields.TypedField("HTTP_Request_Response",
                                             HTTPRequestResponse,
                                             multiple=True)
