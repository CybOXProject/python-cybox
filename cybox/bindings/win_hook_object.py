# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import library_object
from . import win_handle_object


class WinHookType(cybox_common.BaseObjectPropertyType):
    """WinHookType specifies Windows hook procedure types, via a union of
    the WinHookTypeEnum type and the atomic xs:string type. Its base
    type is the CybOX Core cybox_common.BaseObjectPropertyType, for permitting
    complex (i.e. regular-expression based) specifications."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(WinHookType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_, )
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if WinHookType.subclass:
            return WinHookType.subclass(*args_, **kwargs_)
        else:
            return WinHookType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(WinHookType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinHookObj:', name_='WinHookType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WinHookType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinHookObj:', name_='WinHookType'):
        super(WinHookType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WinHookType')
    def exportChildren(self, lwrite, level, namespace_='WinHookObj:', name_='WinHookType', fromsubclass_=False, pretty_print=True):
        super(WinHookType, self).exportChildren(lwrite, level, 'WinHookObj:', name_, True, pretty_print=pretty_print)
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
        super(WinHookType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class WinHookType

class WindowsHookObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsHookObjectType type is intended to characterize Windows
    hook procedure objects.For more information please see
    http://msdn.microsoft.com/en-
    us/library/windows/desktop/ms644990(v=vs.85).aspx."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Type=None, Handle=None, Hooking_Function_Name=None, Hooking_Module=None, Thread_ID=None):
        super(WindowsHookObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.Type = Type
        self.Handle = Handle
        self.Hooking_Function_Name = Hooking_Function_Name
        self.Hooking_Module = Hooking_Module
        self.Thread_ID = Thread_ID
    def factory(*args_, **kwargs_):
        if WindowsHookObjectType.subclass:
            return WindowsHookObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsHookObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_WinHookType(self, value):
        # Validate type WinHookType, a restriction on None.
        pass
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_Hooking_Function_Name(self): return self.Hooking_Function_Name
    def set_Hooking_Function_Name(self, Hooking_Function_Name): self.Hooking_Function_Name = Hooking_Function_Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Hooking_Module(self): return self.Hooking_Module
    def set_Hooking_Module(self, Hooking_Module): self.Hooking_Module = Hooking_Module
    def get_Thread_ID(self): return self.Thread_ID
    def set_Thread_ID(self, Thread_ID): self.Thread_ID = Thread_ID
    def validate_NonNegativeIntegerObjectPropertyType(self, value):
        # Validate type cybox_common.NonNegativeIntegerObjectPropertyType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Handle is not None or
            self.Hooking_Function_Name is not None or
            self.Hooking_Module is not None or
            self.Thread_ID is not None or
            super(WindowsHookObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinHookObj:', name_='WindowsHookObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsHookObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinHookObj:', name_='WindowsHookObjectType'):
        super(WindowsHookObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsHookObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinHookObj:', name_='WindowsHookObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsHookObjectType, self).exportChildren(lwrite, level, 'WinHookObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinHookObj:', name_='Type', pretty_print=pretty_print)
        if self.Handle is not None:
            self.Handle.export(lwrite, level, 'WinHookObj:', name_='Handle', pretty_print=pretty_print)
        if self.Hooking_Function_Name is not None:
            self.Hooking_Function_Name.export(lwrite, level, 'WinHookObj:', name_='Hooking_Function_Name', pretty_print=pretty_print)
        if self.Hooking_Module is not None:
            self.Hooking_Module.export(lwrite, level, 'WinHookObj:', name_='Hooking_Module', pretty_print=pretty_print)
        if self.Thread_ID is not None:
            self.Thread_ID.export(lwrite, level, 'WinHookObj:', name_='Thread_ID', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsHookObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = WinHookType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Handle':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_Handle(obj_)
        elif nodeName_ == 'Hooking_Function_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hooking_Function_Name(obj_)
        elif nodeName_ == 'Hooking_Module':
            obj_ = library_object.LibraryObjectType.factory()
            obj_.build(child_)
            self.set_Hooking_Module(obj_)
        elif nodeName_ == 'Thread_ID':
            obj_ = cybox_common.NonNegativeIntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Thread_ID(obj_)
        super(WindowsHookObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsHookObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Byte_Order': cybox_common.EndiannessType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Thread_ID': cybox_common.NonNegativeIntegerObjectPropertyType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Path': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Hooking_Function_Name': cybox_common.StringObjectPropertyType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'English_Translation': cybox_common.StringObjectPropertyType,
    'Start_Date': cybox_common.DateWithPrecisionType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeWithPrecisionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Version': cybox_common.StringObjectPropertyType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': cybox_common.LibraryType,
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
    'Base_Address': cybox_common.HexBinaryObjectPropertyType,
    'Contributors': cybox_common.PersonnelType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Received_Time': cybox_common.DateTimeWithPrecisionType,
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
    'Usage_Context_Assumption': cybox_common.StructuredTextType,
    'Block_Hash': cybox_common.FuzzyHashBlockType,
    'Dependency': cybox_common.DependencyType,
    'Error': cybox_common.ErrorType,
    'ID': cybox_common.UnsignedIntegerObjectPropertyType,
    'Trigger_Point': cybox_common.HexBinaryObjectPropertyType,
    'Environment_Variable': cybox_common.EnvironmentVariableType,
    'Byte_Run': cybox_common.ByteRunType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': library_object.LibraryObjectType,
    'References': cybox_common.ToolReferencesType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Size': cybox_common.UnsignedLongObjectPropertyType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
    'Libraries': cybox_common.LibrariesType,
    'Hooking_Module': library_object.LibraryObjectType,
    'Function': cybox_common.StringObjectPropertyType,
    'Handle': win_handle_object.WindowsHandleObjectType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
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
        rootTag = 'Windows_Hook'
        rootClass = WindowsHookObjectType
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
        rootTag = 'Windows_Hook'
        rootClass = WindowsHookObjectType
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
        rootTag = 'Windows_Hook'
        rootClass = WindowsHookObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="Windows_Hook",
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
    "WindowsHookObjectType",
    "WinHookType"
    ]
