import unittest

from cybox.common import DefinedObject
from cybox.core import (Object, Observable, ObservableComposition,
                        StatefulMeasure)
from cybox.objects.address_object import Address


class TestObservable(unittest.TestCase):

    def test_Observble_init(self):
        obj = Object()
        dobj = DefinedObject()
        a = Address()
        sm = StatefulMeasure()
        oc = ObservableComposition()

        obs1 = Observable(obj)
        self.assertTrue(obs1.stateful_measure)
        self.assertEqual(obs1.stateful_measure.object_, obj)
        self.assertFalse(obs1.observable_composition)

        obs2 = Observable(dobj)
        self.assertTrue(obs2.stateful_measure)
        self.assertTrue(obs2.stateful_measure.object_)
        self.assertEqual(obs2.stateful_measure.object_.defined_object, dobj)
        self.assertFalse(obs2.observable_composition)

        obs3 = Observable(a)
        self.assertTrue(obs3.stateful_measure)
        self.assertTrue(obs3.stateful_measure.object_)
        self.assertEqual(obs3.stateful_measure.object_.defined_object,a)
        self.assertFalse(obs3.observable_composition)

        obs4 = Observable(sm)
        self.assertEqual(obs4.stateful_measure, sm)
        self.assertFalse(obs4.observable_composition)

        obs5 = Observable(oc)
        self.assertFalse(obs5.stateful_measure)
        self.assertEqual(obs5.observable_composition, oc)

    def test_sm_oc_mutally_exclusive(self):
        sm = StatefulMeasure()
        oc = ObservableComposition()

        o1 = Observable(sm)
        self.assertRaises(ValueError,_set_oc, o1, oc)

        o2 = Observable(oc)
        self.assertRaises(ValueError,_set_sm, o2, sm)

        o3 = Observable()
        _set_sm(o3, sm)
        self.assertRaises(ValueError,_set_oc, o3, oc)

        o4 = Observable()
        _set_oc(o4, oc)
        self.assertRaises(ValueError,_set_sm, o4, sm)

    def test_invalid_arguments(self):
        sm = StatefulMeasure()
        oc = ObservableComposition()

        o1 = Observable()
        self.assertRaises(TypeError,_set_oc, o1, sm)
        self.assertRaises(TypeError,_set_sm, o1, oc)


def _set_sm(observable, stateful_measure):
    observable.stateful_measure = stateful_measure


def _set_oc(observable, observable_composition):
    observable.observable_composition = observable_composition


if __name__ == "__main__":
    unittest.main()
