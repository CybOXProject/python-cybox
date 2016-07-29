# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import volume_object


class WindowsVolumeAttributesListType(GeneratedsSuper):
    """A list of attributes describing this windows volume."""

    subclass = None
    superclass = None
    def __init__(self, Attribute=None):
        if Attribute is None:
            self.Attribute = []
        else:
            self.Attribute = Attribute
    def factory(*args_, **kwargs_):
        if WindowsVolumeAttributesListType.subclass:
            return WindowsVolumeAttributesListType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeAttributesListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attribute(self): return self.Attribute
    def set_Attribute(self, Attribute): self.Attribute = Attribute
    def add_Attribute(self, value): self.Attribute.append(value)
    def insert_Attribute(self, index, value): self.Attribute[index] = value
    def validate_WindowsVolumeAttributeType(self, value):
        # Validate type WindowsVolumeAttributeType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Attribute
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsVolumeAttributesListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType'):
        pass
    def exportChildren(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributesListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attribute_ in self.Attribute:
            Attribute_.export(lwrite, level, 'WinVolumeObj:', name_='Attribute', pretty_print=pretty_print)
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
        if nodeName_ == 'Attribute':
            obj_ = WindowsVolumeAttributeType.factory()
            obj_.build(child_)
            self.Attribute.append(obj_)
# end class WindowsVolumeAttributesListType

class WindowsVolumeAttributeType(cybox_common.BaseObjectPropertyType):
    """WindowsVolumeAttributeType specifies Windows volume attributes via a
    union of the WindowsVolumeAttributeEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WindowsVolumeAttributeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WindowsVolumeAttributeType.subclass:
            return WindowsVolumeAttributeType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WindowsVolumeAttributeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsVolumeAttributeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType'):
        super(WindowsVolumeAttributeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsVolumeAttributeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeAttributeType', fromsubclass_=False, pretty_print=True):
        super(WindowsVolumeAttributeType, self).exportChildren(lwrite, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
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
        super(WindowsVolumeAttributeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WindowsVolumeAttributeType

class WindowsDriveType(cybox_common.BaseObjectPropertyType):
    """WindowsDriveType specifies Windows drive types via a union of the
    WindowsDriveTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, pattern_type=None, datatype='string', refanging_transform=None, bit_mask=None, appears_random=None, trend=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WindowsDriveType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, pattern_type, datatype, refanging_transform, bit_mask, appears_random, trend, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, idref, is_defanged, id, condition, valueOf_, )
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WindowsDriveType.subclass:
            return WindowsDriveType.subclass(*args_, **kwargs_)
        else:
            return WindowsDriveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WindowsDriveType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsDriveType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsDriveType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsDriveType'):
        super(WindowsDriveType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsDriveType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsDriveType', fromsubclass_=False, pretty_print=True):
        super(WindowsDriveType, self).exportChildren(lwrite, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
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
        super(WindowsDriveType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WindowsDriveType

class WindowsVolumeObjectType(volume_object.VolumeObjectType):
    """The WindowsVolumeObjectType type is intended to characterize Windows
    disk volumes."""

    subclass = None
    superclass = volume_object.VolumeObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_mounted=None, Name=None, Device_Path=None, File_System_Type=None, Total_Allocation_Units=None, Sectors_Per_Allocation_Unit=None, Bytes_Per_Sector=None, Actual_Available_Allocation_Units=None, Creation_Time=None, File_System_Flag_List=None, Serial_Number=None, Attributes_List=None, Drive_Letter=None, Drive_Type=None):
        super(WindowsVolumeObjectType, self).__init__(object_reference, Custom_Properties, is_mounted, Name, Device_Path, File_System_Type, Total_Allocation_Units, Sectors_Per_Allocation_Unit, Bytes_Per_Sector, Actual_Available_Allocation_Units, Creation_Time, File_System_Flag_List, Serial_Number, )
        self.Attributes_List = Attributes_List
        self.Drive_Letter = Drive_Letter
        self.Drive_Type = Drive_Type
    def factory(*args_, **kwargs_):
        if WindowsVolumeObjectType.subclass:
            return WindowsVolumeObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsVolumeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attributes_List(self): return self.Attributes_List
    def set_Attributes_List(self, Attributes_List): self.Attributes_List = Attributes_List
    def get_Drive_Letter(self): return self.Drive_Letter
    def set_Drive_Letter(self, Drive_Letter): self.Drive_Letter = Drive_Letter
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Drive_Type(self): return self.Drive_Type
    def set_Drive_Type(self, Drive_Type): self.Drive_Type = Drive_Type
    def validate_WindowsDriveType(self, value):
        # Validate type WindowsDriveType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Attributes_List is not None or
            self.Drive_Letter is not None or
            self.Drive_Type is not None or
            super(WindowsVolumeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsVolumeObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType'):
        super(WindowsVolumeObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsVolumeObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinVolumeObj:', name_='WindowsVolumeObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsVolumeObjectType, self).exportChildren(lwrite, level, 'WinVolumeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Attributes_List is not None:
            self.Attributes_List.export(lwrite, level, 'WinVolumeObj:', name_='Attributes_List', pretty_print=pretty_print)
        if self.Drive_Letter is not None:
            self.Drive_Letter.export(lwrite, level, 'WinVolumeObj:', name_='Drive_Letter', pretty_print=pretty_print)
        if self.Drive_Type is not None:
            self.Drive_Type.export(lwrite, level, 'WinVolumeObj:', name_='Drive_Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsVolumeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attributes_List':
            obj_ = WindowsVolumeAttributesListType.factory()
            obj_.build(child_)
            self.set_Attributes_List(obj_)
        elif nodeName_ == 'Drive_Letter':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Drive_Letter(obj_)
        elif nodeName_ == 'Drive_Type':
            obj_ = WindowsDriveType.factory()
            obj_.build(child_)
            self.set_Drive_Type(obj_)
        super(WindowsVolumeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsVolumeObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Device_Path': cybox_common.StringObjectPropertyType,
    'Time': cybox_common.TimeType,
    'Errors': cybox_common.ErrorsType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'File_System_Flag_List': volume_object.FileSystemFlagListType,
    'Internal_Strings': cybox_common.InternalStringsType,
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
    'File_System_Flag': volume_object.VolumeFileSystemFlagType,
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
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Serial_Number': cybox_common.StringObjectPropertyType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
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
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Total_Allocation_Units': cybox_common.UnsignedLongObjectPropertyType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Language': cybox_common.StringObjectPropertyType,
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
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Volume': volume_object.VolumeObjectType,
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
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
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
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
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
        rootTag = 'Windows_Volume'
        rootClass = WindowsVolumeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Volume",
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
    "WindowsVolumeObjectType",
    "WindowsVolumeAttributesListType",
    "WindowsDriveType",
    "WindowsVolumeAttributeType"
    ]
