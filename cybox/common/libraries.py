# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox.bindings.cybox_common as common_binding


class Library(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.LibraryType
    _namespace = 'http://cybox.mitre.org/common-2'

    version = fields.TypedField("version")
    name = fields.TypedField("name")


class Libraries(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.LibrariesType
    _namespace = 'http://cybox.mitre.org/common-2'

    library = fields.TypedField("Library", Library)
