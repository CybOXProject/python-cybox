# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class KernelHookType(cybox_common.BaseObjectPropertyType):
    """KernelHookType specifies Windows kernel hook types via a union of
    the KernelHookTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(KernelHookType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if KernelHookType.subclass:
            return KernelHookType.subclass(*args_, **kwargs_)
        else:
            return KernelHookType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(KernelHookType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelHookObj:', name_='KernelHookType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KernelHookType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelHookObj:', name_='KernelHookType'):
        super(KernelHookType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='KernelHookType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinKernelHookObj:', name_='KernelHookType', fromsubclass_=False, pretty_print=True):
        super(KernelHookType, self).exportChildren(lwrite, level, 'WinKernelHookObj:', name_, True, pretty_print=pretty_print)
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
        super(KernelHookType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class KernelHookType

class WindowsKernelHookObjectType(cybox_common.ObjectPropertiesType):
    """The WindowsKernelHookObjectType type is intended to characterize
    Windows kernel function hooks."""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, Digital_Signature_Hooking=None, Digital_Signature_Hooked=None, Hooking_Address=None, Hook_Description=None, Hooked_Function=None, Hooked_Module=None, Hooking_Module=None, Type=None):
        super(WindowsKernelHookObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.Digital_Signature_Hooking = Digital_Signature_Hooking
        self.Digital_Signature_Hooked = Digital_Signature_Hooked
        self.Hooking_Address = Hooking_Address
        self.Hook_Description = Hook_Description
        self.Hooked_Function = Hooked_Function
        self.Hooked_Module = Hooked_Module
        self.Hooking_Module = Hooking_Module
        self.Type = Type
    def factory(*args_, **kwargs_):
        if WindowsKernelHookObjectType.subclass:
            return WindowsKernelHookObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsKernelHookObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Digital_Signature_Hooking(self): return self.Digital_Signature_Hooking
    def set_Digital_Signature_Hooking(self, Digital_Signature_Hooking): self.Digital_Signature_Hooking = Digital_Signature_Hooking
    def get_Digital_Signature_Hooked(self): return self.Digital_Signature_Hooked
    def set_Digital_Signature_Hooked(self, Digital_Signature_Hooked): self.Digital_Signature_Hooked = Digital_Signature_Hooked
    def get_Hooking_Address(self): return self.Hooking_Address
    def set_Hooking_Address(self, Hooking_Address): self.Hooking_Address = Hooking_Address
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Hook_Description(self): return self.Hook_Description
    def set_Hook_Description(self, Hook_Description): self.Hook_Description = Hook_Description
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Hooked_Function(self): return self.Hooked_Function
    def set_Hooked_Function(self, Hooked_Function): self.Hooked_Function = Hooked_Function
    def get_Hooked_Module(self): return self.Hooked_Module
    def set_Hooked_Module(self, Hooked_Module): self.Hooked_Module = Hooked_Module
    def get_Hooking_Module(self): return self.Hooking_Module
    def set_Hooking_Module(self, Hooking_Module): self.Hooking_Module = Hooking_Module
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_KernelHookType(self, value):
        # Validate type KernelHookType, a restriction on None.
        pass
    def hasContent_(self):
        if (
            self.Digital_Signature_Hooking is not None or
            self.Digital_Signature_Hooked is not None or
            self.Hooking_Address is not None or
            self.Hook_Description is not None or
            self.Hooked_Function is not None or
            self.Hooked_Module is not None or
            self.Hooking_Module is not None or
            self.Type is not None or
            super(WindowsKernelHookObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinKernelHookObj:', name_='WindowsKernelHookObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsKernelHookObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinKernelHookObj:', name_='WindowsKernelHookObjectType'):
        super(WindowsKernelHookObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsKernelHookObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinKernelHookObj:', name_='WindowsKernelHookObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsKernelHookObjectType, self).exportChildren(lwrite, level, 'WinKernelHookObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Digital_Signature_Hooking is not None:
            self.Digital_Signature_Hooking.export(lwrite, level, 'WinKernelHookObj:', name_='Digital_Signature_Hooking', pretty_print=pretty_print)
        if self.Digital_Signature_Hooked is not None:
            self.Digital_Signature_Hooked.export(lwrite, level, 'WinKernelHookObj:', name_='Digital_Signature_Hooked', pretty_print=pretty_print)
        if self.Hooking_Address is not None:
            self.Hooking_Address.export(lwrite, level, 'WinKernelHookObj:', name_='Hooking_Address', pretty_print=pretty_print)
        if self.Hook_Description is not None:
            self.Hook_Description.export(lwrite, level, 'WinKernelHookObj:', name_='Hook_Description', pretty_print=pretty_print)
        if self.Hooked_Function is not None:
            self.Hooked_Function.export(lwrite, level, 'WinKernelHookObj:', name_='Hooked_Function', pretty_print=pretty_print)
        if self.Hooked_Module is not None:
            self.Hooked_Module.export(lwrite, level, 'WinKernelHookObj:', name_='Hooked_Module', pretty_print=pretty_print)
        if self.Hooking_Module is not None:
            self.Hooking_Module.export(lwrite, level, 'WinKernelHookObj:', name_='Hooking_Module', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinKernelHookObj:', name_='Type', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsKernelHookObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Digital_Signature_Hooking':
            obj_ = cybox_common.DigitalSignatureInfoType.factory()
            obj_.build(child_)
            self.set_Digital_Signature_Hooking(obj_)
        elif nodeName_ == 'Digital_Signature_Hooked':
            obj_ = cybox_common.DigitalSignatureInfoType.factory()
            obj_.build(child_)
            self.set_Digital_Signature_Hooked(obj_)
        elif nodeName_ == 'Hooking_Address':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hooking_Address(obj_)
        elif nodeName_ == 'Hook_Description':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hook_Description(obj_)
        elif nodeName_ == 'Hooked_Function':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hooked_Function(obj_)
        elif nodeName_ == 'Hooked_Module':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hooked_Module(obj_)
        elif nodeName_ == 'Hooking_Module':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Hooking_Module(obj_)
        elif nodeName_ == 'Type':
            obj_ = KernelHookType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(WindowsKernelHookObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsKernelHookObjectType

GDSClassesMapping = {
    'Build_Utility': cybox_common.BuildUtilityType,
    'Errors': cybox_common.ErrorsType,
    'Time': cybox_common.TimeType,
    'Certificate_Issuer': cybox_common.StringObjectPropertyType,
    'Metadata': cybox_common.MetadataType,
    'Hash': cybox_common.HashType,
    'Digital_Signature_Hooking': cybox_common.DigitalSignatureInfoType,
    'Information_Source_Type': cybox_common.ControlledVocabularyStringType,
    'Block_Hash_Value': cybox_common.HashValueType,
    'Fuzzy_Hash_Structure': cybox_common.FuzzyHashStructureType,
    'SubDatum': cybox_common.MetadataType,
    'Segment_Hash': cybox_common.HashValueType,
    'Digital_Signature': cybox_common.DigitalSignatureInfoType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Hooked_Module': cybox_common.StringObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
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
    'Hooked_Function': cybox_common.StringObjectPropertyType,
    'Compilers': cybox_common.CompilersType,
    'Tool_Type': cybox_common.ControlledVocabularyStringType,
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
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
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
    'Hook_Description': cybox_common.StringObjectPropertyType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Hooking_Module': cybox_common.StringObjectPropertyType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Hooking_Address': cybox_common.UnsignedLongObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Digital_Signature_Hooked': cybox_common.DigitalSignatureInfoType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Windows_Kernel_Hook'
        rootClass = WindowsKernelHookObjectType
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
        rootTag = 'Windows_Kernel_Hook'
        rootClass = WindowsKernelHookObjectType
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
        rootTag = 'Windows_Kernel_Hook'
        rootClass = WindowsKernelHookObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Kernel_Hook",
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
    "WindowsKernelHookObjectType",
    "KernelHookType"
    ]
