# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime

import dateutil.parser

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml
import cybox.xs as xs


class BaseProperty(PatternFieldGroup, cybox.Entity):
    # Most Properties are defined in the "common" binding, so we'll just set
    # that here. Some BaseProperty subclasses might have to override this.
    _binding = common_binding
    _namespace = 'http://cybox.mitre.org/common-2'

    # `value` and `datatype` are handled explicitly
    id_ = cybox.TypedField("id", xs.QName)
    idref = cybox.TypedField("idref", xs.QName)
    appears_random = cybox.TypedField('appears_random', xs.boolean)
    is_obfuscated = cybox.TypedField('is_obfuscated', xs.boolean)
    obfuscation_algorithm_ref = \
            cybox.TypedField('obfuscation_algorithm_ref', xs.AnyURI)
    is_defanged = cybox.TypedField('is_defanged', xs.boolean)
    defanging_algorithm_ref = \
            cybox.TypedField('defanging_algorithm_ref', xs.AnyURI)
    refanging_transform_type = \
            cybox.TypedField('refanging_transform_type', xs.string)
    refanging_transform = cybox.TypedField('refanging_transform', xs.string)

    def __init__(self, value=None):
        super(BaseProperty, self).__init__()
        self.value = value
        #Variable for forcing output of the datatype; necessary for certain cases
        self._force_datatype = False

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

            PatternFieldGroup._conditions_equal(self, other) and

            self.bit_mask == other.bit_mask and
            self.pattern_type == other.pattern_type and
            self.regex_syntax == other.regex_syntax and
            self.has_changed == other.has_changed and
            self.trend == other.trend
        )

    def __ne__(self, other):
        return not (self == other)

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

            PatternFieldGroup.is_plain(self)
        )

    def __nonzero__(self):
        return (not self.is_plain()) or (self.value is not None)

    __bool__ = __nonzero__

    def to_obj(self):
        property_obj = super(BaseProperty, self).to_obj()

        property_obj.set_valueOf_(normalize_to_xml(self.serialized_value))

        # Determine whether it's necessary to output "datatype"
        if self._force_datatype:
            property_obj.set_datatype(self.datatype)
        else:
            property_obj.set_datatype(None)

        return property_obj

    def to_dict(self):
        if self.is_plain():
            return self.serialized_value

        property_dict = super(BaseProperty, self).to_dict()

        property_dict['value'] = self.serialized_value

        # For now, don't output the datatype, as it is not required and is
        # usually not needed, as it can be inferred from the context.
        #if self.datatype is not None:
        #    property_dict['datatype'] = self.datatype

        return property_dict

    @classmethod
    def from_obj(cls, property_obj):
        if not property_obj:
            return None

        property_ = super(BaseProperty, cls).from_obj(property_obj)
        property_.value = denormalize_from_xml(property_obj.get_valueOf_())
        return property_

    @classmethod
    def from_dict(cls, property_dict):
        if property_dict is None:
            return None

        if not isinstance(property_dict, dict):
            property_ = cls()
            property_.value = property_dict
        else:
            property_ = super(BaseProperty, cls).from_dict(property_dict)
            # This key should always be present
            property_.value = property_dict.get('value')
            property_._force_datatype = property_dict.get('force_datatype',
                                                          False)

        return property_


class String(BaseProperty):
    _binding_class = common_binding.StringObjectPropertyType
    datatype = "string"

    @staticmethod
    def _parse_value(value):
        if value is not None and not isinstance(value, basestring):
            raise ValueError("Cannot set String type to non-string value")

        return value

# TODO: consolidate _parse_value functions on Numeric types


class UnsignedLong(BaseProperty):
    _binding_class = common_binding.UnsignedLongObjectPropertyType
    datatype = "unsignedLong"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return long(value, 0)
        else:
            return long(value)


class Integer(BaseProperty):
    _binding_class = common_binding.IntegerObjectPropertyType
    datatype = "integer"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return int(value, 0)
        else:
            return int(value)


class PositiveInteger(BaseProperty):
    _binding_class = common_binding.PositiveIntegerObjectPropertyType
    datatype = "positiveInteger"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return int(value, 0)
        else:
            return int(value)


class UnsignedInteger(BaseProperty):
    _binding_class = common_binding.UnsignedIntegerObjectPropertyType
    datatype = "unsignedInt"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return int(value, 0)
        else:
            return int(value)


class NonNegativeInteger(BaseProperty):
    _binding_class = common_binding.NonNegativeIntegerObjectPropertyType
    datatype = "nonNegativeInteger"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return int(value, 0)
        else:
            return int(value)


class AnyURI(BaseProperty):
    _binding_class = common_binding.AnyURIObjectPropertyType
    datatype = "anyURI"


class HexBinary(BaseProperty):
    _binding_class = common_binding.HexBinaryObjectPropertyType
    datatype = "hexBinary"


class Base64Binary(BaseProperty):
    _binding_class = common_binding.Base64BinaryObjectPropertyType
    datatype = "base64Binary"


class Duration(BaseProperty):
    _binding_class = common_binding.DurationObjectPropertyType
    datatype = "duration"


class Time(BaseProperty):
    _binding_class = common_binding.TimeObjectPropertyType
    datatype = "time"


class Date(BaseProperty):
    _binding_class = common_binding.DateObjectPropertyType
    datatype = "date"


class DateTime(BaseProperty):
    _binding_class = common_binding.DateTimeObjectPropertyType
    datatype = "dateTime"

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


class Double(BaseProperty):
    _binding_class = common_binding.DoubleObjectPropertyType
    datatype = "double"


class Float(BaseProperty):
    _binding_class = common_binding.FloatObjectPropertyType
    datatype = "float"


class Long(BaseProperty):
    _binding_class = common_binding.LongObjectPropertyType
    datatype = "long"

    @staticmethod
    def _parse_value(value):
        if value is None:
            return None
        if isinstance(value, basestring):
            return long(value, 0)
        else:
            return long(value)

class Name(BaseProperty):
    _binding_class = common_binding.NameObjectPropertyType
    datatype = "name"

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
