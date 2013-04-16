from datetime import datetime

import dateutil.parser

import cybox
import cybox.bindings.cybox_common_types_1_0 as common_binding

VALUE_SET_DELIMITER = ','


class Attribute(cybox.Entity):

    def __init__(self, value=None):
        self.value = value

        self.id_ = None
        self.idref = None
        self.datatype = None
        self.condition = None
        self.pattern_type = None
        self.regex_syntax = None
        self.start_range = None
        self.end_range = None
        self.value_set = None
        self.has_changed = None
        self.trend = None
        self.appears_random = None
        self.is_obfuscated = None
        self.obfuscation_algorithm_ref = None
        self.is_defanged = None
        self.defanging_algorithm_ref = None
        self.refanging_transform_type = None
        self.refanging_transform = None

    def __str__(self):
        return str(self._serialize_value())

    def __int__(self):
        return int(self._serialize_value())

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value_):
        # This is done here, so the value is always parsed, regardless of
        # whether it is set via the __init__() function, via the from_*
        # static methods, or on an instance of the class after it has been
        # created.
        self._value = self._parse_value(value_)

    @property
    def value_set(self):
        return self._value_set

    @value_set.setter
    def value_set(self, value):
        if (value is not None) and (not isinstance(value, list)):
            if VALUE_SET_DELIMITER in value:
                value = value.split(VALUE_SET_DELIMITER)
            else:
                value = [value]
        self._value_set = value

    def _parse_value(self, value):
        """Parse a user-supplied value into the internal representation.

        For most Attribute types, this does not modify `value`. However,
        some attributes may have a more specific representation.
        """
        return value

    def _serialize_value(self):
        """Format the `value` for serialization (XML, JSON).

        For most attribute types, this will return the `value` unmodified.
        However, some attributes types may need additional formatting.
        """
        return self.value

    def __eq__(self, other):
        # It is possible to compare an Attribute to a single value if
        # the Attribute defines only the "value" property.
        if not isinstance(other, Attribute) and self.is_plain():
            return self.value == other

        return (
            self.value == other.value and
            self.id_ == other.id_ and
            self.idref == other.idref and
            self.datatype == other.datatype and
            self.condition == other.condition and
            self.pattern_type == other.pattern_type and
            self.regex_syntax == other.regex_syntax and
            self.start_range == other.start_range and
            self.end_range == other.end_range and
            self.value_set == other.value_set and
            self.has_changed == other.has_changed and
            self.trend == other.trend and
            self.appears_random == other.appears_random and
            self.is_obfuscated == other.is_obfuscated and
            self.obfuscation_algorithm_ref == other.obfuscation_algorithm_ref and
            self.is_defanged == other.is_defanged and
            self.defanging_algorithm_ref == other.defanging_algorithm_ref and
            self.refanging_transform_type == other.refanging_transform_type and
            self.refanging_transform == other.refanging_transform
        )

    def __ne__(self, other):
        return not (self == other)

    def is_plain(self):
        """Whether the Attribute can be represented as a single value.

        The `datatype` can be inferred by the particular Attribute subclass,
        so if `datatype` and `value` are the only non-None properties, the
        Attribute can be represented by a single value rather than a
        dictionary. This makes the JSON representation simpler without losing
        any data fidelity.
        """
        return (self.id_ is None and
                self.idref is None and
                self.condition is None and
                self.pattern_type is None and
                self.regex_syntax is None and
                self.start_range is None and
                self.end_range is None and
                self.value_set is None and
                self.has_changed is None and
                self.trend is None and
                self.appears_random is None and
                self.is_obfuscated is None and
                self.obfuscation_algorithm_ref is None and
                self.is_defanged is None and
                self.defanging_algorithm_ref is None and
                self.refanging_transform_type is None and
                self.refanging_transform is None)

    def _get_binding_class(self):
        """Each subclass must specify the class from the CybOX Common binding
        which used to represent that attribute type.

        Returns a class.
        """
        raise NotImplementedError

    def __nonzero__(self):
        return (not self.is_plain()) or (self.value is not None)

    __bool__ = __nonzero__

    def to_obj(self):
        AttrBindingClass = self._get_binding_class()

        attr_obj = AttrBindingClass()

        # Required
        attr_obj.set_valueOf_(self._serialize_value())
        attr_obj.set_datatype(self.datatype)

        # Optional
        if self.id_ is not None:
            attr_obj.set_id(self.id_)
        if self.idref is not None:
            attr_obj.set_idref(self.idref)
        if self.condition is not None:
            attr_obj.set_condition(self.condition)
        if self.pattern_type is not None:
            attr_obj.set_pattern_type(self.pattern_type)
        if self.regex_syntax is not None:
            attr_obj.set_regex_syntax(self.regex_syntax)
        if self.start_range is not None:
            attr_obj.set_start_range(self.start_range)
        if self.end_range is not None:
            attr_obj.set_end_range(self.end_range)
        if self.value_set is not None:
            attr_obj.set_value_set(VALUE_SET_DELIMITER.join(self.value_set))
        if self.has_changed is not None:
            attr_obj.set_has_changed(self.has_changed)
        if self.trend is not None:
            attr_obj.set_trend(self.trend)
        if self.appears_random is not None:
            attr_obj.set_appears_random(self.appears_random)
        if self.is_obfuscated is not None:
            attr_obj.set_is_obfuscated(self.is_obfuscated)
        if self.obfuscation_algorithm_ref is not None:
            attr_obj.set_obfuscation_algorithm_ref(self.obfuscation_algorithm_ref)
        if self.is_defanged is not None:
            attr_obj.set_is_defanged(self.is_defanged)
        if self.defanging_algorithm_ref is not None:
            attr_obj.set_defanging_algorithm_ref(self.defanging_algorithm_ref)
        if self.refanging_transform_type is not None:
            attr_obj.set_refanging_transform_type(self.refanging_transform_type)
        if self.refanging_transform is not None:
            attr_obj.set_refanging_transform(self.refanging_transform)

        return attr_obj

    def to_dict(self):
        if self.is_plain():
            return self._serialize_value()

        attr_dict = {}
        if self.id_ is not None:
            attr_dict['id'] = self.id_
        if self.idref is not None:
            attr_dict['idref'] = self.idref
        if self.datatype is not None:
            attr_dict['datatype'] = self.datatype
        if self.condition is not None:
            attr_dict['condition'] = self.condition
        if self.pattern_type is not None:
            attr_dict['pattern_type'] = self.pattern_type
        if self.regex_syntax is not None:
            attr_dict['regex_syntax'] = self.regex_syntax
        if self.start_range is not None:
            attr_dict['start_range'] = self.start_range
        if self.end_range is not None:
            attr_dict['end_range'] = self.end_range
        if self.value_set is not None:
            attr_dict['value_set'] = self.value_set
        if self.has_changed is not None:
            attr_dict['has_changed'] = self.has_changed
        if self.trend is not None:
            attr_dict['trend'] = self.trend
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
        if self.value is not None:
            attr_dict['value'] = self._serialize_value()

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
        self.value = attr_obj.get_valueOf_()
        self.datatype = attr_obj.get_datatype()
        self.id_ = attr_obj.get_id()
        self.idref = attr_obj.get_idref()
        self.condition = attr_obj.get_condition()
        self.pattern_type = attr_obj.get_pattern_type()
        self.regex_syntax = attr_obj.get_regex_syntax()
        self.start_range = attr_obj.get_start_range()
        self.end_range = attr_obj.get_end_range()
        self.value_set = attr_obj.get_value_set()
        self.has_changed = attr_obj.get_has_changed()
        self.trend = attr_obj.get_trend()
        self.appears_random = attr_obj.get_appears_random()
        self.is_obfuscated = attr_obj.get_is_obfuscated()
        self.obfuscation_algorithm_ref = attr_obj.get_obfuscation_algorithm_ref()
        self.is_defanged = attr_obj.get_is_defanged()
        self.defanging_algorithm_ref = attr_obj.get_defanging_algorithm_ref()
        self.refanging_transform_type = attr_obj.get_refanging_transform_type()
        self.refanging_transform = attr_obj.get_refanging_transform()

    @classmethod
    def from_dict(cls, attr_dict):
        # Subclasses with additional fields should override this method
        # and use _populate_from_dict as necessary.

        if not attr_dict:
            return None

        # Use the subclass this was called on to initialize the object.
        attr = cls()
        attr._populate_from_dict(attr_dict)
        return attr

    def _populate_from_dict(self, attr_dict):
        # If this attribute is "plain", use it as the value and assume the
        # datatype was set correctly by the constructor of the particular
        # Attribute Subclass.
        if not isinstance(attr_dict, dict):
            self.value = attr_dict
        else:
            # These keys should always be present
            self.value = attr_dict.get('value')
            self.datatype = attr_dict.get('datatype')

            # 'None' is fine if these keys are missing
            self.id_ = attr_dict.get('id')
            self.idref = attr_dict.get('idref')
            self.condition = attr_dict.get('condition')
            self.pattern_type = attr_dict.get('pattern_type')
            self.regex_syntax = attr_dict.get('regex_syntax')
            self.start_range = attr_dict.get('start_range')
            self.end_range = attr_dict.get('end_range')
            self.value_set = attr_dict.get('value_set')
            self.has_changed = attr_dict.get('has_changed')
            self.trend = attr_dict.get('trend')
            self.appears_random = attr_dict.get('appears_random')
            self.is_obfuscated = attr_dict.get('is_obfuscated')
            self.obfuscation_algorithm_ref = attr_dict.get('obfuscation_algorithm_ref')
            self.is_defanged = attr_dict.get('is_defanged')
            self.defanging_algorithm_ref = attr_dict.get('defanging_algorithm_ref')
            self.refanging_transform_type = attr_dict.get('refanging_transform_type')
            self.refanging_transform = attr_dict.get('refanging_transform')


