# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.x509_certificate_object import (SubjectPublicKey,
                                                   RSAPublicKey, Validity,
                                                   X509Cert, X509Certificate,
                                                   X509CertificateSignature,
                                                   X509NonStandardExtensions,
                                                   X509V3Extensions)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestValidity(EntityTestCase, unittest.TestCase):
    klass = Validity

    _full_dict = {
        'not_before': '2006-11-17T00:00:00+00:00',
        'not_after': '2036-07-16T23:59:59+00:00',
    }


class TestRSAPublicKey(EntityTestCase, unittest.TestCase):
    klass = RSAPublicKey

    _full_dict = {
        'modulus': u('00:ac:a0:f0:fb:80:59:d4:9c:c7:a4:cf:9d:a1:59:73:09:10:45:0c:0d:2c:6e:68:f1:6c:5b:48:68:49:59:37:fc:0b:33:19:c2:77:7f:cc:10:2d:95:34:1c:e6:eb:4d:09:a7:1c:d2:b8:c9:97:36:02:b7:89:d4:24:5f:06:c0:cc:44:94:94:8d:02:62:6f:eb:5a:dd:11:8d:28:9a:5c:84:90:10:7a:0d:bd:74:66:2f:6a:38:a0:e2:d5:54:44:eb:1d:07:9f:07:ba:6f:ee:e9:fd:4e:0b:29:f5:3e:84:a0:01:f1:9c:ab:f8:1c:7e:89:a4:e8:a1:d8:71:65:0d:a3:51:7b:ee:bc:d2:22:60:0d:b9:5b:9d:df:ba:fc:51:5b:0b:af:98:b2:e9:2e:e9:04:e8:62:87:de:2b:c8:d7:4e:c1:4c:64:1e:dd:cf:87:58:ba:4a:4f:ca:68:07:1d:1c:9d:4a:c6:d5:2f:91:cc:7c:71:72:1c:c5:c0:67:eb:32:fd:c9:92:5c:94:da:85:c0:9b:bf:53:7d:2b:09:f4:8c:9d:91:1f:97:6a:52:cb:de:09:36:a4:77:d8:7b:87:50:44:d5:3e:6e:29:69:fb:39:49:26:1e:09:a5:80:7b:40:2d:eb:e8:27:85:c9:fe:61:fd:7e:e6:7c:97:1d:d5:9d'),
        'exponent': 65537,
    }


class TestSubjectPublicKey(EntityTestCase, unittest.TestCase):
    klass = SubjectPublicKey

    _full_dict = {
        'public_key_algorithm': u('rsaEncryption'),
        'rsa_public_key': TestRSAPublicKey._full_dict,
    }


class TestX509NonStandardExtensions(EntityTestCase, unittest.TestCase):
    klass = X509NonStandardExtensions

    _full_dict = {
        'netscape_comment': u('some netscape comment'),
        'netscape_certificate_type': u('cert type'),
        'old_authority_key_identifier': u('CE:CB'),
        'old_primary_key_attributes': u('CA:TRUE'),
    }


class TestX509V3Extensions(EntityTestCase, unittest.TestCase):
    klass = X509V3Extensions

    _full_dict = {
        'basic_constraints': u('CA:TRUE'),
        'key_usage':  u('Certificate Sign, CRL Sign'),
        'subject_key_identifier': u('7B:5B:45:CF:AF:CE:CB:7A:FD:31:92:1A:6A:B6:F3:46:EB:57:48:50')
    }


class TestX509Cert(EntityTestCase, unittest.TestCase):
    klass = X509Cert

    _full_dict = {
        'version': 3,
        'serial_number': u('34:4e:d5:57:20:d5:ed:ec:49:f4:2f:ce:37:db:2b:6d'),
        'signature_algorithm': u('sha1WithRSAEncryption'),
        'issuer': u('C = US, O = "thawte, Inc.", OU = Certification Services Division, OU = "(c) 2006 thawte, Inc. - For authorized use only", CN = thawte Primary Root CA'),
        'validity': TestValidity._full_dict,
        'subject': u('C = US, O = "thawte, Inc.", OU = Certification Services Division, OU = "(c) 2006 thawte, Inc. - For authorized use only", CN = thawte Primary Root CA'),
        'subject_public_key': TestSubjectPublicKey._full_dict,
        'standard_extensions': TestX509V3Extensions._full_dict,
    }


