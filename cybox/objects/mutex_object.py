# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.mutex_object as mutex_binding
from cybox.common import ObjectProperties, String


class Mutex(ObjectProperties):
    _binding = mutex_binding
    _binding_class = mutex_binding.MutexObjectType
    _namespace = "http://cybox.mitre.org/objects#MutexObject-2"
    _XSI_NS = "MutexObj"
    _XSI_TYPE = "MutexObjectType"

    named = fields.TypedField("named")
    name = fields.TypedField("Name", String)
