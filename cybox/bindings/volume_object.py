# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class VolumeOptionsType(GeneratedsSuper):
    """The VolumeOptionsType type specifies the particular options set for
    the volume. This is an abstract type since volume options are
    OS-specific, and is extended by the related OS-specific CybOX
    volume objects."""

    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if VolumeOptionsType.subclass:
            return VolumeOptionsType.subclass(*args_, **kwargs_)
        else:
            return VolumeOptionsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeOptionsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeOptionsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='VolumeObj:', name_='VolumeOptionsType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeOptionsType', fromsubclass_=False, pretty_print=True):
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
# end class VolumeOptionsType

class FileSystemFlagListType(GeneratedsSuper):
    """The FileSystemFlagListType is a listing of the flags specified for
    the volume by the file system."""

    subclass = None
    superclass = None
    def __init__(self, File_System_Flag=None):
        if File_System_Flag is None:
            self.File_System_Flag = []
        else:
            self.File_System_Flag = File_System_Flag
    def factory(*args_, **kwargs_):
        if FileSystemFlagListType.subclass:
            return FileSystemFlagListType.subclass(*args_, **kwargs_)
        else:
            return FileSystemFlagListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_File_System_Flag(self): return self.File_System_Flag
    def set_File_System_Flag(self, File_System_Flag): self.File_System_Flag = File_System_Flag
    def add_File_System_Flag(self, value): self.File_System_Flag.append(value)
    def insert_File_System_Flag(self, index, value): self.File_System_Flag[index] = value
    def validate_VolumeFileSystemFlagType(self, value):
        # Validate type VolumeFileSystemFlagType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.File_System_Flag
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='VolumeObj:', name_='FileSystemFlagListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FileSystemFlagListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='VolumeObj:', name_='FileSystemFlagListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='VolumeObj:', name_='FileSystemFlagListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for File_System_Flag_ in self.File_System_Flag:
            File_System_Flag_.export(lwrite, level, 'VolumeObj:', name_='File_System_Flag', pretty_print=pretty_print)
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
        if nodeName_ == 'File_System_Flag':
            obj_ = VolumeFileSystemFlagType.factory()
            obj_.build(child_)
            self.File_System_Flag.append(obj_)
# end class FileSystemFlagListType

