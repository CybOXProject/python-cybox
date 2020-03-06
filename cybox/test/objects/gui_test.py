# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from cybox.objects.gui_object import GUI
from cybox.test.objects import ObjectTestCase


class TestGUI(ObjectTestCase, unittest.TestCase):
    object_type = "GUIObjectType"
    klass = GUI

    _full_dict = {
        'height': 1024,
        'width': 768,
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
