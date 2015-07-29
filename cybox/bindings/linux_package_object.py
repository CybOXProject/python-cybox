# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class LinuxPackageObjectType(cybox_common.ObjectPropertiesType):
    """The LinuxPackageObjectType type is intended to characterize Linux
    packages."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Architecture=None, Category=None, Description=None, Epoch=None, EVR=None, Name=None, Release=None, Vendor=None, Version=None):
        super(LinuxPackageObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Architecture = Architecture
        self.Category = Category
        self.Description = Description
        self.Epoch = Epoch
        self.EVR = EVR
        self.Name = Name
        self.Release = Release
        self.Vendor = Vendor
        self.Version = Version
    def factory(*args_, **kwargs_):
        if LinuxPackageObjectType.subclass:
            return LinuxPackageObjectType.subclass(*args_, **kwargs_)
        else:
            return LinuxPackageObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Architecture(self): return self.Architecture
    def set_Architecture(self, Architecture): self.Architecture = Architecture
    def validate_ArchitectureType(self, value):
        # Validate type ArchitectureType, a restriction on None.
        pass
    def get_Category(self): return self.Category
    def set_Category(self, Category): self.Category = Category
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Epoch(self): return self.Epoch
    def set_Epoch(self, Epoch): self.Epoch = Epoch
    def get_EVR(self): return self.EVR
    def set_EVR(self, EVR): self.EVR = EVR
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Release(self): return self.Release
    def set_Release(self, Release): self.Release = Release
    def get_Vendor(self): return self.Vendor
    def set_Vendor(self, Vendor): self.Vendor = Vendor
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def hasContent_(self):
        if (
            self.Architecture is not None or
            self.Category is not None or
            self.Description is not None or
            self.Epoch is not None or
            self.EVR is not None or
            self.Name is not None or
            self.Release is not None or
            self.Vendor is not None or
            self.Version is not None or
            super(LinuxPackageObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='LinuxPackageObj:', name_='LinuxPackageObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LinuxPackageObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='LinuxPackageObj:', name_='LinuxPackageObjectType'):
        super(LinuxPackageObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='LinuxPackageObjectType')
    def exportChildren(self, lwrite, level, namespace_='LinuxPackageObj:', name_='LinuxPackageObjectType', fromsubclass_=False, pretty_print=True):
        super(LinuxPackageObjectType, self).exportChildren(lwrite, level, 'LinuxPackageObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Architecture is not None:
            self.Architecture.export(lwrite, level, 'LinuxPackageObj:', name_='Architecture', pretty_print=pretty_print)
        if self.Category is not None:
            self.Category.export(lwrite, level, 'LinuxPackageObj:', name_='Category', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, 'LinuxPackageObj:', name_='Description', pretty_print=pretty_print)
        if self.Epoch is not None:
            self.Epoch.export(lwrite, level, 'LinuxPackageObj:', name_='Epoch', pretty_print=pretty_print)
        if self.EVR is not None:
            self.EVR.export(lwrite, level, 'LinuxPackageObj:', name_='EVR', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'LinuxPackageObj:', name_='Name', pretty_print=pretty_print)
        if self.Release is not None:
            self.Release.export(lwrite, level, 'LinuxPackageObj:', name_='Release', pretty_print=pretty_print)
        if self.Vendor is not None:
            self.Vendor.export(lwrite, level, 'LinuxPackageObj:', name_='Vendor', pretty_print=pretty_print)
        if self.Version is not None:
            self.Version.export(lwrite, level, 'LinuxPackageObj:', name_='Version', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(LinuxPackageObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Architecture':
            obj_ = cybox_common.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Architecture(obj_)
        elif nodeName_ == 'Category':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Category(obj_)
        elif nodeName_ == 'Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Epoch':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Epoch(obj_)
        elif nodeName_ == 'EVR':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_EVR(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Release':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Release(obj_)
        elif nodeName_ == 'Vendor':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Vendor(obj_)
        elif nodeName_ == 'Version':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Version(obj_)
        super(LinuxPackageObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class LinuxPackageObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
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
    'Release': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Epoch': cybox_common.StringObjectPropertyType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'EVR': cybox_common.StringObjectPropertyType,
    'Type': cybox_common.ControlledVocabularyStringType,
    'Compilers': cybox_common.CompilersType,
    'Vendor': cybox_common.StringObjectPropertyType,
    'String': cybox_common.ExtractedStringType,
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
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
    'Category': cybox_common.StringObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Dependencies': cybox_common.DependenciesType,
    'Offset': cybox_common.IntegerObjectPropertyType,
    'Date': cybox_common.DateRangeType,
    'Hashes': cybox_common.HashListType,
    'Segments': cybox_common.HashSegmentsType,
    'Segment_Count': cybox_common.IntegerObjectPropertyType,
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
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
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
        rootTag = 'Linux_Package'
        rootClass = LinuxPackageObjectType
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
        rootTag = 'Linux_Package'
        rootClass = LinuxPackageObjectType
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
        rootTag = 'Linux_Package'
        rootClass = LinuxPackageObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Linux_Package",
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
    "LinuxPackageObjectType",
    "ArchitectureType"
    ]
