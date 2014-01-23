# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.common import MeasureSource, ObjectProperties, StructuredText
from cybox.core import (Event, Object, Observable, ObservableComposition,
        Observables)
from cybox.objects.address_object import Address
import cybox.test


class TestObservable(unittest.TestCase):

    def test_observable_id(self):
        o = Observable()
        self.assertTrue("Observable" in o.id_)

    def test_observble_init(self):
        obj = Object()
        dobj = ObjectProperties()
        a = Address()
        oc = ObservableComposition()
        e = Event()

        obs1 = Observable(obj)
        self.assertTrue(obs1.object_ is obj)
        self.assertFalse(obs1.observable_composition)
        self.assertFalse(obs1.event)

        obs2 = Observable(dobj)
        self.assertTrue(obs2.object_)
        self.assertTrue(obs2.object_.properties is dobj)
        self.assertFalse(obs2.observable_composition)
        self.assertFalse(obs2.event)

        obs3 = Observable(a)
        self.assertTrue(obs3.object_)
        self.assertTrue(obs3.object_.properties is a)
        self.assertFalse(obs3.event)
        self.assertFalse(obs3.observable_composition)

        obs4 = Observable(oc)
        self.assertFalse(obs4.object_)
        self.assertFalse(obs4.event)
        self.assertTrue(obs4.observable_composition is oc)

        obs5 = Observable(e)
        self.assertFalse(obs5.object_)
        self.assertTrue(obs5.event is e)
        self.assertFalse(obs5.observable_composition)

    def test_obj_oc_mutally_exclusive(self):
        obj = Object()
        oc = ObservableComposition()
        e = Event()

        o1 = Observable(obj)
        self.assertRaises(ValueError, _set_event, o1, e)
        self.assertRaises(ValueError, _set_oc, o1, oc)

        o5 = Observable(e)
        self.assertRaises(ValueError, _set_obj, o5, obj)
        self.assertRaises(ValueError, _set_oc, o5, oc)

        o2 = Observable(oc)
        self.assertRaises(ValueError, _set_obj, o2, obj)
        self.assertRaises(ValueError, _set_event, o2, e)

        o3 = Observable()
        _set_obj(o3, obj)
        self.assertRaises(ValueError, _set_event, o3, e)
        self.assertRaises(ValueError, _set_oc, o3, oc)

        o6 = Observable()
        _set_event(o6, e)
        self.assertRaises(ValueError, _set_obj, o6, obj)
        self.assertRaises(ValueError, _set_oc, o6, oc)

        o4 = Observable()
        _set_oc(o4, oc)
        self.assertRaises(ValueError, _set_obj, o4, obj)
        self.assertRaises(ValueError, _set_event, o4, e)

    def test_invalid_arguments(self):
        obj = Object()
        e = Event()
        oc = ObservableComposition()

        o1 = Observable()
        self.assertRaises(TypeError, _set_event, o1, obj)
        self.assertRaises(TypeError, _set_oc, o1, obj)
        self.assertRaises(TypeError, _set_obj, o1, e)
        self.assertRaises(TypeError, _set_oc, o1, e)
        self.assertRaises(TypeError, _set_obj, o1, oc)
        self.assertRaises(TypeError, _set_event, o1, oc)

    def test_round_trip(self):
        o = Observable()
        o.title = "An observable"
        o.description = "some text"
        o.description.structuring_format = "plain"
        o.id_ = "abc123"
        o.object_ = Object()

        o2 = cybox.test.round_trip(o)
        self.assertEqual(o.to_dict(), o2.to_dict())


def _set_obj(observable, object_):
    observable.object_ = object_


def _set_oc(observable, observable_composition):
    observable.observable_composition = observable_composition


def _set_event(observable, event):
    observable.event = event


class ObservablesTest(unittest.TestCase):

    def test_round_trip(self):
        a = Address("test@example.com", Address.CAT_EMAIL)
        a2 = Address("test2@example.com", Address.CAT_EMAIL)

        ms = MeasureSource()
        ms.class_ = "System"
        ms.source_type = "Analysis"
        ms.description = StructuredText("A Description")

        o = Observables([a, a2])
        o.observable_package_source = ms

        o2 = cybox.test.round_trip(o, output=True)
        self.assertEqual(o.to_dict(), o2.to_dict())

if __name__ == "__main__":
    unittest.main()
