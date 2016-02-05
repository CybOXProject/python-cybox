# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_event_log_object as win_event_log_binding
from cybox.common import ObjectProperties, String, Base64Binary, DateTime, Long 


class UnformattedMessageList(entities.EntityList):
    _binding = win_event_log_binding
    _binding_class = win_event_log_binding.UnformattedMessageListType
    _namespace = "http://cybox.mitre.org/objects#WinEventLogObject-2"
    unformatted_message = fields.TypedField("Unformatted_Message", String, multiple=True)


class WinEventLog(ObjectProperties):
    _binding = win_event_log_binding
    _binding_class = win_event_log_binding.WindowsEventLogObjectType
    _namespace = "http://cybox.mitre.org/objects#WinEventLogObject-2"
    _XSI_NS = "WinEventLogObj"
    _XSI_TYPE = "WindowsEventLogObjectType"

    eid = fields.TypedField("EID", Long)
    type_ = fields.TypedField("Type", String)
    log = fields.TypedField("Log", String)
    message = fields.TypedField("Message", String)
    category_num = fields.TypedField("Category_Num", Long)
    category = fields.TypedField("Category", String)
    generation_time = fields.TypedField("Generation_Time", DateTime)
    source = fields.TypedField("Source", String)
    machine = fields.TypedField("Machine", String)
    user = fields.TypedField("User", String)
    blob = fields.TypedField("Blob", Base64Binary)
    correlation_activity_id = fields.TypedField("Correlation_Activity_ID", String)
    correlation_related_activity_id = fields.TypedField("Correlation_Related_Activity_ID", String)
    execution_process_id = fields.TypedField("Execution_Process_ID", String)
    execution_thread_id = fields.TypedField("Execution_Thread_ID", String)
    index = fields.TypedField("Index", Long)
    reserved = fields.TypedField("Reserved", Long)
    unformatted_message_list = fields.TypedField("Unformatted_Message_List", UnformattedMessageList)
    write_time = fields.TypedField("Write_Time", DateTime)
