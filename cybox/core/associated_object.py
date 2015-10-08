# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from cybox.core import Object
from cybox.common.vocabs import VocabFactory
import cybox.bindings.cybox_core as core_binding


# backwards compatibility
from cybox.common.vocabs import ActionObjectAssociationType as AssociationType  # noqa


class AssociatedObject(Object):
    """The CybOX Associated Object element.

    Currently only supports the id, association_type and ObjectProperties properties
    """
    _binding = core_binding
    _binding_class = _binding.AssociatedObjectType
    superclass = Object

    def __init__(self, defined_object=None, type_=None, association_type=None):
        super(AssociatedObject, self).__init__(defined_object, type_)
        self.association_type = association_type

    def to_obj(self, return_obj=None, ns_info=None):
        obj = super(AssociatedObject, self).to_obj(ns_info=ns_info)

        if self.association_type is not None:
            obj.Association_Type = self.association_type.to_obj(ns_info=ns_info)
        return obj

    def to_dict(self):
        object_dict = super(AssociatedObject, self).to_dict()
        if self.association_type is not None:
            object_dict['association_type'] = self.association_type.to_dict()
        return object_dict

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None
        obj = super(AssociatedObject, cls).from_obj(cls_obj)
        obj.association_type = VocabFactory.from_obj(cls_obj.Association_Type)
        return obj

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        obj = super(AssociatedObject, cls).from_dict(cls_dict)
        obj.association_type = VocabFactory.from_dict(cls_dict.get('association_type'))
        return obj
