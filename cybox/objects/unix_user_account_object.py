# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.unix_user_account_object as unix_user_account_binding
from cybox.common import String, NonNegativeInteger, UnsignedInteger
from cybox.objects.user_account_object import (Group, GroupList, Privilege,
                                               PrivilegeList, UserAccount)


class UnixGroup(Group):
    _binding = unix_user_account_binding
    _binding_class = unix_user_account_binding.UnixGroupType
    _namespace = 'http://cybox.mitre.org/objects#UnixUserAccountObject-2'
    _XSI_TYPE = "UnixGroupType"

    group_id = fields.TypedField("Group_ID", NonNegativeInteger)


class UnixGroupList(GroupList):
    group = fields.TypedField("Group", UnixGroup, multiple=True)


class UnixPrivilege(Privilege):
    _binding = unix_user_account_binding
    _binding_class = unix_user_account_binding.UnixPrivilegeType
    _namespace = 'http://cybox.mitre.org/objects#UnixUserAccountObject-2'
    _XSI_TYPE = "UnixPrivilegeType"

    permissions_mask = fields.TypedField("Permissions_Mask", String)


class UnixPrivilegeList(PrivilegeList):
    privilege = fields.TypedField("Privilege", UnixPrivilege, multiple=True)


class UnixUserAccount(UserAccount):
    _binding = unix_user_account_binding
    _binding_class = unix_user_account_binding.UnixUserAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#UnixUserAccountObject-2'
    _XSI_NS = "UnixUserAccountObj"
    _XSI_TYPE = "UnixUserAccountObjectType"

    group_id = fields.TypedField("Group_ID", UnsignedInteger)
    user_id = fields.TypedField("User_ID", UnsignedInteger)
    login_shell = fields.TypedField("Login_Shell", String)

    # Override abstract types
    group_list = fields.TypedField('Group_List', UnixGroupList)
    privilege_list = fields.TypedField('Privilege_List', UnixPrivilegeList)
