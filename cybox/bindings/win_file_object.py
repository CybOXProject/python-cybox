# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import file_object


class StreamListType(GeneratedsSuper):
    """The StreamListType type specifies a list of NTFS alternate data
    streams."""

    subclass = None
    superclass = None
    def __init__(self, Stream=None):
        if Stream is None:
            self.Stream = []
        else:
            self.Stream = Stream
    def factory(*args_, **kwargs_):
        if StreamListType.subclass:
            return StreamListType.subclass(*args_, **kwargs_)
        else:
            return StreamListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Stream(self): return self.Stream
    def set_Stream(self, Stream): self.Stream = Stream
    def add_Stream(self, value): self.Stream.append(value)
    def insert_Stream(self, index, value): self.Stream[index] = value
    def hasContent_(self):
        if (
            self.Stream
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='StreamListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StreamListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='StreamListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='StreamListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Stream_ in self.Stream:
            Stream_.export(lwrite, level, 'WinFileObj:', name_='Stream', pretty_print=pretty_print)
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
        if nodeName_ == 'Stream':
            obj_ = StreamObjectType.factory()
            obj_.build(child_)
            self.Stream.append(obj_)
# end class StreamListType

class WindowsFilePermissionsType(file_object.FilePermissionsType):
    """The WindowsFilePermissionsType type specifies Windows file
    permissions. It imports and extends the file_object.FilePermissionsType from
    the CybOX File Object."""

    subclass = None
    superclass = file_object.FilePermissionsType
    def __init__(self, Full_Control=None, Modify=None, Read=None, Read_And_Execute=None, Write=None):
        super(WindowsFilePermissionsType, self).__init__()
        self.Full_Control = Full_Control
        self.Modify = Modify
        self.Read = Read
        self.Read_And_Execute = Read_And_Execute
        self.Write = Write
    def factory(*args_, **kwargs_):
        if WindowsFilePermissionsType.subclass:
            return WindowsFilePermissionsType.subclass(*args_, **kwargs_)
        else:
            return WindowsFilePermissionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Full_Control(self): return self.Full_Control
    def set_Full_Control(self, Full_Control): self.Full_Control = Full_Control
    def get_Modify(self): return self.Modify
    def set_Modify(self, Modify): self.Modify = Modify
    def get_Read(self): return self.Read
    def set_Read(self, Read): self.Read = Read
    def get_Read_And_Execute(self): return self.Read_And_Execute
    def set_Read_And_Execute(self, Read_And_Execute): self.Read_And_Execute = Read_And_Execute
    def get_Write(self): return self.Write
    def set_Write(self, Write): self.Write = Write
    def hasContent_(self):
        if (
            self.Full_Control is not None or
            self.Modify is not None or
            self.Read is not None or
            self.Read_And_Execute is not None or
            self.Write is not None or
            super(WindowsFilePermissionsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFilePermissionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFilePermissionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='WindowsFilePermissionsType'):
        super(WindowsFilePermissionsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFilePermissionsType')
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFilePermissionsType', fromsubclass_=False, pretty_print=True):
        super(WindowsFilePermissionsType, self).exportChildren(lwrite, level, 'WinFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Full_Control is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sFull_Control>%s</%sFull_Control>%s' % ('WinFileObj:', self.gds_format_boolean(self.Full_Control, input_name='Full_Control'), 'WinFileObj:', eol_))
        if self.Modify is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sModify>%s</%sModify>%s' % ('WinFileObj:', self.gds_format_boolean(self.Modify, input_name='Modify'), 'WinFileObj:', eol_))
        if self.Read is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRead>%s</%sRead>%s' % ('WinFileObj:', self.gds_format_boolean(self.Read, input_name='Read'), 'WinFileObj:', eol_))
        if self.Read_And_Execute is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sRead_And_Execute>%s</%sRead_And_Execute>%s' % ('WinFileObj:', self.gds_format_boolean(self.Read_And_Execute, input_name='Read_And_Execute'), 'WinFileObj:', eol_))
        if self.Write is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%sWrite>%s</%sWrite>%s' % ('WinFileObj:', self.gds_format_boolean(self.Write, input_name='Write'), 'WinFileObj:', eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsFilePermissionsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Full_Control':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Full_Control')
            self.Full_Control = ival_
        elif nodeName_ == 'Modify':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Modify')
            self.Modify = ival_
        elif nodeName_ == 'Read':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Read')
            self.Read = ival_
        elif nodeName_ == 'Read_And_Execute':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Read_And_Execute')
            self.Read_And_Execute = ival_
        elif nodeName_ == 'Write':
            sval_ = child_.text
            if sval_ in ('true', '1'):
                ival_ = True
            elif sval_ in ('false', '0'):
                ival_ = False
            else:
                raise_parse_error(child_, 'requires boolean')
            ival_ = self.gds_validate_boolean(ival_, node, 'Write')
            self.Write = ival_
        super(WindowsFilePermissionsType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsFilePermissionsType

class WindowsFileAttributeType(cybox_common.BaseObjectPropertyType):
    """WindowsFileAttributeType specifies Windows file attributes via a
    union of the FileAttributesEnum type and the atomic xs:string
    type. Its base type is the CybOX Core cybox_common.BaseObjectPropertyType,
    for permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WindowsFileAttributeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WindowsFileAttributeType.subclass:
            return WindowsFileAttributeType.subclass(*args_, **kwargs_)
        else:
            return WindowsFileAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WindowsFileAttributeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileAttributeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='WindowsFileAttributeType'):
        super(WindowsFileAttributeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileAttributeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileAttributeType', fromsubclass_=False, pretty_print=True):
        super(WindowsFileAttributeType, self).exportChildren(lwrite, level, 'WinFileObj:', name_, True, pretty_print=pretty_print)
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
        super(WindowsFileAttributeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WindowsFileAttributeType

class WindowsFileAttributesType(file_object.FileAttributeType):
    """The WindowsFileAttributesType type specifies Windows file
    attributes. It imports and extends the file_object.FileAttributeType from
    the CybOX File Object."""

    subclass = None
    superclass = file_object.FileAttributeType
    def __init__(self, Attribute=None):
        super(WindowsFileAttributesType, self).__init__()
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if WindowsFileAttributesType.subclass:
            return WindowsFileAttributesType.subclass(*args_, **kwargs_)
        else:
            return WindowsFileAttributesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def validate_WindowsFileAttributeType(self, value):
        # Validate type WindowsFileAttributeType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Attribute or
            super(WindowsFileAttributesType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileAttributesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileAttributesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='WindowsFileAttributesType'):
        super(WindowsFileAttributesType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileAttributesType')
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileAttributesType', fromsubclass_=False, pretty_print=True):
        super(WindowsFileAttributesType, self).exportChildren(lwrite, level, 'WinFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(lwrite, level, 'WinFileObj:', name_='Attribute', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsFileAttributesType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attribute':
            obj_ = WindowsFileAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
        super(WindowsFileAttributesType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsFileAttributesType

class StreamObjectType(cybox_common.HashListType):
    """The StreamObjectType type is intended to characterize NTFS alternate
    data streams."""

    subclass = None
    superclass = cybox_common.HashListType
    def __init__(self, Hash=None, Name=None, Size_In_Bytes=None):
        super(StreamObjectType, self).__init__(Hash, )
        self.Name = Name
        self.Size_In_Bytes = Size_In_Bytes
    def factory(*args_, **kwargs_):
        if StreamObjectType.subclass:
            return StreamObjectType.subclass(*args_, **kwargs_)
        else:
            return StreamObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Size_In_Bytes(self): return self.Size_In_Bytes
    def set_Size_In_Bytes(self, Size_In_Bytes): self.Size_In_Bytes = Size_In_Bytes
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Size_In_Bytes is not None or
            super(StreamObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='StreamObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StreamObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='StreamObjectType'):
        super(StreamObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='StreamObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='StreamObjectType', fromsubclass_=False, pretty_print=True):
        super(StreamObjectType, self).exportChildren(lwrite, level, 'WinFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinFileObj:', name_='Name', pretty_print=pretty_print)
        if self.Size_In_Bytes is not None:
            self.Size_In_Bytes.export(lwrite, level, 'WinFileObj:', name_='Size_In_Bytes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(StreamObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Size_In_Bytes':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Size_In_Bytes(obj_)
        super(StreamObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class StreamObjectType

class WindowsFileObjectType(file_object.FileObjectType):
    """The WindowsFileObjectType type is intended to characterize Windows
    files."""

    subclass = None
    superclass = file_object.FileObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_packed=None, File_Name=None, File_Path=None, Device_Path=None, Full_Path=None, File_Extension=None, Size_In_Bytes=None, Magic_Number=None, File_Format=None, Hashes=None, Digital_Signatures=None, Modified_Time=None, Accessed_Time=None, Created_Time=None, File_Attributes_List=None, Permissions=None, User_Owner=None, Packer_List=None, Peak_Entropy=None, Sym_Links=None, Byte_Runs=None, Extracted_Features=None, Filename_Accessed_Time=None, Filename_Created_Time=None, Filename_Modified_Time=None, Drive=None, Security_ID=None, Security_Type=None, Stream_List=None):
        super(WindowsFileObjectType, self).__init__(object_reference, Custom_Properties, is_packed, File_Name, File_Path, Device_Path, Full_Path, File_Extension, Size_In_Bytes, Magic_Number, File_Format, Hashes, Digital_Signatures, Modified_Time, Accessed_Time, Created_Time, File_Attributes_List, Permissions, User_Owner, Packer_List, Peak_Entropy, Sym_Links, Byte_Runs, Extracted_Features, )
        self.Filename_Accessed_Time = Filename_Accessed_Time
        self.Filename_Created_Time = Filename_Created_Time
        self.Filename_Modified_Time = Filename_Modified_Time
        self.Drive = Drive
        self.Security_ID = Security_ID
        self.Security_Type = Security_Type
        self.Stream_List = Stream_List
    def factory(*args_, **kwargs_):
        if WindowsFileObjectType.subclass:
            return WindowsFileObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsFileObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Filename_Accessed_Time(self): return self.Filename_Accessed_Time
    def set_Filename_Accessed_Time(self, Filename_Accessed_Time): self.Filename_Accessed_Time = Filename_Accessed_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Filename_Created_Time(self): return self.Filename_Created_Time
    def set_Filename_Created_Time(self, Filename_Created_Time): self.Filename_Created_Time = Filename_Created_Time
    def get_Filename_Modified_Time(self): return self.Filename_Modified_Time
    def set_Filename_Modified_Time(self, Filename_Modified_Time): self.Filename_Modified_Time = Filename_Modified_Time
    def get_Drive(self): return self.Drive
    def set_Drive(self, Drive): self.Drive = Drive
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Security_ID(self): return self.Security_ID
    def set_Security_ID(self, Security_ID): self.Security_ID = Security_ID
    def get_Security_Type(self): return self.Security_Type
    def set_Security_Type(self, Security_Type): self.Security_Type = Security_Type
    def validate_SIDType(self, value):
        # Validate type cybox_common.SIDType, a restriction on None.
        pass
    def get_Stream_List(self): return self.Stream_List
    def set_Stream_List(self, Stream_List): self.Stream_List = Stream_List
    def hasContent_(self):
        if (
            self.Filename_Accessed_Time is not None or
            self.Filename_Created_Time is not None or
            self.Filename_Modified_Time is not None or
            self.Drive is not None or
            self.Security_ID is not None or
            self.Security_Type is not None or
            self.Stream_List is not None or
            super(WindowsFileObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFileObj:', name_='WindowsFileObjectType'):
        super(WindowsFileObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFileObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinFileObj:', name_='WindowsFileObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsFileObjectType, self).exportChildren(lwrite, level, 'WinFileObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Filename_Accessed_Time is not None:
            self.Filename_Accessed_Time.export(lwrite, level, 'WinFileObj:', name_='Filename_Accessed_Time', pretty_print=pretty_print)
        if self.Filename_Created_Time is not None:
            self.Filename_Created_Time.export(lwrite, level, 'WinFileObj:', name_='Filename_Created_Time', pretty_print=pretty_print)
        if self.Filename_Modified_Time is not None:
            self.Filename_Modified_Time.export(lwrite, level, 'WinFileObj:', name_='Filename_Modified_Time', pretty_print=pretty_print)
        if self.Drive is not None:
            self.Drive.export(lwrite, level, 'WinFileObj:', name_='Drive', pretty_print=pretty_print)
        if self.Security_ID is not None:
            self.Security_ID.export(lwrite, level, 'WinFileObj:', name_='Security_ID', pretty_print=pretty_print)
        if self.Security_Type is not None:
            self.Security_Type.export(lwrite, level, 'WinFileObj:', name_='Security_Type', pretty_print=pretty_print)
        if self.Stream_List is not None:
            self.Stream_List.export(lwrite, level, 'WinFileObj:', name_='Stream_List', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsFileObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Filename_Accessed_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Filename_Accessed_Time(obj_)
        elif nodeName_ == 'Filename_Created_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Filename_Created_Time(obj_)
        elif nodeName_ == 'Filename_Modified_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Filename_Modified_Time(obj_)
        elif nodeName_ == 'Drive':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Drive(obj_)
        elif nodeName_ == 'Security_ID':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_ID(obj_)
        elif nodeName_ == 'Security_Type':
            obj_ = cybox_common.SIDType.factory()
            obj_.build(child_)
            self.set_Security_Type(obj_)
        elif nodeName_ == 'Stream_List':
            obj_ = StreamListType.factory()
            obj_.build(child_)
            self.set_Stream_List(obj_)
        super(WindowsFileObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsFileObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'File_Extension': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Opcodes': cybox_common.StringObjectPropertyType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Size_In_Bytes': cybox_common.UnsignedLongObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Byte_Runs': cybox_common.ByteRunsType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Compiler': cybox_common.CompilerType,
    'Filename_Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Created_Time': cybox_common.DateTimeObjectPropertyType,
    'Type': file_object.PackerClassType,
    'Compilers': cybox_common.CompilersType,
    'Digital_Signatures': cybox_common.DigitalSignaturesType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'File_Format': cybox_common.StringObjectPropertyType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Detected_Entrypoint_Signatures': file_object.EntryPointSignatureListType,
    'Tool_Hashes': cybox_common.HashListType,
    'File_Path': file_object.FilePathType,
    'Entry_Point_Signature': file_object.EntryPointSignatureType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Filename_Modified_Time': cybox_common.DateTimeObjectPropertyType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Signature': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'User_Owner': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Packer': file_object.PackerType,
    'Security_Type': cybox_common.SIDType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'File_Attributes_List': file_object.FileAttributeType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Sym_Links': file_object.SymLinksListType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Packer_List': file_object.PackerListType,
    'Import': cybox_common.StringObjectPropertyType,
    'Accessed_Time': cybox_common.StringObjectPropertyType,
    'Sym_Link': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Permissions': file_object.FilePermissionsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Filename_Accessed_Time': cybox_common.DateTimeObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Time': cybox_common.TimeType,
    'EP_Jump_Codes': file_object.EPJumpCodeType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'File_Name': cybox_common.StringObjectPropertyType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Modified_Time': cybox_common.StringObjectPropertyType,
    'Libraries': cybox_common.LibrariesType,
    'Security_ID': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Magic_Number': cybox_common.HexBinaryObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Full_Path': cybox_common.StringObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Drive': cybox_common.StringObjectPropertyType,
    'Depth': cybox_common.IntegerObjectPropertyType,
    'Entry_Point': cybox_common.HexBinaryObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'File': file_object.FileObjectType,
    'Contributor': cybox_common.ContributorType,
    'Peak_Entropy': cybox_common.DoubleObjectPropertyType,
    'Tools': cybox_common.ToolsInformationType,
    'Tool': cybox_common.ToolInformationType,
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
        rootTag = 'Windows_File'
        rootClass = WindowsFileObjectType
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
        rootTag = 'Windows_File'
        rootClass = WindowsFileObjectType
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
        rootTag = 'Windows_File'
        rootClass = WindowsFileObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_File",
#        namespacedef_='')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

# Register abstract types
setattr(file_object, "WindowsFileAttributesType", WindowsFileAttributesType)
setattr(file_object, "WindowsFilePermissionsType", WindowsFilePermissionsType)

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "WindowsFileObjectType",
    "StreamObjectType",
    "StreamListType",
    "WindowsFileAttributesType",
    "WindowsFileAttributeType",
    "WindowsFilePermissionsType"
    ]
