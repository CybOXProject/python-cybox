# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import logging
import unittest

from mixbox.vendor.six import u

from cybox.common import MeasureSource, ObjectProperties, String, StructuredText
from cybox.core import (Event, Object, Observable, ObservableComposition,
        Observables, PatternFidelity, ObfuscationTechniques,
        ObfuscationTechnique)
from cybox.objects.address_object import Address
from cybox.test import EntityTestCase, round_trip

logger = logging.getLogger(__name__)


class TestObservable(EntityTestCase, unittest.TestCase):
    klass = Observable
    _full_dict = {
        'id': "example:Observable-1",
        'title': "An Observable",
        'description': "A longer description of the observable",
        'keywords': [
            "DANGER!",
            "External",
        ],
        'object': {
            'properties': {
                'file_name': u("example.txt"),
                'xsi:type': "FileObjectType"
            },
        },
        'sighting_count': 2,
        'observable_source': [{
            'name': "ObservingTool",
        }],
        'pattern_fidelity':
            {'evasion_techniques':
                 [{'description':'XOR'}]}
    }

    def test_keywords(self):
        o = Observable()
        o.title = "Test"

        self.assertTrue(b"eyword" not in o.to_xml())
        o.add_keyword("Foo")
        logger.info(o.to_xml())
        self.assertTrue(b"<cybox:Keyword>Foo</cybox:Keyword>" in o.to_xml())

        o2 = round_trip(o)
        self.assertEqual(1, len(o2.keywords))

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

        pf = PatternFidelity()
        ot = ObfuscationTechnique()
        ot.description = "X0Rz"
        pf.evasion_techniques = ObfuscationTechniques()
        pf.evasion_techniques.append(ot)
        o.pattern_fidelity = pf

        o2 = round_trip(o)
        self.assertEqual(o.to_dict(), o2.to_dict())

    def test_id_idref_exclusive(self):
        o = Observable()
        self.assertTrue(o.id_ is not None)
        self.assertTrue(o.idref is None)

        o.idref = "foo"
        self.assertTrue(o.idref is not None)
        self.assertTrue(o.id_ is None)


    # https://github.com/CybOXProject/python-cybox/issues/239
    def test_observable_init(self):
        # Can pass an Object into the Observable constructor
        o = Object()
        obs = Observable(o)

        # Can pass an Event into the Observable constructor
        e = Event()
        obs = Observable(e)

        # Can pass an ObservableComposition into the Observable constructor
        oc = ObservableComposition()
        obs = Observable(oc)

        # Can pass an ObjectProperties subclass into the Observable constructor
        a = Address()
        obs = Observable(a)

        # Cannot pass a String into the Observable constructor.
        s = String()
        self.assertRaises(TypeError, Observable, s)


def _set_obj(observable, object_):
    observable.object_ = object_


def _set_oc(observable, observable_composition):
    observable.observable_composition = observable_composition


def _set_event(observable, event):
    observable.event = event


class TestObservables(EntityTestCase, unittest.TestCase):
    klass = Observables
    _full_dict = {
        'major_version': 2,
        'minor_version': 1,
        'update_version': 0,
        'observables': [
            {
                'id': "example:Observable-1",
                'title': "An Observable",
                'description': "A longer description of the observable",
                'object': {
                    'properties': {
                        'file_name': u("example.txt"),
                        'xsi:type': "FileObjectType"
                    },
                },
            }
        ],
        'observable_package_source': {
            'name': "The Source",
            'information_source_type': u("Logs"),
        },
    }

    # https://github.com/CybOXProject/python-cybox/issues/232
    def test_list_behavior(self):
        obs = Observables.from_dict(self._full_dict)

        self.assertEqual(1, len(obs))
        self.assertTrue(obs[0] is not None)
        self.assertRaises(IndexError, obs.__getitem__, 1)
        self.assertEqual("example.txt", obs[0].object_.properties.file_name)

        self.assertEqual(self._full_dict, obs.to_dict())
        # When calling to_list, only the observables themselves are returned.
        self.assertEqual(self._full_dict['observables'], obs.to_list())

        # Even when using append, an Address automatically gets wrapped in an
        # Object and an Observable.
        obs.append(Address("test@example.com", Address.CAT_EMAIL))
        self.assertEqual(2, len(obs))
        self.assertEqual(Observable, type(obs[1]))
        self.assertEqual(Address.CAT_EMAIL, obs[1].object_.properties.category)

    def test_round_trip(self):
        a = Address("test@example.com", Address.CAT_EMAIL)
        a2 = Address("test2@example.com", Address.CAT_EMAIL)

        ms = MeasureSource()
        ms.class_ = "System"
        ms.source_type = "Analysis"
        ms.description = StructuredText("A Description")

        o = Observables([a, a2])
        o.observable_package_source = ms

        o2 = round_trip(o, output=True)
        self.assertEqual(o.to_dict(), o2.to_dict())

    def test_observables_len(self):
        a = Address("test@example.com", Address.CAT_EMAIL)
        a2 = Address("test2@example.com", Address.CAT_EMAIL)

        o = Observables([a, a2])
        self.assertEqual(2, len(o))

    def test_observable_iterable(self):
        a = Address("test@example.com", Address.CAT_EMAIL)
        a2 = Address("test2@example.com", Address.CAT_EMAIL)

        o = Observables([a, a2])
        for obs in o:
            self.assertTrue(obs.object_.properties in [a, a2])


if __name__ == "__main__":
    unittest.main()
