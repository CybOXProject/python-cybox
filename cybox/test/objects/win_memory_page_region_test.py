# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.win_memory_page_region_object import WinMemoryPageRegion

from cybox.compat import long
from cybox.test.common.hash_test import EMPTY_MD5
from cybox.test.common.extracted_features_test import TestExtractedFeatures
from cybox.test.objects import ObjectTestCase


class TestWinMemoryPageRegion(ObjectTestCase, unittest.TestCase):
    object_type = "WindowsMemoryPageRegionObjectType"
    klass = WinMemoryPageRegion

    _full_dict = {
        'is_injected': True,
        'is_mapped': False,
        'is_protected': True,
        'is_volatile': False,
        'name': u("A page region"),
        'memory_source': u("A source"),
        'region_size': long(10000),
        'block_type': u("A block type"),
        'region_start_address': u("1234abcde"),
        'region_end_address': u("1234abdde"),
        'allocation_base_address': u("1234abbbe"),
        'type': u("A type"),
        'allocation_protect': u("allocate protection"),
        'state': u("A state"),
        'protect': u("protection"),
        'extracted_features': TestExtractedFeatures._full_dict,
        'hashes': [
            {'type': u("MD5"), 'simple_hash_value': EMPTY_MD5}
        ],
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
