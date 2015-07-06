# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_network_share_object as win_network_share_binding
from cybox.common import ObjectProperties, String, NonNegativeInteger


class WinNetworkShare(ObjectProperties):
    _binding = win_network_share_binding
    _binding_class = win_network_share_binding.WindowsNetworkShareObjectType
    _namespace = "http://cybox.mitre.org/objects#WinNetworkShareObject-2"
    _XSI_NS = "WinNetworkShareObj"
    _XSI_TYPE = "WindowsNetworkShareObjectType"

    access_read = fields.TypedField("ACCESS_READ")
    access_write = fields.TypedField("ACCESS_WRITE")
    access_create = fields.TypedField("ACCESS_CREATE")
    access_exec = fields.TypedField("ACCESS_EXEC")
    access_delete = fields.TypedField("ACCESS_DELETE")
    access_atrib = fields.TypedField("ACCESS_ATRIB")
    access_perm = fields.TypedField("ACCESS_PERM")
    access_all = fields.TypedField("ACCESS_ALL")
    current_uses = fields.TypedField("Current_Uses", NonNegativeInteger)
    local_path = fields.TypedField("Local_Path", String)
    max_uses = fields.TypedField("Max_Uses", NonNegativeInteger)
    netname = fields.TypedField("Netname", String)
    type_ = fields.TypedField("Type", String)
