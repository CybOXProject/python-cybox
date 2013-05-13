# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox.utils as utils
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_task_object_1_3 as win_task_binding
from cybox.objects.email_message_object import EmailMessage
from cybox.common import HashList
from cybox.common.baseobjectattribute import Base_Object_Attribute

class Win_Task:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, task_attributes):
        task_obj = win_task_binding.WindowsTaskObjectType()
        task_obj.set_anyAttributes_({'xsi:type' : 'WinTaskObj:WindowsTaskObjectType'})
        
        for key, value in task_attributes.items():
            if key == 'name' and utils.test_value(value):
                task_obj.set_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'status' and utils.test_value(value):
                task_obj.set_Status(Base_Object_Attribute.object_from_dict(win_task_binding.TaskStatusType(), value))
            if key == 'priority' and utils.test_value(value):
                task_obj.set_Priority(Base_Object_Attribute.object_from_dict(win_task_binding.TaskPriorityType(), value))
            if key == 'flags' and utils.test_value(value):
                task_obj.set_Flags(Base_Object_Attribute.object_from_dict(win_task_binding.TaskFlagType(), value))
            if key == 'application_type' and utils.test_value(value):
                task_obj.set_Application_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'paramters' and utils.test_value(value):
                task_obj.set_Parameters(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'account_name' and utils.test_value(value):
                tdfasd;fask_obj.set_Account_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'account_run_level' and utils.test_value(value):
                task_obj.set_Account_Run_Level(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'account_Logon_Type' and utils.test_value(value):
                task_obj.set_Account_Logon_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'account_name' and utils.test_value(value):
                task_obj.set_Account_Name(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'creator' and utils.test_value(value):
                task_obj.set_Creator(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'comment' and utils.test_value(value):
                task_obj.set_Comment(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'working_directory' and utils.test_value(value):
                task_obj.set_Working_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            if key == 'creation_date' and utils.test_value(value):
                task_obj.set_Creation_Date(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), value))
            if key == 'most_recent_run_time' and utils.test_value(value):
                task_obj.set_Most_Recent_Run_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), value))
            if key == 'next_run_time' and utils.test_value(value):
                task_obj.set_Next_Run_Time(Base_Object_Attribute.object_from_dict(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), value))
            if key == 'exit_code' and utils.test_value(value):
                task_obj.set_Exit_Code(Base_Object_Attribute.object_from_dict(common_types_binding.LongObjectAttributeType(datatype='Long'), value))
            if key == 'max_run_time' and utils.test_value(value):
                task_obj.set_Max_Run_Time(Base_Object_Attribute.object_from_dict(common_types_binding.UnsignedLongObjectAttributeType(datatype='UnsignedLong'), value))
            if key == 'work_item_data' and utils.test_value(value):
                task_obj.set_Work_Item_Data(Base_Object_Attribute.object_from_dict(common_types_binding.Base64BinaryObjectAttributeType(datatype='Base64Binary'), value))
            if key == 'action_list' and utils.test_value(value):
                action_list = win_task_binding.TaskActionListType()
                for action in value:
                    action_obj = win_task_binding.TaskActionType()
                    for action_key, action_value in action.items():
                        if action_key == 'action_type' and utils.test_value(action_value):
                            action_obj.set_Action_Type(Base_Object_Attribute.object_from_dict(win_task_binding.TaskActionTypeType(), action_value))
                        if action_key == 'action_id' and utils.test_value(action_value):
                            action_obj.set_Action_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), action_value))
                        if action_key == 'iemailaction' and utils.test_value(action_value):
                            action_obj.set_IEmailAction(EmailMessage.object_from_dict(action_value))
                        if action_key == 'icomhandleraction' and utils.test_value(action_value):
                            icom_obj = win_task_binding.IComHandlerActionType()
                            for icom_key, icom_value in action_value.items():
                                if icom_key == 'com_data' and utils.test_value(icom_value):
                                    icom_obj.set_COM_Data(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), icom_value))
                                if icom_key == 'com_class_id' and utils.test_value(icom_value):
                                    icom_obj.set_COM_Class_ID(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), icom_value))
                            action_obj.set_IComHandlerAction(icom_obj)
                        if action_key == 'iexecaction' and utils.test_value(action_value):
                            iexec_obj = win_task_binding.IExecActionType()
                            for iexec_key, iexec_value in action_value.items():
                                if iexec_key == 'exec_arguments' and utils.test_value(iexec_value):
                                    iexec_obj.set_Exec_Arguments(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), iexec_value))
                                if iexec_key == 'exec_program_path' and utils.test_value(iexec_value):
                                    iexec_obj.set_Exec_Program_Path(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), iexec_value))
                                if iexec_key == 'exec_working_directorys' and utils.test_value(iexec_value):
                                    iexec_obj.set_Exec_Working_Directory(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), iexec_value))
                                if iexec_key == 'exec_program_hashes' and utils.test_value(iexec_value):
                                    iexec_obj.set_Exec_Arguments(HashList.object_from_dict(iexec_value))
                            action_obj.set_IExecAction(iexec_obj)
                        if action_key == 'ishowmessageaction' and utils.test_value(action_value):
                            ishow_obj = win_task_binding.IShowMessageActionType()
                            for ishow_key, ishow_value in action_value.items():
                                if ishow_key == 'show_message_body' and utils.test_value(ishow_value):
                                    ishow_obj.set_Show_Message_Body(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), ishow_value))
                                if ishow_key == 'show_message_title' and utils.test_value(ishow_value):
                                    ishow_obj.set_Show_Message_Title(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), ishow_value))
                            action_obj.set_IShowMessageAction(ishow_obj)
                    action_list.add_Action(action_obj)
                task_obj.set_Action_List(action_list)
            if key == 'trigger_list' and utils.test_value(value):           
                trigger_list = win_task_binding.TriggerListType()
                for trigger in value:
                    trigger_obj = win_task_binding.TriggerType()
                    for trigger_key, trigger_value in trigger.items():
                        if trigger_key == 'trigger_begin' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_Begin(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), trigger_value)
                        if trigger_key == 'trigger_end' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_End(common_types_binding.DateTimeObjectAttributeType(datatype='DateTime'), trigger_value)
                        if trigger_key == 'trigger_delay' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_Begin(common_types_binding.DurationObjectAttributeType(datatype='Duration'), trigger_value)
                        if trigger_key == 'trigger_max_run_time' and utils.test_value(trigger_value):
                            trigger_obj.set_Max_Run_Time(common_types_binding.DurationObjectAttributeType(datatype='Duration'), trigger_value)
                        if trigger_key == 'trigger_session_change_type' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_Session_Change_Type(Base_Object_Attribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), trigger_value))
                        if trigger_key == 'trigger_type' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_Type(Base_Object_Attribute.object_from_dict(win_task_binding.TaskTriggerType(), trigger_value))
                        if trigger_key == 'enabled' and utils.test_value(trigger_value):
                            trigger_obj.set_enabled(trigger_value)
                        if trigger_key == 'trigger_frequency' and utils.test_value(trigger_value):
                            trigger_obj.set_Trigger_Frequency(Base_Object_Attribute.object_from_dict(win_task_binding.TaskTriggerFrequencyType(), trigger_value))
                    trigger_list.add_Trigger(trigger_obj)
                task_obj.set_Trigger_List(trigger_list)
                      
        return task_obj
