# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class BlockType(cybox_common.BaseObjectPropertyType):
    """BlockType specifies memory block types, via a union of the
    BlockTypeEnum type and the atomic xs:string type. Its base type
    is the CybOX Core BaseObjectPropertyType, for permitting complex
    (i.e. regular-expression based) specifications.This attribute is
    optional and specifies the expected type for the value of the
    specified property."""
    subclass = None
    superclass = cybox_common.BaseObjectPropertyType
    def __init__(self, obfuscation_algorithm_ref=None, refanging_transform_type=None, has_changed=None, delimiter='##comma##', pattern_type=None, datatype='string', refanging_transform=None, is_case_sensitive=True, bit_mask=None, appears_random=None, observed_encoding=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, apply_condition='ANY', trend=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(BlockType, self).__init__(obfuscation_algorithm_ref, refanging_transform_type, has_changed, delimiter, pattern_type, datatype, refanging_transform, is_case_sensitive, bit_mask, appears_random, observed_encoding, defanging_algorithm_ref, is_obfuscated, regex_syntax, apply_condition, trend, idref, is_defanged, id, condition, valueOf_)
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if BlockType.subclass:
            return BlockType.subclass(*args_, **kwargs_)
        else:
            return BlockType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(BlockType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='MemoryObj:', name_='BlockType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BlockType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='MemoryObj:', name_='BlockType'):
        super(BlockType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='BlockType')
        if self.datatype is not None:

            lwrite(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, lwrite, level, namespace_='MemoryObj:', name_='BlockType', fromsubclass_=False, pretty_print=True):
        super(BlockType, self).exportChildren(lwrite, level, namespace_, name_, True, pretty_print=pretty_print)
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
        super(BlockType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class BlockType

class MemoryObjectType(cybox_common.ObjectPropertiesType):
    """The MemoryObjectType type is intended to characterize generic memory
    objects.The is_injected field specifies whether or not the
    particular memory object has had data/code injected into it by
    another process.The is_mapped field specifies whether or not the
    particular memory object has been assigned a byte-for-byte
    correlation with some portion of a file or file-like
    resource.The is_protected field specifies whether or not the
    particular memory object is protected (read/write only from the
    process that allocated it).The is_volatile field specifies
    whether or not the particular memory object is volatile."""
    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, is_volatile=None, is_protected=None, is_injected=None, is_mapped=None, Hashes=None, Name=None, Memory_Source=None, Region_Size=None, Block_Type=None, Region_Start_Address=None, Region_End_Address=None, Extracted_Features=None):
        super(MemoryObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.is_volatile = _cast(bool, is_volatile)
        self.is_protected = _cast(bool, is_protected)
        self.is_injected = _cast(bool, is_injected)
        self.is_mapped = _cast(bool, is_mapped)
        self.Hashes = Hashes
        self.Name = Name
        self.Memory_Source = Memory_Source
        self.Region_Size = Region_Size
        self.Block_Type = Block_Type
        self.Region_Start_Address = Region_Start_Address
        self.Region_End_Address = Region_End_Address
        self.Extracted_Features = Extracted_Features
    def factory(*args_, **kwargs_):
        if MemoryObjectType.subclass:
            return MemoryObjectType.subclass(*args_, **kwargs_)
        else:
            return MemoryObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Hashes(self): return self.Hashes
    def set_Hashes(self, Hashes): self.Hashes = Hashes
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_Memory_Source(self): return self.Memory_Source
    def set_Memory_Source(self, Memory_Source): self.Memory_Source = Memory_Source
    def get_Region_Size(self): return self.Region_Size
    def set_Region_Size(self, Region_Size): self.Region_Size = Region_Size
    def validate_UnsignedLongObjectPropertyType(self, value):
        # Validate type cybox_common.UnsignedLongObjectPropertyType, a restriction on None.
        pass
    def get_Block_Type(self): return self.Block_Type
    def set_Block_Type(self, Block_Type): self.Block_Type = Block_Type
    def validate_BlockType(self, value):
        # Validate type BlockType, a restriction on None.
        pass
    def get_Region_Start_Address(self): return self.Region_Start_Address
    def set_Region_Start_Address(self, Region_Start_Address): self.Region_Start_Address = Region_Start_Address
    def validate_HexBinaryObjectPropertyType(self, value):
        # Validate type cybox_common.HexBinaryObjectPropertyType, a restriction on None.
        pass
    def get_Region_End_Address(self): return self.Region_End_Address
    def set_Region_End_Address(self, Region_End_Address): self.Region_End_Address = Region_End_Address
    def get_Extracted_Features(self): return self.Extracted_Features
    def set_Extracted_Features(self, Extracted_Features): self.Extracted_Features = Extracted_Features
    def get_is_volatile(self): return self.is_volatile
    def set_is_volatile(self, is_volatile): self.is_volatile = is_volatile
    def get_is_protected(self): return self.is_protected
    def set_is_protected(self, is_protected): self.is_protected = is_protected
    def get_is_injected(self): return self.is_injected
    def set_is_injected(self, is_injected): self.is_injected = is_injected
    def get_is_mapped(self): return self.is_mapped
    def set_is_mapped(self, is_mapped): self.is_mapped = is_mapped
    def hasContent_(self):
        if (
            self.Hashes is not None or
            self.Name is not None or
            self.Memory_Source is not None or
            self.Region_Size is not None or
            self.Block_Type is not None or
            self.Region_Start_Address is not None or
            self.Region_End_Address is not None or
            self.Extracted_Features is not None or
            super(MemoryObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='MemoryObj:', name_='MemoryObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='MemoryObj:', name_='MemoryObjectType'):
        super(MemoryObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='MemoryObjectType')
        if self.is_volatile is not None:

            lwrite(' is_volatile="%s"' % self.gds_format_boolean(self.is_volatile, input_name='is_volatile'))
        if self.is_protected is not None:

            lwrite(' is_protected="%s"' % self.gds_format_boolean(self.is_protected, input_name='is_protected'))
        if self.is_injected is not None:

            lwrite(' is_injected="%s"' % self.gds_format_boolean(self.is_injected, input_name='is_injected'))
        if self.is_mapped is not None:

            lwrite(' is_mapped="%s"' % self.gds_format_boolean(self.is_mapped, input_name='is_mapped'))
    def exportChildren(self, lwrite, level, namespace_='MemoryObj:', name_='MemoryObjectType', fromsubclass_=False, pretty_print=True):
        super(MemoryObjectType, self).exportChildren(lwrite, level, 'MemoryObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Hashes is not None:
            self.Hashes.export(lwrite, level, 'MemoryObj:', name_='Hashes', pretty_print=pretty_print)
        if self.Name is not None:
            self.Name.export(lwrite, level, 'MemoryObj:', name_='Name', pretty_print=pretty_print)
        if self.Memory_Source is not None:
            self.Memory_Source.export(lwrite, level, 'MemoryObj:', name_='Memory_Source', pretty_print=pretty_print)
        if self.Region_Size is not None:
            self.Region_Size.export(lwrite, level, 'MemoryObj:', name_='Region_Size', pretty_print=pretty_print)
        if self.Block_Type is not None:
            self.Block_Type.export(lwrite, level, 'MemoryObj:', name_='Block_Type', pretty_print=pretty_print)
        if self.Region_Start_Address is not None:
            self.Region_Start_Address.export(lwrite, level, 'MemoryObj:', name_='Region_Start_Address', pretty_print=pretty_print)
        if self.Region_End_Address is not None:
            self.Region_End_Address.export(lwrite, level, 'MemoryObj:', name_='Region_End_Address', pretty_print=pretty_print)
        if self.Extracted_Features is not None:
            self.Extracted_Features.export(lwrite, level, 'MemoryObj:', name_='Extracted_Features', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('is_volatile', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_volatile = True
            elif value in ('false', '0'):
                self.is_volatile = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_protected', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_protected = True
            elif value in ('false', '0'):
                self.is_protected = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_injected', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_injected = True
            elif value in ('false', '0'):
                self.is_injected = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_mapped', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_mapped = True
            elif value in ('false', '0'):
                self.is_mapped = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(MemoryObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Hashes':
            obj_ = cybox_common.HashListType.factory()
            obj_.build(child_)
            self.set_Hashes(obj_)
        elif nodeName_ == 'Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Name(obj_)
        elif nodeName_ == 'Memory_Source':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Memory_Source(obj_)
        elif nodeName_ == 'Region_Size':
            obj_ = cybox_common.UnsignedLongObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Region_Size(obj_)
        elif nodeName_ == 'Block_Type':
            obj_ = BlockType.factory()
            obj_.build(child_)
            self.set_Block_Type(obj_)
        elif nodeName_ == 'Region_Start_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Region_Start_Address(obj_)
        elif nodeName_ == 'Region_End_Address':
            obj_ = cybox_common.HexBinaryObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Region_End_Address(obj_)
        elif nodeName_ == 'Extracted_Features':
            obj_ = cybox_common.ExtractedFeaturesType.factory()
            obj_.build(child_)
            self.set_Extracted_Features(obj_)
        super(MemoryObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class MemoryObjectType

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
    'Value': cybox_common.StringObjectPropertyType,
    'Length': cybox_common.IntegerObjectPropertyType,
    'Encoding': cybox_common.ControlledVocabularyStringType,
    'Internationalization_Settings': cybox_common.InternationalizationSettingsType,
    'Image_Offset': cybox_common.IntegerObjectPropertyType,
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
    'Contributors': cybox_common.PersonnelType,
    'Tool_Configuration': cybox_common.ToolConfigurationType,
    'Imports': cybox_common.ImportsType,
    'Library': cybox_common.LibraryType,
    'References': cybox_common.ToolReferencesType,
    'Internal_Strings': cybox_common.InternalStringsType,
    'Custom_Properties': cybox_common.CustomPropertiesType,
    'Configuration_Setting': cybox_common.ConfigurationSettingType,
    'Libraries': cybox_common.LibrariesType,
    'Function': cybox_common.StringObjectPropertyType,
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
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
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
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
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
        rootTag = 'Memory_Region'
        rootClass = MemoryObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Memory_Region",
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
    "MemoryObjectType"
    ]
