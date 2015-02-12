# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_critical_section_object as win_critical_section_binding
from cybox.common import ObjectProperties, HexBinary, NonNegativeInteger

class WinCriticalSection(ObjectProperties):
    _binding = win_critical_section_binding
    _binding_class = win_critical_section_binding.WindowsCriticalSectionObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinCriticalSectionObject-2'
    _XSI_NS = "WinCriticalSectionObj"
    _XSI_TYPE = "WindowsCriticalSectionObjectType"

    address = cybox.TypedField("Address", HexBinary)
    spin_count = cybox.TypedField("Spin_Count", NonNegativeInteger)
