# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_executable_file_object


class DeviceObjectStructType(GeneratedsSuper):
    """The DeviceObjectStructType type specifies the properties of a device
    object. In this context, a device object represents a logical,
    virtual, or physical device for which a driver handles I/O
    requests. See also: http://msdn.microsoft.com/en-
    us/library/windows/hardware/ff543147(v=vs.85).aspx"""

    subclass = None
    superclass = None
    def __init__(self, Attached_Device_Name=None, Attached_Device_Object=None, Attached_To_Device_Name=None, Attached_To_Device_Object=None, Attached_To_Driver_Object=None, Attached_To_Driver_Name=None, Device_Name=None, Device_Object=None):
        self.Attached_Device_Name = Attached_Device_Name
        self.Attached_Device_Object = Attached_Device_Object
        self.Attached_To_Device_Name = Attached_To_Device_Name
        self.Attached_To_Device_Object = Attached_To_Device_Object
        self.Attached_To_Driver_Object = Attached_To_Driver_Object
        self.Attached_To_Driver_Name = Attached_To_Driver_Name
        self.Device_Name = Device_Name
        self.Device_Object = Device_Object
    def factory(*args_, **kwargs_):
        if DeviceObjectStructType.subclass:
            return DeviceObjectStructType.subclass(*args_, **kwargs_)
        else:
            return DeviceObjectStructType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attached_Device_Name(self): return self.Attached_Device_Name
    def set_Attached_Device_Name(self, Attached_Device_Name): self.Attached_Device_Name = Attached_Device_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Attached_Device_Object(self): return self.Attached_Device_Object
    def set_Attached_Device_Object(self, Attached_Device_Object): self.Attached_Device_Object = Attached_Device_Object
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Attached_To_Device_Name(self): return self.Attached_To_Device_Name
    def set_Attached_To_Device_Name(self, Attached_To_Device_Name): self.Attached_To_Device_Name = Attached_To_Device_Name
    def get_Attached_To_Device_Object(self): return self.Attached_To_Device_Object
    def set_Attached_To_Device_Object(self, Attached_To_Device_Object): self.Attached_To_Device_Object = Attached_To_Device_Object
    def get_Attached_To_Driver_Object(self): return self.Attached_To_Driver_Object
    def set_Attached_To_Driver_Object(self, Attached_To_Driver_Object): self.Attached_To_Driver_Object = Attached_To_Driver_Object
    def get_Attached_To_Driver_Name(self): return self.Attached_To_Driver_Name
    def set_Attached_To_Driver_Name(self, Attached_To_Driver_Name): self.Attached_To_Driver_Name = Attached_To_Driver_Name
    def get_Device_Name(self): return self.Device_Name
    def set_Device_Name(self, Device_Name): self.Device_Name = Device_Name
    def get_Device_Object(self): return self.Device_Object
    def set_Device_Object(self, Device_Object): self.Device_Object = Device_Object
    def hasContent_(self):
        if (
            self.Attached_Device_Name is not None or
            self.Attached_Device_Object is not None or
            self.Attached_To_Device_Name is not None or
            self.Attached_To_Device_Object is not None or
            self.Attached_To_Driver_Object is not None or
            self.Attached_To_Driver_Name is not None or
            self.Device_Name is not None or
            self.Device_Object is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinDriverObj:', name_='DeviceObjectStructType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DeviceObjectStructType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinDriverObj:', name_='DeviceObjectStructType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinDriverObj:', name_='DeviceObjectStructType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Attached_Device_Name is not None:
            self.Attached_Device_Name.export(lwrite, level, 'WinDriverObj:', name_='Attached_Device_Name', pretty_print=pretty_print)
        if self.Attached_Device_Object is not None:
            self.Attached_Device_Object.export(lwrite, level, 'WinDriverObj:', name_='Attached_Device_Object', pretty_print=pretty_print)
        if self.Attached_To_Device_Name is not None:
            self.Attached_To_Device_Name.export(lwrite, level, 'WinDriverObj:', name_='Attached_To_Device_Name', pretty_print=pretty_print)
        if self.Attached_To_Device_Object is not None:
            self.Attached_To_Device_Object.export(lwrite, level, 'WinDriverObj:', name_='Attached_To_Device_Object', pretty_print=pretty_print)
        if self.Attached_To_Driver_Object is not None:
            self.Attached_To_Driver_Object.export(lwrite, level, 'WinDriverObj:', name_='Attached_To_Driver_Object', pretty_print=pretty_print)
        if self.Attached_To_Driver_Name is not None:
            self.Attached_To_Driver_Name.export(lwrite, level, 'WinDriverObj:', name_='Attached_To_Driver_Name', pretty_print=pretty_print)
        if self.Device_Name is not None:
            self.Device_Name.export(lwrite, level, 'WinDriverObj:', name_='Device_Name', pretty_print=pretty_print)
        if self.Device_Object is not None:
            self.Device_Object.export(lwrite, level, 'WinDriverObj:', name_='Device_Object', pretty_print=pretty_print)
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
        if nodeName_ == 'Attached_Device_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_Device_Name(obj_)
        elif nodeName_ == 'Attached_Device_Object':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_Device_Object(obj_)
        elif nodeName_ == 'Attached_To_Device_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_To_Device_Name(obj_)
        elif nodeName_ == 'Attached_To_Device_Object':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_To_Device_Object(obj_)
        elif nodeName_ == 'Attached_To_Driver_Object':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_To_Driver_Object(obj_)
        elif nodeName_ == 'Attached_To_Driver_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Attached_To_Driver_Name(obj_)
        elif nodeName_ == 'Device_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Device_Name(obj_)
        elif nodeName_ == 'Device_Object':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Device_Object(obj_)
# end class DeviceObjectStructType

class DeviceObjectListType(GeneratedsSuper):
    """The DeviceObjectListType specifies a list of device objects."""

    subclass = None
    superclass = None
    def __init__(self, Device_Object_Struct=None):
        if Device_Object_Struct is None:
            self.Device_Object_Struct = []
        else:
            self.Device_Object_Struct = Device_Object_Struct
    def factory(*args_, **kwargs_):
        if DeviceObjectListType.subclass:
            return DeviceObjectListType.subclass(*args_, **kwargs_)
        else:
            return DeviceObjectListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Device_Object_Struct(self): return self.Device_Object_Struct
    def set_Device_Object_Struct(self, Device_Object_Struct): self.Device_Object_Struct = Device_Object_Struct
    def add_Device_Object_Struct(self, value): self.Device_Object_Struct.append(value)
    def insert_Device_Object_Struct(self, index, value): self.Device_Object_Struct[index] = value
    def hasContent_(self):
        if (
            self.Device_Object_Struct
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinDriverObj:', name_='DeviceObjectListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DeviceObjectListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinDriverObj:', name_='DeviceObjectListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinDriverObj:', name_='DeviceObjectListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Device_Object_Struct_ in self.Device_Object_Struct:
            Device_Object_Struct_.export(lwrite, level, 'WinDriverObj:', name_='Device_Object_Struct', pretty_print=pretty_print)
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
        if nodeName_ == 'Device_Object_Struct':
            obj_ = DeviceObjectStructType.factory()
            obj_.build(child_)
            self.Device_Object_Struct.append(obj_)
# end class DeviceObjectListType

class WindowsDriverObjectType(win_executable_file_object.WindowsExecutableFileObjectType):
    """The WindowsDriverObject type is intended to characterize Windows
    device drivers."""

    subclass = None
    superclass = win_executable_file_object.WindowsExecutableFileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Device_Object_List=None, Driver_Init=None, Driver_Name=None, Driver_Object_Address=None, Driver_Start_IO=None, Driver_Unload=None, Image_Base=None, Image_Size=None, IRP_MJ_CLEANUP=None, IRP_MJ_CLOSE=None, IRP_MJ_CREATE=None, IRP_MJ_CREATE_MAILSLOT=None, IRP_MJ_CREATE_NAMED_PIPE=None, IRP_MJ_DEVICE_CHANGE=None, IRP_MJ_DEVICE_CONTROL=None, IRP_MJ_DIRECTORY_CONTROL=None, IRP_MJ_FILE_SYSTEM_CONTROL=None, IRP_MJ_FLUSH_BUFFERS=None, IRP_MJ_INTERNAL_DEVICE_CONTROL=None, IRP_MJ_LOCK_CONTROL=None, IRP_MJ_PNP=None, IRP_MJ_POWER=None, IRP_MJ_READ=None, IRP_MJ_QUERY_EA=None, IRP_MJ_QUERY_INFORMATION=None, IRP_MJ_QUERY_SECURITY=None, IRP_MJ_QUERY_QUOTA=None, IRP_MJ_QUERY_VOLUME_INFORMATION=None, IRP_MJ_SET_EA=None, IRP_MJ_SET_INFORMATION=None, IRP_MJ_SET_SECURITY=None, IRP_MJ_SET_QUOTA=None, IRP_MJ_SET_VOLUME_INFORMATION=None, IRP_MJ_SHUTDOWN=None, IRP_MJ_SYSTEM_CONTROL=None, IRP_MJ_WRITE=None):
        super(WindowsDriverObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Device_Object_List = Device_Object_List
        self.Driver_Init = Driver_Init
        self.Driver_Name = Driver_Name
        self.Driver_Object_Address = Driver_Object_Address
        self.Driver_Start_IO = Driver_Start_IO
        self.Driver_Unload = Driver_Unload
        self.Image_Base = Image_Base
        self.Image_Size = Image_Size
        self.IRP_MJ_CLEANUP = IRP_MJ_CLEANUP
        self.IRP_MJ_CLOSE = IRP_MJ_CLOSE
        self.IRP_MJ_CREATE = IRP_MJ_CREATE
        self.IRP_MJ_CREATE_MAILSLOT = IRP_MJ_CREATE_MAILSLOT
        self.IRP_MJ_CREATE_NAMED_PIPE = IRP_MJ_CREATE_NAMED_PIPE
        self.IRP_MJ_DEVICE_CHANGE = IRP_MJ_DEVICE_CHANGE
        self.IRP_MJ_DEVICE_CONTROL = IRP_MJ_DEVICE_CONTROL
        self.IRP_MJ_DIRECTORY_CONTROL = IRP_MJ_DIRECTORY_CONTROL
        self.IRP_MJ_FILE_SYSTEM_CONTROL = IRP_MJ_FILE_SYSTEM_CONTROL
        self.IRP_MJ_FLUSH_BUFFERS = IRP_MJ_FLUSH_BUFFERS
        self.IRP_MJ_INTERNAL_DEVICE_CONTROL = IRP_MJ_INTERNAL_DEVICE_CONTROL
        self.IRP_MJ_LOCK_CONTROL = IRP_MJ_LOCK_CONTROL
        self.IRP_MJ_PNP = IRP_MJ_PNP
        self.IRP_MJ_POWER = IRP_MJ_POWER
        self.IRP_MJ_READ = IRP_MJ_READ
        self.IRP_MJ_QUERY_EA = IRP_MJ_QUERY_EA
        self.IRP_MJ_QUERY_INFORMATION = IRP_MJ_QUERY_INFORMATION
        self.IRP_MJ_QUERY_SECURITY = IRP_MJ_QUERY_SECURITY
        self.IRP_MJ_QUERY_QUOTA = IRP_MJ_QUERY_QUOTA
        self.IRP_MJ_QUERY_VOLUME_INFORMATION = IRP_MJ_QUERY_VOLUME_INFORMATION
        self.IRP_MJ_SET_EA = IRP_MJ_SET_EA
        self.IRP_MJ_SET_INFORMATION = IRP_MJ_SET_INFORMATION
        self.IRP_MJ_SET_SECURITY = IRP_MJ_SET_SECURITY
        self.IRP_MJ_SET_QUOTA = IRP_MJ_SET_QUOTA
        self.IRP_MJ_SET_VOLUME_INFORMATION = IRP_MJ_SET_VOLUME_INFORMATION
        self.IRP_MJ_SHUTDOWN = IRP_MJ_SHUTDOWN
        self.IRP_MJ_SYSTEM_CONTROL = IRP_MJ_SYSTEM_CONTROL
        self.IRP_MJ_WRITE = IRP_MJ_WRITE
    def factory(*args_, **kwargs_):
        if WindowsDriverObjectType.subclass:
            return WindowsDriverObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsDriverObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Device_Object_List(self): return self.Device_Object_List
    def set_Device_Object_List(self, Device_Object_List): self.Device_Object_List = Device_Object_List
    def get_Driver_Init(self): return self.Driver_Init
    def set_Driver_Init(self, Driver_Init): self.Driver_Init = Driver_Init
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Driver_Name(self): return self.Driver_Name
    def set_Driver_Name(self, Driver_Name): self.Driver_Name = Driver_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Driver_Object_Address(self): return self.Driver_Object_Address
    def set_Driver_Object_Address(self, Driver_Object_Address): self.Driver_Object_Address = Driver_Object_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Driver_Start_IO(self): return self.Driver_Start_IO
    def set_Driver_Start_IO(self, Driver_Start_IO): self.Driver_Start_IO = Driver_Start_IO
    def get_Driver_Unload(self): return self.Driver_Unload
    def set_Driver_Unload(self, Driver_Unload): self.Driver_Unload = Driver_Unload
    def get_Image_Base(self): return self.Image_Base
    def set_Image_Base(self, Image_Base): self.Image_Base = Image_Base
    def get_Image_Size(self): return self.Image_Size
    def set_Image_Size(self, Image_Size): self.Image_Size = Image_Size
    def get_IRP_MJ_CLEANUP(self): return self.IRP_MJ_CLEANUP
    def set_IRP_MJ_CLEANUP(self, IRP_MJ_CLEANUP): self.IRP_MJ_CLEANUP = IRP_MJ_CLEANUP
    def get_IRP_MJ_CLOSE(self): return self.IRP_MJ_CLOSE
    def set_IRP_MJ_CLOSE(self, IRP_MJ_CLOSE): self.IRP_MJ_CLOSE = IRP_MJ_CLOSE
    def get_IRP_MJ_CREATE(self): return self.IRP_MJ_CREATE
    def set_IRP_MJ_CREATE(self, IRP_MJ_CREATE): self.IRP_MJ_CREATE = IRP_MJ_CREATE
    def get_IRP_MJ_CREATE_MAILSLOT(self): return self.IRP_MJ_CREATE_MAILSLOT
    def set_IRP_MJ_CREATE_MAILSLOT(self, IRP_MJ_CREATE_MAILSLOT): self.IRP_MJ_CREATE_MAILSLOT = IRP_MJ_CREATE_MAILSLOT
    def get_IRP_MJ_CREATE_NAMED_PIPE(self): return self.IRP_MJ_CREATE_NAMED_PIPE
    def set_IRP_MJ_CREATE_NAMED_PIPE(self, IRP_MJ_CREATE_NAMED_PIPE): self.IRP_MJ_CREATE_NAMED_PIPE = IRP_MJ_CREATE_NAMED_PIPE
    def get_IRP_MJ_DEVICE_CHANGE(self): return self.IRP_MJ_DEVICE_CHANGE
    def set_IRP_MJ_DEVICE_CHANGE(self, IRP_MJ_DEVICE_CHANGE): self.IRP_MJ_DEVICE_CHANGE = IRP_MJ_DEVICE_CHANGE
    def get_IRP_MJ_DEVICE_CONTROL(self): return self.IRP_MJ_DEVICE_CONTROL
    def set_IRP_MJ_DEVICE_CONTROL(self, IRP_MJ_DEVICE_CONTROL): self.IRP_MJ_DEVICE_CONTROL = IRP_MJ_DEVICE_CONTROL
    def get_IRP_MJ_DIRECTORY_CONTROL(self): return self.IRP_MJ_DIRECTORY_CONTROL
    def set_IRP_MJ_DIRECTORY_CONTROL(self, IRP_MJ_DIRECTORY_CONTROL): self.IRP_MJ_DIRECTORY_CONTROL = IRP_MJ_DIRECTORY_CONTROL
    def get_IRP_MJ_FILE_SYSTEM_CONTROL(self): return self.IRP_MJ_FILE_SYSTEM_CONTROL
    def set_IRP_MJ_FILE_SYSTEM_CONTROL(self, IRP_MJ_FILE_SYSTEM_CONTROL): self.IRP_MJ_FILE_SYSTEM_CONTROL = IRP_MJ_FILE_SYSTEM_CONTROL
    def get_IRP_MJ_FLUSH_BUFFERS(self): return self.IRP_MJ_FLUSH_BUFFERS
    def set_IRP_MJ_FLUSH_BUFFERS(self, IRP_MJ_FLUSH_BUFFERS): self.IRP_MJ_FLUSH_BUFFERS = IRP_MJ_FLUSH_BUFFERS
    def get_IRP_MJ_INTERNAL_DEVICE_CONTROL(self): return self.IRP_MJ_INTERNAL_DEVICE_CONTROL
    def set_IRP_MJ_INTERNAL_DEVICE_CONTROL(self, IRP_MJ_INTERNAL_DEVICE_CONTROL): self.IRP_MJ_INTERNAL_DEVICE_CONTROL = IRP_MJ_INTERNAL_DEVICE_CONTROL
    def get_IRP_MJ_LOCK_CONTROL(self): return self.IRP_MJ_LOCK_CONTROL
    def set_IRP_MJ_LOCK_CONTROL(self, IRP_MJ_LOCK_CONTROL): self.IRP_MJ_LOCK_CONTROL = IRP_MJ_LOCK_CONTROL
    def get_IRP_MJ_PNP(self): return self.IRP_MJ_PNP
    def set_IRP_MJ_PNP(self, IRP_MJ_PNP): self.IRP_MJ_PNP = IRP_MJ_PNP
    def get_IRP_MJ_POWER(self): return self.IRP_MJ_POWER
    def set_IRP_MJ_POWER(self, IRP_MJ_POWER): self.IRP_MJ_POWER = IRP_MJ_POWER
    def get_IRP_MJ_READ(self): return self.IRP_MJ_READ
    def set_IRP_MJ_READ(self, IRP_MJ_READ): self.IRP_MJ_READ = IRP_MJ_READ
    def get_IRP_MJ_QUERY_EA(self): return self.IRP_MJ_QUERY_EA
    def set_IRP_MJ_QUERY_EA(self, IRP_MJ_QUERY_EA): self.IRP_MJ_QUERY_EA = IRP_MJ_QUERY_EA
    def get_IRP_MJ_QUERY_INFORMATION(self): return self.IRP_MJ_QUERY_INFORMATION
    def set_IRP_MJ_QUERY_INFORMATION(self, IRP_MJ_QUERY_INFORMATION): self.IRP_MJ_QUERY_INFORMATION = IRP_MJ_QUERY_INFORMATION
    def get_IRP_MJ_QUERY_SECURITY(self): return self.IRP_MJ_QUERY_SECURITY
    def set_IRP_MJ_QUERY_SECURITY(self, IRP_MJ_QUERY_SECURITY): self.IRP_MJ_QUERY_SECURITY = IRP_MJ_QUERY_SECURITY
    def get_IRP_MJ_QUERY_QUOTA(self): return self.IRP_MJ_QUERY_QUOTA
    def set_IRP_MJ_QUERY_QUOTA(self, IRP_MJ_QUERY_QUOTA): self.IRP_MJ_QUERY_QUOTA = IRP_MJ_QUERY_QUOTA
    def get_IRP_MJ_QUERY_VOLUME_INFORMATION(self): return self.IRP_MJ_QUERY_VOLUME_INFORMATION
    def set_IRP_MJ_QUERY_VOLUME_INFORMATION(self, IRP_MJ_QUERY_VOLUME_INFORMATION): self.IRP_MJ_QUERY_VOLUME_INFORMATION = IRP_MJ_QUERY_VOLUME_INFORMATION
    def get_IRP_MJ_SET_EA(self): return self.IRP_MJ_SET_EA
    def set_IRP_MJ_SET_EA(self, IRP_MJ_SET_EA): self.IRP_MJ_SET_EA = IRP_MJ_SET_EA
    def get_IRP_MJ_SET_INFORMATION(self): return self.IRP_MJ_SET_INFORMATION
    def set_IRP_MJ_SET_INFORMATION(self, IRP_MJ_SET_INFORMATION): self.IRP_MJ_SET_INFORMATION = IRP_MJ_SET_INFORMATION
    def get_IRP_MJ_SET_SECURITY(self): return self.IRP_MJ_SET_SECURITY
    def set_IRP_MJ_SET_SECURITY(self, IRP_MJ_SET_SECURITY): self.IRP_MJ_SET_SECURITY = IRP_MJ_SET_SECURITY
    def get_IRP_MJ_SET_QUOTA(self): return self.IRP_MJ_SET_QUOTA
    def set_IRP_MJ_SET_QUOTA(self, IRP_MJ_SET_QUOTA): self.IRP_MJ_SET_QUOTA = IRP_MJ_SET_QUOTA
    def get_IRP_MJ_SET_VOLUME_INFORMATION(self): return self.IRP_MJ_SET_VOLUME_INFORMATION
    def set_IRP_MJ_SET_VOLUME_INFORMATION(self, IRP_MJ_SET_VOLUME_INFORMATION): self.IRP_MJ_SET_VOLUME_INFORMATION = IRP_MJ_SET_VOLUME_INFORMATION
    def get_IRP_MJ_SHUTDOWN(self): return self.IRP_MJ_SHUTDOWN
    def set_IRP_MJ_SHUTDOWN(self, IRP_MJ_SHUTDOWN): self.IRP_MJ_SHUTDOWN = IRP_MJ_SHUTDOWN
    def get_IRP_MJ_SYSTEM_CONTROL(self): return self.IRP_MJ_SYSTEM_CONTROL
    def set_IRP_MJ_SYSTEM_CONTROL(self, IRP_MJ_SYSTEM_CONTROL): self.IRP_MJ_SYSTEM_CONTROL = IRP_MJ_SYSTEM_CONTROL
    def get_IRP_MJ_WRITE(self): return self.IRP_MJ_WRITE
    def set_IRP_MJ_WRITE(self, IRP_MJ_WRITE): self.IRP_MJ_WRITE = IRP_MJ_WRITE
    def hasContent_(self):
        if (
            self.Device_Object_List is not None or
            self.Driver_Init is not None or
            self.Driver_Name is not None or
            self.Driver_Object_Address is not None or
            self.Driver_Start_IO is not None or
            self.Driver_Unload is not None or
            self.Image_Base is not None or
            self.Image_Size is not None or
            self.IRP_MJ_CLEANUP is not None or
            self.IRP_MJ_CLOSE is not None or
            self.IRP_MJ_CREATE is not None or
            self.IRP_MJ_CREATE_MAILSLOT is not None or
            self.IRP_MJ_CREATE_NAMED_PIPE is not None or
            self.IRP_MJ_DEVICE_CHANGE is not None or
            self.IRP_MJ_DEVICE_CONTROL is not None or
            self.IRP_MJ_DIRECTORY_CONTROL is not None or
            self.IRP_MJ_FILE_SYSTEM_CONTROL is not None or
            self.IRP_MJ_FLUSH_BUFFERS is not None or
            self.IRP_MJ_INTERNAL_DEVICE_CONTROL is not None or
            self.IRP_MJ_LOCK_CONTROL is not None or
            self.IRP_MJ_PNP is not None or
            self.IRP_MJ_POWER is not None or
            self.IRP_MJ_READ is not None or
            self.IRP_MJ_QUERY_EA is not None or
            self.IRP_MJ_QUERY_INFORMATION is not None or
            self.IRP_MJ_QUERY_SECURITY is not None or
            self.IRP_MJ_QUERY_QUOTA is not None or
            self.IRP_MJ_QUERY_VOLUME_INFORMATION is not None or
            self.IRP_MJ_SET_EA is not None or
            self.IRP_MJ_SET_INFORMATION is not None or
            self.IRP_MJ_SET_SECURITY is not None or
            self.IRP_MJ_SET_QUOTA is not None or
            self.IRP_MJ_SET_VOLUME_INFORMATION is not None or
            self.IRP_MJ_SHUTDOWN is not None or
            self.IRP_MJ_SYSTEM_CONTROL is not None or
            self.IRP_MJ_WRITE is not None or
            super(WindowsDriverObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinDriverObj:', name_='WindowsDriverObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsDriverObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinDriverObj:', name_='WindowsDriverObjectType'):
        super(WindowsDriverObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsDriverObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinDriverObj:', name_='WindowsDriverObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsDriverObjectType, self).exportChildren(lwrite, level, 'WinDriverObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Device_Object_List is not None:
            self.Device_Object_List.export(lwrite, level, 'WinDriverObj:', name_='Device_Object_List', pretty_print=pretty_print)
        if self.Driver_Init is not None:
            self.Driver_Init.export(lwrite, level, 'WinDriverObj:', name_='Driver_Init', pretty_print=pretty_print)
        if self.Driver_Name is not None:
            self.Driver_Name.export(lwrite, level, 'WinDriverObj:', name_='Driver_Name', pretty_print=pretty_print)
        if self.Driver_Object_Address is not None:
            self.Driver_Object_Address.export(lwrite, level, 'WinDriverObj:', name_='Driver_Object_Address', pretty_print=pretty_print)
        if self.Driver_Start_IO is not None:
            self.Driver_Start_IO.export(lwrite, level, 'WinDriverObj:', name_='Driver_Start_IO', pretty_print=pretty_print)
        if self.Driver_Unload is not None:
            self.Driver_Unload.export(lwrite, level, 'WinDriverObj:', name_='Driver_Unload', pretty_print=pretty_print)
        if self.Image_Base is not None:
            self.Image_Base.export(lwrite, level, 'WinDriverObj:', name_='Image_Base', pretty_print=pretty_print)
        if self.Image_Size is not None:
            self.Image_Size.export(lwrite, level, 'WinDriverObj:', name_='Image_Size', pretty_print=pretty_print)
        if self.IRP_MJ_CLEANUP is not None:
            self.IRP_MJ_CLEANUP.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_CLEANUP', pretty_print=pretty_print)
        if self.IRP_MJ_CLOSE is not None:
            self.IRP_MJ_CLOSE.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_CLOSE', pretty_print=pretty_print)
        if self.IRP_MJ_CREATE is not None:
            self.IRP_MJ_CREATE.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_CREATE', pretty_print=pretty_print)
        if self.IRP_MJ_CREATE_MAILSLOT is not None:
            self.IRP_MJ_CREATE_MAILSLOT.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_CREATE_MAILSLOT', pretty_print=pretty_print)
        if self.IRP_MJ_CREATE_NAMED_PIPE is not None:
            self.IRP_MJ_CREATE_NAMED_PIPE.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_CREATE_NAMED_PIPE', pretty_print=pretty_print)
        if self.IRP_MJ_DEVICE_CHANGE is not None:
            self.IRP_MJ_DEVICE_CHANGE.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_DEVICE_CHANGE', pretty_print=pretty_print)
        if self.IRP_MJ_DEVICE_CONTROL is not None:
            self.IRP_MJ_DEVICE_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_DEVICE_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_DIRECTORY_CONTROL is not None:
            self.IRP_MJ_DIRECTORY_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_DIRECTORY_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_FILE_SYSTEM_CONTROL is not None:
            self.IRP_MJ_FILE_SYSTEM_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_FILE_SYSTEM_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_FLUSH_BUFFERS is not None:
            self.IRP_MJ_FLUSH_BUFFERS.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_FLUSH_BUFFERS', pretty_print=pretty_print)
        if self.IRP_MJ_INTERNAL_DEVICE_CONTROL is not None:
            self.IRP_MJ_INTERNAL_DEVICE_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_INTERNAL_DEVICE_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_LOCK_CONTROL is not None:
            self.IRP_MJ_LOCK_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_LOCK_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_PNP is not None:
            self.IRP_MJ_PNP.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_PNP', pretty_print=pretty_print)
        if self.IRP_MJ_POWER is not None:
            self.IRP_MJ_POWER.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_POWER', pretty_print=pretty_print)
        if self.IRP_MJ_READ is not None:
            self.IRP_MJ_READ.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_READ', pretty_print=pretty_print)
        if self.IRP_MJ_QUERY_EA is not None:
            self.IRP_MJ_QUERY_EA.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_QUERY_EA', pretty_print=pretty_print)
        if self.IRP_MJ_QUERY_INFORMATION is not None:
            self.IRP_MJ_QUERY_INFORMATION.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_QUERY_INFORMATION', pretty_print=pretty_print)
        if self.IRP_MJ_QUERY_SECURITY is not None:
            self.IRP_MJ_QUERY_SECURITY.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_QUERY_SECURITY', pretty_print=pretty_print)
        if self.IRP_MJ_QUERY_QUOTA is not None:
            self.IRP_MJ_QUERY_QUOTA.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_QUERY_QUOTA', pretty_print=pretty_print)
        if self.IRP_MJ_QUERY_VOLUME_INFORMATION is not None:
            self.IRP_MJ_QUERY_VOLUME_INFORMATION.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_QUERY_VOLUME_INFORMATION', pretty_print=pretty_print)
        if self.IRP_MJ_SET_EA is not None:
            self.IRP_MJ_SET_EA.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SET_EA', pretty_print=pretty_print)
        if self.IRP_MJ_SET_INFORMATION is not None:
            self.IRP_MJ_SET_INFORMATION.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SET_INFORMATION', pretty_print=pretty_print)
        if self.IRP_MJ_SET_SECURITY is not None:
            self.IRP_MJ_SET_SECURITY.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SET_SECURITY', pretty_print=pretty_print)
        if self.IRP_MJ_SET_QUOTA is not None:
            self.IRP_MJ_SET_QUOTA.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SET_QUOTA', pretty_print=pretty_print)
        if self.IRP_MJ_SET_VOLUME_INFORMATION is not None:
            self.IRP_MJ_SET_VOLUME_INFORMATION.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SET_VOLUME_INFORMATION', pretty_print=pretty_print)
        if self.IRP_MJ_SHUTDOWN is not None:
            self.IRP_MJ_SHUTDOWN.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SHUTDOWN', pretty_print=pretty_print)
        if self.IRP_MJ_SYSTEM_CONTROL is not None:
            self.IRP_MJ_SYSTEM_CONTROL.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_SYSTEM_CONTROL', pretty_print=pretty_print)
        if self.IRP_MJ_WRITE is not None:
            self.IRP_MJ_WRITE.export(lwrite, level, 'WinDriverObj:', name_='IRP_MJ_WRITE', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsDriverObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Device_Object_List':
            obj_ = DeviceObjectListType.factory()
            obj_.build(child_)
            self.set_Device_Object_List(obj_)
        elif nodeName_ == 'Driver_Init':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Driver_Init(obj_)
        elif nodeName_ == 'Driver_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Driver_Name(obj_)
        elif nodeName_ == 'Driver_Object_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Driver_Object_Address(obj_)
        elif nodeName_ == 'Driver_Start_IO':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Driver_Start_IO(obj_)
        elif nodeName_ == 'Driver_Unload':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Driver_Unload(obj_)
        elif nodeName_ == 'Image_Base':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Image_Base(obj_)
        elif nodeName_ == 'Image_Size':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Image_Size(obj_)
        elif nodeName_ == 'IRP_MJ_CLEANUP':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_CLEANUP(obj_)
        elif nodeName_ == 'IRP_MJ_CLOSE':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_CLOSE(obj_)
        elif nodeName_ == 'IRP_MJ_CREATE':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_CREATE(obj_)
        elif nodeName_ == 'IRP_MJ_CREATE_MAILSLOT':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_CREATE_MAILSLOT(obj_)
        elif nodeName_ == 'IRP_MJ_CREATE_NAMED_PIPE':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_CREATE_NAMED_PIPE(obj_)
        elif nodeName_ == 'IRP_MJ_DEVICE_CHANGE':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_DEVICE_CHANGE(obj_)
        elif nodeName_ == 'IRP_MJ_DEVICE_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_DEVICE_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_DIRECTORY_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_DIRECTORY_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_FILE_SYSTEM_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_FILE_SYSTEM_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_FLUSH_BUFFERS':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_FLUSH_BUFFERS(obj_)
        elif nodeName_ == 'IRP_MJ_INTERNAL_DEVICE_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_INTERNAL_DEVICE_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_LOCK_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_LOCK_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_PNP':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_PNP(obj_)
        elif nodeName_ == 'IRP_MJ_POWER':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_POWER(obj_)
        elif nodeName_ == 'IRP_MJ_READ':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_READ(obj_)
        elif nodeName_ == 'IRP_MJ_QUERY_EA':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_QUERY_EA(obj_)
        elif nodeName_ == 'IRP_MJ_QUERY_INFORMATION':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_QUERY_INFORMATION(obj_)
        elif nodeName_ == 'IRP_MJ_QUERY_SECURITY':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_QUERY_SECURITY(obj_)
        elif nodeName_ == 'IRP_MJ_QUERY_QUOTA':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_QUERY_QUOTA(obj_)
        elif nodeName_ == 'IRP_MJ_QUERY_VOLUME_INFORMATION':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_QUERY_VOLUME_INFORMATION(obj_)
        elif nodeName_ == 'IRP_MJ_SET_EA':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SET_EA(obj_)
        elif nodeName_ == 'IRP_MJ_SET_INFORMATION':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SET_INFORMATION(obj_)
        elif nodeName_ == 'IRP_MJ_SET_SECURITY':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SET_SECURITY(obj_)
        elif nodeName_ == 'IRP_MJ_SET_QUOTA':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SET_QUOTA(obj_)
        elif nodeName_ == 'IRP_MJ_SET_VOLUME_INFORMATION':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SET_VOLUME_INFORMATION(obj_)
        elif nodeName_ == 'IRP_MJ_SHUTDOWN':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SHUTDOWN(obj_)
        elif nodeName_ == 'IRP_MJ_SYSTEM_CONTROL':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_SYSTEM_CONTROL(obj_)
        elif nodeName_ == 'IRP_MJ_WRITE':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_IRP_MJ_WRITE(obj_)
        super(WindowsDriverObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsDriverObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'IRP_MJ_CREATE_MAILSLOT': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_SET_QUOTA': cybox_common.UnsignedLongObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'IRP_MJ_FLUSH_BUFFERS': cybox_common.UnsignedLongObjectPropertyType,
    'Errors': cybox_common.ErrorsType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Metadata': cybox_common.MetadataType,
    'IRP_MJ_DIRECTORY_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'Image_Base': cybox_common.HexBinaryObjectPropertyType,
    'Hash': cybox_common.HashType,
    'Attached_To_Driver_Name': cybox_common.StringObjectPropertyType,
    'IRP_MJ_SYSTEM_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_CLEANUP': cybox_common.UnsignedLongObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Segment_Hash': cybox_common.HashValueType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'IRP_MJ_QUERY_SECURITY': cybox_common.UnsignedLongObjectPropertyType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'IRP_MJ_SHUTDOWN': cybox_common.UnsignedLongObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'IRP_MJ_DEVICE_CHANGE': cybox_common.UnsignedLongObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'IRP_MJ_QUERY_EA': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_READ': cybox_common.UnsignedLongObjectPropertyType,
    'Driver_Unload': cybox_common.HexBinaryObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'IRP_MJ_CREATE': cybox_common.UnsignedLongObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'IRP_MJ_SET_EA': cybox_common.UnsignedLongObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'Driver_Object_Address': cybox_common.HexBinaryObjectPropertyType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'IRP_MJ_DEVICE_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Import': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'IRP_MJ_CLOSE': cybox_common.UnsignedLongObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Attached_To_Driver_Object': cybox_common.UnsignedLongObjectPropertyType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Device_Object': cybox_common.UnsignedLongObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Driver_Start_IO': cybox_common.HexBinaryObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'IRP_MJ_CREATE_NAMED_PIPE': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_SET_INFORMATION': cybox_common.UnsignedLongObjectPropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'IRP_MJ_FILE_SYSTEM_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Driver_Init': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_QUERY_QUOTA': cybox_common.UnsignedLongObjectPropertyType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'IRP_MJ_SET_VOLUME_INFORMATION': cybox_common.UnsignedLongObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Image_Size': cybox_common.HexBinaryObjectPropertyType,
    'IRP_MJ_SET_SECURITY': cybox_common.UnsignedLongObjectPropertyType,
    'IRP_MJ_INTERNAL_DEVICE_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'IRP_MJ_QUERY_INFORMATION': cybox_common.UnsignedLongObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'IRP_MJ_POWER': cybox_common.UnsignedLongObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Time': cybox_common.TimeType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'IRP_MJ_WRITE': cybox_common.UnsignedLongObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Libraries': cybox_common.LibrariesType,
    'Attached_Device_Object': cybox_common.UnsignedLongObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Attached_To_Device_Name': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'IRP_MJ_PNP': cybox_common.UnsignedLongObjectPropertyType,
    'Device_Name': cybox_common.StringObjectPropertyType,
    'Driver_Name': cybox_common.StringObjectPropertyType,
    'IRP_MJ_LOCK_CONTROL': cybox_common.UnsignedLongObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Attached_To_Device_Object': cybox_common.UnsignedLongObjectPropertyType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Attached_Device_Name': cybox_common.StringObjectPropertyType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'IRP_MJ_QUERY_VOLUME_INFORMATION': cybox_common.UnsignedLongObjectPropertyType,
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
        rootTag = 'Windows_Driver'
        rootClass = WindowsDriverObjectType
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
        rootTag = 'Windows_Driver'
        rootClass = WindowsDriverObjectType
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
        rootTag = 'Windows_Driver'
        rootClass = WindowsDriverObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Driver",
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
    "WindowsDriverObjectType",
    "DeviceObjectStructType",
    "DeviceObjectListType"
    ]
