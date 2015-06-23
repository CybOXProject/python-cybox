# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.common import ExtractedFeatures
from cybox.objects.address_object import Address
from cybox.test import EntityTestCase

# Need to do this so the binding class is registered.
import cybox.bindings.cybox_common
from cybox.bindings.address_object import AddressObjectType
setattr(cybox.bindings.cybox_common, "AddressObjectType", AddressObjectType)

class TestExtractedFeatures(EntityTestCase, unittest.TestCase):
    klass = ExtractedFeatures

    _full_dict = {
        'strings': [
            {'encoding': u("ASCII"), 'string_value': u("A String"), 'length': 8},
            {'encoding': u("UTF-8"), 'string_value': u("Another String")},
        ],
        'imports': [u("CreateFileA"), u("LoadLibrary")],
        'functions': [u("DoSomething"), u("DoSomethingElse")],
        #TODO: Use CodeObject instead of AddressObject
        'code_snippets': [
            {
                'address_value': u("8.8.8.8"),
                'category': Address.CAT_IPV4,
                'xsi:type': "AddressObjectType"
            },
            {
                'address_value': u("1.2.3.4"),
                'category': Address.CAT_IPV4,
                'xsi:type': "AddressObjectType"
            },
        ],
    }


if __name__ == "__main__":
    unittest.main()
