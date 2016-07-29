# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import entities
from mixbox import fields
from mixbox.vendor import six

import cybox.bindings.cybox_common as common_binding
from cybox.common.attribute_groups import PatternFieldGroup
from cybox.common.datetimewithprecision import (validate_date_precision,
    validate_time_precision, validate_datetime_precision)
from cybox.utils import normalize_to_xml, denormalize_from_xml

DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES


def validate_string_type(instance, value):
    if value is None:
        return
    elif isinstance(value, six.string_types):
        return
    elif isinstance(value, list):
        for x in value:
            validate_string_type(instance, x)
    else:
        raise ValueError("Value must be a string. Received %r" % value)


class ListFieldMixin(object):
    """Mixin that allows a TypedField to be set to a list of values or a single
    value. If a list of values are passed in, each item in the list will be
    passed through the _clean() method.
    """
    def check_type(self, value):
        func_check = super(ListFieldMixin, self).check_type
        if isinstance(value, list):
            return all(func_check(x) for x in value)
        return func_check(value)

    def _clean(self, value):
        func_clean = super(ListFieldMixin, self)._clean
        if isinstance(value, list):
            return [func_clean(x) for x in value]
        return func_clean(value)


# Field types that can accept lists or scalar values.
class ListTypedField(ListFieldMixin, fields.TypedField): pass
class ListDateField(ListFieldMixin, fields.DateField): pass
class ListDateTimeField(ListFieldMixin, fields.DateTimeField): pass
class ListFloatField(ListFieldMixin, fields.FloatField): pass
class ListIntegerField(ListFieldMixin, fields.IntegerField): pass
class ListLongField(ListFieldMixin, fields.LongField): pass


