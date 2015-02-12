# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_event_log_object as win_event_log_binding
from cybox.common import ObjectProperties, String, Base64Binary, DateTime, Long, UnsignedInteger, ByteRuns

class UnformattedMessageList(cybox.EntityList):
    _binding = win_event_log_binding
    _binding_class = win_event_log_binding.UnformattedMessageListType
    _binding_var = "Unformatted_Message"
    _contained_type = String
    _namespace = "http://cybox.mitre.org/objects#WinEventLogObject-2"

class WinEventLog(ObjectProperties):
    _binding = win_event_log_binding
    _binding_class = win_event_log_binding.WindowsEventLogObjectType
    _namespace = "http://cybox.mitre.org/objects#WinEventLogObject-2"
    _XSI_NS = "WinEventLogObj"
    _XSI_TYPE = "WindowsEventLogObjectType"

    eid = cybox.TypedField("EID", Long)
    type = cybox.TypedField("Type", String)
    log = cybox.TypedField("Log", String)
    message = cybox.TypedField("Message", String)
    category_num = cybox.TypedField("Category_Num", Long)
    category = cybox.TypedField("Category", String)
    generation_time = cybox.TypedField("Generation_Time", DateTime)
    source = cybox.TypedField("Source", String)
    machine = cybox.TypedField("Machine", String)
    user = cybox.TypedField("User", String)
    blob = cybox.TypedField("Blob", Base64Binary)
    correlation_activity_id = cybox.TypedField("Correlation_Activity_ID", String)
    correlation_related_activity_id = cybox.TypedField("Correlation_Related_Activity_ID", String)
    execution_process_id = cybox.TypedField("Execution_Process_ID", String)
    execution_thread_id = cybox.TypedField("Execution_Thread_ID", String)
    index = cybox.TypedField("Index", Long)
    reserved = cybox.TypedField("Reserved", Long)
    unformatted_message_list = cybox.TypedField("Unformatted_Message_List", UnformattedMessageList)
    write_time = cybox.TypedField("Write_Time", DateTime)


