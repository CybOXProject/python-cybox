# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding

class DateRange(cybox.Entity):
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self):
        super(DateRange, self).__init__()
        self.start_date = None
        self.end_date = None

    def to_obj(self):
        date_range_obj = common_binding.DateRangeType()
        if self.start_date is not None : date_range_obj.set_Start_Date(self.start_date)
        if self.end_date is not None : date_range_obj.set_End_Date(self.end_date)
        return date_range_obj

    def to_dict(self):
        date_range_dict = {}
        if self.start_date is not None : date_range_dict['start_date'] = self.start_date
        if self.end_date is not None : date_range_dict['end_date'] = self.end_date
        return date_range_dict

    @staticmethod
    def from_dict(date_range_dict):
        if not date_range_dict:
            return None
        date_range_ = DateRange()
        date_range_.start_date = date_range_dict.get('start_date')
        date_range_.end_date = date_range_dict.get('end_date')
        return date_range_

    @staticmethod
    def from_obj(date_range_obj):
        if not date_range_obj:
            return None
        date_range_ = DateRange()
        date_range_.start_date = date_range_obj.get_Start_Date()
        date_range_.end_date = date_range_obj.get_End_Date()
        return date_range_