@six.python_2_unicode_compatible
class BaseProperty(PatternFieldGroup, entities.Entity):
    # Most Properties are defined in the "common" binding, so we'll just set
    # that here. Some BaseProperty subclasses might have to override this.
    _binding = common_binding
    _binding_class = _binding.BaseObjectPropertyType
    _namespace = 'http://cybox.mitre.org/common-2'

    # If `True`, force the "datatype" attribute to be output. This is
    # necessary in some cases
    _force_datatype = False
    default_datatype = 'string'

    # BaseObjectProperty Group
    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    value = ListTypedField("valueOf_", key_name="value")
    datatype = fields.TypedField("datatype")
    appears_random = fields.TypedField("appears_random")
    is_obfuscated = fields.TypedField("is_obfuscated")
    obfuscation_algorithm_ref = fields.TypedField("obfuscation_algorithm_ref")
    is_defanged = fields.TypedField("is_defanged")
    defanging_algorithm_ref = fields.TypedField("defanging_algorithm_ref")
    refanging_transform_type = fields.TypedField("refanging_transform_type")
    refanging_transform = fields.TypedField("refanging_transform")
    observed_encoding = fields.TypedField("observed_encoding")

    def __init__(self, value=None):
        super(BaseProperty, self).__init__()
        self._force_datatype = False

        self.value = value
        self.datatype = self.default_datatype

    def __str__(self):
        return six.text_type(self.value)

    def __int__(self):
        return int(self.value)

    @property
    def serialized_value(self):
        return self.value

    @property
    def values(self):
        """Allow uniform access to `value` as a list.

        This allows code like the following to always work where `obj` is a
        CybOX entity and `prop` is any BaseProperty subclass:

        ```
        for x in obj.prop.values():
            do_something(x)
        ```

        If `value` is None, this returns an empty list ([])
        If `value` is a single non-list value, it returns a single-item list.
        If `value` is a list, `values` is identical to `value`.

        NOTE: This property cannot be set. Use the `value` setter for this.
        """
        if self.value is None:
            return []
        elif isinstance(self.value, list):
            return self.value
        else:
            return [self.value]

    def __eq__(self, other):
        # None-type checking
        if not other:
            return False

        # It is possible to compare a Property to a single value if
        # the Property defines only the "value" property.
        if not isinstance(other, BaseProperty) and self.is_plain():
            return self.value == other

        return (
            self.value == other.value and
            self.id_ == other.id_ and
            self.idref == other.idref and
            self.datatype == other.datatype and
            self.appears_random == other.appears_random and
            self.is_obfuscated == other.is_obfuscated and
            self.obfuscation_algorithm_ref == other.obfuscation_algorithm_ref and
            self.is_defanged == other.is_defanged and
            self.defanging_algorithm_ref == other.defanging_algorithm_ref and
            self.refanging_transform_type == other.refanging_transform_type and
            self.refanging_transform == other.refanging_transform and
            self.observed_encoding == other.observed_encoding and

            PatternFieldGroup._conditions_equal(self, other) and

            self.bit_mask == other.bit_mask and
            self.pattern_type == other.pattern_type and
            self.regex_syntax == other.regex_syntax and
            self.is_case_sensitive == other.is_case_sensitive and
            self.has_changed == other.has_changed and
            self.trend == other.trend
        )

    def __ne__(self, other):
        return not self == other

    def is_plain(self):
        """Whether the Property can be represented as a single value.

        The `datatype` can be inferred by the particular BaseProperty subclass,
        so if `datatype` and `value` are the only non-None properties, the
        BaseProperty can be represented by a single value rather than a
        dictionary. This makes the JSON representation simpler without losing
        any data fidelity.
        """
        return (
            # ignore value
            self.id_ is None and
            self.idref is None and
            # ignore datatype
            self.appears_random is None and
            self.is_obfuscated is None and
            self.obfuscation_algorithm_ref is None and
            self.is_defanged is None and
            self.defanging_algorithm_ref is None and
            self.refanging_transform_type is None and
            self.refanging_transform is None and
            self.observed_encoding is None and
            super(BaseProperty, self).is_plain()
        )

    def __nonzero__(self):
        return (not self.is_plain()) or (self.value is not None)

    __bool__ = __nonzero__

    def _datatype_serialized_value(self):
        if self._force_datatype:
            return self.datatype
        elif self.datatype != self.default_datatype:
            return self.datatype
        else:
            return None

    def to_obj(self, ns_info=None):
        attr_obj = super(BaseProperty, self).to_obj(ns_info=ns_info)
        attr_obj.datatype = self._datatype_serialized_value()
        attr_obj.valueOf_ = normalize_to_xml(self.serialized_value,
                                             self.delimiter)
        return attr_obj

    def to_dict(self):
        if self.is_plain():
            return self.serialized_value

        attr_dict = super(BaseProperty, self).to_dict()
        attr_dict.pop("datatype", None)

        if self._datatype_serialized_value():
            attr_dict['datatype'] = self._datatype_serialized_value()
        if self.value is not None:
            attr_dict['value'] = self.serialized_value

        return attr_dict

    @classmethod
    def from_obj(cls, cls_obj):
        # Use the subclass this was called on to initialize the object

        if not cls_obj:
            return None

        # split delimited values now, before converting from bindings object to API object
        cls_obj.valueOf_ = denormalize_from_xml(cls_obj.valueOf_, cls_obj.delimiter)
        attr = super(BaseProperty, cls).from_obj(cls_obj)
        attr.datatype = cls_obj.datatype or cls.default_datatype
        return attr

    @classmethod
    def from_dict(cls, cls_dict):
        attr = super(BaseProperty, cls).from_dict(cls_dict)

        if isinstance(cls_dict, dict):
            attr.datatype = cls_dict.get('datatype', cls.default_datatype)

        return attr

class String(BaseProperty):
    _binding_class = common_binding.StringObjectPropertyType
    default_datatype = "string"
    value = ListTypedField("valueOf_", key_name="value", preset_hook=validate_string_type)


class _IntegerBase(BaseProperty):
    """Define a common _parse_value function for all Integer types"""
    value = ListIntegerField("valueOf_", key_name="value")


class Integer(_IntegerBase):
    _binding_class = common_binding.IntegerObjectPropertyType
    default_datatype = "int"


class PositiveInteger(_IntegerBase):
    _binding_class = common_binding.PositiveIntegerObjectPropertyType
    default_datatype = "positiveInteger"


class UnsignedInteger(_IntegerBase):
    _binding_class = common_binding.UnsignedIntegerObjectPropertyType
    default_datatype = "unsignedInt"


class NonNegativeInteger(_IntegerBase):
    _binding_class = common_binding.NonNegativeIntegerObjectPropertyType
    default_datatype = "nonNegativeInteger"


class AnyURI(BaseProperty):
    _binding_class = common_binding.AnyURIObjectPropertyType
    default_datatype = "anyURI"


