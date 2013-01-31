import common_methods
import cybox.bindings.cybox_common_types_1_0 as common_types_binding
import cybox.bindings.win_process_object_1_3 as win_process_binding
import cybox.bindings.win_handle_object_1_3 as win_handle_binding
from cybox.common.baseobjectattribute import baseobjectattribute
from cybox.objects.process_object import Process
from cybox.objects.win_handle_object import Win_Handle_List
from cybox.objects.win_handle_object import Win_Handle
from cybox.objects.memory_object import Memory

class Win_Process:
    def __init__(self):
        pass
        
    @classmethod
    def object_from_dict(cls, win_process_dict):
        """Create the Win Process Object object representation from an input dictionary"""
        win_process_obj = Process.object_from_dict(win_process_dict,win_process_binding.WindowsProcessObjectType())
        win_process_obj.set_anyAttributes_({'xsi:type' : 'WinProcessObj:WindowsProcessObjectType'})
        
        for key, value in win_process_dict.items():
            if key == 'aslr_enabled' and common_methods.test_value(value): win_process_obj.set_aslr_enabled(value.get('value'))
            elif key == 'dep_enabled' and common_methods.test_value(value): win_process_obj.set_dep_enabled(value.get('value'))
            elif key == 'handle_list' : 
                win_process_obj.set_Handle_List(Win_Handle_List.object_from_dict(value))
            elif key == 'priority' and common_methods.test_value(value):
                win_process_obj.set_Priority(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'section_list' :
                memory_section_list = win_process_binding.MemorySectionListType()
                for memory_section in value:
                    memory_obj = Memory.object_from_dict(memory_section)
                    if memory_obj.hasContent_() : memory_section_list.add_Memory_Section(memory_obj)
                if memory_section_list.hasContent_() : win_process_obj.set_Section_List(memory_section_list)
            elif key == 'security_id' and common_methods.test_value(value): 
                win_process_obj.set_Security_ID(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'startup_info' : 
                startup_info_obj = cls.__startup_info_from_dict(value)
                if startup_info_obj.hasContent_() : win_process_obj.set_Startup_Info()
            elif key == 'security_type' and common_methods.test_value(value): 
                win_process_obj.set_Security_Type(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
            elif key == 'window_title' and common_methods.test_value(value): 
                win_process_obj.set_Window_Title(baseobjectattribute.object_from_dict(common_binding.StringObjectAttributeType(datatype='String'),value))
        return win_proc_obj

    @classmethod
    def dict_from_object(cls, win_process_obj):
        """Parse and return a dictionary for a Win Process Object object"""
        win_process_dict = Process.dict_from_object(win_process_obj)
        if win_process_obj.get_aslr_enabled() is not None: win_process_dict['aslr_enabled'] = {'value':win_process_obj.get_aslr_enabled()}
        if win_process_obj.get_dep_enabled() is not None: win_process_dict['dep_enabled'] = {'value':win_process_obj.get_dep_enabled()}
        if win_process_obj.get_Handle_List() is not None: win_process_dict['handle_list'] = Win_Handle_List.dict_from_object(win_process_obj.get_Handle_List())
        if win_process_obj.get_Priority() is not None: win_process_dict['priority'] = baseobjectattribute.dict_from_object(win_process_obj.get_Priority())
        if win_process_obj.get_Section_List() is not None: 
            memory_section_list = []
            for memory_section in win_process_obj.get_Section_List().get_Memory_Section():
                memory_section_list.append(Memory.dict_from_object(memory_section))
            win_process_dict['section_list'] = memory_section_list
        if win_process_obj.get_Security_ID() is not None: win_process_dict['security_id'] = baseobjectattribute.dict_from_object(win_process_obj.get_Security_ID())
        if win_process_obj.get_Startup_Info() is not None: win_process_dict['startup_info'] = cls.__dict_from_startup_info(win_process_obj.get_Startup_Info())
        if win_process_obj.get_Security_Type() is not None: win_process_dict['security_type'] = baseobjectattribute.dict_from_object(win_process_obj.get_Security_Type())
        if win_process_obj.get_Window_Title() is not None: win_process_dict['window_title'] = baseobjectattribute.dict_from_object(win_process_obj.get_Window_Title())
        return win_process_dict

    @classmethod
    def __dict_from_startup_info(cls, startup_info_obj):
        startup_info_dict = {}
        if startup_info_obj.get_lpDesktop() is not None: startup_info_dict['lpdesktop'] = baseobjectattribute.dict_from_object(startup_info_obj.get_lpDesktop())
        if startup_info_obj.get_lpTitle() is not None: startup_info_dict['lptitle'] = baseobjectattribute.dict_from_object(startup_info_obj.get_lpTitle())
        if startup_info_obj.get_dwX() is not None: startup_info_dict['dwx'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwX())
        if startup_info_obj.get_dwY() is not None: startup_info_dict['dwy'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwY())
        if startup_info_obj.get_dwXSize() is not None: startup_info_dict['dwxsize'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwXSize())
        if startup_info_obj.get_dwYSize() is not None: startup_info_dict['dwysize'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwYSize())
        if startup_info_obj.get_dwXCountChars() is not None: startup_info_dict['dwxcountchars'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwXCountChars())
        if startup_info_obj.get_dwYCountChars() is not None: startup_info_dict['dwycountchars'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwYCountChars())
        if startup_info_obj.get_dwFillAttribute() is not None: startup_info_dict['dwfillattribute'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwFillAttribute())
        if startup_info_obj.get_dwFlags() is not None: startup_info_dict['dwflags'] = baseobjectattribute.dict_from_object(startup_info_obj.get_dwFlags())
        if startup_info_obj.get_wShowWindow() is not None: startup_info_dict['wshowwindow'] = baseobjectattribute.dict_from_object(startup_info_obj.get_wShowWindow())
        if startup_info_obj.get_hStdInput() is not None: startup_info_dict['hstdinput'] = baseobjectattribute.dict_from_object(startup_info_obj.get_hStdInput())
        if startup_info_obj.get_hStdOutput() is not None: startup_info_dict['hstdoutput'] = baseobjectattribute.dict_from_object(startup_info_obj.get_hStdOutput())
        if startup_info_obj.get_hStdError() is not None: startup_info_dict['hstderror'] = baseobjectattribute.dict_from_object(startup_info_obj.get_hStdError())
        return startup_info_dict

    @classmethod
    def __startup_info_from_dict(cls, startup_info_dict):
        startup_info_obj = win_process_binding.StartupInfoType()
        for key, value in startup_info_dict.items():
            if key == 'lpdesktop' and common_methods.test_value(value): 
                startup_info_obj.set_lpDesktop(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'lptitle' and common_methods.test_value(value): 
                startup_info_obj.set_lpTitle(baseobjectattribute.object_from_dict(common_types_binding.StringObjectAttributeType(datatype='String'), value))
            elif key == 'dwx' and common_methods.test_value(value): 
                startup_info_obj.set_dwX(baseobjectattribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'dwy' and common_methods.test_value(value): 
                startup_info_obj.set_dwY(baseobjectattribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'dwxsize' and common_methods.test_value(value): 
                startup_info_obj.set_dwXSize(baseobjectattribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'), value))
            elif key == 'dwysize' and common_methods.test_value(value): 
                startup_info_obj.set_dwYSize(baseobjectattribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'), value))
            elif key == 'dwxcountchars' and common_methods.test_value(value): 
                startup_info_obj.set_dwXCountChars(baseobjectattribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'), value))
            elif key == 'dwycountchars' and common_methods.test_value(value): 
                startup_info_obj.set_dwYCountChars(baseobjectattribute.object_from_dict(common_types_binding.PositiveIntegerObjectAttributeType(datatype='PositiveInteger'), value))
            elif key == 'dwfillattribute' and common_methods.test_value(value): 
                startup_info_obj.set_dwFillAttribute(baseobjectattribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'dwflags' and common_methods.test_value(value): 
                startup_info_obj.set_dwFlags(baseobjectattribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'wshowwindow' and common_methods.test_value(value): 
                startup_info_obj.set_wShowWindow(baseobjectattribute.object_from_dict(common_types_binding.IntegerObjectAttributeType(datatype='Integer'), value))
            elif key == 'hstdinput': 
                startup_info_obj.set_hStdInput(Win_Handle.object_from_dict(value))
            elif key == 'hstdoutput' and common_methods.test_value(value): 
                startup_info_obj.set_hStdOutput(Win_Handle.object_from_dict(value))
            elif key == 'hstderror' and common_methods.test_value(value): 
                startup_info_obj.set_hStdError(Win_Handle.object_from_dict(value))
        return startup_info_obj