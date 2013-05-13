# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.cybox_common as common_binding
from cybox.common import Contributor

class Personnel(cybox.EntityList):
    _contained_type = Contributor
    _binding_class = common_binding.PersonnelType

    def __init__(self):
        super(Contributor, self).__init__()

    @staticmethod
    def _set_list(binding_obj, list_):
        binding_obj.set_Contributor(list_)

    @staticmethod
    def _get_list(binding_obj):
        return binding_obj.get_Contributor()