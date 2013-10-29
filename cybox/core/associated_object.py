# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_core as core_binding
from cybox.common import VocabString
from cybox.core import Object


class AssociationType(VocabString):
    _XSI_TYPE = 'cyboxVocabs:ActionObjectAssociationTypeVocab-1.0'


class AssociatedObject(Object):
    """The CybOX Associated Object element.

    Currently only supports the id, association_type and ObjectProperties properties
    """

    superclass = Object

    def __init__(self, type_=None, association_type=None, defined_object=None):
        super(AssociatedObject, self).__init__(type_, defined_object)
        self.association_type = association_type

    def to_obj(self):
        obj = super(AssociatedObject, self).to_obj(core_binding.AssociatedObjectType())
        if self.association_type is not None:
            obj.set_Association_Type(self.association_type.to_obj())
        return obj

    def to_dict(self):
        object_dict = super(AssociatedObject, self).to_dict()
        if self.association_type is not None:
            object_dict['association_type'] = self.association_type.to_dict()
        return object_dict

    @staticmethod
    def from_obj(object_obj):
        if not object_obj:
            return None
        obj = Object.from_obj(object_obj, AssociatedObject())
        obj.association_type = AssociationType.from_obj(object_obj.get_Association_Type())
        return obj

    @staticmethod
    def from_dict(object_dict):
        if not object_dict:
            return None
        obj = Object.from_dict(object_dict, AssociatedObject())
        obj.association_type = AssociationType.from_dict(object_dict.get('association_type', None))
        return obj
