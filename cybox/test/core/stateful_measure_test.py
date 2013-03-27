import unittest

from cybox.common import DefinedObject, String, Hash
from cybox.core import Object, StatefulMeasure
from cybox.objects.address_object import Address


class StatefulMeasureTest(unittest.TestCase):

    def test_constructor(self):
        valid_objs = [Object(), DefinedObject(), Address()]
        invalid_objs = [String("a"), Hash()]

        for o in valid_objs:
            sm = StatefulMeasure(o)

        for o in invalid_objs:
            self.assertRaises(ValueError, StatefulMeasure, o)

if __name__ == "__main__":
    unittest.main()