class VolumeFileSystemFlagType(cybox_common.BaseObjectPropertyType):
    """VolumeFileSystemFlagType specifies file system flags, via a union of
    the VolumeFileSystemFlagEnum type and the atomic xs:string type.
    Its base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(VolumeFileSystemFlagType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if VolumeFileSystemFlagType.subclass:
            return VolumeFileSystemFlagType.subclass(*args_, **kwargs_)
        else:
            return VolumeFileSystemFlagType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(VolumeFileSystemFlagType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeFileSystemFlagType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeFileSystemFlagType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='VolumeObj:', name_='VolumeFileSystemFlagType'):
        super(VolumeFileSystemFlagType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeFileSystemFlagType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeFileSystemFlagType', fromsubclass_=False, pretty_print=True):
        super(VolumeFileSystemFlagType, self).exportChildren(lwrite, level, 'VolumeObj:', name_, True, pretty_print=pretty_print)
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
        super(VolumeFileSystemFlagType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class VolumeFileSystemFlagType

class VolumeObjectType(cybox_common.ObjectPropertiesType):
    """The VolumeObjectType type is intended to characterize generic drive
    volumes.The is_mounted field specifies whether the volume is
    mounted."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_mounted=None, Name=None, Device_Path=None, File_System_Type=None, Total_Allocation_Units=None, Sectors_Per_Allocation_Unit=None, Bytes_Per_Sector=None, Actual_Available_Allocation_Units=None, Creation_Time=None, File_System_Flag_List=None, Serial_Number=None):
        super(VolumeObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_mounted = _cast(bool, is_mounted)
        self.Name = Name
        self.Device_Path = Device_Path
        self.File_System_Type = File_System_Type
        self.Total_Allocation_Units = Total_Allocation_Units
        self.Sectors_Per_Allocation_Unit = Sectors_Per_Allocation_Unit
        self.Bytes_Per_Sector = Bytes_Per_Sector
        self.Actual_Available_Allocation_Units = Actual_Available_Allocation_Units
        self.Creation_Time = Creation_Time
        self.File_System_Flag_List = File_System_Flag_List
        self.Serial_Number = Serial_Number
    def factory(*args_, **kwargs_):
        if VolumeObjectType.subclass:
            return VolumeObjectType.subclass(*args_, **kwargs_)
        else:
            return VolumeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Device_Path(self): return self.Device_Path
    def set_Device_Path(self, Device_Path): self.Device_Path = Device_Path
    def get_File_System_Type(self): return self.File_System_Type
    def set_File_System_Type(self, File_System_Type): self.File_System_Type = File_System_Type
    def get_Total_Allocation_Units(self): return self.Total_Allocation_Units
    def set_Total_Allocation_Units(self, Total_Allocation_Units): self.Total_Allocation_Units = Total_Allocation_Units
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Sectors_Per_Allocation_Unit(self): return self.Sectors_Per_Allocation_Unit
    def set_Sectors_Per_Allocation_Unit(self, Sectors_Per_Allocation_Unit): self.Sectors_Per_Allocation_Unit = Sectors_Per_Allocation_Unit
    def validate_UnsignedIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Bytes_Per_Sector(self): return self.Bytes_Per_Sector
    def set_Bytes_Per_Sector(self, Bytes_Per_Sector): self.Bytes_Per_Sector = Bytes_Per_Sector
    def validate_PositiveIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.PositiveIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Actual_Available_Allocation_Units(self): return self.Actual_Available_Allocation_Units
    def set_Actual_Available_Allocation_Units(self, Actual_Available_Allocation_Units): self.Actual_Available_Allocation_Units = Actual_Available_Allocation_Units
    def get_Creation_Time(self): return self.Creation_Time
    def set_Creation_Time(self, Creation_Time): self.Creation_Time = Creation_Time
    def validate_DateTimeObjectPropertyType(self, value):
        # Validate type cybox_common.DateTimeObjectPropertyType, a restriction on None.
        pass
    def get_File_System_Flag_List(self): return self.File_System_Flag_List
    def set_File_System_Flag_List(self, File_System_Flag_List): self.File_System_Flag_List = File_System_Flag_List
    def get_Serial_Number(self): return self.Serial_Number
    def set_Serial_Number(self, Serial_Number): self.Serial_Number = Serial_Number
    def get_is_mounted(self): return self.is_mounted
    def set_is_mounted(self, is_mounted): self.is_mounted = is_mounted
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Device_Path is not None or
            self.File_System_Type is not None or
            self.Total_Allocation_Units is not None or
            self.Sectors_Per_Allocation_Unit is not None or
            self.Bytes_Per_Sector is not None or
            self.Actual_Available_Allocation_Units is not None or
            self.Creation_Time is not None or
            self.File_System_Flag_List is not None or
            self.Serial_Number is not None or
            super(VolumeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='VolumeObj:', name_='VolumeObjectType'):
        super(VolumeObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='VolumeObjectType')
        if self.is_mounted is not None:

            lwrite(' is_mounted="%s"' % self.gds_format_boolean(self.is_mounted, input_name='is_mounted'))
    def exportChildren(self, lwrite, level, namespace_='VolumeObj:', name_='VolumeObjectType', fromsubclass_=False, pretty_print=True):
        super(VolumeObjectType, self).exportChildren(lwrite, level, 'VolumeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'VolumeObj:', name_='Name', pretty_print=pretty_print)
        if self.Device_Path is not None:
            self.Device_Path.export(lwrite, level, 'VolumeObj:', name_='Device_Path', pretty_print=pretty_print)
        if self.File_System_Type is not None:
            self.File_System_Type.export(lwrite, level, 'VolumeObj:', name_='File_System_Type', pretty_print=pretty_print)
        if self.Total_Allocation_Units is not None:
            self.Total_Allocation_Units.export(lwrite, level, 'VolumeObj:', name_='Total_Allocation_Units', pretty_print=pretty_print)
        if self.Sectors_Per_Allocation_Unit is not None:
            self.Sectors_Per_Allocation_Unit.export(lwrite, level, 'VolumeObj:', name_='Sectors_Per_Allocation_Unit', pretty_print=pretty_print)
        if self.Bytes_Per_Sector is not None:
            self.Bytes_Per_Sector.export(lwrite, level, 'VolumeObj:', name_='Bytes_Per_Sector', pretty_print=pretty_print)
        if self.Actual_Available_Allocation_Units is not None:
            self.Actual_Available_Allocation_Units.export(lwrite, level, 'VolumeObj:', name_='Actual_Available_Allocation_Units', pretty_print=pretty_print)
        if self.Creation_Time is not None:
            self.Creation_Time.export(lwrite, level, 'VolumeObj:', name_='Creation_Time', pretty_print=pretty_print)
        if self.File_System_Flag_List is not None:
            self.File_System_Flag_List.export(lwrite, level, 'VolumeObj:', name_='File_System_Flag_List', pretty_print=pretty_print)
        if self.Serial_Number is not None:
            self.Serial_Number.export(lwrite, level, 'VolumeObj:', name_='Serial_Number', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_mounted', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_mounted = True
            elif value in ('false', '0'):
                self.is_mounted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(VolumeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Device_Path':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Device_Path(obj_)
        elif nodeName_ == 'File_System_Type':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_File_System_Type(obj_)
        elif nodeName_ == 'Total_Allocation_Units':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Total_Allocation_Units(obj_)
        elif nodeName_ == 'Sectors_Per_Allocation_Unit':
            obj_ = cybox_common.UnsignedIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Sectors_Per_Allocation_Unit(obj_)
        elif nodeName_ == 'Bytes_Per_Sector':
            obj_ = cybox_common.PositiveIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Bytes_Per_Sector(obj_)
        elif nodeName_ == 'Actual_Available_Allocation_Units':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Actual_Available_Allocation_Units(obj_)
        elif nodeName_ == 'Creation_Time':
            obj_ = cybox_common.DateTimeObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Creation_Time(obj_)
        elif nodeName_ == 'File_System_Flag_List':
            obj_ = FileSystemFlagListType.factory()
            obj_.build(child_)
            self.set_File_System_Flag_List(obj_)
        elif nodeName_ == 'Serial_Number':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Serial_Number(obj_)
        super(VolumeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class VolumeObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Errors': cybox_common.ErrorsType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Serial_Number': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
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
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Creation_Time': cybox_common.DateTimeObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'File_System_Type': cybox_common.StringObjectPropertyType,
    'Actual_Available_Allocation_Units': cybox_common.UnsignedLongObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Bytes_Per_Sector': cybox_common.PositiveIntegerObjectPropertyType,
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
        rootTag = 'Volume'
        rootClass = VolumeObjectType
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
        rootTag = 'Volume'
        rootClass = VolumeObjectType
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
        rootTag = 'Volume'
        rootClass = VolumeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Volume",
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
    "VolumeObjectType",
    "VolumeOptionsType",
    "FileSystemFlagListType",
    "VolumeFileSystemFlagType"
    ]
