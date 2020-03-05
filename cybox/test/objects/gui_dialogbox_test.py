# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import u

from cybox.objects.gui_dialogbox_object import GUIDialogbox
from cybox.test.objects import ObjectTestCase


class TestGUIDialogbox(ObjectTestCase, unittest.TestCase):
    object_type = "GUIDialogboxObjectType"
    klass = GUIDialogbox

    _full_dict = {
        'box_caption': u('Sample caption'),
        'box_text': u('Sample text'),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
