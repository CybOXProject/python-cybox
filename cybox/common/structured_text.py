# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox.vendor import six

import cybox.bindings.cybox_common as common_binding


@six.python_2_unicode_compatible
class StructuredText(entities.Entity):
    _binding = common_binding
    _binding_class = _binding.StructuredTextType
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, value=None):
        super(StructuredText, self).__init__()
        self.value = value
        self.structuring_format = None

    def to_obj(self, ns_info=None):
        return_obj = super(StructuredText, self).to_obj(ns_info=ns_info)
        return_obj.valueOf_ = self.value
        if self.structuring_format is not None:
            return_obj.structuring_format = self.structuring_format
        return return_obj

    def to_dict(self):
        # Shortcut if structuring_format is not defined.
        if self.is_plain():
            return self.value

        text_dict = super(StructuredText, self).to_dict()
        text_dict['value'] = self.value
        text_dict['structuring_format'] = self.structuring_format

        return text_dict

    def is_plain(self):
        """Whether this can be represented as a string rather than a dictionary

        Subclasses can override this to include their custom fields in this
        check:

            return (super(..., self).is_plain() and self.other_field is None)
        """
        return (self.structuring_format is None)

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        text = super(StructuredText, cls).from_obj(cls_obj)
        text.value = cls_obj.valueOf_
        text.structuring_format = cls_obj.structuring_format

        return text

    @classmethod
    def from_dict(cls, cls_dict):
        if cls_dict is None:
            return None

        text = super(StructuredText, cls).from_dict(cls_dict)

        if not isinstance(cls_dict, dict):
            text.value = cls_dict
        else:
            text.value = cls_dict.get('value')
            text.structuring_format = cls_dict.get('structuring_format')

        return text

    def __str__(self):
        return six.text_type(self.value)
