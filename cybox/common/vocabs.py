# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import PatternFieldGroup
from cybox.utils import normalize_to_xml, denormalize_from_xml

INVALID_XSI_TYPE = "bad_xsi_type"


class VocabString(PatternFieldGroup, cybox.Entity):
    _namespace = 'http://cybox.mitre.org/default_vocabularies-2'
    # All subclasses should override this
    _XSI_TYPE = INVALID_XSI_TYPE

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE

        self.vocab_name = None
        self.vocab_reference = None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        # Check to make sure the values are identical.
        if isinstance(other, VocabString):
            other = other.value

        return other == self.value

    def is_plain(self):
        """Whether the VocabString can be represented as a single value.

        If `value` is the only non-None properties and a custom XSI type has
        not been set, the VocabString can be represented by a single value
        rather than a dictionary. This makes the JSON representation simpler
        without losing any data fidelity.
        """
        return (
            # ignore value
            self.vocab_name is None and
            self.vocab_reference is None and
            self.xsi_type == self._XSI_TYPE and

            PatternFieldGroup.is_plain(self)
        )

    def is_valid(self):
        """For a vocab string to be valid, it must have an xsi:type, a
        vocab_name, or a vocab_reference."""
        return (
            self.xsi_type != INVALID_XSI_TYPE or
            self.vocab_name is not None or
            self.vocab_reference is not None
        )

    def to_obj(self, return_obj=None, ns_info=None):
        if not self.is_valid():
            raise ValueError("Vocab being used has not been specified")

        self._collect_ns_info(ns_info)
        vocab_obj = common_binding.ControlledVocabularyStringType()

        vocab_obj.valueOf_ = normalize_to_xml(self.value, self.delimiter)
        vocab_obj.xsi_type = self.xsi_type

        if self.vocab_name is not None:
            vocab_obj.vocab_name = self.vocab_name
        if self.vocab_reference is not None:
            vocab_obj.vocab_reference = self.vocab_reference

        PatternFieldGroup.to_obj(self, return_obj=vocab_obj, ns_info=ns_info)

        return vocab_obj

    def to_dict(self):
        if not self.is_valid():
            raise ValueError("Vocab being used has not been specified")

        if self.is_plain():
            return self.value

        vocab_dict = {}
        if self.value is not None:
            vocab_dict['value'] = self.value
        if self.xsi_type != self._XSI_TYPE:
            vocab_dict['xsi:type'] = self.xsi_type
        if self.vocab_name is not None:
            vocab_dict['vocab_name'] = self.vocab_name
        if self.vocab_reference is not None:
            vocab_dict['vocab_reference'] = self.vocab_reference

        PatternFieldGroup.to_dict(self, vocab_dict)

        return vocab_dict

    @classmethod
    def from_obj(cls, vocab_obj):
        if not vocab_obj:
            return None

        vocab_str = cls()
        # xsi_type should be set automatically by the class's constructor.

        vocab_str.vocab_name = vocab_obj.vocab_name
        vocab_str.vocab_reference = vocab_obj.vocab_reference
        vocab_str.xsi_type = vocab_obj.xsi_type

        PatternFieldGroup.from_obj(vocab_obj, vocab_str)

        # We need to check for a non-default delimiter before trying to parse
        # the value.
        vocab_str.value = denormalize_from_xml(vocab_obj.valueOf_,
                                               vocab_str.delimiter)

        return vocab_str

    @classmethod
    def from_dict(cls, vocab_dict):
        if not vocab_dict:
            return None

        vocab_str = cls()
        # xsi_type should be set automatically by the class's constructor.

        # In case this is a "plain" string, just set it.
        if not isinstance(vocab_dict, dict):
            vocab_str.value = vocab_dict
        else:
            vocab_str.xsi_type = vocab_dict.get('xsi:type', cls._XSI_TYPE)
            vocab_str.value = vocab_dict.get('value')
            vocab_str.vocab_name = vocab_dict.get('vocab_name')
            vocab_str.vocab_reference = vocab_dict.get('vocab_reference')

            PatternFieldGroup.from_dict(vocab_dict, vocab_str)

        return vocab_str
