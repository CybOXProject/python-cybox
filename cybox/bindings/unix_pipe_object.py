# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from cybox.bindings import *
from . import cybox_common
from . import pipe_object


class UnixPipeObjectType(pipe_object.PipeObjectType):
    """The UnixPipeObjectType type is intended to characterize Unix pipes."""

    subclass = None
    superclass = pipe_object.PipeObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, named=None, Name=None, Permission_Mode=None):
        super(UnixPipeObjectType, self).__init__(object_reference, Custom_Properties, named, Name, )
        self.Permission_Mode = Permission_Mode
    def factory(*args_, **kwargs_):
        if UnixPipeObjectType.subclass:
            return UnixPipeObjectType.subclass(*args_, **kwargs_)
        else:
            return UnixPipeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Permission_Mode(self): return self.Permission_Mode
    def set_Permission_Mode(self, Permission_Mode): self.Permission_Mode = Permission_Mode
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Permission_Mode is not None or
            super(UnixPipeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='UnixPipeObj:', name_='UnixPipeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixPipeObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='UnixPipeObj:', name_='UnixPipeObjectType'):
        super(UnixPipeObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='UnixPipeObjectType')
    def exportChildren(self, lwrite, level, namespace_='UnixPipeObj:', name_='UnixPipeObjectType', fromsubclass_=False, pretty_print=True):
        super(UnixPipeObjectType, self).exportChildren(lwrite, level, 'UnixPipeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Permission_Mode is not None:
            self.Permission_Mode.export(lwrite, level, 'UnixPipeObj:', name_='Permission_Mode', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(UnixPipeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Permission_Mode':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Permission_Mode(obj_)
        super(UnixPipeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class UnixPipeObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
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
    'Pipe': pipe_object.PipeObjectType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'English_Translation': cybox_common.StringObjectPropertyType,
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
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Language': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'Contributors': cybox_common.PersonnelType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Identifier': cybox_common.PlatformIdentifierType,
    'Tool_Specific_Data': cybox_common.ToolSpecificDataType,
    'Execution_Environment': cybox_common.ExecutionEnvironmentType,
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
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Permission_Mode': cybox_common.StringObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Data_Size': cybox_common.DataSizeType,
    'Dependency_Description': cybox_common.StructuredTextType,
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
        rootTag = 'Unix_Pipe'
        rootClass = UnixPipeObjectType
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
        rootTag = 'Unix_Pipe'
        rootClass = UnixPipeObjectType
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
    from six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Unix_Pipe'
        rootClass = UnixPipeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Unix_Pipe",
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
    "UnixPipeObjectType"
    ]
