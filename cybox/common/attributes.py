import cybox.bindings.cybox_common_types_1_0 as common_binding

import cybox


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

    def to_obj(self):
        AttrBindingClass = self._get_binding_class()

        attr_obj = AttrBindingClass()

        # Required
        attr_obj.set_valueOf_(self.value)
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
            attr_obj.set_value_set(self.value_set)
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
            return self.value

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
            attr_dict['value'] = self.value

        return attr_dict

    @staticmethod
    def from_obj(attr_obj):

        AttrClass = BINDING_CLASS_MAPPING.get(type(attr_obj))
        if not AttrClass:
            raise NotImplementedError("Attribute class %s not implemented" %
                                        str(type(attr_obj)))

        attr = AttrClass()
        attr.value = attr_obj.get_valueOf_()
        attr.datatype = attr_obj.get_datatype()

        attr.id_ = attr_obj.get_id()
        attr.idref = attr_obj.get_idref()
        attr.condition = attr_obj.get_condition()
        attr.pattern_type = attr_obj.get_pattern_type()
        attr.regex_syntax = attr_obj.get_regex_syntax()
        attr.start_range = attr_obj.get_start_range()
        attr.end_range = attr_obj.get_end_range()
        attr.value_set = attr_obj.get_value_set()
        attr.has_changed = attr_obj.get_has_changed()
        attr.trend = attr_obj.get_trend()
        attr.appears_random = attr_obj.get_appears_random()
        attr.is_obfuscated = attr_obj.get_is_obfuscated()
        attr.obfuscation_algorithm_ref = attr_obj.get_obfuscation_algorithm_ref()
        attr.is_defanged = attr_obj.get_is_defanged()
        attr.defanging_algorithm_ref = attr_obj.get_defanging_algorithm_ref()
        attr.refanging_transform_type = attr_obj.get_refanging_transform_type()
        attr.refanging_transform = attr_obj.get_refanging_transform()

        return attr

    @classmethod
    def from_dict(cls, attr_dict):
        # Use the subclass this was called on to initialize the object
        attr = cls()

        # If this attribute is "plain", use it as the value and assume the 
        # datatype was set correctly by the constructor of the particular
        # Attribute Subclass.
        if not isinstance(attr_dict, dict):
            attr.value = attr_dict
        else:
            # These keys should always be present
            attr.value = attr_dict.get('value')
            attr.datatype = attr_dict.get('datatype')

            # 'None' is fine if these keys are missing
            attr.id_ = attr_dict.get('id')
            attr.idref = attr_dict.get('idref')
            attr.condition = attr_dict.get('condition')
            attr.pattern_type = attr_dict.get('pattern_type')
            attr.regex_syntax = attr_dict.get('regex_syntax')
            attr.start_range = attr_dict.get('start_range')
            attr.end_range = attr_dict.get('end_range')
            attr.value_set = attr_dict.get('value_set')
            attr.has_changed = attr_dict.get('has_changed')
            attr.trend = attr_dict.get('trend')
            attr.appears_random = attr_dict.get('appears_random')
            attr.is_obfuscated = attr_dict.get('is_obfuscated')
            attr.obfuscation_algorithm_ref = attr_dict.get('obfuscation_algorithm_ref')
            attr.is_defanged = attr_dict.get('is_defanged')
            attr.defanging_algorithm_ref = attr_dict.get('defanging_algorithm_ref')
            attr.refanging_transform_type = attr_dict.get('refanging_transform_type')
            attr.refanging_transform = attr_dict.get('refanging_transform')

        return attr

    @classmethod
    def object_from_dict(cls, attr_dict):
        """Create the BaseObjectAttributeType object representation from an input dictionary"""
        return cls.from_dict(attr_dict).to_obj()

    @classmethod
    def dict_from_object(cls, attr_obj):
        """Parse and return a dictionary for the BaseObjectAttributeType"""
        return cls.from_obj(attr_obj).to_dict()


class String(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "String"

    def _get_binding_class(self):
        return common_binding.StringObjectAttributeType


class Integer(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "Integer"

    def _get_binding_class(self):
        return common_binding.IntegerObjectAttributeType


class AnyURI(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "AnyURI"

    def _get_binding_class(self):
        return common_binding.AnyURIObjectAttributeType


class HexBinary(Attribute):
    def __init__(self, *args, **kwargs):
        Attribute.__init__(self, *args, **kwargs)
        self.datatype = "HexBinary"

    def _get_binding_class(self):
        return common_binding.HexBinaryObjectAttributeType


# Mapping of binding classes to the corresponding Attribute subclass
BINDING_CLASS_MAPPING = {
        common_binding.StringObjectAttributeType: String,
        common_binding.IntegerObjectAttributeType: Integer,
        common_binding.AnyURIObjectAttributeType: AnyURI,
        common_binding.HexBinaryObjectAttributeType: HexBinary,
    }
