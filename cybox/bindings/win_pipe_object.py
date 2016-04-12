# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import pipe_object
from . import win_handle_object


class WindowsPipeObjectType(pipe_object.PipeObjectType):
    """The WindowsPipeObjectType type is intended to characterize Windows
    pipes."""

    subclass = None
    superclass = pipe_object.PipeObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, named=None, Name=None, Default_Time_Out=None, Handle=None, In_Buffer_Size=None, Max_Instances=None, Open_Mode=None, Out_Buffer_Size=None, Pipe_Mode=None, Security_Attributes=None):
        super(WindowsPipeObjectType, self).__init__(object_reference, Custom_Properties, named, Name, )
        self.Default_Time_Out = Default_Time_Out
        self.Handle = Handle
        self.In_Buffer_Size = In_Buffer_Size
        self.Max_Instances = Max_Instances
        self.Open_Mode = Open_Mode
        self.Out_Buffer_Size = Out_Buffer_Size
        self.Pipe_Mode = Pipe_Mode
        self.Security_Attributes = Security_Attributes
    def factory(*args_, **kwargs_):
        if WindowsPipeObjectType.subclass:
            return WindowsPipeObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsPipeObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Default_Time_Out(self): return self.Default_Time_Out
    def set_Default_Time_Out(self, Default_Time_Out): self.Default_Time_Out = Default_Time_Out
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_In_Buffer_Size(self): return self.In_Buffer_Size
    def set_In_Buffer_Size(self, In_Buffer_Size): self.In_Buffer_Size = In_Buffer_Size
    def get_Max_Instances(self): return self.Max_Instances
    def set_Max_Instances(self, Max_Instances): self.Max_Instances = Max_Instances
    def get_Open_Mode(self): return self.Open_Mode
    def set_Open_Mode(self, Open_Mode): self.Open_Mode = Open_Mode
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Out_Buffer_Size(self): return self.Out_Buffer_Size
    def set_Out_Buffer_Size(self, Out_Buffer_Size): self.Out_Buffer_Size = Out_Buffer_Size
    def get_Pipe_Mode(self): return self.Pipe_Mode
    def set_Pipe_Mode(self, Pipe_Mode): self.Pipe_Mode = Pipe_Mode
    def get_Security_Attributes(self): return self.Security_Attributes
    def set_Security_Attributes(self, Security_Attributes): self.Security_Attributes = Security_Attributes
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Default_Time_Out is not None or
            self.Handle is not None or
            self.In_Buffer_Size is not None or
            self.Max_Instances is not None or
            self.Open_Mode is not None or
            self.Out_Buffer_Size is not None or
            self.Pipe_Mode is not None or
            self.Security_Attributes is not None or
            super(WindowsPipeObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinPipeObj:', name_='WindowsPipeObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsPipeObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinPipeObj:', name_='WindowsPipeObjectType'):
        super(WindowsPipeObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsPipeObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinPipeObj:', name_='WindowsPipeObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsPipeObjectType, self).exportChildren(lwrite, level, 'WinPipeObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Default_Time_Out is not None:
            self.Default_Time_Out.export(lwrite, level, 'WinPipeObj:', name_='Default_Time_Out', pretty_print=pretty_print)
        if self.Handle is not None:
            self.Handle.export(lwrite, level, 'WinPipeObj:', name_='Handle', pretty_print=pretty_print)
        if self.In_Buffer_Size is not None:
            self.In_Buffer_Size.export(lwrite, level, 'WinPipeObj:', name_='In_Buffer_Size', pretty_print=pretty_print)
        if self.Max_Instances is not None:
            self.Max_Instances.export(lwrite, level, 'WinPipeObj:', name_='Max_Instances', pretty_print=pretty_print)
        if self.Open_Mode is not None:
            self.Open_Mode.export(lwrite, level, 'WinPipeObj:', name_='Open_Mode', pretty_print=pretty_print)
        if self.Out_Buffer_Size is not None:
            self.Out_Buffer_Size.export(lwrite, level, 'WinPipeObj:', name_='Out_Buffer_Size', pretty_print=pretty_print)
        if self.Pipe_Mode is not None:
            self.Pipe_Mode.export(lwrite, level, 'WinPipeObj:', name_='Pipe_Mode', pretty_print=pretty_print)
        if self.Security_Attributes is not None:
            self.Security_Attributes.export(lwrite, level, 'WinPipeObj:', name_='Security_Attributes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsPipeObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Default_Time_Out':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Default_Time_Out(obj_)
        elif nodeName_ == 'Handle':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_Handle(obj_)
        elif nodeName_ == 'In_Buffer_Size':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_In_Buffer_Size(obj_)
        elif nodeName_ == 'Max_Instances':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Max_Instances(obj_)
        elif nodeName_ == 'Open_Mode':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Open_Mode(obj_)
        elif nodeName_ == 'Out_Buffer_Size':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Out_Buffer_Size(obj_)
        elif nodeName_ == 'Pipe_Mode':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Pipe_Mode(obj_)
        elif nodeName_ == 'Security_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_Attributes(obj_)
        super(WindowsPipeObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsPipeObjectType

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
    'Pipe': pipe_object.PipeObjectType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Security_Attributes': cybox_common.StringObjectPropertyType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
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
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Default_Time_Out': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Open_Mode': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Access_Mask': cybox_common.UnsignedLongObjectPropertyType,
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
    'Max_Instances': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'In_Buffer_Size': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'Contributors': cybox_common.PersonnelType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Out_Buffer_Size': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Pipe_Mode': cybox_common.HexBinaryObjectPropertyType,
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
        rootTag = 'Windows_Pipe'
        rootClass = WindowsPipeObjectType
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
        rootTag = 'Windows_Pipe'
        rootClass = WindowsPipeObjectType
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
        rootTag = 'Windows_Pipe'
        rootClass = WindowsPipeObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="Windows_Pipe",
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
    "WindowsPipeObjectType"
    ]
