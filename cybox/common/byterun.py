# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import HashList, Integer, String


class ByteRun(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.ByteRunType
    _namespace = 'http://cybox.mitre.org/common-2'

    offset = cybox.TypedField("Offset", Integer)
    byte_order = cybox.TypedField("Byte_Order", String)
    file_system_offset = cybox.TypedField("File_System_Offset", Integer)
    image_offset = cybox.TypedField("Image_Offset", Integer)
    length = cybox.TypedField("Length", Integer)
    hashes = cybox.TypedField("Hashes", HashList)
    byte_run_data = cybox.TypedField("Byte_Run_Data")


class ByteRuns(cybox.EntityList):
    _binding_class = common_binding.ByteRunsType
    _binding_var = "Byte_Run"
    _contained_type = ByteRun
    _namespace = 'http://cybox.mitre.org/common-2'
