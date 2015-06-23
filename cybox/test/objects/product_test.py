# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.product_object import Product
from cybox.test.objects import ObjectTestCase


class TestProduct(ObjectTestCase, unittest.TestCase):
    object_type = "ProductObjectType"
    klass = Product

    _full_dict = {
        'edition': "First",
        'language': "English",
        'product': "Test Product",
        'update': "Test Update",
        'vendor': "Test Vendor",
        'version': "1.2.3.4",
        'device_details': {
            'xsi:type': "LinkObjectType",  # pick some random object type
            'url_label': "http://www.google.com/",
        },
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
