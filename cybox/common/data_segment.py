# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import Integer, String


class DataSize(String):
    _binding = common_binding
    _binding_class = common_binding.DataSizeType
    _namespace = 'http://cybox.mitre.org/common-2'

    units = fields.TypedField("units")

    def is_plain(self):
        return (super(DataSize, self).is_plain() and self.units is None)


class DataSegment(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DataSegmentType
    _namespace = 'http://cybox.mitre.org/common-2'

    id_ = fields.TypedField("id")
    data_format = fields.TypedField("Data_Format")
    data_size = fields.TypedField("Data_Size", DataSize)
    byte_order = fields.TypedField("Byte_Order", String)
    data_segment = fields.TypedField("Data_Segment", String)
    offset = fields.TypedField("Offset", Integer)
    search_distance = fields.TypedField("Search_Distance", Integer)
    search_within = fields.TypedField("Search_Within", Integer)
