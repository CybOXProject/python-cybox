# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.user_account_object as user_account_binding
from cybox.common import DateTime, Duration, String
from cybox.objects.account_object import Account


class Group(cybox.Entity):
    """An abstract class for account groups."""

    def __init__(self):
        raise TypeError("Cannot instantiate abstract type.")


class GroupList(cybox.EntityList):
    _binding = user_account_binding
    _binding_class = user_account_binding.GroupListType
    _binding_var = 'Group'
    _contained_type = Group
    _namespace = 'http://cybox.mitre.org/objects#UserAccountObject-2'


class Privilege(cybox.Entity):
    """An abstract class for account privileges."""

    def __init__(self):
        raise TypeError("Cannot instantiate abstract type.")


class PrivilegeList(cybox.EntityList):
    _binding = user_account_binding
    _binding_class = user_account_binding.PrivilegeListType
    _binding_var = 'Privilege'
    _contained_type = Privilege
    _namespace = 'http://cybox.mitre.org/objects#UserAccountObject-2'


class UserAccount(Account):
    _binding = user_account_binding
    _binding_class = user_account_binding.UserAccountObjectType
    _namespace = 'http://cybox.mitre.org/objects#UserAccountObject-2'
    _XSI_NS = "UserAccountObj"
    _XSI_TYPE = "UserAccountObjectType"

    password_required = cybox.TypedField('password_required')
    full_name = cybox.TypedField('Full_Name', String)
    home_directory = cybox.TypedField('Home_Directory', String)
    last_login = cybox.TypedField('Last_Login', DateTime)
    script_path = cybox.TypedField('Script_Path', String)
    username = cybox.TypedField('Username', String)
    user_password_age = cybox.TypedField('User_Password_Age', Duration)

    # These should be overriden by subclasses
    group_list = cybox.TypedField('Group_List', GroupList)
    privilege_list = cybox.TypedField('Privilege_List', PrivilegeList)
