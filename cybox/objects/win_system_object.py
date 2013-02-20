import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_system_object_1_2 as win_system_binding
import cybox.objects.win_handle_object as win_handle
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_System:
    def __init__(self):
        pass
        
    @classmethod
    def build_object(cls, system_attributes):
        sys_obj = win_system_binding.WindowsSystemObjectType()
        sys_obj.set_anyAttributes_({'xsi:type' : 'WinSystemObj:WindowsSystemObjectType'})
        
        for key, value in system_attributes.items():
            if key == 'local_time' and utils.test_value(value):
                sys_obj.set_Local_Time(Base_Object_Attribute.object_from_dict(common_types_binding.TimeObjectAttributeType(datatype='Time'), value))
            elif key == 'system_time' and utils.test_value(value):
                sys_obj.set_System_Time(Base_Object_Attribute.object_from_dict(common_types_binding.TimeObjectAttributeType(datatype='Time'), value))
            elif key == 'domain' and utils.test_value(value):
                sys_obj.set_Domain(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'netbios_name' and utils.test_value(value):
                sys_obj.set_NetBIOS_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'product_id' and utils.test_value(value):
                sys_obj.set_Product_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'product_name' and utils.test_value(value):
                sys_obj.set_Product_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'registered_organization' and utils.test_value(value):
                sys_obj.set_Registered_Organization(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'registered_owner' and utils.test_value(value):
                sys_obj.set_Registered_Owner(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'windows_directory' and utils.test_value(value):
                sys_obj.set_Windows_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'windows_system_directory' and utils.test_value(value):
                sys_obj.set_Windows_System_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'windows_temp_directory' and utils.test_value(value):
                sys_obj.set_Windows_Temp_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'open_handle_list' and utils.test_value(value):
                sys_obj.set_Open_Handle_List(win_handle.Win_Handle_List.object_from_list(value))
            elif key == 'global_flags' and utils.test_value(value):
                global_flag_list = win_system_binding.GlobalFlagListType()
                for flag in value:
                    global_flag = win_system_binding.GlobalFlagType()
                    global_flag.set_Symbolic_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='string'), flag))
                    global_flag_list.add_Global_Flag(global_flag)
                if global_flag_list.hasContent_():
                    sys_obj.set_Global_Flag_List(global_flag_list)
        
        return sys_obj