# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_network_share_object as win_network_share_binding
from cybox.common import ObjectProperties, String, NonNegativeInteger

class WinNetworkShare(ObjectProperties):
    _XSI_NS = "WinNetworkShareObj"
    _XSI_TYPE = "WindowsNetworkShareObjectType"

    def __init__(self):
        super(WinNetworkShare, self).__init__()
        self.access_read = None
        self.access_write = None
        self.access_create = None
        self.access_exec = None
        self.access_delete = None
        self.access_atrib = None
        self.access_perm = None
        self.access_all = None
        self.current_uses = None
        self.local_path = None
        self.max_uses = None
        self.netname = None
        self.type = None

    def to_obj(self):
        win_network_share_obj = win_network_share_binding.WindowsNetworkShareObjectType()
        super(WinNetworkShare, self).to_obj(win_network_share_obj)
        if self.access_read is not None : win_network_share_obj.set_access_read(self.access_read)
        if self.access_write is not None : win_network_share_obj.set_access_write(self.access_write)
        if self.access_create is not None : win_network_share_obj.set_access_create(self.access_create)
        if self.access_exec is not None : win_network_share_obj.set_access_exec(self.access_exec)
        if self.access_delete is not None : win_network_share_obj.set_access_delete(self.access_delete)
        if self.access_atrib is not None : win_network_share_obj.set_access_atrib(self.access_atrib)
        if self.access_perm is not None : win_network_share_obj.set_access_perm(self.access_perm)
        if self.access_all is not None : win_network_share_obj.set_access_all(self.access_all)
        if self.current_uses is not None : win_network_share_obj.set_Current_Uses(self.current_uses.to_obj())
        if self.local_path is not None : win_network_share_obj.set_Local_Path(self.local_path.to_obj())
        if self.max_uses is not None : win_network_share_obj.set_Max_Uses(self.max_uses.to_obj())
        if self.netname is not None : win_network_share_obj.set_Netname(self.netname.to_obj())
        if self.type is not None : win_network_share_obj.set_Type(self.type.to_obj())
        return win_network_share_obj

    def to_dict(self):
        win_network_share_dict = {}
        super(WinNetworkShare, self).to_dict(win_network_share_dict)

        if self.access_read is not None : win_network_share_dict['access_read'] = self.access_read
        if self.access_write is not None : win_network_share_dict['access_write'] = self.access_write
        if self.access_create is not None : win_network_share_dict['access_create'] = self.access_create
        if self.access_exec is not None : win_network_share_dict['access_exec'] = self.access_exec
        if self.access_delete is not None : win_network_share_dict['access_delete'] = self.access_delete
        if self.access_atrib is not None : win_network_share_dict['access_atrib'] = self.access_atrib
        if self.access_perm is not None : win_network_share_dict['access_perm'] = self.access_perm
        if self.access_all is not None : win_network_share_dict['access_all'] = self.access_all
        if self.current_uses is not None : win_network_share_dict['current_uses'] = self.current_uses.to_obj()
        if self.local_path is not None : win_network_share_dict['local_path'] = self.local_path.to_obj()
        if self.max_uses is not None : win_network_share_dict['max_uses'] = self.max_uses.to_obj()
        if self.netname is not None : win_network_share_dict['netname'] = self.netname.to_obj()
        if self.type is not None : win_network_share_dict['type'] = self.type.to_obj()
        return win_network_share_dict

    @staticmethod
    def from_dict(win_network_share_dict):
        if not win_network_share_dict:
            return None
        win_network_share_ = WinNetworkShare()
        win_network_share_.access_read = win_network_share_dict.get('access_read')
        win_network_share_.access_write = win_network_share_dict.get('access_write')
        win_network_share_.access_create = win_network_share_dict.get('access_create')
        win_network_share_.access_exec = win_network_share_dict.get('access_exec')
        win_network_share_.access_delete = win_network_share_dict.get('access_delete')
        win_network_share_.access_atrib = win_network_share_dict.get('access_atrib')
        win_network_share_.access_perm = win_network_share_dict.get('access_perm')
        win_network_share_.access_all = win_network_share_dict.get('access_all')
        win_network_share_.current_uses = NonNegativeInteger.from_dict(win_network_share_dict.get('current_uses'))
        win_network_share_.local_path = String.from_dict(win_network_share_dict.get('local_path'))
        win_network_share_.max_uses = NonNegativeIntger.from_dict(win_network_share_dict.get('max_uses'))
        win_network_share_.netname = String.from_dict(win_network_share_dict.get('netname'))
        win_network_share_.type = String.from_dict(win_network_share_dict.get('type'))
        return win_network_share_

    @staticmethod
    def from_obj(win_network_share_obj):
        if not win_network_share_obj:
            return None
        win_network_share_ = WinNetworkShare()
        win_network_share_.access_read = win_network_share_obj.get_access_read()
        win_network_share_.access_write = win_network_share_obj.get_access_write()
        win_network_share_.access_create = win_network_share_obj.get_access_create()
        win_network_share_.access_exec = win_network_share_obj.get_access_exec()
        win_network_share_.access_delete = win_network_share_obj.get_access_delete()
        win_network_share_.access_atrib = win_network_share_obj.get_access_atrib()
        win_network_share_.access_perm = win_network_share_obj.get_access_perm()
        win_network_share_.access_all = win_network_share_obj.get_access_all()
        win_network_share_.current_uses = NonNegativeInteger.from_obj(win_network_share_obj.get_Current_Uses())
        win_network_share_.local_path = String.from_obj(win_network_share_obj.get_Local_Path())
        win_network_share_.max_uses = NonNegativeIntger.from_obj(win_network_share_obj.get_Max_Uses())
        win_network_share_.netname = String.from_obj(win_network_share_obj.get_Netname())
        win_network_share_.type = String.from_obj(win_network_share_obj.get_Type())
        return win_network_share_
