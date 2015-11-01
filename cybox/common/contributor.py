# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import DateRange


class Contributor(entities.Entity):
    _binding = common_binding
    _binding_class = common_binding.ContributorType
    _namespace = 'http://cybox.mitre.org/common-2'

    role = fields.TypedField("Role")
    name = fields.TypedField("Name")
    email = fields.TypedField("Email")
    phone = fields.TypedField("Phone")
    organization = fields.TypedField("Organization")
    date = fields.TypedField("Date", DateRange)
    contribution_location = fields.TypedField("Contribution_Location")


class Personnel(entities.EntityList):
    _binding_class = common_binding.PersonnelType
    _namespace = 'http://cybox.mitre.org/common-2'
    contributor = fields.TypedField("Contributor", Contributor, multiple=True)