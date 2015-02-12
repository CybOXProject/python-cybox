# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.mutex_object as mutex_binding
from cybox.common import ObjectProperties, String


class Mutex(ObjectProperties):
    _binding = mutex_binding
    _binding_class = mutex_binding.MutexObjectType
    _namespace = "http://cybox.mitre.org/objects#MutexObject-2"
    _XSI_NS = "MutexObj"
    _XSI_TYPE = "MutexObjectType"

    named = cybox.TypedField("named")
    name = cybox.TypedField("Name", String)
