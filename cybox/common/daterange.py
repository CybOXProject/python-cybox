# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding


class DateRange(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateRangeType
    _namespace = 'http://cybox.mitre.org/common-2'

    start_date = cybox.TypedField("Start_Date")
    end_date = cybox.TypedField("End_Date")
