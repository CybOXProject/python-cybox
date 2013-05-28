# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import cybox
import cybox.bindings.win_process_object as win_process_binding
from cybox.objects.process_object import Process
from cybox.objects.win_handle_object import WinHandleList
from cybox.objects.win_handle_object import WinHandle
from cybox.objects.memory_object import Memory
from cybox.common import String

class WinProcess(Process):
    _XSI_NS = "WinProcessObj"
    _XSI_TYPE = "WindowsProcessObjectType"
    superclass = Process

    def __init__(self):
        super(WinProcess, self).__init__()
        self.aslr_enabled = None
        self.dep_enabled = None
        self.handle_list = None
        self.priority = None
        self.section_list = []
        self.security_id = None
        self.startup_info = None
        self.security_type = None
        self.window_title = None

    def to_obj(self, process_obj = None):
        if process_obj == None:
            win_process_obj = super(WinProcess, self).to_obj(win_process_binding.WindowsProcessObjectType())
        else:
            win_process_obj = super(WinProcess, self).to_obj(process_obj)

        if self.aslr_enabled is not None: win_process_obj.set_aslr_enabled(self.aslr_enabled)
        if self.dep_enabled is not None: win_process_obj.set_dep_enabled(self.dep_enabled)
        if self.handle_list is not None: win_process_obj.set_Handle_List(self.handle_list.to_obj())
        if self.priority is not None: win_process_obj.set_Priority(self.priority.to_obj())
        if len(self.section_list) > 0: 
            section_list_obj = win_process_binding.MemorySectionListType()
            for section_obj in self.section_list:
                section_list_obj.add_Memory_Section(section_obj.to_obj())
            win_process_obj.set_Section_List(section_list_obj)
        if self.security_id is not None: win_process_obj.set_Security_ID(self.security_id.to_obj())
        if self.startup_info is not None: win_process_obj.set_Startup_Info(self.startup_info.to_obj())
        if self.security_type is not None: win_process_obj.set_Security_Type(self.security_type.to_obj())
        if self.window_title is not None: win_process_obj.set_Window_Title(self.window_title.to_obj())

        return win_process_obj

    def to_dict(self):
        win_process_dict = super(WinProcess, self).to_dict()

        if self.aslr_enabled is not None: win_process_dict['aslr_enabled'] = self.aslr_enabled
        if self.dep_enabled is not None: win_process_dict['dep_enabled'] = self.dep_enabled
        if self.handle_list is not None: win_process_dict['handle_list']  = self.handle_list.to_list()
        if self.priority is not None: win_process_dict['priority']  = self.priority.to_dict()
        if len(self.section_list) > 0: win_process_dict['section_list']  = [Memory.to_dict(x) for x in self.section_list]
        if self.security_id is not None: win_process_dict['security_id']  = self.security_id.to_dict()
        if self.startup_info is not None: win_process_dict['startup_info']  = self.startup_info.to_dict()
        if self.security_type is not None: win_process_dict['security_type']  = self.security_type.to_dict()
        if self.window_title is not None: win_process_dict['window_title']  = self.window_title.to_dict()
        win_process_dict['xsi:type'] = self._XSI_TYPE

        return win_process_dict 
    
    @staticmethod
    def from_dict(win_process_dict, win_process_cls = None):
        if not win_process_dict:
            return None
        if win_process_cls == None:
            winprocess_ = Process.from_dict(win_process_dict, WinProcess())
        else:
            winprocess_ = Process.from_dict(win_process_dict, win_process_cls)

        winprocess_.aslr_enabled = win_process_dict.get('aslr_enabled')
        winprocess_.dep_enabled = win_process_dict.get('dep_enabled')
        winprocess_.handle_list = WinHandleList.from_list(win_process_dict.get('handle_list'))
        winprocess_.priority = String.from_dict(win_process_dict.get('priority'))
        winprocess_.section_list = [Memory.from_dict(x) for x in win_process_dict.get('section_list', [])]
        winprocess_.security_id = String.from_dict(win_process_dict.get('security_id'))
        winprocess_.startup_info = StartupInfo.from_dict(win_process_dict.get('startup_info'))
        winprocess_.security_type = String.from_dict(win_process_dict.get('security_type'))
        winprocess_.window_title = String.from_dict(win_process_dict.get('window_title'))

        return winprocess_

    @staticmethod
    def from_obj(win_process_obj, win_process_cls = None):
        if not win_process_obj:
            return None
        if win_process_cls == None:
            winprocess_ = Process.from_obj(win_process_obj, WinProcess())
        else:
            winprocess_ = Process.from_obj(win_process_obj, win_process_cls)

        winprocess_.aslr_enabled = win_process_obj.get_aslr_enabled()
        winprocess_.dep_enabled = win_process_obj.get_dep_enabled()
        winprocess_.handle_list = WinHandleList.from_obj(win_process_obj.get_Handle_List())
        winprocess_.priority = String.from_obj(win_process_obj.get_Priority())
        if win_process_obj.get_Section_List() is not None:
            winprocess_.section_list = [Memory.from_obj(x) for x in win_process_obj.get_Section_List().get_Memory_Section()]
        winprocess_.security_id = String.from_obj(win_process_obj.get_Security_ID())
        winprocess_.startup_info = StartupInfo.from_obj(win_process_obj.get_Startup_Info())
        winprocess_.security_type = String.from_obj(win_process_obj.get_Security_Type())
        winprocess_.window_title = String.from_obj(win_process_obj.get_Window_Title())

        return winprocess_

