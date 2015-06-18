# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.memory_object as memory_binding
from cybox.common import (ExtractedFeatures, HashList, HexBinary,
        ObjectProperties, String, UnsignedLong)


class Memory(ObjectProperties):
    _binding = memory_binding
    _binding_class = memory_binding.MemoryObjectType
    _namespace = 'http://cybox.mitre.org/objects#MemoryObject-2'
    _XSI_NS = "MemoryObj"
    _XSI_TYPE = "MemoryObjectType"

    is_injected = fields.TypedField("is_injected")
    is_mapped = fields.TypedField("is_mapped")
    is_protected = fields.TypedField("is_protected")
    is_volatile = fields.TypedField("is_volatile")
    hashes = fields.TypedField("Hashes", HashList)
    name = fields.TypedField("Name", String)
    region_size = fields.TypedField("Region_Size", UnsignedLong)
    memory_source = fields.TypedField("Memory_Source", String)
    block_type = fields.TypedField("Block_Type", String)
    region_start_address = fields.TypedField("Region_Start_Address", HexBinary)
    region_end_address = fields.TypedField("Region_End_Address", HexBinary)
    extracted_features = fields.TypedField("Extracted_Features",
            ExtractedFeatures)
