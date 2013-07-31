# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.user_account_object as user_account_binding
from cybox.common import DateTime, Duration, String
from cybox.objects.account_object import Account


class Group(cybox.Entity):
    """An abstract class for account groups."""
    pass


class GroupList(cybox.EntityList):
    """An abstract class for lists of account groups."""


class Privilege(cybox.Entity):
    """An abstract class for account privileges."""
    pass


class PrivilegeList(cybox.EntityList):
    """An abstract class for lists of account privileges."""
    pass


class UserAccount(Account):
    _binding = user_account_binding
    _binding_class = user_account_binding.UserAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#UserAccountObject-2'
    _XSI_NS = "UserAccountObj"
    _XSI_TYPE = "UserAccountObjectType"

    password_required = cybox.TypedField('password_required')
    full_name = cybox.TypedField('Full_Name', String)
    group_list = cybox.TypedField('Group_List', GroupList)
    home_directory = cybox.TypedField('Home_Directory', String)
    last_login = cybox.TypedField('Last_Login', DateTime)
    privilege_list = cybox.TypedField('Privilege_List', PrivilegeList)
    script_path = cybox.TypedField('Script_Path', String)
    username = cybox.TypedField('Username', String)
    user_password_age = cybox.TypedField('User_Password_Age', Duration)
