# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime

import dateutil.parser

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml

DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES


class BaseProperty(PatternFieldGroup, cybox.Entity):
    # Most Properties are defined in the "common" binding, so we'll just set
    # that here. Some BaseProperty subclasses might have to override this.
    _binding = common_binding
    _namespace = 'http://cybox.mitre.org/common-2'
    default_datatype = 'string'

    def __init__(self, value=None):
        super(BaseProperty, self).__init__()
        self.value = value
        # If `True`, force the "datatype" attribute to be output. This is
        # necessary in some cases
        self._force_datatype = False

        # BaseObjectProperty Group
        self.id_ = None
        self.idref = None
        # ``datatype`` is a class-level variable
        self.appears_random = None
        self.is_obfuscated = None
        self.obfuscation_algorithm_ref = None
        self.is_defanged = None
        self.defanging_algorithm_ref = None
        self.refanging_transform_type = None
        self.refanging_transform = None
        self.observed_encoding = None

    def __str__(self):
        # To be safe, return the unicode string encoded as UTF-8
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.serialized_value)

    def __int__(self):
        return int(self.serialized_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_):
        # This is done here, so the value is always parsed, regardless of
        # whether it is set via the __init__() function, via the from_*
        # static methods, or on an instance of the class after it has been
        # created.
        if isinstance(value_, list):
            self._value = map(self._parse_value, value_)
        else:
            self._value = self._parse_value(value_)

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

    @staticmethod
    def _parse_value(value):
        """Parse a user-supplied value into the internal representation.

        For most Property types, this does not modify `value`. However,
        some attributes may have a more specific representation.
        """
        return value

    @property
    def serialized_value(self):
        if isinstance(self.value, list):
            return map(self._serialize_value, self.value)
        else:
            return self.__class__._serialize_value(self.value)

    @staticmethod
    def _serialize_value(value):
        """Format the `value` for serialization (XML, JSON).

        For most attribute types, this will return the `value` unmodified.
        However, some attributes types may need additional formatting.
        """
        return value

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

            PatternFieldGroup.is_plain(self)
        )

    def __nonzero__(self):
        return (not self.is_plain()) or (self.value is not None)

    __bool__ = __nonzero__

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        attr_obj = self._binding_class()
        attr_obj.set_valueOf_(normalize_to_xml(self.serialized_value,
                                               self.delimiter))
        # For now, don't output the datatype, as it is not required and is
        # usually not needed, as it can be inferred from the context.
        #attr_obj.datatype = self.datatype

        if self.id_ is not None:
            attr_obj.id = self.id_
        if self.idref is not None:
            attr_obj.idref = self.idref
        if self.appears_random is not None:
            attr_obj.appears_random = self.appears_random
        if self.is_obfuscated is not None:
            attr_obj.is_obfuscated = self.is_obfuscated
        if self.obfuscation_algorithm_ref is not None:
            attr_obj.obfuscation_algorithm_ref = self.obfuscation_algorithm_ref
        if self.is_defanged is not None:
            attr_obj.is_defanged = self.is_defanged
        if self.defanging_algorithm_ref is not None:
            attr_obj.defanging_algorithm_ref = self.defanging_algorithm_ref
        if self.refanging_transform_type is not None:
            attr_obj.refanging_transform_type = self.refanging_transform_type
        if self.refanging_transform is not None:
            attr_obj.refanging_transform = self.refanging_transform
        if self.observed_encoding is not None:
            attr_obj.observed_encoding = self.observed_encoding
        #Datatype output logic
        if self._force_datatype or (self.datatype != self.default_datatype):
            attr_obj.datatype = self.datatype
        else:
            attr_obj.datatype = None

        PatternFieldGroup.to_obj(self, return_obj=attr_obj, ns_info=ns_info)

        return attr_obj

    def to_dict(self):
        if self.is_plain():
            return self.serialized_value

        attr_dict = {}
        if self.value is not None:
            attr_dict['value'] = self.serialized_value

        if self.datatype is not None and (self.datatype != self.default_datatype):
            attr_dict['datatype'] = self.datatype

        if self.id_ is not None:
            attr_dict['id'] = self.id_
        if self.idref is not None:
            attr_dict['idref'] = self.idref
        if self.appears_random is not None:
            attr_dict['appears_random'] = self.appears_random
        if self.is_obfuscated is not None:
            attr_dict['is_obfuscated'] = self.is_obfuscated
        if self.obfuscation_algorithm_ref is not None:
            attr_dict['obfuscation_algorithm_ref'] = self.obfuscation_algorithm_ref
        if self.is_defanged is not None:
            attr_dict['is_defanged'] = self.is_defanged
        if self.defanging_algorithm_ref is not None:
            attr_dict['defanging_algorithm_ref'] = self.defanging_algorithm_ref
        if self.refanging_transform_type is not None:
            attr_dict['refanging_transform_type'] = self.refanging_transform_type
        if self.refanging_transform is not None:
            attr_dict['refanging_transform'] = self.refanging_transform
        if self.observed_encoding is not None:
            attr_dict['observed_encoding'] = self.observed_encoding

        PatternFieldGroup.to_dict(self, attr_dict)

        return attr_dict

    @classmethod
    def from_obj(cls, attr_obj):
        # Subclasses with additional fields should override this method
        # and use _populate_from_obj as necessary.

        # Use the subclass this was called on to initialize the object

        if not attr_obj:
            return None

        attr = cls()
        attr._populate_from_obj(attr_obj)
        return attr

    def _populate_from_obj(self, attr_obj):

        self.id_ = attr_obj.id
        self.idref = attr_obj.idref
        self.datatype = attr_obj.datatype
        self.appears_random = attr_obj.appears_random
        self.is_obfuscated = attr_obj.is_obfuscated
        self.obfuscation_algorithm_ref = attr_obj.obfuscation_algorithm_ref
        self.is_defanged = attr_obj.is_defanged
        self.defanging_algorithm_ref = attr_obj.defanging_algorithm_ref
        self.refanging_transform_type = attr_obj.refanging_transform_type
        self.refanging_transform = attr_obj.refanging_transform
        self.observed_encoding = attr_obj.observed_encoding

        PatternFieldGroup.from_obj(attr_obj, self)

        # We need to check for a non-default delimiter before trying to parse
        # the value.
        self.value = denormalize_from_xml(attr_obj.valueOf_,
                                          self.delimiter)

    @classmethod
    def from_dict(cls, attr_dict):
        # Subclasses with additional fields should override this method
        # and use _populate_from_dict as necessary.

        if attr_dict is None:
            return None

        # Use the subclass this was called on to initialize the object.
        attr = cls()
        attr._populate_from_dict(attr_dict)
        return attr

    def _populate_from_dict(self, attr_dict):
        # If this attribute is "plain", use it as the value and assume the
        # datatype was set correctly by the constructor of the particular
        # BaseProperty Subclass.
        if not isinstance(attr_dict, dict):
            self.value = attr_dict
        else:
            # This key should always be present
            self.value = attr_dict.get('value')

            # This defaults to False if missing
            self._force_datatype = attr_dict.get('force_datatype', False)

            # 'None' is fine if these keys are missing
            self.id_ = attr_dict.get('id')
            self.idref = attr_dict.get('idref')
            self.appears_random = attr_dict.get('appears_random')
            self.datatype = attr_dict.get('datatype')
            self.is_obfuscated = attr_dict.get('is_obfuscated')
            self.obfuscation_algorithm_ref = attr_dict.get('obfuscation_algorithm_ref')
            self.is_defanged = attr_dict.get('is_defanged')
            self.defanging_algorithm_ref = attr_dict.get('defanging_algorithm_ref')
            self.refanging_transform_type = attr_dict.get('refanging_transform_type')
            self.refanging_transform = attr_dict.get('refanging_transform')
            self.observed_encoding = attr_dict.get('observed_encoding')

            PatternFieldGroup.from_dict(attr_dict, self)


