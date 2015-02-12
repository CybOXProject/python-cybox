# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.gui_window_object as gui_window_binding
from cybox.objects.gui_object import GUI
from cybox.common import String


class GUIWindow(GUI):
    _binding = gui_window_binding
    _binding_class = gui_window_binding.GUIWindowObjectType
    _namespace = "http://cybox.mitre.org/objects#GUIWindowObject-2"
    _XSI_NS = "GUIWindowObj"
    _XSI_TYPE = "GUIWindowObjectType"

    owner_window = cybox.TypedField("Owner_Window", String)
    parent_window = cybox.TypedField("Parent_Window", String)
    window_display_name = cybox.TypedField("Window_Display_Name", String)
