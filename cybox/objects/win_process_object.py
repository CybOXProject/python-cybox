# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_process_object as win_process_binding
from cybox.objects.process_object import Process
from cybox.objects.win_handle_object import WinHandleList
from cybox.objects.win_handle_object import WinHandle
from cybox.objects.win_thread_object import WinThread
from cybox.objects.memory_object import Memory
from cybox.common import String, Integer, PositiveInteger


class MemorySectionList(cybox.EntityList):
    _binding = win_process_binding
    _binding_class = win_process_binding.MemorySectionListType
    _binding_var = "Memory_Section"
    _contained_type = Memory
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"

class StartupInfo(cybox.Entity):
    _binding = win_process_binding
    _binding_class = win_process_binding.StartupInfoType
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"

    lpdesktop = cybox.TypedField("lpDesktop", String)
    lptitle = cybox.TypedField("lpTitle", String)
    dwx = cybox.TypedField("dwX", Integer)
    dwy = cybox.TypedField("dwY", Integer)
    dwxsize = cybox.TypedField("dwXSize", PositiveInteger)
    dwysize = cybox.TypedField("dwYSize", PositiveInteger)
    dwxcountchars = cybox.TypedField("dwXCountChars", PositiveInteger)
    dwycountchars = cybox.TypedField("dwYCountChars", PositiveInteger)
    dwfillattribute = cybox.TypedField("dwFillAttribute", Integer)
    dwflags = cybox.TypedField("dwFlags", Integer)
    wshowwindow = cybox.TypedField("wShowWindow", Integer)
    hstdinput = cybox.TypedField("hStdInput", WinHandle)
    hstdoutput = cybox.TypedField("hStdOutput", WinHandle)
    hstderror = cybox.TypedField("hStdError", WinHandle)

class WinProcess(Process):
    _binding = win_process_binding
    _binding_class = win_process_binding.WindowsProcessObjectType
    _namespace = "http://cybox.mitre.org/objects#WinProcessObject-2"
    _XSI_NS = "WinProcessObj"
    _XSI_TYPE = "WindowsProcessObjectType"

    aslr_enabled = cybox.TypedField("aslr_enabled")
    dep_enabled = cybox.TypedField("dep_enabled")
    handle_list = cybox.TypedField("Handle_List", WinHandleList)
    priority = cybox.TypedField("Priority", String)
    section_list = cybox.TypedField("Section_List", MemorySectionList)
    security_id = cybox.TypedField("Security_ID", String)
    startup_info = cybox.TypedField("Startup_Info", StartupInfo)
    security_type = cybox.TypedField("Security_Type", String)
    window_title = cybox.TypedField("Window_Title", String)
    thread = cybox.TypedField("Thread", WinThread, multiple=True)
