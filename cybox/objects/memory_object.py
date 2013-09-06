# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.memory_object as memory_binding
from cybox.common import (ExtractedFeatures, HashList, HexBinary,
        ObjectProperties, String, UnsignedLong)


class Memory(ObjectProperties):
    _binding = memory_binding
    _binding_class = memory_binding.MemoryObjectType
    _namespace = 'http://cybox.mitre.org/objects#MemoryObject-2'
    _XSI_NS = "MemoryObj"
    _XSI_TYPE = "MemoryObjectType"

    is_injected = cybox.TypedField("is_injected")
    is_mapped = cybox.TypedField("is_mapped")
    is_protected = cybox.TypedField("is_protected")
    hashes = cybox.TypedField("Hashes", HashList)
    name = cybox.TypedField("Name", String)
    region_size = cybox.TypedField("Region_Size", UnsignedLong)
    region_start_address = cybox.TypedField("Region_Start_Address", HexBinary)
    extracted_features = cybox.TypedField("Extracted_Features",
            ExtractedFeatures)
