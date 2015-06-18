# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_semaphore_object as semaphore_binding
from cybox.common import String
from cybox.objects.win_handle_object import WinHandle
from cybox.objects.semaphore_object import Semaphore


class WinSemaphore(Semaphore):
    _binding = semaphore_binding
    _binding_class = semaphore_binding.WindowsSemaphoreObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinSemaphoreObject-2'
    _XSI_NS = "WinSemaphoreObj"
    _XSI_TYPE = "WindowsSemaphoreObjectType"

    handle = fields.TypedField("Handle", WinHandle)
    security_attributes = fields.TypedField("Security_Attributes", String)