class String(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "String"

    def _get_binding_class(self):
        return common_binding.StringObjectAttributeType


class UnsignedLong(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "UnsignedLong"

    def _get_binding_class(self):
        return common_binding.UnsignedLongObjectAttributeType


class Integer(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "Integer"

    def _get_binding_class(self):
        return common_binding.IntegerObjectAttributeType


class PositiveInteger(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "PositiveInteger"

    def _get_binding_class(self):
        return common_binding.PositiveIntegerObjectAttributeType


class UnsignedInteger(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "UnsignedInt"

    def _get_binding_class(self):
        return common_binding.UnsignedIntegerObjectAttributeType


class AnyURI(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "AnyURI"

    def _get_binding_class(self):
        return common_binding.AnyURIObjectAttributeType


class HexBinary(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "hexBinary"

    def _get_binding_class(self):
        return common_binding.HexBinaryObjectAttributeType

class Duration(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "Duration"

    def _get_binding_class(self):
        return common_binding.DurationObjectAttributeType

class DateTime(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "DateTime"

    def _get_binding_class(self):
        return common_binding.DateTimeObjectAttributeType

    def _parse_value(self, value):
        if not value:
            return None
        elif isinstance(value, datetime):
            return value
        return dateutil.parser.parse(value)

    def _serialize_value(self):
        if not self.value:
            return None
        return self.value.isoformat()


class SimpleHashValue(HexBinary):
    def _get_binding_class(self):
        return common_binding.SimpleHashValueType


class HashName(String):
    def _get_binding_class(self):
        return common_binding.HashNameType

# Mapping of binding classes to the corresponding Attribute subclass
BINDING_CLASS_MAPPING = {
        common_binding.StringObjectAttributeType: String,
        common_binding.IntegerObjectAttributeType: Integer,
        common_binding.PositiveIntegerObjectAttributeType: PositiveInteger,
        common_binding.UnsignedIntegerObjectAttributeType: UnsignedInteger,
        common_binding.UnsignedLongObjectAttributeType: UnsignedLong,
        common_binding.AnyURIObjectAttributeType: AnyURI,
        common_binding.HexBinaryObjectAttributeType: HexBinary,
        common_binding.DateTimeObjectAttributeType: DateTime,
        common_binding.DurationObjectAttributeType: Duration,
        common_binding.SimpleHashValueType: SimpleHashValue,
        common_binding.HashNameType: HashName,
    }
