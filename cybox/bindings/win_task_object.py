# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import email_message_object


class TriggerListType(GeneratedsSuper):
    """The TriggerListType type specifies a set of triggers associated with
    the scheduled task."""

    subclass = None
    superclass = None
    def __init__(self, Trigger=None):
        if Trigger is None:
            self.Trigger = []
        else:
            self.Trigger = Trigger
    def factory(*args_, **kwargs_):
        if TriggerListType.subclass:
            return TriggerListType.subclass(*args_, **kwargs_)
        else:
            return TriggerListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Trigger(self): return self.Trigger
    def set_Trigger(self, Trigger): self.Trigger = Trigger
    def add_Trigger(self, value): self.Trigger.append(value)
    def insert_Trigger(self, index, value): self.Trigger[index] = value
    def hasContent_(self):
        if (
            self.Trigger
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TriggerListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TriggerListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TriggerListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TriggerListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Trigger_ in self.Trigger:
            Trigger_.export(lwrite, level, 'WinTaskObj:', name_='Trigger', pretty_print=pretty_print)
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
        if nodeName_ == 'Trigger':
            obj_ = TriggerType.factory()
            obj_.build(child_)
            self.Trigger.append(obj_)
# end class TriggerListType

class TriggerType(GeneratedsSuper):
    """The TriggerType type characterizes task triggers. See also:
    http://msdn.microsoft.com/en-
    us/library/windows/desktop/aa383868(v=vs.85).aspxThe enabled
    field specifies whether the trigger is enabled."""

    subclass = None
    superclass = None
    def __init__(self, enabled=None, Trigger_Begin=None, Trigger_Delay=None, Trigger_End=None, Trigger_Frequency=None, Trigger_Max_Run_Time=None, Trigger_Session_Change_Type=None, Trigger_Type=None):
        self.enabled = _cast(bool, enabled)
        self.Trigger_Begin = Trigger_Begin
        self.Trigger_Delay = Trigger_Delay
        self.Trigger_End = Trigger_End
        self.Trigger_Frequency = Trigger_Frequency
        self.Trigger_Max_Run_Time = Trigger_Max_Run_Time
        self.Trigger_Session_Change_Type = Trigger_Session_Change_Type
        self.Trigger_Type = Trigger_Type
    def factory(*args_, **kwargs_):
        if TriggerType.subclass:
            return TriggerType.subclass(*args_, **kwargs_)
        else:
            return TriggerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Trigger_Begin(self): return self.Trigger_Begin
    def set_Trigger_Begin(self, Trigger_Begin): self.Trigger_Begin = Trigger_Begin
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Trigger_Delay(self): return self.Trigger_Delay
    def set_Trigger_Delay(self, Trigger_Delay): self.Trigger_Delay = Trigger_Delay
    def validate_DurationObjectPropertyType(self, value):
        # Validate type cybox_common.DurationObjectPropertyType, a restriction on None.
        pass
    def get_Trigger_End(self): return self.Trigger_End
    def set_Trigger_End(self, Trigger_End): self.Trigger_End = Trigger_End
    def get_Trigger_Frequency(self): return self.Trigger_Frequency
    def set_Trigger_Frequency(self, Trigger_Frequency): self.Trigger_Frequency = Trigger_Frequency
    def validate_TaskTriggerFrequencyType(self, value):
        # Validate type TaskTriggerFrequencyType, a restriction on None.
        pass
    def get_Trigger_Max_Run_Time(self): return self.Trigger_Max_Run_Time
    def set_Trigger_Max_Run_Time(self, Trigger_Max_Run_Time): self.Trigger_Max_Run_Time = Trigger_Max_Run_Time
    def get_Trigger_Session_Change_Type(self): return self.Trigger_Session_Change_Type
    def set_Trigger_Session_Change_Type(self, Trigger_Session_Change_Type): self.Trigger_Session_Change_Type = Trigger_Session_Change_Type
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Trigger_Type(self): return self.Trigger_Type
    def set_Trigger_Type(self, Trigger_Type): self.Trigger_Type = Trigger_Type
    def get_enabled(self): return self.enabled
    def set_enabled(self, enabled): self.enabled = enabled
    def hasContent_(self):
        if (
            self.Trigger_Begin is not None or
            self.Trigger_Delay is not None or
            self.Trigger_End is not None or
            self.Trigger_Frequency is not None or
            self.Trigger_Max_Run_Time is not None or
            self.Trigger_Session_Change_Type is not None or
            self.Trigger_Type is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TriggerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TriggerType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TriggerType'):
        if self.enabled is not None:

            lwrite(' enabled="%s"' % self.gds_format_boolean(self.enabled, input_name='enabled'))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TriggerType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Trigger_Begin is not None:
            self.Trigger_Begin.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Begin', pretty_print=pretty_print)
        if self.Trigger_Delay is not None:
            self.Trigger_Delay.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Delay', pretty_print=pretty_print)
        if self.Trigger_End is not None:
            self.Trigger_End.export(lwrite, level, 'WinTaskObj:', name_='Trigger_End', pretty_print=pretty_print)
        if self.Trigger_Frequency is not None:
            self.Trigger_Frequency.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Frequency', pretty_print=pretty_print)
        if self.Trigger_Max_Run_Time is not None:
            self.Trigger_Max_Run_Time.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Max_Run_Time', pretty_print=pretty_print)
        if self.Trigger_Session_Change_Type is not None:
            self.Trigger_Session_Change_Type.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Session_Change_Type', pretty_print=pretty_print)
        if self.Trigger_Type is not None:
            self.Trigger_Type.export(lwrite, level, 'WinTaskObj:', name_='Trigger_Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('enabled', node)
        if value is not None:

            if value in ('true', '1'):
                self.enabled = True
            elif value in ('false', '0'):
                self.enabled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Trigger_Begin':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Begin(obj_)
        elif nodeName_ == 'Trigger_Delay':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Delay(obj_)
        elif nodeName_ == 'Trigger_End':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_End(obj_)
        elif nodeName_ == 'Trigger_Frequency':
            obj_ = TaskTriggerFrequencyType.factory()
            obj_.build(child_)
            self.set_Trigger_Frequency(obj_)
        elif nodeName_ == 'Trigger_Max_Run_Time':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Max_Run_Time(obj_)
        elif nodeName_ == 'Trigger_Session_Change_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Session_Change_Type(obj_)
        elif nodeName_ == 'Trigger_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Trigger_Type(obj_)
# end class TriggerType

class TaskActionListType(GeneratedsSuper):
    """The TaskActionListType type specifies a list of task actions."""

    subclass = None
    superclass = None
    def __init__(self, Action=None):
        if Action is None:
            self.Action = []
        else:
            self.Action = Action
    def factory(*args_, **kwargs_):
        if TaskActionListType.subclass:
            return TaskActionListType.subclass(*args_, **kwargs_)
        else:
            return TaskActionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action(self): return self.Action
    def set_Action(self, Action): self.Action = Action
    def add_Action(self, value): self.Action.append(value)
    def insert_Action(self, index, value): self.Action[index] = value
    def hasContent_(self):
        if (
            self.Action
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskActionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskActionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Action_ in self.Action:
            Action_.export(lwrite, level, 'WinTaskObj:', name_='Action', pretty_print=pretty_print)
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
        if nodeName_ == 'Action':
            obj_ = TaskActionType.factory()
            obj_.build(child_)
            self.Action.append(obj_)
# end class TaskActionListType

class TaskActionType(GeneratedsSuper):
    """The TaskActionType type characterizes scheduled task actions."""

    subclass = None
    superclass = None
    def __init__(self, Action_Type=None, Action_ID=None, IEmailAction=None, IComHandlerAction=None, IExecAction=None, IShowMessageAction=None):
        self.Action_Type = Action_Type
        self.Action_ID = Action_ID
        self.IEmailAction = IEmailAction
        self.IComHandlerAction = IComHandlerAction
        self.IExecAction = IExecAction
        self.IShowMessageAction = IShowMessageAction
    def factory(*args_, **kwargs_):
        if TaskActionType.subclass:
            return TaskActionType.subclass(*args_, **kwargs_)
        else:
            return TaskActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Type(self): return self.Action_Type
    def set_Action_Type(self, Action_Type): self.Action_Type = Action_Type
    def validate_TaskActionTypeType(self, value):
        # Validate type TaskActionTypeType, a restriction on None.
        pass
    def get_Action_ID(self): return self.Action_ID
    def set_Action_ID(self, Action_ID): self.Action_ID = Action_ID
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_IEmailAction(self): return self.IEmailAction
    def set_IEmailAction(self, IEmailAction): self.IEmailAction = IEmailAction
    def get_IComHandlerAction(self): return self.IComHandlerAction
    def set_IComHandlerAction(self, IComHandlerAction): self.IComHandlerAction = IComHandlerAction
    def get_IExecAction(self): return self.IExecAction
    def set_IExecAction(self, IExecAction): self.IExecAction = IExecAction
    def get_IShowMessageAction(self): return self.IShowMessageAction
    def set_IShowMessageAction(self, IShowMessageAction): self.IShowMessageAction = IShowMessageAction
    def hasContent_(self):
        if (
            self.Action_Type is not None or
            self.Action_ID is not None or
            self.IEmailAction is not None or
            self.IComHandlerAction is not None or
            self.IExecAction is not None or
            self.IShowMessageAction is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskActionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Action_Type is not None:
            self.Action_Type.export(lwrite, level, 'WinTaskObj:', name_='Action_Type', pretty_print=pretty_print)
        if self.Action_ID is not None:
            self.Action_ID.export(lwrite, level, 'WinTaskObj:', name_='Action_ID', pretty_print=pretty_print)
        if self.IEmailAction is not None:
            self.IEmailAction.export(lwrite, level, 'WinTaskObj:', name_='IEmailAction', pretty_print=pretty_print)
        if self.IComHandlerAction is not None:
            self.IComHandlerAction.export(lwrite, level, 'WinTaskObj:', name_='IComHandlerAction', pretty_print=pretty_print)
        if self.IExecAction is not None:
            self.IExecAction.export(lwrite, level, 'WinTaskObj:', name_='IExecAction', pretty_print=pretty_print)
        if self.IShowMessageAction is not None:
            self.IShowMessageAction.export(lwrite, level, 'WinTaskObj:', name_='IShowMessageAction', pretty_print=pretty_print)
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
        if nodeName_ == 'Action_Type':
            obj_ = TaskActionTypeType.factory()
            obj_.build(child_)
            self.set_Action_Type(obj_)
        elif nodeName_ == 'Action_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Action_ID(obj_)
        elif nodeName_ == 'IEmailAction':
            obj_ = email_message_object.EmailMessageObjectType.factory()
            obj_.build(child_)
            self.set_IEmailAction(obj_)
        elif nodeName_ == 'IComHandlerAction':
            obj_ = IComHandlerActionType.factory()
            obj_.build(child_)
            self.set_IComHandlerAction(obj_)
        elif nodeName_ == 'IExecAction':
            obj_ = IExecActionType.factory()
            obj_.build(child_)
            self.set_IExecAction(obj_)
        elif nodeName_ == 'IShowMessageAction':
            obj_ = IShowMessageActionType.factory()
            obj_.build(child_)
            self.set_IShowMessageAction(obj_)
# end class TaskActionType

class IComHandlerActionType(GeneratedsSuper):
    """The IComHandlerActionType type characterizes IComHandler actions."""

    subclass = None
    superclass = None
    def __init__(self, COM_Data=None, COM_Class_ID=None):
        self.COM_Data = COM_Data
        self.COM_Class_ID = COM_Class_ID
    def factory(*args_, **kwargs_):
        if IComHandlerActionType.subclass:
            return IComHandlerActionType.subclass(*args_, **kwargs_)
        else:
            return IComHandlerActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_COM_Data(self): return self.COM_Data
    def set_COM_Data(self, COM_Data): self.COM_Data = COM_Data
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_COM_Class_ID(self): return self.COM_Class_ID
    def set_COM_Class_ID(self, COM_Class_ID): self.COM_Class_ID = COM_Class_ID
    def hasContent_(self):
        if (
            self.COM_Data is not None or
            self.COM_Class_ID is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='IComHandlerActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IComHandlerActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='IComHandlerActionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='IComHandlerActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.COM_Data is not None:
            self.COM_Data.export(lwrite, level, 'WinTaskObj:', name_='COM_Data', pretty_print=pretty_print)
        if self.COM_Class_ID is not None:
            self.COM_Class_ID.export(lwrite, level, 'WinTaskObj:', name_='COM_Class_ID', pretty_print=pretty_print)
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
        if nodeName_ == 'COM_Data':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_COM_Data(obj_)
        elif nodeName_ == 'COM_Class_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_COM_Class_ID(obj_)
# end class IComHandlerActionType

class IExecActionType(GeneratedsSuper):
    """The IExecActionType type characterizes IExec actions."""

    subclass = None
    superclass = None
    def __init__(self, Exec_Arguments=None, Exec_Program_Path=None, Exec_Working_Directory=None, Exec_Program_Hashes=None):
        self.Exec_Arguments = Exec_Arguments
        self.Exec_Program_Path = Exec_Program_Path
        self.Exec_Working_Directory = Exec_Working_Directory
        self.Exec_Program_Hashes = Exec_Program_Hashes
    def factory(*args_, **kwargs_):
        if IExecActionType.subclass:
            return IExecActionType.subclass(*args_, **kwargs_)
        else:
            return IExecActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Exec_Arguments(self): return self.Exec_Arguments
    def set_Exec_Arguments(self, Exec_Arguments): self.Exec_Arguments = Exec_Arguments
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Exec_Program_Path(self): return self.Exec_Program_Path
    def set_Exec_Program_Path(self, Exec_Program_Path): self.Exec_Program_Path = Exec_Program_Path
    def get_Exec_Working_Directory(self): return self.Exec_Working_Directory
    def set_Exec_Working_Directory(self, Exec_Working_Directory): self.Exec_Working_Directory = Exec_Working_Directory
    def get_Exec_Program_Hashes(self): return self.Exec_Program_Hashes
    def set_Exec_Program_Hashes(self, Exec_Program_Hashes): self.Exec_Program_Hashes = Exec_Program_Hashes
    def hasContent_(self):
        if (
            self.Exec_Arguments is not None or
            self.Exec_Program_Path is not None or
            self.Exec_Working_Directory is not None or
            self.Exec_Program_Hashes is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='IExecActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IExecActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='IExecActionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='IExecActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Exec_Arguments is not None:
            self.Exec_Arguments.export(lwrite, level, 'WinTaskObj:', name_='Exec_Arguments', pretty_print=pretty_print)
        if self.Exec_Program_Path is not None:
            self.Exec_Program_Path.export(lwrite, level, 'WinTaskObj:', name_='Exec_Program_Path', pretty_print=pretty_print)
        if self.Exec_Working_Directory is not None:
            self.Exec_Working_Directory.export(lwrite, level, 'WinTaskObj:', name_='Exec_Working_Directory', pretty_print=pretty_print)
        if self.Exec_Program_Hashes is not None:
            self.Exec_Program_Hashes.export(lwrite, level, 'WinTaskObj:', name_='Exec_Program_Hashes', pretty_print=pretty_print)
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
        if nodeName_ == 'Exec_Arguments':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exec_Arguments(obj_)
        elif nodeName_ == 'Exec_Program_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exec_Program_Path(obj_)
        elif nodeName_ == 'Exec_Working_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exec_Working_Directory(obj_)
        elif nodeName_ == 'Exec_Program_Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Exec_Program_Hashes(obj_)
# end class IExecActionType

class IShowMessageActionType(GeneratedsSuper):
    """The IShowMessageActionType type characterizes IShowMessage actions."""

    subclass = None
    superclass = None
    def __init__(self, Show_Message_Body=None, Show_Message_Title=None):
        self.Show_Message_Body = Show_Message_Body
        self.Show_Message_Title = Show_Message_Title
    def factory(*args_, **kwargs_):
        if IShowMessageActionType.subclass:
            return IShowMessageActionType.subclass(*args_, **kwargs_)
        else:
            return IShowMessageActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Show_Message_Body(self): return self.Show_Message_Body
    def set_Show_Message_Body(self, Show_Message_Body): self.Show_Message_Body = Show_Message_Body
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Show_Message_Title(self): return self.Show_Message_Title
    def set_Show_Message_Title(self, Show_Message_Title): self.Show_Message_Title = Show_Message_Title
    def hasContent_(self):
        if (
            self.Show_Message_Body is not None or
            self.Show_Message_Title is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='IShowMessageActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IShowMessageActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='IShowMessageActionType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='IShowMessageActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Show_Message_Body is not None:
            self.Show_Message_Body.export(lwrite, level, 'WinTaskObj:', name_='Show_Message_Body', pretty_print=pretty_print)
        if self.Show_Message_Title is not None:
            self.Show_Message_Title.export(lwrite, level, 'WinTaskObj:', name_='Show_Message_Title', pretty_print=pretty_print)
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
        if nodeName_ == 'Show_Message_Body':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Show_Message_Body(obj_)
        elif nodeName_ == 'Show_Message_Title':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Show_Message_Title(obj_)
# end class IShowMessageActionType

class TaskStatusType(cybox_common.BaseObjectPropertyType):
    """The TaskStatusType type specifies Windows Task states via a union of
    the TaskStatusEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskStatusType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskStatusType.subclass:
            return TaskStatusType.subclass(*args_, **kwargs_)
        else:
            return TaskStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskStatusType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskStatusType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskStatusType'):
        super(TaskStatusType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskStatusType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskStatusType', fromsubclass_=False, pretty_print=True):
        super(TaskStatusType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskStatusType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskStatusType

class TaskTriggerType(cybox_common.BaseObjectPropertyType):
    """The TaskTriggerType type specifies Windows Task trigger types via a
    union of the TriggerTypeEnum enumeration and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskTriggerType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskTriggerType.subclass:
            return TaskTriggerType.subclass(*args_, **kwargs_)
        else:
            return TaskTriggerType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskTriggerType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskTriggerType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskTriggerType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskTriggerType'):
        super(TaskTriggerType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskTriggerType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskTriggerType', fromsubclass_=False, pretty_print=True):
        super(TaskTriggerType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskTriggerType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskTriggerType

class TaskTriggerFrequencyType(cybox_common.BaseObjectPropertyType):
    """The TaskTriggerFrequencyType type specifies Windows Task trigger
    frequency types via a union of the TriggerFrequencyEnum type and
    the atomic xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskTriggerFrequencyType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskTriggerFrequencyType.subclass:
            return TaskTriggerFrequencyType.subclass(*args_, **kwargs_)
        else:
            return TaskTriggerFrequencyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskTriggerFrequencyType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskTriggerFrequencyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskTriggerFrequencyType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskTriggerFrequencyType'):
        super(TaskTriggerFrequencyType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskTriggerFrequencyType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskTriggerFrequencyType', fromsubclass_=False, pretty_print=True):
        super(TaskTriggerFrequencyType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskTriggerFrequencyType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskTriggerFrequencyType

class TaskPriorityType(cybox_common.BaseObjectPropertyType):
    """The TaskPriorityType type specifies Windows Task priority types via
    a union of the TaskPriorityEnum type and the atomic xs:string
    type. Its base type is the CybOX Core cybox_common.BaseObjectPropertyType,
    for permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskPriorityType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskPriorityType.subclass:
            return TaskPriorityType.subclass(*args_, **kwargs_)
        else:
            return TaskPriorityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskPriorityType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskPriorityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskPriorityType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskPriorityType'):
        super(TaskPriorityType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskPriorityType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskPriorityType', fromsubclass_=False, pretty_print=True):
        super(TaskPriorityType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskPriorityType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskPriorityType

class TaskFlagType(cybox_common.BaseObjectPropertyType):
    """The TaskFlagType type specifies Windows Task flag types via a union
    of the TaskFlagEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications.This
    attribute is optional and specifies the expected type for the
    value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskFlagType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskFlagType.subclass:
            return TaskFlagType.subclass(*args_, **kwargs_)
        else:
            return TaskFlagType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskFlagType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskFlagType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskFlagType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskFlagType'):
        super(TaskFlagType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskFlagType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskFlagType', fromsubclass_=False, pretty_print=True):
        super(TaskFlagType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskFlagType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskFlagType

class TaskActionTypeType(cybox_common.BaseObjectPropertyType):
    """The TaskActionTypeType characterizes the specific types of task
    actions.This attribute is optional and specifies the expected
    type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(TaskActionTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if TaskActionTypeType.subclass:
            return TaskActionTypeType.subclass(*args_, **kwargs_)
        else:
            return TaskActionTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(TaskActionTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskActionTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='TaskActionTypeType'):
        super(TaskActionTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TaskActionTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='TaskActionTypeType', fromsubclass_=False, pretty_print=True):
        super(TaskActionTypeType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None:

            self.datatype = value
        super(TaskActionTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TaskActionTypeType

class WindowsTaskObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsTaskObjectType type is intended to characterize Windows
    task scheduler tasks. See Also: http://msdn.microsoft.com/en-
    us/library/windows/desktop/aa381311(v=vs.85).aspx"""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Status=None, Priority=None, Name=None, Application_Name=None, Parameters=None, Flags=None, Account_Name=None, Account_Run_Level=None, Account_Logon_Type=None, Creator=None, Creation_Date=None, Most_Recent_Run_Time=None, Exit_Code=None, Max_Run_Time=None, Next_Run_Time=None, Action_List=None, Trigger_List=None, Comment=None, Working_Directory=None, Work_Item_Data=None):
        super(WindowsTaskObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Status = Status
        self.Priority = Priority
        self.Name = Name
        self.Application_Name = Application_Name
        self.Parameters = Parameters
        self.Flags = Flags
        self.Account_Name = Account_Name
        self.Account_Run_Level = Account_Run_Level
        self.Account_Logon_Type = Account_Logon_Type
        self.Creator = Creator
        self.Creation_Date = Creation_Date
        self.Most_Recent_Run_Time = Most_Recent_Run_Time
        self.Exit_Code = Exit_Code
        self.Max_Run_Time = Max_Run_Time
        self.Next_Run_Time = Next_Run_Time
        self.Action_List = Action_List
        self.Trigger_List = Trigger_List
        self.Comment = Comment
        self.Working_Directory = Working_Directory
        self.Work_Item_Data = Work_Item_Data
    def factory(*args_, **kwargs_):
        if WindowsTaskObjectType.subclass:
            return WindowsTaskObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsTaskObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def validate_TaskStatusType(self, value):
        # Validate type TaskStatusType, a restriction on None.
        pass
    def get_Priority(self): return self.Priority
    def set_Priority(self, Priority): self.Priority = Priority
    def validate_TaskPriorityType(self, value):
        # Validate type TaskPriorityType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Application_Name(self): return self.Application_Name
    def set_Application_Name(self, Application_Name): self.Application_Name = Application_Name
    def get_Parameters(self): return self.Parameters
    def set_Parameters(self, Parameters): self.Parameters = Parameters
    def get_Flags(self): return self.Flags
    def set_Flags(self, Flags): self.Flags = Flags
    def validate_TaskFlagType(self, value):
        # Validate type TaskFlagType, a restriction on None.
        pass
    def get_Account_Name(self): return self.Account_Name
    def set_Account_Name(self, Account_Name): self.Account_Name = Account_Name
    def get_Account_Run_Level(self): return self.Account_Run_Level
    def set_Account_Run_Level(self, Account_Run_Level): self.Account_Run_Level = Account_Run_Level
    def get_Account_Logon_Type(self): return self.Account_Logon_Type
    def set_Account_Logon_Type(self, Account_Logon_Type): self.Account_Logon_Type = Account_Logon_Type
    def get_Creator(self): return self.Creator
    def set_Creator(self, Creator): self.Creator = Creator
    def get_Creation_Date(self): return self.Creation_Date
    def set_Creation_Date(self, Creation_Date): self.Creation_Date = Creation_Date
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Most_Recent_Run_Time(self): return self.Most_Recent_Run_Time
    def set_Most_Recent_Run_Time(self, Most_Recent_Run_Time): self.Most_Recent_Run_Time = Most_Recent_Run_Time
    def get_Exit_Code(self): return self.Exit_Code
    def set_Exit_Code(self, Exit_Code): self.Exit_Code = Exit_Code
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_Max_Run_Time(self): return self.Max_Run_Time
    def set_Max_Run_Time(self, Max_Run_Time): self.Max_Run_Time = Max_Run_Time
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Next_Run_Time(self): return self.Next_Run_Time
    def set_Next_Run_Time(self, Next_Run_Time): self.Next_Run_Time = Next_Run_Time
    def get_Action_List(self): return self.Action_List
    def set_Action_List(self, Action_List): self.Action_List = Action_List
    def get_Trigger_List(self): return self.Trigger_List
    def set_Trigger_List(self, Trigger_List): self.Trigger_List = Trigger_List
    def get_Comment(self): return self.Comment
    def set_Comment(self, Comment): self.Comment = Comment
    def get_Working_Directory(self): return self.Working_Directory
    def set_Working_Directory(self, Working_Directory): self.Working_Directory = Working_Directory
    def get_Work_Item_Data(self): return self.Work_Item_Data
    def set_Work_Item_Data(self, Work_Item_Data): self.Work_Item_Data = Work_Item_Data
    def validate_Base64BinaryObjectPropertyType(self, value):
        # Validate type cybox_common.Base64BinaryObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Status is not None or
            self.Priority is not None or
            self.Name is not None or
            self.Application_Name is not None or
            self.Parameters is not None or
            self.Flags is not None or
            self.Account_Name is not None or
            self.Account_Run_Level is not None or
            self.Account_Logon_Type is not None or
            self.Creator is not None or
            self.Creation_Date is not None or
            self.Most_Recent_Run_Time is not None or
            self.Exit_Code is not None or
            self.Max_Run_Time is not None or
            self.Next_Run_Time is not None or
            self.Action_List is not None or
            self.Trigger_List is not None or
            self.Comment is not None or
            self.Working_Directory is not None or
            self.Work_Item_Data is not None or
            super(WindowsTaskObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinTaskObj:', name_='WindowsTaskObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsTaskObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinTaskObj:', name_='WindowsTaskObjectType'):
        super(WindowsTaskObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsTaskObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinTaskObj:', name_='WindowsTaskObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsTaskObjectType, self).exportChildren(lwrite, level, 'WinTaskObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Status is not None:
            self.Status.export(lwrite, level, 'WinTaskObj:', name_='Status', pretty_print=pretty_print)
        if self.Priority is not None:
            self.Priority.export(lwrite, level, 'WinTaskObj:', name_='Priority', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinTaskObj:', name_='Name', pretty_print=pretty_print)
        if self.Application_Name is not None:
            self.Application_Name.export(lwrite, level, 'WinTaskObj:', name_='Application_Name', pretty_print=pretty_print)
        if self.Parameters is not None:
            self.Parameters.export(lwrite, level, 'WinTaskObj:', name_='Parameters', pretty_print=pretty_print)
        if self.Flags is not None:
            self.Flags.export(lwrite, level, 'WinTaskObj:', name_='Flags', pretty_print=pretty_print)
        if self.Account_Name is not None:
            self.Account_Name.export(lwrite, level, 'WinTaskObj:', name_='Account_Name', pretty_print=pretty_print)
        if self.Account_Run_Level is not None:
            self.Account_Run_Level.export(lwrite, level, 'WinTaskObj:', name_='Account_Run_Level', pretty_print=pretty_print)
        if self.Account_Logon_Type is not None:
            self.Account_Logon_Type.export(lwrite, level, 'WinTaskObj:', name_='Account_Logon_Type', pretty_print=pretty_print)
        if self.Creator is not None:
            self.Creator.export(lwrite, level, 'WinTaskObj:', name_='Creator', pretty_print=pretty_print)
        if self.Creation_Date is not None:
            self.Creation_Date.export(lwrite, level, 'WinTaskObj:', name_='Creation_Date', pretty_print=pretty_print)
        if self.Most_Recent_Run_Time is not None:
            self.Most_Recent_Run_Time.export(lwrite, level, 'WinTaskObj:', name_='Most_Recent_Run_Time', pretty_print=pretty_print)
        if self.Exit_Code is not None:
            self.Exit_Code.export(lwrite, level, 'WinTaskObj:', name_='Exit_Code', pretty_print=pretty_print)
        if self.Max_Run_Time is not None:
            self.Max_Run_Time.export(lwrite, level, 'WinTaskObj:', name_='Max_Run_Time', pretty_print=pretty_print)
        if self.Next_Run_Time is not None:
            self.Next_Run_Time.export(lwrite, level, 'WinTaskObj:', name_='Next_Run_Time', pretty_print=pretty_print)
        if self.Action_List is not None:
            self.Action_List.export(lwrite, level, 'WinTaskObj:', name_='Action_List', pretty_print=pretty_print)
        if self.Trigger_List is not None:
            self.Trigger_List.export(lwrite, level, 'WinTaskObj:', name_='Trigger_List', pretty_print=pretty_print)
        if self.Comment is not None:
            self.Comment.export(lwrite, level, 'WinTaskObj:', name_='Comment', pretty_print=pretty_print)
        if self.Working_Directory is not None:
            self.Working_Directory.export(lwrite, level, 'WinTaskObj:', name_='Working_Directory', pretty_print=pretty_print)
        if self.Work_Item_Data is not None:
            self.Work_Item_Data.export(lwrite, level, 'WinTaskObj:', name_='Work_Item_Data', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsTaskObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Status':
            obj_ = TaskStatusType.factory()
            obj_.build(child_)
            self.set_Status(obj_)
        elif nodeName_ == 'Priority':
            obj_ = TaskPriorityType.factory()
            obj_.build(child_)
            self.set_Priority(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Application_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Application_Name(obj_)
        elif nodeName_ == 'Parameters':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Parameters(obj_)
        elif nodeName_ == 'Flags':
            obj_ = TaskFlagType.factory()
            obj_.build(child_)
            self.set_Flags(obj_)
        elif nodeName_ == 'Account_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Account_Name(obj_)
        elif nodeName_ == 'Account_Run_Level':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Account_Run_Level(obj_)
        elif nodeName_ == 'Account_Logon_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Account_Logon_Type(obj_)
        elif nodeName_ == 'Creator':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creator(obj_)
        elif nodeName_ == 'Creation_Date':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Date(obj_)
        elif nodeName_ == 'Most_Recent_Run_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Most_Recent_Run_Time(obj_)
        elif nodeName_ == 'Exit_Code':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Exit_Code(obj_)
        elif nodeName_ == 'Max_Run_Time':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Max_Run_Time(obj_)
        elif nodeName_ == 'Next_Run_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Next_Run_Time(obj_)
        elif nodeName_ == 'Action_List':
            obj_ = TaskActionListType.factory()
            obj_.build(child_)
            self.set_Action_List(obj_)
        elif nodeName_ == 'Trigger_List':
            obj_ = TriggerListType.factory()
            obj_.build(child_)
            self.set_Trigger_List(obj_)
        elif nodeName_ == 'Comment':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Comment(obj_)
        elif nodeName_ == 'Working_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Working_Directory(obj_)
        elif nodeName_ == 'Work_Item_Data':
            obj_ = cybox_common.Base64BinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Work_Item_Data(obj_)
        super(WindowsTaskObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsTaskObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Next_Run_Time': cybox_common.DateTimeObjectPropertyType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Working_Directory': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'COM_Data': cybox_common.StringObjectPropertyType,
    'Exit_Code': cybox_common.LongObjectPropertyType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Application_Name': cybox_common.StringObjectPropertyType,
    'By': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Trigger_Delay': cybox_common.DurationObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Account_Run_Level': cybox_common.StringObjectPropertyType,
    'Attachments': email_message_object.AttachmentsType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Most_Recent_Run_Time': cybox_common.DateTimeObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Creator': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Trigger_Begin': cybox_common.DateTimeObjectPropertyType,
    'Subject': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'From': cybox_common.StringObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Parameters': cybox_common.StringObjectPropertyType,
    'Trigger_Max_Run_Time': cybox_common.DurationObjectPropertyType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'MIME_Version': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Message_ID': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Raw_Body': cybox_common.StringObjectPropertyType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Link': email_message_object.LinkReferenceType,
    'Tool_Hashes': cybox_common.HashListType,
    'X_Priority': cybox_common.PositiveIntegerObjectPropertyType,
    'COM_Class_ID': cybox_common.StringObjectPropertyType,
    'Exec_Arguments': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Trigger_End': cybox_common.DateTimeObjectPropertyType,
    'Show_Message_Body': cybox_common.StringObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Comment': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'X_Mailer': cybox_common.StringObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Received': email_message_object.EmailReceivedLineType,
    'Timestamp': cybox_common.DateTimeObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'In_Reply_To': cybox_common.StringObjectPropertyType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'BCC': email_message_object.EmailRecipientsType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Boundary': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'For': cybox_common.StringObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Exec_Working_Directory': cybox_common.StringObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'Received_Lines': email_message_object.EmailReceivedLineListType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'CC': email_message_object.EmailRecipientsType,
    'Errors_To': cybox_common.StringObjectPropertyType,
    'Creation_Date': cybox_common.DateTimeObjectPropertyType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'ID': cybox_common.StringObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Trigger_Session_Change_Type': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Precedence': cybox_common.StringObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'Header': email_message_object.EmailHeaderType,
    'References': cybox_common.ToolReferencesType,
    'IEmailAction': email_message_object.EmailMessageObjectType,
    'Exec_Program_Hashes': cybox_common.HashListType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Max_Run_Time': cybox_common.UnsignedLongObjectPropertyType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'To': email_message_object.EmailRecipientsType,
    'Email_Server': cybox_common.StringObjectPropertyType,
    'Action_ID': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'With': cybox_common.StringObjectPropertyType,
    'Links': email_message_object.LinksType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Work_Item_Data': cybox_common.Base64BinaryObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Account_Name': cybox_common.StringObjectPropertyType,
    'Account_Logon_Type': cybox_common.StringObjectPropertyType,
    'Exec_Program_Path': cybox_common.StringObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Show_Message_Title': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Email_Message': email_message_object.EmailMessageObjectType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'File': email_message_object.AttachmentReferenceType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
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
        rootTag = 'Windows_Task'
        rootClass = WindowsTaskObjectType
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
        rootTag = 'Windows_Task'
        rootClass = WindowsTaskObjectType
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
        rootTag = 'Windows_Task'
        rootClass = WindowsTaskObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Task",
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
    "WindowsTaskObjectType",
    "TriggerListType",
    "TriggerType",
    "TaskActionListType",
    "TaskActionType",
    "TaskActionTypeType",
    "IComHandlerActionType",
    "IExecActionType",
    "IShowMessageActionType",
    "TaskFlagType",
    "TaskPriorityType",
    "TaskTriggerFrequencyType",
    "TaskTriggerType",
    "TaskStatusType"
    ]
