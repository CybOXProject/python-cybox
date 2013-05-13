# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute
from cybox.common import HashList, Integer


class ByteRun(cybox.Entity):

    offset = cybox.TypedField("Offset", Integer)
    file_system_offset = cybox.TypedField("File_System_Offset", Integer)
    image_offset = cybox.TypedField("Image_Offset", Integer)
    length = cybox.TypedField("Length", Integer)
    hashes = cybox.TypedField("Hashes", HashList, try_cast=False)

    def __init__(self):
        self.byte_run_data = None
        pass

    def to_obj(self):
        byterun_obj = common_binding.ByteRunType()

        if self.offset is not None:
            byterun_obj.set_Offset(self.offset.to_obj())
        if self.file_system_offset is not None:
            byterun_obj.set_File_System_Offset(self.file_system_offset.to_obj())
        if self.image_offset is not None:
            byterun_obj.set_Image_Offset(self.image_offset.to_obj())
        if self.length is not None:
            byterun_obj.set_Length(self.length.to_obj())
        if self.hashes:
            byterun_obj.set_Hashes(self.hashes.to_obj())
        if self.byte_run_data is not None:
            byterun_obj.set_Byte_Run_Data(self.byte_run_data)

        return byterun_obj

    def to_dict(self):
        byterun_dict = {}

        if self.offset is not None:
            byterun_dict['offset'] = self.offset.to_dict()
        if self.file_system_offset is not None:
            byterun_dict['file_system_offset'] = self.file_system_offset.to_dict()
        if self.image_offset is not None:
            byterun_dict['image_offset'] = self.image_offset.to_dict()
        if self.length is not None:
            byterun_dict['length'] = self.length.to_dict()
        if self.hashes:
            byterun_dict['hashes'] = self.hashes.to_list()
        if self.byte_run_data is not None:
            byterun_dict['byte_run_data'] = self.byte_run_data

        return byterun_dict

    @staticmethod
    def from_obj(byterun_obj):
        if byterun_obj is None:
            return None

        byterun = ByteRun()

        byterun.offset = Integer.from_obj(byterun_obj.get_Offset())
        byterun.file_system_offset = Integer.from_obj(byterun_obj.get_File_System_Offset())
        byterun.image_offset = Integer.from_obj(byterun_obj.get_Image_Offset())
        byterun.length = Integer.from_obj(byterun_obj.get_Length())
        byterun.hashes = HashList.from_obj(byterun_obj.get_Hashes())
        byterun.byte_run_data = byterun_obj.get_Byte_Run_Data()

        return byterun

    @staticmethod
    def from_dict(byterun_dict):
        if byterun_dict is None:
            return None

        byterun = ByteRun()

        byterun.offset = Integer.from_dict(byterun_dict.get('offset'))
        byterun.file_system_offset = Integer.from_dict(byterun_dict.get('file_system_offset'))
        byterun.image_offset = Integer.from_dict(byterun_dict.get('image_offset'))
        byterun.length = Integer.from_dict(byterun_dict.get('length'))
        byterun.hashes = HashList.from_list(byterun_dict.get('hashes'))
        byterun.byte_run_data = byterun_dict.get('byte_run_data')

        return byterun


class ByteRuns(cybox.EntityList):
    _binding_class = common_binding.ByteRunsType
    _contained_type = ByteRun

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Byte_Run(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Byte_Run()
