# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_memory_page_region_object as win_memory_page_region_binding
from cybox.common import (String, HashList, UnsignedLong, HexBinary, 
                ExtractedFeatures, ObjectProperties)
from cybox.objects.memory_object import Memory


class WinMemoryPageRegion(Memory):
    _binding = win_memory_page_region_binding
    _binding_class = win_memory_page_region_binding.WindowsMemoryPageRegionObjectType
    _namespace = "http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2"
    _XSI_NS = "WinMemoryPageRegionObj"
    _XSI_TYPE = "WindowsMemoryPageRegionObjectType"

    is_injected = cybox.TypedField("is_injected")
    is_mapped = cybox.TypedField("is_mapped")
    is_protected = cybox.TypedField("is_protected")
    is_volatile = cybox.TypedField("is_volatile")
    
    hashes = cybox.TypedField("Hashes", HashList)
    name = cybox.TypedField("Name", String)
    memory_source = cybox.TypedField("Memory_Source", String)
    region_size = cybox.TypedField("Region_Size", UnsignedLong)
    block_type = cybox.TypedField("Block_Type", String)
    region_start_address = cybox.TypedField("Region_Start_Address", HexBinary)
    region_end_address = cybox.TypedField("Region_End_Address", HexBinary)
    extracted_features = cybox.TypedField("Extracted_Features", ExtractedFeatures)
    allocation_base_address = cybox.TypedField("Allocation_Base_Address", HexBinary)

    type_ = cybox.TypedField("Type", String)
    allocation_protect = cybox.TypedField("Allocation_Protect", String)
    state = cybox.TypedField("State", String)
    protect = cybox.TypedField("Protect", String)
    