class String(BaseProperty):
    _binding_class = common_binding.StringObjectPropertyType
    datatype = "string"
    default_datatype = "string"

    @staticmethod
    def _parse_value(value):
        if value is not None and not isinstance(value, basestring):
            raise ValueError("Cannot set String type to non-string value")

        return value


class _IntegerBase(BaseProperty):
    '''Define a common _parse_value function for all Integer types'''

    @staticmethod
    def _parse_value(value):
        if value is None or value == '':
            return None
        if isinstance(value, basestring):
            return int(value, 0)
        else:
            return int(value)

class Integer(_IntegerBase):
    _binding_class = common_binding.IntegerObjectPropertyType
    datatype = "integer"
    default_datatype = "integer"


class PositiveInteger(_IntegerBase):
    _binding_class = common_binding.PositiveIntegerObjectPropertyType
    datatype = "positiveInteger"
    default_datatype = "positiveInteger"

class UnsignedInteger(_IntegerBase):
    _binding_class = common_binding.UnsignedIntegerObjectPropertyType
    datatype = "unsignedInt"
    default_datatype = "unsignedInt"

class NonNegativeInteger(_IntegerBase):
    _binding_class = common_binding.NonNegativeIntegerObjectPropertyType
    datatype = "nonNegativeInteger"
    default_datatype = "nonNegativeInteger"

