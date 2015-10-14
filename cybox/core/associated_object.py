# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from cybox.core import Object
from cybox.common.vocabs import VocabField
import cybox.bindings.cybox_core as core_binding

# backwards compatibility
from cybox.common.vocabs import ActionObjectAssociationType as AssociationType  # noqa


class AssociatedObject(Object):
    """The CybOX Associated Object element.

    Currently only supports the id, association_type and ObjectProperties properties
    """
    _binding = core_binding
    _binding_class = _binding.AssociatedObjectType

    association_type = VocabField("Association_Type", AssociationType)

    def __init__(self, defined_object=None, type_=None, association_type=None):
        super(AssociatedObject, self).__init__(defined_object, type_)
        self.association_type = association_type
