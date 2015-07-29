# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common
from . import memory_object


class MemoryPageTypeType(cybox_common.BaseObjectPropertyType):
    """MemoryPageTypeType specifies memory protection type, via a union of
    the MemoryPageTypeEnum type and the atomic xs:string type. Its
    base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(MemoryPageTypeType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if MemoryPageTypeType.subclass:
            return MemoryPageTypeType.subclass(*args_, **kwargs_)
        else:
            return MemoryPageTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(MemoryPageTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageTypeType'):
        super(MemoryPageTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageTypeType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageTypeType', fromsubclass_=False, pretty_print=True):
        super(MemoryPageTypeType, self).exportChildren(lwrite, level, 'WinMemoryPageRegionObj:', name_, True, pretty_print=pretty_print)
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
        super(MemoryPageTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MemoryPageTypeType

class MemoryPageStateType(cybox_common.BaseObjectPropertyType):
    """MemoryPageStateType specifies memory protection states, via a union
    of the MemoryPageStateEnum type and the atomic xs:string type.
    Its base type is the CybOX Core cybox_common.BaseObjectPropertyType, for
    permitting complex (i.e. regular-expression based)
    specifications.This attribute is optional and specifies the
    expected type for the value of the specified property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(MemoryPageStateType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if MemoryPageStateType.subclass:
            return MemoryPageStateType.subclass(*args_, **kwargs_)
        else:
            return MemoryPageStateType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(MemoryPageStateType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageStateType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageStateType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageStateType'):
        super(MemoryPageStateType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageStateType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageStateType', fromsubclass_=False, pretty_print=True):
        super(MemoryPageStateType, self).exportChildren(lwrite, level, 'WinMemoryPageRegionObj:', name_, True, pretty_print=pretty_print)
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
        super(MemoryPageStateType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MemoryPageStateType

class MemoryPageProtectionType(cybox_common.BaseObjectPropertyType):
    """MemoryPageProtectionType specifies memory protection constant types,
    via a union of the MemoryPageProtectionEnum type and the atomic
    xs:string type. Its base type is the CybOX Core
    cybox_common.BaseObjectPropertyType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    property."""

    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(MemoryPageProtectionType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if MemoryPageProtectionType.subclass:
            return MemoryPageProtectionType.subclass(*args_, **kwargs_)
        else:
            return MemoryPageProtectionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(MemoryPageProtectionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageProtectionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageProtectionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageProtectionType'):
        super(MemoryPageProtectionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryPageProtectionType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='MemoryPageProtectionType', fromsubclass_=False, pretty_print=True):
        super(MemoryPageProtectionType, self).exportChildren(lwrite, level, 'WinMemoryPageRegionObj:', name_, True, pretty_print=pretty_print)
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
        super(MemoryPageProtectionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MemoryPageProtectionType

class WindowsMemoryPageRegionObjectType(memory_object.MemoryObjectType):
    """The WindowsMemoryPageRegionObjectType type is intended to
    characterize Windows memory page regions."""

    subclass = None
    superclass = memory_object.MemoryObjectType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_protected=None, is_injected=None, is_mapped=None, Hashes=None, Name=None, Region_Size=None, Region_Start_Address=None, Extracted_Features=None, Type=None, Allocation_Base_Address=None, Allocation_Protect=None, State=None, Protect=None):
        super(WindowsMemoryPageRegionObjectType, self).__init__(object_reference, Custom_Properties, is_protected, is_injected, is_mapped, Hashes, Name, Region_Size, Region_Start_Address, Extracted_Features, )
        self.Type = Type
        self.Allocation_Base_Address = Allocation_Base_Address
        self.Allocation_Protect = Allocation_Protect
        self.State = State
        self.Protect = Protect
    def factory(*args_, **kwargs_):
        if WindowsMemoryPageRegionObjectType.subclass:
            return WindowsMemoryPageRegionObjectType.subclass(*args_, **kwargs_)
        else:
            return WindowsMemoryPageRegionObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_MemoryPageTypeType(self, value):
        # Validate type MemoryPageTypeType, a restriction on None.
        pass
    def get_Allocation_Base_Address(self): return self.Allocation_Base_Address
    def set_Allocation_Base_Address(self, Allocation_Base_Address): self.Allocation_Base_Address = Allocation_Base_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Allocation_Protect(self): return self.Allocation_Protect
    def set_Allocation_Protect(self, Allocation_Protect): self.Allocation_Protect = Allocation_Protect
    def validate_MemoryPageProtectionType(self, value):
        # Validate type MemoryPageProtectionType, a restriction on None.
        pass
    def get_State(self): return self.State
    def set_State(self, State): self.State = State
    def validate_MemoryPageStateType(self, value):
        # Validate type MemoryPageStateType, a restriction on None.
        pass
    def get_Protect(self): return self.Protect
    def set_Protect(self, Protect): self.Protect = Protect
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Allocation_Base_Address is not None or
            self.Allocation_Protect is not None or
            self.State is not None or
            self.Protect is not None or
            super(WindowsMemoryPageRegionObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='WindowsMemoryPageRegionObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsMemoryPageRegionObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='WinMemoryPageRegionObj:', name_='WindowsMemoryPageRegionObjectType'):
        super(WindowsMemoryPageRegionObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='WindowsMemoryPageRegionObjectType')
    def exportChildren(self, lwrite, level, namespace_='WinMemoryPageRegionObj:', name_='WindowsMemoryPageRegionObjectType', fromsubclass_=False, pretty_print=True):
        super(WindowsMemoryPageRegionObjectType, self).exportChildren(lwrite, level, 'WinMemoryPageRegionObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, 'WinMemoryPageRegionObj:', name_='Type', pretty_print=pretty_print)
        if self.Allocation_Base_Address is not None:
            self.Allocation_Base_Address.export(lwrite, level, 'WinMemoryPageRegionObj:', name_='Allocation_Base_Address', pretty_print=pretty_print)
        if self.Allocation_Protect is not None:
            self.Allocation_Protect.export(lwrite, level, 'WinMemoryPageRegionObj:', name_='Allocation_Protect', pretty_print=pretty_print)
        if self.State is not None:
            self.State.export(lwrite, level, 'WinMemoryPageRegionObj:', name_='State', pretty_print=pretty_print)
        if self.Protect is not None:
            self.Protect.export(lwrite, level, 'WinMemoryPageRegionObj:', name_='Protect', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(WindowsMemoryPageRegionObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = MemoryPageTypeType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Allocation_Base_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Allocation_Base_Address(obj_)
        elif nodeName_ == 'Allocation_Protect':
            obj_ = MemoryPageProtectionType.factory()
            obj_.build(child_)
            self.set_Allocation_Protect(obj_)
        elif nodeName_ == 'State':
            obj_ = MemoryPageStateType.factory()
            obj_.build(child_)
            self.set_State(obj_)
        elif nodeName_ == 'Protect':
            obj_ = MemoryPageProtectionType.factory()
            obj_.build(child_)
            self.set_Protect(obj_)
        super(WindowsMemoryPageRegionObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class WindowsMemoryPageRegionObjectType

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
    'Region_Start_Address': cybox_common.HexBinaryObjectPropertyType,
    'Code_Snippets': cybox_common.CodeSnippetsType,
    'Allocation_Base_Address': cybox_common.HexBinaryObjectPropertyType,
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Memory_Region': memory_object.MemoryObjectType,
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
    'Tool': cybox_common.ToolInformationType,
    'Build_Information': cybox_common.BuildInformationType,
    'Tool_Hashes': cybox_common.HashListType,
    'Compiler_Platform_Specification': cybox_common.PlatformSpecificationType,
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
    'Contributors': cybox_common.PersonnelType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
    'Description': cybox_common.StructuredTextType,
    'User_Account_Info': cybox_common.ObjectPropertiesType,
    'Build_Configuration': cybox_common.BuildConfigurationType,
    'Extracted_Features': cybox_common.ExtractedFeaturesType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
    'Region_Size': cybox_common.UnsignedLongObjectPropertyType,
    'Fuzzy_Hash_Value': cybox_common.FuzzyHashValueType,
    'Dependency_Description': cybox_common.StructuredTextType,
    'Contributor': cybox_common.ContributorType,
    'Tools': cybox_common.ToolsInformationType,
    'Data_Size': cybox_common.DataSizeType,
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
        rootTag = 'Windows_Memory_Page_Region'
        rootClass = WindowsMemoryPageRegionObjectType
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
        rootTag = 'Windows_Memory_Page_Region'
        rootClass = WindowsMemoryPageRegionObjectType
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
        rootTag = 'Windows_Memory_Page_Region'
        rootClass = WindowsMemoryPageRegionObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Windows_Memory_Page_Region",
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
    "WindowsMemoryPageRegionObjectType",
    "MemoryPageProtectionType",
    "MemoryPageStateType",
    "MemoryPageTypeType"
    ]
