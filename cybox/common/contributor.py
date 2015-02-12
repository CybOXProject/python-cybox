# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import DateRange


class Contributor(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.ContributorType
    _namespace = 'http://cybox.mitre.org/common-2'

    role = cybox.TypedField("Role")
    name = cybox.TypedField("Name")
    email = cybox.TypedField("Email")
    phone = cybox.TypedField("Phone")
    organization = cybox.TypedField("Organization")
    date = cybox.TypedField("Date", DateRange)
    contribution_location = cybox.TypedField("Contribution_Location")


class Personnel(cybox.EntityList):
    _binding_class = common_binding.PersonnelType
    _binding_var = "Contributor"
    _contained_type = Contributor
    _namespace = 'http://cybox.mitre.org/common-2'
