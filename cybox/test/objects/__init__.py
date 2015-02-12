# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from cybox.core import Observable

import cybox.test
import cybox.utils


class ObjectTestCase(cybox.test.EntityTestCase):
    """A base class for testing all subclasses of ObjectProperties.

    Each subclass of ObjectTestCase should subclass both unittest.TestCase
    and ObjectTestCase, and defined two class-level fields:
    - klass: the ObjectProperties subclass being tested
    - object_type: The name prefix used in the XML Schema bindings for the
      object.
    """
    def test_round_trip_dict(self):
        # We don't want to run this test on this (abstract) class
        if type(self) != type(ObjectTestCase):
            super(ObjectTestCase, self).test_round_trip_dict()

    def test_type_exists(self):
        # Verify that the correct class has been added to the metadata lists
        # in cybox.utils.nsparser

        # Skip this base class
        if type(self) == type(ObjectTestCase):
            return

        t = self.__class__.object_type

        expected_class = cybox.utils.get_class_for_object_type(t)
        actual_class = self.__class__.klass

        self.assertEqual(expected_class, actual_class)

        expected_namespace = expected_class._XSI_NS
        namespace = cybox.utils.META.lookup_object(t).namespace
        actual_namespace = cybox.utils.META.lookup_namespace(namespace).prefix
        self.assertEqual(expected_namespace, actual_namespace)

        self.assertEqual(expected_class._XSI_TYPE, t)

    def test_round_trip_observable(self):
        # Don't run this test on the base class
        if type(self) == type(ObjectTestCase):
            return

        obj = self.klass.from_dict(self._full_dict)
        observable = Observable(obj)
        observable2 = cybox.test.round_trip(observable, output=True)


    def test_object_reference(self, obj_dict=None):
        klass = self.__class__.klass

        if not obj_dict:
            obj_dict = {}

        obj_dict['object_reference'] = "some:object-reference-1"
        obj_dict['xsi:type'] = klass._XSI_TYPE

        obj_dict2 = cybox.test.round_trip_dict(klass, obj_dict)
        self.assertEqual(obj_dict, obj_dict2)
