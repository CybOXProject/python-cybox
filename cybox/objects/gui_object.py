# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.gui_object as gui_binding
from cybox.common import ObjectProperties, Integer


class GUI(ObjectProperties):
    _binding = gui_binding
    _binding_class = gui_binding.GUIObjectType
    _namespace = "http://cybox.mitre.org/objects#GUIObject-2"
    _XSI_NS = "GUIObj"
    _XSI_TYPE = "GUIObjectType"

    height = fields.TypedField("Height", Integer)
    width = fields.TypedField("Width", Integer)
