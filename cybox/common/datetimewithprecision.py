# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields
from mixbox import dates

import cybox.bindings.cybox_common as common_binding

DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES


def _validate_precision(value, allowed):
    if value is None:
        return
    elif value in allowed:
        return
    else:
        error = "The precision must be one of {allowed}. Received '{value}'"
        error = error.format(**locals())
        raise ValueError(error)


def validate_date_precision(instance, value):
    _validate_precision(value, DATE_PRECISION_VALUES)


def validate_datetime_precision(instance, value):
    _validate_precision(value, DATETIME_PRECISION_VALUES)


def validate_time_precision(instance, value):
    _validate_precision(value, TIME_PRECISION_VALUES)



class DateTimeWithPrecision(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateTimeWithPrecisionType
    _namespace = 'http://cybox.mitre.org/common-2'

    value = fields.DateTimeField("valueOf_", key_name="value")
    precision = fields.TypedField("precision", preset_hook=validate_datetime_precision)

    def __init__(self, value=None, precision='second'):
        super(DateTimeWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    def to_dict(self):
        if self.precision == 'second':
            return dates.serialize_datetime(self.value)
        return super(DateTimeWithPrecision, self).to_dict()


class DateWithPrecision(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.DateWithPrecisionType
    _namespace = 'http://cybox.mitre.org/common-2'

    value = fields.DateField("valueOf_", key_name="value")
    precision = fields.TypedField("precision", preset_hook=validate_date_precision)

    def __init__(self, value=None, precision='day'):
        super(DateWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    def to_dict(self):
        if self.precision == 'day':
            return dates.serialize_date(self.value)
        return super(DateWithPrecision, self).to_dict()
