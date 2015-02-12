# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_task_object as win_task_binding
from cybox.common import (Base64Binary, DateTime, Duration, HashList, Long,
        ObjectProperties, String, UnsignedLong)
from cybox.objects.email_message_object import EmailMessage


class Trigger(cybox.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.TriggerType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    trigger_begin = cybox.TypedField("Trigger_Begin", DateTime)
    trigger_delay = cybox.TypedField("Trigger_Delay", Duration)
    trigger_end = cybox.TypedField("Trigger_End", DateTime)
    trigger_frequency = cybox.TypedField("Trigger_Frequency", String)
    trigger_max_run_time = cybox.TypedField("Trigger_Max_Run_Time", Duration)
    trigger_session_change_type = cybox.TypedField(
                                    "Trigger_Session_Change_Type", String)
    trigger_type = cybox.TypedField("Trigger_Type", String)


class TriggerList(cybox.EntityList):
    _binding = win_task_binding
    _binding_class = win_task_binding.TriggerListType
    _binding_var = 'Trigger'
    _contained_type = Trigger
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'


class IComHandlerAction(cybox.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IComHandlerActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    com_data = cybox.TypedField("COM_Data", String)
    com_class_id = cybox.TypedField("COM_Class_ID", String)


class IExecAction(cybox.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IExecActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    exec_arguments = cybox.TypedField("Exec_Arguments", String)
    exec_program_path = cybox.TypedField("Exec_Program_Path", String)
    exec_working_directory = cybox.TypedField("Exec_Working_Directory", String)
    exec_program_hashes = cybox.TypedField("Exec_Program_Hashes", HashList)


class IShowMessageAction(cybox.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IShowMessageActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    show_message_body = cybox.TypedField("Show_Message_Body", String)
    show_message_title = cybox.TypedField("Show_Message_Title", String)


class TaskAction(cybox.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.TaskActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    action_type = cybox.TypedField("Action_Type", String)
    action_id = cybox.TypedField("Action_ID", String)
    iemailaction = cybox.TypedField("IEmailAction", EmailMessage)
    icomhandleraction = cybox.TypedField("IComHandlerAction",
                                         IComHandlerAction)
    iexecaction = cybox.TypedField("IExecAction", IExecAction)
    ishowmessageaction = cybox.TypedField("IShowMessageAction",
                                          IShowMessageAction)


class TaskActionList(cybox.EntityList):
    _binding = win_task_binding
    _binding_class = win_task_binding.TaskActionListType
    _binding_var = 'Action'
    _contained_type = TaskAction
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'


class WinTask(ObjectProperties):
    _binding = win_task_binding
    _binding_class = win_task_binding.WindowsTaskObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'
    _XSI_NS = "WinTaskObj"
    _XSI_TYPE = "WindowsTaskObjectType"

    status = cybox.TypedField("Status", String)
    priority = cybox.TypedField("Priority", String)
    name = cybox.TypedField("Name", String)
    application_name = cybox.TypedField("Application_Name", String)
    parameters = cybox.TypedField("Parameters", String)
    flags = cybox.TypedField("Flags", String)
    account_name = cybox.TypedField("Account_Name", String)
    account_run_level = cybox.TypedField("Account_Run_Level", String)
    account_logon_type = cybox.TypedField("Account_Logon_Type", String)
    creator = cybox.TypedField("Creator", String)
    creation_date = cybox.TypedField("Creation_Date", DateTime)
    most_recent_run_time = cybox.TypedField("Most_Recent_Run_Time", DateTime)
    exit_code = cybox.TypedField("Exit_Code", Long)
    max_run_time = cybox.TypedField("Max_Run_Time", UnsignedLong)
    next_run_time = cybox.TypedField("Next_Run_Time", DateTime)
    action_list = cybox.TypedField("Action_List", TaskActionList)
    trigger_list = cybox.TypedField("Trigger_List", TriggerList)
    comment = cybox.TypedField("Comment", String)
    working_directory = cybox.TypedField("Working_Directory", String)
    work_item_data = cybox.TypedField("Work_Item_Data", Base64Binary)
