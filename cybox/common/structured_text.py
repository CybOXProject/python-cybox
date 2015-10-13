# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields
from mixbox.vendor import six

import cybox.bindings.cybox_common as common_binding


@six.python_2_unicode_compatible
class StructuredText(entities.Entity):
    _binding = common_binding
    _binding_class = _binding.StructuredTextType
    _namespace = 'http://cybox.mitre.org/common-2'

    value = fields.TypedField("valueOf_", key_name="value")
    structuring_format = fields.TypedField("structuring_format")

    def __init__(self, value=None):
        super(StructuredText, self).__init__()
        self.value = value

    def to_dict(self):
        # Shortcut if structuring_format is not defined.
        if self.is_plain():
            return self.value
        return super(StructuredText, self).to_dict()

    def is_plain(self):
        """Whether this can be represented as a string rather than a dictionary

        Subclasses can override this to include their custom fields in this
        check:

            return (super(..., self).is_plain() and self.other_field is None)
        """
        return (self.structuring_format is None)

    def __str__(self):
        return six.text_type(self.value)
