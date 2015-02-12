# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.gui_dialogbox_object as gui_dialogbox_binding
from cybox.objects.gui_object import GUI
from cybox.common import String


class GUIDialogbox(GUI):
    _binding = gui_dialogbox_binding
    _binding_class = gui_dialogbox_binding.GUIDialogboxObjectType
    _namespace = "http://cybox.mitre.org/objects#GUIDialogboxObject-2"
    _XSI_NS = "GUIDialogBoxObj"
    _XSI_TYPE = "GUIDialogboxObjectType"

    box_caption = cybox.TypedField("Box_Caption", String)
    box_text = cybox.TypedField("Box_Text", String)
