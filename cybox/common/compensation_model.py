# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.bindings.cybox_common as common_binding
from cybox.common import BaseProperty


class CompensationModel(BaseProperty):
    _binding = common_binding
    _binding_class = common_binding.CompensationModelType
    _namespace = 'http://cybox.mitre.org/common-2'

    TERM_FREEWARE = "Freeware"
    TERM_SHAREWARE = "Shareware"
    TERM_COMMERCIAL = "Commercial"
    TERM_ADWARE = "Adware"
