# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import cybox.bindings.user_session_object as user_session_binding
from cybox.common import DateTime, String, ObjectProperties


class UserSession(ObjectProperties):
    _binding = user_session_binding
    _binding_class = user_session_binding.UserSessionObjectType
    _namespace = "http://cybox.mitre.org/objects#UserSessionObject-2"
    _XSI_NS = "UserSessionObj"
    _XSI_TYPE = "UserSessionObjectType"

    effective_group = fields.TypedField("Effective_Group", String)
    effective_group_id = fields.TypedField("Effective_Group_ID", String)
    effective_user = fields.TypedField("Effective_User", String)
    effective_user_id = fields.TypedField("Effective_User_ID", String)
    login_time = fields.TypedField("Login_Time", DateTime)
    logout_time = fields.TypedField("Logout_Time", DateTime)
