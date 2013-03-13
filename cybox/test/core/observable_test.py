import unittest

from cybox.core import Observable, StatefulMeasure


class TestObservable(unittest.TestCase):

    def test_create_observable_from_sm(self):
        s = StatefulMeasure()
        o = Observable(s)


if __name__ == "__main__":
    unittest.main()