class StartupInfo(cybox.Entity):

    def __init__(self):
        super(StartupInfo, self).__init__()
        self.lpdesktop = None
        self.lptitle = None
        self.dwx = None
        self.dwy = None
        self.dwxsize = None
        self.dwysize = None
        self.dwxcountchars = None
        self.dwycountchars = None
        self.dwfillattribute = None
        self.dwflags = None
        self.wshowwindow = None
        self.hstdinput = None
        self.hstdoutput = None
        self.hstderror = None

    def to_obj(self):
        startup_info_obj = win_process_binding.StartupInfoType()

        if self.lpdesktop is not None: startup_info_obj.set_lpDesktop(self.lpdesktop.to_obj())
        if self.lptitle is not None: startup_info_obj.set_lpTitle(self.lptitle.to_obj())
        if self.dwx is not None: startup_info_obj.set_dwX(self.dwx.to_obj())
        if self.dwy is not None: startup_info_obj.set_dwY(self.dwy.to_obj())
        if self.dwxsize is not None: startup_info_obj.set_dwXSize(self.dwxsize.to_obj())
        if self.dwysize is not None: startup_info_obj.set_dwYSize(self.dwysize.to_obj())
        if self.dwxcountchars is not None: startup_info_obj.set_dwXCountChars(self.dwxcountchars.to_obj())
        if self.dwycountchars is not None: startup_info_obj.set_dwYCountChars(self.dwycountchars.to_obj())
        if self.dwfillattribute is not None: startup_info_obj.set_dwFillAttribute(self.dwfillattribute.to_obj())
        if self.dwflags is not None: startup_info_obj.set_dwFlags(self.dwflags.to_obj())
        if self.wshowwindow is not None: startup_info_obj.set_wShowWindow(self.wshowwindow.to_obj())
        if self.hstdinput is not None: startup_info_obj.set_hStdInput(self.hstdinput.to_obj())
        if self.hstdoutput is not None: startup_info_obj.set_hStdOutput(self.hstdoutput.to_obj())

        return startup_info_obj

    def to_dict(self):
        startup_info_dict = {}

        if self.lpdesktop is not None: startup_info_dict['lpdesktop'] = self.lpdesktop.to_dict()
        if self.lptitle is not None: startup_info_dict['lptitle'] = self.lptitle.to_dict()
        if self.dwx is not None: startup_info_dict['dwx'] = self.dwx.to_dict()
        if self.dwy is not None: startup_info_dict['dwy'] = self.dwy.to_dict()
        if self.dwxsize is not None: startup_info_dict['dwxsize'] = self.dwxsize.to_dict()
        if self.dwysize is not None: startup_info_dict['dwysize'] = self.dwysize.to_dict()
        if self.dwxcountchars is not None: startup_info_dict['dwxcountchars'] = self.dwxcountchars.to_dict()
        if self.dwycountchars is not None: startup_info_dict['dwycountchars'] = self.dwycountchars.to_dict()
        if self.dwfillattribute is not None: startup_info_dict['dwfillattribute'] = self.dwfillattribute.to_dict()
        if self.dwflags is not None: startup_info_dict['dwflags'] = self.dwflags.to_dict()
        if self.wshowwindow is not None: startup_info_dict['wshowwindow'] = self.wshowwindow.to_dict()
        if self.hstdinput is not None: startup_info_dict['hstdinput'] = self.hstdinput.to_dict()
        if self.hstdoutput is not None: startup_info_dict['hstdoutput'] = self.hstdoutput.to_dict()

        return startup_info_dict

    @staticmethod
    def from_obj(startup_info_obj):
        if not startup_info_obj:
            return None
        
        startup_info_ = StartupInfo()
        startup_info_.lpdesktop = String.from_obj(startup_info_obj.get_lpDesktop())
        startup_info_.lptitle = String.from_obj(startup_info_obj.get_lpTitle())
        startup_info_.dwx = Integer.from_obj(startup_info_obj.get_dwX())
        startup_info_.dwy = Integer.from_obj(startup_info_obj.get_dwY())
        startup_info_.dwxsize = PositiveInteger.from_obj(startup_info_obj.get_dwXSize())
        startup_info_.dwysize = PositiveInteger.from_obj(startup_info_obj.get_dwYSize())
        startup_info_.dwxcountchars = PositiveInteger.from_obj(startup_info_obj.get_dwXCountChars())
        startup_info_.dwycountchars = PositiveInteger.from_obj(startup_info_obj.get_dwYCountChars())
        startup_info_.dwfillattribute = Integer.from_obj(startup_info_obj.get_dwFillAttribute())
        startup_info_.dwflags = Integer.from_obj(startup_info_obj.get_dwFlags())
        startup_info_.wshowwindow = Integer.from_obj(startup_info_obj.get_wShowWindow())
        startup_info_.hstdinput = WinHandle.from_obj(startup_info_obj.get_hStdInput())
        startup_info_.hstdoutput = WinHandle.from_obj(startup_info_obj.get_hStdOutput())
        startup_info_.hstderror = WinHandle.from_obj(startup_info_obj.get_hStdError())

        return startup_info_

    @staticmethod
    def from_dict(startup_info_dict):
        if not startup_info_dict:
            return None
        
        startup_info_ = StartupInfo()
        startup_info_.lpdesktop = String.from_dict(startup_info_dict.get('lpdesktop'))
        startup_info_.lptitle = String.from_dict(startup_info_dict.get('lptitle'))
        startup_info_.dwx = Integer.from_dict(startup_info_dict.get('dwx'))
        startup_info_.dwy = Integer.from_dict(startup_info_dict.get('dwy'))
        startup_info_.dwxsize = PositiveInteger.from_dict(startup_info_dict.get('dwxsize'))
        startup_info_.dwysize = PositiveInteger.from_dict(startup_info_dict.get('dwysize'))
        startup_info_.dwxcountchars = PositiveInteger.from_dict(startup_info_dict.get('dwxcountchars'))
        startup_info_.dwycountchars = PositiveInteger.from_dict(startup_info_dict.get('dwycountchars'))
        startup_info_.dwfillattribute = Integer.from_dict(startup_info_dict.get('dwfillattribute'))
        startup_info_.dwflags = Integer.from_dict(startup_info_dict.get('dwflags'))
        startup_info_.wshowwindow = Integer.from_dict(startup_info_dict.get('wshowwindow'))
        startup_info_.hstdinput = WinHandle.from_dict(startup_info_dict.get('hstdinput'))
        startup_info_.hstdoutput = WinHandle.from_dict(startup_info_dict.get('hstdoutput'))
        startup_info_.hstderror = WinHandle.from_dict(startup_info_dict.get('hstderror'))

        return startup_info_dict