class HexBinary(BaseProperty):
    _binding_class = common_binding.HexBinaryObjectPropertyType
    default_datatype = "hexBinary"


class Base64Binary(BaseProperty):
    _binding_class = common_binding.Base64BinaryObjectPropertyType
    default_datatype = "base64Binary"


class Duration(BaseProperty):
    _binding_class = common_binding.DurationObjectPropertyType
    default_datatype = "duration"


class Time(BaseProperty):
    _binding_class = common_binding.TimeObjectPropertyType
    default_datatype = "time"

    precision = fields.TypedField("precision", preset_hook=validate_time_precision)

    def __init__(self, value=None, precision='second'):
        super(Time, self).__init__(value=value)
        self.precision = precision


@six.python_2_unicode_compatible
class Date(BaseProperty):
    _binding_class = common_binding.DateObjectPropertyType
    default_datatype = "date"

    value = ListDateField("valueOf_", key_name="value")
    precision = fields.TypedField("precision", preset_hook=validate_date_precision)

    def __init__(self, value=None, precision='day'):
        super(Date, self).__init__(value=value)
        self.precision = precision

    def __str__(self):
        if self.value:
            return self.value.isoformat()
        return super(BaseProperty, self).__str__()

    @property
    def serialized_value(self):
        if isinstance(self.value, list):
            return [x.isoformat() for x in self.value]
        elif self.value is None:
            return None
        else:
            return self.value.isoformat()


@six.python_2_unicode_compatible
class DateTime(BaseProperty):
    _binding_class = common_binding.DateTimeObjectPropertyType
    default_datatype = "dateTime"

    value = ListDateTimeField("valueOf_", key_name="value")
    precision = fields.TypedField("precision", preset_hook=validate_datetime_precision)

    def __init__(self, value=None, precision='second'):
        super(DateTime, self).__init__(value=value)
        self.precision = precision

    def __str__(self):
        if self.value:
            return self.value.isoformat()
        return super(BaseProperty, self).__str__()

    @property
    def serialized_value(self):
        if isinstance(self.value, list):
            return [x.isoformat() for x in self.value]
        elif self.value is None:
            return None
        else:
            return self.value.isoformat()


class _FloatBase(BaseProperty):
    """Define a common _parse_value function for Float and Double types."""
    value = ListFloatField("valueOf_", key_name="value")


class Double(_FloatBase):
    _binding_class = common_binding.DoubleObjectPropertyType
    default_datatype = "double"


class Float(_FloatBase):
    _binding_class = common_binding.FloatObjectPropertyType
    default_datatype = "float"


class _LongBase(BaseProperty):
    """Define a common _parse_value function for all Long types."""
    value = ListLongField("valueOf_", key_name="value")


class Long(_LongBase):
    _binding_class = common_binding.LongObjectPropertyType
    default_datatype = "long"


class UnsignedLong(_LongBase):
    _binding_class = common_binding.UnsignedLongObjectPropertyType
    default_datatype = "unsignedLong"


class Name(BaseProperty):
    _binding_class = common_binding.NameObjectPropertyType
    default_datatype = "name"


# Mapping of binding classes to the corresponding BaseProperty subclass
BINDING_CLASS_MAPPING = {
        common_binding.StringObjectPropertyType: String,
        common_binding.IntegerObjectPropertyType: Integer,
        common_binding.PositiveIntegerObjectPropertyType: PositiveInteger,
        common_binding.UnsignedIntegerObjectPropertyType: UnsignedInteger,
        common_binding.UnsignedLongObjectPropertyType: UnsignedLong,
        common_binding.AnyURIObjectPropertyType: AnyURI,
        common_binding.HexBinaryObjectPropertyType: HexBinary,
        common_binding.DateTimeObjectPropertyType: DateTime,
        common_binding.DateObjectPropertyType: Date,
        common_binding.TimeObjectPropertyType: Time,
        common_binding.DurationObjectPropertyType: Duration,
        common_binding.NonNegativeIntegerObjectPropertyType: NonNegativeInteger,
        common_binding.FloatObjectPropertyType: Float,
        common_binding.DoubleObjectPropertyType: Double,
        common_binding.LongObjectPropertyType: Long,
        # This shouldn't be needed anymore, but we'll leave it here to be safe.
        common_binding.SimpleHashValueType: HexBinary,
#        common_binding.HashNameType: HashName,
    }
