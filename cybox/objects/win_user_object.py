# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_user_account_object as win_user_binding
from cybox.common import String
from cybox.objects.user_account_object import (GroupList, PrivilegeList,
        UserAccount)


class WinGroup(cybox.Entity):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsGroupType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'

    name = cybox.TypedField("Name", String)

    # TODO: Allow these to be represented as single strings in to/from_dict


class WinGroupList(GroupList):
    _contained_type = WinGroup


class WinPrivilege(cybox.Entity):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsPrivilegeType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'

    user_right = cybox.TypedField("User_Right", String)

    # TODO: Allow these to be represented as single strings in to/from_dict


class WinPrivilegeList(PrivilegeList):
    _contained_type = WinPrivilege


class WinUser(UserAccount):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsUserAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'
    _XSI_NS = "WinUserAccountObj"
    _XSI_TYPE = "WindowsUserAccountObjectType"

    security_id = cybox.TypedField('Security_ID', String)
    security_type = cybox.TypedField('Security_Type', String)

    #Override abstract types here
    group_list = cybox.TypedField('Group_List', WinGroupList)
    privilege_list = cybox.TypedField('Privilege_List', WinPrivilegeList)