class AnyURI(BaseProperty):
    _binding_class = common_binding.AnyURIObjectPropertyType
    datatype = "anyURI"
    default_datatype = "anyURI"

class HexBinary(BaseProperty):
    _binding_class = common_binding.HexBinaryObjectPropertyType
    datatype = "hexBinary"
    default_datatype = "hexBinary"

class Base64Binary(BaseProperty):
    _binding_class = common_binding.Base64BinaryObjectPropertyType
    datatype = "base64Binary"
    default_datatype = "base64Binary"

class Duration(BaseProperty):
    _binding_class = common_binding.DurationObjectPropertyType
    datatype = "duration"
    default_datatype = "duration"

class Time(BaseProperty):
    _binding_class = common_binding.TimeObjectPropertyType
    datatype = "time"
    default_datatype = "time"

    def __init__(self, value=None, precision='second'):
        super(Time, self).__init__(value=value)
        self.precision = precision

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in TIME_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in TIME_PRECISION_VALUES))

        self._precision = value


class Date(BaseProperty):
    _binding_class = common_binding.DateObjectPropertyType
    datatype = "date"
    default_datatype = "date"

    def __init__(self, value=None, precision='day'):
        super(Date, self).__init__(value=value)
        self.precision = precision

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in DATE_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in DATE_PRECISION_VALUES))

        self._precision = value


class DateTime(BaseProperty):
    _binding_class = common_binding.DateTimeObjectPropertyType
    datatype = "dateTime"
    default_datatype = "dateTime"

    def __init__(self, value=None, precision='second'):
        super(DateTime, self).__init__(value=value)
        self.precision = precision

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in DATETIME_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in DATETIME_PRECISION_VALUES))

        self._precision = value


    @staticmethod
    def _parse_value(value):
        if not value:
            return None
        elif isinstance(value, datetime):
            return value
        return dateutil.parser.parse(value)

    @staticmethod
    def _serialize_value(value):
        if not value:
            return None
        return value.isoformat()


class _FloatBase(BaseProperty):
    '''Define a common _parse_value function for Float and Double types'''

    @staticmethod
    def _parse_value(value):
        if value is None or value == '':
            return None
        else:
            return float(value)


class Double(_FloatBase):
    _binding_class = common_binding.DoubleObjectPropertyType
    datatype = "double"
    default_datatype = "double"

class Float(_FloatBase):
    _binding_class = common_binding.FloatObjectPropertyType
    datatype = "float"
    default_datatype = "float"

class _LongBase(BaseProperty):
    '''Define a common _parse_value function for all Long types'''

    @staticmethod
    def _parse_value(value):
        if value is None or value == '':
            return None
        if isinstance(value, basestring):
            return long(value, 0)
        else:
            return long(value)


class Long(_LongBase):
    _binding_class = common_binding.LongObjectPropertyType
    datatype = "long"
    default_datatype = "long"

class UnsignedLong(_LongBase):
    _binding_class = common_binding.UnsignedLongObjectPropertyType
    datatype = "unsignedLong"
    default_datatype = "unsignedLong"

class Name(BaseProperty):
    _binding_class = common_binding.NameObjectPropertyType
    datatype = "name"
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
        common_binding.UnsignedLongObjectPropertyType: UnsignedLong,
        # This shouldn't be needed anymore, but we'll leave it here to be safe.
        common_binding.SimpleHashValueType: HexBinary,
#        common_binding.HashNameType: HashName,
    }
