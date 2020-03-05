# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.library_object as library_binding
from cybox.common.extracted_features import ExtractedFeatures
from cybox.common import BaseProperty, ObjectProperties, String, UnsignedLong, HexBinary


class LibraryType(BaseProperty):
    _binding = library_binding
    _binding_class = library_binding.LibraryType
    _namespace = "http://cybox.mitre.org/objects#LibraryObject-2"
    default_datatype = "string"

    TYPE_DYNAMIC = "Dynamic"
    TYPE_STATIC = "Static"
    TYPE_REMOTE = "Remote"
    TYPE_SHARED = "Shared"
    TYPE_OTHER = "Other"


class Library(ObjectProperties):
    _binding = library_binding
    _binding_class = library_binding.LibraryObjectType
    _namespace = "http://cybox.mitre.org/objects#LibraryObject-2"
    _XSI_NS = "LibraryObj"
    _XSI_TYPE = "LibraryObjectType"

    name = fields.TypedField("Name", String)
    path = fields.TypedField("Path", String)
    size = fields.TypedField("Size", UnsignedLong)
    type_ = fields.TypedField("Type", LibraryType)
    version = fields.TypedField("Version", String)
    base_address = fields.TypedField("Base_Address", HexBinary)
    extracted_features = fields.TypedField("Extracted_Features", ExtractedFeatures)
