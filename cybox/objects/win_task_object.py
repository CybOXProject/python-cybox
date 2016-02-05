# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_task_object as win_task_binding
from cybox.common import (Base64Binary, DateTime, Duration, HashList, Long,
        ObjectProperties, String, UnsignedLong)
from cybox.objects.email_message_object import EmailMessage


class Trigger(entities.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.TriggerType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    trigger_begin = fields.TypedField("Trigger_Begin", DateTime)
    trigger_delay = fields.TypedField("Trigger_Delay", Duration)
    trigger_end = fields.TypedField("Trigger_End", DateTime)
    trigger_frequency = fields.TypedField("Trigger_Frequency", String)
    trigger_max_run_time = fields.TypedField("Trigger_Max_Run_Time", Duration)
    trigger_session_change_type = fields.TypedField(
                                    "Trigger_Session_Change_Type", String)
    trigger_type = fields.TypedField("Trigger_Type", String)


class TriggerList(entities.EntityList):
    _binding = win_task_binding
    _binding_class = win_task_binding.TriggerListType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'
    trigger = fields.TypedField("Trigger", Trigger, multiple=True)


class IComHandlerAction(entities.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IComHandlerActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    com_data = fields.TypedField("COM_Data", String)
    com_class_id = fields.TypedField("COM_Class_ID", String)


class IExecAction(entities.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IExecActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    exec_arguments = fields.TypedField("Exec_Arguments", String)
    exec_program_path = fields.TypedField("Exec_Program_Path", String)
    exec_working_directory = fields.TypedField("Exec_Working_Directory", String)
    exec_program_hashes = fields.TypedField("Exec_Program_Hashes", HashList)


class IShowMessageAction(entities.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.IShowMessageActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    show_message_body = fields.TypedField("Show_Message_Body", String)
    show_message_title = fields.TypedField("Show_Message_Title", String)


class TaskAction(entities.Entity):
    _binding = win_task_binding
    _binding_class = win_task_binding.TaskActionType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'

    action_type = fields.TypedField("Action_Type", String)
    action_id = fields.TypedField("Action_ID", String)
    iemailaction = fields.TypedField("IEmailAction", EmailMessage)
    icomhandleraction = fields.TypedField("IComHandlerAction",
                                         IComHandlerAction)
    iexecaction = fields.TypedField("IExecAction", IExecAction)
    ishowmessageaction = fields.TypedField("IShowMessageAction",
                                          IShowMessageAction)


class TaskActionList(entities.EntityList):
    _binding = win_task_binding
    _binding_class = win_task_binding.TaskActionListType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'
    action = fields.TypedField("Action", TaskAction, multiple=True)


class WinTask(ObjectProperties):
    _binding = win_task_binding
    _binding_class = win_task_binding.WindowsTaskObjectType
    _namespace = 'http://cybox.mitre.org/objects#WinTaskObject-2'
    _XSI_NS = "WinTaskObj"
    _XSI_TYPE = "WindowsTaskObjectType"

    status = fields.TypedField("Status", String)
    priority = fields.TypedField("Priority", String)
    name = fields.TypedField("Name", String)
    application_name = fields.TypedField("Application_Name", String)
    parameters = fields.TypedField("Parameters", String)
    flags = fields.TypedField("Flags", String)
    account_name = fields.TypedField("Account_Name", String)
    account_run_level = fields.TypedField("Account_Run_Level", String)
    account_logon_type = fields.TypedField("Account_Logon_Type", String)
    creator = fields.TypedField("Creator", String)
    creation_date = fields.TypedField("Creation_Date", DateTime)
    most_recent_run_time = fields.TypedField("Most_Recent_Run_Time", DateTime)
    exit_code = fields.TypedField("Exit_Code", Long)
    max_run_time = fields.TypedField("Max_Run_Time", UnsignedLong)
    next_run_time = fields.TypedField("Next_Run_Time", DateTime)
    action_list = fields.TypedField("Action_List", TaskActionList)
    trigger_list = fields.TypedField("Trigger_List", TriggerList)
    comment = fields.TypedField("Comment", String)
    working_directory = fields.TypedField("Working_Directory", String)
    work_item_data = fields.TypedField("Work_Item_Data", Base64Binary)
