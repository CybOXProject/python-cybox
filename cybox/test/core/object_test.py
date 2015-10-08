# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import logging
import unittest

from mixbox.vendor.six import u
from cybox.core import Object, Observables, RelatedObject
from cybox.objects.address_object import Address
from cybox.objects.uri_object import URI
from cybox.test import EntityTestCase, round_trip, round_trip_dict
from cybox.utils import CacheMiss

logger = logging.getLogger(__name__)


class ObjectTest(EntityTestCase, unittest.TestCase):
    klass = Object

    _full_dict = {
        'id': "example:Object-1",
        'properties': {
            'file_name': u("example.txt"),
            'xsi:type': "FileObjectType"
        },
        'related_objects': [
            {
                'idref': "example:Object-2",
                'relationship': u("Same As"),
            },
        ],
    }

    def test_id_autoset(self):
        o = Object()
        self.assertNotEqual(o.id_, None)

    def test_id_prefix(self):
        a = Address()
        o = Object(a)
        self.assertTrue("Address" in o.id_)

    def test_round_trip(self):
        o = Object()
        o.idref = "example:a1"
        o.properties = Address("1.2.3.4", Address.CAT_IPV4)
        o2 = round_trip(o)

        self.assertEqual(o.to_dict(), o2.to_dict())


class RelatedObjectTest(EntityTestCase, unittest.TestCase):
    klass = RelatedObject

    _full_dict = {
        'id': "example:Object-1",
        'relationship': u("Created"),
    }

    def setUp(self):
        self.ip = Address("192.168.1.1", Address.CAT_IPV4)
        self.domain = URI("example.local", URI.TYPE_DOMAIN)

    def test_inline_changes_parent_id(self):
        old_domain_parent_id = self.domain.parent.id_
        old_ip_parent_id = self.ip.parent.id_
        self.domain.add_related(self.ip, "Resolved_To", inline=True)
        self.assertEqual(old_domain_parent_id, self.domain.parent.id_)
        self.assertNotEqual(old_ip_parent_id, self.ip.parent.id_)

    def test_noninline_does_not_change_parent_id(self):
        old_domain_parent_id = self.domain.parent.id_
        old_ip_parent_id = self.ip.parent.id_
        self.domain.add_related(self.ip, "Resolved_To", inline=False)
        self.assertEqual(old_domain_parent_id, self.domain.parent.id_)
        self.assertEqual(old_ip_parent_id, self.ip.parent.id_)

    def test_no_relationships(self):
        self._test_round_trip(Observables([self.ip, self.domain]))

    def test_inline(self):
        self.domain.add_related(self.ip, "Resolved_To", inline=True)
        o2 = self._test_round_trip(Observables(self.domain))
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the first observable, and has an inlined object with an id
        actual_id = o2.observables[0].object_.related_objects[0].id_
        self.assertEqual(expected_id, actual_id)

    def test_backward_relationship(self):
        self.domain.add_related(self.ip, "Resolved_To", inline=False)

        # IP should already be known before Domain is parsed
        o2 = self._test_round_trip(Observables([self.ip, self.domain]))
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the second observable, and should only have an IDREF
        actual_id = o2.observables[1].object_.related_objects[0].idref
        self.assertEqual(expected_id, actual_id)

    def test_forward_relationship(self):
        self.domain.add_related(self.ip, "Resolved_To", inline=False)
        o1 = Observables([self.domain, self.ip])

        # The "related" IP object will be encountered in the Domain object
        # before the actual IP has been seen. Make sure this doesn't break.
        o2 = self._test_round_trip(o1)
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the second observable, and should only have an IDREF
        actual_id = o2.observables[0].object_.related_objects[0].idref
        self.assertEqual(expected_id, actual_id)

    def test_missing_related_object(self):
        self.domain.add_related(self.ip, "Resolved_To", inline=False)

        # If we only include the domain, the dereference will fail.
        o2 = self._test_round_trip(Observables([self.domain]))

        rel_obj = o2.observables[0].object_.related_objects[0]
        self.assertRaises(CacheMiss, rel_obj.get_properties)

    def test_relationship_standard_xsitype(self):
        d = {
            'id': "example:Object-1",
            'relationship': u("Created"),
        }
        self._test_round_trip_dict(d)

    def test_relationship_nonstandard_xsitype(self):
        d = {
            'id': "example:Object-1",
            'relationship': {
                'value': u("Created"),
                'xsi:type': "Foo",
            }
        }
        self._test_round_trip_dict(d)

    def test_relationship_vocabnameref(self):
        d = {
            'id': "example:Object-1",
            'relationship': {
                'value': u("Created"),
                'vocab_name': "Foo",
                'vocab_reference': "http://example.com/FooVocab",
            }
        }
        self._test_round_trip_dict(d)

    def _test_round_trip(self, observables):
        self.maxDiff = None
        logger.info(observables.to_xml())
        observables2 = round_trip(observables)
        self.assertEqual(observables.to_dict(), observables2.to_dict())

        return observables2

    def _test_returned_objects(self, o2):
        # Get the Domain object (ID will contain "URI")
        for obs in o2.observables:
            if "URI" in obs.object_.id_:
                ip_obj = obs.object_.related_objects[0]
                break

        # Check that the properties are identical
        self.assertEqual(self.ip.to_dict(), ip_obj.get_properties().to_dict())

    def _test_round_trip_dict(self, d):
        d2 = round_trip_dict(RelatedObject, d)
        self.maxDiff = None
        self.assertEqual(d, d2)


if __name__ == "__main__":
    unittest.main()
