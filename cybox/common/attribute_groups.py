# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

DEFAULT_DELIM = "##comma##"
DEFAULT_APPLY_CONDITION = "ANY"


class PatternFieldGroup(object):
    """A mixin class for CybOX entities which are patternable."""

    condition = fields.TypedField("condition")
    apply_condition = fields.TypedField("apply_condition")
    bit_mask = fields.TypedField("bit_mask")
    pattern_type = fields.TypedField("pattern_type")
    regex_syntax = fields.TypedField("regex_syntax")
    has_changed = fields.TypedField("has_changed")
    trend = fields.TypedField("trend")
    is_case_sensitive = fields.TypedField("is_case_sensitive")
    delimiter = fields.TypedField("delimiter")

    def __init__(self):
        super(PatternFieldGroup, self).__init__()
        self.is_case_sensitive = True
        self.delimiter = DEFAULT_DELIM
        self.apply_condition = DEFAULT_APPLY_CONDITION

    def is_plain(self):
        return (
            self.condition is None and
            self.apply_condition in (None, DEFAULT_APPLY_CONDITION) and
            self.bit_mask is None and
            self.pattern_type is None and
            self.regex_syntax is None and
            self.has_changed is None and
            self.trend is None and
            self.is_case_sensitive in (None, True) and
            self.delimiter in (None, DEFAULT_DELIM)
        )

    @staticmethod
    def _conditions_equal(first, second):
        if first.condition is None and second.condition is None:
            return True

        if first.condition != second.condition:
            return False

        if (first.apply_condition in (None, DEFAULT_APPLY_CONDITION) and
            second.apply_condition in (None, DEFAULT_APPLY_CONDITION)):
            return True

        return first.apply_condition == second.apply_condition

    def _apply_condition_xml_value(self):
        if self.condition is None:
            return None
        elif self.apply_condition is not None and isinstance(self.value, list):
            return self.apply_condition
        else:
            return DEFAULT_APPLY_CONDITION

    def _apply_condition_dict_value(self):
        if self.condition is None:
            return None
        elif self.apply_condition is not None and isinstance(self.value, list):
            return self.apply_condition
        else:
            return None

    def to_obj(self, ns_info=None):
        obj = super(PatternFieldGroup, self).to_obj(ns_info=ns_info)
        obj.apply_condition = self._apply_condition_xml_value()

        if self.is_case_sensitive is not True:
            obj.is_case_sensitive = self.is_case_sensitive
        else:
            obj.is_case_sensitive = None

        if self.delimiter is not DEFAULT_DELIM:
            obj.delimiter = self.delimiter

        return obj

    def to_dict(self):
        d = super(PatternFieldGroup, self).to_dict()

        # Custom processing of these dictionary items. Unset them and re-add
        # if necessary.
        d.pop("is_case_sensitive", None)
        d.pop("delimiter", None)
        d.pop("apply_condition", None)

        if self.is_case_sensitive not in (None, True):
            d['is_case_sensitive'] = self.is_case_sensitive
        if self.delimiter not in (None, DEFAULT_DELIM):
            d['delimiter'] = self.delimiter
        if self._apply_condition_dict_value():
            d["apply_condition"] = self._apply_condition_dict_value()

        return d

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(PatternFieldGroup, cls).from_obj(cls_obj)
        obj.delimiter = cls_obj.delimiter or DEFAULT_DELIM
        obj.apply_condition = cls_obj.apply_condition or DEFAULT_APPLY_CONDITION

        return obj

    @classmethod
    def from_dict(cls, cls_dict):
        obj = super(PatternFieldGroup, cls).from_dict(cls_dict)

        if not isinstance(cls_dict, dict):
            return obj

        obj.is_case_sensitive = cls_dict.get('is_case_sensitive', True)
        obj.delimiter = cls_dict.get('delimiter', DEFAULT_DELIM)
        obj.apply_condition = cls_dict.get('apply_condition', DEFAULT_APPLY_CONDITION)

        return obj