# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.custom_object import Custom
from cybox.test.objects import ObjectTestCase


class TestCustom(ObjectTestCase, unittest.TestCase):
    object_type = "CustomObjectType"
    klass = Custom

    _full_dict = {
        'custom_name': u("SuperCustomizedObjectName"),
        'description': "Some description of the custom object",
        'custom_properties': [
            {'name': "Property #1", 'description': "A First Property", 'value': "12345"},
            {'name': "Property #2", 'description': "A Second Property", 'value': "true"},
        ],
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
