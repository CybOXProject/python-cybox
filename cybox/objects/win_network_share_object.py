# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from cybox import TypedField
import cybox.bindings.win_network_share_object as win_network_share_binding
from cybox.common import ObjectProperties, String, NonNegativeInteger
import cybox.xs as xs


class WinNetworkShare(ObjectProperties):
    _binding = win_network_share_binding
    _binding_class = win_network_share_binding.WindowsNetworkShareObjectType
    _namespace = "http://cybox.mitre.org/objects#WinNetworkShareObject-2"
    _XSI_NS = "WinNetworkShareObj"
    _XSI_TYPE = "WindowsNetworkShareObjectType"

    access_read = TypedField("ACCESS_READ", xs.boolean)
    access_write = TypedField("ACCESS_WRITE", xs.boolean)
    access_create = TypedField("ACCESS_CREATE", xs.boolean)
    access_exec = TypedField("ACCESS_EXEC", xs.boolean)
    access_delete = TypedField("ACCESS_DELETE", xs.boolean)
    access_atrib = TypedField("ACCESS_ATRIB", xs.boolean)
    access_perm = TypedField("ACCESS_PERM", xs.boolean)
    access_all = TypedField("ACCESS_ALL", xs.boolean)
    current_uses = TypedField("Current_Uses", NonNegativeInteger)
    local_path = TypedField("Local_Path", String)
    max_uses = TypedField("Max_Uses", NonNegativeInteger)
    netname = TypedField("Netname", String)
    type = TypedField("Type", String)

    def __init__(self):
        super(WinNetworkShare, self).__init__()
