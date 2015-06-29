# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

from mixbox.vendor.six import StringIO

class CIQAddressTests(unittest.TestCase):

    def test_can_load_ciq_extension(self):
        from cybox.bindings.extensions.location import ciq_address_3_0
        addr = ciq_address_3_0.CIQAddress3_0InstanceType()

        # Really basic test to verify the extension works.
        s = StringIO()
        addr.export(s.write, 0)
        xml = s.getvalue()
        self.assertEqual(165, len(xml))


if __name__ == "__main__":
    unittest.main()
