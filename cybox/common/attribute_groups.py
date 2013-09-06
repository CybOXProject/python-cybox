# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.xs as xs


class PatternFieldGroup(object):
    """A mixin class for CybOX entities which are patternable."""

    condition = cybox.TypedField('condition', xs.Enum)
    apply_condition = cybox.TypedField('apply_condition', xs.Enum)
    bit_mask = cybox.TypedField('bit_mask', xs.hexBinary)
    pattern_type = cybox.TypedField('pattern_type', xs.Enum)
    regex_syntax = cybox.TypedField('regex_syntax', xs.string)
    has_changed = cybox.TypedField('has_changed', xs.boolean)
    trend = cybox.TypedField('trend', xs.boolean)

    def is_plain(self):
        return (
            self.condition is None and
            self.apply_condition in (None, "ANY") and
            self.bit_mask is None and
            self.pattern_type is None and
            self.regex_syntax is None and
            self.has_changed is None and
            self.trend is None
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

    def _include_apply_condition(self):
        """Determine whether to include `apply_condition` on output.

        We only include it if:
        - this is meant to be a pattern rather than an instance (as indicated
          by the presence of the `condition` attribute).
        - `apply_condition` has been set.
        - the value of the Property is a list.
        """
        return (self.condition and
                self.apply_condition and
                isinstance(self.value, list))

    def to_obj(self):
        entity_obj = super(PatternFieldGroup, self).to_obj()

        # Remove apply_condition if needed
        if not self._include_apply_condition():
            entity_obj.set_apply_condition(None)

        return entity_obj

    def to_dict(self):
        entity_dict = super(PatternFieldGroup, self).to_dict()

        # Remove apply_condition if needed
        if (not self._include_apply_condition() and
                'apply_condition' in entity_dict):
            del entity_dict['apply_condition']

        return entity_dict
