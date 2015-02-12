# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import DateTimeWithPrecision


class Time(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.TimeType
    _namespace = 'http://cybox.mitre.org/common-2'

    start_time = cybox.TypedField("Start_Time", DateTimeWithPrecision)
    end_time = cybox.TypedField("End_Time", DateTimeWithPrecision)
    produced_time = cybox.TypedField("Produced_Time", DateTimeWithPrecision)
    received_time = cybox.TypedField("Received_Time", DateTimeWithPrecision)

    def __init__(self, start_time=None, end_time=None, produced_time=None, received_time=None):
        super(Time, self).__init__()
        self.start_time = start_time
        self.end_time = end_time
        self.produced_time = produced_time
        self.received_time = received_time

