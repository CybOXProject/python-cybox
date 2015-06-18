# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_memory_page_region_object as win_memory_page_region_binding
from cybox.common import String, HashList, UnsignedLong, HexBinary, ExtractedFeatures
from cybox.objects.memory_object import Memory


class WinMemoryPageRegion(Memory):
    _binding = win_memory_page_region_binding
    _binding_class = win_memory_page_region_binding.WindowsMemoryPageRegionObjectType
    _namespace = "http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2"
    _XSI_NS = "WinMemoryPageRegionObj"
    _XSI_TYPE = "WindowsMemoryPageRegionObjectType"

    is_injected = fields.TypedField("is_injected")
    is_mapped = fields.TypedField("is_mapped")
    is_protected = fields.TypedField("is_protected")
    is_volatile = fields.TypedField("is_volatile")

    hashes = fields.TypedField("Hashes", HashList)
    name = fields.TypedField("Name", String)
    memory_source = fields.TypedField("Memory_Source", String)
    region_size = fields.TypedField("Region_Size", UnsignedLong)
    block_type = fields.TypedField("Block_Type", String)
    region_start_address = fields.TypedField("Region_Start_Address", HexBinary)
    region_end_address = fields.TypedField("Region_End_Address", HexBinary)
    extracted_features = fields.TypedField("Extracted_Features", ExtractedFeatures)
    allocation_base_address = fields.TypedField("Allocation_Base_Address", HexBinary)

    type_ = fields.TypedField("Type", String)
    allocation_protect = fields.TypedField("Allocation_Protect", String)
    state = fields.TypedField("State", String)
    protect = fields.TypedField("Protect", String)
