# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_mutex_object as win_mutex_binding
from cybox.objects.mutex_object import Mutex
from cybox.objects.win_handle_object import WinHandle
from cybox.common import String


class WinMutex(Mutex):
    _binding = win_mutex_binding
    _binding_class = win_mutex_binding.WindowsMutexObjectType
    _namespace = "http://cybox.mitre.org/objects#WinMutexObject-2"
    _XSI_NS = "WinMutexObj"
    _XSI_TYPE = "WindowsMutexObjectType"

    handle = cybox.TypedField("Handle", WinHandle)
    security_attributes = cybox.TypedField("Security_Attributes", String)

