# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.library_object as library_binding
from cybox.common.extracted_features import ExtractedFeatures
from cybox.common import ObjectProperties, HashList, String, UnsignedLong, HexBinary

class Library(ObjectProperties):
    _binding = library_binding
    _binding_class = library_binding.LibraryObjectType
    _namespace = "http://cybox.mitre.org/objects#LibraryObject-2"
    _XSI_NS = "LibraryObj"
    _XSI_TYPE = "LibraryObjectType"

    name = cybox.TypedField("Name", String)
    path = cybox.TypedField("Path", String)
    size = cybox.TypedField("Size", UnsignedLong)
    type_ = cybox.TypedField("Type", String)
    version = cybox.TypedField("Version", String)
    base_address = cybox.TypedField("Base_Address", HexBinary)
    extracted_features = cybox.TypedField("Extracted_Features", ExtractedFeatures)
