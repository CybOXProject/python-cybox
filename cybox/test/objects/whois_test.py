import unittest

from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI
from cybox.objects.whois_object import WhoisEntry
import cybox.test


class TestWhois(unittest.TestCase, cybox.test.objects.ObjectTestCase):
    object_type = "WhoisObjectType"
    klass = WhoisEntry

    def test_round_trip(self):
        whois_dict = {
                        'domain_name': {'value': "www.example.com",
                                        'type': URI.TYPE_DOMAIN},
                        'domain_id': 'test_id',
                        'server_name': {'value': "whois.example.com",
                                        'type': URI.TYPE_DOMAIN},
                        'ip_address': {'address_value': '1.2.3.4',
                                       'category': Address.CAT_IPV4},
                        'dnssec': WhoisEntry.DNSSEC_SIGNED,
                        'nameservers': [{'value': "ns1.example.com",
                                         'type': URI.TYPE_DOMAIN},
                                        {'value': "ns2.example.com",
                                         'type': URI.TYPE_DOMAIN}],
                        'status': ['OK', 'PENDING_RESTORE', 'CLIENT_HOLD'],
                        'updated_date': "2012-05-03T14:49:00-04:00",
                        'creation_date': "2010-05-03T07:49:00-04:00",
                        'expiration_date': "2015-05-03T04:49:00-04:00",

                        'sponsoring_registrar': "SRegistrar",
                     }

        whois_dict2 = cybox.test.round_trip_dict(WhoisEntry, whois_dict)
        cybox.test.assert_equal_ignore(whois_dict, whois_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
