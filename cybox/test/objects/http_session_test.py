# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.address_object import Address
from cybox.objects.http_session_object import HTTPSession
from cybox.objects.uri_object import URI
from cybox.test.objects import ObjectTestCase


class TestHTTPSession(ObjectTestCase, unittest.TestCase):
    object_type = "HTTPSessionObjectType"
    klass = HTTPSession

    _full_dict = {
        'http_request_response': [
            {
                'http_client_request': {
                    'http_request_line': {
                        'http_method': u("GET"),
                        'value': u("/index.html"),
                        'version': u("http/1.1"),
                    },
                    'http_request_header': {
                        'raw_header': u("...ALL THE REQUEST HEADERS..."),
                        'parsed_header': {
                            'accept': u("text/plain"),
                            'accept_charset': u("utf-8"),
                            'accept_language': u("en-US"),
                            'accept_datetime':
                                    u("Thu, 31 May 2007 20:35:00 GMT"),
                            'accept_encoding': u("gzip, deflate"),
                            'authorization': u("Basic QWxhZGRbpjpvc"),
                            'cache_control': u("no-cache"),
                            'connection': u("keep-alive"),
                            'cookie': u("$Version=1; Skin=new;"),
                            'content_length': 348,
                            'content_md5': u("Q2hlY2sgSW50ZWdyaXR5IQ=="),
                            'content_type': u("application/xml"),
                            'date': "1994-11-15T08:12:31+00:00",
                            'expect': u("200-ok"),
                            'from': {'address_value': u("bob@example.com"),
                                        'category': Address.CAT_EMAIL,
                                        'xsi:type': "AddressObjectType"},
                            'host': {
                                'domain_name': {
                                    'value': u("en.wikipedia.org"),
                                    'type': URI.TYPE_DOMAIN,
                                    'xsi:type': "URIObjectType"
                                },
                                'port': {
                                    'port_value': 80,
                                    'layer4_protocol': u("TCP"),
                                    'xsi:type': "PortObjectType"
                                }
                            },
                            'if_match':
                                    u("737060cd8c284d8af7ad3082f209582d"),
                            'if_modified_since':
                                    "1994-10-29T19:43:31+00:00",
                            'if_none_match':
                                    u("737060cd8c284d8af7ad3082f209582e"),
                            'if_range':
                                    u("737060cd8c284d8af7ad3082f209582f"),
                            'if_unmodified_since':
                                    "1996-11-22T09:33:32+00:00",
                            'max_forwards': 10,
                            'pragma': u("no-cache"),
                            'proxy_authorization': u("Basic QwxhZ=="),
                            'range': u("bytes=500-999"),
                            'referer': {
                                'value': u("http://en.wikipedia.org/wiki"),
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                            'te': u("trailers, deflate"),
                            'user_agent': u("Mozilla/5.0 Firefox/21.0"),
                            'via': u("1.0 fred, 1.1 example.com"),
                            'warning': u("199 Miscellaneous warning"),
                            'dnt': u("1 (Do Not Track Enabled)"),
                            'x_requested_with': u("XMLHttpRequest"),
                            'x_forwarded_for': u("client1, proxy1"),
                            'x_forwarded_proto': u("https"),
                            'x_att_deviceid': u("MakeModel/Firmware"),
                            'x_wap_profile': {
                                'value': u("http://samsung.com/SGHI777.xml"),
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                        }
                    },
                    'http_message_body': {
                        'length': 10,
                        'message_body': u("Hi there!!"),
                    }
                },
            },
            {
                'http_server_response': {
                    'http_status_line': {
                        'version': u("http/1.0"),
                        'status_code': 200,
                        'reason_phrase': u("OK")
                    },
                    'http_response_header': {
                        'raw_header': u("...ALL THE RESPONSE HEADERS..."),
                        'parsed_header': {
                            'access_control_allow_origin': u("*"),
                            'accept_ranges': u("bytes"),
                            'age': 12,
                            'cache_control': u("max-age=3600"),
                            'connection': u("close"),
                            'content_encoding': u("gzip"),
                            'content_language': u("da"),
                            'content_length': 348,
                            'content_location': u("/index.htm"),
                            'content_md5': u("Q2hlY2sgSW50ZWdyaXR5IQ=="),
                            'content_disposition': u("attachment; filename"),
                            'content_range': u("bytes 21010-47021"),
                            'content_type': u("text/html; charset=utf-8"),
                            'date': "1994-11-15T08:12:31+00:00",
                            'etag': u('"737060cd8c284d8af7ad3082f20"'),
                            'expires': "1994-12-01T16:00:00+00:00",
                            'last_modified': "1994-11-15T16:00:00+00:00",
                            'link': u('1</feed>; rel="alternate"'),
                            'location': {
                                'value': u("http://www.w3c.org/pub/hi.html"),
                                'type': URI.TYPE_URL,
                                'xsi:type': "URIObjectType",
                            },
                            'p3p': u("CP=\"This is not a P3P policy!\""),
                            'pragma': u("no-cache"),
                            'proxy_authenticate': u("Basic"),
                            'refresh': u("5"),
                            'retry_after': 120,
                            'server': u("Apache/2.4.1 (Unix)"),
                            'set_cookie': u("UserID=JohnDoe, Version=1"),
                            'strict_transport_security': u("max-age=160740"),
                            'trailer': u("Max-Forwards"),
                            'transfer_encoding': u("chunked"),
                            'vary': u("*"),
                            'via': u("1.0 fred, 1.1 example.com"),
                            'warning': u("199 Miscellaneous warning"),
                            'www_authenticate': u("Basic"),
                            'x_frame_options': u("deny"),
                            'x_xss_protection': u("1; mode=block"),
                            'x_content_type_options': u("nosniff"),
                            'x_powered_by': u("PHP/5.4.0"),
                            'x_ua_compatible': u("Chrome=1"),
                        }
                    },
                    'http_message_body': {
                        'length': 26,
                        'message_body': u("<html><head></head></html>"),
                    }
                },
            },
        ],
        'xsi:type': object_type,
    }

    def test_object_reference(self, ref_dict=None):
        # We have to put at least some content in here, since at least one
        # HTTPRequestResponse is required by the bindings for the round trip.
        sess_dict = {
            'http_request_response': [{
                    'http_client_request': {
                        'http_request_line': {'http_method': u("GET")}
                    }
            }]
        }
        ObjectTestCase.test_object_reference(self, sess_dict)


if __name__ == "__main__":
    unittest.main()
