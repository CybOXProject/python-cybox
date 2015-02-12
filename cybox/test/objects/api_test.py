# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.api_object import API

from cybox.test import EntityTestCase, round_trip
from cybox.test.objects import ObjectTestCase


class TestAPI(ObjectTestCase, unittest.TestCase):
    object_type = "APIObjectType"
    klass = API

    _full_dict = {
        'description': "Some API",
        'function_name': "someTestFunction",
        'normalized_function_name': "some_test_function",
        'platform': {
            'description': "Test Platform"
        },
        'address': "876cdbeb87cd8e7",
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
