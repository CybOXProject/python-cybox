# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox
import cybox.bindings.cybox_common as common_binding


class LocationFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        return cybox.lookup_extension(key, default=Location)


class Location(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.LocationType
    _namespace = 'http://cybox.mitre.org/common-2'
    _XSI_TYPE = None  # overridden by subclasses

    id_ = fields.IdrefField("id")
    idref = fields.IdrefField("idref")
    name = fields.TypedField("Name")

    def to_dict(self):
        d = super(Location, self).to_dict()

        if self._XSI_TYPE:
            d["xsi:type"] = self._XSI_TYPE

        return d

    @staticmethod
    def lookup_class(xsi_type):
        return cybox.lookup_extension(xsi_type, default=Location)
