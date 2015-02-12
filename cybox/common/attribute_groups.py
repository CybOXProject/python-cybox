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


    def to_obj(self, return_obj, ns_info=None):
        self._collect_ns_info(ns_info)

        # Partial_obj is required since PatternFieldGroup is not a full Entity.
        if self.condition is not None:
            return_obj.condition = self.condition
            # Only add 'apply_condition' if 'condition' is set
            if self.apply_condition is not None and isinstance(self.value, list):
                return_obj.apply_condition = self.apply_condition
        else:
            return_obj.apply_condition = None
        if self.bit_mask is not None:
            return_obj.bit_mask = self.bit_mask
        if self.pattern_type is not None:
            return_obj.pattern_type = self.pattern_type
        if self.regex_syntax is not None:
            return_obj.regex_syntax = self.regex_syntax
        if self.has_changed is not None:
            return_obj.has_changed = self.has_changed
        if self.trend is not None:
            return_obj.trend = self.trend
        if self.is_case_sensitive is not True:
            return_obj.is_case_sensitive = self.is_case_sensitive
        else:
            return_obj.is_case_sensitive = None
        if self.delimiter is not DEFAULT_DELIM:
            return_obj.delimiter = self.delimiter

        # Do not return anything, since it is modifying partial_obj in place.

    def to_dict(self, partial_dict):
        # Partial_dict is required since PatternFieldGroup is not a full Entity.
        if self.condition is not None:
            partial_dict['condition'] = self.condition
            # Only add 'apply_condition' if 'condition' is set
            if self.apply_condition is not None and isinstance(self.value, list):
                partial_dict['apply_condition'] = self.apply_condition
        if self.bit_mask is not None:
            partial_dict['bit_mask'] = self.bit_mask
        if self.pattern_type is not None:
            partial_dict['pattern_type'] = self.pattern_type
        if self.regex_syntax is not None:
            partial_dict['regex_syntax'] = self.regex_syntax
        if self.has_changed is not None:
            partial_dict['has_changed'] = self.has_changed
        if self.trend is not None:
            partial_dict['trend'] = self.trend
        if self.is_case_sensitive not in (None, True):
            partial_dict['is_case_sensitive'] = self.is_case_sensitive
        if self.delimiter not in (None, DEFAULT_DELIM):
            partial_dict['delimiter'] = self.delimiter

        # Do not return anything, since it is modifying partial_dict in place.

    @staticmethod
    def from_obj(obj, partial):
        if not obj:
            return

        partial.condition = obj.condition
        partial.apply_condition = obj.apply_condition
        partial.bit_mask = obj.bit_mask
        partial.pattern_type = obj.pattern_type
        partial.regex_syntax = obj.regex_syntax
        partial.has_changed = obj.has_changed
        partial.trend = obj.trend
        partial.is_case_sensitive = obj.is_case_sensitive
        partial.delimiter = obj.delimiter or DEFAULT_DELIM

    @staticmethod
    def from_dict(dict_, partial):
        if not dict_:
            return

        partial.condition = dict_.get('condition')
        partial.apply_condition = dict_.get('apply_condition')
        partial.bit_mask = dict_.get('bit_mask')
        partial.pattern_type = dict_.get('pattern_type')
        partial.regex_syntax = dict_.get('regex_syntax')
        partial.has_changed = dict_.get('has_changed')
        partial.trend = dict_.get('trend')
        partial.is_case_sensitive = dict_.get('is_case_sensitive', True)
        partial.delimiter = dict_.get('delimiter', DEFAULT_DELIM)
