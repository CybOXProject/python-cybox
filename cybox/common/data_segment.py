# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import Integer, String


class DataSize(String):
    _binding = common_binding
    _binding_class = common_binding.DataSizeType
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, *args, **kwargs):
        String.__init__(self, *args, **kwargs)
        self.units = None

    def is_plain(self):
        return (super(DataSize, self).is_plain() and
                self.units is None)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        datasize_obj = String.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        if self.units is not None:
            datasize_obj.units = self.units
        return datasize_obj

    def to_dict(self):
        datasize_dict = String.to_dict(self)
        if self.units is not None:
            datasize_dict['units'] = self.units
        return datasize_dict

    @staticmethod
    def from_obj(datasize_obj):
        if not datasize_obj:
            return None
        datasize = DataSize()
        datasize._populate_from_obj(datasize_obj)
        datasize.units = datasize_obj.units
        return datasize

    @staticmethod
    def from_dict(datasize_dict):
        if not datasize_dict:
            return None
        datasize = DataSize()
        datasize._populate_from_dict(datasize_dict)
        if isinstance(datasize_dict, dict):
            datasize.units = datasize_dict.get('units')
        return datasize


class DataSegment(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.DataSegmentType
    _namespace = 'http://cybox.mitre.org/common-2'

    id_ = cybox.TypedField("id")
    data_format = cybox.TypedField("Data_Format")
    data_size = cybox.TypedField("Data_Size", DataSize)
    byte_order = cybox.TypedField("Byte_Order", String)
    data_segment = cybox.TypedField("Data_Segment", String)
    offset = cybox.TypedField("Offset", Integer)
    search_distance = cybox.TypedField("Search_Distance", Integer)
    search_within = cybox.TypedField("Search_Within", Integer)