class TestX509CertificateSignature(EntityTestCase, unittest.TestCase):
    klass = X509CertificateSignature

    _full_dict = {
        'signature_algorithm': u('sha1WithRSAEncryption'),
        'signature': u('79:11:c0:4b:b3:91:b6:fc:f0:e9:67:d4:0d:6e:45:be:55:e8:93:d2:ce:03:3f:ed:da:25:b0:1d:57:cb:1e:3a:76:a0:4c:ec:50:76:e8:64:72:0c:a4:a9:f1:b8:8b:d6:d6:87:84:bb:32:e5:41:11:c0:77:d9:b3:60:9d:eb:1b:d5:d1:6e:44:44:a9:a6:01:ec:55:62:1d:77:b8:5c:8e:48:49:7c:9c:3b:57:11:ac:ad:73:37:8e:2f:78:5c:90:68:47:d9:60:60:e6:fc:07:3d:22:20:17:c4:f7:16:e9:c4:d8:72:f9:c8:73:7c:df:16:2f:15:a9:3e:fd:6a:27:b6:a1:eb:5a:ba:98:1f:d5:e3:4d:64:0a:9d:13:c8:61:ba:f5:39:1c:87:ba:b8:bd:7b:22:7f:f6:fe:ac:40:79:e5:ac:10:6f:3d:8f:1b:79:76:8b:c4:37:b3:21:18:84:e5:36:00:eb:63:20:99:b9:e9:fe:33:04:bb:41:c8:c1:02:f9:44:63:20:9e:81:ce:42:d3:d6:3f:2c:76:d3:63:9c:59:dd:8f:a6:e1:0e:a0:2e:41:f7:2e:95:47:cf:bc:fd:33:f3:f6:0b:61:7e:7e:91:2b:81:47:c2:27:30:ee:a7:10:5d:37:8f:5c:39:2b:e4:04:f0:7b:8d:56:8c:68'),
    }


class TestX509Certificate(ObjectTestCase, unittest.TestCase):
    object_type = "X509CertificateObjectType"
    klass = X509Certificate

    _full_dict = {
        'certificate': TestX509Cert._full_dict,
        'raw_certificate': u('''-----BEGIN CERTIFICATE-----
MIIEIDCCAwigAwIBAgIQNE7VVyDV7exJ9C/ON9srbTANBgkqhkiG9w0BAQUFADCB
qTELMAkGA1UEBhMCVVMxFTATBgNVBAoTDHRoYXd0ZSwgSW5jLjEoMCYGA1UECxMf
Q2VydGlmaWNhdGlvbiBTZXJ2aWNlcyBEaXZpc2lvbjE4MDYGA1UECxMvKGMpIDIw
MDYgdGhhd3RlLCBJbmMuIC0gRm9yIGF1dGhvcml6ZWQgdXNlIG9ubHkxHzAdBgNV
BAMTFnRoYXd0ZSBQcmltYXJ5IFJvb3QgQ0EwHhcNMDYxMTE3MDAwMDAwWhcNMzYw
NzE2MjM1OTU5WjCBqTELMAkGA1UEBhMCVVMxFTATBgNVBAoTDHRoYXd0ZSwgSW5j
LjEoMCYGA1UECxMfQ2VydGlmaWNhdGlvbiBTZXJ2aWNlcyBEaXZpc2lvbjE4MDYG
A1UECxMvKGMpIDIwMDYgdGhhd3RlLCBJbmMuIC0gRm9yIGF1dGhvcml6ZWQgdXNl
IG9ubHkxHzAdBgNVBAMTFnRoYXd0ZSBQcmltYXJ5IFJvb3QgQ0EwggEiMA0GCSqG
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQCsoPD7gFnUnMekz52hWXMJEEUMDSxuaPFs
W0hoSVk3/AszGcJ3f8wQLZU0HObrTQmnHNK4yZc2AreJ1CRfBsDMRJSUjQJib+ta
3RGNKJpchJAQeg29dGYvajig4tVUROsdB58Hum/u6f1OCyn1PoSgAfGcq/gcfomk
6KHYcWUNo1F77rzSImANuVud37r8UVsLr5iy6S7pBOhih94ryNdOwUxkHt3Ph1i6
Sk/KaAcdHJ1KxtUvkcx8cXIcxcBn6zL9yZJclNqFwJu/U30rCfSMnZEfl2pSy94J
NqR32HuHUETVPm4pafs5SSYeCaWAe0At6+gnhcn+Yf1+5nyXHdWdAgMBAAGjQjBA
MA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEGMB0GA1UdDgQWBBR7W0XP
r87Lev0xkhpqtvNG61dIUDANBgkqhkiG9w0BAQUFAAOCAQEAeRHAS7ORtvzw6WfU
DW5FvlXok9LOAz/t2iWwHVfLHjp2oEzsUHboZHIMpKnxuIvW1oeEuzLlQRHAd9mz
YJ3rG9XRbkREqaYB7FViHXe4XI5ISXycO1cRrK1zN44veFyQaEfZYGDm/Ac9IiAX
xPcW6cTYcvnIc3zfFi8VqT79aie2oetaupgf1eNNZAqdE8hhuvU5HIe6uL17In/2
/qxAeeWsEG89jxt5dovEN7MhGITlNgDrYyCZuen+MwS7QcjBAvlEYyCegc5C09Y/
LHbTY5xZ3Y+m4Q6gLkH3LpVHz7z9M/P2C2F+fpErgUfCJzDupxBdN49cOSvkBPB7
jVaMaA==
-----END CERTIFICATE-----'''),
        'certificate_signature': TestX509CertificateSignature._full_dict,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
