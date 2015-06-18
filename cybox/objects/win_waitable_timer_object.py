# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_waitable_timer_object as win_waitable_timer_binding
from cybox.common import String, ObjectProperties


class WinWaitableTimer(ObjectProperties):
    _binding = win_waitable_timer_binding
    _binding_class = win_waitable_timer_binding.WindowsWaitableTimerObjectType
    _namespace = "http://cybox.mitre.org/objects#WinWaitableTimerObject-2"
    _XSI_NS = "WinWaitableTimerObj"
    _XSI_TYPE = "WindowsWaitableTimerObjectType"

    security_attributes = fields.TypedField("Security_Attributes", String)
    name = fields.TypedField("Name", String)
    type_ = fields.TypedField("Type", String)
