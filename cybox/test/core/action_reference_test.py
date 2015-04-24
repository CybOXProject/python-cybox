# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.core import ActionReference
from cybox.test import EntityTestCase


class TestActionReference(EntityTestCase, unittest.TestCase):
    klass = ActionReference
    _full_dict = {
        'action_id': "example:Action-1",
    }

    def test_construction(self):
        aref = ActionReference(action_id="example:Action-1")
        print aref.to_xml()
        print aref.to_dict()
        self.assertTrue("example:Action-1" in aref.to_xml())
        self.assertTrue("example:Action-1" in aref.to_json())


if __name__ == "__main__":
    unittest.main()
