# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import Contributor


class Personnel(cybox.EntityList):
    _binding_class = common_binding.PersonnelType
    _binding_var = "Contributor"
    _contained_type = Contributor
    _namespace = 'http://cybox.mitre.org/common-2'
