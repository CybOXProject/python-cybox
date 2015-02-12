# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.semaphore_object as semaphore_binding
from cybox.common import (ObjectProperties, String, UnsignedInteger,
                          PositiveInteger)


class Semaphore(ObjectProperties):
    _binding = semaphore_binding
    _binding_class = semaphore_binding.SemaphoreObjectType
    _namespace = 'http://cybox.mitre.org/objects#SemaphoreObject-2'
    _XSI_NS = "SemaphoreObj"
    _XSI_TYPE = "SemaphoreObjectType"

    named = cybox.TypedField("named")
    current_count = cybox.TypedField("Current_Count", UnsignedInteger)
    maximum_count = cybox.TypedField("Maximum_Count", PositiveInteger)
    name = cybox.TypedField("Name", String)
