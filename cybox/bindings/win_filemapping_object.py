# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import win_handle_object


class PageProtectionAttributeType(cybox_common.BaseObjectPropertyType):
    """The PageProtectionValueType specifies the optional Windows file
    mapping page protection attribute types (i.e. SEC_) via a union
    of the PageProtectionAttributeEnum type and the atomic xs:string
    type. Its base type is the CybOX Core cybox_common.BaseObjectPropertyType,
    for permitting complex (i.e. regular-expression based)
    specifications."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(PageProtectionAttributeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PageProtectionAttributeType.subclass:
            return PageProtectionAttributeType.subclass(*args_, **kwargs_)
        else:
            return PageProtectionAttributeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PageProtectionAttributeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFilemappingObj:', name_='PageProtectionAttributeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PageProtectionAttributeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFilemappingObj:', name_='PageProtectionAttributeType'):
        super(PageProtectionAttributeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PageProtectionAttributeType')
    def exportChildren(self, lwrite, level, namespace_='WinFilemappingObj:', name_='PageProtectionAttributeType', fromsubclass_=False, pretty_print=True):
        super(PageProtectionAttributeType, self).exportChildren(lwrite, level, 'WinFilemappingObj:', name_, True, pretty_print=pretty_print)
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
        super(PageProtectionAttributeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PageProtectionAttributeType

class PageProtectionValueType(cybox_common.BaseObjectPropertyType):
    """The PageProtectionValueType specifies Windows file mapping page
    protection value types (i.e. PAGE_) via a union of the
    PageProtectionValueEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications."""
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(PageProtectionValueType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if PageProtectionValueType.subclass:
            return PageProtectionValueType.subclass(*args_, **kwargs_)
        else:
            return PageProtectionValueType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(PageProtectionValueType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFilemappingObj:', name_='PageProtectionValueType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PageProtectionValueType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFilemappingObj:', name_='PageProtectionValueType'):
        super(PageProtectionValueType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PageProtectionValueType')
    def exportChildren(self, lwrite, level, namespace_='WinFilemappingObj:', name_='PageProtectionValueType', fromsubclass_=False, pretty_print=True):
        super(PageProtectionValueType, self).exportChildren(lwrite, level, 'WinFilemappingObj:', name_, True, pretty_print=pretty_print)
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
        super(PageProtectionValueType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PageProtectionValueType

class WindowsFilemappingObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsFilemappingObjectType type is intended to characterize
    Windows file mapping objects."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Name=None, File_Handle=None, Handle=None, Page_Protection_Value=None, Page_Protection_Attribute=None, Maximum_Size=None, Actual_Size=None, Security_Attributes=None):
        super(WindowsFilemappingObjectType, self).__init__(object_reference, Custom_Properties, xsi_type)
        self.Name = Name
        self.File_Handle = File_Handle
        self.Handle = Handle
        self.Page_Protection_Value = Page_Protection_Value
        if Page_Protection_Attribute is None:
            self.Page_Protection_Attribute = []
        else:
            self.Page_Protection_Attribute = Page_Protection_Attribute
        self.Maximum_Size = Maximum_Size
        self.Actual_Size = Actual_Size
        self.Security_Attributes = Security_Attributes
    def factory(*args_, **kwargs_):
        if WindowsFilemappingObjectType.subclass:
            return WindowsFilemappingObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsFilemappingObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_File_Handle(self): return self.File_Handle
    def set_File_Handle(self, File_Handle): self.File_Handle = File_Handle
    def get_Handle(self): return self.Handle
    def set_Handle(self, Handle): self.Handle = Handle
    def get_Page_Protection_Value(self): return self.Page_Protection_Value
    def set_Page_Protection_Value(self, Page_Protection_Value): self.Page_Protection_Value = Page_Protection_Value
    def validate_PageProtectionValueType(self, value):
        # Validate type PageProtectionValueType, a restriction on None.
        pass
    def get_Page_Protection_Attribute(self): return self.Page_Protection_Attribute
    def set_Page_Protection_Attribute(self, Page_Protection_Attribute): self.Page_Protection_Attribute = Page_Protection_Attribute
    def add_Page_Protection_Attribute(self, value): self.Page_Protection_Attribute.append(value)
    def insert_Page_Protection_Attribute(self, index, value): self.Page_Protection_Attribute[index] = value
    def validate_PageProtectionAttributeType(self, value):
        # Validate type PageProtectionAttributeType, a restriction on None.
        pass
    def get_Maximum_Size(self): return self.Maximum_Size
    def set_Maximum_Size(self, Maximum_Size): self.Maximum_Size = Maximum_Size
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Actual_Size(self): return self.Actual_Size
    def set_Actual_Size(self, Actual_Size): self.Actual_Size = Actual_Size
    def get_Security_Attributes(self): return self.Security_Attributes
    def set_Security_Attributes(self, Security_Attributes): self.Security_Attributes = Security_Attributes
    def hasContent_(self):
        if (
            self.Name is not None or
            self.File_Handle is not None or
            self.Handle is not None or
            self.Page_Protection_Value is not None or
            self.Page_Protection_Attribute or
            self.Maximum_Size is not None or
            self.Actual_Size is not None or
            self.Security_Attributes is not None or
            super(WindowsFilemappingObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinFilemappingObj:', name_='WindowsFilemappingObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFilemappingObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinFilemappingObj:', name_='WindowsFilemappingObjectType'):
        super(WindowsFilemappingObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsFilemappingObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinFilemappingObj:', name_='WindowsFilemappingObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsFilemappingObjectType, self).exportChildren(lwrite, level, 'WinFilemappingObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            self.Name.export(lwrite, level, 'WinFilemappingObj:', name_='Name', pretty_print=pretty_print)
        if self.File_Handle is not None:
            self.File_Handle.export(lwrite, level, 'WinFilemappingObj:', name_='File_Handle', pretty_print=pretty_print)
        if self.Handle is not None:
            self.Handle.export(lwrite, level, 'WinFilemappingObj:', name_='Handle', pretty_print=pretty_print)
        if self.Page_Protection_Value is not None:
            self.Page_Protection_Value.export(lwrite, level, 'WinFilemappingObj:', name_='Page_Protection_Value', pretty_print=pretty_print)
        for Page_Protection_Attribute_ in self.Page_Protection_Attribute:
            Page_Protection_Attribute_.export(lwrite, level, 'WinFilemappingObj:', name_='Page_Protection_Attribute', pretty_print=pretty_print)
        if self.Maximum_Size is not None:
            self.Maximum_Size.export(lwrite, level, 'WinFilemappingObj:', name_='Maximum_Size', pretty_print=pretty_print)
        if self.Actual_Size is not None:
            self.Actual_Size.export(lwrite, level, 'WinFilemappingObj:', name_='Actual_Size', pretty_print=pretty_print)
        if self.Security_Attributes is not None:
            self.Security_Attributes.export(lwrite, level, 'WinFilemappingObj:', name_='Security_Attributes', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsFilemappingObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'File_Handle':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_File_Handle(obj_)
        elif nodeName_ == 'Handle':
            obj_ = win_handle_object.WindowsHandleObjectType.factory()
            obj_.build(child_)
            self.set_Handle(obj_)
        elif nodeName_ == 'Page_Protection_Value':
            obj_ = PageProtectionValueType.factory()
            obj_.build(child_)
            self.set_Page_Protection_Value(obj_)
        elif nodeName_ == 'Page_Protection_Attribute':
            obj_ = PageProtectionAttributeType.factory()
            obj_.build(child_)
            self.Page_Protection_Attribute.append(obj_)
        elif nodeName_ == 'Maximum_Size':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Maximum_Size(obj_)
        elif nodeName_ == 'Actual_Size':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Actual_Size(obj_)
        elif nodeName_ == 'Security_Attributes':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Security_Attributes(obj_)
        super(WindowsFilemappingObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsFilemappingObjectType

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
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Produced_Time': cybox_common.DateTimeWithPrecisionType,
    'Actual_Size': cybox_common.UnsignedLongObjectPropertyType,
    'Reference': cybox_common.ToolReferenceType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Security_Attributes': cybox_common.StringObjectPropertyType,
    'Object_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Compiler': cybox_common.CompilerType,
    'Start_Date': cybox_common.DateWithPrecisionType,
    'Functions': cybox_common.FunctionsType,
    'String_Value': cybox_common.StringObjectPropertyType,
    'Pointer_Count': cybox_common.UnsignedLongObjectPropertyType,
    'Build_Utility_Platform_Specification': cybox_common.PlatformSpecificationType,
    'Compiler_Informal_Description': cybox_common.CompilerInformalDescriptionType,
    'Start_Time': cybox_common.DateTimeWithPrecisionType,
    'System': cybox_common.ObjectPropertiesType,
    'Platform': cybox_common.PlatformSpecificationType,
    'Usage_Context_Assumptions': cybox_common.UsageContextAssumptionsType,
    'Type': win_handle_object.HandleType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
    'String': cybox_common.ExtractedStringType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Maximum_Size': cybox_common.UnsignedLongObjectPropertyType,
    'Observable_Location': cybox_common.LocationType,
    'Error_Instances': cybox_common.ErrorInstancesType,
    'End_Date': cybox_common.DateWithPrecisionType,
    'Data_Segment': cybox_common.StringObjectPropertyType,
    'Certificate_Subject': cybox_common.StringObjectPropertyType,
    'Compensation_Model': cybox_common.CompensationModelType,
    'Property': cybox_common.PropertyType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_Handle': win_handle_object.WindowsHandleObjectType,
    'Contributors': cybox_common.PersonnelType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
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
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Windows_Handle': win_handle_object.WindowsHandleObjectType,
    'Compilation_Date': cybox_common.DateTimeWithPrecisionType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Observation_Location': cybox_common.LocationType,
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
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
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
        rootTag = 'Windows_Filemapping'
        rootClass = WindowsFilemappingObjectType
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
        rootTag = 'Windows_Filemapping'
        rootClass = WindowsFilemappingObjectType
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
        rootTag = 'Windows_Filemapping'
        rootClass = WindowsFilemappingObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout.write, 0, name_="Windows_Filemapping",
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
    "WindowsFilemappingObjectType",
    "PageProtectionValueType",
    "PageProtectionAttributeType"
    ]
