# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

DEFAULT_DELIM = "##comma##"

class PatternFieldGroup(object):
    """A mixin class for CybOX entities which are patternable."""

    def __init__(self):
        super(PatternFieldGroup, self).__init__()
        self.condition = None
        self.apply_condition = None
        self.bit_mask = None
        self.pattern_type = None
        self.regex_syntax = None
        self.has_changed = None
        self.trend = None
        self.is_case_sensitive = True
        self.delimiter = DEFAULT_DELIM

    def is_plain(self):
        return (
            self.condition is None and
            self.apply_condition in (None, "ANY") and
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

        if first.apply_condition in (None, "ANY") and \
                second.apply_condition in (None, "ANY"):
            return True

        return first.apply_condition == second.apply_condition


    def to_obj(self, ns_info=None):
        obj = super(PatternFieldGroup, self).to_obj(ns_info=ns_info)

        # Partial_obj is required since PatternFieldGroup is not a full Entity.
        if self.condition is not None:
            obj.condition = self.condition
            # Only add 'apply_condition' if 'condition' is set
            if self.apply_condition is not None and isinstance(self.value, list):
                obj.apply_condition = self.apply_condition
        else:
            obj.apply_condition = None
        if self.bit_mask is not None:
            obj.bit_mask = self.bit_mask
        if self.pattern_type is not None:
            obj.pattern_type = self.pattern_type
        if self.regex_syntax is not None:
            obj.regex_syntax = self.regex_syntax
        if self.has_changed is not None:
            obj.has_changed = self.has_changed
        if self.trend is not None:
            obj.trend = self.trend
        if self.is_case_sensitive is not True:
            obj.is_case_sensitive = self.is_case_sensitive
        else:
            obj.is_case_sensitive = None
        if self.delimiter is not DEFAULT_DELIM:
            obj.delimiter = self.delimiter

        return obj

    def to_dict(self):
        d = super(PatternFieldGroup, self).to_dict()

        # partial_dict is required since PatternFieldGroup is not a full Entity.
        if self.condition is not None:
            d['condition'] = self.condition
            # Only add 'apply_condition' if 'condition' is set
            if self.apply_condition is not None and isinstance(self.value, list):
                d['apply_condition'] = self.apply_condition
        if self.bit_mask is not None:
            d['bit_mask'] = self.bit_mask
        if self.pattern_type is not None:
            d['pattern_type'] = self.pattern_type
        if self.regex_syntax is not None:
            d['regex_syntax'] = self.regex_syntax
        if self.has_changed is not None:
            d['has_changed'] = self.has_changed
        if self.trend is not None:
            d['trend'] = self.trend
        if self.is_case_sensitive not in (None, True):
            d['is_case_sensitive'] = self.is_case_sensitive
        if self.delimiter not in (None, DEFAULT_DELIM):
            d['delimiter'] = self.delimiter

        return d

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(PatternFieldGroup, cls).from_obj(cls_obj)

        obj.condition = cls_obj.condition
        obj.apply_condition = cls_obj.apply_condition
        obj.bit_mask = cls_obj.bit_mask
        obj.pattern_type = cls_obj.pattern_type
        obj.regex_syntax = cls_obj.regex_syntax
        obj.has_changed = cls_obj.has_changed
        obj.trend = cls_obj.trend
        obj.is_case_sensitive = cls_obj.is_case_sensitive
        obj.delimiter = cls_obj.delimiter or DEFAULT_DELIM

        return obj

    @classmethod
    def from_dict(cls, cls_dict):
        obj = super(PatternFieldGroup, cls).from_dict(cls_dict)

        if not isinstance(cls_dict, dict):
            return obj

        obj.condition = cls_dict.get('condition')
        obj.apply_condition = cls_dict.get('apply_condition')
        obj.bit_mask = cls_dict.get('bit_mask')
        obj.pattern_type = cls_dict.get('pattern_type')
        obj.regex_syntax = cls_dict.get('regex_syntax')
        obj.has_changed = cls_dict.get('has_changed')
        obj.trend = cls_dict.get('trend')
        obj.is_case_sensitive = cls_dict.get('is_case_sensitive', True)
        obj.delimiter = cls_dict.get('delimiter', DEFAULT_DELIM)

        return obj