# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys

from mixbox.binding_utils import *
from . import cybox_common


class AddressObjectType(cybox_common.ObjectPropertiesType):
    """The AddressObjectType is intended to characterize cyber
    addresses.The category field specifies the address category that
    is being defined. The is_source field specifies if this is a
    "Source" addressThe is_destination field specifies if this is a
    "Destination" address"""

    subclass = None
    superclass = cybox_common.ObjectPropertiesType
    def __init__(self, object_reference=None, Custom_Properties=None, xsi_type=None, category='ipv4-addr', is_source=None, is_destination=None, is_spoofed=None, Address_Value=None, VLAN_Name=None, VLAN_Num=None):
        super(AddressObjectType, self).__init__(object_reference, Custom_Properties, xsi_type )
        self.category = _cast(None, category)
        self.is_source = _cast(bool, is_source)
        self.is_destination = _cast(bool, is_destination)
        self.is_spoofed = _cast(bool, is_spoofed)
        self.Address_Value = Address_Value
        self.VLAN_Name = VLAN_Name
        self.VLAN_Num = VLAN_Num
    def factory(*args_, **kwargs_):
        if AddressObjectType.subclass:
            return AddressObjectType.subclass(*args_, **kwargs_)
        else:
            return AddressObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Address_Value(self): return self.Address_Value
    def set_Address_Value(self, Address_Value): self.Address_Value = Address_Value
    def validate_StringObjectPropertyType(self, value):
        # Validate type cybox_common.StringObjectPropertyType, a restriction on None.
        pass
    def get_VLAN_Name(self): return self.VLAN_Name
    def set_VLAN_Name(self, VLAN_Name): self.VLAN_Name = VLAN_Name
    def get_VLAN_Num(self): return self.VLAN_Num
    def set_VLAN_Num(self, VLAN_Num): self.VLAN_Num = VLAN_Num
    def validate_IntegerObjectPropertyType(self, value):
        # Validate type cybox_common.IntegerObjectPropertyType, a restriction on None.
        pass
    def get_category(self): return self.category
    def set_category(self, category): self.category = category
    def get_is_source(self): return self.is_source
    def set_is_source(self, is_source): self.is_source = is_source
    def get_is_destination(self): return self.is_destination
    def set_is_destination(self, is_destination): self.is_destination = is_destination
    def get_is_spoofed(self): return self.spoofed
    def set_is_spoofed(self, is_spoofed): self.is_spoofed = is_spoofed
    def hasContent_(self):
        if (
            self.Address_Value is not None or
            self.VLAN_Name is not None or
            self.VLAN_Num is not None or
            super(AddressObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, namespace_='AddressObj:', name_='AddressObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AddressObjectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AddressObj:', name_='AddressObjectType'):
        super(AddressObjectType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AddressObjectType')
        if self.category is not None:

            lwrite(' category=%s' % (quote_attrib(self.category), ))
        if self.is_source is not None:

            lwrite(' is_source="%s"' % self.gds_format_boolean(self.is_source, input_name='is_source'))
        if self.is_destination is not None:

            lwrite(' is_destination="%s"' % self.gds_format_boolean(self.is_destination, input_name='is_destination'))
        if self.is_spoofed is not None:

            lwrite(' is_spoofed="%s"' % self.gds_format_boolean(self.is_spoofed, input_name='is_spoofed'))
    def exportChildren(self, lwrite, level, namespace_='AddressObj:', name_='AddressObjectType', fromsubclass_=False, pretty_print=True):
        super(AddressObjectType, self).exportChildren(lwrite, level, 'AddressObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Address_Value is not None:
            self.Address_Value.export(lwrite, level, 'AddressObj:', name_='Address_Value', pretty_print=pretty_print)
        if self.VLAN_Name is not None:
            self.VLAN_Name.export(lwrite, level, 'AddressObj:', name_='VLAN_Name', pretty_print=pretty_print)
        if self.VLAN_Num is not None:
            self.VLAN_Num.export(lwrite, level, 'AddressObj:', name_='VLAN_Num', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('category', node)
        if value is not None:
            self.category = value
        value = find_attr_value_('is_source', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_source = True
            elif value in ('false', '0'):
                self.is_source = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_destination', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_destination = True
            elif value in ('false', '0'):
                self.is_destination = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('is_spoofed', node)
        if value is not None:

            if value in ('true', '1'):
                self.is_spoofed = True
            elif value in ('false', '0'):
                self.is_spoofed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(AddressObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Address_Value':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_Address_Value(obj_)
        elif nodeName_ == 'VLAN_Name':
            obj_ = cybox_common.StringObjectPropertyType.factory()
            obj_.build(child_)
            self.set_VLAN_Name(obj_)
        elif nodeName_ == 'VLAN_Num':
            obj_ = cybox_common.IntegerObjectPropertyType.factory()
            obj_.build(child_)
            self.set_VLAN_Num(obj_)
        super(AddressObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class AddressObjectType

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
    'Identifier': cybox_common.PlatformIdentifierType,
    'Strings': cybox_common.ExtractedStringsType,
    'File_System_Offset': cybox_common.IntegerObjectPropertyType,
    'Reference_Description': cybox_common.StructuredTextType,
    'Code_Snippet': cybox_common.ObjectPropertiesType,
    'Configuration_Settings': cybox_common.ConfigurationSettingsType,
    'Simple_Hash_Value': cybox_common.SimpleHashValueType,
    'Byte_String_Value': cybox_common.HexBinaryObjectPropertyType,
    'Instance': cybox_common.ObjectPropertiesType,
    'Import': cybox_common.StringObjectPropertyType,
    'Property': cybox_common.PropertyType,
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
    'VLAN_Name': cybox_common.StringObjectPropertyType,
    'Address': cybox_common.HexBinaryObjectPropertyType,
    'Search_Within': cybox_common.IntegerObjectPropertyType,
    'Segment': cybox_common.HashSegmentType,
    'Compiler': cybox_common.CompilerType,
    'Name': cybox_common.StringObjectPropertyType,
    'Address_Value': cybox_common.StringObjectPropertyType,
    'VLAN_Num': cybox_common.IntegerObjectPropertyType,
    'Signature_Description': cybox_common.StringObjectPropertyType,
    'Block_Size': cybox_common.IntegerObjectPropertyType,
    'Search_Distance': cybox_common.IntegerObjectPropertyType,
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
        rootTag = 'Address'
        rootClass = AddressObjectType
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
        rootTag = 'Address'
        rootClass = AddressObjectType
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
        rootTag = 'Address'
        rootClass = AddressObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#    sys.stdout.write('<?xml version="1.0" ?>\n')
#    rootObj.export(sys.stdout.write, 0, name_="Address",
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
    "AddressObjectType"
    ]
