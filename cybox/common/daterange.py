# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import DateWithPrecision


class DateRange(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateRangeType
    _namespace = 'http://cybox.mitre.org/common-2'

    start_date = cybox.TypedField("Start_Date", DateWithPrecision)
    end_date = cybox.TypedField("End_Date", DateWithPrecision)
