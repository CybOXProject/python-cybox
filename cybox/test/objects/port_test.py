# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.port_object import Port
from cybox.test.objects import ObjectTestCase


class TestPort(ObjectTestCase, unittest.TestCase):
    object_type = "PortObjectType"
    klass = Port

    _full_dict = {
        'port_value': 80,
        'layer4_protocol': 'TCP',
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
