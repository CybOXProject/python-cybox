# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.http_session_object as http_session_binding
from cybox.objects.uri_object import URI
from cybox.objects.address_object import EmailAddress
from cybox.objects.port_object import Port
from cybox.common import ObjectProperties, String, DateTime, PositiveInteger, Integer


class HTTPRequestLine(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestLineType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_method = cybox.TypedField("HTTP_Method", String)
    value = cybox.TypedField("Value", String)
    version = cybox.TypedField("Version", String)


class HostField(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HostFieldType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    domain_name = cybox.TypedField("Domain_Name", URI)
    port = cybox.TypedField("Port", Port)


class HTTPRequestHeaderFields(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestHeaderFieldsType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    accept = cybox.TypedField("Accept", String)
    accept_charset = cybox.TypedField("Accept_Charset", String)
    accept_language = cybox.TypedField("Accept_Language", String)
    accept_datetime = cybox.TypedField("Accept_Datetime", String)
    accept_encoding = cybox.TypedField("Accept_Encoding", String)
    authorization = cybox.TypedField("Authorization", String)
    cache_control = cybox.TypedField("Cache_Control", String)
    connection = cybox.TypedField("Connection", String)
    cookie = cybox.TypedField("Cookie", String)
    content_length = cybox.TypedField("Content_Length", Integer)
    content_md5 = cybox.TypedField("Content_MD5", String)
    content_type = cybox.TypedField("Content_Type", String)
    date = cybox.TypedField("Date", DateTime)
    expect = cybox.TypedField("Expect", String)
    from_ = cybox.TypedField("From", EmailAddress)
    host = cybox.TypedField("Host", HostField)
    if_match = cybox.TypedField("If_Match", String)
    if_modified_since = cybox.TypedField("If_Modified_Since", DateTime)
    if_none_match = cybox.TypedField("If_None_Match", String)
    if_range = cybox.TypedField("If_Range", String)
    if_unmodified_since = cybox.TypedField("If_Unmodified_Since", DateTime)
    max_forwards = cybox.TypedField("Max_Forwards", Integer)
    pragma = cybox.TypedField("Pragma", String)
    proxy_authorization = cybox.TypedField("Proxy_Authorization", String)
    range_ = cybox.TypedField("Range", String)
    referer = cybox.TypedField("Referer", URI)
    te = cybox.TypedField("TE", String)
    user_agent = cybox.TypedField("User_Agent", String)
    via = cybox.TypedField("Via", String)
    warning = cybox.TypedField("Warning", String)
    dnt = cybox.TypedField("DNT", String)
    x_requested_with = cybox.TypedField("X_Requested_With", String)
    x_forwarded_for = cybox.TypedField("X_Forwarded_For", String)
    x_forwarded_proto = cybox.TypedField("X_Forwarded_Proto", String)
    x_att_deviceid = cybox.TypedField("X_ATT_DeviceId", String)
    x_wap_profile = cybox.TypedField("X_Wap_Profile", URI)


class HTTPRequestHeader(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestHeaderType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    raw_header = cybox.TypedField("Raw_Header", String)
    parsed_header = cybox.TypedField("Parsed_Header", HTTPRequestHeaderFields)


class HTTPMessage(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPMessageType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    length = cybox.TypedField("Length", PositiveInteger)
    message_body = cybox.TypedField("Message_Body", String)


class HTTPClientRequest(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPClientRequestType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_request_line = cybox.TypedField("HTTP_Request_Line", HTTPRequestLine)
    http_request_header = cybox.TypedField("HTTP_Request_Header",
                                           HTTPRequestHeader)
    http_message_body = cybox.TypedField("HTTP_Message_Body", HTTPMessage)


class HTTPStatusLine(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPStatusLineType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    version = cybox.TypedField("Version", String)
    status_code = cybox.TypedField("Status_Code", PositiveInteger)
    reason_phrase = cybox.TypedField("Reason_Phrase", String)


class HTTPResponseHeaderFields(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPResponseHeaderFieldsType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    access_control_allow_origin = \
            cybox.TypedField("Access_Control_Allow_Origin", String)
    accept_ranges = cybox.TypedField("Accept_Ranges", String)
    age = cybox.TypedField("Age", Integer)
    cache_control = cybox.TypedField("Cache_Control", String)
    connection = cybox.TypedField("Connection", String)
    content_encoding = cybox.TypedField("Content_Encoding", String)
    content_language = cybox.TypedField("Content_Language", String)
    content_length = cybox.TypedField("Content_Length", Integer)
    content_location = cybox.TypedField("Content_Location", String)
    content_md5 = cybox.TypedField("Content_MD5", String)
    content_disposition = cybox.TypedField("Content_Disposition", String)
    content_range = cybox.TypedField("Content_Range", String)
    content_type = cybox.TypedField("Content_Type", String)
    date = cybox.TypedField("Date", DateTime)
    etag = cybox.TypedField("ETag", String)
    expires = cybox.TypedField("Expires", DateTime)
    last_modified = cybox.TypedField("Last_Modified", DateTime)
    link = cybox.TypedField("Link", String)
    location = cybox.TypedField("Location", URI)
    p3p = cybox.TypedField("P3P", String)
    pragma = cybox.TypedField("Pragma", String)
    proxy_authenticate = cybox.TypedField("Proxy_Authenticate", String)
    refresh = cybox.TypedField("Refresh", String)
    retry_after = cybox.TypedField("Retry_After", Integer)
    server = cybox.TypedField("Server", String)
    set_cookie = cybox.TypedField("Set_Cookie", String)
    strict_transport_security = cybox.TypedField("Strict_Transport_Security",
                                                 String)
    trailer = cybox.TypedField("Trailer", String)
    transfer_encoding = cybox.TypedField("Transfer_Encoding", String)
    vary = cybox.TypedField("Vary", String)
    via = cybox.TypedField("Via", String)
    warning = cybox.TypedField("Warning", String)
    www_authenticate = cybox.TypedField("WWW_Authenticate", String)
    x_frame_options = cybox.TypedField("X_Frame_Options", String)
    x_xss_protection = cybox.TypedField("X_XSS_Protection", String)
    x_content_type_options = cybox.TypedField("X_Content_Type_Options", String)
    x_powered_by = cybox.TypedField("X_Powered_By", String)
    x_ua_compatible = cybox.TypedField("X_UA_Compatible", String)


class HTTPResponseHeader(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPResponseHeaderType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    raw_header = cybox.TypedField("Raw_Header", String)
    parsed_header = cybox.TypedField("Parsed_Header", HTTPResponseHeaderFields)


class HTTPServerResponse(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPServerResponseType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    http_status_line = cybox.TypedField("HTTP_Status_Line", HTTPStatusLine)
    http_response_header = cybox.TypedField("HTTP_Response_Header",
                                            HTTPResponseHeader)
    http_message_body = cybox.TypedField("HTTP_Message_Body", HTTPMessage)


class HTTPRequestResponse(cybox.Entity):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPRequestResponseType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"

    ordinal_position = cybox.TypedField("ordinal_position")
    http_client_request = cybox.TypedField("HTTP_Client_Request", HTTPClientRequest)
    http_provisional_server_response = cybox.TypedField("HTTP_Provisional_Server_Response", HTTPServerResponse)
    http_server_response = cybox.TypedField("HTTP_Server_Response", HTTPServerResponse)


class HTTPSession(ObjectProperties):
    _binding = http_session_binding
    _binding_class = http_session_binding.HTTPSessionObjectType
    _namespace = "http://cybox.mitre.org/objects#HTTPSessionObject-2"
    _XSI_NS = "HTTPSessionObj"
    _XSI_TYPE = "HTTPSessionObjectType"

    http_request_response = cybox.TypedField("HTTP_Request_Response",
                                             HTTPRequestResponse,
                                             multiple=True)
