# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import HashList, Integer, String, PositiveInteger


class ByteRun(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ByteRunType
    _namespace = 'http://cybox.mitre.org/common-2'

    offset = fields.TypedField("Offset", Integer)
    byte_order = fields.TypedField("Byte_Order", String)
    file_system_offset = fields.TypedField("File_System_Offset", Integer)
    image_offset = fields.TypedField("Image_Offset", Integer)
    length = fields.TypedField("Length", PositiveInteger)
    hashes = fields.TypedField("Hashes", HashList)
    byte_run_data = fields.TypedField("Byte_Run_Data")


class ByteRuns(entities.EntityList):
    _binding_class = common_binding.ByteRunsType
    _namespace = 'http://cybox.mitre.org/common-2'
    byte_run = fields.TypedField("Byte_Run", ByteRun, multiple=True)
