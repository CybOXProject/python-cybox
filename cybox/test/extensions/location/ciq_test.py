# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

from mixbox.binding_utils import etree_
from mixbox.vendor.six import StringIO


class CIQAddressTests(unittest.TestCase):

    def test_can_load_extension(self):
        if etree_.LXML_VERSION < (2, 3, 0, 0):
            # Older versions of LXML do not support `register_namespace` needed
            # for CybOX extensions to work. This is only an issue during RHEL6
            # tests, which also use Python 2.6, meaning that unittest.skipTest
            # is not implemented. So we just 'return' here.
            return
            # self.skipTest("LXML >= 2.3 required to use extensions")

        from cybox.bindings.extensions.location import ciq_address_3_0
        addr = ciq_address_3_0.CIQAddress3_0InstanceType()

        # Really basic test to verify the extension works.
        s = StringIO()
        addr.export(s.write, 0)
        xml = s.getvalue()
        self.assertEqual(165, len(xml))


if __name__ == "__main__":
    unittest.main()
