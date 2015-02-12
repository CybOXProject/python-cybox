# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding


class StructuredText(cybox.Entity):
    _binding = common_binding
    _namespace = 'http://cybox.mitre.org/common-2'

    def __init__(self, value=None):
        super(StructuredText, self).__init__()
        self.value = value
        self.structuring_format = None

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = common_binding.StructuredTextType()

        return_obj.valueOf_ = self.value
        if self.structuring_format is not None:
            return_obj.structuring_format = self.structuring_format
        return return_obj

    def to_dict(self):
        # Shortcut if structuring_format is not defined.
        if self.is_plain():
            return self.value

        text_dict = {}
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
    def from_obj(cls, text_obj, text=None):
        if not text_obj:
            return None

        if not text:
            text = StructuredText()

        text.value = text_obj.valueOf_
        text.structuring_format = text_obj.structuring_format

        return text

    @classmethod
    def from_dict(cls, text_dict, text=None):
        if text_dict is None:
            return None

        if not text:
            text = StructuredText()

        if not isinstance(text_dict, dict):
            text.value = text_dict
        else:
            text.value = text_dict.get('value')
            text.structuring_format = text_dict.get('structuring_format')

        return text

    def __str__(self):
        return self.__unicode__().encode("utf-8")
    
    def __unicode__(self):
        return unicode(self.value)
