# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import Integer, String
import cybox.xs as xs


class DataSize(String):
    _binding = common_binding
    _binding_class = common_binding.DataSizeType
    _namespace = 'http://cybox.mitre.org/common-2'

    units = cybox.TypedField("units", xs.Enum)

    def is_plain(self):
        return super(DataSize, self).is_plain() and self.units is None


class DataSegment(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.DataSegmentType
    _namespace = 'http://cybox.mitre.org/common-2'

    id_ = cybox.TypedField("id", xs.QName)
    data_format = cybox.TypedField("Data_Format", xs.Enum)
    data_size = cybox.TypedField("Data_Size", DataSize)
    data_segment = cybox.TypedField("Data_Segment", String)
    offset = cybox.TypedField("Offset", Integer)
    search_distance = cybox.TypedField("Search_Distance", Integer)
    search_within = cybox.TypedField("Search_Within", Integer)
