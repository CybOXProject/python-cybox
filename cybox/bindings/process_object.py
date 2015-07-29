# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import network_connection_object
from . import port_object


class NetworkConnectionListType(GeneratedsSuper):
    """The NetworkConnectionListType type is a list of network connections."""

    subclass = None
    superclass = None
    def __init__(self, Network_Connection=None):
        if Network_Connection is None:
            self.Network_Connection = []
        else:
            self.Network_Connection = Network_Connection
    def factory(*args_, **kwargs_):
        if NetworkConnectionListType.subclass:
            return NetworkConnectionListType.subclass(*args_, **kwargs_)
        else:
            return NetworkConnectionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Network_Connection(self): return self.Network_Connection
    def set_Network_Connection(self, Network_Connection): self.Network_Connection = Network_Connection
    def add_Network_Connection(self, value): self.Network_Connection.append(value)
    def insert_Network_Connection(self, index, value): self.Network_Connection[index] = value
    def hasContent_(self):
        if (
            self.Network_Connection
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='NetworkConnectionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NetworkConnectionListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='NetworkConnectionListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='NetworkConnectionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Network_Connection_ in self.Network_Connection:
            Network_Connection_.export(lwrite, level, 'ProcessObj:', name_='Network_Connection', pretty_print=pretty_print)
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
        if nodeName_ == 'Network_Connection':
            obj_ = network_connection_object.NetworkConnectionObjectType.factory()
            obj_.build(child_)
            self.Network_Connection.append(obj_)
# end class NetworkConnectionListType

class ImageInfoType(GeneratedsSuper):
    """The ImageInfoType type captures information about the process image."""

    subclass = None
    superclass = None
    def __init__(self, File_Name=None, Command_Line=None, Current_Directory=None, Path=None):
        self.File_Name = File_Name
        self.Command_Line = Command_Line
        self.Current_Directory = Current_Directory
        self.Path = Path
    def factory(*args_, **kwargs_):
        if ImageInfoType.subclass:
            return ImageInfoType.subclass(*args_, **kwargs_)
        else:
            return ImageInfoType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File_Name(self): return self.File_Name
    def set_File_Name(self, File_Name): self.File_Name = File_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Command_Line(self): return self.Command_Line
    def set_Command_Line(self, Command_Line): self.Command_Line = Command_Line
    def get_Current_Directory(self): return self.Current_Directory
    def set_Current_Directory(self, Current_Directory): self.Current_Directory = Current_Directory
    def get_Path(self): return self.Path
    def set_Path(self, Path): self.Path = Path
    def hasContent_(self):
        if (
            self.File_Name is not None or
            self.Command_Line is not None or
            self.Current_Directory is not None or
            self.Path is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='ImageInfoType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ImageInfoType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='ImageInfoType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='ImageInfoType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.File_Name is not None:
            self.File_Name.export(lwrite, level, 'ProcessObj:', name_='File_Name', pretty_print=pretty_print)
        if self.Command_Line is not None:
            self.Command_Line.export(lwrite, level, 'ProcessObj:', name_='Command_Line', pretty_print=pretty_print)
        if self.Current_Directory is not None:
            self.Current_Directory.export(lwrite, level, 'ProcessObj:', name_='Current_Directory', pretty_print=pretty_print)
        if self.Path is not None:
            self.Path.export(lwrite, level, 'ProcessObj:', name_='Path', pretty_print=pretty_print)
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
        if nodeName_ == 'File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_Name(obj_)
        elif nodeName_ == 'Command_Line':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Command_Line(obj_)
        elif nodeName_ == 'Current_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Current_Directory(obj_)
        elif nodeName_ == 'Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Path(obj_)
# end class ImageInfoType

class ProcessStatusType(GeneratedsSuper):
    """The ProcessStatusType is used for specifying the status of a running
    or terminated process. Since this property is platform-specific,
    it is created here as an abstract type and then used in the
    platform-specific process CybOX objects."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if ProcessStatusType.subclass:
            return ProcessStatusType.subclass(*args_, **kwargs_)
        else:
            return ProcessStatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='ProcessStatusType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessStatusType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='ProcessStatusType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='ProcessStatusType', fromsubclass_=False, pretty_print=True):
        pass
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
        pass
# end class ProcessStatusType

class ChildPIDListType(GeneratedsSuper):
    """The ChildPIDListType type captures the PID's of the children of the
    process in a list format."""

    subclass = None
    superclass = None
    def __init__(self, Child_PID=None):
        if Child_PID is None:
            self.Child_PID = []
        else:
            self.Child_PID = Child_PID
    def factory(*args_, **kwargs_):
        if ChildPIDListType.subclass:
            return ChildPIDListType.subclass(*args_, **kwargs_)
        else:
            return ChildPIDListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Child_PID(self): return self.Child_PID
    def set_Child_PID(self, Child_PID): self.Child_PID = Child_PID
    def add_Child_PID(self, value): self.Child_PID.append(value)
    def insert_Child_PID(self, index, value): self.Child_PID[index] = value
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Child_PID
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='ChildPIDListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ChildPIDListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='ChildPIDListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='ChildPIDListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Child_PID_ in self.Child_PID:
            Child_PID_.export(lwrite, level, 'ProcessObj:', name_='Child_PID', pretty_print=pretty_print)
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
        if nodeName_ == 'Child_PID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.Child_PID.append(obj_)
# end class ChildPIDListType

class ArgumentListType(GeneratedsSuper):
    """The ArgumentListType is intended to specify a list of arguments
    utlized in intiating the process."""

    subclass = None
    superclass = None
    def __init__(self, Argument=None):
        if Argument is None:
            self.Argument = []
        else:
            self.Argument = Argument
    def factory(*args_, **kwargs_):
        if ArgumentListType.subclass:
            return ArgumentListType.subclass(*args_, **kwargs_)
        else:
            return ArgumentListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Argument(self): return self.Argument
    def set_Argument(self, Argument): self.Argument = Argument
    def add_Argument(self, value): self.Argument.append(value)
    def insert_Argument(self, index, value): self.Argument[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Argument
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='ArgumentListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ArgumentListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='ArgumentListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='ArgumentListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Argument_ in self.Argument:
            Argument_.export(lwrite, level, 'ProcessObj:', name_='Argument', pretty_print=pretty_print)
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
        if nodeName_ == 'Argument':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Argument.append(obj_)
# end class ArgumentListType

class PortListType(GeneratedsSuper):
    """The PortListType is intended to specify a list of network ports."""

    subclass = None
    superclass = None
    def __init__(self, Port=None):
        if Port is None:
            self.Port = []
        else:
            self.Port = Port
    def factory(*args_, **kwargs_):
        if PortListType.subclass:
            return PortListType.subclass(*args_, **kwargs_)
        else:
            return PortListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Port(self): return self.Port
    def set_Port(self, Port): self.Port = Port
    def add_Port(self, value): self.Port.append(value)
    def insert_Port(self, index, value): self.Port[index] = value
    def hasContent_(self):
        if (
            self.Port
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='PortListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PortListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='PortListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='PortListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Port_ in self.Port:
            Port_.export(lwrite, level, 'ProcessObj:', name_='Port', pretty_print=pretty_print)
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
        if nodeName_ == 'Port':
            obj_ = port_object.PortObjectType.factory()
            obj_.build(child_)
            self.Port.append(obj_)
# end class PortListType

class ProcessObjectType(cybox_common.ObjectPropertiesType):
    """The ProcessObjectType type is intended to characterize system
    processes.The is_hidden field specifies whether the process is
    hidden or not."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_hidden=None, PID=None, Name=None, Creation_Time=None, Parent_PID=None, Child_PID_List=None, Image_Info=None, Argument_List=None, Environment_Variable_List=None, Kernel_Time=None, Port_List=None, Network_Connection_List=None, Start_Time=None, Status=None, Username=None, User_Time=None, Extracted_Features=None):
        super(ProcessObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_hidden = _cast(bool, is_hidden)
        self.PID = PID
        self.Name = Name
        self.Creation_Time = Creation_Time
        self.Parent_PID = Parent_PID
        self.Child_PID_List = Child_PID_List
        self.Image_Info = Image_Info
        self.Argument_List = Argument_List
        self.Environment_Variable_List = Environment_Variable_List
        self.Kernel_Time = Kernel_Time
        self.Port_List = Port_List
        self.Network_Connection_List = Network_Connection_List
        self.Start_Time = Start_Time
        self.Status = Status
        self.Username = Username
        self.User_Time = User_Time
        self.Extracted_Features = Extracted_Features
    def factory(*args_, **kwargs_):
        if ProcessObjectType.subclass:
            return ProcessObjectType.subclass(*args_, **kwargs_)
        else:
            return ProcessObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PID(self): return self.PID
    def set_PID(self, PID): self.PID = PID
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Creation_Time(self): return self.Creation_Time
    def set_Creation_Time(self, Creation_Time): self.Creation_Time = Creation_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Parent_PID(self): return self.Parent_PID
    def set_Parent_PID(self, Parent_PID): self.Parent_PID = Parent_PID
    def get_Child_PID_List(self): return self.Child_PID_List
    def set_Child_PID_List(self, Child_PID_List): self.Child_PID_List = Child_PID_List
    def get_Image_Info(self): return self.Image_Info
    def set_Image_Info(self, Image_Info): self.Image_Info = Image_Info
    def get_Argument_List(self): return self.Argument_List
    def set_Argument_List(self, Argument_List): self.Argument_List = Argument_List
    def get_Environment_Variable_List(self): return self.Environment_Variable_List
    def set_Environment_Variable_List(self, Environment_Variable_List): self.Environment_Variable_List = Environment_Variable_List
    def get_Kernel_Time(self): return self.Kernel_Time
    def set_Kernel_Time(self, Kernel_Time): self.Kernel_Time = Kernel_Time
    def validate_DurationObjectPropertyType(self, value):
        # Validate type cybox_common.DurationObjectPropertyType, a restriction on None.
        pass
    def get_Port_List(self): return self.Port_List
    def set_Port_List(self, Port_List): self.Port_List = Port_List
    def get_Network_Connection_List(self): return self.Network_Connection_List
    def set_Network_Connection_List(self, Network_Connection_List): self.Network_Connection_List = Network_Connection_List
    def get_Start_Time(self): return self.Start_Time
    def set_Start_Time(self, Start_Time): self.Start_Time = Start_Time
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def get_Username(self): return self.Username
    def set_Username(self, Username): self.Username = Username
    def get_User_Time(self): return self.User_Time
    def set_User_Time(self, User_Time): self.User_Time = User_Time
    def get_Extracted_Features(self): return self.Extracted_Features
    def set_Extracted_Features(self, Extracted_Features): self.Extracted_Features = Extracted_Features
    def get_is_hidden(self): return self.is_hidden
    def set_is_hidden(self, is_hidden): self.is_hidden = is_hidden
    def hasContent_(self):
        if (
            self.PID is not None or
            self.Name is not None or
            self.Creation_Time is not None or
            self.Parent_PID is not None or
            self.Child_PID_List is not None or
            self.Image_Info is not None or
            self.Argument_List is not None or
            self.Environment_Variable_List is not None or
            self.Kernel_Time is not None or
            self.Port_List is not None or
            self.Network_Connection_List is not None or
            self.Start_Time is not None or
            self.Status is not None or
            self.Username is not None or
            self.User_Time is not None or
            self.Extracted_Features is not None or
            super(ProcessObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ProcessObj:', name_='ProcessObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ProcessObj:', name_='ProcessObjectType'):
        super(ProcessObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ProcessObjectType')
        if self.is_hidden is not None:

            lwrite(' is_hidden="%s"' % self.gds_format_boolean(self.is_hidden, input_name='is_hidden'))
    def exportChildren(self, lwrite, level, namespace_='ProcessObj:', name_='ProcessObjectType', fromsubclass_=False, pretty_print=True):
        super(ProcessObjectType, self).exportChildren(lwrite, level, 'ProcessObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PID is not None:
            self.PID.export(lwrite, level, 'ProcessObj:', name_='PID', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'ProcessObj:', name_='Name', pretty_print=pretty_print)
        if self.Creation_Time is not None:
            self.Creation_Time.export(lwrite, level, 'ProcessObj:', name_='Creation_Time', pretty_print=pretty_print)
        if self.Parent_PID is not None:
            self.Parent_PID.export(lwrite, level, 'ProcessObj:', name_='Parent_PID', pretty_print=pretty_print)
        if self.Child_PID_List is not None:
            self.Child_PID_List.export(lwrite, level, 'ProcessObj:', name_='Child_PID_List', pretty_print=pretty_print)
        if self.Image_Info is not None:
            self.Image_Info.export(lwrite, level, 'ProcessObj:', name_='Image_Info', pretty_print=pretty_print)
        if self.Argument_List is not None:
            self.Argument_List.export(lwrite, level, 'ProcessObj:', name_='Argument_List', pretty_print=pretty_print)
        if self.Environment_Variable_List is not None:
            self.Environment_Variable_List.export(lwrite, level, 'ProcessObj:', name_='Environment_Variable_List', pretty_print=pretty_print)
        if self.Kernel_Time is not None:
            self.Kernel_Time.export(lwrite, level, 'ProcessObj:', name_='Kernel_Time', pretty_print=pretty_print)
        if self.Port_List is not None:
            self.Port_List.export(lwrite, level, 'ProcessObj:', name_='Port_List', pretty_print=pretty_print)
        if self.Network_Connection_List is not None:
            self.Network_Connection_List.export(lwrite, level, 'ProcessObj:', name_='Network_Connection_List', pretty_print=pretty_print)
        if self.Start_Time is not None:
            self.Start_Time.export(lwrite, level, 'ProcessObj:', name_='Start_Time', pretty_print=pretty_print)
        if self.Status is not None:
            self.Status.export(lwrite, level, 'ProcessObj:', name_='Status', pretty_print=pretty_print)
        if self.Username is not None:
            self.Username.export(lwrite, level, 'ProcessObj:', name_='Username', pretty_print=pretty_print)
        if self.User_Time is not None:
            self.User_Time.export(lwrite, level, 'ProcessObj:', name_='User_Time', pretty_print=pretty_print)
        if self.Extracted_Features is not None:
            self.Extracted_Features.export(lwrite, level, 'ProcessObj:', name_='Extracted_Features', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_hidden', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_hidden = True
            elif value in ('false', '0'):
                self.is_hidden = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(ProcessObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'PID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_PID(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Creation_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Time(obj_)
        elif nodeName_ == 'Parent_PID':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Parent_PID(obj_)
        elif nodeName_ == 'Child_PID_List':
            obj_ = ChildPIDListType.factory()
            obj_.build(child_)
            self.set_Child_PID_List(obj_)
        elif nodeName_ == 'Image_Info':
            obj_ = ImageInfoType.factory()
            obj_.build(child_)
            self.set_Image_Info(obj_)
        elif nodeName_ == 'Argument_List':
            obj_ = ArgumentListType.factory()
            obj_.build(child_)
            self.set_Argument_List(obj_)
        elif nodeName_ == 'Environment_Variable_List':
            obj_ = cybox_common.EnvironmentVariableListType.factory()
            obj_.build(child_)
            self.set_Environment_Variable_List(obj_)
        elif nodeName_ == 'Kernel_Time':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Kernel_Time(obj_)
        elif nodeName_ == 'Port_List':
            obj_ = PortListType.factory()
            obj_.build(child_)
            self.set_Port_List(obj_)
        elif nodeName_ == 'Network_Connection_List':
            obj_ = NetworkConnectionListType.factory()
            obj_.build(child_)
            self.set_Network_Connection_List(obj_)
        elif nodeName_ == 'Start_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Start_Time(obj_)
        elif nodeName_ == 'Status':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Status> element')
            self.set_Status(obj_)
        elif nodeName_ == 'Username':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Username(obj_)
        elif nodeName_ == 'User_Time':
            obj_ = cybox_common.DurationObjectPropertyType.factory()
            obj_.build(child_)
            self.set_User_Time(obj_)
        elif nodeName_ == 'Extracted_Features':
            obj_ = cybox_common.ExtractedFeaturesType.factory()
            obj_.build(child_)
            self.set_Extracted_Features(obj_)
        super(ProcessObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class ProcessObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Accept_Charset': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Max_Forwards': cybox_common.IntegerObjectPropertyType,
    'Proxy_Authorization': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Entry_Type': cybox_common.StringObjectPropertyType,
    'PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Path': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Record_Name': cybox_common.StringObjectPropertyType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'X_Forwarded_Proto': cybox_common.StringObjectPropertyType,
    'X_ATT_DeviceId': cybox_common.StringObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.AnyURIObjectPropertyType,
    'Length': cybox_common.PositiveIntegerObjectPropertyType,
    'Expect': cybox_common.StringObjectPropertyType,
    'If_Range': cybox_common.StringObjectPropertyType,
    'Layer3_Protocol': network_connection_object.Layer3ProtocolType,
    'TE': cybox_common.StringObjectPropertyType,
    'Parent_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Status_Code': cybox_common.PositiveIntegerObjectPropertyType,
    'Warning': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Layer4_Protocol': port_object.Layer4ProtocolType,
    'Content_Length': cybox_common.IntegerObjectPropertyType,
    'X_UA_Compatible': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Current_Directory': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeObjectPropertyType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Accept_Language': cybox_common.StringObjectPropertyType,
    'Raw_Header': cybox_common.StringObjectPropertyType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Compilers': cybox_common.CompilersType,
    'Username': cybox_common.StringObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Refresh': cybox_common.IntegerObjectPropertyType,
    'Build_Information': cybox_common.BuildInformationType,
    'Link': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'TTL': cybox_common.IntegerObjectPropertyType,
    'X_Frame_Options': cybox_common.StringObjectPropertyType,
    'Message_Body': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Age': cybox_common.IntegerObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Server': cybox_common.StringObjectPropertyType,
    'Access_Control_Allow_Origin': cybox_common.StringObjectPropertyType,
    'Range': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Retry_After': cybox_common.IntegerObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'WWW_Authenticate': cybox_common.StringObjectPropertyType,
    'Via': cybox_common.StringObjectPropertyType,
    'X_Requested_For': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Transfer_Encoding': cybox_common.StringObjectPropertyType,
    'Command_Line': cybox_common.StringObjectPropertyType,
    'Argument': cybox_common.StringObjectPropertyType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Child_PID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'User_Time': cybox_common.DurationObjectPropertyType,
    'Reason_Phrase': cybox_common.StringObjectPropertyType,
    'Record_Type': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Authorization': cybox_common.StringObjectPropertyType,
    'Accept_Encoding': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'If_Modified_Since': cybox_common.DateTimeObjectPropertyType,
    'X_Content_Type_Options': cybox_common.StringObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateTimeObjectPropertyType,
    'Cookie': cybox_common.StringObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Strict_Transport_Security': cybox_common.StringObjectPropertyType,
    'Content_Disposition': cybox_common.StringObjectPropertyType,
    'Segments': cybox_common.HashSegmentsType,
    'User_Agent': cybox_common.StringObjectPropertyType,
    'Address_Class': cybox_common.StringObjectPropertyType,
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
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'X_Powered_By': cybox_common.StringObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'Cache_Control': cybox_common.StringObjectPropertyType,
    'References': cybox_common.ToolReferencesType,
    'Service_Used': cybox_common.StringObjectPropertyType,
    'X_XSS_Protection': cybox_common.StringObjectPropertyType,
    'Layer7_Connections': network_connection_object.Layer7ConnectionsType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Trailer': cybox_common.StringObjectPropertyType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Data_Size': cybox_common.DataSizeType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Libraries': cybox_common.LibrariesType,
    'QClass': cybox_common.StringObjectPropertyType,
    'Content_Language': cybox_common.StringObjectPropertyType,
    'Content_Location': cybox_common.StringObjectPropertyType,
    'Content_MD5': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Expires': cybox_common.DateTimeObjectPropertyType,
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Content_Range': cybox_common.StringObjectPropertyType,
    'Content_Encoding': cybox_common.StringObjectPropertyType,
    'Pragma': cybox_common.StringObjectPropertyType,
    'Layer7_Protocol': network_connection_object.Layer7ProtocolType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Port_Value': cybox_common.PositiveIntegerObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Set_Cookie': cybox_common.StringObjectPropertyType,
    'Accept_Datetime': cybox_common.StringObjectPropertyType,
    'Environment_Variable_List': cybox_common.EnvironmentVariableListType,
    'Last_Modified': cybox_common.DateTimeObjectPropertyType,
    'Flags': cybox_common.HexBinaryObjectPropertyType,
    'Content_Type': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Proxy_Authenticate': cybox_common.StringObjectPropertyType,
    'If_None_Match': cybox_common.StringObjectPropertyType,
    'Accept_Ranges': cybox_common.StringObjectPropertyType,
    'Network_Connection': network_connection_object.NetworkConnectionObjectType,
    'Data_Length': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Accept': cybox_common.StringObjectPropertyType,
    'Port': port_object.PortObjectType,
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
        rootTag = 'Process'
        rootClass = ProcessObjectType
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
        rootTag = 'Process'
        rootClass = ProcessObjectType
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
        rootTag = 'Process'
        rootClass = ProcessObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Process",
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
    "ProcessObjectType",
    "NetworkConnectionListType",
    "ImageInfoType",
    "ProcessStatusType",
    "ChildPIDListType",
    "ArgumentListType",
    "PortListType"
    ]
