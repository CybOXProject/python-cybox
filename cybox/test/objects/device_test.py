# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.device_object import Device
from cybox.test.objects import ObjectTestCase


class TestAccount(ObjectTestCase, unittest.TestCase):
    object_type = "DeviceObjectType"
    klass = Device

    _full_dict = {
        'description': "Just a description",
        'device_type': "GPU",
        'manufacturer': "NVIDIA",
        'model': "GTX 670",
        'serial_number': "412984-124123-test",
        'firmware_version': "v2",
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
