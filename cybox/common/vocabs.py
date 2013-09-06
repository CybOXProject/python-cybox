# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml
import cybox.xs as xs


class VocabString(PatternFieldGroup, cybox.Entity):
    #TODO: use a different binding class for each type of string
    _binding_class = common_binding.ControlledVocabularyStringType
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'

    # All subclasses should override this
    _XSI_TYPE = "BAD_XSI_TYPE"

    vocab_name = cybox.TypedField("vocab_name", xs.string)
    vocab_reference = cybox.TypedField("vocab_reference", xs.AnyURI)

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        # Check to make sure the values are identical.
        if isinstance(other, VocabString):
            other = other.value

        return other == self.value

    def is_plain(self):
        """Whether the VocabString can be represented as a single value.

        If `value` is the only non-None properties, the VocabString can be
        represented by a single value rather than a dictionary. This makes the
        JSON representation simpler without losing any data fidelity.
        """
        return (
            # ignore value
            self.vocab_name is None and
            self.vocab_reference is None and

            PatternFieldGroup.is_plain(self)
        )

    def to_obj(self):
        vocab_obj = super(VocabString, self).to_obj()
        vocab_obj.set_valueOf_(normalize_to_xml(self.value))
        vocab_obj.set_xsi_type(self._XSI_TYPE)

        return vocab_obj

    def to_dict(self):
        if self.is_plain():
            return self.value

        vocab_dict = super(VocabString, self).to_dict()
        vocab_dict['value'] = self.value
        vocab_dict['xsi:type'] = self._XSI_TYPE

        return vocab_dict

    @classmethod
    def from_obj(cls, vocab_obj):
        if not vocab_obj:
            return None

        vocab_str = super(VocabString, cls).from_obj(vocab_obj)
        vocab_str.value = denormalize_from_xml(vocab_obj.get_valueOf_())

        return vocab_str

    @classmethod
    def from_dict(cls, vocab_dict):
        if not vocab_dict:
            return None

        if not isinstance(vocab_dict, dict):
            vocab_str = cls()
            vocab_str.value = vocab_dict
        else:
            vocab_str = super(VocabString, cls).from_dict(vocab_dict)
            vocab_str.value = vocab_dict.get('value')

        return vocab_str
