# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.gui_window_object import GUIWindow
from cybox.test.objects import ObjectTestCase


class TestGUIWindow(ObjectTestCase, unittest.TestCase):
    object_type = "GUIWindowObjectType"
    klass = GUIWindow

    _full_dict = {
        'owner_window': u('owner window'),
        'parent_window': u('parent window'),
        'window_display_name': u('Tilte window'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
