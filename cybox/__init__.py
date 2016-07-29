# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox.vendor import six

from .version import __version__  # noqa


#TODO: Should this get moved to mixbox or not?
class Unicode(entities.Entity):
    """Shim class to allow xs:string's in EntityList"""

    def __init__(self, value):
        super(Unicode, self).__init__()
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = six.text_type(value)

    def to_obj(self, ns_info=None):
        return self.value

    def to_dict(self):
        return self.value

    @classmethod
    def from_obj(cls, cls_obj):
        return cls(cls_obj)

    from_dict = from_obj
