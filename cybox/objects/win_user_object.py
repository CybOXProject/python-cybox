# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.win_user_account_object as win_user_binding
from cybox.common import String
from cybox.objects.user_account_object import (Group, GroupList, Privilege,
                                               PrivilegeList, UserAccount)


class WinGroup(Group):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsGroupType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'
    _XSI_TYPE = "WindowsGroupType"

    name = fields.TypedField("Name", String)


class WinGroupList(GroupList):
    group = fields.TypedField("Group", WinGroup, multiple=True)


class WinPrivilege(Privilege):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsPrivilegeType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'
    _XSI_TYPE = "WindowsPrivilegeType"

    user_right = fields.TypedField("User_Right", String)


class WinPrivilegeList(PrivilegeList):
    privilege = fields.TypedField("Privilege", WinPrivilege, multiple=True)


class WinUser(UserAccount):
    _binding = win_user_binding
    _binding_class = win_user_binding.WindowsUserAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinUserAccountObject-2'
    _XSI_NS = "WinUserAccountObj"
    _XSI_TYPE = "WindowsUserAccountObjectType"

    security_id = fields.TypedField('Security_ID', String)
    security_type = fields.TypedField('Security_Type', String)

    # Override abstract types
    group_list = fields.TypedField('Group_List', WinGroupList)
    privilege_list = fields.TypedField('Privilege_List', WinPrivilegeList)
