# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import uuid

from mixbox.vendor.six import u

from cybox.bindings.cybox_common import StringObjectPropertyType
from cybox.bindings.whois_object import (WhoisContactType,
        WhoisRegistrantInfoType)

from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI
from cybox.objects.whois_object import (WhoisEntry, WhoisContact,
        WhoisRegistrar, WhoisRegistrant)
from cybox.test import EntityTestCase
from cybox.test.objects import ObjectTestCase


class TestWhois(ObjectTestCase, unittest.TestCase):
    object_type = "WhoisObjectType"
    klass = WhoisEntry

    _full_dict = {
        'domain_name': {
            'value': "www.example.com",
            'type': URI.TYPE_DOMAIN,
            'xsi:type': "URIObjectType",
        },
        'domain_id': 'test_id',
        'server_name': {
            'value': "whois.example.com",
            'type': URI.TYPE_DOMAIN,
            'xsi:type': "URIObjectType",
        },
        'ip_address': {
            'address_value': '1.2.3.4',
            'category': Address.CAT_IPV4,
            'xsi:type': "AddressObjectType"
        },
        'dnssec': WhoisEntry.DNSSEC_SIGNED,
        'nameservers': [
            {
                'value': "ns1.example.com",
                'type': URI.TYPE_DOMAIN,
                'xsi:type': "URIObjectType",
            },
            {
                'value': "ns2.example.com",
                'type': URI.TYPE_DOMAIN,
                'xsi:type': "URIObjectType",
            },
        ],
        'status': ['OK', 'PENDING_RESTORE', 'CLIENT_HOLD'],
        'updated_date': "2012-05-03",
        'creation_date': "2010-05-04",
        'expiration_date': "2015-05-05",
        'regional_internet_registry': "ARIN",
        'sponsoring_registrar': "SRegistrar",
        'registrar_info': {
            'registrar_id': "aaa111",
            'name': "Awesome Registrar",
            'whois_server': {
                'value': "whois.example.com",
                'type': URI.TYPE_DOMAIN,
                'xsi:type': "URIObjectType",
            },
        },
        'registrants': [
            {
                'name': "Registrant1",
                'registrant_id': "R_ID_1",
            },
            {
                'name': "Registrant2",
                'registrant_id': "R_ID_2",
            },
        ],
        'contact_info': {
            'contact_type': "ADMIN",
            'name': "John Smith"
        },
        'xsi:type': object_type,
    }


class TestContact(EntityTestCase, unittest.TestCase):
    klass = WhoisContact

    _full_dict = {
        'contact_type': "ADMIN",
        'contact_id': u("abc123"),
        'name': u("John Smith"),
        'email_address': {
            'address_value': u("john@smith.com"),
            'category': Address.CAT_EMAIL,
            'xsi:type': "AddressObjectType",
        },
        'phone_number': u("(800) 555-1212"),
        'fax_number': u("(800) 555-1200"),
        'address': u("123 Main St.\nAnytown, CA 01234"),
        'organization': u("XYZ Hosting"),
    }

    def test_parse_email_address(self):
        contact_dict = {'contact_type': "ADMIN",
                        'email_address': "admin@example.com"}

        c = WhoisContact.from_dict(contact_dict)
        self.assertEqual("ADMIN", c.contact_type)
        self.assertEqual("admin@example.com", c.email_address.address_value)
        self.assertEqual(Address.CAT_EMAIL, c.email_address.category)


class TestRegistrant(EntityTestCase, unittest.TestCase):
    klass = WhoisRegistrant

    _full_dict = {
        'contact_type': "ADMIN",
        'name': "John Smith",
        'registrant_id': "reg1234",
    }

    # https://github.com/CybOXProject/python-cybox/issues/227
    def test_issue_227_binding_init(self):
        # Fax_Number and Organization were added to the __init__ method of
        # WhoisContactType, but not to its subclass (WhoisRegistrantType). Once
        # the objects are constructed, they should have equivalent dictionary
        # represesntations (as long as the extra fields in the subclass are not
        # present).
        contact_obj = WhoisContactType(
            contact_type="ADMIN",
            Contact_ID=StringObjectPropertyType(valueOf_="abc123"),
            Fax_Number=StringObjectPropertyType(valueOf_=u("(800) 555-1200")),
            Organization=StringObjectPropertyType(valueOf_=u("XYZ Hosting")),
        )
        contact = WhoisContact.from_obj(contact_obj)

        reg_obj = WhoisRegistrantInfoType(
            contact_type="ADMIN",
            Contact_ID=StringObjectPropertyType(valueOf_="abc123"),
            Fax_Number=StringObjectPropertyType(valueOf_=u("(800) 555-1200")),
            Organization=StringObjectPropertyType(valueOf_=u("XYZ Hosting")),
        )
        registrant = WhoisRegistrant.from_obj(reg_obj)

        self.assertEqual(contact.to_dict(), registrant.to_dict())


class TestRegistrar(EntityTestCase, unittest.TestCase):
    klass = WhoisRegistrar

    _full_dict = {
        'registrar_id': "aaa111",
        'registrar_guid': str(uuid.uuid4()),
        'name': "Awesome Registrar",
        'address': "123 Market St.\nSometown, CA 98765",
        'email_address': {
            'address_value': "awesomeregistrar@example.com",
            'category': Address.CAT_EMAIL,
            'xsi:type': "AddressObjectType",
        },
        'phone_number': "(800) 555-1212",
        'whois_server': {
            'value': "whois.example.com",
            'type': URI.TYPE_DOMAIN,
            'xsi:type': "URIObjectType",
        },
        'referral_url': {
            'value': "http://www.example.com/referral",
            'type': URI.TYPE_GENERAL,
            'xsi:type': "URIObjectType",
        },
        'contacts': [
            {
                'contact_type': "ADMIN",
                'name': "John Smith"
            },
            {
                'contact_type': "BILLING",
                'name': "Bob Smith"
            }
        ],
    }


if __name__ == "__main__":
    unittest.main()
