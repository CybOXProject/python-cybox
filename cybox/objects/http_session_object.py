import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.http_session_object_1_0 as http_session_object_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.objects.uri_object import uri_object
from cybox.objects.address_object import address_object
from cybox.objects.port_object import port_object

class http_session_object(object):
    def __init__(self):
        pass

    @classmethod
    def create_from_dict(cls, http_session_attributes):
        """Create the HTTP Session Object object representation from an input dictionary"""
        pass

    @classmethod
    def parse_into_dict(cls, defined_object, defined_object_dict = None):
        """Parse and return a dictionary for an HTTP Session Object object"""
        if defined_object_dict == None:
            defined_object_dict = {}
        http_request_responses = []
        for http_request_response in defined_object.get_HTTP_Request_Response():
            http_request_response_dict = {}
            if http_request_response.get_HTTP_Client_Request() is not None:
                http_request_response_dict['http_client_request'] = cls.__parse_http_client_request(http_request_response.get_HTTP_Client_Request())
            if http_request_response.get_HTTP_Server_Response() is not None:
                http_request_response_dict['http_server_response'] = cls.__parse_http_server_response(http_request_response.get_HTTP_Server_Response())
            http_request_responses.append(http_request_response_dict)
        defined_object_dict['http_request_responses'] = http_request_responses
        return defined_object_dict

    @classmethod
    def __parse_http_client_request(cls, http_client_request):
        http_client_request_dict = {}
        if http_client_request.get_HTTP_Request_Line() is not None:
            client_request_line = http_client_request.get_HTTP_Request_Line() 
            client_request_line_dict = {}
            if client_request_line.get_HTTP_Method() is not None:
                client_request_line_dict['http_method'] = baseobjectattribute.parse_into_dict(client_request_line.get_HTTP_Method())
            if client_request_line.get_Value() is not None:
                client_request_line_dict['value'] = baseobjectattribute.parse_into_dict(client_request_line.get_HTTP_Value())
            if client_request_line.get_Version() is not None:
                client_request_line_dict['version'] = baseobjectattribute.parse_into_dict(client_request_line.get_Version())
            http_client_request_dict['http_request_line'] = client_request_line_dict
        if http_client_request.get_HTTP_Request_Header() is not None:
            request_header = http_client_request.get_HTTP_Request_Header()
            request_header_dict = {}
            if request_header.get_Raw_Header() is not None:
                request_header_dict['raw_header'] = request_header.get_Raw_Header()
            if request_header.get_Parsed_Header() is not None:
                parsed_header = request_header.get_Parsed_Header()
                parsed_header_dict = {}
                if parsed_header.get_Accept() is not None: parsed_header_dict['accept'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept())
                if parsed_header.get_Accept_Charset() is not None: parsed_header_dict['accept-charset'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept_Charset())
                if parsed_header.get_Accept_Language() is not None: parsed_header_dict['accept-language'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept_Language())
                if parsed_header.get_Accept_Datetime() is not None: parsed_header_dict['accept-datetime'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept_Datetime())
                if parsed_header.get_Accept_Encoding() is not None: parsed_header_dict['accept'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept_Encoding())
                if parsed_header.get_Authorization() is not None: parsed_header_dict['authorization'] = baseobjectattribute.parse_into_dict(parsed_header.get_Authorization())
                if parsed_header.get_Cache_Control() is not None: parsed_header_dict['cache-control'] = baseobjectattribute.parse_into_dict(parsed_header.get_Cache_Control())
                if parsed_header.get_Connection() is not None: parsed_header_dict['connection'] = baseobjectattribute.parse_into_dict(parsed_header.get_Connection())
                if parsed_header.get_Cookie() is not None: parsed_header_dict['cookie'] = baseobjectattribute.parse_into_dict(parsed_header.get_Cookie())
                if parsed_header.get_Content_Length() is not None: parsed_header_dict['content-length'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Length())
                if parsed_header.get_Content_MD5() is not None: parsed_header_dict['content-md5'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_MD5())
                if parsed_header.get_Content_Type() is not None: parsed_header_dict['content-type'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Type())
                if parsed_header.get_Date() is not None: parsed_header_dict['date'] = baseobjectattribute.parse_into_dict(parsed_header.get_Date())
                if parsed_header.get_Expect() is not None: parsed_header_dict['expect'] = baseobjectattribute.parse_into_dict(parsed_header.get_Expect())
                if parsed_header.get_From() is not None: parsed_header_dict['from'] = address_object.parse_into_dict(parsed_header.get_From())
                if parsed_header.get_Host() is not None: 
                    host = parsed_header.get_Host()
                    host_dict = {}
                    if host.get_Domain_Name() is not None: host_dict['domain_name'] = uri_object.parse_into_dict(host.get_Domain_Name())
                    if host.get_Port() is not None: host_dict['port'] = port_object.parse_into_dict(host.get_Port())
                    parsed_header_dict['host'] = host_dict
                if parsed_header.get_If_Match() is not None: parsed_header_dict['if-match'] = baseobjectattribute.parse_into_dict(parsed_header.get_If_Match())
                if parsed_header.get_If_Modified_Since() is not None: parsed_header_dict['if-modified-since'] = baseobjectattribute.parse_into_dict(parsed_header.get_If_Modified_Since())
                if parsed_header.get_If_None_Match() is not None: parsed_header_dict['if-none-match'] = baseobjectattribute.parse_into_dict(parsed_header.get_If_None_Match())
                if parsed_header.get_If_Range() is not None: parsed_header_dict['if-range'] =baseobjectattribute.parse_into_dict( parsed_header.get_If_Range())
                if parsed_header.get_If_Unmodified_Since() is not None: parsed_header_dict['if-unmodified-since'] = baseobjectattribute.parse_into_dict(parsed_header.get_If_Unmodified_Since())
                if parsed_header.get_Max_Forwards() is not None: parsed_header_dict['max-forwards'] = baseobjectattribute.parse_into_dict(parsed_header.get_Max_Forwards())
                if parsed_header.get_Pragma() is not None: parsed_header_dict['pragma'] = baseobjectattribute.parse_into_dict(parsed_header.get_Pragma())
                if parsed_header.get_Proxy_Authorization() is not None: parsed_header_dict['proxy-authorization'] = baseobjectattribute.parse_into_dict(parsed_header.get_Proxy_Authorization())
                if parsed_header.get_Range() is not None: parsed_header_dict['range'] = baseobjectattribute.parse_into_dict(parsed_header.get_Range())
                if parsed_header.get_Referer() is not None: parsed_header_dict['referer'] = uri_object.parse_into_dict(parsed_header.get_Referer())
                if parsed_header.get_TE() is not None: parsed_header_dict['te'] = baseobjectattribute.parse_into_dict(parsed_header.get_TE())
                if parsed_header.get_User_Agent() is not None: parsed_header_dict['user-agent'] = baseobjectattribute.parse_into_dict(parsed_header.get_User_Agent())
                if parsed_header.get_Via() is not None: parsed_header_dict['via'] = baseobjectattribute.parse_into_dict(parsed_header.get_Via())
                if parsed_header.get_Warning() is not None: parsed_header_dict['warning'] = baseobjectattribute.parse_into_dict(parsed_header.get_Warning())
                if parsed_header.get_DNT() is not None: parsed_header_dict['DNT'] = uri_object.parse_into_dict(parsed_header.get_DNT())
                if parsed_header.get_X_Requested_With() is not None: parsed_header_dict['x-requested-with'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Requested_With())
                if parsed_header.get_X_Requested_For() is not None: parsed_header_dict['x-requested-for'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Requested_For())
                if parsed_header.get_X_ATT_DeviceId() is not None: parsed_header_dict['x-att-deviceid'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_ATT_DeviceId())
                if parsed_header.get_X_Wap_Profile() is not None: parsed_header_dict['x-wap-profile'] = uri_object.parse_into_dict(parsed_header.get_X_Wap_Profile())
                request_header_dict['parsed_header'] = parsed_header_dict
            http_client_request_dict['http_request_header'] = request_header_dict
        if http_client_request.get_HTTP_Message_Body() is not None:
            message_body = http_client_request.get_HTTP_Message_Body()
            message_body_dict = {}
            if message_body.get_Length() is not None: message_body_dict['length'] = baseobjectattribute.parse_into_dict(message_body.get_Length())
            if message_body.get_Message_Body() is not None: message_body_dict['message_body'] = baseobjectattribute.parse_into_dict(message_body.get_Message_Body())
            http_client_request_dict['http_message_body'] = message_body_dict 
        return http_client_request_dict

    @classmethod
    def __parse_http_server_response(cls, http_server_response):
        http_server_response_dict = {}
        if http_server_response.get_HTTP_Status_Line() is not None:
            server_status_line = http_server_response.get_HTTP_Status_Line() 
            server_status_line_dict = {}
            if server_status_line_dict.get_Version() is not None:
                server_status_line_dict['version'] = baseobjectattribute.parse_into_dict(server_status_line.get_Version())
            if server_status_line_dict.get_Status_Code() is not None:
                server_status_line_dict['status_code'] = baseobjectattribute.parse_into_dict(server_status_line.get_Status_Code())
            if server_status_line_dict.get_Reason_Phrase() is not None:
                server_status_line_dict['reason_phrase'] = baseobjectattribute.parse_into_dict(server_status_line.get_Reason_Phrase())
            http_server_response_dict['http_status_line'] = server_status_line_dict
        if http_server_response.get_HTTP_Response_Header() is not None:
            response_header = http_server_response.get_HTTP_Response_Header()
            response_header_dict = {}
            if response_header.get_Raw_Header() is not None:
                response_header_dict['raw_header'] = response_header.get_Raw_Header()
            if response_header.get_Parsed_Header() is not None:
                parsed_header = response_header.get_Parsed_Header()
                parsed_header_dict = {}
                if parsed_header.get_Access_Control_Allow_Origin() is not None: parsed_header_dict['access-control-allow-origin'] = baseobjectattribute.parse_into_dict(parsed_header.get_Access_Control_Allow_Origin())
                if parsed_header.get_Accept_Ranges() is not None: parsed_header_dict['accept-ranges'] = baseobjectattribute.parse_into_dict(parsed_header.get_Accept_Ranges())
                if parsed_header.get_Age() is not None: parsed_header_dict['age'] = baseobjectattribute.parse_into_dict(parsed_header.get_Age())
                if parsed_header.get_Cache_Control() is not None: parsed_header_dict['cache-control'] = baseobjectattribute.parse_into_dict(parsed_header.get_Cache_Control())
                if parsed_header.get_Connection() is not None: parsed_header_dict['connection'] = baseobjectattribute.parse_into_dict(parsed_header.get_Connection())
                if parsed_header.get_Content_Encoding() is not None: parsed_header_dict['content-encoding'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Encoding())
                if parsed_header.get_Content_Language() is not None: parsed_header_dict['content-language'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Language())
                if parsed_header.get_Content_Length() is not None: parsed_header_dict['content-length'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Length())
                if parsed_header.get_Content_Location() is not None: parsed_header_dict['content-location'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Location())
                if parsed_header.get_Content_MD5() is not None: parsed_header_dict['content-md5'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_MD5())
                if parsed_header.get_Content_Disposition() is not None: parsed_header_dict['content-disposition'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Disposition())
                if parsed_header.get_Content_Range() is not None: parsed_header_dict['content-range'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Range())
                if parsed_header.get_Content_Type() is not None: parsed_header_dict['content-type'] = baseobjectattribute.parse_into_dict(parsed_header.get_Content_Type())
                if parsed_header.get_Date() is not None: parsed_header_dict['date'] = baseobjectattribute.parse_into_dict(parsed_header.get_Date())
                if parsed_header.get_ETag() is not None: parsed_header_dict['etag'] = baseobjectattribute.parse_into_dict(parsed_header.get_ETag())
                if parsed_header.get_Expires() is not None: parsed_header_dict['expires'] = baseobjectattribute.parse_into_dict(parsed_header.get_Expires())
                if parsed_header.get_Last_Modified() is not None: parsed_header_dict['last-modified'] = baseobjectattribute.parse_into_dict(parsed_header.get_Last_Modified())
                if parsed_header.get_Link() is not None: parsed_header_dict['link'] = baseobjectattribute.parse_into_dict(parsed_header.get_Link())
                if parsed_header.get_Location() is not None: parsed_header_dict['location'] = uri_object.create_from_dict(parsed_header.get_Location())
                if parsed_header.get_P3P() is not None: parsed_header_dict['p3p'] = baseobjectattribute.parse_into_dict(parsed_header.get_P3P())
                if parsed_header.get_Pragma() is not None: parsed_header_dict['pragma'] = baseobjectattribute.parse_into_dict(parsed_header.get_Pragma())
                if parsed_header.get_Proxy_Authenticate() is not None: parsed_header_dict['proxy-authenticate'] = baseobjectattribute.parse_into_dict(parsed_header.get_Proxy_Authenticate())
                if parsed_header.get_Refresh() is not None: parsed_header_dict['refresh'] = baseobjectattribute.parse_into_dict(parsed_header.get_Refresh())
                if parsed_header.get_Retry_After() is not None: parsed_header_dict['retry-after'] = baseobjectattribute.parse_into_dict(parsed_header.get_Retry_After())
                if parsed_header.get_Server() is not None: parsed_header_dict['server'] = baseobjectattribute.parse_into_dict(parsed_header.get_Server())
                if parsed_header.get_Set_Cookie() is not None: parsed_header_dict['set-cookie'] = baseobjectattribute.parse_into_dict(parsed_header.get_Set_Cookie())
                if parsed_header.get_Strict_Transport_Security() is not None: parsed_header_dict['strict-transport-security'] = baseobjectattribute.parse_into_dict(parsed_header.get_Strict_Transport_Security())
                if parsed_header.get_Trailer() is not None: parsed_header_dict['trailer'] = baseobjectattribute.parse_into_dict(parsed_header.get_Trailer())
                if parsed_header.get_Transfer_Encoding() is not None: parsed_header_dict['transfer-encoding'] = baseobjectattribute.parse_into_dict(parsed_header.get_Transfer_Encoding())
                if parsed_header.get_Vary() is not None: parsed_header_dict['vary'] = uri_object.parse_into_dict(parsed_header.get_Vary(), vary_dict)
                if parsed_header.get_Via() is not None: parsed_header_dict['via'] = baseobjectattribute.parse_into_dict(parsed_header.get_Via())
                if parsed_header.get_Warning() is not None: parsed_header_dict['warning'] = baseobjectattribute.parse_into_dict(parsed_header.get_Warning())
                if parsed_header.get_WWW_Authenticate() is not None: parsed_header_dict['www-authenticate'] = baseobjectattribute.parse_into_dict(parsed_header.get_WWW_Authenticate())
                if parsed_header.get_X_Frame_Options() is not None: parsed_header_dict['x-frame-options'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Frame_Options())
                if parsed_header.get_X_XSS_Protection() is not None: parsed_header_dict['x-xss-protection'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_XSS_Protection())
                if parsed_header.get_X_Content_Type_Options() is not None: parsed_header_dict['x-content-type-options'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Content_Type_Options())
                if parsed_header.get_X_Forwarded_Proto() is not None: parsed_header_dict['x-forwarded-proto'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Forwareded_Proto())
                if parsed_header.get_X_Powered_By() is not None: parsed_header_dict['x-powered-by'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_Powered_By())
                if parsed_header.get_X_UA_Compatible() is not None: parsed_header_dict['x-ua-compatible'] = baseobjectattribute.parse_into_dict(parsed_header.get_X_UA_Compatible())
                response_header_dict['parsed_header'] = parsed_header_dict
            http_server_response_dict['http_response_header'] = response_header_dict
        if http_server_response.get_HTTP_Message_Body() is not None:
            message_body = http_server_response.get_HTTP_Message_Body()
            message_body_dict = {}
            if message_body.get_Length() is not None: message_body_dict['length'] = baseobjectattribute.parse_into_dict(message_body.get_Length())
            if message_body.get_Message_Body() is not None: message_body_dict['message_body'] = baseobjectattribute.parse_into_dict(message_body.get_Message_Body())
            http_server_response_dict['http_message_body'] = message_body_dict 
        return http_server_response_dict