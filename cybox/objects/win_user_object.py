# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_user_account_object_1_3 as win_user_binding
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_User:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, user_attributes):
        user_obj = win_user_binding.WindowsUserAccountObjectType()
        user_obj.set_anyAttributes_({'xsi:type' : 'WinUserAccountObj:WindowsUserAccountObjectType'})
        
        for key, value in user_attributes.items():
            if key == 'username' and utils.test_value(value)(value):
                user_obj.set_Username(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'security_id' and utils.test_value(value)(value):
                user_obj.set_Security_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'security_type' and utils.test_value(value)(value):
                user_obj.set_Username(Base_Object_Attribute.object_from_dict(common_types_binding.SIDType(), value))
            
        return user_obj
