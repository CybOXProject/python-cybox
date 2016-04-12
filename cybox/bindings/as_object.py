# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class ASObjectType(cybox_common.ObjectPropertiesType):
    """The ASObjectType type is intended to characterize an autonomous
    system (AS)."""
    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Number=None, Name=None, Handle=None, Regional_Internet_Registry=None):
        super(ASObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.Number = Number
        self.Name = Name
        self.Handle = Handle
        self.Regional_Internet_Registry = Regional_Internet_Registry
    def factory(*args_, **kwargs_):
        if ASObjectType.subclass:
            return ASObjectType.subclass(*args_, **kwargs_)
        else:
            return ASObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Number(self): return self.Number
    def set_Number(self, Number): self.Number = Number
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_Regional_Internet_Registry(self): return self.Regional_Internet_Registry
    def set_Regional_Internet_Registry(self, Regional_Internet_Registry): self.Regional_Internet_Registry = Regional_Internet_Registry
    def validate_RegionalRegistryType(self, value):
        # Validate type cybox_common.RegionalRegistryType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Number is not None or
            self.Name is not None or
            self.Handle is not None or
            self.Regional_Internet_Registry is not None or
            super(ASObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='ASObj:', name_='ASObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ASObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ASObj:', name_='ASObjectType'):
        super(ASObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ASObjectType')
    def exportChildren(self, lwrite, level, namespace_='ASObj:', name_='ASObjectType', fromsubclass_=False, pretty_print=True):
        super(ASObjectType, self).exportChildren(lwrite, level, 'ASObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Number is not None:
            self.Number.export(lwrite, level, 'ASObj:', name_='Number', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'ASObj:', name_='Name', pretty_print=pretty_print)
        if self.Handle is not None:
            self.Handle.export(lwrite, level, 'ASObj:', name_='Handle', pretty_print=pretty_print)
        if self.Regional_Internet_Registry is not None:
            self.Regional_Internet_Registry.export(lwrite, level, 'ASObj:', name_='Regional_Internet_Registry', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ASObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Number':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Number(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Handle':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Handle(obj_)
        elif nodeName_ == 'Regional_Internet_Registry':
            obj_ = cybox_common.RegionalRegistryType.factory()
            obj_.build(child_)
            self.set_Regional_Internet_Registry(obj_)
        super(ASObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class ASObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Compiler': cybox_common.CompilerType,
    'Start_Date': cybox_common.DateWithPrecisionType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeWithPrecisionType,
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
    'Observable_Location': cybox_common.LocationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Regional_Internet_Registry': cybox_common.RegionalRegistryType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
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
    'Error': cybox_common.ErrorType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Number': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'End_Time': cybox_common.DateTimeWithPrecisionType,
    'Contributor': cybox_common.ContributorType,
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
        rootTag = 'AS'
        rootClass = ASObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'AS'
        rootClass = ASObjectType
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
        rootTag = 'AS'
        rootClass = ASObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="AS",
        namespacedef_='')
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
    "ASObjectType"    ]
