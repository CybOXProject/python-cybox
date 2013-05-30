# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.utils as utils
import cybox.bindings.memory_object as memory_binding
from cybox.common import HashList, ObjectProperties, String, UnsignedLong, HexBinary

class Memory(ObjectProperties):
    _XSI_NS = "MemoryObj"
    _XSI_TYPE = "MemoryObjectType"

    def __init__(self):
        self.is_injected = None
        self.is_mapped = None
        self.is_protected =  None
        self.hashes = None
        self.name = None
        self.region_size = None
        self.region_start_address = None
        self.extracted_features = None

    def to_obj(self):
        memory_obj = memory_binding.MemoryObjectType()
        super(Memory, self).to_obj(memory_obj)

        if self.is_injected is not None: memory_obj.set_is_injected(self.is_injected)
        if self.is_mapped is not None: memory_obj.set_is_mapped(self.is_mapped)
        if self.is_protected is not None: memory_obj.set_is_protected(self.is_protected)
        if self.hashes is not None: memory_obj.set_Hashes(self.hashes.to_obj())
        if self.name is not None: memory_obj.set_Name(self.name.to_obj())
        if self.region_size is not None: memory_obj.set_Region_Size(self.region_size.to_obj())
        if self.region_start_address is not None: memory_obj.set_Region_Start_Address(self.region_start_address.to_obj())
        if self.extracted_features is not None: memory_obj.set_Extracted_Features(self.extracted_features.to_obj())

        return memory_obj

    def to_dict(self):
        memory_dict = {}
        super(Memory, self).to_dict(memory_dict)

        if self.is_injected is not None: memory_dict['is_injected'] = self.is_injected
        if self.is_mapped is not None: memory_dict['is_mapped'] = self.is_mapped
        if self.is_protected is not None: memory_dict['is_protected'] = self.is_protected
        if self.hashes is not None: memory_dict['hashes'] = self.hashes.to_list()
        if self.name is not None: memory_dict['name'] = self.name.to_dict()
        if self.region_size is not None: memory_dict['region_size'] = self.region_size.to_dict()
        if self.region_start_address is not None: memory_dict['region_start_address'] = self.region_start_address.to_dict()
        if self.extracted_features is not None: memory_dict['extracted_features'] = self.extracted_features.to_dict()

        return memory_dict
        
    @staticmethod
    def from_dict(memory_dict):
        if not memory_dict:
            return None

        memory_ = Memory()
        memory_.is_injected = memory_dict.get('is_injected')
        memory_.is_mapped = memory_dict.get('is_mapped')
        memory_.is_protected = memory_dict.get('is_protected')
        memory_.hashes = HashList.from_list(memory_dict.get('hashes'))
        memory_.name = String.from_dict(memory_dict.get('name'))
        memory_.region_size = UnsignedLong.from_dict(memory_dict.get('region_size'))
        memory_.region_start_address = HexBinary.from_dict(memory_dict.get('region_start_address'))
        memory_.extracted_features = None

        return memory_

    @staticmethod
    def from_obj(memory_obj):
        if not memory_obj:
            return None

        memory_ = Memory()
        memory_.is_injected = memory_obj.get_is_injected()
        memory_.is_mapped = memory_obj.get_is_mapped()
        memory_.is_protected = memory_obj.get_is_protected()
        memory_.hashes = HashList.from_obj(memory_obj.get_Hashes())
        memory_.name = String.from_obj(memory_obj.get_Name())
        memory_.region_size = UnsignedLong.from_obj(memory_obj.get_Region_Size())
        memory_.region_start_address = HexBinary.from_obj(memory_obj.get_Region_Start_Address())
        memory_.extracted_features = None

        return memory_
