# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import memory_object
from . import process_object
from . import win_handle_object
from . import win_thread_object


class MemorySectionListType(GeneratedsSuper):
    """The MemorySectionListType type specifies a list of memory sections
    used by the process."""

    subclass = None
    superclass = None
    def __init__(self, Memory_Section=None):
        if Memory_Section is None:
            self.Memory_Section = []
        else:
            self.Memory_Section = Memory_Section
    def factory(*args_, **kwargs_):
        if MemorySectionListType.subclass:
            return MemorySectionListType.subclass(*args_, **kwargs_)
        else:
            return MemorySectionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Memory_Section(self): return self.Memory_Section
    def set_Memory_Section(self, Memory_Section): self.Memory_Section = Memory_Section
    def add_Memory_Section(self, value): self.Memory_Section.append(value)
    def insert_Memory_Section(self, index, value): self.Memory_Section[index] = value
    def hasContent_(self):
        if (
            self.Memory_Section
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinProcessObj:', name_='MemorySectionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MemorySectionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinProcessObj:', name_='MemorySectionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinProcessObj:', name_='MemorySectionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Memory_Section_ in self.Memory_Section:
            Memory_Section_.export(lwrite, level, 'WinProcessObj:', name_='Memory_Section', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Memory_Section':
            obj_ = memory_object.MemoryObjectType.factory()
            obj_.build(child_)
            self.Memory_Section.append(obj_)
# end class MemorySectionListType

class StartupInfoType(GeneratedsSuper):
    """The StartupInfoType type encapsulates the information contained in
    the STARTUPINFO struct for the process."""

    subclass = None
    superclass = None
    def __init__(self, lpDesktop=None, lpTitle=None, dwX=None, dwY=None, dwXSize=None, dwYSize=None, dwXCountChars=None, dwYCountChars=None, dwFillAttribute=None, dwFlags=None, wShowWindow=None, hStdInput=None, hStdOutput=None, hStdError=None):
        self.lpDesktop = lpDesktop
        self.lpTitle = lpTitle
        self.dwX = dwX
        self.dwY = dwY
        self.dwXSize = dwXSize
        self.dwYSize = dwYSize
        self.dwXCountChars = dwXCountChars
        self.dwYCountChars = dwYCountChars
        self.dwFillAttribute = dwFillAttribute
        self.dwFlags = dwFlags
        self.wShowWindow = wShowWindow
        self.hStdInput = hStdInput
        self.hStdOutput = hStdOutput
        self.hStdError = hStdError
    def factory(*args_, **kwargs_):
        if StartupInfoType.subclass:
            return StartupInfoType.subclass(*args_, **kwargs_)
        else:
            return StartupInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_lpDesktop(self): return self.lpDesktop
    def set_lpDesktop(self, lpDesktop): self.lpDesktop = lpDesktop
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_lpTitle(self): return self.lpTitle
    def set_lpTitle(self, lpTitle): self.lpTitle = lpTitle
    def get_dwX(self): return self.dwX
    def set_dwX(self, dwX): self.dwX = dwX
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_dwY(self): return self.dwY
    def set_dwY(self, dwY): self.dwY = dwY
    def get_dwXSize(self): return self.dwXSize
    def set_dwXSize(self, dwXSize): self.dwXSize = dwXSize
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_dwYSize(self): return self.dwYSize
    def set_dwYSize(self, dwYSize): self.dwYSize = dwYSize
    def get_dwXCountChars(self): return self.dwXCountChars
    def set_dwXCountChars(self, dwXCountChars): self.dwXCountChars = dwXCountChars
    def get_dwYCountChars(self): return self.dwYCountChars
    def set_dwYCountChars(self, dwYCountChars): self.dwYCountChars = dwYCountChars
    def get_dwFillAttribute(self): return self.dwFillAttribute
    def set_dwFillAttribute(self, dwFillAttribute): self.dwFillAttribute = dwFillAttribute
    def get_dwFlags(self): return self.dwFlags
    def set_dwFlags(self, dwFlags): self.dwFlags = dwFlags
    def get_wShowWindow(self): return self.wShowWindow
    def set_wShowWindow(self, wShowWindow): self.wShowWindow = wShowWindow
    def get_hStdInput(self): return self.hStdInput
    def set_hStdInput(self, hStdInput): self.hStdInput = hStdInput
    def get_hStdOutput(self): return self.hStdOutput
    def set_hStdOutput(self, hStdOutput): self.hStdOutput = hStdOutput
    def get_hStdError(self): return self.hStdError
    def set_hStdError(self, hStdError): self.hStdError = hStdError
    def hasContent_(self):
        if (
            self.lpDesktop is not None or
            self.lpTitle is not None or
            self.dwX is not None or
            self.dwY is not None or
            self.dwXSize is not None or
            self.dwYSize is not None or
            self.dwXCountChars is not None or
            self.dwYCountChars is not None or
            self.dwFillAttribute is not None or
            self.dwFlags is not None or
            self.wShowWindow is not None or
            self.hStdInput is not None or
            self.hStdOutput is not None or
            self.hStdError is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinProcessObj:', name_='StartupInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StartupInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinProcessObj:', name_='StartupInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinProcessObj:', name_='StartupInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.lpDesktop is not None:
            self.lpDesktop.export(lwrite, level, 'WinProcessObj:', name_='lpDesktop', pretty_print=pretty_print)
        if self.lpTitle is not None:
            self.lpTitle.export(lwrite, level, 'WinProcessObj:', name_='lpTitle', pretty_print=pretty_print)
        if self.dwX is not None:
            self.dwX.export(lwrite, level, 'WinProcessObj:', name_='dwX', pretty_print=pretty_print)
        if self.dwY is not None:
            self.dwY.export(lwrite, level, 'WinProcessObj:', name_='dwY', pretty_print=pretty_print)
        if self.dwXSize is not None:
            self.dwXSize.export(lwrite, level, 'WinProcessObj:', name_='dwXSize', pretty_print=pretty_print)
        if self.dwYSize is not None:
            self.dwYSize.export(lwrite, level, 'WinProcessObj:', name_='dwYSize', pretty_print=pretty_print)
        if self.dwXCountChars is not None:
            self.dwXCountChars.export(lwrite, level, 'WinProcessObj:', name_='dwXCountChars', pretty_print=pretty_print)
        if self.dwYCountChars is not None:
            self.dwYCountChars.export(lwrite, level, 'WinProcessObj:', name_='dwYCountChars', pretty_print=pretty_print)
        if self.dwFillAttribute is not None:
            self.dwFillAttribute.export(lwrite, level, 'WinProcessObj:', name_='dwFillAttribute', pretty_print=pretty_print)
        if self.dwFlags is not None:
            self.dwFlags.export(lwrite, level, 'WinProcessObj:', name_='dwFlags', pretty_print=pretty_print)
        if self.wShowWindow is not None:
            self.wShowWindow.export(lwrite, level, 'WinProcessObj:', name_='wShowWindow', pretty_print=pretty_print)
        if self.hStdInput is not None:
            self.hStdInput.export(lwrite, level, 'WinProcessObj:', name_='hStdInput', pretty_print=pretty_print)
        if self.hStdOutput is not None:
            self.hStdOutput.export(lwrite, level, 'WinProcessObj:', name_='hStdOutput', pretty_print=pretty_print)
        if self.hStdError is not None:
            self.hStdError.export(lwrite, level, 'WinProcessObj:', name_='hStdError', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'lpDesktop':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_lpDesktop(obj_)
        elif nodeName_ == 'lpTitle':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_lpTitle(obj_)
        elif nodeName_ == 'dwX':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwX(obj_)
        elif nodeName_ == 'dwY':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwY(obj_)
        elif nodeName_ == 'dwXSize':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwXSize(obj_)
        elif nodeName_ == 'dwYSize':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwYSize(obj_)
        elif nodeName_ == 'dwXCountChars':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwXCountChars(obj_)
        elif nodeName_ == 'dwYCountChars':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwYCountChars(obj_)
        elif nodeName_ == 'dwFillAttribute':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwFillAttribute(obj_)
        elif nodeName_ == 'dwFlags':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_dwFlags(obj_)
        elif nodeName_ == 'wShowWindow':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_wShowWindow(obj_)
        elif nodeName_ == 'hStdInput':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_hStdInput(obj_)
        elif nodeName_ == 'hStdOutput':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_hStdOutput(obj_)
        elif nodeName_ == 'hStdError':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_hStdError(obj_)
# end class StartupInfoType

class WindowsProcessObjectType(process_object.ProcessObjectType):
    """The WindowsProcessObjectType type is intended to characterize
    Windows processes.The aslr_enabled field specifies whether
    Address Space Layout Randomization (ASLR) is enabled for the
    process.The dep_enabled field specifies whether Data Execution
    Prevention (DEP) is enabled for the process."""

    subclass = None
    superclass = process_object.ProcessObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_hidden=None, PID=None, Name=None, Creation_Time=None, Parent_PID=None, Child_PID_List=None, Image_Info=None, Argument_List=None, Environment_Variable_List=None, Kernel_Time=None, Port_List=None, Network_Connection_List=None, Start_Time=None, Status=None, Username=None, User_Time=None, Extracted_Features=None, aslr_enabled=None, dep_enabled=None, Handle_List=None, Priority=None, Section_List=None, Security_ID=None, Startup_Info=None, Security_Type=None, Window_Title=None, Thread=None):
        super(WindowsProcessObjectType, self).__init__(object_reference, Custom_Properties, is_hidden, PID, Name, Creation_Time, Parent_PID, Child_PID_List, Image_Info, Argument_List, Environment_Variable_List, Kernel_Time, Port_List, Network_Connection_List, Start_Time, Status, Username, User_Time, Extracted_Features, )
        self.aslr_enabled = _cast(bool, aslr_enabled)
        self.dep_enabled = _cast(bool, dep_enabled)
        self.Handle_List = Handle_List
        self.Priority = Priority
        self.Section_List = Section_List
        self.Security_ID = Security_ID
        self.Startup_Info = Startup_Info
        self.Security_Type = Security_Type
        self.Window_Title = Window_Title
        if not Thread:
            self.Thread = []
        else:
            self.Thread = Thread
    def factory(*args_, **kwargs_):
        if WindowsProcessObjectType.subclass:
            return WindowsProcessObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsProcessObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Handle_List(self): return self.Handle_List
    def set_Handle_List(self, Handle_List): self.Handle_List = Handle_List
    def get_Priority(self): return self.Priority
    def set_Priority(self, Priority): self.Priority = Priority
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Section_List(self): return self.Section_List
    def set_Section_List(self, Section_List): self.Section_List = Section_List
    def get_Security_ID(self): return self.Security_ID
    def set_Security_ID(self, Security_ID): self.Security_ID = Security_ID
    def get_Startup_Info(self): return self.Startup_Info
    def set_Startup_Info(self, Startup_Info): self.Startup_Info = Startup_Info
    def get_Security_Type(self): return self.Security_Type
    def set_Security_Type(self, Security_Type): self.Security_Type = Security_Type
    def validate_SIDType(self, value):
        # Validate type cybox_common.SIDType, a restriction on None.
        pass
    def get_Window_Title(self): return self.Window_Title
    def set_Window_Title(self, Window_Title): self.Window_Title = Window_Title
    def get_Thread(self): return self.Thread
    def set_Thread(self, Thread): self.Thread = Thread
    def add_Thread(self, Thread): self.Thread.append(Thread)
    def get_aslr_enabled(self): return self.aslr_enabled
    def set_aslr_enabled(self, aslr_enabled): self.aslr_enabled = aslr_enabled
    def get_dep_enabled(self): return self.dep_enabled
    def set_dep_enabled(self, dep_enabled): self.dep_enabled = dep_enabled
    def hasContent_(self):
        if (
            self.Handle_List is not None or
            self.Priority is not None or
            self.Section_List is not None or
            self.Security_ID is not None or
            self.Startup_Info is not None or
            self.Security_Type is not None or
            self.Window_Title is not None or
            self.Thread or
            super(WindowsProcessObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinProcessObj:', name_='WindowsProcessObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsProcessObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinProcessObj:', name_='WindowsProcessObjectType'):
        super(WindowsProcessObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsProcessObjectType')
        if self.aslr_enabled is not None:

            lwrite(' aslr_enabled="%s"' % self.gds_format_boolean(self.aslr_enabled, input_name='aslr_enabled'))
        if self.dep_enabled is not None:

            lwrite(' dep_enabled="%s"' % self.gds_format_boolean(self.dep_enabled, input_name='dep_enabled'))
    def exportChildren(self, lwrite, level, namespace_='WinProcessObj:', name_='WindowsProcessObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsProcessObjectType, self).exportChildren(lwrite, level, 'WinProcessObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Handle_List is not None:
            self.Handle_List.export(lwrite, level, 'WinProcessObj:', name_='Handle_List', pretty_print=pretty_print)
        if self.Priority is not None:
            self.Priority.export(lwrite, level, 'WinProcessObj:', name_='Priority', pretty_print=pretty_print)
        if self.Section_List is not None:
            self.Section_List.export(lwrite, level, 'WinProcessObj:', name_='Section_List', pretty_print=pretty_print)
        if self.Security_ID is not None:
            self.Security_ID.export(lwrite, level, 'WinProcessObj:', name_='Security_ID', pretty_print=pretty_print)
        if self.Startup_Info is not None:
            self.Startup_Info.export(lwrite, level, 'WinProcessObj:', name_='Startup_Info', pretty_print=pretty_print)
        if self.Security_Type is not None:
            self.Security_Type.export(lwrite, level, 'WinProcessObj:', name_='Security_Type', pretty_print=pretty_print)
        if self.Window_Title is not None:
            self.Window_Title.export(lwrite, level, 'WinProcessObj:', name_='Window_Title', pretty_print=pretty_print)
        for Thread_ in self.Thread:
            Thread_.export(lwrite, level, 'WinProcessObj:', name_='Thread', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('aslr_enabled', node)
        if value is not None:

            if value in ('true', '1'):
                self.aslr_enabled = True
            elif value in ('false', '0'):
                self.aslr_enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('dep_enabled', node)
        if value is not None:

            if value in ('true', '1'):
                self.dep_enabled = True
            elif value in ('false', '0'):
                self.dep_enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(WindowsProcessObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Handle_List':
            obj_ = win_handle_object.WindowsHandleListType.factory()
            obj_.build(child_)
            self.set_Handle_List(obj_)
        elif nodeName_ == 'Priority':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Priority(obj_)
        elif nodeName_ == 'Section_List':
            obj_ = MemorySectionListType.factory()
            obj_.build(child_)
            self.set_Section_List(obj_)
        elif nodeName_ == 'Security_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_ID(obj_)
        elif nodeName_ == 'Startup_Info':
            obj_ = StartupInfoType.factory()
            obj_.build(child_)
            self.set_Startup_Info(obj_)
        elif nodeName_ == 'Security_Type':
            obj_ = cybox_common.SIDType.factory()
            obj_.build(child_)
            self.set_Security_Type(obj_)
        elif nodeName_ == 'Window_Title':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Window_Title(obj_)
        elif nodeName_ == 'Thread':
            obj_ = win_thread_object.WindowsThreadObjectType.factory()
            obj_.build(child_)
            self.Thread.append(obj_)
        super(WindowsProcessObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsProcessObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'lpDesktop': cybox_common.StringObjectPropertyType,
    'Argument_List': process_object.ArgumentListType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Path': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Byte_Run': cybox_common.ByteRunType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'Region_Start_Address': cybox_common.HexBinaryObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.PositiveIntegerObjectPropertyType,
    'Expect': cybox_common.StringObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'TE': cybox_common.StringObjectPropertyType,
    'Parent_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Warning': cybox_common.StringObjectPropertyType,
    'Memory_Region': memory_object.MemoryObjectType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Memory_Section': memory_object.MemoryObjectType,
    'Segments': cybox_common.HashSegmentsType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Priority': cybox_common.StringObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'lpTitle': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'hStdOutput': win_handle_object.WindowsHandleObjectType,
    'Link': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'dwFlags': cybox_common.IntegerObjectPropertyType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Via': cybox_common.StringObjectPropertyType,
    'X_Requested_For': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Security_Type': cybox_common.SIDType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Server': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Child_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'wShowWindow': cybox_common.IntegerObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'User_Time': cybox_common.DurationObjectPropertyType,
    'dwYSize': cybox_common.PositiveIntegerObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Handle_List': win_handle_object.WindowsHandleListType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'dwXSize': cybox_common.PositiveIntegerObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
    'dwFillAttribute': cybox_common.IntegerObjectPropertyType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Status': process_object.ProcessStatusType,
    'Window_Title': cybox_common.StringObjectPropertyType,
    'Current_Directory': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'hStdError': win_handle_object.WindowsHandleObjectType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Child_PID_List': process_object.ChildPIDListType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'dwX': cybox_common.IntegerObjectPropertyType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Address_Class': cybox_common.StringObjectPropertyType,
    'hStdInput': win_handle_object.WindowsHandleObjectType,
    'Command_Line': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Connection': cybox_common.StringObjectPropertyType,
    'X_Requested_With': cybox_common.StringObjectPropertyType,
    'Kernel_Time': cybox_common.DurationObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'P3P': cybox_common.StringObjectPropertyType,
    'If_Unmodified_Since': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'dwXCountChars': cybox_common.PositiveIntegerObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Process': process_object.ProcessObjectType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'Image_Info': process_object.ImageInfoType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'dwY': cybox_common.IntegerObjectPropertyType,
    'Argument': cybox_common.StringObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'Security_ID': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Network_Connection_List': process_object.NetworkConnectionListType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Port_List': process_object.PortListType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Region_Size': cybox_common.UnsignedLongObjectPropertyType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'dwYCountChars': cybox_common.PositiveIntegerObjectPropertyType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'ETag': cybox_common.StringObjectPropertyType,
    'Date_Ran': cybox_common.DateTimeObjectPropertyType,
    'Contributor': cybox_common.ContributorType,
    'If_Match': cybox_common.StringObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Process'
        rootClass = WindowsProcessObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_=rootTag,
#        namespacedef_='',
#        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Process'
        rootClass = WindowsProcessObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Windows_Process'
        rootClass = WindowsProcessObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Process",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "WindowsProcessObjectType",
    "MemorySectionListType",
    "StartupInfoType"
    ]
