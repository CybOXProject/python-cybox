# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.win_process_object as win_process_binding
from cybox.common import String, Integer, PositiveInteger
from cybox.objects.process_object import Process
from cybox.objects.win_handle_object import WinHandleList
from cybox.objects.win_handle_object import WinHandle
from cybox.objects.win_thread_object import WinThread
from cybox.objects.memory_object import Memory


class MemorySectionList(entities.EntityList):
    _binding = win_process_binding
    _binding_class = win_process_binding.MemorySectionListType
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"
    memory_section = fields.TypedField("Memory_Section", Memory, multiple=True)


class StartupInfo(entities.Entity):
    _binding = win_process_binding
    _binding_class = win_process_binding.StartupInfoType
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"

    lpdesktop = fields.TypedField("lpDesktop", String)
    lptitle = fields.TypedField("lpTitle", String)
    dwx = fields.TypedField("dwX", Integer)
    dwy = fields.TypedField("dwY", Integer)
    dwxsize = fields.TypedField("dwXSize", PositiveInteger)
    dwysize = fields.TypedField("dwYSize", PositiveInteger)
    dwxcountchars = fields.TypedField("dwXCountChars", PositiveInteger)
    dwycountchars = fields.TypedField("dwYCountChars", PositiveInteger)
    dwfillattribute = fields.TypedField("dwFillAttribute", Integer)
    dwflags = fields.TypedField("dwFlags", Integer)
    wshowwindow = fields.TypedField("wShowWindow", Integer)
    hstdinput = fields.TypedField("hStdInput", WinHandle)
    hstdoutput = fields.TypedField("hStdOutput", WinHandle)
    hstderror = fields.TypedField("hStdError", WinHandle)


class WinProcess(Process):
    _binding = win_process_binding
    _binding_class = win_process_binding.WindowsProcessObjectType
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"
    _XSI_NS = "WinProcessObj"
    _XSI_TYPE = "WindowsProcessObjectType"

    aslr_enabled = fields.TypedField("aslr_enabled")
    dep_enabled = fields.TypedField("dep_enabled")
    handle_list = fields.TypedField("Handle_List", WinHandleList)
    priority = fields.TypedField("Priority", String)
    section_list = fields.TypedField("Section_List", MemorySectionList)
    security_id = fields.TypedField("Security_ID", String)
    startup_info = fields.TypedField("Startup_Info", StartupInfo)
    security_type = fields.TypedField("Security_Type", String)
    window_title = fields.TypedField("Window_Title", String)
    thread = fields.TypedField("Thread", WinThread, multiple=True)
