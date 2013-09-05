# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import DateRange
import cybox.xs as xs


class Contributor(cybox.Entity):
    _binding = common_binding
    _binding_class = common_binding.ContributorType
    _namespace = 'http://cybox.mitre.org/common-2'

    role = cybox.TypedField("Role", xs.string)
    name = cybox.TypedField("Name", xs.string)
    email = cybox.TypedField("Email", xs.string)
    phone = cybox.TypedField("Phone", xs.string)
    organization = cybox.TypedField("Organization", xs.string)
    date = cybox.TypedField("Date", DateRange)
    contribution_location = cybox.TypedField("Contribution_Location",
                                             xs.string)


class Personnel(cybox.EntityList):
    _binding_class = common_binding.PersonnelType
    _binding_var = "Contributor"
    _contained_type = Contributor
    _namespace = 'http://cybox.mitre.org/common-2'
