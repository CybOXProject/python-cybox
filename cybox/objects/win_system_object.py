import maec_bundle_3_0 as maecbundle
import cybox.win_system_object_1_2 as cybox_win_system_object

class win_system_object:
    def __init__(self, id):
        self.id = id
        
    def build_object(self, system_attributes):
        cybox_object = maecbundle.cybox_core_1_0.AssociatedObjectType(id=self.generator.generate_obj_id(), type_='System')
        sys_obj = cybox_win_system_object.WindowsSystemObjectType()
        sys_obj.set_anyAttributes_({'xsi:type' : 'WinSystemObj:WindowsSystemObjectType'})
        
        for key, value in system_attributes.items():
            if key == 'local_time' and self.__value_test(value):
                sys_obj.set_Local_Time(maecbundle.cybox_common_types_1_0.TimeObjectAttributeType(datatype='Time',valueOf_=value))
            elif key == 'system_time' and self.__value_test(value):
                sys_obj.set_System_Time(maecbundle.cybox_common_types_1_0.TimeObjectAttributeType(datatype='Time',valueOf_=value))
            elif key == 'global_flags' and self.__value_test(value):
                global_flag_list = cybox_win_system_object.GlobalFlagListType()
                for flag in value:
                    global_flag = cybox_win_system_object.GlobalFlagType()
                    global_flag.set_Symbolic_Name(maecbundle.cybox_common_types_1_0.StringObjectAttributeType(datatype='string', valueOf_=flag))
                    global_flag_list.add_Global_Flag(global_flag)
                if global_flag_list.hasContent_():
                    sys_obj.set_Global_Flag_List(global_flag_list)
            elif key == 'association':
                cybox_object.set_association_type(value)
        
        if sys_obj.hasContent_():
            cybox_object.set_Defined_Object(sys_obj)
        
        return cybox_object