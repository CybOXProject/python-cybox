# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.port_object import Port
import cybox.test
from cybox.test.objects import ObjectTestCase


class TestPort(unittest.TestCase, ObjectTestCase):
    object_type = "PortObjectType"
    klass = Port

    def test_round_trip(self):
        port_dict = {'port_value': 80,
                     'layer4_protocol': 'TCP',
                     'xsi:type': 'PortObjectType'}
        port_dict2 = cybox.test.round_trip_dict(Port, port_dict)
        self.assertEqual(port_dict, port_dict2)


if __name__ == "__main__":
    unittest.main()
