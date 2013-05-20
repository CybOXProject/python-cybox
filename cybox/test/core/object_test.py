# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.core import Object, Observables, RelatedObject
from cybox.objects.address_object import Address
from cybox.objects.email_message_object import EmailMessage
from cybox.objects.uri_object import URI
import cybox.test


class ObjectTest(unittest.TestCase):

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
        o2 = cybox.test.round_trip(o)

        self.assertEqual(o.to_dict(), o2.to_dict())


class RelatedObjectTest(unittest.TestCase):

    def setUp(self):
        cybox.utils.set_id_method(2)
        self.ip = Address("192.168.1.1", Address.CAT_IPV4)
        self.domain = URI("example.local", URI.TYPE_DOMAIN)

    def test_inline_changes_parent_id(self):
        old_domain_parent_id = self.domain.parent.id_
        old_ip_parent_id = self.ip.parent.id_
        self.domain.add_related(self.ip, "Resolves To", inline=True)
        self.assertEqual(old_domain_parent_id, self.domain.parent.id_)
        self.assertNotEqual(old_ip_parent_id, self.ip.parent.id_)

    def test_noninline_does_not_change_parent_id(self):
        old_domain_parent_id = self.domain.parent.id_
        old_ip_parent_id = self.ip.parent.id_
        self.domain.add_related(self.ip, "Resolves To", inline=False)
        self.assertEqual(old_domain_parent_id, self.domain.parent.id_)
        self.assertEqual(old_ip_parent_id, self.ip.parent.id_)

    def test_no_relationships(self):
        self._test_round_trip(Observables([self.ip, self.domain]))

    def test_inline(self):
        self.domain.add_related(self.ip, "Resolves To", inline=True)
        o2 = self._test_round_trip(Observables(self.domain))
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the first observable, and has an inlined object with an id
        actual_id = o2.observables[0].object_.related_objects[0].id_
        self.assertEqual(expected_id, actual_id)

    def test_backward_relationship(self):
        self.domain.add_related(self.ip, "Resolves To", inline=False)

        # IP should already be known before Domain is parsed
        o2 = self._test_round_trip(Observables([self.ip, self.domain]))
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the second observable, and should only have an IDREF
        actual_id = o2.observables[1].object_.related_objects[0].idref
        self.assertEqual(expected_id, actual_id)

    def test_forward_relationship(self):
        self.domain.add_related(self.ip, "Resolves To", inline=False)

        # The "related" IP object will be encountered in the Domain object
        # before the actual IP has been seen. Make sure this doesn't break.
        o2 = self._test_round_trip(Observables([self.domain, self.ip]))
        self._test_returned_objects(o2)

        expected_id = self.ip.parent.id_
        # Domain is the second observable, and should only have an IDREF
        actual_id = o2.observables[0].object_.related_objects[0].idref
        self.assertEqual(expected_id, actual_id)

    def test_missing_related_object(self):
        self.domain.add_related(self.ip, "Resolves To", inline=False)

        # If we only include the domain, the dereference will fail.
        o2 = self._test_round_trip(Observables([self.domain]))

        rel_obj = o2.observables[0].object_.related_objects[0]
        self.assertRaises(cybox.utils.CacheMiss, rel_obj.get_properties)

    def _test_round_trip(self, observables):
        self.maxDiff = None
        print observables.to_xml()
        observables2 = cybox.test.round_trip(observables)
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

if __name__ == "__main__":
    unittest.main()
