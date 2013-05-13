# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import uuid

from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI
from cybox.objects.whois_object import WhoisEntry, WhoisContact, WhoisRegistrar, WhoisRegistrant
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
                        'regional_internet_registry': "ARIN",
                        'sponsoring_registrar': "SRegistrar",
                        'registrar_info': {'registrar_id': "aaa111",
                                           'name': "Awesome Registrar",
                                           'whois_server': {'value': "whois.example.com",
                                                            'type': URI.TYPE_DOMAIN},
                                          },
                        'registrants': [{'name': "Registrant1",
                                         'registrant_id': "R_ID_1"},
                                        {'name': "Registrant2",
                                         'registrant_id': "R_ID_2"}],
                        'contact_info': {'contact_type': "ADMIN",
                                         'name': "John Smith"},
                     }

        whois_dict2 = cybox.test.round_trip_dict(WhoisEntry, whois_dict)
        cybox.test.assert_equal_ignore(whois_dict, whois_dict2, ['xsi:type'])


class TestContact(unittest.TestCase):

    def test_round_trip(self):
        contact_dict = {
                            'contact_type': "ADMIN",
                            'contact_id': "abc123",
                            'name': "John Smith",
                            'email_address': {'address_value': "john@smith.com",
                                              'category': Address.CAT_EMAIL},
                            'phone_number': "(800) 555-1212",
                            'address': "123 Main St.\nAnytown, CA 01234",
                       }

        contact_dict2 = cybox.test.round_trip_dict(WhoisContact, contact_dict)
        cybox.test.assert_equal_ignore(contact_dict, contact_dict2, ['xsi:type'])

    def test_parse_email_address(self):
        contact_dict = {'contact_type': "ADMIN",
                        'email_address': "admin@example.com"}

        c = WhoisContact.from_dict(contact_dict)
        self.assertEqual("ADMIN", c.contact_type)
        self.assertEqual("admin@example.com", c.email_address.address_value)
        self.assertEqual(Address.CAT_EMAIL, c.email_address.category)


class TestRegistrant(unittest.TestCase):

    def test_round_trip(self):
        registrant_dict = {
                            'contact_type': "ADMIN",
                            'name': "John Smith",
                            'registrant_id': "reg1234",
                          }

        registrant_dict2 = cybox.test.round_trip_dict(WhoisRegistrant, registrant_dict)
        self.assertEqual(registrant_dict, registrant_dict2)


class TestRegistrar(unittest.TestCase):

    def test_round_trip(self):
        registrar_dict = {
                            'registrar_id': "aaa111",
                            'registrar_guid': str(uuid.uuid4()),
                            'name': "Awesome Registrar",
                            'address': "123 Market St.\nSometown, CA 98765",
                            'email_address': {'address_value': "awesomeregistrar@example.com",
                                              'category': Address.CAT_EMAIL},
                            'phone_number': "(800) 555-1212",
                            'whois_server': {'value': "whois.example.com",
                                             'type': URI.TYPE_DOMAIN},
                            'referral_url': {'value': "http://www.example.com/referral",
                                             'type': URI.TYPE_GENERAL},
                            'contacts': [{'contact_type': "ADMIN",
                                          'name': "John Smith"},
                                         {'contact_type': "BILLING",
                                          'name': "Bob Smith"}],

                       }

        registrar_dict2 = cybox.test.round_trip_dict(WhoisRegistrar, registrar_dict)
        cybox.test.assert_equal_ignore(registrar_dict, registrar_dict2, ['xsi:type'])


if __name__ == "__main__":
    unittest.main()
