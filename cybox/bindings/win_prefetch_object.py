# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import device_object
from . import win_volume_object


class AccessedFileListType(GeneratedsSuper):
    """The AccessedFileListType specifies a list of files accessed by a
    prefetch application."""

    subclass = None
    superclass = None
    def __init__(self, Accessed_Filename=None):
        if Accessed_Filename is None:
            self.Accessed_Filename = []
        else:
            self.Accessed_Filename = Accessed_Filename
    def factory(*args_, **kwargs_):
        if AccessedFileListType.subclass:
            return AccessedFileListType.subclass(*args_, **kwargs_)
        else:
            return AccessedFileListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Accessed_Filename(self): return self.Accessed_Filename
    def set_Accessed_Filename(self, Accessed_Filename): self.Accessed_Filename = Accessed_Filename
    def add_Accessed_Filename(self, value): self.Accessed_Filename.append(value)
    def insert_Accessed_Filename(self, index, value): self.Accessed_Filename[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Accessed_Filename
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinPrefetchObj:', name_='AccessedFileListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AccessedFileListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinPrefetchObj:', name_='AccessedFileListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinPrefetchObj:', name_='AccessedFileListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Accessed_Filename_ in self.Accessed_Filename:
            Accessed_Filename_.export(lwrite, level, 'WinPrefetchObj:', name_='Accessed_Filename', pretty_print=pretty_print)
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
        if nodeName_ == 'Accessed_Filename':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Accessed_Filename.append(obj_)
# end class AccessedFileListType

class AccessedDirectoryListType(GeneratedsSuper):
    """The AccessedDirectoryListType specifies a list of directories
    accessed by a prefetch application."""

    subclass = None
    superclass = None
    def __init__(self, Accessed_Directory=None):
        if Accessed_Directory is None:
            self.Accessed_Directory = []
        else:
            self.Accessed_Directory = Accessed_Directory
    def factory(*args_, **kwargs_):
        if AccessedDirectoryListType.subclass:
            return AccessedDirectoryListType.subclass(*args_, **kwargs_)
        else:
            return AccessedDirectoryListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Accessed_Directory(self): return self.Accessed_Directory
    def set_Accessed_Directory(self, Accessed_Directory): self.Accessed_Directory = Accessed_Directory
    def add_Accessed_Directory(self, value): self.Accessed_Directory.append(value)
    def insert_Accessed_Directory(self, index, value): self.Accessed_Directory[index] = value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Accessed_Directory
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinPrefetchObj:', name_='AccessedDirectoryListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AccessedDirectoryListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinPrefetchObj:', name_='AccessedDirectoryListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinPrefetchObj:', name_='AccessedDirectoryListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Accessed_Directory_ in self.Accessed_Directory:
            Accessed_Directory_.export(lwrite, level, 'WinPrefetchObj:', name_='Accessed_Directory', pretty_print=pretty_print)
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
        if nodeName_ == 'Accessed_Directory':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.Accessed_Directory.append(obj_)
# end class AccessedDirectoryListType

class VolumeType(GeneratedsSuper):
    """VolumeType characterizes the volume information in the Windows
    prefetch file."""

    subclass = None
    superclass = None
    def __init__(self, VolumeItem=None, DeviceItem=None):
        if VolumeItem is None:
            self.VolumeItem = []
        else:
            self.VolumeItem = VolumeItem
        if DeviceItem is None:
            self.DeviceItem = []
        else:
            self.DeviceItem = DeviceItem
    def factory(*args_, **kwargs_):
        if VolumeType.subclass:
            return VolumeType.subclass(*args_, **kwargs_)
        else:
            return VolumeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_VolumeItem(self): return self.VolumeItem
    def set_VolumeItem(self, VolumeItem): self.VolumeItem = VolumeItem
    def add_VolumeItem(self, value): self.VolumeItem.append(value)
    def insert_VolumeItem(self, index, value): self.VolumeItem[index] = value
    def get_DeviceItem(self): return self.DeviceItem
    def set_DeviceItem(self, DeviceItem): self.DeviceItem = DeviceItem
    def add_DeviceItem(self, value): self.DeviceItem.append(value)
    def insert_DeviceItem(self, index, value): self.DeviceItem[index] = value
    def hasContent_(self):
        if (
            self.VolumeItem or
            self.DeviceItem
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinPrefetchObj:', name_='VolumeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinPrefetchObj:', name_='VolumeType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinPrefetchObj:', name_='VolumeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for VolumeItem_ in self.VolumeItem:
            VolumeItem_.export(lwrite, level, 'WinPrefetchObj:', name_='VolumeItem', pretty_print=pretty_print)
        for DeviceItem_ in self.DeviceItem:
            DeviceItem_.export(lwrite, level, 'WinPrefetchObj:', name_='DeviceItem', pretty_print=pretty_print)
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
        if nodeName_ == 'VolumeItem':
            obj_ = win_volume_object.WindowsVolumeObjectType.factory()
            obj_.build(child_)
            self.VolumeItem.append(obj_)
        elif nodeName_ == 'DeviceItem':
            obj_ = device_object.DeviceObjectType.factory()
            obj_.build(child_)
            self.DeviceItem.append(obj_)
# end class VolumeType

class WindowsPrefetchObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsPrefetchObjectType type is intended to characterize
    entries in the Windows prefetch files. Starting with Windows XP,
    prefetching was introduced to speed up application startup. The
    prefetch object draws upon the descriptions and XML sample at
    http://www.forensicswiki.org/wiki/Prefetch_XML"""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Application_File_Name=None, Prefetch_Hash=None, Times_Executed=None, First_Run=None, Last_Run=None, Volume=None, Accessed_File_List=None, Accessed_Directory_List=None):
        super(WindowsPrefetchObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Application_File_Name = Application_File_Name
        self.Prefetch_Hash = Prefetch_Hash
        self.Times_Executed = Times_Executed
        self.First_Run = First_Run
        self.Last_Run = Last_Run
        self.Volume = Volume
        self.Accessed_File_List = Accessed_File_List
        self.Accessed_Directory_List = Accessed_Directory_List
    def factory(*args_, **kwargs_):
        if WindowsPrefetchObjectType.subclass:
            return WindowsPrefetchObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsPrefetchObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Application_File_Name(self): return self.Application_File_Name
    def set_Application_File_Name(self, Application_File_Name): self.Application_File_Name = Application_File_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Prefetch_Hash(self): return self.Prefetch_Hash
    def set_Prefetch_Hash(self, Prefetch_Hash): self.Prefetch_Hash = Prefetch_Hash
    def get_Times_Executed(self): return self.Times_Executed
    def set_Times_Executed(self, Times_Executed): self.Times_Executed = Times_Executed
    def validate_LongObjectPropertyType(self, value):
        # Validate type cybox_common.LongObjectPropertyType, a restriction on None.
        pass
    def get_First_Run(self): return self.First_Run
    def set_First_Run(self, First_Run): self.First_Run = First_Run
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_Last_Run(self): return self.Last_Run
    def set_Last_Run(self, Last_Run): self.Last_Run = Last_Run
    def get_Volume(self): return self.Volume
    def set_Volume(self, Volume): self.Volume = Volume
    def get_Accessed_File_List(self): return self.Accessed_File_List
    def set_Accessed_File_List(self, Accessed_File_List): self.Accessed_File_List = Accessed_File_List
    def get_Accessed_Directory_List(self): return self.Accessed_Directory_List
    def set_Accessed_Directory_List(self, Accessed_Directory_List): self.Accessed_Directory_List = Accessed_Directory_List
    def hasContent_(self):
        if (
            self.Application_File_Name is not None or
            self.Prefetch_Hash is not None or
            self.Times_Executed is not None or
            self.First_Run is not None or
            self.Last_Run is not None or
            self.Volume is not None or
            self.Accessed_File_List is not None or
            self.Accessed_Directory_List is not None or
            super(WindowsPrefetchObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinPrefetchObj:', name_='WindowsPrefetchObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsPrefetchObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinPrefetchObj:', name_='WindowsPrefetchObjectType'):
        super(WindowsPrefetchObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsPrefetchObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinPrefetchObj:', name_='WindowsPrefetchObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsPrefetchObjectType, self).exportChildren(lwrite, level, 'WinPrefetchObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Application_File_Name is not None:
            self.Application_File_Name.export(lwrite, level, 'WinPrefetchObj:', name_='Application_File_Name', pretty_print=pretty_print)
        if self.Prefetch_Hash is not None:
            self.Prefetch_Hash.export(lwrite, level, 'WinPrefetchObj:', name_='Prefetch_Hash', pretty_print=pretty_print)
        if self.Times_Executed is not None:
            self.Times_Executed.export(lwrite, level, 'WinPrefetchObj:', name_='Times_Executed', pretty_print=pretty_print)
        if self.First_Run is not None:
            self.First_Run.export(lwrite, level, 'WinPrefetchObj:', name_='First_Run', pretty_print=pretty_print)
        if self.Last_Run is not None:
            self.Last_Run.export(lwrite, level, 'WinPrefetchObj:', name_='Last_Run', pretty_print=pretty_print)
        if self.Volume is not None:
            self.Volume.export(lwrite, level, 'WinPrefetchObj:', name_='Volume', pretty_print=pretty_print)
        if self.Accessed_File_List is not None:
            self.Accessed_File_List.export(lwrite, level, 'WinPrefetchObj:', name_='Accessed_File_List', pretty_print=pretty_print)
        if self.Accessed_Directory_List is not None:
            self.Accessed_Directory_List.export(lwrite, level, 'WinPrefetchObj:', name_='Accessed_Directory_List', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsPrefetchObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Application_File_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Application_File_Name(obj_)
        elif nodeName_ == 'Prefetch_Hash':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Prefetch_Hash(obj_)
        elif nodeName_ == 'Times_Executed':
            obj_ = cybox_common.LongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Times_Executed(obj_)
        elif nodeName_ == 'First_Run':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_First_Run(obj_)
        elif nodeName_ == 'Last_Run':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Last_Run(obj_)
        elif nodeName_ == 'Volume':
            obj_ = VolumeType.factory()
            obj_.build(child_)
            self.set_Volume(obj_)
        elif nodeName_ == 'Accessed_File_List':
            obj_ = AccessedFileListType.factory()
            obj_.build(child_)
            self.set_Accessed_File_List(obj_)
        elif nodeName_ == 'Accessed_Directory_List':
            obj_ = AccessedDirectoryListType.factory()
            obj_.build(child_)
            self.set_Accessed_Directory_List(obj_)
        super(WindowsPrefetchObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsPrefetchObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Windows_Volume': win_volume_object.WindowsVolumeObjectType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'DeviceItem': device_object.DeviceObjectType,
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
    'Last_Run': cybox_common.DateTimeObjectPropertyType,
    'Attribute': win_volume_object.WindowsVolumeAttributeType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'VolumeItem': win_volume_object.WindowsVolumeObjectType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Accessed_Directory': cybox_common.StringObjectPropertyType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Application_File_Name': cybox_common.StringObjectPropertyType,
    'Tool_Hashes': cybox_common.HashListType,
    'Serial_Number': cybox_common.StringObjectPropertyType,
    'Times_Executed': cybox_common.LongObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Device': device_object.DeviceObjectType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Prefetch_Hash': cybox_common.StringObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Drive_Letter': cybox_common.StringObjectPropertyType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Sectors_Per_Allocation_Unit': cybox_common.UnsignedIntegerObjectPropertyType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Total_Allocation_Units': cybox_common.UnsignedLongObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Manufacturer': cybox_common.StringObjectPropertyType,
    'Accessed_Filename': cybox_common.StringObjectPropertyType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Device_Type': cybox_common.StringObjectPropertyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Drive_Type': win_volume_object.WindowsDriveType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'File_System_Type': cybox_common.StringObjectPropertyType,
    'Actual_Available_Allocation_Units': cybox_common.UnsignedLongObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Model': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'First_Run': cybox_common.DateTimeObjectPropertyType,
    'Attributes_List': win_volume_object.WindowsVolumeAttributesListType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Bytes_Per_Sector': cybox_common.PositiveIntegerObjectPropertyType,
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
        rootTag = 'Windows_Prefetch_Entry'
        rootClass = WindowsPrefetchObjectType
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
        rootTag = 'Windows_Prefetch_Entry'
        rootClass = WindowsPrefetchObjectType
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
        rootTag = 'Windows_Prefetch_Entry'
        rootClass = WindowsPrefetchObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Prefetch_Entry",
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
    "WindowsPrefetchObjectType",
    "AccessedFileListType",
    "AccessedDirectoryListType",
    "VolumeType"
    ]
