# Copyright (c) 2020, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities, fields

import cybox
import cybox.bindings.unix_process_object as unix_process_binding
from cybox.common import BaseProperty, DateTime, NonNegativeInteger, UnsignedInteger
from cybox.objects.process_object import Process, ProcessStatus


class FileDescriptorList(entities.EntityList):
    _binding = unix_process_binding
    _binding_class = unix_process_binding.FileDescriptorListType
    _namespace = "http://cybox.mitre.org/objects#UnixProcessObject-2"

    file_descriptor = fields.TypedField("File_Descriptor", UnsignedInteger, multiple=True)


class UnixProcessState(BaseProperty):
    _binding = unix_process_binding
    _binding_class = unix_process_binding.UnixProcessStateType
    _namespace = "http://cybox.mitre.org/objects#UnixProcessObject-2"

    STATE_RUNNING = "Running"
    STATE_UNINTERRUPTIBLE_SLEEP = "UninterruptibleSleep"
    STATE_INTERRUPTIBLE_SLEEP = "InterruptibleSleep"
    STATE_STOPPED = "Stopped"
    STATE_PAGING = "Paging"
    STATE_DEAD = "Dead"
    STATE_ZOMBIE = "Zombie"


@cybox.register_extension
class UnixProcessStatus(ProcessStatus):
    _binding = unix_process_binding
    _binding_class = unix_process_binding.UnixProcessStatusType
    _namespace = "http://cybox.mitre.org/objects#UnixProcessObject-2"
    _XSI_TYPE = "UnixProcessObj:UnixProcessStatusType"

    current_status = fields.TypedField("Current_Status", UnixProcessState)
    timestamp = fields.TypedField("Timestamp", DateTime)


class UnixProcess(Process):
    _binding = unix_process_binding
    _binding_class = unix_process_binding.UnixProcessObjectType
    _namespace = "http://cybox.mitre.org/objects#UnixProcessObject-2"
    _XSI_NS = "UnixProcessObj"
    _XSI_TYPE = "UnixProcessObjectType"

    open_file_descriptor_list = fields.TypedField("Open_File_Descriptor_List", FileDescriptorList)
    priority = fields.TypedField("Priority", NonNegativeInteger)
    ruid = fields.TypedField("RUID", NonNegativeInteger)
    session_id = fields.TypedField("Session_ID", NonNegativeInteger)
